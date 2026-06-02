# poojakira

**TL;DR**: ML Security Engineer Portfolio Component - poojakira
**Demo**: `make smoke`
**Evidence**: `sarif_output.json`

# Pooja Kiran

**Recruiter Demo:** `./run_evidence.sh` (outputs `evidence.json`, `evidence.sarif`)

ML Security Engineer candidate focused on LLM application security, model supply chain risk, adversarial ML, privacy attacks, and production ML platform controls.

M.S. Information Technology Security, Arizona State University. IEEE INDICON 2023 author. Honeywell Aerospace Lab background.

## 2026 Target

I am targeting ML Security Engineer / AI Security Engineer / MLSecOps roles where the work is practical:

- secure LLM/RAG and agentic systems against prompt injection, data leakage, unsafe tool use, and excessive agency
- scan, sign, and verify model artifacts before deployment
- threat-model ML systems using OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, and cloud/AppSec controls
- build detection, audit, rollback, and CI/CD gates around ML infrastructure
- document limitations honestly instead of selling demos as production systems

## 2026 ML Security Map

### Supply Chain Security
- **[Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor)** — Pickle/PyTorch artifact scanning, SafeTensors validation, Ed25519 signing, SARIF output. Shows how to catch malicious model weights pre-deployment.

### LLM & RAG Security
- **[LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner)** — Prompt injection patterns, PII/secret output scanning, RAG poisoning checks mapped to OWASP LLM Top 10. Deterministic baseline for LLM application defense.
- **[docquery](https://github.com/poojakira/docquery)** — RAG pipeline with Qdrant retrieval, reranking, prompt versioning, fail-closed auth/rate-limit controls. Evidence of hardened vector retrieval.
- **[coderev-agents](https://github.com/poojakira/coderev-agents)** — LangGraph agentic prototype with untrusted diff hashing, line-numbered rendering, prompt-injection markers. Shows trust-boundary thinking in multi-agent systems.

### Adversarial ML
- **[Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit)** — FGSM, PGD, C&W, AutoAttack-inspired attacks. Includes measured defenses with documented accuracy/robustness trade-offs and limitations.

### Privacy Attacks
- **[ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks)** — Membership inference (Shokri 2017) and model inversion (Fredrikson 2015). Quantifies privacy leakage with reproducible plots and DP-SGD gap analysis.

### Secure ML Serving & Production Controls
- **[production-ml-platform](https://github.com/poojakira/production-ml-platform)** — FastAPI inference, JWT auth, encryption, hash-chain audit logging, drift detection, and dependency scanning. Uses official NYC TLC dataset with hash verification. Canonical secure-serving reference.
- **[RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard)** — PyTorch CUDA memory fragmentation monitoring and tensor compaction. Shows ML systems depth and infrastructure-level security thinking.

### Production ML Rigor (Gold Standard)
- **[PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting)** — Official NASA C-MAPSS FD001 predictive-maintenance system with data lineage, threat model, CI gates, auth/RBAC, tenant audit, and measured evidence. **This is what secure, auditable ML looks like end-to-end.**

---

## Strongest Evidence by Hiring Signal

| Area recruiters screen for | Repository | Evidence |
| --- | --- | --- |
| Model supply chain security | [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Pickle opcode scanning, PyTorch archive inspection, SafeTensors validation, Ed25519 key management, SARIF reporting, threat model, CI gates |
| LLM application security | [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) + docquery | Prompt injection patterns, output PII/secret scanning, RAG poisoning pipeline checks, OWASP LLM mapping, attack corpus |
| Adversarial ML fundamentals | [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | FGSM, PGD, C&W attacks, adversarial training defenses, documented accuracy/robustness trade-offs, reproducible results table |
| ML privacy attacks | [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | Membership inference, model inversion, privacy leakage quantification, DP-SGD defense comparison, reproducible metrics |
| Secure ML serving | production-ml-platform + Secure-ML-platform | FastAPI inference, JWT auth, encryption, hash-chain audit log, rate-limit and leakage fixes, real NYC TLC dataset with hash verification |
| ML systems infrastructure | [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard) | CUDA fragmentation research, tensor compaction, memory usage visualization, documented limitations |
| Production ML controls | [production-ml-platform](https://github.com/poojakira/production-ml-platform) | Model registry, rollback, drift detection, A/B testing, auth, RBAC, dependency audit, tenant isolation |
| Agentic system security | [coderev-agents](https://github.com/poojakira/coderev-agents) | LangGraph review agents, untrusted input handling, prompt-injection markers, tool authorization thinking |
| Governed ML systems | [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | NASA official data, data lineage, threat model, CI gates, auth/RBAC, tenant audit, measured CI evidence |

---

## Full Repository Map

| Repo | Status | Reason |
| --- | --- | --- |
| [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | **Feature** | Highest-signal for 2026 MLSecOps and AI supply-chain hiring |
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | **Feature** | Direct LLM security surface: prompt injection, data leakage, RAG poisoning |
| [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | **Feature** | Adversarial ML attack/defense fundamentals with measured trade-offs |
| [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | **Feature** | Privacy-attack quantification with reproducible metrics |
| [production-ml-platform](https://github.com/poojakira/production-ml-platform) | **Feature** | Canonical secure ML platform with real data and controls |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | **Feature** | Gold standard: governed ML system with NASA data, lineage, threat model, CI gates |
| [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) | **Archived** | Earlier version of production-ml-platform; kept for reference |
| [docquery](https://github.com/poojakira/docquery) | **Support** | RAG pipeline security; shows vector-retrieval hardening |
| [coderev-agents](https://github.com/poojakira/coderev-agents) | **Support** | Agentic trust-boundary thinking and prompt-injection defense |
| [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard) | **Support** | ML infrastructure and CUDA-level security awareness |
| [CubeSat-Health-Monitor](https://github.com/poojakira/CubeSat-Health-Monitor) | **Archived** | Anomaly detection demo; synthetic telemetry |
| [Mission-Control-Telemetry-Simulator](https://github.com/poojakira/Mission-Control-Telemetry-Simulator) | **Archived** | Systems/telemetry demo; not security-aligned |
| [Aerospace-Trajectory-Simulator](https://github.com/poojakira/Aerospace-Trajectory-Simulator) | **Archived** | Numerical methods demo; not security-aligned |
| [ESG-Carbon-Telemetry](https://github.com/poojakira/ESG-Carbon-Telemetry) | **Archived** | Backend/data-pipeline demo |
| [Orbital-IoT-Monitor](https://github.com/poojakira/Orbital-IoT-Monitor) | **Archived** | Hardware/IoT telemetry demo |
| [Pooja_Portfolio](https://github.com/poojakira/Pooja_Portfolio) | **Archived** | Web portfolio; not engineering proof |

---

## Skill Coverage

| 2026 hiring signal | Current proof |
| --- | --- |
| AI/LLM security (A01–A10) | LLM-Guard-Scanner (OWASP mapped), docquery, coderev-agents trust-boundary controls |
| Model artifact supply chain | Model-Supply-Chain-Auditor scan/sign/attest/policy flow |
| Adversarial ML | Adversarial-Robustness-Toolkit measured attack/defense trade-offs |
| Privacy attacks & defenses | ML-Privacy-Attacks with DP-SGD gap analysis |
| Secure ML serving & auth | production-ml-platform FastAPI + JWT + encryption + audit log |
| Detection/response thinking | SARIF output, audit logs, verification scripts, documented failure modes |
| Cloud/MLOps fundamentals | Docker, FastAPI, CI gates, registry/rollback, dependency audit, monitoring |
| Governed ML systems | PulseNet-RUL-Forecasting (NASA data, lineage, threat model, RBAC, CI gates) |
| Research discipline | README limitations, threat models, references, reproducible scripts |

---

## Gaps I Am Actively Closing

- **Model-Supply-Chain-Auditor**: Add before/after scanning story, threat model of what is NOT protected, CI/GitHub Actions SARIF upload workflow, tests/ folder with malicious artifacts
- **LLM-Guard-Scanner**: Expand OWASP A01–A10 mapping table, add attacks/ corpus with real prompt-injection examples and expected scanner output, add precision/recall benchmarks
- **ML-Privacy-Attacks**: Add privacy-leakage plots, reproducible metrics command, DP-SGD defense with trade-off analysis
- **Adversarial-Robustness-Toolkit**: Add results table (clean vs robust accuracy for each defense), YAML config for attack/defense combinations, production-readiness caveats
- **RTX-OOM-Guard**: Add concrete scenario with fragmentation visualization, training loop integration example
- **production-ml-platform**: Add architecture diagram (ASCII or PNG), STRIDE threat model, cloud-mapping notes (KMS, secrets manager, IAM)
- **PulseNet-RUL-Forecasting**: Add CI gate screenshots, lineage report examples, short narrative emphasizing governance end-to-end
- **docquery & coderev-agents**: Add threat/mitigation sections, security rule packs, end-to-end demo flows with output logs
- Add MITRE ATLAS and NIST AI RMF control mappings to remaining security repos
- Replace any portfolio metric or CI claim that cannot be reproduced from checked-in scripts with documented artifacts or remove it

---

## What I Am Not Claiming

- I do not claim these repos are production aerospace or enterprise security products.
- I do not claim prompt injection is solved by regex scanning.
- I do not claim synthetic telemetry is real satellite data.
- I do not claim benchmark numbers unless a repo contains the command, artifact, or documented limitation needed to reproduce them.
- I do not claim that one model defense works against all attacks or certified robustness without stating the threat model and attacker budget.
- I do not claim fine-tuning or training claims unless published benchmarks and artifacts are available.

---

## References I Build Against

- **OWASP Top 10 for LLM Applications**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **MITRE ATLAS**: https://atlas.mitre.org/
- **NIST AI Risk Management Framework**: https://www.nist.gov/itl/ai-risk-management-framework
- **Cloud Security Alliance AI Controls Matrix**: https://cloudsecurityalliance.org/artifacts/ai-controls-matrix
- **Shokri et al. (2017) – Membership Inference Attacks**: https://arxiv.org/abs/1610.05820
- **Fredrikson et al. (2015) – Model Inversion Attacks**: https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/fredrikson

---

## Threat Model

- **Assets**: ML Models, Training Data, User Queries, System Availability
- **Adversaries**: Script kiddies (model theft, prompt injection), sophisticated attackers (supply-chain compromise, privacy attacks, adversarial examples), insider threats (data exfiltration)
- **Mitigations**: Hardened CI/CD (signed artifacts, SBOM, supply-chain scanning), Input Validation (prompt sanitization, rate limiting), Encryption (data at rest/in transit), RBAC/audit logging, Rollback and detection capabilities, Differential privacy (defenses)

---

## Contact

Phoenix, AZ. Open to **ML Security Engineer**, **AI Security Engineer**, **MLSecOps**, and security-focused ML platform roles.

**Links**: [Portfolio](https://pooja-kiran.com) | [LinkedIn](https://linkedin.com/in/poojakiran) | Email: contact@pooja-kiran.com
