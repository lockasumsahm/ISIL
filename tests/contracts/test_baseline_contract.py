from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_project_has_canonical_engineering_contracts():
    assert (ROOT / "docs/ENGINEERING-QUALITY-STANDARD.md").is_file()
    assert (ROOT / "docs/CLAUDE-DEVELOPMENT-CONTRACT.md").is_file()
    assert (ROOT / "specs/TRACEABILITY.md").is_file()
