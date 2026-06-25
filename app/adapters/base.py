from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AdapterResult:
    source: str
    scores: dict[str, float]  # 0-100 per label
    raw: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None


class BaseAdapter(ABC):
    name: str = "base"

    @abstractmethod
    async def analyze(self, text: str, locale: str = "en-US") -> AdapterResult:
        pass

    @staticmethod
    def to_percent(score: float, scale: str = "unit") -> float:
        """Normalize score to 0-100."""
        if scale == "unit":
            return min(100.0, max(0.0, score * 100))
        return min(100.0, max(0.0, score))
