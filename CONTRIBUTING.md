# Contributing

## Scope
This repository maintains the public GitHub profile README and a conservative evidence dashboard for selected public AI/ML security repositories.

## How to Submit Changes
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-change`.
3. Make the smallest truthful change.
4. Install validation dependencies: `python -m pip install -r requirements-dev.txt` (`py -3.12 -m pip ...` on Windows if `python` is unavailable).
5. Run tests: `python -m pytest tests -q -ra -W error`.
6. Rebuild the dashboard: `python tools/build_security_dashboard.py`.
7. Submit a pull request with command output.


## Dashboard Inputs
- Clone the selected public repositories as siblings of this checkout before citing dashboard counts.
- Treat missing sibling clones as open checks, not as evidence of failure or success.
## Evidence Rules
- Do not commit generated `evidence_artifacts/`, `docs/`, or `provenance.json` output.
- Do not cite benchmark, production, or security maturity claims unless the source repository contains the command and passing validation evidence.
- Use `./run_evidence.sh` only to regenerate local evidence outputs.

## Coding Standards
- Keep profile claims public and inspectable.
- Prefer explicit unknown/open-check labels over unsupported maturity claims.
- No sensitive data, keys, passwords, or private employment data in this repository.

## Code of Conduct
Be respectful, constructive, and professional.