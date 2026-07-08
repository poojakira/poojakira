from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_profile_readme_is_current_and_conservative():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "All 10 repos are public and runnable" not in readme
    assert "Elite" not in readme
    assert "world-class" not in readme.lower()
    assert "Verified 2026 security controls" not in readme


def test_legacy_evidence_is_not_marked_verified_pass():
    evidence_dir = ROOT / "evidence_artifacts"
    if not evidence_dir.exists():
        return

    for artifact in evidence_dir.glob("*_sarif.json"):
        text = artifact.read_text(encoding="utf-8")
        assert "Verified 2026 security controls" not in text, artifact.name
        assert '"level": "pass"' not in text, artifact.name
