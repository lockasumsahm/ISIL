# ISIL Claude Engineering Contract

Claude is an engineering accelerator, not an unrestricted system administrator.

## Mandatory workflow

CANONICAL SPEC
    ↓
ARCHITECTURE
    ↓
TASK
    ↓
IMPLEMENTATION
    ↓
TEST
    ↓
SECURITY REVIEW
    ↓
DIFF REVIEW
    ↓
PULL REQUEST
    ↓
MERGE

## Rules

1. Never work directly on main.
2. Never overwrite unrelated user changes.
3. Never delete canonical files without explicit task authority.
4. Never expose or print secrets.
5. Never weaken security controls to make tests pass.
6. Never bypass failing CI without documenting why.
7. Every behavior change needs tests.
8. Every security-sensitive change needs security tests.
9. Every API change requires contract verification.
10. Every schema change requires migration verification.
11. Every external integration must have explicit scope.
12. Generated artifacts stay out of source control unless explicitly required.
13. Do not invent architecture that conflicts with canonical ADRs.
14. Existing architecture must be inspected before introducing a new subsystem.

## Completion standard

A task is incomplete until:

- implementation exists,
- tests exist,
- relevant checks pass,
- security impact is reviewed,
- the final diff is understood.
