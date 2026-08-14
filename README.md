# Pooja Kiran

## AI Agent Security Engineer

**Agent Runtime Security · MCP & Tool Security · Agent Identity & Authorization · AI/ML Security**

I build security boundaries for AI agents and autonomous systems — controlling **what agents can access, which tools they can invoke, how identities and permissions are scoped, how agent actions are monitored, and how malicious or unintended behavior is detected and contained**.

My work spans agent runtime security, MCP and tool-call inspection, least-privilege cloud identity, AI supply-chain security, adversarial evaluation, and security controls designed to produce **inspectable and reproducible evidence**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://linkedin.com/in/poojakiran)
[![GitHub](https://img.shields.io/badge/GitHub-poojakira-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/poojakira)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge\&logo=gmail\&logoColor=white)](mailto:poojakiranbhardwaj@gmail.com)

---

## AI Agent Security Engineering

| Project                                                                                       | Security Boundary                    | Engineering Focus                                                                                                                                   |
| :-------------------------------------------------------------------------------------------- | :----------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor)** | Agent ↔ Tool                         | MCP / JSON-RPC tool-call inspection, injection and exfiltration detection, egress controls, audit logging, rate limiting, shadow-mode enforcement   |
| **[aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)**         | Agent ↔ Cloud Identity               | Agent IAM analysis, least privilege, `PassRole` risk, Bedrock/Lambda/S3 permission scoping, trust policies, permission boundaries, SARIF CI gates   |
| **[hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)**   | Agent/ML System ↔ Model Supply Chain | Model provenance, malicious pickle analysis, suspicious metadata, typosquat detection, temporal integrity checks, SARIF and SBOM-oriented workflows |
| **[mlsec-benchmark-suite](https://github.com/poojakira/mlsec-benchmark-suite)**               | Security Control ↔ Evidence          | Reproducible security regression fixtures and structured evidence across IAM, model supply-chain and AI-security controls                           |
| **[llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework)**               | Agent/LLM ↔ Untrusted Input          | Prompt-injection and LLM security experiments, adversarial evaluation, PII/RAG security checks and CI-integrated findings                           |

### What I am working toward

My current engineering direction is centered on the security architecture surrounding autonomous agents:

**Identity → Authorization → Tool Invocation → Runtime Execution → Network/Data Access → Observability → Policy Enforcement**

The goal is to build security controls that remain useful after an LLM has decided to act — at the points where an agent interacts with tools, credentials, APIs, infrastructure and sensitive data.

---

## Agent Security Focus

### Agent Runtime & Harness Security

* Runtime security boundaries for autonomous and semi-autonomous agents
* Tool execution controls and capability restriction
* MCP client/server trust boundaries
* Tool-call inspection and policy enforcement
* Network egress and data-exfiltration controls
* Auditability, traceability and security telemetry
* Fail-closed controls, rate limits and circuit breakers
* Secure agent harness architecture

### Agent Identity, Authorization & Governance

* Least-privilege identities for AI agents and tool executors
* Agent-specific IAM policy analysis
* Permission and trust-boundary review
* Scoped access to cloud resources and tools
* Delegated authorization and workload identity concepts
* Agent governance implemented through enforceable technical controls
* Human approval boundaries for high-risk actions

### AI / ML Supply-Chain Security

* Model provenance and artifact inspection
* Pickle deserialization risk
* Malicious or suspicious model metadata
* Repository impersonation and typosquatting
* Model integrity and temporal-change analysis
* Security evidence integrated into CI/CD workflows

### AI Security Evaluation

* Prompt-injection and indirect-injection testing
* Tool misuse and excessive-agency threat modeling
* Adversarial ML evaluation
* Dataset-poisoning research
* Model privacy attacks
* Security regression testing
* Reproducible fixtures and evidence artifacts

---

## AI/ML Security Foundations

My earlier work provides the ML-security foundation underneath my current AI Agent Security specialization.

| Project                                                                                   | Research Area                                                                           |
| :---------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **[adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab)**                 | FGSM, PGD and C&W adversarial attacks, adversarial training and robustness evaluation   |
| **[model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks)**           | Membership inference, model extraction, privacy evaluation and privacy-risk experiments |
| **[dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector)** | Dataset poisoning and anomalous-sample detection research                               |

These projects remain part of the portfolio as **research and security foundations**, while my primary engineering focus is now agent security.

---

## Engineering Stack

**Languages**
Python · SQL · Bash

**AI / ML**
PyTorch · scikit-learn · Hugging Face ecosystem · adversarial ML · model security

**Agent & LLM Security**
MCP · JSON-RPC · prompt injection · tool-call security · RAG security · agent identity · authorization · security gateways

**Backend & Security Engineering**
FastAPI · REST APIs · JWT · RBAC · IAM · rate limiting · audit logging · policy enforcement

**Cloud & Infrastructure**
AWS IAM · Bedrock security concepts · Docker · Kubernetes · GitHub Actions · CI/CD security gates

**Security Outputs & Observability**
SARIF · structured JSON evidence · Prometheus metrics · tamper-evident audit trails · reproducible security fixtures

---

## Security Engineering Principles

I try to make security claims **testable rather than promotional**.

My projects are built around several principles:

* **Threat-model first** — define the boundary and attacker before adding controls.
* **Least privilege** — agents should receive only the capabilities required for a task.
* **Inspect actions, not only prompts** — security must extend beyond LLM input filtering to tool execution and runtime behavior.
* **Evidence over adjectives** — benchmarks and security claims should include scope, fixtures, versions and reproducible commands.
* **Fail safely** — security-sensitive systems should have explicit behavior for malformed input, unavailable dependencies and overloaded conditions.
* **Auditability** — autonomous actions should produce enough evidence for investigation and accountability.
* **Known limitations matter** — research prototypes and production controls should not be presented as the same thing.

---

## AI Security Research

### Cybersecurity Innovation Researcher

**TEM 598 Technology Innovation Lab — Arizona State University × Honeywell Aerospace Innovation Hub**

Contributed to a graduate research practicum exploring cybersecurity and AI-related challenges in aerospace technology environments.

### Publications

**Personalized E-learning System Using Reinforcement Learning Through Satellite**
IEEE Xplore, 2024
https://ieeexplore.ieee.org/document/10440852

**Smart Charge Pro: Empowering Future Mobility With Advanced Safety and Efficiency in Electric Vehicle Charging Infrastructure**
IOSR Journal of Computer Engineering, 2023
https://www.iosrjournals.org/iosr-jce/pages/25(4)Series-1.html

---

## Current Research Direction

I am continuing to deepen my work around:

* AI Agent Security
* Agent Runtime Security
* Agent Harness Security
* MCP Security
* Tool and Plugin Security
* Agent Identity and Workload Authorization
* Agent Governance Controls
* Secure Agent-to-Agent Communication
* Runtime Isolation and Sandboxing
* Indirect Prompt Injection
* Excessive Agency
* Agent Data Exfiltration
* AI Security Gateways
* Agent Security Observability
* AI Red Teaming
* AI/ML Supply-Chain Security

---

## Selected Architecture

```text
                         ┌──────────────────────┐
                         │       AI Agent       │
                         └──────────┬───────────┘
                                    │
                           Identity / Context
                                    │
                                    ▼
                     ┌──────────────────────────┐
                     │ Identity & Authorization │
                     │   Least Privilege / IAM  │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │   Agent Security Gateway │
                     │ MCP / Tool Policy Layer  │
                     └────────────┬─────────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 │                │                │
                 ▼                ▼                ▼
             APIs / SaaS     Cloud Resources   Local Tools
                 │                │                │
                 └────────────────┼────────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │ Runtime Security Controls│
                     │ Isolation · Egress · DLP │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │ Security Telemetry       │
                     │ Audit · Detection · Eval │
                     └──────────────────────────┘
```

This is the security layer I am interested in engineering: the infrastructure **between an agent's intent and its real-world capabilities**.



## Opportunities

I am primarily interested in engineering and research roles involving:

**AI Agent Security Engineer**
**Agent Security Engineer**
**Agentic AI Security Engineer**
**AI Security Engineer**
**AI Agent Infrastructure Security Engineer**
**Security Research Engineer — AI / Agentic Systems**
**AI/LLM Security Engineer**

Particularly interested in problems involving **agent runtimes, MCP, tool security, workload identity, authorization, cloud security, sandboxing, policy enforcement, AI security infrastructure and adversarial evaluation**.

---

## Location & Contact

**Location:** Greater Phoenix Area, Arizona, USA
**Work authorization:** F-1 OPT; H-1B sponsorship required for longer-term employment

**Email:** [poojakiranbhardwaj@gmail.com](mailto:poojakiranbhardwaj@gmail.com)
**LinkedIn:** [linkedin.com/in/poojakiran](https://linkedin.com/in/poojakiran)
**GitHub:** [github.com/poojakira](https://github.com/poojakira)

---

> **Security for autonomous systems cannot stop at the prompt. The real boundary begins when an agent is allowed to act.**

*Portfolio claims are scoped to publicly inspectable implementations, committed evidence and documented limitations.*

