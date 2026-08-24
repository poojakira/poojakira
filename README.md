# Pooja Kiran Bharadwaj

**AI Security Engineer** · Building detection and enforcement tools for ML/AI systems

What if the AI model you just downloaded is already attacking you?

Pickle files on Hugging Face execute arbitrary code the moment you call `torch.load()`. Most scanners require downloading full model weights to check them. Mine fetches only the first few KB and catches exploits that existing tools miss.

That question — *is this AI system safe to run?* — led me to build open-source tools that sit between AI systems and the damage they can do.

---

## 🛡️ Production Security Tools

### [mcp-agent-security-gateway](https://github.com/poojakira/mcp-agent-security-gateway)
Real-time interception layer for AI agent tool calls. Catches prompt injection, PII leakage, and data exfiltration before they leave your infrastructure. Enforces policy on every MCP tool invocation.

### [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Supply-chain security scanner for HuggingFace model repos — without downloading weights. Detects pickle exploits, typosquatting, rug-pulls, and obfuscated payloads using file headers alone. Runtime `torch.load()` interception blocks malicious models before execution.

> 100 top HuggingFace models scanned · 12/12 documented real-world attacks detected · 350+ tests

### [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)
Static IAM analysis purpose-built for AI agent roles. Identifies privilege escalation paths and credential-harvesting patterns that standard AWS tools miss.

---

## 🔬 Research & Red Team Labs

| Domain | Repository | Techniques |
|--------|-----------|------------|
| Adversarial robustness | [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM, PGD, C&W attack benchmarks |
| LLM guardrail evasion | [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Automated jailbreak simulation & evaluation |
| Model privacy | [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership inference, model inversion |
| Data integrity | [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Statistical anomaly detection for training data |

---

## 🧭 Frameworks & Methodology

My work maps to established AI/ML threat taxonomies:

- **OWASP Top 10 for LLMs** — prompt injection defense, insecure output handling, supply chain vulnerabilities
- **MITRE ATLAS** — adversarial ML threat modeling, technique coverage across reconnaissance through impact
- **NIST AI RMF** — risk identification and measurement for ML systems in production
- **OWASP ML Security Top 10** — model theft prevention, data poisoning detection, adversarial input resilience

---

## ⚡ Technical Focus

```
Supply Chain Security    ██████████████████░░  Model provenance, dependency integrity, artifact signing
Agent Runtime Security   █████████████████░░░  Tool-call interception, policy enforcement, sandboxing
Adversarial ML           ████████████████░░░░  Evasion attacks, robustness testing, certified defenses
Privacy & Extraction     ██████████████░░░░░░  Membership inference, model inversion, differential privacy
LLM Red Teaming          █████████████████░░░  Jailbreak automation, guardrail evaluation, alignment testing
```

**Languages & Tools:** Python · PyTorch · AWS IAM · Docker · GitHub Actions · Pytest · FastAPI

---

## 📌 Highlights

- **IEEE published** — INDICON 2023
- **MS Information Technology** — Arizona State University (2026)
- **350+ tests** across the flagship model scanner
- **100 HuggingFace models** scanned with results published

---

## Let's talk

[![LinkedIn](https://img.shields.io/badge/LinkedIn-poojakiran-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/poojakiran) · 📧 pkiran1@asu.edu

Greater Phoenix Area · F-1 OPT EAD
