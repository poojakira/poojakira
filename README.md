<!-- Profile README for @poojakira -->

<p align="center">
  <img src="https://raw.githubusercontent.com/poojakira/poojakira/main/assets/profile-banner.svg" alt="Pooja Kiran — Security Engineering" width="100%" />
</p>

<h1 align="center">Pooja Kiran</h1>
<p align="center">
  <strong>Security Engineer · AI & Agent Security · Application Security · Cloud IAM</strong>
</p>

<p align="center">
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/">Portfolio</a> ·
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/Pooja_Kiran_Software_Engineer_Resume.pdf">Résumé</a> ·
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a>
</p>

I build security tooling for AI execution paths, workload identities, model supply chains, and security detection and investigation. My work focuses on practical policy enforcement, deterministic analysis, automated regression testing, and engineering evidence that can be independently inspected.

## Selected engineering work

The [evidence index](RESUME_METRICS_EVIDENCE.md) records local verification snapshots from November 18, 2026 America/Phoenix. Each number below belongs to an exact source commit. The four linked drafts contain work under review, and the archived release assessments record **PARTIAL**. Visit the PRs for current branch and review status.

### [Agent → Tool: MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)

Agent developers submit bounded MCP requests, change capability permissions, and inspect real fixed-child execution receipts and disposable tool-side state in a local policy workbench. Default-deny policy and execution outcomes remain distinct.

