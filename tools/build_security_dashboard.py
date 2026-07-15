from __future__ import annotations

import html
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

PROFILE_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = PROFILE_ROOT.parent
OUT = PROFILE_ROOT / "security-dashboard.html"
SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".pytest_cache",
    ".ruff_cache",
    "htmlcov",
    ".mypy_cache",
    ".pyright_cache",
    "data",
    "docs",
    "evidence_artifacts",
    "mlruns",
    "models",
}


@dataclass(frozen=True)
class RepoSpec:
    name: str
    topic: str
    controls: tuple[str, ...]
    run_command: str


REPOS = (
    RepoSpec(
        "poojakira",
        "Public GitHub profile and evidence dashboard",
        ("pytest", "github actions", "pages", "license", "security"),
        "python -m pytest tests -q -ra -W error",
    ),
    RepoSpec(
        "hf-model-provenance-scanner",
        "Hugging Face model supply-chain scanner",
        ("pickle", "safetensors", "sarif", "webhook", "baseline", "sandbox"),
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest tests -q -ra -W error",
    ),
    RepoSpec(
        "mcp-security-gateway-monitor",
        "MCP tool-call security monitor",
        ("prompt injection", "pii", "audit", "rate limit", "metrics", "docker"),
        "python -m pytest tests -q -ra",
    ),
    RepoSpec(
        "llm-redteam-framework",
        "Offline LLM red-team detector experiments",
        ("red team", "detector", "prompt injection", "pytest", "grouped"),
        "PYTHONPATH=src python -m pytest tests -q -ra",
    ),
    RepoSpec(
        "PulseNet-RUL-Forecasting",
        "NASA C-MAPSS RUL forecasting with security gates",
        ("audit", "rbac", "prometheus", "pip-audit", "bandit", "pyright"),
        "python -m pytest tests -q -ra -W error",
    ),
    RepoSpec(
        "dataset-poisoning-detector",
        "Dataset poisoning and anomaly detection",
        ("fastapi", "api key", "redis", "kafka", "prometheus", "pytest"),
        "python -m pytest tests -q -ra -W error",
    ),
    RepoSpec(
        "model-privacy-attacks",
        "Membership inference and privacy attack evaluation",
        ("membership inference", "privacy", "pytest", "metrics", "report"),
        "python -m pytest tests -q -ra",
    ),
    RepoSpec(
        "adversarial-ml-lab",
        "Adversarial ML attacks and defenses",
        ("fgsm", "pgd", "adversarial", "pytest", "robustness"),
        "python -m pytest tests -q -ra",
    ),
)


def main() -> None:
    cards = [repo_card(spec, repo_snapshot(spec)) for spec in REPOS]
    OUT.write_text(render_page(cards), encoding="utf-8")
    print(f"wrote {OUT}")


def repo_path(spec: RepoSpec) -> Path:
    if spec.name == "poojakira":
        return PROFILE_ROOT
    return WORKSPACE_ROOT / spec.name


def repo_snapshot(spec: RepoSpec) -> dict[str, object]:
    path = repo_path(spec)
    files = list(iter_repo_files(path)) if path.exists() else []
    text_index = read_repo_text(files)
    tests = [p for p in files if is_test_file(path, p)]
    workflows = [p for p in files if is_workflow_file(path, p)]
    licenses = [
        p
        for p in files
        if p.name.lower()
        in {"license", "license.md", "license.txt", "copying", "notice"}
    ]
    evidence = [
        control
        for control in spec.controls
        if normalize(control) in normalize(text_index)
    ]
    missing = [control for control in spec.controls if control not in evidence]
    return {
        "path": path,
        "exists": path.exists(),
        "files": files,
        "tests": tests,
        "workflows": workflows,
        "licenses": licenses,
        "evidence": evidence,
        "missing": missing,
        "git": git_status(path),
    }


def repo_card(spec: RepoSpec, snapshot: dict[str, object]) -> str:
    exists = bool(snapshot["exists"])
    files = snapshot["files"]
    tests = snapshot["tests"]
    workflows = snapshot["workflows"]
    licenses = snapshot["licenses"]
    evidence = snapshot["evidence"]
    missing = snapshot["missing"]
    git = str(snapshot["git"])
    risk = (
        "ready"
        if exists and licenses and workflows and not missing and git == "clean"
        else "attention"
    )
    open_checks = []
    if not exists:
        open_checks.append("repo clone unavailable in this workspace")
    if not licenses:
        open_checks.append("license file not detected")
    open_checks.extend(str(item) for item in missing)
    if git != "clean":
        open_checks.append(f"git state: {git}")
    return f"""
    <article class="card {risk}">
      <div class="card-head">
        <h2><a href="https://github.com/poojakira/{html.escape(spec.name)}">{html.escape(spec.name)}</a></h2>
        <span>{html.escape(spec.topic)}</span>
      </div>
      <dl>
        <div><dt>Files</dt><dd>{len(files)}</dd></div>
        <div><dt>Tests</dt><dd>{len(tests)}</dd></div>
        <div><dt>Workflows</dt><dd>{len(workflows)}</dd></div>
        <div><dt>License</dt><dd>{"yes" if licenses else "no"}</dd></div>
      </dl>
      <p><strong>Evidence terms found:</strong> {html.escape(", ".join(evidence) if evidence else "none from configured map")}</p>
      <p><strong>Open checks:</strong> {html.escape(", ".join(open_checks) if open_checks else "none from configured map")}</p>
      <p><strong>User run command:</strong> <code>{html.escape(spec.run_command)}</code></p>
    </article>
    """


