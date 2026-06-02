# Pooja Kiran â€” ML Security Engineer

**I build defenses for ML systems: model supply chain, LLM/RAG security, adversarial ML, and privacy attacks.**  
M.S. IT Security, Arizona State University Â· IEEE INDICON 2023 Â· Honeywell Aerospace background  
Phoenix, AZ Â· [LinkedIn](https://linkedin.com/in/poojakiran) Â· [Portfolio](https://pooja-kiran.com) Â· Open to work

---

## 2026 Highlights

- **Model-Supply-Chain-Auditor**: catches pickle RCE, MEMOWNED desync (CVE-2025-10155â€“10157), post-STOP payloads â€” SARIF output for GitHub Code Scanning
- **LLM-Guard-Scanner**: OWASP LLM A01â€“A10 coverage, 0.90 F1 on 600-prompt corpus, RAG poisoning detection, FastAPI middleware
- **ML-Privacy-Attacks**: reproduced Shokri 2017 membership inference + Fredrikson 2015 model inversion, DP-SGD defense with Îµ/accuracy trade-off quantified
- **Adversarial-Robustness-Toolkit**: FGSM, PGD, C&W, AutoAttack-inspired ensemble on CIFAR-10 with documented clean/robust accuracy trade-offs
- **production-ml-platform**: JWT auth, RS256, hash-chain audit log, drift detection, model registry with rollback â€” on official NYC TLC data
- **Private**: `secure_ml` (available on request) â€” end-to-end secure inference with hardware-backed key management
- **Research**: INDICON 2023 RL paper â€” contact for preprint/slides

---

## 2026 ML Security Map

### Supply Chain Security
[![CI](https://github.com/poojakira/Model-Supply-Chain-Auditor/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/Model-Supply-Chain-Auditor/actions/workflows/ci.yml)  
**[Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor)** â€” Pickle/PyTorch artifact scanning, SafeTensors validation, Ed25519 signing, SARIF output. Catches malicious model weights at the CI gate before deployment.

### LLM & RAG Security
[![CI](https://github.com/poojakira/LLM-Guard-Scanner/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/LLM-Guard-Scanner/actions/workflows/ci.yml)  
**[LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner)** â€” Prompt injection patterns, PII/secret output scanning, RAG poisoning checks mapped to OWASP LLM Top 10. Deterministic baseline for LLM application defense.

[![CI](https://github.com/poojakira/docquery/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/docquery/actions/workflows/ci.yml)  
**[docquery](https://github.com/poojakira/docquery)** â€” RAG pipeline with Qdrant retrieval, reranking, prompt versioning, fail-closed auth/rate-limit controls. Evidence of hardened vector retrieval.

**[coderev-agents](https://github.com/poojakira/coderev-agents)** â€” LangGraph agentic prototype with untrusted diff hashing, line-numbered rendering, prompt-injection markers. Shows trust-boundary thinking in multi-agent systems.

### Adversarial ML
[![CI](https://github.com/poojakira/Adversarial-Robustness-Toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/Adversarial-Robustness-Toolkit/actions/workflows/ci.yml)  
**[Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit)** â€” FGSM, PGD, C&W, AutoAttack-inspired attacks on CIFAR-10 with measured clean/robust accuracy trade-offs and documented limitations.

### Privacy Attacks
[![CI](https://github.com/poojakira/ML-Privacy-Attacks/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/ML-Privacy-Attacks/actions/workflows/ci.yml)  
**[ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks)** â€” Membership inference (Shokri 2017) and model inversion (Fredrikson 2015). Quantifies privacy leakage with reproducible DP-SGD gap analysis.

### Secure ML Serving & Production Controls
[![CI](https://github.com/poojakira/production-ml-platform/actions/workflows/smoke.yml/badge.svg)](https://github.com/poojakira/production-ml-platform/actions/workflows/smoke.yml)  
**[production-ml-platform](https://github.com/poojakira/production-ml-platform)** â€” FastAPI inference, JWT auth, encryption, hash-chain audit logging, drift detection, and dependency scanning. Official NYC TLC dataset, SHA-256 verified.

**[RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard)** â€” CUDA memory fragmentation monitoring. OOM in a serving pod is a DoS vector; this guard provides structured alerting before impact.

### Production ML Rigor (Gold Standard)
[![CI](https://github.com/poojakira/PulseNet-RUL-Forecasting/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/PulseNet-RUL-Forecasting/actions/workflows/ci.yml)  
**[PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting)** â€” NASA C-MAPSS FD001, data lineage, STRIDE threat model, CI security gates, RBAC, tenant audit, measured evidence. **End-to-end governed ML system.**

---

## Strongest Evidence by Hiring Signal

| Area | Repository | Evidence |
|------|-----------|----------|
| Model supply chain | [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Pickle RCE scanning, CVE-2025-10155/10156/10157, Ed25519 signing, SARIF, threat model, CI gates |
| LLM application security | [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) + [docquery](https://github.com/poojakira/docquery) | OWASP A01â€“A10 mapped, 600-prompt corpus, RAG poisoning pipeline, FP/FN analysis |
| Adversarial ML fundamentals | [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | FGSM/PGD/C&W/AA attacks, adversarial training, clean vs robust trade-offs, literature ranges |
| ML privacy attacks | [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | MI advantage table across model sizes, model inversion, DP-SGD Îµ/accuracy trade-off |
| Secure ML serving | [production-ml-platform](https://github.com/poojakira/production-ml-platform) | JWT RS256, hash-chain audit log, drift detection, rollback, real NYC TLC data |
| ML systems / infrastructure | [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard) | CUDA fragmentation monitoring, DoS framing, multi-tenant limitations |
| Governed ML systems | [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | NASA official data, lineage, STRIDE, CI gates, RBAC, tenant audit |

---

## Full Repository Map

| Repo | Role | Notes |
|------|------|-------|
| [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | **Flagship** | Highest-signal for 2026 MLSecOps / AI supply-chain hiring |
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | **Flagship** | Direct LLM security surface: injection, data leakage, RAG poisoning |
| [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | **Core** | Adversarial ML attack/defense fundamentals with measured trade-offs |
| [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | **Core** | Privacy-attack quantification with reproducible metrics |
| [production-ml-platform](https://github.com/poojakira/production-ml-platform) | **Core** | Canonical secure ML platform with real data and controls |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | **Gold standard** | Governed ML system with NASA data, lineage, threat model, CI gates |
| [docquery](https://github.com/poojakira/docquery) | **Support** | RAG pipeline security; hardened vector retrieval |
| [coderev-agents](https://github.com/poojakira/coderev-agents) | **Support** | Agentic trust-boundary thinking and prompt-injection defense |
| [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard) | **Support** | ML infrastructure and CUDA-level security awareness |
| [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) | Archived | Earlier version of production-ml-platform; kept for reference |
| Aerospace / IoT repos (5) | Archived | Safety-critical telemetry supporting work â€” anomaly detection, numerical methods |
| [Pooja_Portfolio](https://github.com/poojakira/Pooja_Portfolio) | Archived | Web portfolio; GitHub is the primary engineering signal |
| `secure_ml` | **Private â€” available on request** | End-to-end secure inference with hardware-backed key management |

---

## Skill Coverage

| 2026 hiring signal | Proof |
|-------------------|-------|
| AI/LLM security (OWASP A01â€“A10) | LLM-Guard-Scanner, docquery, coderev-agents |
| Model artifact supply chain | Model-Supply-Chain-Auditor scan/sign/attest/policy |
| Adversarial ML | Adversarial-Robustness-Toolkit measured attack/defense trade-offs |
| Privacy attacks & defenses | ML-Privacy-Attacks MI + model inversion + DP-SGD gap |
| Secure ML serving & auth | production-ml-platform FastAPI + JWT + audit log + drift |
| Detection/response thinking | SARIF output, audit logs, verification scripts, failure mode docs |
| Cloud/MLOps fundamentals | Docker, FastAPI, CI gates, registry/rollback, dependency audit |
| Governed ML systems | PulseNet-RUL-Forecasting (NASA data, lineage, STRIDE, RBAC, CI) |
| Research discipline | Limitations sections, threat models, references, reproducible scripts |

---

## What I Am Not Claiming

- These repos are not production aerospace or enterprise security products.
- Prompt injection is not solved by regex scanning.
- Synthetic telemetry is not real satellite data.
- Benchmark numbers only appear where the command and artifact needed to reproduce them are checked in.
- Model defense claims include the threat model and attacker budget.

---

## References

- **OWASP LLM Top 10**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **MITRE ATLAS**: https://atlas.mitre.org/
- **NIST AI RMF**: https://www.nist.gov/itl/ai-risk-management-framework
- **SLSA Framework**: https://slsa.dev
- **Shokri et al. (2017)**: https://arxiv.org/abs/1610.05820
- **Fredrikson et al. (2015)**: https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/fredrikson

---

Phoenix, AZ Â· Open to **ML Security Engineer**, **AI Security Engineer**, **MLSecOps** roles
