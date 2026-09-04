from contextvars import ContextVar


request_id: ContextVar[str | None] = ContextVar("request_id", default=None)
trace_id: ContextVar[str | None] = ContextVar("trace_id", default=None)
organization_id: ContextVar[str | None] = ContextVar(
    "organization_id",
    default=None,
)
workflow_id: ContextVar[str | None] = ContextVar(
    "workflow_id",
    default=None,
)
model_request_id: ContextVar[str | None] = ContextVar(
    "model_request_id",
    default=None,
)
