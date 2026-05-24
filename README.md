# Pooja Kiran

ML Security Engineer candidate focused on LLM application security, model supply chain risk, adversarial ML, privacy attacks, and production ML platform controls.

M.S. Information Technology Security, Arizona State University. IEEE INDICON 2023 author. Honeywell Aerospace Lab background.

## 2026 Target

I am targeting ML Security Engineer / AI Security Engineer / MLSecOps roles where the work is practical:

- secure LLM/RAG and agentic systems against prompt injection, data leakage, unsafe tool use, and excessive agency
- scan, sign, and verify model artifacts before deployment
- threat-model ML systems using OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, and cloud/AppSec controls
- build detection, audit, rollback, and CI/CD gates around ML infrastructure
- document limitations honestly instead of selling demos as production systems

## Strongest Evidence

Live local evidence dashboard: [security-dashboard.html](security-dashboard.html). Rebuild with `python tools/build_security_dashboard.py`; it scans local repo files and avoids unsupported benchmark claims.

| Area recruiters screen for | Repository | Evidence |
| --- | --- | --- |
| Model supply chain security | [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Pickle opcode scanning, PyTorch archive inspection, SafeTensors validation, Ed25519 signing, SLSA-style provenance, YAML promotion policy gate, SARIF output |
| LLM application security | [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | Prompt injection patterns, output PII/secret scanning, RAG poisoning pipeline checks, OWASP LLM mapping, deterministic evidence tests, documented semantic bypass limits |
| Adversarial ML | [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | FGSM, PGD, C&W, AutoAttack-inspired attacks, PGD adversarial training, randomized smoothing, measured JSON/Markdown/SVG robustness reporting |
| ML privacy attacks | [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | Membership inference and model inversion implementations with stated threat models and DP-SGD gap called out |
| Secure ML serving | [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) | FastAPI inference, JWT auth, encryption, hash-chain audit log, rate-limit and leakage fixes, limitations documented |
| ML systems reliability | [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard) | CUDA fragmentation research prototype with dashboard wording corrected to demo/research telemetry only |
| Production ML controls | [production-ml-platform](https://github.com/poojakira/production-ml-platform) | Model registry, rollback, drift detection, A/B testing, auth, monitoring, online learning patterns; README now labels it a security prototype, not a verified production platform |
| Secure RAG infrastructure | [docquery](https://github.com/poojakira/docquery) | Qdrant retrieval, reranking, prompt versioning, citation grounding, fail-closed auth/rate-limit controls, no remote-code embedding load by default |
| Agentic system security | [coderev-agents](https://github.com/poojakira/coderev-agents) | LangGraph review prototype with untrusted diff hashing, line-numbered rendering, prompt-injection marker detection, and security routing for sensitive small diffs |

## Full Repository Map

| Repo | Keep visible? | Why |
| --- | --- | --- |
| [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Feature | Best direct match for 2026 MLSecOps and AI supply-chain hiring screens |
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | Feature | Direct LLM security surface: prompt injection, leakage, RAG poisoning |
| [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | Feature | Shows adversarial ML fundamentals and attack implementation |
| [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | Feature, but archived | Useful privacy-security proof; archive status means it should not be sold as active product work |
| [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) | Feature, but archived | Good security-control integration; README already admits limits and synthetic fixture caveats |
| [RTX-OOM-Guard](https://github.com/poojakira/RTX-OOM-Guard) | Support with caveat | ML systems depth; useful for infrastructure credibility, but public description/CI must match research-prototype status |
| [production-ml-platform](https://github.com/poojakira/production-ml-platform) | Support only | Good MLOps/control-plane concept; demo auth now fails closed and fake production metrics were removed |
| [docquery](https://github.com/poojakira/docquery) | Support | RAG architecture with security controls; performance metrics require generated artifacts before citation |
| [coderev-agents](https://github.com/poojakira/coderev-agents) | Support | Agentic trust-boundary prototype; unverified fine-tuning/benchmark claims removed |
| [CubeSat-Health-Monitor](https://github.com/poojakira/CubeSat-Health-Monitor) | De-emphasize | Good anomaly-detection demo, archived, synthetic telemetry |
| [Mission-Control-Telemetry-Simulator](https://github.com/poojakira/Mission-Control-Telemetry-Simulator) | De-emphasize | Systems/telemetry demo; not a core ML-security signal |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | De-emphasize | Predictive maintenance/MLOps demo; archived |
| [Aerospace-Trajectory-Simulator](https://github.com/poojakira/Aerospace-Trajectory-Simulator) | De-emphasize | Numerical methods demo; not security-aligned |
| [ESG-Carbon-Telemetry](https://github.com/poojakira/ESG-Carbon-Telemetry) | De-emphasize | Backend/data-pipeline demo; only weak security relevance through audit logging |
| [Orbital-IoT-Monitor](https://github.com/poojakira/Orbital-IoT-Monitor) | De-emphasize | Hardware/IoT telemetry demo; useful breadth, not ML security |
| [Pooja_Portfolio](https://github.com/poojakira/Pooja_Portfolio) | Archive/de-emphasize | Recruiter site, not engineering proof |
| [poojakira](https://github.com/poojakira/poojakira) | Feature | This profile README, used as the evidence index |

## Skill Coverage

| 2026 hiring signal | Current proof |
| --- | --- |
| AI/LLM security | LLM-Guard-Scanner, docquery, coderev-agents trust-boundary controls |
| Model artifact supply chain | Model-Supply-Chain-Auditor scan/sign/attest/policy flow |
| Adversarial ML | Adversarial-Robustness-Toolkit measured-report workflow |
| Privacy attacks | ML-Privacy-Attacks |
| Secure ML serving | Secure-ML-platform, production-ml-platform |
| Detection/response thinking | audit logs, SARIF, verification scripts, documented failure modes |
| Cloud/MLOps fundamentals | Docker, FastAPI, CI, registry/rollback, monitoring patterns |
| Research discipline | README limitations, threat models, references, reproducible scripts |

## Gaps I Am Actively Closing

- publish one end-to-end AI security lab that combines RAG, tool-use authorization, red-team tests, detections, and rollback
- add MITRE ATLAS and NIST AI RMF control mappings to the remaining security repos
- expand LLM-Guard-Scanner from deterministic baseline tests to a larger multilingual/adversarial corpus
- add SBOM/image signing/code-scanning upload workflows where local validation can prove they work
- replace any portfolio metric, live-demo claim, or CI claim that cannot be reproduced from checked-in scripts or current GitHub Actions with a documented artifact or remove it
- fix failing public CI before describing any repo as production-grade or recruiter-ready

## What I Am Not Claiming

- I do not claim these repos are production aerospace or enterprise security products.
- I do not claim prompt injection is solved by regex scanning.
- I do not claim synthetic telemetry is real satellite data.
- I do not claim benchmark numbers unless a repo contains the command, artifact, or documented limitation needed to reproduce them.

## References I Build Against

- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- MITRE ATLAS: https://atlas.mitre.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Cloud Security Alliance AI Controls Matrix: https://cloudsecurityalliance.org/artifacts/ai-controls-matrix

## Contact

Phoenix, AZ. Open to ML Security Engineer, AI Security Engineer, MLSecOps, and security-focused ML platform roles.
