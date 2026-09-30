# Pooja Kiran — Security Engineer

I build **security infrastructure for AI agents, cloud identities, and model supply chains**.

My work focuses on three security boundaries:

**agent → tool execution** · **identity → authorization** · **model artifact → load**

I build the controls, tests, and evidence needed to make those boundaries measurable and reproducible.

## Start here

### [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)
Inline MCP/JSON-RPC inspection for agent tool calls, with policy decisions, prompt-injection signals, audit logging, telemetry, and a local Elastic detection lab.

- Current verified baseline: **707 passing tests, 82.85% statement coverage** (Python 3.12; the same suite is green on Python 3.10 and 3.11 in GitHub Actions)
- Evidence: [VERIFIED_METRICS.md](https://github.com/poojakira/mcp-agent-security-gateway/blob/main/VERIFIED_METRICS.md)
- Scope: production-oriented security gateway; enforcement applies only to traffic routed through a supported integration path

### [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)
Static IAM analysis for AI-agent and tool-executor roles, including identity-policy, trust-policy, and permission-boundary checks.

- **25 deterministic rule IDs**
- Fresh CI evidence: **235 passed, 3 skipped**
- Performance is reported as a synthetic CI gate, not production throughput
- Evidence: [VERIFIED_METRICS.md](https://github.com/poojakira/aws-agent-identity-guard/blob/main/VERIFIED_METRICS.md)

### [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Pre-load scanning for model repositories, including pickle-risk, provenance, impersonation, and model-supply-chain signals.

- Fixture-scoped detection evidence is documented in the repository
- No claim of real-world detection rate or commercial scanner parity
- Evidence: [VERIFIED_METRICS.md](https://github.com/poojakira/hf-model-provenance-scanner/blob/main/VERIFIED_METRICS.md)

The portfolio site is live, and the public `Pooja_Kiran_Portfolio_Website` repository now contains the Next.js/TypeScript site source plus the tracked resume PDF. Website claims should still be checked against the underlying project evidence rather than inferred from presentation copy.

## Six-project security portfolio

| Project | Security boundary |
|---|---|
| [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway) | Agent/tool execution |
| [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard) | Cloud identity & authorization |
| [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Model supply chain |
| [LLM Red Team Framework](https://github.com/poojakira/llm-redteam-framework) | Adversarial evaluation |
| [Dataset Poisoning Detector](https://github.com/poojakira/dataset-poisoning-detector) | Data/ML security |
| [Adversarial ML Lab](https://github.com/poojakira/adversarial-ml-lab) | Adversarial robustness |

## Supporting work

- [ML Security Benchmark Suite](https://github.com/poojakira/mlsec-benchmark-suite) — cross-project regression and fixture harness
- [ATT&CK v19 Core](https://github.com/poojakira/attack-v19-core) — shared ATT&CK v19 mapping utilities
- [Unified ML Security Platform](https://github.com/poojakira/unified-ml-security-platform) — deployable integration gateway and normalized service topology for the security tools above

## Research poster collection — *Security Systems*

Each project has a technical research poster (36 × 48 in) following IEEE-style research-poster information architecture: problem, threat model, one research question, hero architecture, methodology, verified evidence, honest negative results, security boundary, limitations, and reproducibility. Metrics are tied to named evidence snapshots. A poster printed at an older commit is a dated result, not a fresh measurement of the latest `main`; project evidence files carry newer baselines where available. *These are engineering research posters, not IEEE submissions — no affiliation or endorsement is claimed.*

| # | Poster | Repository |
|---|---|---|
| 01 | Runtime Policy Enforcement at the AI Agent-to-Tool Boundary | [poster](https://github.com/poojakira/mcp-agent-security-gateway#research-poster) · [PDF](https://github.com/poojakira/mcp-agent-security-gateway/blob/main/poster/poster_36x48.pdf) |
| 02 | Static Security Analysis of AWS IAM Policies for AI Workload Identities | [poster](https://github.com/poojakira/aws-agent-identity-guard#research-poster) · [PDF](https://github.com/poojakira/aws-agent-identity-guard/blob/main/poster/poster_36x48.pdf) |
| 03 | Non-Executing Security Analysis of AI Model Supply-Chain Artifacts | [poster](https://github.com/poojakira/hf-model-provenance-scanner#research-poster) · [PDF](https://github.com/poojakira/hf-model-provenance-scanner/blob/main/poster/poster_36x48.pdf) |
| 04 | Statistical Screening for Poisoned ML Training Data | [poster](https://github.com/poojakira/dataset-poisoning-detector#research-poster) · [PDF](https://github.com/poojakira/dataset-poisoning-detector/blob/main/poster/poster_36x48.pdf) |
| 05 | Evaluating an Offline Detector Against Adversarial Prompt Attacks | [poster](https://github.com/poojakira/llm-redteam-framework#research-poster) · [PDF](https://github.com/poojakira/llm-redteam-framework/blob/main/poster/poster_36x48.pdf) |
| 06 | Measuring Neural-Network Robustness Under Adversarial Perturbation | [poster](https://github.com/poojakira/adversarial-ml-lab#research-poster) · [PDF](https://github.com/poojakira/adversarial-ml-lab/blob/main/poster/poster_36x48.pdf) |
| 07 | A Unified Control Plane for ML Security Services | [poster](https://github.com/poojakira/unified-ml-security-platform#research-poster) · [PDF](https://github.com/poojakira/unified-ml-security-platform/blob/main/poster/poster_36x48.pdf) |
| 08 | Version-Aware Normalization of Findings Against MITRE ATT&CK v19 | [poster](https://github.com/poojakira/attack-v19-core#research-poster) · [PDF](https://github.com/poojakira/attack-v19-core/blob/main/poster/poster_36x48.pdf) |
| 09 | Reproducible Regression Harness for ML Security Tools | [poster](https://github.com/poojakira/mlsec-benchmark-suite#research-poster) · [PDF](https://github.com/poojakira/mlsec-benchmark-suite/blob/main/poster/poster_36x48.pdf) |
| 10 | Evidence-Centered Visualization for ML Security Engineering | [poster](https://github.com/poojakira/mlsec-dashboards#research-poster) · [PDF](https://github.com/poojakira/mlsec-dashboards/blob/main/poster/poster_36x48.pdf) |

## What I care about

- **Agent security:** MCP, tool-call security, prompt injection, authorization, data-flow controls, and execution boundaries
- **Cloud security:** AWS IAM, policy analysis, least privilege, and agent/tool identity
- **AI/ML security:** adversarial testing, model provenance, poisoning, and security evaluation; model-privacy source is currently private
- **Security engineering:** Python, FastAPI, Docker, CI, testing, telemetry, and reproducible security controls; Kubernetes deployment manifests are present for selected projects, without a claim of live cluster operation

## Repository security

This profile repository is documentation-only; it does not run an API, database, authentication system, payment flow, or upload endpoint. Repository-level hardening is enforced through read-only/pinned GitHub Actions, secret-file and token scanning, CODEOWNERS, Dependabot, and CI policy checks.

- [Security checklist](SECURITY_CHECKLIST.md)
- [Security audit](SECURITY_AUDIT_2026-09-30.md)
- [Recovery runbook](RUNBOOK.md)
- [Security policy](SECURITY.md)

## Engineering principles

- **Attach scope to every metric.** A test count, F1 score, or latency number is incomplete without the environment and dataset.
- **Separate detection from enforcement.** A component that returns a decision is not a firewall unless it actually controls execution.
- **Prefer reproducible evidence over adjectives.** CI, committed fixtures, and explicit limitations carry more weight than "production-ready."
- **Treat failure modes as part of the design.** Security behavior during parse errors, unavailable dependencies, and incomplete scans is documented and tested.

## Research and publications

- [A Personalized E-Learning System Using Reinforcement Learning Through Satellite](https://ieeexplore.ieee.org/document/10440852) — IEEE INDICON 2023 proceedings
- [Smart Charge Pro: Empowering Future Mobility With Advanced Safety And Efficiency In Electric Vehicle Charging Infrastructure](https://www.iosrjournals.org/iosr-jce/pages/25(4)Series-1.html) — IOSR-JCE, 2023

## Explore the work

If you're interested in **AI agent security, MCP security, cloud IAM, adversarial ML, or model supply-chain security**, start with the flagship projects above, reproduce the tests, open an issue, or contribute a fix.

- Portfolio: https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/
- LinkedIn: https://www.linkedin.com/in/poojakiran/
- Provenance ledger: [PROVENANCE_LEDGER.md](PROVENANCE_LEDGER.md)

<sub>Quantitative claims above are intentionally limited to values with repository-level evidence.</sub>

<!-- repo-verification:start -->
## Verification update — 2026-09-30

- **Scope:** Account-wide `poojakira` repository pass covering source/configuration, CI/release workflows, security-hygiene gates, dependency/SAST controls, and documentation consistency.
- **Remediation:** Reviewed profile workflows and documentation surfaces; no repository-controlled defect required a code change in this pass.
- **Verification state:** Latest completed Profile CI, Production Gate, Security Hygiene, and Documentation Integrity checks were green.
- **Security note:** Keep claims tied to repository evidence and avoid presenting portfolio metrics as production/customer metrics.
- **Evidence boundary:** This update records repository and GitHub Actions evidence observed during the pass. It is not a claim of independent penetration testing, production deployment, or zero residual risk.
<!-- repo-verification:end -->
