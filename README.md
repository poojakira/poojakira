# Pooja Kiran
**ML Security Engineer**

Phoenix, AZ | [LinkedIn](https://www.linkedin.com/in/pooja-kiran/) | [GitHub](https://github.com/poojakira)

---

## Flagship ML Security Repositories

| Repository | Core Function | Security Property Demonstrated | Status |
|---|---|---|---|
| [Model-Supply-Chain-Auditor](https://github.com/poojakira/Model-Supply-Chain-Auditor) | Static analysis of pickle bytecode for malicious opcodes and Ed25519 model signing. | **Integrity**: Prevents arbitrary code execution via model weights and ensures artifact provenance. | ![CI](https://github.com/poojakira/Model-Supply-Chain-Auditor/actions/workflows/ci.yml/badge.svg) |
| [LLM-Guard-Scanner](https://github.com/poojakira/LLM-Guard-Scanner) | Lightweight scanner for prompt injection detection, PII leakage, and RAG poisoning. | **Input Validation**: Hardens LLM interfaces against adversarial prompts and sensitive data exfiltration. | ![CI](https://github.com/poojakira/LLM-Guard-Scanner/actions/workflows/ci.yml/badge.svg) |
| [ML-Privacy-Attacks](https://github.com/poojakira/ML-Privacy-Attacks) | Implementation of membership inference and model inversion attacks with DP-SGD defenses. | **Confidentiality**: Quantifies and mitigates training data leakage in deep learning models. | ![CI](https://github.com/poojakira/ML-Privacy-Attacks/actions/workflows/ci.yml/badge.svg) |
| [docquery](https://github.com/poojakira/docquery) | Production RAG pipeline with multi-tenant isolation and retrieval-stage security controls. | **Isolation**: Ensures data separation and prevents indirect prompt injection in retrieval-augmented systems. | ![CI](https://github.com/poojakira/docquery/actions/workflows/ci.yml/badge.svg) |
| [Adversarial-Robustness-Toolkit](https://github.com/poojakira/Adversarial-Robustness-Toolkit) | Adversarial attack suite (FGSM, PGD, C&W) and robust training implementations for vision models. | **Availability/Reliability**: Evaluates model performance under adversarial noise and implements hardening. | ![CI](https://github.com/poojakira/Adversarial-Robustness-Toolkit/actions/workflows/ci.yml/badge.svg) |
| [Secure-ML-platform](https://github.com/poojakira/Secure-ML-platform) | Infrastructure for secure model serving with JWT-based RBAC and hash-chained audit logs. | **Access Control**: Implements least-privilege access and non-repudiable auditing for ML infrastructure. | ![CI](https://github.com/poojakira/Secure-ML-platform/actions/workflows/ci.yml/badge.svg) |

---

## Technical Competencies

- **Adversarial ML**: Implementation of evasion, poisoning, and privacy attacks; adversarial training and defense.
- **ML Ops Security**: Model signing (Ed25519), SBOM generation, SLSA provenance, and secure artifact distribution.
- **LLM Security**: Prompt injection detection, PII redaction, and security controls for RAG pipelines.
- **Security Engineering**: JWT/OAuth2, RBAC, hash-chained logging, and automated security scanning (pip-audit, ruff).
- **Frameworks**: PyTorch, FastAPI, Qdrant, Docker, GitHub Actions.
- **Standards**: MITRE ATLAS, OWASP LLM Top 10, NIST AI RMF.


## Security & Limitations
This project is a research prototype and is not intended for production use. It has not been formally audited and may contain vulnerabilities. Specific limitations include:
- No formal guarantees of security or robustness.
- May not protect against all classes of attacks.


### Threat Model
This section outlines the assumed attacker capabilities and the scope of protection. We assume a "white-box" attacker with access to the model and data, but not necessarily the training infrastructure. We do not explicitly protect against zero-day exploits or highly sophisticated, targeted attacks beyond the scope of typical research prototypes.


## Data, Privacy, and Ethics
This project uses data that is either synthetic, publicly available, or anonymized. No sensitive personal data is used unless explicitly stated and justified. Users should be aware of the ethical implications of deploying ML models and ensure compliance with relevant privacy regulations.


## Supply Chain Security
To ensure the integrity of dependencies, we recommend running `pip-audit` or `safety` regularly. For model artifacts, hashes and verification steps should be documented to prevent tampering.
