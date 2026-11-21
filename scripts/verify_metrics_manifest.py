"""Check source-scoped profile content, not independent CI or release acceptance."""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {
    "mcp-agent-security-gateway",
    "aws-agent-identity-guard",
    "hf-model-provenance-scanner",
    "attack-detection-engine",
}
SHA = re.compile(r"[0-9a-f]{40}")


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    try:
        data = json.loads((root / "evidence/portfolio_metrics.json").read_text())
        profile = (root / "README.md").read_text(encoding="utf-8")
        evidence = (root / "RESUME_METRICS_EVIDENCE.md").read_text(encoding="utf-8")
    except (OSError, ValueError) as exc:
        return [f"Cannot read recruiting evidence: {exc}"]
    if data.get("schema_version") != 2:
        return ["Unsupported recruiting evidence schema"]
    projects = data.get("projects", {})
    if not isinstance(projects, dict) or set(projects) != PROJECTS:
        return ["Expected exactly the four reviewed security projects"]
    if not all(isinstance(item, dict) for item in projects.values()):
        return ["Expected project records"]

    historical = data.get("historical_snapshot", {})
    old_path = "evidence/portfolio_metrics_2026-10-12.json"
    if historical.get("path") != old_path:
        failures.append("Historical snapshot must use the fixed archive path")
    else:
        try:
            old_bytes = (root / old_path).read_bytes()
            if hashlib.sha256(old_bytes).hexdigest() != historical.get("sha256"):
                failures.append("Preserved historical snapshot digest mismatch")
            if json.loads(old_bytes).get("schema_version") != 1:
                failures.append("Expected original historical schema")
        except (OSError, ValueError) as exc:
            failures.append(f"Cannot verify historical snapshot: {exc}")

    for repository, item in projects.items():
        base = f"https://github.com/poojakira/{repository}"
        source = item.get("source_commit", "")
        archive = item.get("archive_commit", "")
        if (
            not isinstance(source, str)
            or not isinstance(archive, str)
            or not SHA.fullmatch(source)
            or not SHA.fullmatch(archive)
            or source == archive
        ):
            failures.append(f"Expected distinct full source/archive SHAs: {repository}")
        if item.get("repository") != repository:
            failures.append(f"Repository identity mismatch: {repository}")
        if item.get("release_decision") != "PARTIAL":
            failures.append(f"Unverified release-decision change: {repository}")
        expected_urls = {
            "source_url": f"{base}/blob/{source}/README.md",
            "manifest_url": (
                f"https://raw.githubusercontent.com/poojakira/{repository}/"
                f"{archive}/release-evidence/manifest.json"
            ),
            "assessment_url": (
                f"{base}/blob/{archive}/release-evidence/RELEASE_ASSESSMENT.md"
            ),
        }
        for field, expected in expected_urls.items():
            if item.get(field) != expected:
                failures.append(f"Invalid immutable {field}: {repository}")
            if expected not in profile or expected not in evidence:
                failures.append(f"Missing profile/index link: {expected}")
        if not re.fullmatch(rf"{re.escape(base)}/pull/[1-9][0-9]*", item.get("pr", "")):
            failures.append(f"Invalid review URL: {repository}")

        counts = [item.get(key) for key in ("passed", "skipped", "subtests_passed")]
        coverage = item.get("coverage_percent")
        valid_counts = all(type(value) is int and value >= 0 for value in counts)
        valid_coverage = (
            type(coverage) in (int, float)
            and math.isfinite(coverage)
            and 0 <= coverage <= 100
        )
        if not valid_counts or not valid_coverage:
            failures.append(
                f"Invalid local testcase/coverage measurements: {repository}"
            )
            continue
        passed, skipped, subtests = counts
        coverage_unit = "line" if repository == "attack-detection-engine" else "statement"
        metric = (
            f"{passed} passed / {skipped} skipped · "
            f"{coverage:.2f}% local {coverage_unit} coverage"
        )
        if subtests:
            metric += f" · {subtests} separate passing subtests"
        if metric not in profile or metric not in evidence:
            failures.append(f"Local metrics drift: {repository}")
        if source not in evidence:
            failures.append(
                f"Full source SHA missing from evidence index: {repository}"
            )

    iam = projects["aws-agent-identity-guard"]
    if iam.get("static_checks") != 24 or iam.get("additional_live_context_checks") != 1:
        failures.append("IAM check classification changed without reconciled evidence")
    if projects["hf-model-provenance-scanner"].get("independent_closure") != "BLOCKED":
        failures.append("HF independent closure must retain its actual blocked state")
    aegis = projects["attack-detection-engine"].get("hosted_ci", {})
    run_id = aegis.get("run_id")
    run_url = (
        "https://github.com/poojakira/attack-detection-engine/actions/runs/" f"{run_id}"
    )
    if (
        type(run_id) is not int
        or run_id <= 0
        or aegis.get("url") != run_url
        or aegis.get("status") != "queued"
        or aegis.get("conclusion") is not None
    ):
        failures.append(
            "Aegis hosted observation differs from the dated queued recheck"
        )
    if run_url not in profile or run_url not in evidence:
        failures.append("Missing Aegis hosted observation link")
    for text, label in ((profile, "README"), (evidence, "evidence index")):
        for required in (
            "PARTIAL",
            "24 static checks plus 1 additional live-context check",
            "3 skips cover the absent legacy TestRulesModule API",
            "BLOCKED",
            "queued / NOT VERIFIED",
            "hosted Colab",
        ):
            if required not in text:
                failures.append(f"Missing measurement scope in {label}: {required}")
    return failures


def main() -> int:
    failures = validate(ROOT)
    if failures:
        raise SystemExit("\n".join(failures))
    print("Four source-scoped candidates agree with profile and evidence index")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
