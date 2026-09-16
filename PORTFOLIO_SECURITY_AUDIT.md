# Portfolio Security Audit

Date: 2026-09-16
Owner: `poojakira`

## Audit scope

The GitHub account currently exposes 20 repositories. The mandatory security/ML-security scope was 14 repositories:

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

Additional account repositories were classified as portfolio/site or non-security work rather than silently treating them as security projects.

## Important execution limitation

The GitHub connector permitted source inspection and direct commits, but this environment could not clone repositories with the local git client because outbound DNS/network access was unavailable. Therefore no local `pytest`, `ruff`, `pip-audit`, Docker, Kubernetes, Terraform, or build command is claimed as executed by this audit.

Any test result below that is described as existing evidence comes from committed repository artifacts or source inspection, not a fresh local execution.

## Executive summary

The audit found several material security/documentation issues and corrected the highest-confidence issues that could be fixed safely through the GitHub source interface.

### Severity counts

- P0: 1 confirmed correctness/security-claim issue: the former DP-SGD implementation was not DP-SGD because it clipped the aggregate batch gradient.
- P1: 3 confirmed boundary issues: MCP client authentication/default availability behavior, LLM red-team API fail-open authentication, and unified gateway header forwarding.
- P2: 2 confirmed documentation/semantic mismatches: stale WebSocket authentication documentation and stale DP-SGD documentation/claims.
- P3: 0 freshly executed build/test failures because local execution was unavailable.
- P4: multiple stale or overly broad claims identified for follow-up, especially benchmark/readiness wording.

## Repository matrix

| Repository | Classification | Code | Security boundary | Tests/evidence | Docs | Status |
|---|---|---|---|---|---|---|
| mcp-agent-security-gateway | Flagship security repo | substantive | API-key protected production server; client corrected | committed tests present; not freshly executed | extensive; some historical claim material | VERIFIED WITH LIMITATIONS |
| hf-model-provenance-scanner | Flagship security repo | substantive | provenance/static scanning | substantial committed evidence | limitations explicitly present | VERIFIED WITH LIMITATIONS |
| aws-agent-identity-guard | Flagship cloud/IAM security repo | substantive static analyzer | static policy analysis | tests present | explicitly says it cannot determine effective permissions | VERIFIED WITH LIMITATIONS |
| llm-redteam-framework | Flagship AI security/research repo | substantive | API key corrected to fail closed | security tests present; not freshly executed | corrected security config added | VERIFIED WITH LIMITATIONS |
| adversarial-ml-lab | ML security research repo | substantive benchmark harness | attack/evaluation boundary | 94-test claim exists in README; not freshly executed | several readiness claims require evidence review | EXPERIMENTAL |
| dataset-poisoning-detector | ML security detection service | substantive | REST auth and WebSocket auth implemented | WebSocket auth regression test exists | source docstring contains stale WebSocket statement | VERIFIED WITH LIMITATIONS |
| model-privacy-attacks | Privacy research repo | substantive | DP path corrected to Opacus-backed setup | new regression test added; not executed locally | DP documentation corrected | RESEARCH/EXPERIMENTAL |
| unified-ml-security-platform | Integration gateway | substantive scaffold | gateway auth enforced | gateway tests present; not freshly executed | shared-key architecture remains a limitation | INTEGRATION SCAFFOLD |
| attack-v19-core | ATT&CK data/model library | substantive data package | not a runtime security boundary | package metadata and migration docs inspected | versioned ATT&CK model | VERIFIED WITH LIMITATIONS |
| attack-detection-engine | Detection engine | substantive | detection-oriented | package/test surface identified; not freshly executed | needs current evidence verification | VERIFIED WITH LIMITATIONS |
| mlsec-benchmark-suite | Benchmark suite | benchmark/research | measurement boundary | benchmark artifacts require reproducibility checks | benchmark claims need artifact-level verification | RESEARCH/EXPERIMENTAL |
| mlsec-dashboards | Observability/dashboard | presentation/integration | depends on upstream controls | dashboard code present | should not be treated as enforcement | INTEGRATION SCAFFOLD |
| ml-security-command-center | Integration/dashboard | small private repo | architecture surface | not enough executable evidence exposed through current inspection | requires deeper local execution | UNVERIFIED |
| PulseNet-RUL-Forecasting | ML project, not primarily security | ML application | not a security control | private repository; not locally executable here | security portfolio relevance is limited | UNRELATED/ML |

