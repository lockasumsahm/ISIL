# ADR-001 — Modular Monolith

## Status
Accepted

## Decision
ISIL will begin as a modular monolith with explicit internal boundaries rather than premature microservices.

## Rationale
The current product scope does not justify distributed-service complexity. Strong module boundaries provide a path to later service extraction without introducing unnecessary operational overhead.

## Consequences
- Clear module ownership is required.
- Cross-module dependencies must remain explicit.
- Service extraction remains possible later.
