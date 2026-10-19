<!-- Profile README for @poojakira -->

<p align="center">
  <img src="https://raw.githubusercontent.com/poojakira/poojakira/main/assets/profile-banner.svg" alt="Pooja Kiran — Security Engineering" width="100%" />
</p>

<h1 align="center">Pooja Kiran</h1>
<p align="center">
  <strong>Security Engineer · AI & Agent Security · Application Security · Cloud IAM</strong>
</p>

<p align="center">
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/">Portfolio</a> ·
  <a href="https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/Pooja_Kiran_Agentic_AI_Security_Engineer_Resume.pdf">Technical Resume</a> ·
  <a href="https://www.linkedin.com/in/poojakiran/">LinkedIn</a>
</p>

I build security tooling for AI execution paths, workload identities, and model supply chains. My work focuses on practical policy enforcement, deterministic analysis, automated regression testing, and engineering evidence that can be independently inspected.

## Selected engineering work

### [MCP Agent Security Gateway](https://github.com/poojakira/mcp-agent-security-gateway)
Default-deny MCP/JSON-RPC request gateway that inspects selected agent-to-tool calls before execution, with capability authorization, prompt-injection inspection, sensitive-data/exfiltration checks, anti-SSRF controls, rate limiting, tamper-evident audit records, and SIEM integration.

- **782 passing tests · 81.93% statement coverage** in a dated hosted Python 3.12 CI run.
- **69 named runtime detector signatures** and nine Elastic Security rules (source-inventory counts, not real-world detection rates).
- [CI evidence](https://github.com/poojakira/mcp-agent-security-gateway/actions/runs/38462601803) · [Repository](https://github.com/poojakira/mcp-agent-security-gateway)

### [AWS Agent Identity Guard](https://github.com/poojakira/aws-agent-identity-guard)
Static AWS IAM policy analysis with 25 deterministic rule IDs covering excessive permissions, role trust, privilege-escalation paths, and audit-control weaknesses. Exports text, JSON, and SARIF 2.1.0 findings.

- **244 passed / 3 skipped** in a dated CI run; skipped checks require live AWS credentials.
- [CI evidence](https://github.com/poojakira/aws-agent-identity-guard/actions/runs/38009457205) · [Repository](https://github.com/poojakira/aws-agent-identity-guard)

### [HF Model Provenance Scanner](https://github.com/poojakira/hf-model-provenance-scanner)
Non-executing inspection of supported model artifacts, serialization risks, provenance, and dependency evidence. Untrusted model code is not executed by default.

- **260 passed / 1 skipped · 75.67% coverage** in a dated CI run.
- **33/33 curated adversarial fixtures flagged** in a bounded evaluation; this is fixture evidence, not a general detection guarantee.
- [CI evidence](https://github.com/poojakira/hf-model-provenance-scanner/actions/runs/38002138828) · [Repository](https://github.com/poojakira/hf-model-provenance-scanner)

## More security engineering

- [LLM Red-Team Framework](https://github.com/poojakira/llm-redteam-framework) — structured adversarial testing for LLM applications.
- [Dataset Poisoning Detector](https://github.com/poojakira/dataset-poisoning-detector) — dataset-integrity and poisoning analysis.
- [Adversarial ML Lab](https://github.com/poojakira/adversarial-ml-lab) — experiments and tests for adversarial machine learning.
- [ML Security Benchmark Suite](https://github.com/poojakira/mlsec-benchmark-suite) — evaluation harnesses for ML security.
- [Unified ML Security Platform](https://github.com/poojakira/unified-ml-security-platform) — integrated ML security tooling.

## Engineering toolkit

**Languages & platforms:** Python, Rust, C++, Bash, FastAPI, Docker, GitHub Actions, AWS  
**Security:** AI/LLM security, MCP/JSON-RPC, application security, IAM and least privilege, threat modeling, model supply-chain security  
**Testing & detection:** pytest, SARIF, CodeQL, Elastic Security, SIEM telemetry, automated regression testing

## Background

- **M.S., Information Technology**, Arizona State University (2026)
- Graduate Teaching Assistant and IT Grader
- Business & Compliance Lead, AEROSEC academic technology externship (Aug–Dec 2025)

## Connect

- Portfolio: https://poojakira.github.io/Pooja_Kiran_Portfolio_Website/
- LinkedIn: https://www.linkedin.com/in/poojakiran/
- Email: poojakiranbhardwaj@gmail.com

---

<sub>Metrics above are tied to specific dated CI runs or bounded fixture sets. They are not claims of production deployment, customer adoption, or universal detection effectiveness. Review each repository's scope, limitations, and license before reuse.</sub>
