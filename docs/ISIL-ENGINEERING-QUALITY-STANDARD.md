# ISIL Engineering Quality Standard

Status: Canonical Engineering Policy
Authority: ISIL Engineering
Version: 1.0

## Non-negotiable controls

1. No critical feature without executable tests.
2. No direct production change without CI verification.
3. No secret committed to source control.
4. No privileged endpoint without centralized authorization.
5. No tenant-scoped resource without tenant-bound authorization.
6. No destructive operation without explicit policy enforcement.
7. No breaking API change without contract/version review.
8. No database migration without forward and rollback validation where rollback is technically applicable.
9. No dependency change without lockfile update.
10. No production artifact without reproducible build metadata.
11. No security claim without executable evidence.
12. No external data transmission without an identified destination and policy approval.
13. No agent/tool execution based solely on untrusted external content.
14. No merge to protected production branches without required checks.
15. Every major requirement must map to architecture, implementation, tests, and security controls.

## Required evidence

Each production capability should provide:

- implementation location
- automated tests
- security controls
- observability signals
- operational runbook
- rollback or recovery procedure
- traceability identifier

## Architecture rule

Prefer a modular monolith until scale or isolation requirements justify service separation.

Do not introduce microservices merely to make diagrams look mature.
