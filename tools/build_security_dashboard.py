from __future__ import annotations

import argparse
import html
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

PROFILE_ROOT = Path(__file__).resolve().parents[1]
if str(PROFILE_ROOT) not in sys.path:
    sys.path.insert(0, str(PROFILE_ROOT))

from tools.validate_claims import DEFAULT_REGISTRY, load_registry, validate_registry

DEFAULT_OUT = PROFILE_ROOT / "security-dashboard.html"

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build evidence-based portfolio dashboard")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--max-age-days", type=int, default=90)
    args = parser.parse_args(argv)

    registry = load_registry(args.registry)
    validate_registry(registry, max_age_days=args.max_age_days, check_links=False)
    page = render_page(registry)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8")
    print(f"wrote {args.output}")


def render_page(registry: dict[str, Any]) -> str:
    claims = sorted(
        registry["claims"], key=lambda item: (item["repository"].lower(), item["claim"].lower())
    )
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for claim in claims:
        grouped[claim["repository"]].append(claim)

    rows = "\n".join(render_repo_section(repo, grouped[repo]) for repo in sorted(grouped))
    registry_json = json.dumps(registry, sort_keys=True, separators=(",", ":"))
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Evidence-Based Engineering Portfolio</title>
  <style>
    :root {{ color-scheme: light; --ink:#17202a; --muted:#526172; --line:#d7dde5; --bg:#f7f8fa; --panel:#fff; --ok:#176b45; --warn:#9a5a00; --bad:#a12828; }}
    body {{ margin:0; font-family: Arial, sans-serif; background:var(--bg); color:var(--ink); }}
    header, main, footer {{ max-width:1120px; margin:0 auto; padding:24px; }}
    header {{ padding-top:38px; }}
    h1 {{ margin:0 0 10px; font-size:32px; letter-spacing:0; }}
    h2 {{ margin:0; font-size:20px; }}
    a {{ color:#195db3; text-decoration:none; }}
    p {{ line-height:1.5; }}
    .summary {{ color:var(--muted); max-width:860px; }}
    .repo {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; margin:0 0 16px; overflow:hidden; }}
    .repo-head {{ display:flex; justify-content:space-between; gap:12px; padding:16px; border-bottom:1px solid var(--line); }}
    .type {{ color:var(--muted); font-size:13px; }}
    table {{ width:100%; border-collapse:collapse; }}
    th, td {{ text-align:left; vertical-align:top; padding:12px 16px; border-bottom:1px solid var(--line); font-size:14px; }}
    th {{ color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.04em; }}
    tr:last-child td {{ border-bottom:0; }}
    .status {{ display:inline-block; border-radius:999px; padding:3px 8px; font-size:12px; background:#eef2f7; }}
    .verified_documentation, .verified_public_repository {{ color:var(--ok); background:#e9f6ef; }}
    .blocked, .stale, .unverified {{ color:var(--bad); background:#faeaea; }}
    .note {{ color:var(--muted); }}
    code {{ background:#eef2f7; border:1px solid var(--line); border-radius:4px; padding:2px 4px; }}
  </style>
</head>
<body>
  <header>
    <h1>Evidence-Based Engineering Portfolio</h1>
    <p class="summary">This page summarizes only claims recorded in <code>claims/registry.json</code>. Documentation keywords, repository size, test-file counts, and local dashboard formulas do not count as implemented controls. Missing CI, release, coverage, SBOM, provenance, or benchmark evidence stays explicit instead of becoming a score.</p>
  </header>
  <main>
{rows}
  </main>
  <footer>
    <p>Generated deterministically from the claim registry. Rebuild with <code>python tools/build_security_dashboard.py</code>. Validate with <code>python tools/validate_claims.py --check-links</code>.</p>
  </footer>
  <script type="application/json" id="claim-registry">{html.escape(registry_json)}</script>
</body>
</html>
"""


def render_repo_section(repo: str, claims: list[dict[str, str]]) -> str:
    first = claims[0]
    rows = "\n".join(render_claim_row(claim) for claim in claims)
    return f"""    <section class="repo" aria-labelledby="repo-{slug(repo)}">
      <div class="repo-head">
        <div>
          <h2 id="repo-{slug(repo)}"><a href="https://github.com/{html.escape(repo)}">{html.escape(repo)}</a></h2>
          <div class="type">{html.escape(first['project_type'])}</div>
        </div>
        <span class="status {html.escape(first['status'])}">{html.escape(first['status'].replace('_', ' '))}</span>
      </div>
      <table>
        <thead><tr><th>Claim</th><th>Evidence</th><th>Status and limitations</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </section>"""


def render_claim_row(claim: dict[str, str]) -> str:
    evidence = (
        f"<a href=\"{html.escape(claim['evidence_url'])}\">{html.escape(claim['evidence_type'].replace('_', ' '))}</a>"
        f"<br><span class=\"note\">commit <code>{html.escape(claim['source_commit'])}</code>; measured {html.escape(claim['measurement_date'])}</span>"
    )
    status = (
        f"<span class=\"status {html.escape(claim['status'])}\">{html.escape(claim['status'].replace('_', ' '))}</span>"
        f"<br><span class=\"note\">{html.escape(claim['limitations'])}</span>"
    )
    return f"          <tr><td>{html.escape(claim['claim'])}</td><td>{evidence}</td><td>{status}</td></tr>"


def slug(value: str) -> str:
    return "".join(char.lower() if char.isalnum() else "-" for char in value).strip("-")


if __name__ == "__main__":
    main()
