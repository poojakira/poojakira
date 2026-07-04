# Pooja Kiran — ML Security Engineer

I build security controls around ML systems: model supply-chain scanning, LLM/agent security monitoring, adversarial robustness, privacy-attack measurement, and secure ML serving.

[![Portfolio](https://img.shields.io/badge/Portfolio-poojakira.github.io-2563eb?style=for-the-badge&logo=google-chrome&logoColor=white)](https://poojakira.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/poojakiran)
[![Email](https://img.shields.io/badge/Email-Reach%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:poojakiranbhardwaj@gmail.com)

---

## Public Repositories

### AI Security Infrastructure

| Repo | What it does | Tests | Release |
|---|---|---|---|
| [aegisai-public-dashboard](https://github.com/poojakira/aegisai-public-dashboard) | Live AI security monitoring dashboard — request metrics, threat heatmaps, RAG canary monitoring, agent trust graphs, CVE timeline. Deployed on Vercel. | CI ✅ | v1.0.0 |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Scan any Hugging Face repo for malicious signals before `model.load()`. Detects org impersonation, pickle exploits, download velocity anomalies. Zero deps. | 100 tests ✅ | v0.1.0 |
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | Monitor MCP tool calls for prompt injection in descriptions, PII leakage, shadow servers, and exfiltration patterns. Immutable audit trail. | 105 tests ✅ | v0.1.0 |
| [ml-pipeline-integrity-guard](https://github.com/poojakira/ml-pipeline-integrity-guard) | Per-layer SHA-256 weight fingerprinting, output drift detection, backdoor canary probing, rollback urgency scoring 0–100. Pure Python. | 89 tests ✅ | v0.1.0 |

### Applied ML Security

| Repo | What it does | Tests | Release |
|---|---|---|---|
| [docquery](https://github.com/poojakira/docquery) | Production RAG pipeline for financial document Q&A with RAG poisoning detection (OWASP LLM08:2025). Qdrant retrieval, cross-encoder reranking, FastAPI, Redis. | CI ✅ | v0.1.0 |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Remaining Useful Life forecasting on NASA C-MAPSS data with adversarial sensor input detection (FDIA), RBAC, STRIDE threat model, CI security gates. | CI ✅ | v1.0.0 |

---

## What each tool actually solves

**hf-model-provenance-scanner** — In May 2026 a fake AI model repo reached 244,000 downloads in 18 hours before detection. This tool checks repos for impersonation, hidden execution scripts, and trust signals *before* any file is downloaded.
```bash
pip install -e . && hf-scan meta-llama/Llama-3-8B
```

**mcp-security-gateway-monitor** — 200,000 exposed MCP server instances with zero auth by default (mid-2026). One server silently BCCed every email to an attacker. This tool monitors every tool call for exactly these patterns.
```bash
pip install -e ".[dev]" && python -m pytest tests/ -v
```

**ml-pipeline-integrity-guard** — A major ML framework was compromised for 42 undetected minutes in 2026. This tool fingerprints your model's weights per-layer, detects output drift, probes for backdoor triggers, and scores rollback urgency.
```bash
pip install -e ".[dev]" && python -m pytest tests/ -v
```

**aegisai-public-dashboard** — Live, public, zero-auth dashboard with 9 threat-intelligence panels. Deployed and running at no cost.
- Live: [aegisai-public-dashboard.vercel.app](https://aegisai-public-dashboard.vercel.app)

---

## Technical areas

- **LLM/Agent security**: Prompt injection, tool poisoning, MCP security, RAG poisoning (OWASP LLM Top 10)
- **Model supply chain**: Provenance verification, pickle exploit detection, typosquat detection, SBOM
- **ML integrity**: Weight fingerprinting, output drift detection, backdoor probing, rollback scoring
- **Adversarial ML**: FDIA detection on sensor streams, adversarial robustness evaluation
- **Secure serving**: JWT RS256, RBAC, rate limiting, audit logging, Prometheus metrics
- **Stack**: Python 3.11+, FastAPI, Next.js 14, Supabase, Docker, GitHub Actions, Qdrant, Redis

---

## Availability

- **Location**: Greater Phoenix Area, AZ
- **Available**: July 6, 2026
- **Visa**: F-1 OPT (H-1B sponsorship needed)
- **Preferred roles**: ML Security Engineer · AI Security Researcher · Applied ML Security

---

## Contact

- **Email**: [poojakiranbhardwaj@gmail.com](mailto:poojakiranbhardwaj@gmail.com)
- **GitHub**: [github.com/poojakira](https://github.com/poojakira)
- **LinkedIn**: [linkedin.com/in/poojakiran](https://linkedin.com/in/poojakiran)
- **Portfolio**: [poojakira.github.io](https://poojakira.github.io)

---

*Last updated: July 2026 · All repos are public and runnable · No broken links*
