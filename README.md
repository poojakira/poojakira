# Pooja Kiran

I build security controls for AI agents  -  the kind that hold delegated credentials, invoke external tools, and make autonomous decisions that existing security tooling wasn't designed for.

## Primary Work

| Repository | Problem It Solves | Evidence |
|-----------|------------------|----------|
| [mcp-agent-security-gateway](https://github.com/poojakira/mcp-agent-security-gateway) | MCP tool calls cross trust boundaries with no inspection point | 5-layer pipeline, 0.015ms latency, 529 tests, 9 attack classes |
| [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard) | Agent IAM roles get provisioned with wildcard permissions nobody audits | 25 rules, 0 deps, CI merge gate, SARIF output |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Model files execute arbitrary code on load and nobody checks | 12/12 detections (incl. CVE-2026-46432 missed by ModelScan), 116ms, 99.9% bandwidth reduction |

Each has a [DESIGN_DECISIONS.md](https://github.com/poojakira/mcp-agent-security-gateway/blob/main/DESIGN_DECISIONS.md) explaining the architecture rationale  -  not just what was built, but what was considered and rejected.

## Detection & Response Stack

These tools don't exist in isolation  -  they feed into operational security workflows:

- **SIEM integration**  -  the MCP gateway's SHA-256 hash-chained audit logs forward to Splunk and Microsoft Sentinel via structured JSON over syslog. I wrote correlation rules for detecting multi-step agent compromise patterns (tool-call anomalies -> credential access -> lateral movement) across 15-minute sliding windows.
- **SOAR playbooks**  -  built automated response playbooks in Splunk SOAR (Phantom) and Cortex XSOAR for agent-specific incidents: auto-revoke agent IAM role on critical finding, isolate MCP tool server on exfiltration detection, trigger model quarantine on supply-chain alert.
- **EDR telemetry**  -  the process-spawn evaluation layer (Layer 3) in the MCP gateway was designed to produce EDR-compatible telemetry. Events map to CrowdStrike Falcon and Microsoft Defender for Endpoint process tree schemas, enabling SOC analysts to trace agent-initiated process spawns back to the original tool call.

The detection engineering work: I authored Sigma rules for agent-specific TTPs (credential chaining via sts:AssumeRole sequences, tool-call injection patterns in CloudTrail, model file hash changes indicating supply-chain compromise) and tested them against Elastic Security and Splunk ES.

## Supporting Work

| Repository | Role |
|-----------|------|
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/C&W robustness benchmark, MITRE ATLAS mapped |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Prompt injection classifier (F1=0.70 OOD), FastAPI + SARIF |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Training data anomaly detection, 12,400 samples/sec |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | MIA + model inversion with DP-SGD countermeasures |
| [attack-v19-core](https://github.com/poojakira/attack-v19-core) | MITRE ATT&CK v19 data models shared across all repos |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Secure MLOps reference (archived, NASA C-MAPSS) |

## Background

- MS Information Technology, Arizona State University (May 2026)
- 2 years building AI security tooling full-time alongside coursework
- Focus: agentic AI security, MCP protocol security, LLM security, IAM for autonomous agents, model supply-chain integrity
- Operational security: Splunk (ES + SOAR), Microsoft Sentinel, Cortex XSOAR, CrowdStrike Falcon, Elastic Security, Sigma rule authoring
- F-1 OPT EAD. Available now. Open to relocating to SF.

## Contact

[LinkedIn](https://linkedin.com/in/poojakiran) | [Portfolio](https://pooja-kiran-portfolio-website.vercel.app)
