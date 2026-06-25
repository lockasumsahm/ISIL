import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from app.adapters.base import AdapterResult, BaseAdapter
from app.config import get_settings

PERSPECTIVE_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"


class PerspectiveAdapter(BaseAdapter):
    name = "perspective"

    ATTRIBUTES = [
        "TOXICITY",
        "SEVERE_TOXICITY",
        "IDENTITY_ATTACK",
        "INSULT",
        "THREAT",
        "PROFANITY",
    ]

    def __init__(self) -> None:
        self.api_key = get_settings().perspective_api_key

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=0.5, max=4))
    async def analyze(self, text: str, locale: str = "en-US") -> AdapterResult:
        if not self.api_key:
            return AdapterResult(source=self.name, scores={}, error="no_api_key")

        payload = {
            "comment": {"text": text},
            "languages": [locale.split("-")[0] if locale else "en"],
            "requestedAttributes": {attr: {} for attr in self.ATTRIBUTES},
        }
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(
                PERSPECTIVE_URL,
                params={"key": self.api_key},
                json=payload,
            )
            resp.raise_for_status()
            data = resp.json()

        scores: dict[str, float] = {}
        attrs = data.get("attributeScores", {})
        mapping = {
            "TOXICITY": "toxicity",
            "SEVERE_TOXICITY": "toxicity",
            "IDENTITY_ATTACK": "hate",
            "INSULT": "cyberbullying",
            "THREAT": "threat",
            "PROFANITY": "toxicity",
        }
        for attr, key in mapping.items():
            if attr in attrs:
                val = attrs[attr]["summaryScore"]["value"]
                pct = self.to_percent(val)
                scores[key] = max(scores.get(key, 0), pct)

        return AdapterResult(source=self.name, scores=scores, raw=data)
