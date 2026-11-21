# Resume Metrics Evidence

This is the active evidence index for the four security-project claims in the profile, portfolio, and canonical résumés. The current local-verification archives were assembled November 18, 2026 (America/Phoenix; November 19 UTC). They identify exact reviewed candidate commits and retain original logs, environments, individual testcase inventories, skip reasons, browser evidence, limitations, and hashes. These results are not new executions by the profile's content verifier.

## Current reviewed candidates — November 18, 2026

**All four products remain PARTIAL.** Their draft PRs are unmerged. Local tests, a browser workflow, and an available notebook do not by themselves establish deployment readiness or field effectiveness. The full browser interfaces run locally; no verified public hosted full security app is claimed. Committed notebook cells passed locally, while hosted Colab execution remains NOT VERIFIED.

[evidence/portfolio_metrics.json](evidence/portfolio_metrics.json) binds each row to a full source SHA and an immutable archive commit. [scripts/verify_metrics_manifest.py](scripts/verify_metrics_manifest.py) checks schema, exact source/archive URL shapes, separate subtest counts, release scope, historical snapshot integrity, and agreement with the current profile and table. It does not independently execute product tests, attest GitHub logs, validate every external link, or replace release acceptance.

| Project | Exact reviewed source | Bounded local full-suite result | Immutable archive |
|---|---|---|---|
| MCP Agent Security Gateway | [`d2e7b6ea7c1a1f9cb0fb71f73d0a692d8fa0410c`](https://github.com/poojakira/mcp-agent-security-gateway/blob/d2e7b6ea7c1a1f9cb0fb71f73d0a692d8fa0410c/README.md) | **834 passed / 0 skipped · 81.80% local statement coverage** | [Manifest](https://raw.githubusercontent.com/poojakira/mcp-agent-security-gateway/4f83f01a3ed8aca5639143fe2179afb0f864f46e/release-evidence/manifest.json) · [PARTIAL assessment](https://github.com/poojakira/mcp-agent-security-gateway/blob/4f83f01a3ed8aca5639143fe2179afb0f864f46e/release-evidence/RELEASE_ASSESSMENT.md) |
| AWS Agent Identity Guard | [`abe1c0a1e5953b18eae762a5c41f400ff677adb2`](https://github.com/poojakira/aws-agent-identity-guard/blob/abe1c0a1e5953b18eae762a5c41f400ff677adb2/README.md) | **272 passed / 3 skipped · 77.15% local statement coverage** | [Manifest](https://raw.githubusercontent.com/poojakira/aws-agent-identity-guard/a396433a4070a0ddc68aa83f9b1093e87fc3224f/release-evidence/manifest.json) · [PARTIAL assessment](https://github.com/poojakira/aws-agent-identity-guard/blob/a396433a4070a0ddc68aa83f9b1093e87fc3224f/release-evidence/RELEASE_ASSESSMENT.md) |
| HF Model Provenance Scanner | [`ab26ad5cd6fe28ae1b0986e20da46be9ebb2f27a`](https://github.com/poojakira/hf-model-provenance-scanner/blob/ab26ad5cd6fe28ae1b0986e20da46be9ebb2f27a/README.md) | **317 passed / 3 skipped · 76.08% local statement coverage · 6 separate passing subtests** | [Manifest](https://raw.githubusercontent.com/poojakira/hf-model-provenance-scanner/ed25d66b72e374f86e2975930b0ed83b9acf3c09/release-evidence/manifest.json) · [PARTIAL assessment](https://github.com/poojakira/hf-model-provenance-scanner/blob/ed25d66b72e374f86e2975930b0ed83b9acf3c09/release-evidence/RELEASE_ASSESSMENT.md) |
| Attack Detection Engine / Aegis HealthSec | [`aa45efd2f9f7e229a0ae7b7f8d77adac18d96e83`](https://github.com/poojakira/attack-detection-engine/blob/aa45efd2f9f7e229a0ae7b7f8d77adac18d96e83/README.md) | **332 passed / 0 skipped · 82.47% local line coverage** | [Manifest](https://raw.githubusercontent.com/poojakira/attack-detection-engine/875299dd6a7ed061df792d1150371c688383fc05/release-evidence/manifest.json) · [PARTIAL assessment](https://github.com/poojakira/attack-detection-engine/blob/875299dd6a7ed061df792d1150371c688383fc05/release-evidence/RELEASE_ASSESSMENT.md) |

The rounded percentages above come from the full precision values in the manifest; coverage is local statement/line coverage, not hosted-run coverage. Separate subtests and focused/browser checks are not added to individual full-suite totals.

- **MCP:** bounded capability decisions and real fixed-child execution are demonstrated. Full MCP conformance, arbitrary-server OS containment, PII filtering, externally anchored audit, and deployment-specific operations remain open.
- **IAM:** **24 static checks plus 1 additional live-context check**. The **3 skips cover the absent legacy TestRulesModule API**, not missing AWS credentials. Effective AWS permissions, complete policy intersections, exploitability, and public deployment remain unproven.
- **HF:** **independent closing review is BLOCKED**. Static artifact inspection does not prove publisher identity, training lineage, behavioral safety, semantic equivalence, or absence of backdoors. Large-artifact and deployment acceptance remain open.
- **Aegis:** [CI run 44431212087](https://github.com/poojakira/attack-detection-engine/actions/runs/44431212087) was **queued / NOT VERIFIED** when rechecked November 19, 2026 at 18:12 UTC. No hosted passing artifact is claimed. The local persisted workflow uses synthetic inputs; hard parser/detector process deadlines, full FHIR conformance, PHI/privacy/recovery/load approval, and hostile public hosting remain open.

The assessments document full reviewed local-ref/history scanning for the four products, including recovery refs. No confirmed provider key was found in that reviewed scope; this is not an absolute guarantee about every credential, provider revocation, inaccessible ref, log, or artifact.

## Historical October 12, 2026 profile snapshot

The original three-project JSON is preserved byte-for-byte at [evidence/portfolio_metrics_2026-10-12.json](evidence/portfolio_metrics_2026-10-12.json). Its SHA256 is tracked in the active manifest. Its test numbers are dated snapshot records, not current-source results. The original IAM note incorrectly described the skips as AWS-credential-dependent and classified all 25 checks as static; current source distinguishes 24 static checks and one additional live-context check.

The following run identifiers and values were recorded by the older profile. They have not been freshly reproduced in this profile correction. Link labels now agree with their URL identifiers.

| Project | Historical hosted reference | Recorded snapshot values |
|---|---|---|
| MCP Agent Security Gateway | [Run 38012954359](https://github.com/poojakira/mcp-agent-security-gateway/actions/runs/38012954359) | 782 passed, 81.93% coverage (Python 3.12); 69 detector signatures were a separate source inventory |
| AWS Agent Identity Guard | [Run 38009457205](https://github.com/poojakira/aws-agent-identity-guard/actions/runs/38009457205) | 247 collected, 244 passed, 3 skipped; the original credential-skip explanation is retired |
| HF Model Provenance Scanner | [Run 38002138828](https://github.com/poojakira/hf-model-provenance-scanner/actions/runs/38002138828) | 260 passed, 1 skipped, 6 separate subtests, 75.67% coverage; 33/33 curated fixture result was separate |

Previously submitted résumé versions and posters contain additional dated snapshots. They must not be relabeled as results from the current candidate commits.

## Historical poster and résumé records

These are earlier recorded values retained for chronology, not fresh validation of current source. Repository `VERIFIED_METRICS.md` links below are mutable indexes; use the immutable current archive above for today's candidate claims.

| Project | Historical values | Repository index |
|---|---|---|
| MCP Agent Security Gateway | 723 tests; 81.91% coverage; 55 injection-collection entries; 9 Elastic rules; 21 core SIEM tests. Other historical test/coverage records include 622/78%, 641/79.54%, 659/82%, 707/82.85%, and a 752-test Docker résumé snapshot. | [Historical metrics index](https://github.com/poojakira/mcp-agent-security-gateway/blob/main/VERIFIED_METRICS.md) |
| AWS Agent Identity Guard | 243 collected, 240 passed, 3 skipped; SARIF 2.1.0. Older wording called all 25 checks static and the skips credential-gated; those interpretations must not be carried into current claims. | [Historical metrics index](https://github.com/poojakira/aws-agent-identity-guard/blob/main/VERIFIED_METRICS.md) |
| HF Model Provenance Scanner | 241 passed; 1 platform-specific skip; 6 additional subtests; 75.67% coverage; 33/33 curated adversarial fixtures; 0 actionable findings in 4 committed benign samples. | [Historical metrics index](https://github.com/poojakira/hf-model-provenance-scanner/blob/main/VERIFIED_METRICS.md) |
| Dataset Poisoning Detector | 200 tests; 91.20% coverage; 90% CI/release coverage floor. | [Historical poster index](https://github.com/poojakira/dataset-poisoning-detector/blob/main/poster/03_verified_metrics.md) |

Fixture results are regression evidence. Synthetic benchmark latency, throughput, and poisoning scores are scoped measurements; none establishes population-level detector accuracy or a production SLO.

## Account-wide repository-hardening wording

The October 12, 2026 connected-account inventory recorded 20 repositories (14 public, 6 private). The October 9 inventory recorded 21, including the then-empty `aegis-immune-fabric`. Both are historical inventories. They are not a current account count or an attestation of uniform controls.

Branch protection, required status checks, and workflow cadence vary by repository. Several private repositories intentionally use manual-only workflows to avoid unplanned hosted-runner usage. State that protected-branch and CI/security controls apply where configured; do not imply every repository has identical merge-gate enforcement.

## Interview rule

1. Tie every metric to the source snapshot and evidence that produced it.
2. Keep historical counts separate from current candidate results.
3. Describe fixture detection as bounded regression evidence, not population-level accuracy.
4. Describe MCP Elastic rules as detection rules, not observed production incidents.
5. Describe AWS benchmarks as synthetic measurements, not production SLOs.
6. Require observed platform settings before claiming protected branches or enforced CI gates.
