# CLAIM_AUDIT.md

Date: 2026-09-16

A claim is treated as verified only when implementation and evidence support the same scope. Historical, synthetic, fixture-only, and unexecuted claims are labeled accordingly.

| Repository | Claim | Evidence checked | Current status | Required wording |
|---|---|---|---|---|
| `mcp-agent-security-gateway` | Protected production API requires an API key | Production server auth + client API-key support | VERIFIED WITH LIMITED SCOPE | Protected production endpoints require a configured `X-API-Key` |
| `mcp-agent-security-gateway` | Client fails closed by default | `GatewayClient` + regression tests | VERIFIED IN SOURCE; CI TEST EVIDENCE AVAILABLE | Client defaults to fail-closed on gateway availability failure; explicit 4xx denials always block |
| `mcp-agent-security-gateway` | 100% detection | historical/self-test material | UNVERIFIED AS CURRENT REAL-WORLD PERFORMANCE | State the exact committed fixture/self-test scope only |
| `hf-model-provenance-scanner` | 100% detection/blocking | committed fixture suite | VERIFIED WITH LIMITED SCOPE | 100% on the named committed fixture suite; not universal detection |
| `hf-model-provenance-scanner` | provenance finding proves compromise | scanner semantics/limitations | NOT SUPPORTED | Identifies suspicious provenance indicators; does not prove compromise |
| `aws-agent-identity-guard` | static analyzer determines effective AWS permissions | documented static-policy scope | NOT SUPPORTED | Static policy analysis; effective permissions require AWS-side/runtime validation |
| `llm-redteam-framework` | protected API authentication | current API + `SECURITY_CONFIGURATION.md` | VERIFIED IN SOURCE | Protected endpoints fail closed when `REDTEAM_API_KEY` is absent or wrong |
| `llm-redteam-framework` | benchmark F1 = 0.97 | committed artifact/configuration | HISTORICAL/COMMITTED RESULT | 0.97 on the specified grouped split/configuration; no fresh reproduction in this audit |
| `adversarial-ml-lab` | production-ready attack suite | technical report + limitations | OVERSTATED | Research/measurement harness; advanced modules remain experimental unless separately validated |
| `dataset-poisoning-detector` | WebSocket stream is authenticated | `/stream` implementation + regression test | VERIFIED IN SOURCE | `/stream` requires `X-API-Key`; stale source docstring should be removed |
| `model-privacy-attacks` | formal DP-SGD | corrected Opacus path + disabled legacy path | VERIFIED WITH REQUIRED USAGE CONDITIONS | Formal DP-SGD only through Opacus-backed path with actual accountant output; NumPy path is research-only |
| `model-privacy-attacks` | historical epsilon 0.5429 is a formal bound | legacy artifact | INCORRECT / RETIRED | Historical unverified value only; do not cite as a privacy guarantee |
| `unified-ml-security-platform` | strong zero-trust service isolation | shared internal API key | NOT SUPPORTED | Simplified shared-key integration architecture |
| `mlsec-benchmark-suite` | benchmark composite score demonstrates production readiness | scoring framework | CORRECTED | Benchmark score/gate only; deployment readiness requires separate review/evidence |
| `mlsec-dashboards` | dashboards represent live security monitoring | static evidence architecture | NOT SUPPORTED | Static evidence dashboard; only MCP gateway has runtime capability when running |
| `ml-security-command-center` | test-declaration count is test coverage/effectiveness | AST source inventory | NOT SUPPORTED | Static source inventory; does not execute tests or measure effectiveness |
| `PulseNet-RUL-Forecasting` | SHA-256 ledger is tamper-proof | local hash chain only | INCORRECT / FIXED | Tamper-evident local integrity mechanism; not tamper-proof or immutable |

## Claim rules

- Synthetic, fixture-only, and historical results are labeled explicitly.
- A detector is not called an enforcement control unless the caller actually enforces the verdict.
- Static analysis is not described as runtime protection.
- Absence of provenance is not described as proof of maliciousness.
- Formal differential privacy is not claimed for the retired hand-written accountant.
- Benchmark scores are measurement outputs, not production approvals.
- A local hash chain is tamper-evident, not automatically tamper-proof.
