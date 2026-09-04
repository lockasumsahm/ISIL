# ADR-001 — Modular Monolith

Status: Accepted

ISIL begins as a modular monolith with explicit internal boundaries.

Reason:
- smaller operational surface
- easier transactional consistency
- simpler local development
- clearer migration path to services later

Service extraction requires an evidence-based need such as scaling, security isolation, team ownership, or availability requirements.
