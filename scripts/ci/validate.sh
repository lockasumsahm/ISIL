#!/usr/bin/env bash
set -Eeuo pipefail

echo "=== ISIL LOCAL QUALITY GATE ==="

uv sync --locked
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest -q
uv run pip-audit
uv export --format cyclonedx1.5 --output-file sbom.cdx.json

echo
echo "✅ LOCAL QUALITY GATE PASSED"
