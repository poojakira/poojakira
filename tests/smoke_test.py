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
    for repo in [
        "poojakira",
        "hf-model-provenance-scanner",
        "dataset-poisoning-detector",
    ]:
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


def test_dashboard_counts_only_real_test_and_workflow_files(tmp_path):
    from tools import build_security_dashboard

    repo = tmp_path / "repo"
    (repo / "tests").mkdir(parents=True)
    (repo / "docs").mkdir()
    (repo / ".github" / "workflows").mkdir(parents=True)
    real_test = repo / "tests" / "test_api.py"
    fake_test = repo / "docs" / "contest.md"
    real_workflow = repo / ".github" / "workflows" / "ci.yml"
    non_workflow_yaml = repo / ".github" / "dependabot.yml"
    for path in (real_test, fake_test, real_workflow, non_workflow_yaml):
        path.write_text("x", encoding="utf-8")

    assert build_security_dashboard.is_test_file(repo, real_test)
    assert not build_security_dashboard.is_test_file(repo, fake_test)
    assert build_security_dashboard.is_workflow_file(repo, real_workflow)
    assert not build_security_dashboard.is_workflow_file(repo, non_workflow_yaml)


def test_dashboard_ignores_own_generated_outputs_for_profile_dirty_state():
    from tools import build_security_dashboard

    generated_only = " M security-dashboard.html\n M provenance.json\n"
    source_change = " M README.md\n"

    assert (
        build_security_dashboard.effective_git_status_lines(
            build_security_dashboard.PROFILE_ROOT, generated_only
        )
        == []
    )
    assert build_security_dashboard.effective_git_status_lines(
        build_security_dashboard.PROFILE_ROOT, source_change
    ) == [" M README.md"]