- **834 passed / 0 skipped · 81.80% local statement coverage** at source [`d2e7b6ea7c1a`](https://github.com/poojakira/mcp-agent-security-gateway/blob/d2e7b6ea7c1a1f9cb0fb71f73d0a692d8fa0410c/README.md).
- Broader MCP conformance, arbitrary-server OS containment, externally anchored audit, and deployment-specific privacy/recovery gates remain open.
- [Source-scoped manifest](https://raw.githubusercontent.com/poojakira/mcp-agent-security-gateway/4f83f01a3ed8aca5639143fe2179afb0f864f46e/release-evidence/manifest.json) · [PARTIAL release assessment](https://github.com/poojakira/mcp-agent-security-gateway/blob/4f83f01a3ed8aca5639143fe2179afb0f864f46e/release-evidence/RELEASE_ASSESSMENT.md) · [Draft review](https://github.com/poojakira/mcp-agent-security-gateway/pull/194)

### [Identity → Authority: AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)

Cloud developers review bounded IAM and trust policies through the actual static scanners, navigate statement evidence, compare policy edits, and export SARIF 2.1.0. The engine has **24 static checks plus 1 additional live-context check**; the local studio requires no AWS credentials.

- **272 passed / 3 skipped · 77.15% local statement coverage** at source [`abe1c0a1e595`](https://github.com/poojakira/aws-agent-identity-guard/blob/abe1c0a1e5953b18eae762a5c41f400ff677adb2/README.md).
- The **3 skips cover the absent legacy TestRulesModule API**, not missing AWS credentials. Static findings do not determine effective AWS permissions or prove exploitability.
- [Source-scoped manifest](https://raw.githubusercontent.com/poojakira/aws-agent-identity-guard/a396433a4070a0ddc68aa83f9b1093e87fc3224f/release-evidence/manifest.json) · [PARTIAL release assessment](https://github.com/poojakira/aws-agent-identity-guard/blob/a396433a4070a0ddc68aa83f9b1093e87fc3224f/release-evidence/RELEASE_ASSESSMENT.md) · [Draft review](https://github.com/poojakira/aws-agent-identity-guard/pull/75)

### [Artifact → Review: HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)

ML supply-chain reviewers compare supported local artifacts through a sealed static worker, inspecting hashes, metadata, structure, and concern evidence without loading a model.

- **317 passed / 3 skipped · 76.08% local statement coverage · 6 separate passing subtests** at source [`ab26ad5cd6fe`](https://github.com/poojakira/hf-model-provenance-scanner/blob/ab26ad5cd6fe28ae1b0986e20da46be9ebb2f27a/README.md).
- **Independent closing review is BLOCKED.** Static inspection does not establish publisher identity, training lineage, behavioral safety, model equivalence, or absence of backdoors.
- [Source-scoped manifest](https://raw.githubusercontent.com/poojakira/hf-model-provenance-scanner/ed25d66b72e374f86e2975930b0ed83b9acf3c09/release-evidence/manifest.json) · [PARTIAL release assessment](https://github.com/poojakira/hf-model-provenance-scanner/blob/ed25d66b72e374f86e2975930b0ed83b9acf3c09/release-evidence/RELEASE_ASSESSMENT.md) · [Draft review](https://github.com/poojakira/hf-model-provenance-scanner/pull/103)

### [Telemetry → Investigation: Attack Detection Engine / Aegis HealthSec](https://github.com/poojakira/attack-detection-engine)

Analysts import bounded synthetic FHIR AuditEvent data into a local React/FastAPI investigation workbench, inspect canonical detector/correlation evidence persisted in PostgreSQL, change thresholds, rerun the same dataset, and export checksummed reports. This is batch investigation.

- **332 passed / 0 skipped · 82.47% local line coverage** at source [`aa45efd2f9f7`](https://github.com/poojakira/attack-detection-engine/blob/aa45efd2f9f7e229a0ae7b7f8d77adac18d96e83/README.md).
- Hosted [CI run 44431212087](https://api.github.com/repos/poojakira/attack-detection-engine/actions/runs/44431212087) was **queued / NOT VERIFIED** at the November 19, 2026 18:12 UTC recheck. Hard parser/detector process deadlines, complete FHIR conformance, PHI/privacy/recovery/load approval, and hostile public hosting remain open.
- [Source-scoped manifest](https://raw.githubusercontent.com/poojakira/attack-detection-engine/875299dd6a7ed061df792d1150371c688383fc05/release-evidence/manifest.json) · [PARTIAL release assessment](https://github.com/poojakira/attack-detection-engine/blob/875299dd6a7ed061df792d1150371c688383fc05/release-evidence/RELEASE_ASSESSMENT.md) · [Draft review](https://github.com/poojakira/attack-detection-engine/pull/58)

The full browser interfaces run locally using each candidate README. Each assessment links a free guided notebook; its committed cells were executed locally, while the hosted Colab kernel remains **NOT VERIFIED**. There is no verified public hosted full security application. The notebooks and synthetic fixtures do not establish multi-user isolation, continuous monitoring, or production readiness.

## More security engineering

- [LLM Red-Team Framework](https://github.com/poojakira/llm-redteam-framework) — structured adversarial testing for LLM applications.
- [Dataset Poisoning Detector](https://github.com/poojakira/dataset-poisoning-detector) — dataset-integrity and poisoning analysis.
- [Adversarial ML Lab](https://github.com/poojakira/adversarial-ml-lab) — experiments and tests for adversarial machine learning.
- [ML Security Benchmark Suite](https://github.com/poojakira/mlsec-benchmark-suite) — evaluation harnesses for ML security.
- [Unified ML Security Platform](https://github.com/poojakira/unified-ml-security-platform) — integrated ML security tooling.

## Engineering toolkit

**Languages & platforms:** Python, Rust, C++, Bash, FastAPI, Docker, GitHub Actions, AWS  
**Security:** AI/LLM security, MCP/JSON-RPC, application security, IAM and least privilege, threat modeling, model supply-chain security  
**Testing & detection:** pytest, SARIF, CodeQL, Elastic Security, SIEM telemetry, automated regression testing

## Background

- **M.S., Information Technology**, Arizona State University (2026)
- IT Grader
- Business & Compliance Lead, AEROSEC academic technology externship (Aug–Dec 2025)

## Connect

- Portfolio: https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/
- LinkedIn: https://www.linkedin.com/in/poojakiran/
- Email: poojakiranbhardwaj@gmail.com

---

<sub>Metrics above are tied to exact candidate commits and immutable local-verification archives. They are not claims of production deployment, customer adoption, or universal detection effectiveness. Review each repository's scope, limitations, and license before reuse.</sub>
