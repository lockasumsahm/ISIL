from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_engineering_contract_exists() -> None:
    assert (ROOT / "docs/ISIL-ENGINEERING-QUALITY-STANDARD.md").exists()


def test_traceability_exists() -> None:
    assert (ROOT / "docs/traceability/TRACEABILITY-MATRIX.md").exists()


def test_security_catalog_exists() -> None:
    assert (ROOT / "docs/security/SECURITY-CONTROL-CATALOG.md").exists()


def test_claude_contract_exists() -> None:
    assert (ROOT / "docs/CLAUDE-DEVELOPMENT-CONTRACT.md").exists()
