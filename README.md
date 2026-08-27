# Pooja Kiran Bharadwaj

I build security tools for AI/ML systems -- focused on supply-chain integrity, agent runtime safety, and adversarial robustness.

Most of my work starts from a concrete problem: pickle files on Hugging Face can execute arbitrary code on `torch.load()`, AI agents can be tricked into exfiltrating data through tool calls, and IAM policies for agent roles are rarely reviewed for escalation paths. I built tools to address each of these.

These are research and portfolio projects, not deployed production systems. They're functional, tested, and open-source -- but they haven't been hardened for enterprise use or run at scale.

---

## Detection & Enforcement Tools

### [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) `[Beta]`
Supply-chain scanner for HuggingFace model repos. Detects pickle exploits, typosquatting, and obfuscated payloads by inspecting file headers -- without downloading full model weights. Includes a runtime `torch.load()` interception hook.

See the [repo README](https://github.com/poojakira/hf-model-provenance-scanner#readme) for test coverage and scan methodology.

### [mcp-agent-security-gateway](https://github.com/poojakira/mcp-agent-security-gateway) `[Beta]`
Interception layer for MCP-protocol AI agent tool calls. Applies policy checks for prompt injection patterns, PII in outbound payloads, and data exfiltration attempts.

See the [repo README](https://github.com/poojakira/mcp-agent-security-gateway#readme) for architecture and current detection capabilities.

### [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard) `[Beta]`
Static analysis of IAM policies for AI agent roles. Flags privilege escalation paths and credential-harvesting patterns specific to agent workloads.

See the [repo README](https://github.com/poojakira/aws-agent-identity-guard#readme) for supported checks and usage.

---

## Research & Red Team Labs

| Repository | What it does | Status |
|-----------|-------------|--------|
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM, PGD, C&W attack implementations and robustness benchmarks | Research |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Automated jailbreak simulation and guardrail evaluation | Beta |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership inference and model inversion experiments | Research |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Statistical anomaly detection for training data integrity | Beta |

---

## Relevant Frameworks

My work draws from these threat taxonomies:

- **OWASP Top 10 for LLMs** -- prompt injection, insecure output handling, supply chain
- **MITRE ATLAS** -- adversarial ML threat modeling
- **NIST AI RMF** -- risk identification for ML systems

---

## Background

- MS Information Technology -- Arizona State University (2026)
- Published at IEEE INDICON 2023
- Languages & tools: Python, PyTorch, AWS IAM, Docker, GitHub Actions, Pytest, FastAPI

---

## Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-poojakiran-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/poojakiran) · 📧 pkiran1@asu.edu

Greater Phoenix Area · F-1 OPT EAD
