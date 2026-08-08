# Pooja Kiran

I build security tooling for AI agent infrastructure.

[GitHub](https://github.com/poojakira) · [LinkedIn](https://linkedin.com/in/poojakiran)

## Tools

### [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)
Static IAM policy linter for AI agent roles. 22 rules. Catches overprivileged Bedrock/SageMaker/Lambda agent permissions before they deploy. Zero dependencies. Blocks bad deploys in CI.

### [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Supply chain security scanner for ML models. Detects pickle RCE, safetensors injection, typosquatting, and obfuscated payloads. Taint engine with symbolic resolution. Catches attacks ModelScan misses.

### [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor)
JSON-RPC 2.0 proxy for MCP tool calls. Inspects every tool-call argument for injection, exfiltration, and poisoning. 55 detection patterns with Unicode normalization. Blocks before execution.

## Supporting Tools

| Repo | What |
|------|------|
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Secure MLOps pipeline with JWT revocation, WORM audit logs, STRIDE threat model |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Spectral signature detection for training data poisoning (Tran et al. 2018) |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Prompt injection detection service with 80-pattern seed corpus from HackAPrompt/Gandalf |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/C&W adversarial robustness testing with CIFAR-10 benchmarks |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership inference attacks with UCI Adult Income benchmarks |
| [attack-v19-core](https://github.com/poojakira/attack-v19-core) | MITRE ATT&CK data models with CLI lookup and Navigator layer generation |
| [unified-ml-security-platform](https://github.com/poojakira/unified-ml-security-platform) | API gateway aggregating all scanning tools behind a single endpoint |
| [mlsec-benchmark-suite](https://github.com/poojakira/mlsec-benchmark-suite) | Automated benchmarking across all tools with signed evidence |
| [ml-security-command-center](https://github.com/poojakira/ml-security-command-center) | Portfolio metrics dashboard with live data from all tools |
| [mlsec-dashboards](https://github.com/poojakira/mlsec-dashboards) | Dashboard server with authentication and real-time metrics API |

## Focus

- Per-call authorization enforcement for AI agents on AWS
- Model supply chain integrity (pickle/safetensors/GGUF binary analysis)
- MCP protocol security (40+ CVEs in 2026, zero open-source defenses existed)
- n8n workflow automation for SOC integration
