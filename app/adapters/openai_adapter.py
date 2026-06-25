import json

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

from app.adapters.base import AdapterResult, BaseAdapter
from app.config import get_settings

CONTEXT_PROMPT = """Analyze this user content for safety signals. Return ONLY valid JSON:
{
  "scam": 0-100,
  "ai_generated": 0-100,
  "spam": 0-100,
  "threat": 0-100,
  "intent": "joke|sarcasm|threat|solicitation|neutral",
  "sarcasm_likelihood": 0.0-1.0,
  "threat_probability": 0.0-1.0,
  "summary": "one sentence"
}
Content: """


class OpenAIAdapter(BaseAdapter):
    name = "openai"

    def __init__(self) -> None:
        settings = get_settings()
        self.api_key = settings.openai_api_key
        self.model = settings.openai_model

    @retry(stop=stop_after_attempt(2), wait=wait_exponential(multiplier=0.5, max=4))
    async def analyze(self, text: str, locale: str = "en-US") -> AdapterResult:
        if not self.api_key:
            return AdapterResult(source=self.name, scores={}, error="no_api_key")

        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are a content safety analyst. Respond with JSON only.",
                        },
                        {"role": "user", "content": CONTEXT_PROMPT + text[:8000]},
                    ],
                    "temperature": 0.1,
                    "response_format": {"type": "json_object"},
                },
            )
            resp.raise_for_status()
            data = resp.json()

        content = data["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        scores = {
            "scam": float(parsed.get("scam", 0)),
            "ai_generated": float(parsed.get("ai_generated", 0)),
            "spam": float(parsed.get("spam", 0)),
            "threat": float(parsed.get("threat", 0)),
        }
        return AdapterResult(
            source=self.name,
            scores=scores,
            raw={
                "intent": parsed.get("intent", "neutral"),
                "sarcasm_likelihood": float(parsed.get("sarcasm_likelihood", 0)),
                "threat_probability": float(parsed.get("threat_probability", 0)),
                "summary": parsed.get("summary", ""),
            },
        )
