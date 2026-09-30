from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "PRODUCTION.md",
    "CLAIM_AUDIT.md",
    "RESUME_METRICS_EVIDENCE.md",
    "PROVENANCE_LEDGER.md",
    "SECURITY.md",
    "SECURITY_AUDIT_2026-09-30.md",
    "SECURITY_CHECKLIST.md",
    "RUNBOOK.md",
)

FORBIDDEN_ACTIVE = (
    "scope: prototype security gateway",
    "integration-topology prototype",
)

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate_readme_links(readme: str) -> list[str]:
    failures: list[str] = []

    for target in MARKDOWN_LINK.findall(readme):
        target = target.strip()
        if not target or target.startswith("#"):
            continue

        parsed = urlparse(target)
        if parsed.scheme:
            if parsed.scheme != "https":
                failures.append(f"README contains non-HTTPS link: {target}")
            continue

        local_target = target.split("#", 1)[0]
        if local_target and not (ROOT / local_target).exists():
            failures.append(f"README contains missing local link target: {target}")

    return failures


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required profile evidence file: {rel}")

    readme_path = ROOT / "README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        readme_lower = readme.lower()
        for marker in FORBIDDEN_ACTIVE:
            if marker in readme_lower:
                failures.append(f"README contains retired active-system marker: {marker}")
        failures.extend(validate_readme_links(readme))

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print("profile production/evidence/security surfaces verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
