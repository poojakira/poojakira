# Pooja Kiran — ML Security Engineer

I build security controls around ML systems: model supply-chain scanning, LLM/agent
security monitoring, adversarial robustness, dataset-poisoning detection, and secure ML serving.

[![Portfolio](https://img.shields.io/badge/Portfolio-poojakira.github.io-2563eb?style=for-the-badge&logo=google-chrome&logoColor=white)](https://poojakira.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/poojakiran)
[![Email](https://img.shields.io/badge/Email-Reach%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:poojakiranbhardwaj@gmail.com)

---

## Public Repositories

> Facts below (versions, test counts) are taken directly from each repo's
> `pyproject.toml` and `tests/`. "Tests" = number of test functions in the
> suite. Status reflects whether the repo currently ships a runnable
> implementation or is a design spec.

### Shipping — real implementations

| Repo | What it does | Version | Tests |
|---|---|---|---|
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Zero-dependency scan of a Hugging Face repo/dir before `model.load()`: pickle-opcode RCE-gadget detection, org-impersonation (Levenshtein + homoglyph), SafeTensors/GGUF/ONNX checks, SBOM/signature/provenance policy. | 0.2.0 | 100 |
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | Monitors MCP tool calls for prompt injection, PII leakage, shadow servers, and exfiltration, with a SHA-256 hash-chained, WAL-persisted immutable audit log. Optional (BETA) scikit-learn classifier. | 0.1.0 | 462 |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM, PGD, and C&W attacks on PyTorch classifiers plus PGD adversarial-training defense. Eval harness emits CI-gateable JSON benchmark reports. | 0.1.0 | 290 |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Detects anomalous/poisoned training samples via per-class z-score, IQR fences, and IsolationForest, returning per-sample anomaly scores with feature-level attribution. | 0.2.0 | 32 |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Turbofan remaining-useful-life forecasting on NASA C-MAPSS, with JWT RS256 RBAC, a hash-chained audit ledger, and an FGSM adversarial-eval CI gate. | 2.1.0 | 54 |

### Design stage — specification only (no implementation yet)

These repositories currently contain a design/README specification. The code,
tests, and benchmark numbers described in them are **not yet implemented** and
should be treated as planned work, not shipped results.

| Repo | Planned scope | Status |
|---|---|---|
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership-inference (threshold / shadow) and model-extraction simulators; LLM Min-K% Prob MIA. | Spec only — implementation pending |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Adversarial-prompt generation across mutation categories + an offline TF-IDF/LR detector. | Spec only — implementation pending |

---

## What the shipping tools solve

**hf-model-provenance-scanner** — Fake/impersonating model repos have reached
hundreds of thousands of downloads before takedown. This tool statically checks
a repo for org impersonation, pickle deserialization RCE gadgets, and missing
trust signals *before* any file is loaded — without executing the model.

```bash
pip install -e . && hf-scanner meta-llama/Llama-3-8B --mode remote
```

**adversarial-ml-lab** — Most production classifiers are never tested for
adversarial robustness. This lab runs FGSM/PGD/C&W against a PyTorch model and
produces a JSON report you can gate CI on.

```bash
pip install -e ".[dev]" && python -m adv_lab.eval.harness --n-samples 500 --output results/report.json
```

**mcp-security-gateway-monitor** — Exposed MCP servers with weak auth can leak
tool-call data. This monitors every tool call for injection/exfiltration/PII
patterns with a cryptographically hash-chained audit trail.

```bash
pip install -e ".[dev]" && python -m pytest tests/ -q
```

**dataset-poisoning-detector** — Scans training data for anomalous samples
before training, with three detectors and per-sample feature attribution.

```bash
pip install -e ".[dev]" && python -m pytest tests/ -q
```

**PulseNet-RUL-Forecasting** — Predictive-maintenance RUL forecasting on NASA
C-MAPSS with authn/z, audit logging, and an adversarial-eval CI gate.

```bash
pip install -e . && python -m pytest tests/ -q
```

---

## Technical areas

- **Model supply chain**: pickle-opcode RCE detection, typosquat/homoglyph detection, SBOM/provenance policy
- **Adversarial ML**: FGSM, PGD, C&W attacks; PGD adversarial training; FGSM CI gating
- **LLM/Agent security**: prompt-injection & exfiltration monitoring for MCP tool calls (OWASP LLM Top 10)
- **Data security**: dataset-poisoning detection with per-sample anomaly attribution
- **Secure serving**: JWT RS256, RBAC, rate limiting, hash-chained audit logging, Prometheus metrics
- **Stack**: Python 3.11+, PyTorch, scikit-learn, FastAPI, Docker, GitHub Actions

---

## Availability

- **Location**: Greater Phoenix Area, AZ
- **Visa**: F-1 OPT (H-1B sponsorship needed)
- **Preferred roles**: ML Security Engineer · AI Security Researcher · Applied ML Security

---

## Contact

- **Email**: [poojakiranbhardwaj@gmail.com](mailto:poojakiranbhardwaj@gmail.com)
- **GitHub**: [github.com/poojakira](https://github.com/poojakira)
- **LinkedIn**: [linkedin.com/in/poojakiran](https://linkedin.com/in/poojakiran)
- **Portfolio**: [poojakira.github.io](https://poojakira.github.io)

---

*Last updated: July 2026 · 5 repositories ship runnable code; 2 are design specs in progress.*
