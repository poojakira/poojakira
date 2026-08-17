# Runbook

## Engineering Update - 2026-07-27

Repository: poojakira
Purpose: Public profile and portfolio evidence dashboard

## Build

- Lint: make lint
- Format: make format
- Test: make test
- Full local gate: make verify

## Dashboard

3D operational dashboard: security-dashboard.html; make dashboard regenerates and preserves the 3D view.

## Dependencies And Data

Dashboard remains an evidence index, not a certification or production-readiness claim.

## Validation Snapshot

Validated: profile smoke tests passed (5 tests), Ruff passed for tools/tests, generator py_compile passed, browser validation reported nonblank WebGL canvas.

## Operating Limits

- Re-check Linux and GitHub Actions after pushing to main.
- Treat local dashboard scores as evidence indicators, not certifications.
- Do not cite production readiness until clean CI, dependency audit, license status, and runtime smoke tests are current.