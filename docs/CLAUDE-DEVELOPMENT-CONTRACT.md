# ISIL — Claude Development Contract

Claude is an implementation accelerator, not an unrestricted architecture authority.

Required execution lifecycle:

CANONICAL SPEC
    ->
ARCHITECTURE
    ->
TASK
    ->
IMPLEMENTATION
    ->
TESTS
    ->
SECURITY REVIEW
    ->
DIFF REVIEW
    ->
CI
    ->
PULL REQUEST
    ->
HUMAN MERGE

Rules:

- Work on a feature branch, never directly on main.
- Inspect existing architecture before changing it.
- Prefer existing abstractions over duplication.
- Never invent unsupported requirements.
- Never silently weaken security controls.
- Never commit secrets.
- Never bypass failed tests.
- Never disable security checks merely to obtain a green build.
- Every behavior change needs tests.
- Every security-sensitive change needs security tests.
- Every database change needs migration validation.
- Every externally connected feature needs explicit data-flow documentation.
