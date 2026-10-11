# Resume Metrics Evidence

This page is the central evidence index for quantitative security-project claims used across Pooja Kiran's resume and portfolio. Exported or previously submitted resume snapshots may retain an older verified metric set; current repository/profile wording should use the latest **separately anchored** evidence recorded below.

Metrics below are tied to named repository snapshots or verification runs. A later repository commit may contain more tests or a different measurement; that does not invalidate an earlier dated snapshot. The historical poster snapshots below must be distinguished from the current October 2026 hosted results and from the older public resume PDF.


## October 11, 2026 latest inspected hosted results (not poster snapshots)

| Project | Main CI reference | Hosted test evidence | Scope |
|---|---|---|---|
| MCP Agent Security Gateway | [Run 38012954359](https://github.com/poojakira/mcp-agent-security-gateway/actions/runs/38012954359) | **782 passed, 81.93% coverage** (Python 3.12) | Current CI at cited commit; 69 named detector signatures from separate source inventory, not an independently validated detector recall |
| AWS Agent Identity Guard | [Run 38009457205](https://github.com/poojakira/aws-agent-identity-guard/actions/runs/38009457205) | **247 collected, 244 passed, 3 skipped** | Static IAM rules; credential-dependent tests not executed |
| HF Model Provenance Scanner | [Run 38002138828](https://github.com/poojakira/hf-model-provenance-scanner/actions/runs/38002138828) | **260 passed, 1 skipped, 6 subtests, 75.67% coverage** | 33/33 committed fixture detection is separate curated regression evidence |

The tracked portfolio resume cites a different dated Docker gateway snapshot (752 tests), while historical posters cite 723 tests. Neither should be described as the same test run as the newer 782-pass hosted CI. The published resume PDF must be regenerated together with its LaTeX source before changing PDF-facing numbers.

## Historical poster evidence (archived)

## MCP Agent Security Gateway

Cited historical 2026 poster snapshot values (not a test run of the latest commit):

- **723 passing tests**
- **81.91% statement coverage**
- **55 prompt-injection collection entries**
- **9 Elastic Security detection rules**
- **21 core SIEM tests**

Primary evidence: https://github.com/poojakira/mcp-agent-security-gateway/blob/main/VERIFIED_METRICS.md

Historical snapshots such as 622/78%, 641/79.54%, 659/82%, and 707/82.85% remain historical evidence only. They are not all the values used by the current canonical resume.

## AWS Agent Identity Guard

Cited 2026 verification snapshot values (not a test run of the latest commit):

- **25 deterministic rule IDs**
- **243 tests collected**
- **240 passed**
- **3 credential-gated skips**
- **SARIF 2.1.0 output**

Primary evidence: https://github.com/poojakira/aws-agent-identity-guard/blob/main/VERIFIED_METRICS.md

Repository performance figures are synthetic benchmark measurements and CI regression gates. They are not production throughput or latency SLOs.

## HF Model Provenance Scanner

Cited 2026 verification snapshot values (not a test run of the latest commit):

- **241 passing tests**
- **1 platform-specific skip**
- **6 additional pytest subtests**
- **75.67% statement coverage**
- **33/33 committed adversarial fixtures detected**
- **0 actionable findings across 4 committed benign samples**

Primary evidence: https://github.com/poojakira/hf-model-provenance-scanner/blob/main/VERIFIED_METRICS.md

Fixture results are regression evidence only. They are not universal detection or false-positive rates.

## Dataset Poisoning Detector

Cited 2026 verification snapshot values (not a test run of the latest commit):

- **200 passing tests**
- **91.20% statement coverage**
- **90% CI/release coverage floor**

Primary evidence: https://github.com/poojakira/dataset-poisoning-detector/blob/main/poster/03_verified_metrics.md and the repository's CI/evidence files.

Synthetic poisoning benchmark scores remain dataset- and configuration-scoped. They are not production detector accuracy claims.

## Account-wide repository-hardening wording

The October 9, 2026 account inventory found **21 repositories**, including the empty `aegis-immune-fabric` repository. Branch protection, required status checks, and workflow cadence are not uniform across the fleet; several private repositories intentionally use manual-only workflows to avoid unplanned hosted-runner usage.

Current resume/profile wording should therefore say that the portfolio uses protected-branch and CI/security controls where configured. It must not imply that every repository has identical merge-gate enforcement.

## Interview rule

1. Tie every metric to the repository snapshot or CI evidence that produced it.
2. Explain older values as historical validated snapshots when a repository has evolved.
3. Never describe fixture results as population-level detection accuracy.
4. Describe MCP Elastic rules as detection rules, not observed production incidents.
5. Describe AWS performance figures as synthetic CI/benchmark measurements, not production SLOs.
6. Do not claim that protected branches automatically require CI unless required status-check enforcement is actually configured.
