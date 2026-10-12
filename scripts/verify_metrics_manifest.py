"""Check the dated profile/metrics evidence is internally consistent.

This is a repository-content check, not an independent GitHub CI attestation.
"""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads(
    (root / "evidence/portfolio_metrics.json").read_text(encoding="utf-8")
)
profile = (root / "README.md").read_text(encoding="utf-8")
evidence = (root / "RESUME_METRICS_EVIDENCE.md").read_text(
    encoding="utf-8"
)
projects = data["projects"]

if data["schema_version"] != 1:
    raise SystemExit("Unsupported recruiting evidence schema")

for item in projects.values():
    run_url = f'{item["url"]}/actions/runs/{item["run_id"]}'
    if run_url not in evidence or run_url not in profile:
        raise SystemExit(f"Missing linked run evidence: {run_url}")

gateway = projects["mcp_agent_security_gateway"]
iam = projects["aws_agent_identity_guard"]
hf = projects["hf_model_provenance_scanner"]

expected_profile = [
    f'{gateway["passed"]} passing tests',
    f'{gateway["statement_coverage_percent"]}% coverage',
    f'{gateway["source_signature_count"]} named runtime detector signatures',
    f'{iam["passed"]} passed / {iam["skipped"]} skipped',
    f'{hf["passed"]} passed / {hf["skipped"]} skipped',
    f'{hf["statement_coverage_percent"]}% coverage',
    f'{hf["curated_adversarial_fixtures_detected"]}/{hf["curated_adversarial_fixtures_total"]} adversarial fixtures',
]
for entry in expected_profile:
    if entry not in profile:
        raise SystemExit(f"README/manifest drift: missing {entry}")

expected_evidence = [
    f'{gateway["passed"]} passed, {gateway["statement_coverage_percent"]}% coverage',
    f'{iam["collected"]} collected, {iam["passed"]} passed, {iam["skipped"]} skipped',
    f'{hf["passed"]} passed, {hf["skipped"]} skipped',
]
for entry in expected_evidence:
    if entry not in evidence:
        raise SystemExit(f"Evidence index/manifest drift: missing {entry}")

print("Dated recruiting evidence agrees with profile and evidence index")
