import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_public_profile_contains_selected_repos_and_contact_links():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for repo in [
        "hf-model-provenance-scanner",
        "mcp-security-gateway-monitor",
        "llm-redteam-framework",
        "PulseNet-RUL-Forecasting",
        "dataset-poisoning-detector",
        "model-privacy-attacks",
        "adversarial-ml-lab",
    ]:
        assert f"https://github.com/poojakira/{repo}" in readme
    assert "https://github.com/poojakira" in readme
    assert "https://linkedin.com/in/poojakiran" in readme


def test_dashboard_builder_outputs_conservative_public_page():
    from tools import build_security_dashboard

    build_security_dashboard.main()
    dashboard = (ROOT / "security-dashboard.html").read_text(encoding="utf-8")
    assert "benchmark certification" in dashboard
    assert "Generated from checked-out repository files" in dashboard
    for forbidden in ("El" + "ite", "Verified 2026" + " security controls"):
        assert forbidden not in dashboard
    for repo in ["poojakira", "hf-model-provenance-scanner", "dataset-poisoning-detector"]:
        assert repo in dashboard


def test_profile_provenance_has_real_sha256_digests():
    from tools import write_profile_provenance

    write_profile_provenance.main()
    provenance = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
    assert provenance["subject"]
    for subject in provenance["subject"]:
        digest = subject["digest"]["sha256"]
        assert len(digest) == 64
        assert set(digest) <= set("0123456789abcdef")
        assert digest != "..."