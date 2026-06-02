"""Build an evidence-backed ML security portfolio dashboard.

The dashboard intentionally reports only local repository evidence: files,
tests, workflows, and source-control state. It does not invent benchmark
numbers or production-readiness claims.
"""

from __future__ import annotations

import html
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / "security-dashboard.html"
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
    "mlruns",
    "artifacts",
}


@dataclass(frozen=True)
class RepoSpec:
    name: str
    topic: str
    data_provenance: str
    standards: tuple[str, ...]
    expected_controls: tuple[str, ...]


REPOS = (
    RepoSpec(
        "Model-Supply-Chain-Auditor",
        "Model supply-chain security",
        "Security fixtures only; no company dataset required.",
        ("OWASP LLM05", "SLSA", "NIST AI RMF Map/Measure"),
        ("pickle scanner", "safetensors", "signing", "provenance", "policy", "sarif"),
    ),
    RepoSpec(
        "LLM-Guard-Scanner",
        "LLM application security",
        "Deterministic attack fixtures; no company dataset claimed.",
        ("OWASP LLM01", "OWASP LLM02", "MITRE ATLAS"),
        (
            "prompt injection",
            "rag poisoning",
            "output scanner",
            "canary",
            "normalization",
        ),
    ),
    RepoSpec(
        "Adversarial-Robustness-Toolkit",
        "Adversarial ML",
        "Attack implementation fixtures; no company dataset claimed.",
        ("MITRE ATLAS", "NIST AI RMF Measure"),
        ("fgsm", "pgd", "autoattack", "randomized smoothing", "robustness report"),
    ),
    RepoSpec(
        "ML-Privacy-Attacks",
        "Privacy attack evaluation",
        "Official UCI Bank Marketing loader; not company-financial data.",
        ("NIST AI RMF Govern/Measure", "Privacy threat modeling"),
        (
            "membership inference",
            "model inversion",
            "confidence sanitization",
            "privacy report",
        ),
    ),
    RepoSpec(
        "Secure-ML-platform",
        "Secure ML serving",
        "NASA C-MAPSS predictive-maintenance data path where available.",
        ("OWASP A03/A05", "NIST AI RMF Manage"),
        ("jwt", "tenant", "rate limit", "audit", "artifact integrity", "encryption"),
    ),
    RepoSpec(
        "PulseNet-RUL-Forecasting",
        "Predictive maintenance ML serving",
        "NASA C-MAPSS predictive-maintenance data path where available.",
        ("OWASP A03/A05", "NIST AI RMF Manage"),
        ("jwt", "rate limit", "audit", "artifact integrity", "prometheus"),
    ),
    RepoSpec(
        "RTX-OOM-Guard",
        "ML systems reliability",
        "Local telemetry/benchmark traces; not official company data.",
        ("Operational resilience", "AppSec API hardening"),
        ("cors allowlist", "prometheus", "pytest", "oom risk", "telemetry"),
    ),
    RepoSpec(
        "docquery",
        "Secure RAG infrastructure",
        "Official SEC EDGAR filings/company facts supported.",
        ("OWASP LLM01", "OWASP LLM06", "OWASP LLM08"),
        ("context guard", "citation", "auth", "rate limit", "trust_remote_code"),
    ),
    RepoSpec(
        "coderev-agents",
        "Agentic trust boundaries",
        "Security fixtures over code diffs; no company dataset claimed.",
        ("OWASP LLM01", "OWASP LLM06", "OWASP LLM08"),
        ("trust boundary", "untrusted diff", "langgraph", "pip-audit"),
    ),
    RepoSpec(
        "production-ml-platform",
        "ML platform controls",
        "Official NYC TLC sample loader; not company-financial data.",
        ("OWASP A03", "NIST AI RMF Govern/Manage"),
        ("rs256", "drift", "rollback", "pip-audit", "bandit", "official data"),
    ),
    RepoSpec(
        "CubeSat-Health-Monitor",
        "Telemetry anomaly security",
        "Synthetic/simulated telemetry; must be labeled as demo data.",
        ("IoT telemetry integrity", "Secrets management"),
        ("hmac", "ephemeral secret", "audit", "stress test"),
    ),
    RepoSpec(
        "Mission-Control-Telemetry-Simulator",
        "Mission telemetry validation",
        "Synthetic/simulated telemetry; must be labeled as demo data.",
        ("Secure SDLC", "CI security gate"),
        ("bandit", "pytest", "streaming ml", "telemetry"),
    ),
    RepoSpec(
        "Orbital-IoT-Monitor",
        "IoT broker exposure control",
        "Synthetic/simulated telemetry; must be labeled as demo data.",
        ("IoT broker hardening", "CI security gate"),
        ("mqtt config validation", "pip-audit", "docker", "verification"),
    ),
    RepoSpec(
        "Aerospace-Trajectory-Simulator",
        "Scientific API hardening",
        "NASA physics references plus simulation outputs; not company data.",
        ("API hardening", "Numerical validation"),
        ("cors allowlist", "pytest", "prometheus", "schemas"),
    ),
    RepoSpec(
        "ESG-Carbon-Telemetry",
        "Audit-backed data API",
        "Demo sustainability records unless replaced with official filings.",
        ("Secrets management", "Secure SDLC"),
        ("ephemeral secret", "jwt", "bandit", "pip-audit", "hash chain"),
    ),
    RepoSpec(
        "A-Personalized-E-Learning-System-Using-Reinforcement-Learning-Through-Satellite-",
        "RL demo reliability",
        "Interactive quiz data only; no company dataset claimed.",
        ("Input validation", "Testability"),
        ("safe parsing", "pytest", "q-learning"),
    ),
    RepoSpec(
        "Pooja_Portfolio",
        "Recruiter site claim hygiene",
        "Portfolio metadata only; claims validated by scripts.",
        ("Supply-chain hygiene", "Evidence claims"),
        ("verify claims", "npm audit", "github pages"),
    ),
)


