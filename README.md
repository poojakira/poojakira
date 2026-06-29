### Hi, I'm Pooja Kiran. ML Security Engineer.

I build and test security controls around ML systems: model supply-chain verification, LLM/RAG application security, adversarial ML evaluation, and secure ML serving infrastructure. Every featured repo includes a documented threat model, verified test suite, and known-limitations section.

[![Portfolio](https://img.shields.io/badge/Portfolio-poojakira.github.io-2563eb?style=for-the-badge&logo=google-chrome&logoColor=white)](https://poojakira.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/poojakiran)
[![Email](https://img.shields.io/badge/Email-Reach%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:poojakiranbhardwaj@gmail.com)

---

## GitHub Actions Status — Flagship Repos

[![LLM-Guard-Scanner CI](https://github.com/poojakira/LLM-Guard-Scanner/actions/workflows/redteam.yml/badge.svg)](https://github.com/poojakira/LLM-Guard-Scanner/actions)
[![Model-Supply-Chain-Auditor CI](https://github.com/poojakira/Model-Supply-Chain-Auditor/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/Model-Supply-Chain-Auditor/actions)
[![Secure-ML-Platform CI](https://github.com/poojakira/Secure-ML-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/Secure-ML-platform/actions)
[![docquery CI](https://github.com/poojakira/docquery/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/docquery/actions)
[![ML-Privacy-Attacks CI](https://github.com/poojakira/ML-Privacy-Privacy-Attacks/actions/workflows/ci.yml/badge.svg)](https://github.com/poojakira/ML-Privacy-Attacks/actions)

---

### Portfolio by Security Layer

#### Model Supply Chain
| Repo | What it does |
|------|-------------|
| [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Pickle opcode AST analysis, SafeTensors validation, Ed25519 signing, SLSA v1.0 provenance, policy-as-code CI gates, SARIF output |
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | Prompt injection detection (pattern + embedding), PII/secret scanning, RAG poisoning checks, PyRIT/Garak red-teaming, OWASP LLM Top 10 mapping |

#### LLM / RAG Security
| Repo | What it does |
|------|-------------|
| [docquery](https://github.com/poojakira/docquery) | Multi-tenant RAG pipeline with context guard, source provenance, PII redaction, prompt versioning, Qdrant + BGE reranking |
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | (above) — also covers agentic scanner for tool-calling contexts |

#### Adversarial ML & Privacy
| Repo | What it does |
|------|-------------|
| [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | 5 attack families (FGSM/PGD/C&W/APGD/Square) + 3 defenses (PGD-AT/TRADES/RS) on CIFAR-10 ResNet-18 with measured reports |
| [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | Membership inference (Shokri 2017, Carlini 2022, Yeom 2018), model inversion, DP-SGD accounting, EU AI Act / GDPR compliance mapping |

#### Secure ML Platform & Infrastructure
| Repo | What it does |
|------|-------------|
| [production-ml-platform](https://github.com/poojakira/production-ml-platform) | ML serving with A/B testing (Thompson sampling), drift detection (KS/ADWIN), SHAP explainability, JWT auth, K8s deployment, Istio canary routing |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Predictive maintenance on NASA C-MAPSS with data lineage, JWT auth, RBAC, hash-chain audit logging, CI verification |
| [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) | ML serving prototype with CORS/HSTS/rate-limiting/JWT/RBAC/audit/integrity/encryption — 15 security controls |

#### Supporting
| Repo | What it does |
|------|-------------|
| [coderev-agents](https://github.com/poojakira/coderev-agents) | Multi-agent code review combining Bandit SAST + LLM reasoning with prompt-injection guards (prototype) |
| [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard) | GPU out-of-memory detection and prevention for PyTorch training (GPU systems research) |

---

## 2026 Blueprint Skills Coverage

| Domain | Repo Evidence | Level |
|---|---|---|
| Adversarial ML (FGSM/PGD/C&W/TRADES) | Adversarial-Robustness-Toolkit | ██████████ Advanced |
| LLM Security / Prompt Injection | LLM-Guard-Scanner, docquery | ██████████ Advanced |
| ML Supply Chain / SLSA / Pickle | Model-Supply-Chain-Auditor | █████████░ Strong |
| Privacy Attacks (MIA/Inversion/DP) | ML-Privacy-Attacks | █████████░ Strong |
| RAG Pipeline Security | docquery, LLM-Guard-Scanner | █████████░ Strong |
| Agentic AI Security | coderev-agents | ███████░░░ Developing |
| Secure MLOps (CI/CD/SBOM/SARIF) | Secure-ML-platform, production-ml-platform | █████████░ Strong |
| Cloud Security (AWS/GCP/Azure) | ⚠️ IN PROGRESS | ████░░░░░░ Gap |
| Governance (NIST AI RMF/EU AI Act) | ML-Privacy-Attacks, PulseNet | ████████░░ Solid |
| Red Teaming (garak/PyRIT) | LLM-Guard-Scanner | ███████░░░ Developing |

---

## Currently Building

- [ ] cloud-ml-infra-hardening: Terraform AWS VPC+EKS+Bedrock guardrails (target: July 14, 2026)
- [ ] LLM-Guard-Scanner: DeBERTa fine-tuned classifier on labeled injection dataset
- [ ] llm-red-teaming-toolkit: Live attacks against Ollama llama3.2 with measured results

---

## Portfolio Website: [poojakira.github.io](https://poojakira.github.io)

---

### Infrastructure & Security

`Kubernetes` `Terraform` `AWS` `FastAPI` `PyTorch` `GitHub Actions` `Prometheus` `Grafana` `OpenTelemetry` `SARIF` `Ed25519` `Qdrant` `Redis` `Helm`

### Verification Standard

Each featured repo includes:
- `make test` / `pytest` — local verification
- Documented threat model with adversary/attack/mitigation table
- Known-limitations section
- CI workflow with least-privilege permissions
- Reproducible example commands

---

### Metrics

[![GitHub stats](https://github-readme-stats.vercel.app/api?username=poojakira&show_icons=true&hide=stars&count_private=true&include_all_commits=true&theme=transparent)](https://github.com/poojakira)
[![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=poojakira&layout=compact&theme=transparent)](https://github.com/poojakira)