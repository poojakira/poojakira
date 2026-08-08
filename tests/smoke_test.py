import json
import subprocess
import sys
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
    assert "aws-agent-identity-guard" in readme
    assert "production-grade" not in readme.lower()
    assert "https://github.com/poojakira" in readme
    assert "https://linkedin.com/in/poojakiran" in readme


def test_claim_registry_schema_is_conservative():
    from tools.validate_claims import load_registry, validate_registry

    registry = load_registry(ROOT / "claims" / "registry.json")
    validate_registry(registry, max_age_days=3650)
    for claim in registry["claims"]:
        searchable = json.dumps(claim).lower()
        assert "maturity score" not in searchable
        assert "security score" not in searchable
        assert "production-grade" not in searchable
        assert "att&ck coverage" not in searchable
        assert len(claim["source_commit"]) == 40


def test_dashboard_builder_is_deterministic_and_tempfile_only(tmp_path):
    from tools import build_security_dashboard

    first = tmp_path / "dashboard-1.html"
    second = tmp_path / "dashboard-2.html"
    build_security_dashboard.main(["--output", first.as_posix(), "--max-age-days", "3650"])
    build_security_dashboard.main(["--output", second.as_posix(), "--max-age-days", "3650"])

    assert first.read_text(encoding="utf-8") == second.read_text(encoding="utf-8")
    dashboard = first.read_text(encoding="utf-8")
    assert "Evidence-Based Engineering Portfolio" in dashboard
    assert "Documentation keywords" in dashboard
    assert "maturity" not in dashboard.lower()
    assert "security score" not in dashboard.lower()
    assert "production-grade" not in dashboard.lower()


def test_profile_manifest_has_real_sha256_digests_and_no_slsa_claim(tmp_path):
    from tools import write_profile_provenance

    out = tmp_path / "manifest.json"
    write_profile_provenance.main(["--output", out.as_posix()])
    manifest = json.loads(out.read_text(encoding="utf-8"))

    assert manifest["kind"] == "unsigned-profile-evidence-manifest"
    manifest_text = json.dumps(manifest).lower()
    assert "slsa.dev" not in manifest_text
    assert "predicatetype" not in manifest_text
    assert manifest["subject"]
    for subject in manifest["subject"]:
        digest = subject["digest"]["sha256"]
        assert len(digest) == 64
        assert set(digest) <= set("0123456789abcdef")


def test_pytest_entrypoints_work_from_repo_root():
    import os

    env = dict(os.environ)
    path_key = next((key for key in env if key.upper() == "PATH"), "PATH")
    env[path_key] = str(ROOT) + os.pathsep + env.get(path_key, "")
    direct = subprocess.run(
        "pytest tests/entrypoint_probe.py -q",
        cwd=ROOT,
        env=env,
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    )
    module = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/entrypoint_probe.py", "-q"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert direct.returncode == 0, direct.stdout + direct.stderr
    assert module.returncode == 0, module.stdout + module.stderr


def test_tests_do_not_dirty_tracked_artifacts(tmp_path):
    from tools import build_security_dashboard, write_profile_provenance

    before = subprocess.run(
        ["git", "status", "--short"], cwd=ROOT, capture_output=True, text=True, check=False
    ).stdout
    build_security_dashboard.main(["--output", (tmp_path / "dash.html").as_posix(), "--max-age-days", "3650"])
    write_profile_provenance.main(["--output", (tmp_path / "manifest.json").as_posix()])
    after = subprocess.run(
        ["git", "status", "--short"], cwd=ROOT, capture_output=True, text=True, check=False
    ).stdout
    assert after == before
