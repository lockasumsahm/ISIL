# ISIL Test Architecture

Tests are organized by engineering responsibility.

- `unit/` — isolated module behavior.
- `integration/` — component boundaries and persistence.
- `api/` — request/response/API contracts.
- `security/` — authentication, authorization, isolation, abuse resistance.
- `database/` — schema, transaction, migration, and consistency behavior.
- `intelligence/` — inference, orchestration, context, memory, and model behavior.
- `adapters/` — provider and external integration contracts.
- `e2e/` — full user/system workflows.
- `contracts/` — executable architectural contracts.
- `performance/` — benchmark and latency controls.
- `load/` — concurrency and sustained-load behavior.
- `chaos/` — failure and recovery behavior.
- `fixtures/` — deterministic test data.

Do not add empty tests merely to increase test counts.

Every critical production behavior should eventually have an executable contract.
