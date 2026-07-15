import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ["README.md", "RUNBOOK.md", "security-dashboard.html"]
OUT = ROOT / "provenance.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_value(args: list[str]) -> str:
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def main() -> None:
    subjects = []
    for relative in SUBJECTS:
        path = ROOT / relative
        if path.exists():
            subjects.append({"name": relative, "digest": {"sha256": sha256(path)}})
    statement = {
        "_type": "https://in-toto.io/Statement/v0.1",
        "subject": subjects,
        "predicateType": "https://slsa.dev/provenance/v0.2",
        "predicate": {
            "builder": {
                "id": "https://github.com/poojakira/poojakira/.github/workflows/pages.yml"
            },
            "buildType": "profile-dashboard-local-build",
            "invocation": {
                "configSource": {
                    "uri": "https://github.com/poojakira/poojakira",
                    "digest": {"gitCommit": git_value(["git", "rev-parse", "HEAD"])},
                    "entryPoint": "python tools/build_security_dashboard.py",
                }
            },
            "metadata": {"buildStartedOn": datetime.now(timezone.utc).isoformat()},
        },
    }
    OUT.write_text(
        json.dumps(statement, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