def main() -> None:
    cards = []
    for spec in REPOS:
        snapshot = repo_snapshot(spec)
        cards.append(repo_card(spec, snapshot))
        write_repo_audit(spec, snapshot)
    OUT.write_text(render_page(cards), encoding="utf-8")
    print(f"wrote {OUT}")


def repo_snapshot(spec: RepoSpec) -> dict[str, object]:
    path = ROOT / spec.name
    text_index = read_repo_text(path)
    files = list(iter_repo_files(path)) if path.exists() else []
    tests = [p for p in files if "test" in p.name.lower() or "tests" in p.parts]
    workflows = [
        p for p in files if ".github" in p.parts and p.suffix in {".yml", ".yaml"}
    ]
    normalized_index = normalize_evidence(text_index)
    evidence = [
        control
        for control in spec.expected_controls
        if normalize_evidence(control) in normalized_index
    ]
    missing = [control for control in spec.expected_controls if control not in evidence]
    status = git_status(path)
    return {
        "path": path,
        "files": files,
        "tests": tests,
        "workflows": workflows,
        "evidence": evidence,
        "missing": missing,
        "status": status,
    }


def repo_card(spec: RepoSpec, snapshot: dict[str, object]) -> str:
    files = snapshot["files"]
    tests = snapshot["tests"]
    workflows = snapshot["workflows"]
    evidence = snapshot["evidence"]
    missing = snapshot["missing"]
    status = str(snapshot["status"])
    risk = (
        "attention" if missing or status not in {"clean", "not-a-git-repo"} else "ready"
    )
    return f"""
    <article class="card {risk}">
      <div class="card-head">
        <h2>{html.escape(spec.name)}</h2>
        <span>{html.escape(spec.topic)}</span>
      </div>
      <p class="standards">{html.escape(" / ".join(spec.standards))}</p>
      <p><strong>Data:</strong> {html.escape(spec.data_provenance)}</p>
      <dl>
        <div><dt>Files</dt><dd>{len(files)}</dd></div>
        <div><dt>Tests</dt><dd>{len(tests)}</dd></div>
        <div><dt>Workflows</dt><dd>{len(workflows)}</dd></div>
        <div><dt>Git</dt><dd>{html.escape(status)}</dd></div>
      </dl>
      <p><strong>Evidence:</strong> {html.escape(", ".join(evidence) if evidence else "none detected")}</p>
      <p><strong>Open checks:</strong> {html.escape(", ".join(missing) if missing else "none from configured map")}</p>
    </article>
    """


