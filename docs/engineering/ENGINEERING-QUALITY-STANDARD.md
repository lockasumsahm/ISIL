# ISIL Engineering Quality Standard

## Core Rules

1. No feature is complete without executable verification.
2. No production-bound change bypasses CI.
3. No secret belongs in source control.
4. No critical resource is accessible without an explicit authorization model.
5. No external data transmission occurs without an explicit boundary.
6. No destructive operation is hidden behind automation.
7. No breaking API change is introduced without a contract update.
8. No database migration is accepted without a recovery strategy.
9. No security claim is made without evidence.
10. No deployment is considered successful without health verification.
11. No dependency is introduced outside the declared project dependency system.
12. Generated local state must not pollute source control.
13. Architecture decisions must be recorded.
14. Requirements must trace to implementation and tests.
15. Agents are engineering accelerators, not unrestricted production authorities.

## Completion Standard

A feature is considered complete only when:

Requirement
→ design/architecture
→ implementation
→ automated tests
→ security verification
→ observability
→ documentation
→ CI validation
→ review
