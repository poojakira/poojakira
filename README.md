# Pooja Kiran - ML Security Engineer

I build and test security controls around ML systems: model supply-chain scanning, LLM and agent monitoring, adversarial robustness, privacy-attack measurement, dataset poisoning checks, and secure ML serving.

[Portfolio](https://poojakira.github.io) | [LinkedIn](https://linkedin.com/in/poojakiran) | [Email](mailto:poojakiranbhardwaj@gmail.com)

## Current Public Repository Inventory

Verified from `gh repo list poojakira --limit 100` on 2026-07-08: 11 public repositories.

| Repo | Area | Local validation run on 2026-07-08 |
|---|---|---|
| [aegisai-public-dashboard](https://github.com/poojakira/aegisai-public-dashboard) | Public AI security dashboard | `npm run lint`, `npm run typecheck`, `npm run test`, `npm run build` passed. `npm audit` reports 2 moderate issues through Next.js bundled PostCSS; no newer stable Next version was available via npm at validation time. |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Hugging Face model provenance and malicious-file scanning | `102 passed` |
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | MCP tool-call monitoring, PII detection, audit log chaining | `119 passed` |
| [ml-pipeline-integrity-guard](https://github.com/poojakira/ml-pipeline-integrity-guard) | Model fingerprinting, drift checks, backdoor probes, rollback scoring | `98 passed` |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/CW attack harness and adversarial training utilities | `13 passed` |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership inference and model-extraction simulators | `12 passed` |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Statistical and IsolationForest dataset poisoning detectors | `13 passed` |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Offline prompt-injection generation and detection fixtures | `15 passed` |
| [docquery](https://github.com/poojakira/docquery) | Secure RAG pipeline controls: tenant isolation, context guard, PII redaction, citations | `62 passed` |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Predictive-maintenance ML serving, API controls, anomaly/security tests | `68 passed`; 1502 dependency warnings observed from `joblib`/NumPy path during tests |
| [poojakira](https://github.com/poojakira/poojakira) | GitHub profile and evidence index | Profile honesty tests added; legacy generated evidence is explicitly marked unverified |

## Verification Commands

Python repos were validated from fresh clones with:

```bash
PYTHONPATH=src python -m pytest -q
```

The dashboard was validated with:

```bash
npm ci
npm run lint
npm run typecheck
npm run test
npm run build
npm audit --audit-level=moderate
npm view next version
```

## Evidence Policy

- Do not cite benchmark numbers, production readiness, incident counts, or deployment health unless the repository contains reproducible commands and current passing evidence.
- Synthetic/demo data must be labeled as synthetic/demo data.
- Legacy generated SARIF files in this profile repository are collection artifacts only, not proof that linked repositories passed security verification.
- Each repository should be judged by its own source, tests, workflows, and reproducible runtime output.

## Technical Areas

- Adversarial ML: FGSM, PGD, C&W, adversarial training, FDIA detection
- Privacy attacks: membership inference, entropy/threshold/shadow attacks, model extraction
- LLM/agent security: prompt injection, MCP monitoring, tool poisoning, RAG poisoning controls
- Model supply chain: provenance checks, pickle/code execution detection, typosquat and trust signals
- ML integrity: model fingerprints, drift detection, backdoor probes, rollback urgency scoring
- Secure serving: auth, RBAC, tenant isolation, audit logging, metrics, deployment manifests

## Availability

- Location: Greater Phoenix Area, AZ
- Available: July 2026
- Visa: F-1 OPT, H-1B sponsorship needed
- Preferred roles: ML Security Engineer, AI Security Researcher, Applied ML Security Engineer

## Contact

- Email: [poojakiranbhardwaj@gmail.com](mailto:poojakiranbhardwaj@gmail.com)
- GitHub: [github.com/poojakira](https://github.com/poojakira)
- LinkedIn: [linkedin.com/in/poojakiran](https://linkedin.com/in/poojakiran)
- Portfolio: [poojakira.github.io](https://poojakira.github.io)

Last updated: 2026-07-08
