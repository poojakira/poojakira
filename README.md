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
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/Pooja_Kiran_Agentic_AI_Security_Engineer_Resume.pdf">Technical Resume</a> ·
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a>
</p>

I build security tooling for AI execution paths, workload identities, model supply chains, and security detection and investigation. My work focuses on practical policy enforcement, deterministic analysis, automated regression testing, and engineering evidence that can be independently inspected.

## Selected engineering work

### Agent → Tool: [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)
Default-deny MCP/JSON-RPC request gateway that inspects selected agent-to-tool calls before execution, with capability authorization, prompt-injection inspection, sensitive-data/exfiltration checks, anti-SSRF controls, rate limiting, tamper-evident audit records, and SIEM integration.

- **782 passing tests · 81.93% coverage** (statement) in a dated hosted Python 3.12 CI run.
- **69 named runtime detector signatures** and nine Elastic Security rules (source-inventory counts, not real-world detection rates).
- [CI evidence](https://github.com/poojakira/mcp-agent-security-gateway/actions/runs/38012954359) · [Repository](https://github.com/poojakira/mcp-agent-security-gateway)

### Identity → Authority: [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)
Static AWS IAM policy analysis with 25 deterministic rule IDs covering excessive permissions, role trust, privilege-escalation paths, and audit-control weaknesses. Exports text, JSON, and SARIF 2.1.0 findings.

- **244 passed / 3 skipped** in a dated CI run; skipped checks require live AWS credentials.
- [CI evidence](https://github.com/poojakira/aws-agent-identity-guard/actions/runs/38009457205) · [Repository](https://github.com/poojakira/aws-agent-identity-guard)

### Artifact → Runtime: [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Non-executing inspection of supported model artifacts, serialization risks, provenance, and dependency evidence. 

- **260 passed / 1 skipped · 75.67% coverage** in a dated CI run.
- **33/33 adversarial fixtures flagged** (curated) in a bounded evaluation; this is fixture evidence, not a general detection guarantee.
- [CI evidence](https://github.com/poojakira/hf-model-provenance-scanner/actions/runs/38002138828) · [Repository](https://github.com/poojakira/hf-model-provenance-scanner)


### [Attack Detection Engine / Aegis HealthSec](https://github.com/poojakira/attack-detection-engine) — Telemetry → Investigation

A rule-based, multi-domain security engine covering ATT&CK-oriented telemetry, offline CAN/firmware/ARM lab analysis, and a developing healthcare investigation workflow. The **unmerged development branches** add clinical-access detection, PostgreSQL persistence, deterministic correlation, a FastAPI investigation API, analyst audit history, and a React SOC console. The healthcare examples use synthetic access events; MIMIC-IV Demo contributes de-identified clinical context, not actual hospital security logs or authorization decisions.

- **Milestone C, October 27, 2026:** 212 tests passed in an isolated Python 3.12.3 environment with real PostgreSQL integration; a Docker Compose investigation scenario was also reported as passing. See [PR #48](https://github.com/poojakira/attack-detection-engine/pull/48) and [Milestone C report](https://github.com/poojakira/attack-detection-engine/blob/feat/milestone-c-platform/MILESTONE_C_FINAL_REPORT.md).
- **Milestone D, October 27, 2026:** 280 local tests reported after authentication, tenant-isolation, container, audit-integrity and supply-chain hardening; see [PR #49](https://github.com/poojakira/attack-detection-engine/pull/49) and its underlying branch. **Hosted CI is blocked because repository Actions are disabled.**
- **FHIR R4 AuditEvent connector:** additional implementation and 296-test local result reported by the coding agent, **not yet pushed or independently available on GitHub** as of this update. Do not treat this as released connector support. CloudTrail, Sysmon, auditd, and Ruby/Go/Swift/Java/.NET SAST remain planned.

[Healthcare detection PR #47](https://github.com/poojakira/attack-detection-engine/pull/47) · [Investigation PR #48](https://github.com/poojakira/attack-detection-engine/pull/48) · [Hardening PR #49](https://github.com/poojakira/attack-detection-engine/pull/49)

**Scope:** Synthetic security telemetry, bounded test evidence, and controlled local/container evaluation only; no customer deployment, real-world detection-rate measurement, HIPAA certification, or production-readiness claim. The `main` branch still reflects the earlier offline detection engine until the stacked PRs are reviewed and merged.

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
- Graduate Teaching Assistant and IT Grader
- Business & Compliance Lead, AEROSEC academic technology externship (Aug–Dec 2025)

## Connect

- Portfolio: https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/
- LinkedIn: https://www.linkedin.com/in/poojakiran/
- Email: poojakiranbhardwaj@gmail.com

---

<sub>Metrics above are tied to specific dated CI runs or bounded fixture sets. They are not claims of production deployment, customer adoption, or universal detection effectiveness. Review each repository's scope, limitations, and license before reuse.</sub>
