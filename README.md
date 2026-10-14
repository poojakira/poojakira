<p align="center">
  <img src="./assets/security-engineering-mesh.svg" width="100%" alt="Technical illustration of agent, identity and model artifact trust boundaries" />
</p>

# Pooja Kiran
**Security Engineer · AI & Agent Security · Application Security · Cloud IAM**

I build security tooling for AI execution paths, workload identities, and model supply chains. My focus is on practical enforcement, deterministic analysis, automated regression testing, and engineering evidence that can be independently inspected.

[Portfolio](https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/) · [Technical resume](https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/Pooja_Kiran_Agentic_AI_Security_Engineer_Resume.pdf) · [LinkedIn](https://www.linkedin.com/in/poojakiran)

## Selected engineering work

### [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)
Default-deny MCP/JSON-RPC request gateway with capability authorization, prompt-injection inspection, PII/exfiltration checks, anti-SSRF controls, rate limiting, tamper-evident audit records, and SIEM integration.

**Engineering evidence:** [782 passing tests, 81.93% statement coverage](https://github.com/poojakira/mcp-agent-security-gateway/actions/runs/38012954359) in a dated Python 3.12 CI run. Separate source inventory: 69 detector signatures and 9 Elastic Security rules.

### [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)
Static AWS IAM policy analysis with 25 deterministic rule IDs covering excessive permissions, role trust, privilege escalation paths, and audit-control weaknesses. Exports text, JSON, and SARIF 2.1.0 findings for developer review.

**Engineering evidence:** [244 passing tests](https://github.com/poojakira/aws-agent-identity-guard/actions/runs/38009457205) in a dated CI run; three credential-dependent checks were skipped.

### [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Non-executing inspection of supported model artifacts, with serialization-risk analysis, provenance checks, and dependency evidence. Untrusted model code is not executed by default.

**Engineering evidence:** [260 passing tests, 75.67% statement coverage](https://github.com/poojakira/hf-model-provenance-scanner/actions/runs/38002138828) in a dated CI run; 33 of 33 committed adversarial fixtures flagged in a separate, bounded evaluation.

## Other systems

[LLM Red-Team Framework](https://github.com/poojakira/llm-redteam-framework) · [Dataset Poisoning Detector](https://github.com/poojakira/dataset-poisoning-detector) · [Adversarial ML Lab](https://github.com/poojakira/adversarial-ml-lab) · [ML Security Benchmark Suite](https://github.com/poojakira/mlsec-benchmark-suite) · [Unified ML Security Platform](https://github.com/poojakira/unified-ml-security-platform)

## Engineering foundation

**Languages and platforms:** Python, Rust, C++, Bash, FastAPI, Docker, GitHub Actions, AWS.

**Security and testing:** API security, IAM, least privilege, MCP/JSON-RPC, threat modeling, pytest, SARIF, CodeQL, Elastic Security, SIEM telemetry.

**Education:** M.S., Information Technology (Security), Arizona State University, 2026.

**Experience:** Independent security engineering; Graduate Teaching Assistant and IT Grader; Business & Compliance Lead, AEROSEC academic technology externship (Aug–Dec 2025).

---

The measurements above refer to identified CI snapshots and controlled tests, not production deployment outcomes or generalized attack-detection guarantees. Source code, tests, limitations, and dated evidence are available in the linked repositories.

**Contact:** poojakiranbhardwaj@gmail.com · Tempe, Arizona · Open to U.S. on-site and hybrid roles.

<sub>Review the repository [LICENSE](LICENSE) before reusing original materials.</sub>
