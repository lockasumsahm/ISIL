import json
from dataclasses import dataclass, field
from pathlib import Path

from app.intelligence.context import ContextAnalysis
from app.intelligence.jurisdiction import PolicyPack


@dataclass
class FusionResult:
    final_score: float
    breakdown: dict[str, float]
    confidence: float
    weighted_contributions: dict[str, float] = field(default_factory=dict)


class FusionEngine:
    LABELS = [
        "toxicity",
        "scam",
        "cyberbullying",
        "hate",
        "ai_generated",
        "spam",
        "threat",
    ]

    def __init__(self, fusion_path: Path, thresholds_path: Path) -> None:
        with open(fusion_path) as f:
            self.config = json.load(f)
        with open(thresholds_path) as f:
            self.thresholds = json.load(f)

    def aggregate_signals(
        self,
        all_scores: dict[str, float],
        jurisdiction: str,
        context: ContextAnalysis | None = None,
        memory_modifier: float = 0.0,
    ) -> FusionResult:
        weights = self.config.get("default", {})
        mults = self.config.get("jurisdiction_multipliers", {}).get(
            jurisdiction,
            self.config.get("jurisdiction_multipliers", {}).get("GLOBAL", {}),
        )

        breakdown: dict[str, float] = {k: 0.0 for k in self.LABELS}
        contributions: dict[str, float] = {}

        for label in self.LABELS:
            raw = all_scores.get(label, 0.0)
            breakdown[label] = raw

        if context:
            if context.toxicity_modifier:
                breakdown["toxicity"] = max(
                    0,
                    breakdown["toxicity"] + context.toxicity_modifier,
                )
            if context.threat_modifier:
                breakdown["threat"] = min(
                    100,
                    breakdown["threat"] + context.threat_modifier,
                )

        total_weight = 0.0
        weighted_sum = 0.0
        active_signals = 0

        for label in self.LABELS:
            w = weights.get(label, 0.0)
            if w <= 0:
                continue
            mult = mults.get(label, 1.0)
            score = breakdown[label] * mult
            if score > 0:
                active_signals += 1
            weighted_sum += score * w
            total_weight += w
            contributions[label] = score * w

        if total_weight == 0:
            final = 0.0
        else:
            final = weighted_sum / total_weight

        final = min(100.0, max(0.0, final + memory_modifier))

        confidence = min(
            0.99,
            0.5 + (active_signals * 0.08) + (0.1 if final > 60 or final < 20 else 0),
        )

        return FusionResult(
            final_score=round(final, 2),
            breakdown={k: round(v, 2) for k, v in breakdown.items()},
            confidence=round(confidence, 3),
            weighted_contributions=contributions,
        )

    def decide(
        self,
        final_score: float,
        jurisdiction: str,
        forced: str | None = None,
    ) -> tuple[str, str]:
        if forced:
            action = forced
            if forced == "block":
                return "block", action
            if forced == "review":
                return "review", action
            return forced, action

        thresholds = self.thresholds.get(
            jurisdiction,
            self.thresholds.get("default", self.thresholds.get("GLOBAL", {})),
        )
        block = thresholds.get("block", 85)
        review = thresholds.get("review", 70)
        warn = thresholds.get("warn", 50)

        if final_score >= block:
            return "block", "block"
        if final_score >= review:
            return "review", "review"
        if final_score >= warn:
            return "warn", "warn"
        return "allow", "allow"

    def update_thresholds(self, jurisdiction: str, updates: dict[str, int]) -> None:
        if jurisdiction not in self.thresholds:
            self.thresholds[jurisdiction] = dict(self.thresholds.get("default", {}))
        for k, v in updates.items():
            if v is not None:
                self.thresholds[jurisdiction][k] = v
        with open(
            Path(self.config.get("_thresholds_path", "config/thresholds.json")),
            "w",
        ) as f:
            json.dump(self.thresholds, f, indent=2)
