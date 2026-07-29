from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "claims" / "registry.json"
REQUIRED_FIELDS = {
    "claim",
    "repository",
    "project_type",
    "evidence_type",
    "evidence_url",
    "source_commit",
    "measurement_date",
    "status",
    "limitations",
}
ALLOWED_EVIDENCE_TYPES = {
    "default_branch_ci",
    "signed_release",
    "coverage_artifact",
    "sbom",
    "provenance",
    "benchmark_result",
    "current_documentation",
}
ALLOWED_STATUSES = {
    "verified_documentation",
    "verified_public_repository",
    "verified_ci_green",
    "verified_signed_release",
    "verified_benchmark",
    "stale",
    "blocked",
    "unverified",
}
FORBIDDEN_CLAIM_TERMS = {
    "production-grade",
    "production ready",
    "maturity score",
    "security score",
    "attack coverage",
    "att&ck coverage",
    "slsa provenance",
}
NUMERIC_PATTERN = re.compile(r"(?<![a-f0-9])\d+(?:\.\d+)?\s*(?:%|percent|score|coverage|maturity|ms|s|x|fps|rps)", re.I)


class ClaimValidationError(ValueError):
    pass


def load_registry(path: Path = DEFAULT_REGISTRY) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        registry = json.load(handle)
    if not isinstance(registry, dict):
        raise ClaimValidationError("registry root must be an object")
    if registry.get("schema_version") != "1.0.0":
        raise ClaimValidationError("schema_version must be 1.0.0")
    claims = registry.get("claims")
    if not isinstance(claims, list) or not claims:
        raise ClaimValidationError("claims must be a non-empty list")
    return registry


def parse_date(value: str) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ClaimValidationError(f"invalid measurement_date: {value!r}") from exc


def validate_registry(
    registry: dict[str, Any], *, max_age_days: int = 90, check_links: bool = False
) -> list[str]:
    warnings: list[str] = []
    today = datetime.now(timezone.utc).date()
    seen: set[tuple[str, str]] = set()
    for index, claim in enumerate(registry["claims"]):
        if not isinstance(claim, dict):
            raise ClaimValidationError(f"claim[{index}] must be an object")
        missing = REQUIRED_FIELDS - set(claim)
        if missing:
            raise ClaimValidationError(f"claim[{index}] missing fields: {sorted(missing)}")
        extra_empty = [field for field in REQUIRED_FIELDS if not str(claim[field]).strip()]
        if extra_empty:
            raise ClaimValidationError(f"claim[{index}] has empty fields: {extra_empty}")
        evidence_type = claim["evidence_type"]
        if evidence_type not in ALLOWED_EVIDENCE_TYPES:
            raise ClaimValidationError(f"claim[{index}] invalid evidence_type: {evidence_type}")
        status = claim["status"]
        if status not in ALLOWED_STATUSES:
            raise ClaimValidationError(f"claim[{index}] invalid status: {status}")
        source_commit = claim["source_commit"]
        if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
            raise ClaimValidationError(f"claim[{index}] source_commit must be a full SHA")
        measured = parse_date(claim["measurement_date"])
        if measured > today:
            raise ClaimValidationError(f"claim[{index}] measurement_date is in the future")
        if (today - measured).days > max_age_days:
            raise ClaimValidationError(
                f"claim[{index}] stale: {claim['repository']} measured {measured.isoformat()}"
            )
        key = (claim["repository"], claim["claim"])
        if key in seen:
            raise ClaimValidationError(f"duplicate claim for {claim['repository']}: {claim['claim']}")
        seen.add(key)
        searchable = f"{claim['claim']} {claim['status']} {claim['limitations']}".lower()
        for term in FORBIDDEN_CLAIM_TERMS:
            if term in searchable:
                raise ClaimValidationError(f"claim[{index}] contains forbidden term: {term}")
        if NUMERIC_PATTERN.search(claim["claim"]):
            if evidence_type not in {"coverage_artifact", "benchmark_result", "default_branch_ci"}:
                raise ClaimValidationError(
                    f"claim[{index}] numeric result requires immutable metric evidence"
                )
        if check_links:
            check_url(str(claim["evidence_url"]))
    return warnings


def check_url(url: str) -> None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "poojakira-evidence-validator"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            if response.status >= 400:
                raise ClaimValidationError(f"link check failed {response.status}: {url}")
    except urllib.error.HTTPError as exc:
        raise ClaimValidationError(f"link check failed {exc.code}: {url}") from exc
    except urllib.error.URLError as exc:
        raise ClaimValidationError(f"link check failed: {url}: {exc.reason}") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate portfolio evidence claims")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--max-age-days", type=int, default=90)
    parser.add_argument("--check-links", action="store_true")
    args = parser.parse_args(argv)
    try:
        registry = load_registry(args.registry)
        validate_registry(registry, max_age_days=args.max_age_days, check_links=args.check_links)
    except ClaimValidationError as exc:
        print(f"claim validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"validated {len(registry['claims'])} claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