## Confirmed findings and fixes

### SEC-001 — `model-privacy-attacks`: aggregate-gradient pseudo-DP

Severity: P0

The former `dp_sgd_step` computed one aggregate gradient over a batch, clipped that aggregate norm, then added Gaussian noise. Per-example clipping is required for the standard DP-SGD mechanism. Adding Gaussian noise to an aggregate gradient does not by itself establish `(epsilon, delta)`-DP.

**Fix:** the legacy function now raises explicitly instead of allowing a caller to mistake it for formal DP-SGD. A new `make_private_training_components()` path delegates per-example gradients, clipping, noise, and accounting to Opacus. `get_privacy_spent()` obtains epsilon from the actual accountant.

**Regression test:** `tests/test_dp_sgd_security.py` prevents the legacy implementation from silently returning a training result.

### SEC-002 — `mcp-agent-security-gateway`: GatewayClient authentication and fail-open default

Severity: P1

The production server requires `X-API-Key`, while the client did not provide a key and defaulted to fail-open. That made the integration path inconsistent with the protected production boundary.

**Fix:** `GatewayClient` now accepts `api_key`, sends `X-API-Key`, defaults to `fail_closed=True`, rejects non-positive timeouts, and treats an unavailable/authentication-failed gateway as blocking under the default mode.

**Regression tests:** client API-key propagation, fail-closed default, explicit fail-open opt-in, HTTP 401 blocking, and guard-before-tool-execution behavior.

### SEC-003 — `llm-redteam-framework`: missing API secret disabled authentication

Severity: P1

The API previously treated an absent `REDTEAM_API_KEY` as an anonymous deployment mode.

**Fix:** protected endpoints now fail closed when the secret is missing. Key comparison uses `hmac.compare_digest`. `/metrics` is also authenticated. The test suite was updated so rate-limit/input tests use an explicit test key and the missing-secret case expects 401.

### SEC-004 — `unified-ml-security-platform`: unrestricted upstream header forwarding

Severity: P1

The gateway copied the entire incoming request header set to internal services. This could propagate caller-controlled `Authorization`, `Cookie`, and other security-sensitive material across the trust boundary.

**Fix:** added an explicit request-header allowlist and injects the gateway's configured internal `X-API-Key`. Caller-supplied authentication material is not implicitly forwarded.

**Remaining limitation:** the architecture still uses one shared API key for internal services. This is a simplified integration architecture, not strong per-service identity or zero-trust authentication.

### SEC-005 — `dataset-poisoning-detector`: WebSocket authentication status

Current source inspection shows `/stream` already validates `X-API-Key` and rejects unauthorized upgrades with WebSocket close code 1008. A corresponding regression test exists.

However, the module-level security docstring still contains an obsolete statement saying WebSockets are unauthenticated. This is a documentation defect and should be cleaned in the next source edit.

## Claim audit highlights

- `mcp-agent-security-gateway`: historical 313-test/100%-coverage language is explicitly identified in its research report as stale and requiring re-run before current citation.
- `hf-model-provenance-scanner`: 100% detection claims are documented as narrow fixture/suite claims, not universal real-world detection. Keep that scope visible.
- `adversarial-ml-lab`: several capabilities are labeled production-ready in technical reporting even though the README describes advanced modules as experimental/lightly tested. Those readiness labels need artifact-level reconciliation before being treated as current production claims.
- `aws-agent-identity-guard`: documentation correctly distinguishes static policy analysis from effective AWS permissions and runtime validation.
- `model-privacy-attacks`: formal DP wording has been corrected to require Opacus-backed training; no fresh DP epsilon benchmark was produced by this audit.

