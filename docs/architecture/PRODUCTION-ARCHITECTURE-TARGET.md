# ISIL Production Architecture Target

Start as a modular monolith unless measured requirements justify decomposition.

Core boundaries:

API
IDENTITY
AUTHORIZATION
TENANCY
INTELLIGENCE
MODEL ORCHESTRATION
MEMORY / CONTEXT
KNOWLEDGE GRAPH
WORKFLOWS
DATA
EVENTS / QUEUES
AUDIT
OBSERVABILITY
SECURITY
BILLING
ADMIN
DEVELOPER PLATFORM

The boundaries are logical first and may share one deployable application initially.

No service split is justified solely for organizational aesthetics.