def write_repo_audit(spec: RepoSpec, snapshot: dict[str, object]) -> None:
    path = snapshot["path"]
    if not isinstance(path, Path) or not path.exists():
        return
    docs = path / "docs"
    docs.mkdir(exist_ok=True)
    evidence = snapshot["evidence"]
    missing = snapshot["missing"]
    status = str(snapshot["status"])
    tests = snapshot["tests"]
    workflows = snapshot["workflows"]
    markdown = f"""# 2026 ML Security Audit

Generated from local repository evidence. This file is intentionally conservative: it reports files, controls, and gaps that can be inspected in this repository.

## Scope

- Topic: {spec.topic}
- Standards map: {", ".join(spec.standards)}
- Data provenance: {spec.data_provenance}
- Git state at generation: {status}
- Test files detected: {len(tests)}
- GitHub workflows detected: {len(workflows)}

## Evidence Found

{bullet_list(evidence)}

## Open Gaps

{bullet_list(missing) if missing else "- No configured evidence-map gaps detected."}

## Recruiter Signal

This repository should be evaluated by running its checked-in tests and CI/security gates. Do not cite benchmark numbers or production readiness unless the repo contains the command, artifact, and current passing validation needed to reproduce the claim.

## Rebuild

Run from the profile repository:

```bash
python tools/build_security_dashboard.py
```
"""
    (docs / "ML_SECURITY_AUDIT_2026.md").write_text(markdown, encoding="utf-8")
    (docs / "security-showcase.html").write_text(
        render_repo_page(spec, snapshot), encoding="utf-8"
    )


def bullet_list(items: object) -> str:
    if not isinstance(items, list) or not items:
        return "- None detected from configured evidence map."
    return "\n".join(f"- {item}" for item in items)


