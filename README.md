# Pooja Kiran Bharadwaj

**What if the AI model you just downloaded is already attacking you?**

Pickle files on Hugging Face execute arbitrary code the moment you call `torch.load()`. Most scanners require downloading the full model to check — gigabytes of weights you might not want on your machine. Mine fetches only the first few KB and catches exploits that existing tools miss.

That question — *is this AI system safe to run?* — led me to build three open-source tools that sit between AI systems and the damage they can do.

---

## The Tools

**[mcp-agent-security-gateway](https://github.com/poojakira/mcp-agent-security-gateway)** — What happens when your AI agent calls a tool you didn't expect?

Intercepts every MCP tool call in real-time. Catches prompt injection, PII leakage, and data exfiltration before they leave your infrastructure. `17 ★` · `5 forks`

---

**[hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner)** — Can you trust a model file you haven't opened yet?

Scans HuggingFace repos without downloading weights. Detects pickle exploits, typosquatting, rug-pulls, and obfuscated payloads using only file headers. Intercepts `torch.load()` at runtime to block malicious models before execution. Scanned the top 100 most-downloaded models. 12/12 documented real-world attacks detected.

---

**[aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard)** — Does your AI agent have permissions it should never use?

Static IAM analysis for AI agent roles. Finds privilege escalation paths and credential-harvesting patterns that standard AWS tools don't flag.

---

## The Research Stack

| What I wanted to know | What I built |
|----------------------|-------------|
| Can I fool a vision model with imperceptible noise? | [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) — FGSM/PGD/C&W benchmarks |
| Can I break an LLM's guardrails systematically? | [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) — Automated jailbreak simulation |
| Can I extract training data from a model? | [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) — Membership inference & inversion |
| Can I poison a dataset without being detected? | [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) — Statistical anomaly detection |

---

## Numbers

- 16 public repos · 15 with CI green
- 350+ tests across the flagship scanner alone
- 100 HuggingFace models scanned with real results published
- IEEE published (INDICON 2023)
- MS Information Technology, Arizona State University (2026)

---

## Let's talk

[LinkedIn](https://linkedin.com/in/poojakiran) · pooja.kiran@asu.edu

F-1 OPT EAD | Greater Phoenix Area
