# Pooja Kiran — ML Security Engineer

Building security tooling for the ML lifecycle: model supply chain security, LLM red-teaming, adversarial robustness, and privacy-preserving ML.

[GitHub](https://github.com/poojakira) · [LinkedIn](https://linkedin.com/in/poojakiran)

## Projects

| Repo | What It Does | Key Threat | Status | Evidence |
|------|-------------|-----------|--------|----------|
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | FastAPI scan service: prompt injection, PII leakage, RAG poisoning → SARIF output, PR gate | LLM01 Prompt Injection | F1=0.70 OOD / 0.93 curated | [`results/scan_metrics.json`](https://github.com/poojakira/llm-redteam-framework/blob/main/results/scan_metrics.json) |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Scan HuggingFace models for supply chain attacks; Ed25519 model signing | T1683.001 ML Supply Chain | 12/12 internal fixture suite | [`tests/redteam/`](https://github.com/poojakira/hf-model-provenance-scanner/tree/main/tests/redteam) |
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | MCP tool-call security monitor — layered call inspection and policy decisions | T1684, T1687 | P99 < 5ms per tool call | [`benchmark/`](https://github.com/poojakira/mcp-security-gateway-monitor/tree/main/benchmark) |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/C&W attacks on CIFAR-10 ResNet-18; Madry adversarial training | AML.T0043 Craft Adversarial Data | Literature-consistent results (no weights committed) | [`results/cifar10_resnet18_benchmark.json`](https://github.com/poojakira/adversarial-ml-lab/blob/main/results/cifar10_resnet18_benchmark.json) |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Yeom MIA, Fredrikson inversion, DP-SGD defense (synthetic data) | T1685 ML Privacy | MIA advantage=0.42; ε=1.16 at σ=4.0 | [`results/mia_advantage_report.json`](https://github.com/poojakira/model-privacy-attacks/blob/main/results/mia_advantage_report.json) |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Anomaly screening for training data integrity | T1685, T1688 | Research baseline | [`README.md`](https://github.com/poojakira/dataset-poisoning-detector/blob/main/README.md) |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Jointly authored RUL forecasting and anomaly-serving research; STRIDE threat model | 12 STRIDE surfaces | F1=0.54 Isolation Forest, NASA C-MAPSS FD001 | [`docs/evidence/validation_results.json`](https://github.com/poojakira/PulseNet-RUL-Forecasting/blob/main/docs/evidence/validation_results.json) |

## Security Engineering Focus

- **Threat Modeling**: STRIDE across ML pipelines; MITRE ATLAS + ATT&CK v19 mapping
- **Privacy**: Membership inference (Yeom 2018), model inversion (Fredrikson 2015), DP-SGD
- **Supply Chain**: Ed25519 model signing, SHA-256 artifact manifests, SARIF CI gates
- **LLM Security**: OWASP LLM Top 10, RAG poisoning detection, canary token tracking
- **Adversarial ML**: FGSM, PGD, C&W attacks; Madry AT on CIFAR-10 ResNet-18

## Evidence Policy

All metrics link to committed JSON artifacts in their respective repositories. Synthetic data results are marked as such. Each repo README states what is and is not production-ready. No metric is claimed without a reproducible evidence file.
