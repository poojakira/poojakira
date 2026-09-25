# Pooja Kiran — Security Engineer

I build security controls for AI systems, cloud identities, and model supply chains.

My current work focuses on three boundaries that are easy to describe and hard to secure well: **agent-to-tool execution**, **cloud permissions**, and **model artifacts before load**.

## Flagship projects

### [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)
Inline MCP/JSON-RPC inspection for agent tool calls, with policy decisions, prompt-injection signals, audit logging, telemetry, and a local Elastic detection lab.

- Current verified CI baseline: **648 passing tests, 79.61% statement coverage**
- Evidence: [VERIFIED_METRICS.md](https://github.com/poojakira/mcp-agent-security-gateway/blob/main/VERIFIED_METRICS.md)
- Scope: production-oriented security gateway; enforcement applies only to traffic routed through a supported integration path

### [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)
Static IAM analysis for AI-agent and tool-executor roles, including identity-policy, trust-policy, and permission-boundary checks.

- **25 deterministic rule IDs**
- Fresh CI evidence: **235 passed, 3 skipped**
- Performance is reported as a synthetic CI gate, not production throughput
- Evidence: [VERIFIED_METRICS.md](https://github.com/poojakira/aws-agent-identity-guard/blob/main/VERIFIED_METRICS.md)

### [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Pre-load scanning for model repositories, including pickle-risk, provenance, impersonation, and model-supply-chain signals.

- Fixture-scoped detection evidence is documented in the repository
- No claim of real-world detection rate or commercial scanner parity
- Evidence: [VERIFIED_METRICS.md](https://github.com/poojakira/hf-model-provenance-scanner/blob/main/VERIFIED_METRICS.md)

## Supporting work

- [LLM Red Team Framework](https://github.com/poojakira/llm-redteam-framework) — prompt-injection evaluation with grouped and out-of-distribution testing
- [Dataset Poisoning Detector](https://github.com/poojakira/dataset-poisoning-detector) — streaming/statistical screening with explicit benchmark limitations
- [Adversarial ML Lab](https://github.com/poojakira/adversarial-ml-lab) — adversarial robustness measurement
- [ML Security Benchmark Suite](https://github.com/poojakira/mlsec-benchmark-suite) — cross-project regression and fixture harness
- [ATT&CK v19 Core](https://github.com/poojakira/attack-v19-core) — shared ATT&CK v19 mapping utilities
- [Unified ML Security Platform](https://github.com/poojakira/unified-ml-security-platform) — deployable integration gateway and normalized service topology for the security tools above

## Engineering principles

- **Attach scope to every metric.** A test count, F1 score, or latency number is incomplete without the environment and dataset.
- **Separate detection from enforcement.** A component that returns a decision is not a firewall unless it actually controls execution.
- **Prefer reproducible evidence over adjectives.** CI, committed fixtures, and explicit limitations carry more weight than "production-ready."
- **Treat failure modes as part of the design.** Security behavior during parse errors, unavailable dependencies, and incomplete scans is documented and tested.

## Research and publications

- [A Personalized E-Learning System Using Reinforcement Learning Through Satellite](https://ieeexplore.ieee.org/document/10440852) — IEEE INDICON 2023 proceedings
- [Smart Charge Pro: Empowering Future Mobility With Advanced Safety And Efficiency In Electric Vehicle Charging Infrastructure](https://www.iosrjournals.org/iosr-jce/pages/25(4)Series-1.html) — IOSR-JCE, 2023

## Links

- Portfolio: https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/
- Provenance ledger: [PROVENANCE_LEDGER.md](PROVENANCE_LEDGER.md)
- LinkedIn: https://www.linkedin.com/in/poojakiran/
- Email: poojakiranbhardwaj@gmail.com

<sub>Quantitative claims above are intentionally limited to values with repository-level evidence.</sub>