def render_repo_page(spec: RepoSpec, snapshot: dict[str, object]) -> str:
    evidence = snapshot["evidence"]
    missing = snapshot["missing"]
    status = str(snapshot["status"])
    tests = snapshot["tests"]
    workflows = snapshot["workflows"]
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(spec.name)} Security Showcase</title>
  <style>
    body {{ margin: 0; font-family: Inter, Arial, sans-serif; background: #f8fafc; color: #172033; }}
    main {{ max-width: 920px; margin: 0 auto; padding: 36px 24px; }}
    h1 {{ margin: 0 0 8px; font-size: 30px; letter-spacing: 0; }}
    .topic {{ color: #475569; margin-bottom: 24px; }}
    section {{ background: #fff; border: 1px solid #dbe2ea; border-radius: 8px; padding: 18px; margin: 14px 0; }}
    dl {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }}
    dt {{ color: #64748b; font-size: 12px; }}
    dd {{ margin: 4px 0 0; font-weight: 700; }}
    li {{ margin: 6px 0; }}
    code {{ background: #edf2f7; padding: 2px 5px; border-radius: 4px; }}
  </style>
</head>
<body>
  <main>
    <h1>{html.escape(spec.name)}</h1>
    <p class="topic">{html.escape(spec.topic)}</p>
    <section>
      <h2>Evidence Snapshot</h2>
      <dl>
        <div><dt>Git state</dt><dd>{html.escape(status)}</dd></div>
        <div><dt>Test files</dt><dd>{len(tests)}</dd></div>
        <div><dt>Workflows</dt><dd>{len(workflows)}</dd></div>
      </dl>
    </section>
    <section>
      <h2>Standards Map</h2>
      <p>{html.escape(", ".join(spec.standards))}</p>
      <p><strong>Data provenance:</strong> {html.escape(spec.data_provenance)}</p>
    </section>
    <section>
      <h2>Controls Found</h2>
      <ul>{html_list(evidence)}</ul>
    </section>
    <section>
      <h2>Open Checks</h2>
      <ul>{html_list(missing) if missing else "<li>No configured evidence-map gaps detected.</li>"}</ul>
    </section>
    <section>
      <h2>How To Verify</h2>
      <p>Run this repo's checked-in tests and CI/security gates. Treat this page as an index, not a benchmark report.</p>
      <p>Generated by <code>python tools/build_security_dashboard.py</code> from the profile repository.</p>
    </section>
  </main>
</body>
</html>
"""


def html_list(items: object) -> str:
    if not isinstance(items, list) or not items:
        return "<li>None detected from configured evidence map.</li>"
    return "".join(f"<li>{html.escape(str(item))}</li>" for item in items)


def read_repo_text(path: Path) -> str:
    if not path.exists():
        return ""
    chunks: list[str] = []
    for candidate in iter_repo_files(path):
        if candidate.suffix.lower() not in {
            ".py",
            ".md",
            ".yml",
            ".yaml",
            ".json",
            ".toml",
            ".js",
            ".jsx",
        }:
            continue
        try:
            chunks.append(
                candidate.read_text(encoding="utf-8", errors="ignore").lower()
            )
        except OSError:
            continue
    return "\n".join(chunks)


def normalize_evidence(value: str) -> str:
    return value.lower().replace("-", " ").replace("_", " ")


def iter_repo_files(path: Path):
    for candidate in path.rglob("*"):
        if any(part in SKIP_DIRS for part in candidate.parts):
            continue
        if candidate.is_file():
            yield candidate


def git_status(path: Path) -> str:
    if not (path / ".git").exists():
        return "not-a-git-repo"
    result = subprocess.run(
        ["git", "status", "--short"],
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
    .sub {{ max-width: 900px; color: #4d5b6a; line-height: 1.5; }}
    main {{ max-width: 1180px; margin: 0 auto 48px; padding: 0 28px; display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 16px; }}
    .card {{ background: white; border: 1px solid #d9dee5; border-radius: 8px; padding: 18px; box-shadow: 0 1px 2px rgba(15, 23, 42, .04); }}
    .card.attention {{ border-left: 4px solid #b45309; }}
    .card.ready {{ border-left: 4px solid #047857; }}
    .card-head {{ display: flex; gap: 10px; align-items: flex-start; justify-content: space-between; }}
    h2 {{ margin: 0; font-size: 17px; line-height: 1.25; }}
    .card-head span {{ color: #526172; font-size: 12px; text-align: right; max-width: 130px; }}
    .standards {{ color: #2f5d8c; font-size: 13px; }}
    dl {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 14px 0; }}
    dt {{ color: #657386; font-size: 11px; }}
    dd {{ margin: 2px 0 0; font-weight: 700; font-size: 15px; }}
    p {{ font-size: 13px; line-height: 1.45; }}
    footer {{ max-width: 1180px; margin: 0 auto 36px; padding: 0 28px; color: #5f6f80; font-size: 12px; }}
  </style>
</head>
<body>
  <header>
    <h1>ML Security Portfolio Evidence Dashboard</h1>
    <p class="sub">Generated from local repository files. Counts and evidence terms are computed from checked-in code, tests, workflows, and docs; this page intentionally avoids unsupported benchmark or production claims.</p>
  </header>
  <main>
    {''.join(cards)}
  </main>
  <footer>
    Standards map: OWASP LLM Top 10 2025, MITRE ATLAS, NIST AI RMF, SLSA, and practical AppSec/DevSecOps controls. Rebuild with <code>python tools/build_security_dashboard.py</code>.
  </footer>
</body>
</html>
"""


if __name__ == "__main__":
    main()
