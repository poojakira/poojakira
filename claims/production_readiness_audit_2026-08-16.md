# Production Readiness Audit - 2026-08-16

Scope: 15 public repositories under `poojakira`, reviewed from clean clones in `C:\tmp\poojakira-production-audit-20260816`.

Verdict: current CI is green across the portfolio, but the repositories are not collectively production-certified or proven novel. Several are strong prototypes or evidence hubs; production-grade claims should remain narrow and evidence-linked.

## Summary

| Repository | Current classification | Verified strengths | Production blockers |
| --- | --- | --- | --- |
| `poojakira` | GitHub evidence profile | Evidence-first README and dashboard workflow | Profile-level claims still depend on downstream repo evidence |
| `Pooja_Kiran_Portfolio_Website` | Static portfolio | GitHub Pages deploys; cinematic redesign; metric evidence links | No automated UI regression tests |
| `mcp-agent-security-gateway` | Pre-production security prototype | Fail-closed API key behavior; prompt/PII/audit tests | Metrics endpoint and deployment hardening need stricter policy |
| `hf-model-provenance-scanner` | Supply-chain scanner prototype | Safe archive scanning posture; CI green | Threat model and uniqueness claims need conservative wording |
| `aws-agent-identity-guard` | Static IAM/security linter | SARIF/JSON flows; CI green | Coverage gate and stale security audit language need cleanup |
| `llm-redteam-framework` | Evaluation fixture framework | Prompt/security test fixtures; CI green | Not a production LLM defense; app metrics exposure needs review |
| `dataset-poisoning-detector` | Research prototype | 55 local tests passed | README metrics are low; not a deployable poisoning detector |
| `model-privacy-attacks` | Research prototype | 18 local tests passed | README references absent evidence paths; low coverage gate |
| `adversarial-ml-lab` | Research harness | Local tests reported 40 passed | Test wrapper timed out; README has conflicting CIFAR/coverage claims |
| `attack-v19-core` | Dataset/version utility | Focused tests passed in clean clone | Checkout has line-ending drift; CI misses shipped namespace checks |
| `PulseNet-RUL-Forecasting` | Archived experiment | Archive marker present | Archive verification fails on `ledger_public.json`; not active production code |
| `ml-security-command-center` | Static command center | Metrics source now tracks renamed MCP repo | Static inventory only; no license before this audit |
| `mlsec-dashboards` | Static dashboard/live API prototype | Dashboard pages and live server entrypoint | Minimal manifest/tests; deployment/API claims require evidence |
| `mlsec-benchmark-suite` | Benchmark harness | CI green; adapter evidence design | Smoke benchmark is not a third-party benchmark; dependency pinning still weak |
| `unified-ml-security-platform` | Architecture/spec hub | Integration docs and dashboard | Not a working platform; production compose/deploy claims are stubs |

## Validation Evidence

- GitHub Actions: latest `main` CI status was green for all 15 repositories at audit time.
- Local tests:
  - `dataset-poisoning-detector`: `55 passed`.
  - `model-privacy-attacks`: `18 passed`.
  - `attack-v19-core`: focused downloader/CLI tests `28 passed`.
  - `adversarial-ml-lab`: tests printed `40 passed`, but the command wrapper timed out after 121 seconds.
  - `PulseNet-RUL-Forecasting`: `scripts/verify_archive.py` failed because `ledger_public.json` is still an unsupported restored deployment surface.

## Fixes Applied In This Audit

- Added MIT license files to `Pooja_Kiran_Portfolio_Website`, `ml-security-command-center`, and `mlsec-dashboards`.
- Replaced stale `mcp-security-gateway-monitor` public references with `mcp-agent-security-gateway` in current docs, dashboards, and adapter references.
- Added `requirements.txt` to `mlsec-dashboards` for the live FastAPI server surface.
- Linked portfolio hero metrics directly to evidence artifacts.
- Updated the portfolio runbook to match the current static-site asset model.
- Fixed the GitHub profile dashboard generator so rebuilds do not duplicate the summary prefix.

## Open Risks

- Novelty is not proven. The portfolio is differentiated, but external prior-art and competitor review is required before claiming novelty.
- Several repositories are research or evaluation tools, not production services.
- Coverage gates remain intentionally low in multiple repos.
- Some docs still need repo-local truthing against generated evidence before stronger claims are safe.
- Account-level GitHub profile metadata could not be updated because the current `gh` token lacks the `user` scope.

## Recommended Next Pass

1. Add repo-local production readiness checklists and coverage gates to active code repos.
2. Convert `ml-security-command-center` and `mlsec-dashboards` from static evidence mirrors into tested products or label them clearly as dashboards.
3. Fix `PulseNet-RUL-Forecasting` archive verification or keep it visibly archived.
4. Add UI smoke tests for the portfolio site.
5. Run external prior-art research before any "novel product" claim.
