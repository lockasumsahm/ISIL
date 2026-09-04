# ISIL Claude Development Contract

Claude must work in the following order:

1. Read canonical architecture and task requirements.
2. Inspect the existing implementation.
3. Identify the smallest safe change.
4. Implement the change.
5. Add or update tests.
6. Run formatting/lint/type/security checks.
7. Review the resulting diff.
8. Report limitations and failed checks.
9. Never bypass CI, branch protections, or security controls.
10. Never invent completed architecture that is not implemented.

Default working branch:

feature/<scope>/<short-description>

Never use `main` as an experimentation branch.

A task is complete only when implementation,
tests, verification, and evidence agree.
