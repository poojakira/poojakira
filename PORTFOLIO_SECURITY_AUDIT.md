# PORTFOLIO_SECURITY_AUDIT.md

Date: 2026-09-16
Owner: `poojakira`

## Executive summary

The account currently exposes **19 repositories**. The requested security/AI-security audit scope contains **14 repositories**; the remaining repositories are portfolio/site, infrastructure, private non-security work, or unrelated ML work and were classified rather than silently treated as security projects.

The audit was performed against the live GitHub repositories using source, tests, documentation, CI configuration, committed evidence, and GitHub Actions results where available. Direct source changes were made for the highest-confidence correctness and security findings.

The most important corrected issue was the former NumPy DP-SGD implementation in `model-privacy-attacks`: it clipped an aggregate batch gradient and produced an unvalidated epsilon estimate. That path can no longer be mistaken for formal DP-SGD. Formal DP-SGD is now explicitly routed through an Opacus-backed path with per-example clipping/noising/accounting, while the NumPy implementation is labeled research-only.

### Current finding counts

These counts include historical findings that were fixed during this audit and residual documentation/architecture findings that remain open.

| Priority | Count | State |
|---|---:|---|
| P0 | 1 | fixed |
| P1 | 5 | fixed or materially mitigated |
| P2 | 6 | mixed: fixed and remaining limitations |
| P3 | 1 | fixed in current patch; CI verification pending |
| P4 | 3 | documentation mismatches remain |

No numerical repository score is assigned.

## Repositories inspected

### Mandatory security/AI-security scope

1. `mcp-agent-security-gateway`
2. `hf-model-provenance-scanner`
3. `aws-agent-identity-guard`
4. `llm-redteam-framework`
5. `adversarial-ml-lab`
6. `dataset-poisoning-detector`
7. `model-privacy-attacks`
8. `unified-ml-security-platform`
9. `attack-v19-core`
10. `attack-detection-engine`
11. `mlsec-benchmark-suite`
12. `mlsec-dashboards`
13. `ml-security-command-center`
14. `PulseNet-RUL-Forecasting`

### Additional account repositories classified outside the security audit scope

- `poojakira` — profile/report repository
- `poojakira.github.io` — portfolio/documentation site
- `Pooja_Kiran_Portfolio_Website` — portfolio website
- `Carrier` — private/non-security repository
- `pooja_carrier-website` — private career-site work

## Repository matrix

| Repository | Classification | Code | Security tests/evidence | Documentation | Benchmarks/evidence | Status |
|---|---|---|---|---|---|---|
| `mcp-agent-security-gateway` | Flagship runtime security repo | Substantive | Strong boundary tests; CI evidence | Extensive; some historical claims need rerun | Fixture/committed benchmarks | **VERIFIED WITH LIMITATIONS** |
| `hf-model-provenance-scanner` | Flagship supply-chain scanner | Substantive | Strong static-analysis tests | Narrow-claim language present | Fixture-scoped | **VERIFIED WITH LIMITATIONS** |
| `aws-agent-identity-guard` | Flagship cloud/IAM static analyzer | Substantive | Rule/test surface present | Correctly limits effective-permission claims | Rule corpus | **VERIFIED WITH LIMITATIONS** |
| `llm-redteam-framework` | Flagship adversarial AI-security harness | Substantive | API/auth/security tests present | Security configuration is correct; README has one stale auth paragraph | Historical benchmark artifacts | **VERIFIED WITH LIMITATIONS** |
| `adversarial-ml-lab` | ML-security research/attack lab | Substantive experimental harness | Large committed test surface; fresh run not completed | Readiness wording is broader than evidence | Historical synthetic benchmarks | **EXPERIMENTAL** |
| `dataset-poisoning-detector` | ML-security detection service | Substantive | REST + WebSocket auth tests exist | One stale source docstring remains | Controlled benchmarks | **VERIFIED WITH LIMITATIONS** |
| `model-privacy-attacks` | Privacy/security research | Substantive | New DP regression tests; latest CI rerun pending | Formal/non-formal DP scope corrected | Historical MIA/DP artifacts | **EXPERIMENTAL** |
| `unified-ml-security-platform` | Integration gateway/scaffold | Substantive | Header and gateway-auth tests | Shared-key limitation remains | Integration checks | **INTEGRATION SCAFFOLD** |
| `attack-v19-core` | Threat-intelligence data foundation | Substantive data package | Package/data validation surface | Versioned model, not runtime enforcement | Data artifacts | **VERIFIED WITH LIMITATIONS** |
| `attack-detection-engine` | Detection engine | Substantive | Test surface identified; fresh run unavailable | Requires current artifact reproduction | Detection evaluation | **VERIFIED WITH LIMITATIONS** |
| `mlsec-benchmark-suite` | Benchmark/research framework | Substantive | Benchmark tests present | Scoring framework corrected to avoid readiness labels | Benchmark artifacts | **EXPERIMENTAL** |
| `mlsec-dashboards` | Evidence/observability dashboard | Substantive presentation layer | Dashboard tests/evidence | Readiness language narrowed to local tool scope | Static committed evidence | **INTEGRATION SCAFFOLD** |
| `ml-security-command-center` | Static portfolio inventory | Small focused implementation | Unit-test surface; not a runtime security tool | Production-readiness claim removed | Static source inventory | **VERIFIED WITH LIMITATIONS** |
| `PulseNet-RUL-Forecasting` | Non-security ML application with security utilities | Substantive | Security utility tests exist; fresh run unavailable | Ledger security language corrected | ML application benchmarks | **EXPERIMENTAL** |

