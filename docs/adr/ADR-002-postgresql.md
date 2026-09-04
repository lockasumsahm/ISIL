# ADR-002 — Primary Relational Data Store

Status: Proposed

PostgreSQL is the candidate primary transactional data store.

Decision criteria:
- ACID transactions
- tenant isolation
- mature indexing
- JSON support
- operational tooling
- backup and recovery maturity

Implementation must follow an actual deployment decision and migration plan.
