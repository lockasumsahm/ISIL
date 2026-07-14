from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.request import FeedbackRequest
from app.api.schemas.response import AnalyticsSummary
from app.db.models import FeedbackRecord, SafetyDecision


async def record_feedback(session: AsyncSession, body: FeedbackRequest) -> None:
    row = FeedbackRecord(
        trace_id=body.trace_id,
        human_decision=body.human_decision,
        correct=body.correct,
        notes=body.notes,
    )
    session.add(row)
    await session.flush()


async def get_analytics(
    session: AsyncSession,
    tenant_id: str | None = None,
    limit: int = 1000,
) -> AnalyticsSummary:
    q = select(SafetyDecision).order_by(SafetyDecision.created_at.desc()).limit(limit)
    if tenant_id:
        q = q.where(SafetyDecision.tenant_id == tenant_id)

    result = await session.execute(q)
    rows = result.scalars().all()

    if not rows:
        return AnalyticsSummary(
            total_checks=0,
            decisions={},
            avg_risk_score=0.0,
            top_signals=[],
        )

    decisions: dict[str, int] = {}
    total_score = 0.0
    for r in rows:
        decisions[r.decision] = decisions.get(r.decision, 0) + 1
        total_score += r.final_risk_score

    fb_q = select(func.count(FeedbackRecord.id))
    fb_result = await session.execute(fb_q)
    feedback_count = fb_result.scalar() or 0

    return AnalyticsSummary(
        total_checks=len(rows),
        decisions=decisions,
        avg_risk_score=round(total_score / len(rows), 2),
        top_signals=[{"feedback_records": feedback_count}],
    )
