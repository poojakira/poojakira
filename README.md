<!-- GitHub profile README: source-scoped engineering work, updated November 2026. -->

<p align="center">
  <img src="assets/profile-banner.svg" alt="Pooja Kiran — Software Engineer | AI Agents & Application Security" width="100%" />
</p>

<h1 align="center">Pooja Kiran</h1>
<p align="center"><strong>Software Engineer | AI Agents &amp; Application Security</strong></p>
<p align="center">
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/">Portfolio</a> ·
  <a href="RESUME_METRICS_EVIDENCE.md">Engineering evidence</a> ·
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a> ·
  <a href="https://ieeexplore.ieee.org/document/10440852">Published research</a>
</p>

**When software can act on its own, who decides what it is allowed to do—and how do we verify what happened?**

That question drives my work. I build Python-backed security and developer tools around **agent execution, identity and permissions, model artifacts, and investigation workflows**. I care about the boundary between a proposed action and an authorized one, and about testing the system's behavior when inputs, dependencies, or evidence fail.

My approach: **build the mechanism, exercise the failure path, inspect the state change, and publish the limits of the result.**

## Selected engineering work

Four independent projects, each with an inspectable implementation and a dated local-verification record. I lead with what the software does; detailed release boundaries follow below.

### 01 / Agent → Tool — [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)
**Python · MCP/JSON-RPC · Authorization · Execution tracing**

Built a local MCP workbench that routes agent tool calls through a **default-deny policy engine and stdio proxy**, then compares execution receipts with disposable tool-side state. The important distinction is explicit: **a policy decision is not proof of an external action's outcome**.