## Test execution record

### Actually executed in this environment

No repository test suite was executed locally. The attempted git clone failed because the environment could not resolve `github.com`.

### Not executed

- `pytest`
- `pytest --cov`
- `ruff check`
- `ruff format --check`
- `pip-audit`
- `python -m build`
- Docker builds/compose validation
- Kubernetes validation
- Terraform validation
- full cross-repository end-to-end tests

Reason: local repository cloning/network access was unavailable.

## Files changed

### `mcp-agent-security-gateway`
- `src/mcp_monitor/client.py`
- `tests/test_client.py`

Commits:
- `e8e866b8d3c5a2da99dbd7dbc31699657b7895b6`
- `73cca8a08023191e0fd1aaf6b6b43d9ebdbb00de`

### `llm-redteam-framework`
- `src/redteam/api/app.py`
- `tests/test_api_security.py`
- `SECURITY_CONFIGURATION.md`

Commits:
- `d5f92bbb7450d378fb460e0f5edae0f5bc2351f9`
- `56cc80517264fee91da064f49506fada6c6bc563`
- `d5f1b4921f512a03ecb0d860a35f55405ee48d60`

### `model-privacy-attacks`
- `pyproject.toml`
- `src/privacy_attacks/defenses.py`
- `DP_SGD.md`
- `README.md`
- `tests/test_dp_sgd_security.py`

Commits:
- `9f4bb863d32fefa870b408c949f2cce85f8297b7`
- `57db67c8a0f14f79c15376e773967d7b838b4c98`
- `7f8d834ec836674e457036f4543252f71817f4b7`
- `81f1ec54dcff2272a28636d261d4ecdab1348f3f`
- `db2af97b09068de09ade333c39f0b5535af343b3`

### `unified-ml-security-platform`
- `gateway_server.py`

Commit:
- `7864d70ff832954cbec221b41f4e399cab7e06da`

## Remaining work

1. Re-run all repository test/lint/security/build commands from fresh clones in a network-enabled environment.
2. Reconcile stale documentation in `dataset-poisoning-detector` source docstrings.
3. Add/verify header-forwarding regression tests in `unified-ml-security-platform`.
4. Independently run and compare Opacus epsilon accounting for representative DP configurations.
5. Perform artifact-by-artifact benchmark reproduction for all repositories before citing current metrics.
6. Audit GitHub Actions permissions and action pinning repository-by-repository.
7. Audit historical git history for secrets where repository visibility and access make that appropriate.
8. Perform full cross-repository schema compatibility tests.

## Portfolio security posture

### Runtime enforcement
- `mcp-agent-security-gateway`
- `unified-ml-security-platform` gateway

### Static analysis
- `aws-agent-identity-guard`
- `hf-model-provenance-scanner`

### Detection
- `dataset-poisoning-detector`
- `attack-detection-engine`

### Adversarial testing/research
- `llm-redteam-framework`
- `adversarial-ml-lab`
- `model-privacy-attacks`

### Threat-intelligence/data foundation
- `attack-v19-core`

### Benchmarking/evidence
- `mlsec-benchmark-suite`

### Observability/integration
- `mlsec-dashboards`
- `ml-security-command-center`

### Non-security ML work
- `PulseNet-RUL-Forecasting`

## Bottom line

The strongest engineering evidence is concentrated in the MCP gateway, AWS agent identity guard, HF provenance scanner, LLM red-team framework, and dataset poisoning detector. The privacy repository is now more honest technically because the former pseudo-DP implementation cannot be mistaken for formal DP-SGD.

This audit deliberately does **not** claim that the portfolio is production-ready or that every repository is fully verified. The remaining gap is fresh execution and artifact-level reproduction, not cosmetic README polishing.
