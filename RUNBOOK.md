# Runbook

This is a GitHub profile repository. It contains only the profile README and supporting automation scripts.

## Operations

- `tools/build_security_dashboard.py` - generates `security-dashboard.html` from sibling repo evidence
- `tools/write_profile_provenance.py` - generates `provenance.json` with SHA-256 digests

## No runtime services

This repo has no services to operate. CI generates static artifacts only.
