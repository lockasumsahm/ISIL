import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from app.adapters.base import AdapterResult, BaseAdapter
from app.config import get_settings

HF_INFERENCE = "https://api-inference.huggingface.co/models"


class HuggingFaceAdapter(BaseAdapter):
    name = "huggingface"

    def __init__(self) -> None:
        settings = get_settings()
        self.token = settings.huggingface_api_token
        self.toxicity_model = settings.huggingface_toxicity_model

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=0.5, max=4))
    async def _infer(self, model: str, text: str) -> list[dict]:
        headers = {"Authorization": f"Bearer {self.token}"}
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                f"{HF_INFERENCE}/{model}",
                headers=headers,
                json={"inputs": text[:5000]},
            )
            if resp.status_code == 503:
                return []
            resp.raise_for_status()
            return resp.json()

    async def analyze(self, text: str, locale: str = "en-US") -> AdapterResult:
        if not self.token:
            return AdapterResult(source=self.name, scores={}, error="no_api_key")

        scores: dict[str, float] = {}
        raw: dict = {"models": []}

        try:
            result = await self._infer(self.toxicity_model, text)
            raw["toxicity_result"] = result
            if isinstance(result, list) and result:
                if isinstance(result[0], list):
                    for item in result[0]:
                        label = str(item.get("label", "")).lower()
                        score = float(item.get("score", 0))
                        if "toxic" in label or "hate" in label:
                            scores["toxicity"] = max(
                                scores.get("toxicity", 0),
                                self.to_percent(score),
                            )
                        if "hate" in label:
                            scores["hate"] = max(
                                scores.get("hate", 0),
                                self.to_percent(score),
                            )
                elif isinstance(result[0], dict):
                    scores["toxicity"] = self.to_percent(float(result[0].get("score", 0)))
        except Exception as e:
            return AdapterResult(source=self.name, scores=scores, raw=raw, error=str(e))

        scam_heuristic = 80.0 if any(
            w in text.lower() for w in ("wire transfer", "bitcoin", "verify account", "you won")
        ) else 0.0
        if scam_heuristic:
            scores["scam"] = scam_heuristic

        return AdapterResult(source=self.name, scores=scores, raw=raw)
