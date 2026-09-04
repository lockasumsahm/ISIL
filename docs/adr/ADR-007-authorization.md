# ADR-007 — Centralized Authorization

Status: Proposed

Authorization decisions must be represented by a centralized policy interface.

The application must not rely on scattered comparisons such as user_id == owner_id as its security architecture.
