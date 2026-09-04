# ADR-002 — Python Dependency and Environment Management

## Status
Accepted

## Decision
ISIL uses `pyproject.toml` as the project metadata and dependency authority and `uv.lock` for reproducible dependency resolution.

## Consequences
- CI must validate the lockfile.
- Development environments should use the locked dependency graph.
- Ad-hoc dependency installation is not part of the normal workflow.
