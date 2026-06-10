# Pooja Kiran — ML Security Engineer

Building defenses where ML systems actually fail: supply-chain integrity, LLM attack surfaces,
privacy leakage at inference time, and adversarial robustness with honest failure documentation.

Phoenix, AZ · [LinkedIn](https://www.linkedin.com/in/poojakiran/) · [GitHub](https://github.com/poojakira)

---

### Active work

| Repo | Threat domain | What it measures |
|------|--------------|-----------------|
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | LLM attack surface | Prompt injection, PII/secret leakage, RAG poisoning — OWASP LLM Top 10 mapped |
| [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Supply chain integrity | Pickle/PyTorch artifact scanning, SafeTensors validation, Ed25519 signing, SARIF output |
| [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | Privacy leakage | MIA advantage 0.42 on UCI Bank Marketing — EU AI Act Art.10 FAIL flagged automatically |
| [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | Adversarial robustness | FGSM / PGD / C&W / AutoAttack on CIFAR-10 — clean-trained model drops to 0% under PGD |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Secure MLOps | C-MAPSS pipeline: STRIDE threat model, RBAC, 2.7 ms mean inference, SARIF CI gates |
| [docquery](https://github.com/poojakira/docquery) | RAG security | Multi-tenant RAG hardened against indirect injection — Qdrant, reranking, FastAPI |

---

### Focus areas

- LLM agent security — prompt injection, indirect injection, RAG poisoning, context guard
- ML supply-chain integrity — artifact signing, pickle scanning, SBOM, SLSA alignment
- Privacy attacks at inference — membership inference, model inversion, DP-SGD accounting
- Adversarial robustness — documented failure conditions, not just "defense works" claims
- Secure MLOps — SARIF gates, RBAC, audit logging, drift detection, tenant isolation

---

### Standards and frameworks

OWASP LLM Top 10 · MITRE ATLAS · NIST AI RMF · EU AI Act Art.10/15 · STRIDE · SLSA

---

### Currently

Building an agentic threat evaluation harness covering indirect prompt injection, tool-call hijacking,
and memory poisoning — motivated by the 31% browser-agent hijack rate in Anthropic's 2026 system card.