## Finding register

### SEC-001 — `model-privacy-attacks` aggregate-gradient pseudo-DP

**Severity:** P0 — fixed

**Problem:** The former `dp_sgd_step` clipped the aggregate batch gradient rather than clipping each example's contribution, then added Gaussian noise. A hand-written sampled-Gaussian accountant produced a formal-looking epsilon without validated accounting.

**Security impact:** A caller could incorrectly treat the mechanism as providing formal `(epsilon, delta)`-DP when the implementation did not support that conclusion.

**Root cause:** The mechanism and the privacy accountant were implemented independently without a trusted accounting boundary.

**Fix:**
- Legacy `dp_sgd_step()` now raises explicitly instead of performing pseudo-DP.
- The NumPy `DPSGD` path is retained only as a research mechanism demonstration and reports `epsilon=None` and `formal_guarantee=False`.
- Formal training now uses `PrivacyEngine.make_private()` or `make_private_with_epsilon()` through `make_private_training_components()`.
- `get_privacy_spent()` obtains epsilon from the configured accountant.
- Historical epsilon output is preserved but relabeled as an unverified historical artifact.

**Tests added:** `tests/test_dp_sgd_security.py`.

**Verification:** Latest CI patch is in progress after a first CI attempt caught only Ruff issues in the new patch. No formal epsilon result was claimed by this audit.

**Evidence:** the current defense code explicitly distinguishes formal Opacus-backed training from the research mechanism. fileciteturn93file0

**Remaining limitation:** The actual training run must use the returned private model, optimizer, and data loader consistently for the stated privacy accounting to apply.

### SEC-002 — `mcp-agent-security-gateway` client authorization denial could fail open

**Severity:** P1 — fixed

**Problem:** The client had `fail_closed=False` available and caught HTTP errors too broadly. An explicit 4xx authorization denial from a protected gateway could be interpreted as an availability failure and become allowed in fail-open mode.

**Fix:**
- Explicit 4xx responses are always blocking.
- 5xx responses and transport failures are the only failures governed by the explicit availability mode.
- Default remains `fail_closed=True`.
- Client sends `X-API-Key` when configured.

**Regression tests:** `tests/test_client.py` covers 400/401/403/429, 503, transport failure, API-key propagation, and guard-before-tool execution.

### SEC-003 — `mcp-agent-security-gateway` client/server authentication semantics were inconsistent

**Severity:** P1 — fixed

**Problem:** The protected API required API-key authentication while the client configuration did not make credential handling explicit and defaulted toward availability.

