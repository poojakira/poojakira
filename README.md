# Pooja Kiran

Security engineer focused on AI/ML workload protection on AWS. I build tools that catch real misconfigurations before they become incidents.

## What I Ship

### [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)
Static IAM policy linter for AI agent roles. 22 rules targeting Bedrock, SageMaker, Lambda, and ECS agent permissions. Zero runtime dependencies. SARIF output for CI gating.

```bash
pip install aws-agent-identity-guard
aws-agent-identity-guard deploy/agent-role-policy.json
```
Catches: unconstrained PassRole, wildcard tool execution, Bedrock control-plane in runtime roles, audit-trail tampering, missing session tags.

### [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Supply chain security scanner for HuggingFace models. Detects malicious pickle opcodes, safetensors metadata injection, obfuscated Python, and typosquatted organizations. Taint engine with symbolic resolution — capabilities not in Protect AI's ModelScan.

- 12/12 internal incident-reproduction fixtures detected
- FP rate: 5.9% on known-good configs from meta-llama, google, mistralai, microsoft
- P99 < 5ms for header-only mode

## Research & Reference Implementations

| Repo | What | Honest Status |
|------|------|---------------|
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | MCP tool-call security monitor | 51% detection — architecture prototype, not production |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership inference + DP-SGD | Educational. Synthetic data only. |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/C&W attack library | Educational. Use IBM ART for production. |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Secure MLOps reference architecture | STRIDE threat model + security controls. F1=0.54 ML. |
| [attack-v19-core](https://github.com/poojakira/attack-v19-core) | MITRE ATT&CK v19 data models | Typed Pydantic wrapper + v19 revocation map |

## What I Focus On

- **IAM for AI agents** — Least-privilege policies for Bedrock, SageMaker, MCP servers
- **Model supply chain** — Binary analysis of pickle/safetensors/GGUF without execution
- **Workflow automation** — n8n pipelines for scan orchestration, alert routing, and automated quarantine
- **Threat modeling** — STRIDE for ML pipelines, MITRE ATT&CK v19 mapping
- **Zero-cost tooling** — Stdlib-only Python, n8n Community Edition, no paid services required

## Evidence Policy

Every metric in this profile links to a committed artifact. Synthetic results are labeled. No metric is claimed without a reproducible evidence file. I'd rather report F1=0.54 honestly than fake 0.95.
