import hashlib
import re
from typing import Any

from app.adapters.base import AdapterResult, BaseAdapter

# Heuristic patterns for demo/dev without API keys
SCAM_PATTERNS = [
    r"send\s+(money|btc|crypto|wire)",
    r"click\s+here",
    r"verify\s+your\s+account",
    r"you\s+won",
    r"free\s+iphone",
    r"investment\s+opportunity",
    r"urgent\s+transfer",
]
HATE_PATTERNS = [
    r"\b(kill|die)\s+all\b",
    r"genocide",
    r"inferior\s+race",
]
BULLY_PATTERNS = [
    r"nobody\s+likes\s+you",
    r"kill\s+yourself",
    r"kys\b",
    r"ugly\s+fat",
]
THREAT_PATTERNS = [
    r"i('ll|\s+will)\s+(kill|hurt|find)\s+you",
    r"watch\s+your\s+back",
    r"you're\s+dead",
]
SARCASM_MARKERS = ["/s", "yeah right", "totally", "sure jan", "lol jk"]


def _hash_score(text: str, salt: str, base: float = 0.0) -> float:
    h = int(hashlib.sha256(f"{salt}:{text}".encode()).hexdigest()[:8], 16)
    return min(100.0, base + (h % 30))


def _pattern_score(text: str, patterns: list[str]) -> float:
    lower = text.lower()
    hits = sum(1 for p in patterns if re.search(p, lower, re.I))
    if hits == 0:
        return 0.0
    return min(100.0, 40 + hits * 25)


class MockPerspectiveAdapter(BaseAdapter):
    name = "perspective"

    async def analyze(self, text: str, locale: str = "en-US") -> AdapterResult:
        toxicity = _pattern_score(text, THREAT_PATTERNS + BULLY_PATTERNS + HATE_PATTERNS)
        if not toxicity:
            toxicity = _hash_score(text, "tox", 5)
        insult = _pattern_score(text, BULLY_PATTERNS) * 0.8
        threat = _pattern_score(text, THREAT_PATTERNS)
        identity = _pattern_score(text, HATE_PATTERNS)
        return AdapterResult(
            source=self.name,
            scores={
                "toxicity": max(toxicity, insult * 0.5),
                "cyberbullying": max(insult, _pattern_score(text, BULLY_PATTERNS)),
                "hate": identity,
                "threat": threat,
            },
            raw={"mode": "mock", "locale": locale},
        )


class MockOpenAIAdapter(BaseAdapter):
    name = "openai"

    async def analyze(self, text: str, locale: str = "en-US") -> AdapterResult:
        lower = text.lower()
        scam = _pattern_score(text, SCAM_PATTERNS)
        ai_gen = 70.0 if "as an ai language model" in lower else _hash_score(text, "aigen", 8)
        spam = 60.0 if len(re.findall(r"http[s]?://", text)) >= 2 else _hash_score(text, "spam", 5)
        intent_threat = _pattern_score(text, THREAT_PATTERNS)
        sarcasm = 75.0 if any(m in lower for m in SARCASM_MARKERS) else 15.0
        return AdapterResult(
            source=self.name,
            scores={
                "scam": scam,
                "ai_generated": ai_gen,
                "spam": spam,
                "threat": intent_threat,
            },
            raw={
                "mode": "mock",
                "intent": "threat" if intent_threat > 50 else "neutral",
                "sarcasm_likelihood": sarcasm / 100,
            },
        )


class MockHuggingFaceAdapter(BaseAdapter):
    name = "huggingface"

    async def analyze(self, text: str, locale: str = "en-US") -> AdapterResult:
        return AdapterResult(
            source=self.name,
            scores={
                "toxicity": _hash_score(text, "hf_tox", 10),
                "scam": _pattern_score(text, SCAM_PATTERNS),
            },
            raw={"mode": "mock", "model": "heuristic"},
        )
