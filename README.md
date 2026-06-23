# Pooja Kiran -- ML Security Engineer

**Phoenix, AZ** -- M.S. Information Technology Security, Arizona State University
F-1 OPT (STEM) -- Available July 2026 -- Seeking ML Security / AI Security roles

---

## Critical Security Focus Areas

| Area | What I Actually Do | Evidence |
|------|-------------------|----------|
| **ML Supply Chain Security** | Static scan of pickle/safetensors/PyTorch files for unsafe operations; Ed25519 sign/verify; SARIF output for CI integration | [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) |
| **LLM Application Security** | Prompt injection pattern detection, output leakage/SSN check, RAG poisoning heuristic checks | [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) -- OWASP LLM01/02/03/06 |
| **Adversarial ML** | FGSM, PGD, C&W, APGD, Square attacks; PGD-AT, TRADES, Randomized Smoothing defenses | [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) |
| **ML Privacy Attacks** | Shokri-style membership inference on UCI data | [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) |
| **Secure RAG** | Auth, rate limiting, citation grounding | [docquery](https://github.com/poojakira/docquery) |
| **Secure ML Serving** | JWT/RBAC, hash-chain audit, Prometheus metrics, Docker CI | [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) |
| **Standards Fluency** | OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF (threat models in repo docs) | `docs/THREAT_MODEL.md` in security repos |

---

## Portfolio Overview

| Repo | Description | Status |
|------|-------------|--------|
| [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Static scanner for model artifacts (pickle/safetensors) + Ed25519 signing + CI policy gate | Active |
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | Prompt injection, output leakage, RAG poisoning detectors | Active |
| [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | 5 attack + 3 defense implementations on CIFAR-10 with reproducible reports | Active |
| [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | Membership inference attack on UCI data | Active |
| [docquery](https://github.com/poojakira/docquery) | RAG with auth, rate limits, citation grounding | Active |
| [coderev-agents](https://github.com/poojakira/coderev-agents) | Agentic code review with trust boundary analysis | Active |
| [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) | JWT auth, audit chain, NASA C-MAPSS serving demo | Active |
| [production-ml-platform](https://github.com/poojakira/production-ml-platform) | Model registry, drift detection, A/B testing prototype | Active |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Secure MLOps pipeline on NASA benchmark with Docker CI | Active |
| RTX-OOM-Guard | Out-of-memory analysis for GPU workloads | Research |

---

## Verified Capabilities

- [x] **Adversarial attack implementation** -- FGSM, PGD, C&W, APGD, Square Attack (5 attack families)
- [x] **Adversarial defense implementation** -- PGD-AT, TRADES loss, Randomized Smoothing certification (3 defenses)
- [x] **Supply chain scanning** -- Unsafe op detection in pickle/safetensors, Ed25519 signing, SARIF output
- [x] **LLM prompt injection detection** -- Heuristic and pattern-based checks (not ML-based classifier)
- [x] **CI-integrated verification** -- GitHub Actions with lint, type check, coverage, and verification scripts
- [x] **Threat models** -- Documented per OWASP/MITRE ATLAS in security repos
- [x] **Reproducible evaluation** -- All metrics generated from live inference, not hardcoded
- [x] **Data lineage** -- Official dataset SHAs documented, verify.py scripts validate data integrity
- [ ] **Production deployment** -- Portfolio-scale prototypes, not deployed production systems
- [ ] **CVE disclosures** -- None published
- [ ] **Published research** -- IEEE INDICON 2023 (not ML security)

---

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| Attack implementations | 5 (FGSM, PGD, C&W, APGD, Square) | `src/attacks/` |
| Defense implementations | 3 (PGD-AT, TRADES, RS) | `src/defenses/` |
| Model parameters | ~11.2M (ResNet-18 CIFAR) | `verify.py:28` |
| Test coverage | >=70% (enforced in CI) | `.github/workflows/ci.yml` |
| CI checks | lint, format, type, verify, test, coverage | `.github/workflows/ci.yml` |
| Unit tests | 20+ across attacks, defenses, reports | `tests/test_attacks.py` |
| Repo documentation | Threat models, data lineage, evidence policies | `docs/` and `*_POLICY.md` |

---

## Security Engineering

- **Static model scanning** -- Detect unsafe operations in pickle and PyTorch archives (Model-Supply-Chain-Auditor)
- **Ed25519 signing** -- Sign and verify model artifacts for provenance (Model-Supply-Chain-Auditor)
- **SARIF CI output** -- Security scanner output formatted for GitHub Code Scanning integration
- **Policy gates** -- Promotion policy checks based on scan results
- **JWT access control** -- Bearer token auth with role-based endpoints (Secure-ML-platform)
- **Hash-chain audit logs** -- Tamper-evident audit trail for model serving requests
- **Rate limiting** -- Per-token and per-IP rate limits on RAG endpoints (docquery)

## ML & AI Security

- **Adversarial attacks**: FGSM, PGD, C&W L2, APGD (CE + DLR), Square Attack -- all with Linf or L2 perturbation budgets and [0,1] clipping
- **Adversarial defenses**: PGD adversarial training, TRADES loss, Randomized Smoothing certification
- **Robustness evaluation**: Automated pipeline that trains on CIFAR-10, evaluates clean + attack accuracy, generates JSON/MD/SVG reports
- **LLM security**: Prompt injection detection, output DLP pattern matching, RAG poisoning heuristics
- **Privacy**: Membership inference attack implementation (Shokri-style)

---

## Current Status

**F-1 OPT (STEM)** -- Seeking H1B sponsorship -- Open to onsite/hybrid/remote

- Available for interviews: June 2026
- Available start date: July 2026
- Preferred roles: ML Security Engineer, AI Security Engineer, MLSecOps Engineer

---

*These repos demonstrate security engineering patterns for hiring screens -- not certified production products. Every metric is generated from code, not fabricated.*