**Fix:** `GatewayClient(base_url, api_key=..., fail_closed=True)` is now explicit and safe by default. The server already rejects missing/invalid keys.

### SEC-004 — `llm-redteam-framework` authentication previously disabled when secret was absent

**Severity:** P1 — fixed in code

**Problem:** Earlier API behavior treated a missing `REDTEAM_API_KEY` as authentication disabled.

**Fix:** Current API code requires the secret for protected endpoints, uses `hmac.compare_digest`, and protects `/metrics` as well as `/scan`. `SECURITY_CONFIGURATION.md` is explicit that there is no anonymous production mode.

**Remaining documentation defect:** `README.md` still contains a stale historical paragraph saying a missing key disables authentication. The dedicated security configuration is authoritative and the README section should be reconciled in the next edit.

### SEC-005 — `unified-ml-security-platform` trust-boundary header forwarding

**Severity:** P1 — fixed

**Problem:** The gateway previously forwarded arbitrary caller headers to internal services.

**Fix:** Explicit allowlist now permits only intentionally selected request metadata; the gateway sets its own internal `X-API-Key`. Caller `Authorization`, `Cookie`, and caller `X-API-Key` do not cross the boundary.

**Regression tests:** `tests/test_gateway.py` now proves security-sensitive headers are excluded and gateway identity is injected.

**Additional hardening:** external API-key comparison now uses `hmac.compare_digest`.

**Remaining limitation:** one shared internal API key still creates shared blast radius. The repository should be described as a simplified integration architecture, not zero-trust service identity.

### SEC-006 — `dataset-poisoning-detector` WebSocket authentication documentation mismatch

**Severity:** P4 — open documentation defect

**Observed implementation:** `/stream` validates `X-API-Key` and rejects unauthorized connections; a regression test covers the behavior.

**Problem:** A module-level docstring still says WebSocket connections are unauthenticated.

**Required fix:** Remove the obsolete statement and keep the security configuration, implementation, and tests aligned.

### SEC-007 — `adversarial-ml-lab` readiness claims exceed current evidence

**Severity:** P2/P4 — open documentation reconciliation

**Problem:** `docs/TECHNICAL_REPORT.md` labels several attack/harness capabilities "production-ready" while the same project describes advanced modules as experimental and its evaluations as synthetic/small-model research.

**Required wording:** describe those components as research/benchmark capabilities until real deployment validation exists. Synthetic benchmark results must not be promoted to production claims.

### SEC-008 — `mlsec-benchmark-suite` composite score previously implied production readiness

**Severity:** P2 — fixed

**Fix:** `docs/SCORING_FRAMEWORK.md` now states that benchmark scores are measurement results only. Score ranges no longer map to "production-ready" or "best-in-class" and CI gates are explicitly benchmark gates rather than deployment approvals.

### SEC-009 — `mlsec-dashboards` readiness wording exceeded evidence

**Severity:** P2 — fixed

**Fix:** README now describes it as a local developer/portfolio evidence dashboard, not a production-facing service. Static benchmark output is explicitly distinguished from live monitoring.

### SEC-010 — `ml-security-command-center` readiness wording exceeded implementation scope

**Severity:** P2 — fixed

**Fix:** README now uses "Intended-Use Readiness Assessment" and states that the project is a bounded static source inventory. Test counts are not security-effectiveness measurements.

### SEC-011 — `PulseNet-RUL-Forecasting` audit ledger overstated integrity and failed silently on corruption

**Severity:** P1 within the ledger's audit scope — fixed

**Problems found:**
- Hash chaining was described as "tamper-proof" even though the implementation has no external trust anchor/signature/distributed immutability.
- Corrupt/unreadable persisted ledgers were silently replaced with a new genesis block, which could destroy evidence.
- Integrity validation did not validate the genesis block's own hash; rewriting the genesis contents and hash could evade a chain-link-only check.
- Persistence errors were swallowed.

**Fix:**
- Language changed from tamper-proof to tamper-evident.
- Genesis block is explicitly validated.
- Corrupt persisted ledgers raise `LedgerIntegrityError` instead of silently resetting.
- Persistence failures propagate as `LedgerIntegrityError`.
- Atomic temp-file write + `os.replace()` is used for persistence.

