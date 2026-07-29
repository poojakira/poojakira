# Portfolio Evidence Runbook

This repository publishes an evidence index for public engineering work. It must not turn documentation keywords into implementation claims, score formulas, or production-readiness labels.

## Local Validation

```powershell
py -3.12 -m pip install -r requirements-dev.txt
py -3.12 -m pytest
python -m pytest
python tools/validate_claims.py --max-age-days 3650
python tools/build_security_dashboard.py
python tools/write_profile_provenance.py
```

Use the long local staleness window only for historical/local validation. CI uses a shorter freshness window.

## Claim Registry

Claims live in `claims/registry.json`. Each claim must include:

- claim
- repository
- project_type
- evidence_type
- evidence_url
- source_commit
- measurement_date
- status
- limitations

Allowed evidence types are encoded in `tools/validate_claims.py`. Numerical metric claims require immutable coverage, benchmark, or CI evidence. Unsupported score or maturity wording fails validation.

## Dashboard

`tools/build_security_dashboard.py` renders `security-dashboard.html` from the registry only. It does not scan repository text for keywords and does not compute readiness, risk, security, ATT&CK, or score formulas.

## Stale Evidence

`.github/workflows/evidence-freshness.yml` runs on a schedule with external link checks. When validation fails, it opens or comments on an issue and fails the workflow. It must not silently update claims or generated artifacts.

## Provenance Language

`tools/write_profile_provenance.py` writes an unsigned profile evidence manifest. It is not SLSA provenance and must not be described as signed provenance.
