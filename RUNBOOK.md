# Public Profile Runbook

## Scope
This repository publishes the GitHub profile README and a conservative evidence dashboard for selected public AI/ML security repositories.

## Local validation

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests -q -ra -W error
python tools/build_security_dashboard.py
```

## Evidence refresh

```bash
./run_evidence.sh
```

The evidence script writes generated logs and hashes under `evidence_artifacts/`. Those files are local build outputs and are intentionally ignored by git. Do not cite them unless they were regenerated from a clean checkout and the command output is available.

## GitHub Pages
The Pages workflow clones the selected public repositories, runs profile tests, rebuilds `security-dashboard.html`, copies it to `docs/index.html`, and deploys GitHub Pages. The dashboard is an index of observable repo files, not a certification that any project is production ready.