def relative_parts(root: Path, candidate: Path) -> tuple[str, ...]:
    try:
        return candidate.relative_to(root).parts
    except ValueError:
        return candidate.parts


def is_test_file(root: Path, candidate: Path) -> bool:
    parts = relative_parts(root, candidate)
    return (
        len(parts) >= 2
        and parts[0] == "tests"
        and candidate.suffix == ".py"
        and (candidate.name.startswith("test_") or candidate.name.endswith("_test.py"))
    )


def is_workflow_file(root: Path, candidate: Path) -> bool:
    parts = relative_parts(root, candidate)
    return (
        len(parts) == 3
        and parts[0] == ".github"
        and parts[1] == "workflows"
        and candidate.suffix.lower() in {".yml", ".yaml"}
    )


def iter_repo_files(path: Path):
    for root, dirs, files in os.walk(path):
        dirs[:] = [directory for directory in dirs if directory not in SKIP_DIRS]
        current = Path(root)
        for filename in files:
            candidate = current / filename
            if any(part in SKIP_DIRS for part in candidate.parts):
                continue
            yield candidate


def read_repo_text(files: list[Path]) -> str:
    chunks: list[str] = []
    for candidate in files:
        if candidate.suffix.lower() not in {
            ".py",
            ".md",
            ".yml",
            ".yaml",
            ".json",
            ".toml",
            ".sh",
        }:
            continue
        try:
            chunks.append(candidate.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
    return "\n".join(chunks)


def normalize(value: str) -> str:
    return value.lower().replace("-", " ").replace("_", " ")


def git_status(path: Path) -> str:
    if not path.exists():
        return "missing"
    if not (path / ".git").exists():
        return "not-a-git-repo"
    result = subprocess.run(
        ["git", "status", "--short", "--untracked-files=no"],
        cwd=path,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return "git-error"
    return "clean" if not result.stdout.strip() else "dirty"


def render_page(cards: list[str]) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ML Security Portfolio Evidence Dashboard</title>
  <style>
    body {{ margin: 0; font-family: Inter, Arial, sans-serif; background: #f6f7f9; color: #15202b; }}
    header {{ padding: 40px 28px 20px; max-width: 1180px; margin: auto; }}
    h1 {{ margin: 0 0 10px; font-size: 34px; letter-spacing: 0; }}
    a {{ color: #1d4ed8; text-decoration: none; }}
    .sub {{ max-width: 920px; color: #4d5b6a; line-height: 1.5; }}
    main {{ max-width: 1180px; margin: 0 auto 48px; padding: 0 28px; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; }}
    .card {{ background: white; border: 1px solid #d9dee5; border-radius: 8px; padding: 18px; box-shadow: 0 1px 2px rgba(15, 23, 42, .04); }}
    .card.attention {{ border-left: 4px solid #b45309; }}
    .card.ready {{ border-left: 4px solid #047857; }}
    .card-head {{ display: flex; gap: 10px; align-items: flex-start; justify-content: space-between; }}
    h2 {{ margin: 0; font-size: 17px; line-height: 1.25; }}
    .card-head span {{ color: #526172; font-size: 12px; text-align: right; max-width: 150px; }}
    dl {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 14px 0; }}
    dt {{ color: #657386; font-size: 11px; }}
    dd {{ margin: 2px 0 0; font-weight: 700; font-size: 15px; }}
    p {{ font-size: 13px; line-height: 1.45; }}
    code {{ background: #eef2f7; border: 1px solid #d8e0ea; border-radius: 4px; padding: 2px 5px; white-space: normal; }}
    footer {{ max-width: 1180px; margin: 0 auto 36px; padding: 0 28px; color: #5f6f80; font-size: 12px; }}
  </style>
</head>
<body>
  <header>
    <h1>ML Security Portfolio Evidence Dashboard</h1>
    <p class="sub">Generated from checked-out repository files. This dashboard reports only observable files, tests, workflows, licenses, git state, and configured evidence terms. It is an index, not a benchmark certification or production-readiness claim.</p>
  </header>
  <main>
    {''.join(cards)}
  </main>
  <footer>
    Rebuild with <code>python tools/build_security_dashboard.py</code>. Verify each project with its own README/RUNBOOK and CI logs before citing results.
  </footer>
</body>
</html>
"""


if __name__ == "__main__":
    main()
