# ADR-005 — Tenant Isolation

Status: Proposed

Tenant identity must be explicit at the authorization boundary.

Canonical hierarchy:

User
  -> Organization
    -> Workspace
      -> Project
        -> Resource

Authorization must be centralized rather than scattered across handlers.
