# ISIL Production Architecture Boundaries

Initial architecture should remain a modular monolith until
operational evidence justifies service extraction.

Target logical boundaries:

- API
- identity/authentication
- authorization
- tenancy
- intelligence
- model orchestration
- memory/context
- knowledge graph
- workflow
- persistence
- events/jobs
- audit/compliance
- observability
- security
- billing
- admin
- developer platform

These are logical modules, not a requirement for separate services.
