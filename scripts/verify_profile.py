from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "README.md",
    "PRODUCTION.md",
    "CLAIM_AUDIT.md",
    "RESUME_METRICS_EVIDENCE.md",
    "PROVENANCE_LEDGER.md",
)

FORBIDDEN_ACTIVE = (
    "scope: prototype security gateway",
    "integration-topology prototype",
)


def main() -> int:
    failures: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required profile evidence file: {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    for marker in FORBIDDEN_ACTIVE:
        if marker in readme:
            failures.append(f"README contains retired active-system marker: {marker}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print("profile production/evidence surfaces verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