**Regression tests:** `tests/test_blockchain_integrity_regressions.py` covers tampered genesis, corrupt storage, and persistence failure.

**Remaining limitation:** The ledger remains locally tamper-evident, not cryptographically unforgeable against an operator who can rewrite both ledger state and trusted reference state.

### SEC-012 — `model-privacy-attacks` CI feedback on new patch

**Severity:** P3 — fixed in source, CI rerun pending

The first run of the new DP regression commit failed only on Ruff (`unused torch import` and one E501 line). Both were corrected in commit `500ce145eb59dcbabae19ff07622a7805013e09e`; the corresponding CI run was pending at the time of this report.

## Security-boundary review

For each runtime boundary, the audit used this model:

```text
Input
  -> Authentication
  -> Authorization
  -> Validation
  -> Policy evaluation
  -> Enforcement
  -> Logging/evidence
  -> Response
```

### `mcp-agent-security-gateway`

- **Input:** structured MCP tool-call payloads
- **Authentication:** API key at protected server boundary
- **Authorization:** policy/layer verdicts
- **Validation:** JSON/protocol/input guards
- **Policy evaluation:** multi-layer inspection
- **Enforcement:** client `guard()` raises `ToolBlocked` before real tool invocation
- **Failure mode:** fail closed by default for transport availability
- **Known trade-off:** shadow mode intentionally allows detector failures for monitoring deployments

### `llm-redteam-framework`

- **Authentication:** explicit API key for protected endpoints
- **Validation:** prompt-length and rate-limit controls
- **Enforcement semantics:** detector verdict blocks at the API response layer only; downstream tool/agent execution must still enforce the verdict

### `dataset-poisoning-detector`

- **Authentication:** REST API key and WebSocket API key
- **Enforcement:** unauthorized WebSocket upgrades are rejected
- **Known limitation:** in-memory rate limiting is process-local, not distributed

### `unified-ml-security-platform`

- **Authentication:** gateway API key
- **Authorization:** gateway dependency before proxying
- **Validation:** path service allowlist
- **Enforcement:** internal service identity is gateway-controlled; caller security headers are filtered
- **Known limitation:** shared internal key creates shared blast radius

## Test execution and verification record

### Verified through GitHub Actions during this audit

`mcp-agent-security-gateway`, commit `0f25219d0f20521382819654f8a267202febe304`:
- Ruff lint: success
- Ruff formatter check: success
- focused Pyright: success
- Bandit: success
- pip-audit: success
- CodeQL: success
- Windows control-plane job: success
- Python 3.10 tests: success
- Python 3.11 tests: success
- Python 3.12 tests: success
- security scanner job: success
- Docker build was still running at report time

`unified-ml-security-platform`, commit `80bb66ddd964ad08153b71490346b0ff0c00c3a8`:
- prior CI run completed successfully, including the header-boundary regression tests.
- new constant-time comparison commit `00226b719cfb933687b35d6145979d57fd6c8ca0` had a workflow in progress at report time.

`model-privacy-attacks`:
- commit `bf2fefd0863d50676a127f309b206c446b83653e` CI run was executed and failed at Ruff before tests could run; the failure was corrected.
- latest corrected commit `500ce145eb59dcbabae19ff07622a7805013e09e` had a new CI run pending/in progress at report time.

### Not executed locally in this environment

No local repository test suites were run because local git cloning/outbound network access was unavailable. Consequently the following are not claimed as locally executed:

- `python -m pytest -q`
- `python -m pytest --cov`
- `ruff check .`
- `ruff format --check .`
- `pip-audit`
- `python -m build`
- Docker/Compose validation
- Kubernetes validation
- Terraform validation
- complete cross-repository end-to-end tests

### Benchmark reproduction

No new benchmark numbers were generated by this audit. Existing benchmark artifacts are treated as historical or scoped evidence until fresh reproduction is performed.

## Files changed in the current audit

### `mcp-agent-security-gateway`
- `src/mcp_monitor/client.py`
- `tests/test_client.py`

