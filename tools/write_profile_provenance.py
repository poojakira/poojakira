from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ["README.md", "RUNBOOK.md", "security-dashboard.html", "claims/registry.json"]
DEFAULT_OUT = ROOT / "provenance.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_value(args: list[str]) -> str:
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def build_manifest() -> dict[str, Any]:
    subjects = []
    for relative in sorted(SUBJECTS):
        path = ROOT / relative
        if path.exists():
            subjects.append({"name": relative, "digest": {"sha256": sha256(path)}})
    return {
        "schema_version": "1.0.0",
        "kind": "unsigned-profile-evidence-manifest",
        "subject": subjects,
        "source": {
            "repository": "https://github.com/poojakira/poojakira",
            "commit": git_value(["git", "rev-parse", "HEAD"]),
            "tree_state": git_value(["git", "status", "--short"]),
        },
        "limitations": "This is a deterministic digest manifest for profile artifacts. It is not SLSA provenance and is not signed.",
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write unsigned profile evidence manifest")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args(argv)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build_manifest(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
