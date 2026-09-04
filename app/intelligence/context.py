from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ContextAnalysis:
    """
    Contextual modifiers applied by the fusion engine.

    All modifier values are score deltas, not replacement scores.

    Attributes:
        sarcasm_likelihood:
            Probability-like estimate in the range [0.0, 1.0].
            Currently informational; retained as part of the public contract.

        toxicity_modifier:
            Additive modifier applied to the toxicity score.

        threat_modifier:
            Additive modifier applied to the threat score.
    """

    sarcasm_likelihood: float = 0.0
    toxicity_modifier: float = 0.0
    threat_modifier: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.sarcasm_likelihood <= 1.0:
            raise ValueError(
                "sarcasm_likelihood must be between 0.0 and 1.0"
            )
