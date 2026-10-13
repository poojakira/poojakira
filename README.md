> **READ THIS LICENSE BEFORE COPYING, USING, OR MODIFYING ANY MATERIAL.** This repository's owner-controlled original content is proprietary and **All Rights Reserved**. There is no permission to copy, modify, distribute, or reuse it without prior written authorization, subject to existing third-party rights, any prior valid licenses, GitHub's Terms, and applicable law. See [LICENSE](LICENSE).

<p align="center">
  <img src="./assets/profile-banner.svg" width="100%" alt="Pooja Kiran, Security Engineer" />
</p>

<p align="center">
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/">Portfolio</a>
  ·
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/Pooja_Kiran_Agentic_AI_Security_Engineer_Resume.pdf">Resume</a>
  ·
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a>
  ·
  <a href="mailto:poojakiranbhardwaj@gmail.com">Email</a>
</p>

<table>
<tr>
<td width="68%" valign="top">

## About

I am a **Security Engineer focused on AI & Agent Security, Application Security, Cloud IAM Security, and Model Supply-Chain Security**.

I secure three trust boundaries where AI systems become security-critical: **Agent → Tool**, **Identity → Authority**, and **Artifact → Runtime**. My work emphasizes **default-deny design, reproducible testing, security telemetry, and evidence that can be independently reviewed**.

I completed an **M.S. in Information Technology (Security) at Arizona State University**, GPA **3.87/4.00**.

</td>
<td width="32%" align="center" valign="middle">
  <img src="./photo.png" width="230" alt="Pooja Kiran" />
</td>
</tr>
</table>

## Selected security systems

<table>
<tr>
<td width="33%" valign="top">

### [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)

**Agent → Tool.** Default-deny MCP/JSON-RPC gateway for authorization and execution control before downstream tool calls.

**782 passing tests**  
**81.93% coverage**  
**69 named runtime detector signatures** (source count; not detection efficacy)

Python · FastAPI · Elastic Security

</td>
<td width="33%" valign="top">

### [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)

**Identity → Authority.** Static analysis for privilege, trust-policy, and escalation risk in AI-agent and workload IAM policies.

**25 deterministic rules**  
**244 passed / 3 skipped**  
SARIF 2.1.0 · Code Scanning

Python · AWS IAM · GitHub Actions

</td>
<td width="33%" valign="top">

### [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)

**Artifact → Runtime.** Non-executing inspection of model repositories and artifacts before they enter trusted workflows.

**260 passed / 1 skipped**  
**75.67% coverage**  
**33/33 adversarial fixtures**

Python · SafeTensors · GGUF · ONNX

</td>
</tr>
</table>

## Supporting security research

- [LLM Red Team Framework](https://github.com/poojakira/llm-redteam-framework): adversarial evaluation for LLM security
- [Dataset Poisoning Detector](https://github.com/poojakira/dataset-poisoning-detector): statistical and streaming checks for training-data integrity
- [Adversarial ML Lab](https://github.com/poojakira/adversarial-ml-lab): FGSM, PGD, C&W, robustness evaluation, and MITRE ATLAS mapping

## Experience

- **Independent AI Security Researcher & Engineer** · Self-directed research · Aug. 2024 to Present
  - **Led security design and architecture reviews** across self-directed AI and cloud security systems, translating threat models into enforceable requirements, CI gates, and documented repository release criteria.
  - Published independently checkable October 2026 CI snapshots: **782 passing MCP Gateway tests at 81.93% statement coverage**, **244 passing IAM analyzer tests** (3 credential-dependent skips), and **260 passing model-scanner tests** (1 skipped). These are software test results, not production security-effectiveness rates.
- **Business & Compliance Lead, AEROSEC (academic externship)** · Honeywell Aerospace Technologies × ASU · Aug. 2025 to Dec. 2025
- **Graduate Teaching Assistant / IT Grader** · Arizona State University · Jan. 2025 to Oct. 2025

## Core toolkit

**AI & Agent Security:** MCP/JSON-RPC 2.0, tool-call security, prompt injection, LLM red teaming, model supply-chain security

**Identity & Application Security:** Cloud IAM Security, AWS IAM, least privilege, trust policies, permission boundaries, capability-based authorization, API security, threat modeling

**Security Engineering & DevSecOps:** Python, FastAPI, pytest, GitHub Actions, CI/CD security, SARIF 2.1.0, GitHub Code Scanning, Docker

**Detection & Observability:** Elastic Security, ECS, SIEM, Prometheus, tamper-evident audit logging, MITRE ATLAS

## Research

[A Personalized E-Learning System Using Reinforcement Learning Through Satellite](https://ieeexplore.ieee.org/document/10440852) · IEEE INDICON 2023

## Connect

**Portfolio:** https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/  
**LinkedIn:** https://www.linkedin.com/in/poojakiran/  
**Email:** poojakiranbhardwaj@gmail.com

<sub>The headline test and coverage metrics above are tied to explicitly cited October 2026 hosted runs; the 69-signature figure is a separate detector source count. These must not be treated as a joint security-effectiveness experiment. Consult RESUME_METRICS_EVIDENCE.md for the evidence sources. Original development periods are documented separately in each repository's provenance file; current metrics are not projected backward to project inception.</sub>


## Verification status — October 9, 2026

See [evidence and limitations](docs/VERIFICATION_STATUS_2026-10-09.md). Passing CI at a dated commit or a preview deployment does not certify all source, security controls or operational claims.


Maintenance checks and their limits are recorded in [the October 9 fix verification](docs/FIX_VERIFICATION_2026-10-09.md).

## Hosted CI evidence (reviewed October 12, 2026; run dates differ)

Machine-readable index: [portfolio_metrics.json](evidence/portfolio_metrics.json). CI checks that the main profile and evidence index agree on these dated claims.

- MCP Agent Security Gateway: [CI 38012954359](https://github.com/poojakira/mcp-agent-security-gateway/actions/runs/38012954359), Python 3.12 **782 passed, 81.93% coverage**. The 69 signatures are a separate code inventory, not this run's efficacy measure; older 723/81.91%/55 metrics remain historical.
- AWS Agent Identity Guard: [CI 38009457205](https://github.com/poojakira/aws-agent-identity-guard/actions/runs/38009457205), **247 collected, 244 passed, 3 credential-dependent skips**.
- HF Model Provenance Scanner: [CI 38002138828](https://github.com/poojakira/hf-model-provenance-scanner/actions/runs/38002138828), **260 passed, 1 skipped, 6 subtests, 75.67% statement coverage**. The 33/33 fixture count remains scoped to committed adversarial examples, not real-world detection rate.
- Historical posters intentionally retain dated earlier results. The canonical portfolio resume is source-built; confirm the deployed PDF matches the LaTeX and recruiter view after any artifact-sync pull request. Do not silently combine historical denominators or dates. See [RESUME_METRICS_EVIDENCE.md](RESUME_METRICS_EVIDENCE.md).
