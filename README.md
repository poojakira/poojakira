<!-- Profile README — the gateway into the full interactive experience. -->

# Pooja Kiran — AI Security Engineer

**Security for the moment AI stops generating text and starts taking actions.**

I build the controls that sit between an AI agent's decision and a real-world action:
inspecting tool calls, constraining cloud identity, and checking model artifacts before
they are trusted.

Agentic AI &amp; LLM security · MCP &amp; tool security · IAM &amp; least privilege · model supply-chain security.

### ▶ Enter the interactive portfolio

**[poojakira.github.io/Pooja_Kiran_Portfolio_Website](https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/)**

Ask my AI, talk to me by voice, explore an Engineering Atlas, open flagship projects with
threat models and architecture, and run safe in-browser security demos — every answer linked
to its source. Static, keyless, and private: no trackers, no third-party scripts.

[![Interactive portfolio](https://img.shields.io/badge/Interactive_Portfolio-Enter-1b2a4a?style=for-the-badge)](https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/poojakiran/)
[![Email](https://img.shields.io/badge/Email-Reach%20me-c8532b?style=for-the-badge&logo=gmail&logoColor=white)](mailto:poojakiranbhardwaj@gmail.com)

---

## Flagship work

| Project | What it does | Evidence &amp; limits |
| :--- | :--- | :--- |
| **[mcp-agent-security-gateway](https://github.com/poojakira/mcp-agent-security-gateway)** | Inspects and gates MCP tool calls at the agent-to-tool boundary — inline stdio proxy, 5-layer decision pipeline, 50+ injection rules, hash-chained audit log, ECS/Elastic detection lab. 569 tests, 75% coverage. | Prototype; controls only traffic routed through it. |
| **[aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)** | Static IAM linter for agent roles: 25 deterministic rules, text/JSON/SARIF, CI merge gate. No AWS credentials needed. | Best-effort linter; complements Access Analyzer/Prowler. |
| **[hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)** | Scans model repos for pickle-risk, provenance, and impersonation; maps findings to MITRE ATT&amp;CK v19. | Fixture-scoped evidence; not a real-world detection rate. |

### Supporting research

| Project | Focus | Honest status |
| :--- | :--- | :--- |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Prompt-injection detection with grouped / out-of-distribution evaluation. | Research baseline; F1 0.97 held-out, ≥0.85 on novel phrasings. |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM / PGD / C&amp;W attacks, unit-tested; maps to MITRE ATLAS. | Benchmark artifacts not committed; defenses not implemented. |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership-inference and model-privacy risk measurement. | No metric claimed without benchmark-suite evidence. |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Anomaly-based poisoning screening over a streaming pipeline. | ROC-AUC ≈ 0.53–0.56 (near random); research baseline. |

---

## How I work

- **Secure the action, not just the prompt.** Controls belong at the hand-off from decision to execution.
- **A metric is meaningful only with its scope attached.** Distribution and model before the number.
- **A documented weakness beats an undocumented promise.** Every project names what it does not do.
- **Least privilege is a pre-deploy decision.** Catch over-broad IAM before an agent holds it.

Findings map to **MITRE ATT&amp;CK v19 / ATLAS** and **NIST AI RMF** where the repositories support it.

---

## Research &amp; publications

- Cybersecurity Innovation Researcher — TEM 598 Technology Innovation Lab, Arizona State University × Honeywell Aerospace Innovation Hub.
- [Personalized E-learning System Using Reinforcement Learning Through Satellite](https://ieeexplore.ieee.org/document/10440852) — IEEE Xplore, 2024.
- [Smart Charge Pro — EV Charging Infrastructure](https://www.iosrjournals.org/iosr-jce/pages/25(4)Series-1.html) — IOSR-JCE, 2023.

## Contact

- **Interactive portfolio:** https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/
- Greater Phoenix Area, AZ · F-1 OPT · open to AI / ML Security Engineer roles
- Email: [poojakiranbhardwaj@gmail.com](mailto:poojakiranbhardwaj@gmail.com) · GitHub: [@poojakira](https://github.com/poojakira) · LinkedIn: [in/poojakiran](https://www.linkedin.com/in/poojakiran/)

---

<sub>Claims are limited to public, inspectable work with traceable evidence. Last updated August 2026.</sub>