Commits:
- `16446df24772aa2260790b83537f2d482e2ab8a9`
- `0f25219d0f20521382819654f8a267202febe304`

### `model-privacy-attacks`
- `src/privacy_attacks/defenses.py`
- `src/privacy_attacks/defenses/dp_sgd.py`
- `scripts/verify_epsilon.py`
- `results/epsilon_verification.json`
- `tests/test_dp_sgd_security.py`

Commits:
- `8d6c1471bb902331d4422cda549041a8cfc38eea`
- `414b3ddb70ca1f85eccd26ce5d5df09e60531ed2`
- `b1109039b1c46dc83a363e69b2e402950973b03e`
- `1cf506e81d0274d204a92876d3d4ac3925380c74`
- `bf2fefd0863d50676a127f309b206c446b83653e`
- `ddbbde7430223d7063a44ac6544d11e16d6c2a4d`
- `500ce145eb59dcbabae19ff07622a7805013e09e`

### `unified-ml-security-platform`
- `tests/test_gateway.py`
- `gateway_server.py`

Commits:
- `80bb66ddd964ad08153b71490346b0ff0c00c3a8`
- `00226b719cfb933687b35d6145979d57fd6c8ca0`

### `mlsec-dashboards`
- `README.md`

Commit:
- `b04e9563810ae7746a9e24afd0dca536c38274c2`

### `mlsec-benchmark-suite`
- `docs/SCORING_FRAMEWORK.md`

Commit:
- `df4a9d6a4fece4882e4c7643d45d0779a8cb7d1f`

### `ml-security-command-center`
- `README.md`

Commit:
- `c8bba4f062a86ca373649bf559ea04baa9998478`

### `PulseNet-RUL-Forecasting`
- `src/pulsenet/security/blockchain.py`
- `tests/test_blockchain_integrity_regressions.py`

Commits:
- `dcb79437063b1b0bd55657d96d2969a4a68171c9`
- `3f3f61721ad8d68f1d10188303b6452566d6fb8a`

## Remaining known limitations

1. `llm-redteam-framework/README.md` has a stale historical paragraph saying missing `REDTEAM_API_KEY` disables auth; the current code and `SECURITY_CONFIGURATION.md` are fail-closed.
2. `dataset-poisoning-detector` retains one stale source docstring describing `/stream` as unauthenticated.
3. `adversarial-ml-lab` technical reporting still has production-readiness wording that must be narrowed to experimental/research scope.
4. `unified-ml-security-platform` uses a shared internal API key, so service identity separation is simplified rather than zero-trust.
5. Fresh benchmark reproduction remains outstanding across the portfolio.
6. Historical git-secret scanning, complete cross-repo schema compatibility testing, and exhaustive workflow/action review remain outstanding.

## Portfolio security posture

### Runtime enforcement
- `mcp-agent-security-gateway`
- `unified-ml-security-platform` gateway

### Static analysis
- `hf-model-provenance-scanner`
- `aws-agent-identity-guard`

### Detection
- `dataset-poisoning-detector`
- `attack-detection-engine`

### Adversarial testing / research
- `llm-redteam-framework`
- `adversarial-ml-lab`
- `model-privacy-attacks`

### Threat intelligence / data foundation
- `attack-v19-core`

### Benchmark / evidence
- `mlsec-benchmark-suite`

### Observability / integration
- `mlsec-dashboards`
- `ml-security-command-center`

### Non-security ML
- `PulseNet-RUL-Forecasting`

## Portfolio conclusion

The strongest evidence for a Security Engineer / Detection Engineering / AI Security portfolio comes from projects where the security boundary is explicit and the evidence chain is inspectable: MCP gateway enforcement, AWS IAM analysis, HF model provenance, LLM red-team evaluation, and dataset-poisoning detection.

The privacy project is now technically more defensible because formal DP language is limited to the Opacus-backed path and the old pseudo-accountant cannot silently produce a formal-looking epsilon.

This report does **not** claim that every repository is fully verified or production-ready. The unresolved gap is primarily fresh execution/reproduction and a small set of stale documentation claims.
