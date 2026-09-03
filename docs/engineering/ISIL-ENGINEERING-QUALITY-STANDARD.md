# ISIL Engineering Quality Standard

## Hard Rules

1. No critical feature without automated tests.
2. No production change without CI validation.
3. No secret committed to the repository.
4. No critical endpoint without centralized authorization.
5. No cross-tenant access without an explicit authorization decision.
6. No destructive operation without policy enforcement.
7. No undocumented breaking API change.
8. No schema migration without rollback or recovery strategy.
9. No security claim without evidence.
10. No deployment without a traceable release identifier.
11. No dependency without a lockfile and vulnerability review.
12. No external data transmission without a defined trust boundary.
13. No agent capability without a documented privilege boundary.
14. No architecture decision without an ADR.
15. No requirement is considered implemented until executable verification exists.

## Definition of Done

A production change is complete only when:

- implementation exists,
- tests exist,
- security impact is reviewed,
- observability is sufficient,
- CI passes,
- documentation is updated,
- traceability is recorded,
- rollback/recovery behavior is understood.