- **Verified candidate:** **834 passed / 0 skipped · 81.80% local statement coverage**.
- **Engineering boundary:** fixed-child local execution is exercised; broad MCP conformance, arbitrary-server OS isolation, externally anchored audit and cross-provider side-effect reconciliation are not established.
- [Repository](https://github.com/poojakira/mcp-agent-security-gateway) · [Reviewed source](https://github.com/poojakira/mcp-agent-security-gateway/blob/d2e7b6ea7c1a1f9cb0fb71f73d0a692d8fa0410c/README.md) · [Evidence manifest](https://raw.githubusercontent.com/poojakira/mcp-agent-security-gateway/4f83f01a3ed8aca5639143fe2179afb0f864f46e/release-evidence/manifest.json) · [Release assessment](https://github.com/poojakira/mcp-agent-security-gateway/blob/4f83f01a3ed8aca5639143fe2179afb0f864f46e/release-evidence/RELEASE_ASSESSMENT.md) · [Draft PR](https://github.com/poojakira/mcp-agent-security-gateway/pull/194)

### 02 / Telemetry → Investigation — [Attack Detection Engine / Aegis HealthSec](https://github.com/poojakira/attack-detection-engine)
**Python · FastAPI · React · PostgreSQL · FHIR AuditEvent**

Built a full-stack, local investigation workflow for **synthetic clinical-access events**: authenticated API endpoints, event detection and correlation, persisted cases, adjustable thresholds, repeatable analysis, and checksummed report exports.

- **Verified candidate:** **332 passed / 0 skipped · 82.47% local statement coverage**.
- **Engineering boundary:** batch investigation using synthetic data, not live clinical monitoring. Hosted [CI run 44431212087](https://github.com/poojakira/attack-detection-engine/actions/runs/44431212087) was **queued / NOT VERIFIED** at the dated November 19, 2026 recheck; privacy, recovery, load and public-hosting approvals remain open.
- [Repository](https://github.com/poojakira/attack-detection-engine) · [Reviewed source](https://github.com/poojakira/attack-detection-engine/blob/aa45efd2f9f7e229a0ae7b7f8d77adac18d96e83/README.md) · [Evidence manifest](https://raw.githubusercontent.com/poojakira/attack-detection-engine/875299dd6a7ed061df792d1150371c688383fc05/release-evidence/manifest.json) · [Release assessment](https://github.com/poojakira/attack-detection-engine/blob/875299dd6a7ed061df792d1150371c688383fc05/release-evidence/RELEASE_ASSESSMENT.md) · [Draft PR](https://github.com/poojakira/attack-detection-engine/pull/58)

### 03 / Identity → Authority — [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)
**Python · AWS IAM · Static analysis · SARIF 2.1.0**

Developed a **credential-free IAM policy review tool** that parses identity and trust policies, maps findings back to source statements, compares revisions, and exports structured reports. The current engine contains **24 static checks plus 1 additional live-context check**.

- **Verified candidate:** **272 passed / 3 skipped · 77.15% local statement coverage**.
- **Engineering boundary:** the **3 skips cover the absent legacy TestRulesModule API**, not missing cloud credentials. Static findings do not establish effective AWS permissions or exploitability.
- [Repository](https://github.com/poojakira/aws-agent-identity-guard) · [Reviewed source](https://github.com/poojakira/aws-agent-identity-guard/blob/abe1c0a1e5953b18eae762a5c41f400ff677adb2/README.md) · [Evidence manifest](https://raw.githubusercontent.com/poojakira/aws-agent-identity-guard/a396433a4070a0ddc68aa83f9b1093e87fc3224f/release-evidence/manifest.json) · [Release assessment](https://github.com/poojakira/aws-agent-identity-guard/blob/a396433a4070a0ddc68aa83f9b1093e87fc3224f/release-evidence/RELEASE_ASSESSMENT.md) · [Draft PR](https://github.com/poojakira/aws-agent-identity-guard/pull/75)

### 04 / Artifact → Review — [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)
**Python · SafeTensors · GGUF · File integrity · Bounded static inspection**

Built an isolated, bounded inspection path to compare supported model artifacts by **hashes, metadata and file structure without loading model code**. This helps reviewers investigate changes, not certify the safety or origin of a model.

- **Verified candidate:** **317 passed / 3 skipped · 76.08% local statement coverage · 6 separate passing subtests**.
- **Engineering boundary:** independent closing review is **BLOCKED**. Static inspection does not prove publisher identity, training lineage, behavioral safety or absence of backdoors.
- [Repository](https://github.com/poojakira/hf-model-provenance-scanner) · [Reviewed source](https://github.com/poojakira/hf-model-provenance-scanner/blob/ab26ad5cd6fe28ae1b0986e20da46be9ebb2f27a/README.md) · [Evidence manifest](https://raw.githubusercontent.com/poojakira/hf-model-provenance-scanner/ed25d66b72e374f86e2975930b0ed83b9acf3c09/release-evidence/manifest.json) · [Release assessment](https://github.com/poojakira/hf-model-provenance-scanner/blob/ed25d66b72e374f86e2975930b0ed83b9acf3c09/release-evidence/RELEASE_ASSESSMENT.md) · [Draft PR](https://github.com/poojakira/hf-model-provenance-scanner/pull/103)

## How I work

| Design question | Engineering practice |
| --- | --- |
| **Who has authority?** | Make identities, capabilities and policy decisions explicit. |
| **What actually executed?** | Compare application decisions with receipts, persisted state and repeatable tests. |
| **What happens on failure?** | Exercise denied actions, malformed inputs, retries, uncertain outcomes and recovery paths. |
| **What can we legitimately claim?** | Link metrics to exact source commits, distinguish local testing from deployed behavior, and disclose open risks. |

**Daily engineering stack:** Python, FastAPI, React, TypeScript, PostgreSQL, Docker, pytest, GitHub Actions, JSON/JSON-RPC, AWS IAM, SARIF, and security-event telemetry.

<details>
<summary><strong>Other labs and research repositories</strong></summary>

- [LLM Red-Team Framework](https://github.com/poojakira/llm-redteam-framework) — structured adversarial LLM testing.
- [Dataset Poisoning Detector](https://github.com/poojakira/dataset-poisoning-detector) — dataset integrity and poisoning analysis.
- [Adversarial ML Lab](https://github.com/poojakira/adversarial-ml-lab) — adversarial machine-learning experiments.
- [ML Security Benchmark Suite](https://github.com/poojakira/mlsec-benchmark-suite) — ML-security evaluation harnesses.
- [Unified ML Security Platform](https://github.com/poojakira/unified-ml-security-platform) — integrated security-tooling experiments.

</details>

## Experience and research

- **Technical Collaborator · Cerberus (Sep–Oct 2026)** — connected gateway telemetry to a security-event schema and tested identity attribution in bounded integration workflows; short-term collaboration.
- **IT Grader · Arizona State University (Jan 2025–May 2026)** — paid part-time university role evaluating security, systems configuration and web-programming coursework.
- **Business & Compliance Lead · Honeywell Aerospace × ASU Technology Innovation Lab (Aug–Dec 2025)** — academic externship translating stakeholder input into security/compliance requirements and technical comparisons; **not Honeywell employment**.
- **M.S. Information Technology · Arizona State University (2026)**; **B.Tech. Computer Science & Engineering · M. S. Ramaiah University of Applied Sciences (2023)**.
- **IEEE INDICON 2023** — coauthored [*A Personalized E-Learning System Using Reinforcement Learning Through Satellite*](https://ieeexplore.ieee.org/document/10440852), developing the adaptive-learning work and writing the manuscript with faculty collaborators.

## Evidence, not performance theater

The metrics above are the **November 18, 2026 (America/Phoenix) source-scoped local snapshots**, not continuously updated test results. All four reviewed release assessments remain **PARTIAL**; their reviewed candidates are in unmerged draft pull requests. These are **not** production releases, customer adoption claims, field detection rates, or approvals for public deployment.

Read the [evidence index](RESUME_METRICS_EVIDENCE.md) for exact commits, test scope, skips, archived manifests, historical snapshots and limitations. Browser workbenches were exercised locally; committed guided-notebook cells ran locally, while **hosted Colab execution remains NOT VERIFIED**. No publicly hosted full security application is claimed.

## Connect

[**Portfolio**](https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/) · [**LinkedIn**](https://www.linkedin.com/in/poojakiran/) · [**IEEE publication**](https://ieeexplore.ieee.org/document/10440852) · [**Email**](mailto:poojakiranbhardwaj@gmail.com)

*Interested in software engineering, backend systems, AI-agent infrastructure, and application security. The code and its limits are open for inspection.*

<!-- Resume link intentionally omitted until the single Software Engineer PDF is published at a stable URL. -->
