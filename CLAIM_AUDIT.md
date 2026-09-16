# Claim Audit

Date: 2026-09-16

This document records high-value claims checked during the portfolio security audit. A claim is only treated as verified when implementation and evidence support the same scope.

| Repository | Claim | Evidence | Current status | Required wording |
|---|---|---|---|---|
| mcp-agent-security-gateway | production API requires API key | `src/mcp_monitor/production/server.py` validates `X-API-Key` | VERIFIED WITH LIMITED SCOPE | Protected production API requires configured key |
| mcp-agent-security-gateway | fail-closed operation | client now defaults to `fail_closed=True`; regression tests added | VERIFIED IN SOURCE, NOT EXECUTED LOCALLY | Client defaults to fail-closed when gateway is unavailable |
| mcp-agent-security-gateway | 100% detection | historical/self-test material | UNVERIFIED AS CURRENT REAL-WORLD PERFORMANCE | Report only the exact committed fixture/self-test scope |
| hf-model-provenance-scanner | 100% detection | committed fixture suites and limitation documents | VERIFIED WITH LIMITED SCOPE | 100% on the named committed fixture suite, not universal detection |
| hf-model-provenance-scanner | provenance finding proves compromise | scanner design/limitations | NOT SUPPORTED | Identifies suspicious provenance indicators; does not prove compromise |
| aws-agent-identity-guard | effective AWS permissions are determined statically | README explicitly limits scope | NOT SUPPORTED | Static IAM policy analysis; runtime/effective permissions require AWS-side validation |
| llm-redteam-framework | API authentication | `REDTEAM_API_KEY` check | VERIFIED IN SOURCE, NOT EXECUTED LOCALLY | Protected endpoints fail closed without a configured key |
| llm-redteam-framework | benchmark F1 0.97 | committed benchmark artifact referenced by README | HISTORICAL/COMMITTED RESULT | 0.97 on the specified grouped split/configuration |
| adversarial-ml-lab | production-ready attack suite | technical report readiness table | NEEDS EVIDENCE RECONCILIATION | Research/measurement harness; advanced modules remain lightly tested unless separately verified |
| dataset-poisoning-detector | WebSocket authentication | current `/stream` implementation + security test | VERIFIED IN SOURCE, NOT EXECUTED LOCALLY | `/stream` requires `X-API-Key` |
| model-privacy-attacks | formal DP-SGD | former implementation clipped aggregate gradient | INCORRECT (fixed) | Formal DP-SGD requires the corrected Opacus-backed training path and actual accountant result |
| unified-ml-security-platform | strong service isolation | shared API key across services | NOT SUPPORTED | Simplified shared-key integration architecture |
| attack-v19-core | ATT&CK v19 core data model | package metadata/version | VERIFIED WITH LIMITED SCOPE | Versioned ATT&CK v19 data/model package |
| mlsec-dashboards | security enforcement | dashboard role | NOT SUPPORTED | Observability/presentation layer, not an enforcement boundary |
| mlsec-benchmark-suite | benchmark result is current | artifact-dependent | UNVERIFIED UNTIL REPRODUCED | Historical committed result unless rerun and environment recorded |

## Rules applied

- Synthetic or fixture results are labeled as such.
- A detector is not called an enforcement control unless the caller actually enforces its verdict.
- Static analysis is not described as runtime protection.
- Absence of provenance is not described as proof of maliciousness.
- Formal DP is not claimed without a valid mechanism and accountant.
