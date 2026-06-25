from typing import Any

from pydantic import BaseModel, Field


class SignalDetail(BaseModel):
    source: str
    label: str
    score: float
    raw: dict[str, Any] | None = None
    modifier: float | None = None


class Explanation(BaseModel):
    summary: str
    signals: list[SignalDetail]
    jurisdiction_notes: list[str] = Field(default_factory=list)
    context_notes: list[str] = Field(default_factory=list)
    memory_notes: list[str] = Field(default_factory=list)


class RiskBreakdown(BaseModel):
    toxicity: float = 0
    scam: float = 0
    cyberbullying: float = 0
    hate: float = 0
    ai_generated: float = 0
    spam: float = 0
    threat: float = 0


class SafetyCheckResponse(BaseModel):
    decision: str
    action: str
    final_risk_score: float
    confidence: float
    risk_breakdown: RiskBreakdown
    explanation: Explanation
    trace_id: str
    policy_pack_id: str
    latency_ms: float


class HealthResponse(BaseModel):
    status: str
    version: str
    adapters: dict[str, str]


class AnalyticsSummary(BaseModel):
    total_checks: int
    decisions: dict[str, int]
    avg_risk_score: float
    top_signals: list[dict[str, Any]]


class ApiKeyResponse(BaseModel):
    api_key: str
    name: str
    created: bool
