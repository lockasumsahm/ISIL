# ISIL Test Architecture

## Required layers

- unit/
- integration/
- api/
- security/
- database/
- intelligence/
- adapters/
- contracts/
- e2e/
- fixtures/

## Principle

Every critical behavior requires an executable contract.

Priority domains:

- authentication
- authorization
- tenant isolation
- input validation
- persistence
- transactions
- provider failures
- timeouts
- retry behavior
- rate limiting
- audit events
- prompt injection
- tool injection
- secret handling
- data deletion
- backup/restore
