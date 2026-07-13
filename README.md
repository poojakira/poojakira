# Pooja Kiran — ML Security Engineer

I build security controls around ML systems: model supply-chain scanning, LLM/agent security monitoring, adversarial robustness, privacy-attack measurement, and secure ML serving.

[![Portfolio](https://img.shields.io/badge/Portfolio-poojakira.github.io-2563eb?style=for-the-badge&logo=google-chrome&logoColor=white)](https://poojakira.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/poojakiran)
[![Contact](https://img.shields.io/badge/Contact-via%20Portfolio-EA4335?style=for-the-badge&logo=google-chrome&logoColor=white)](https://poojakira.github.io)

---

## Public Repositories

### AI Security Infrastructure

| Repo | What it does | Tests | Release |
|---|---|---|---|
| aegisai-public-dashboard *(not currently public)* | Live AI security monitoring dashboard — request metrics, threat heatmaps, RAG canary monitoring, agent trust graphs, CVE timeline. | — | — |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Scan any Hugging Face repo for malicious signals before `model.load()`. Detects org impersonation (Levenshtein + Unicode homoglyphs), pickle exploits, SBOM absence. Zero deps. | 100 tests ✅ | v0.1.0 |
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | Monitor MCP tool calls for prompt injection, PII leakage, shadow servers, and exfiltration. SHA-256 hash-chained immutable audit log with WAL persistence. | 105 tests ✅ | v0.1.0 |
| ml-pipeline-integrity-guard *(not currently public)* | Per-layer SHA-256 weight fingerprinting, output drift detection (min-sample-guarded), backdoor canary probing, rollback urgency scoring 0–100. | — | — |

### Adversarial ML & Privacy Attacks

| Repo | What it does | Tests | Release |
|---|---|---|---|
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM, PGD, C&W L2 attacks on PyTorch classifiers + PGD adversarial training defense. Eval harness produces CI-gateable JSON benchmark reports. | 13 tests ✅ | v0.1.0 |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | *(Planned)* Membership inference (threshold / entropy / shadow model) and model extraction simulators, black-box only. | 🚧 WIP | — |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Detect injected malicious training samples using z-score (per-class), IQR fences, and IsolationForest. Returns per-sample anomaly scores with feature-level attribution. | 13 tests ✅ | v0.1.0 |

### LLM & Agent Security

| Repo | What it does | Tests | Release |
|---|---|---|---|
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | *(Planned)* Adversarial prompt generation across mutation categories + an offline detector for testing guardrails. | 🚧 WIP | — |

### Applied ML Security

| Repo | What it does | Tests | Release |
|---|---|---|---|
| docquery *(not currently public)* | Production RAG pipeline with tenant-isolated Qdrant retrieval, context_guard (NFKC + homoglyph injection detection), PII redaction, JWT auth, Prometheus metrics, k8s + Terraform. | — | — |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Turbofan RUL forecasting on SHA-256 verified NASA C-MAPSS data. JWT RS256 RBAC, hash-chained audit ledger, FDIA detector implementing BaseAnomalyModel, FGSM adversarial eval CI gate. | CI ✅ | v2.1.0 |

---

## What each tool actually solves

**hf-model-provenance-scanner** — In May 2026, a fake OpenAI repo reached 244,000 downloads in 18 hours before detection. This tool checks repos for org impersonation, hidden execution scripts, and trust signals *before* any file is downloaded.

```bash
pip install -e . && hf-scan meta-llama/Llama-3-8B
```

**adversarial-ml-lab** — Most production classifiers have never been tested for adversarial robustness. This lab runs FGSM, PGD, and C&W attacks against any PyTorch model and produces a JSON report you can gate CI on.

```bash
pip install -e ".[dev]" && python -m adv_lab.eval.harness --n-samples 500 --output results/report.json
```

**mcp-security-gateway-monitor** — 200,000 exposed MCP server instances with zero auth (mid-2026). One server silently BCCed every email to an attacker. This tool monitors every tool call for exactly these patterns, with a cryptographically verified audit trail.

```bash
pip install -e ".[dev]" && python -m pytest tests/ -v
```

**model-privacy-attacks** *(WIP — scaffold only, no code/tests yet)* — Planned: measure privacy leakage from ML inference APIs (membership inference from confidence scores; decision-boundary extraction under a query budget).

**llm-redteam-framework** *(WIP — scaffold only, no code/tests yet)* — Planned: generate adversarial prompts across mutation categories and train an offline classifier to detect them, for testing guardrails and building labeled safety datasets.

**ml-pipeline-integrity-guard** *(not currently public)* — Intended to fingerprint model weights per-layer, detect output drift, and probe for backdoor triggers.

**dataset-poisoning-detector** — Scans training datasets for anomalous samples before training begins. Three detectors (z-score, IQR, IsolationForest) return per-sample anomaly scores with feature attribution.

```bash
pip install -e ".[dev]" && python -m pytest tests/ -v
```

**aegisai-public-dashboard** *(not currently public)* — Intended as a live AI security monitoring dashboard. Links removed until the repository/deployment is public and verifiable.

---

## Technical areas

- **Adversarial ML**: FGSM, PGD, C&W attacks, PGD adversarial training, FDIA detection
- **Privacy attacks**: Membership inference (threshold / entropy / shadow), model extraction
- **LLM/Agent security**: Prompt injection, tool poisoning, MCP security, RAG poisoning (OWASP LLM Top 10)
- **Model supply chain**: Provenance verification, pickle exploit detection, typosquat detection, SBOM
- **ML integrity**: Weight fingerprinting, output drift detection, backdoor probing, rollback scoring
- **Data security**: Dataset poisoning detection, per-sample anomaly attribution
- **Secure serving**: JWT RS256, RBAC, rate limiting, audit logging, Prometheus metrics
- **Stack**: Python 3.11+, PyTorch, FastAPI, Next.js 14, Supabase, Docker, GitHub Actions, Qdrant, Redis

---

## Availability

- **Location**: Greater Phoenix Area, AZ
- **Available**: July 6, 2026
- **Visa**: F-1 OPT (H-1B sponsorship needed)
- **Preferred roles**: ML Security Engineer · AI Security Researcher · Applied ML Security

---

## Contact

Reach me via LinkedIn or the portfolio contact form (preferred). Email is shown
obfuscated to reduce automated scraping/phishing:

- **Email**: `poojakiranbhardwaj [at] gmail [dot] com`
- **GitHub**: [github.com/poojakira](https://github.com/poojakira)
- **LinkedIn**: [linkedin.com/in/poojakiran](https://linkedin.com/in/poojakiran)
- **Portfolio**: [poojakira.github.io](https://poojakira.github.io)

---

*Last updated: July 2026. Repos marked ✅ are public and runnable; those marked
🚧 WIP are early scaffolds without code/tests yet. `docquery`,
`aegisai-public-dashboard`, and `ml-pipeline-integrity-guard` are listed but not
currently public/verifiable, so their links were removed — they will be restored
once the repositories are public. Per-repo "N tests" counts are passing-test
counts, not branch or mutation coverage; run `pytest --cov --cov-branch` (and a
mutation tool such as `mutmut`) for a figure that reflects real test strength.*
