# Pooja Kiran Bharadwaj

AI Security Engineer. I build detection and enforcement tools for ML/AI systems — scanning model files before they execute, intercepting dangerous tool calls, and analyzing cloud permissions for AI agent roles.

---

## Flagship Projects

### [mcp-agent-security-gateway](https://github.com/poojakira/mcp-agent-security-gateway)
Security middleware for MCP (Model Context Protocol) tool calls. Sits between AI agents and the tools they invoke, inspecting every call for prompt injection, PII leakage, and exfiltration patterns.

`17 stars` · `5 forks` · `114 commits` · CI passing · Python/FastAPI

---

### [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Scans Hugging Face model repositories for pickle exploits, supply-chain attacks, and provenance issues — without downloading full model weights. Fetches only file headers via HTTP Range requests.

- 350 tests passing · CI green on Python 3.10/3.11/3.12
- Scanned top 100 most-downloaded HF models
- 12/12 red-team attacks detected (JFrog, Sonatype, CRLF bypass techniques)
- Runtime inference monitor — intercepts `torch.load()` before execution
- Cryptographic provenance ledger — hash-chained, Ed25519-signed event log
- Model quality evaluator — bias, drift, and accuracy monitoring
- Output: SARIF 2.1, CycloneDX 1.5, MITRE ATT&CK mapping

---

### [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)
Static IAM policy analyzer for AI agent roles on AWS. Detects privilege escalation paths, credential-harvesting patterns, and audit-trail suppression in IAM policies. SARIF output for CI integration.

`64 commits` · CI passing · Python

---

## Other Projects

| Project | What it does |
|---------|-------------|
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/C&W robustness benchmarks for CIFAR-10 (MITRE ATLAS AML.T0043) |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Automated prompt injection and jailbreak simulation (OWASP LLM Top 10) |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership inference and model inversion attack implementations |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Statistical anomaly detection for training data integrity |
| [attack-v19-core](https://github.com/poojakira/attack-v19-core) | MITRE ATT&CK v19 data models and technique lookup for Python |
| [unified-ml-security-platform](https://github.com/poojakira/unified-ml-security-platform) | Orchestration layer integrating the above tools |
| [mlsec-benchmark-suite](https://github.com/poojakira/mlsec-benchmark-suite) | Cross-project benchmark harness for ML security tooling |

---

## Skills

**Languages & Frameworks**: Python · FastAPI · pytest

**Security**: MITRE ATT&CK · MITRE ATLAS · SARIF · Sigma rules · CodeQL · Bandit · pip-audit · Trivy · Grype

**AI/ML Security**: Prompt injection detection · Model supply-chain verification · Adversarial robustness · MCP protocol security · Pickle exploit analysis

**Cloud**: AWS IAM · STS credential chains · Least-privilege policy analysis

---

## Background

MS Information Technology, Arizona State University (2026). IEEE published researcher (INDICON 2023). 16 public repos, 15 with CI passing.

---

## Contact

[LinkedIn](https://linkedin.com/in/poojakiran) · pooja.kiran@asu.edu

F-1 OPT EAD | Greater Phoenix Area
