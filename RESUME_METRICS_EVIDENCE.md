# Resume Metrics Evidence

This page is the central evidence index for quantitative security-project claims used across Pooja Kiran's resume and portfolio. Exported or previously submitted resume snapshots may retain an older verified metric set; current repository/profile wording should use the latest cited evidence below.

Metrics below are tied to named repository snapshots or verification runs. A later repository commit may contain more tests or a different measurement; that does not invalidate an earlier dated snapshot, but current resume wording should use the current evidence set documented here.

## MCP Agent Security Gateway

Current repository evidence values:

- **723 passing tests**
- **81.91% statement coverage**
- **55 prompt-injection collection entries**
- **9 Elastic Security detection rules**
- **21 core SIEM tests**

Primary evidence: https://github.com/poojakira/mcp-agent-security-gateway/blob/main/VERIFIED_METRICS.md

Historical snapshots such as 622/78%, 641/79.54%, 659/82%, and 707/82.85% remain historical evidence only. They are not the values used by the current resume.

## AWS Agent Identity Guard

Current repository evidence values:

- **25 deterministic rule IDs**
- **243 tests collected**
- **240 passed**
- **3 credential-gated skips**
- **SARIF 2.1.0 output**

Primary evidence: https://github.com/poojakira/aws-agent-identity-guard/blob/main/VERIFIED_METRICS.md

Repository performance figures are synthetic benchmark measurements and CI regression gates. They are not production throughput or latency SLOs.

## HF Model Provenance Scanner

Current repository evidence values:

- **241 passing tests**
- **1 platform-specific skip**
- **6 additional pytest subtests**
- **75.67% statement coverage**
- **33/33 committed adversarial fixtures detected**
- **0 actionable findings across 4 committed benign samples**

Primary evidence: https://github.com/poojakira/hf-model-provenance-scanner/blob/main/VERIFIED_METRICS.md

Fixture results are regression evidence only. They are not universal detection or false-positive rates.

## Dataset Poisoning Detector

Current repository evidence values:

- **200 passing tests**
- **91.20% statement coverage**
- **90% CI/release coverage floor**

Primary evidence: https://github.com/poojakira/dataset-poisoning-detector/blob/main/poster/03_verified_metrics.md and the repository's CI/evidence files.

Synthetic poisoning benchmark scores remain dataset- and configuration-scoped. They are not production detector accuracy claims.

## Account-wide repository-hardening wording

The account currently contains **22 repositories**. Branch protection, required status checks, and workflow cadence are not uniform across the fleet; several private repositories intentionally use manual-only workflows to avoid unplanned hosted-runner usage.

Current resume/profile wording should therefore say that the portfolio uses protected-branch and CI/security controls where configured. It must not imply that every repository has identical merge-gate enforcement.

## Interview rule

1. Tie every metric to the repository snapshot or CI evidence that produced it.
2. Explain older values as historical validated snapshots when a repository has evolved.
3. Never describe fixture results as population-level detection accuracy.
4. Describe MCP Elastic rules as detection rules, not observed production incidents.
5. Describe AWS performance figures as synthetic CI/benchmark measurements, not production SLOs.
6. Do not claim that protected branches automatically require CI unless required status-check enforcement is actually configured.
