# ADR-008 — Observability

Status: Proposed

Production requests should carry correlation identifiers sufficient to relate:

request
trace
organization
workspace
project
workflow
model request

The implementation should emit structured logs, metrics, traces, errors, audit events, and AI cost/latency measurements.
