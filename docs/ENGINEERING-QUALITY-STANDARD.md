# ISIL Engineering Quality Standard

## Core Rules

1. No production feature without executable tests.
2. No merge to `main` without required CI checks.
3. No secrets committed to source control.
4. No security claim without machine-verifiable evidence.
5. No destructive operation without explicit authorization and policy enforcement.
6. No external data transmission without explicit policy approval.
7. No dependency change without lockfile and review.
8. No critical API without authentication and authorization design.
9. No database migration without rollback or recovery strategy.
10. No breaking API change without a versioning/compatibility decision.
11. No production deployment without release validation.
12. Every critical requirement must map to implementation and tests.

## Development Flow

Requirement
  -> Architecture
  -> Implementation Contract
  -> Code
  -> Unit Tests
  -> Integration Tests
  -> Security Tests
  -> CI
  -> Review
  -> Merge
  -> Release

## Agent Boundary

AI coding agents are implementation accelerators.

They do not receive unrestricted authority over:
- production deployment
- credentials
- destructive repository operations
- branch protection changes
- external data publication
- irreversible data operations

## Evidence Standard

"Implemented" means code exists.

"Verified" means automated tests passed.

"Secure" means controls were tested and evidence exists.

"Production ready" requires all applicable release, security,
observability, backup/recovery, and operational gates.
