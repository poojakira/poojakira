# Pooja Kiran — ML Security Engineer

Building security tooling for the ML lifecycle: model supply chain security, LLM red-teaming, adversarial robustness, and privacy-preserving ML.

## Projects

| Repo | What It Does | Key Threat | Honest Status |
|------|-------------|-----------|---------------|
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | FastAPI scan service: prompt injection, PII leakage, RAG poisoning → SARIF output, PR gate | LLM01 Prompt Injection, LLM06 PII, LLM07 RAG | F1=0.70 OOD / 0.93 curated |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Scan HuggingFace models for supply chain attacks; Ed25519 model signing | T1683.001 ML Supply Chain | 12/12 internal fixture suite |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/C&W attacks on CIFAR-10 ResNet-18; Madry adversarial training | AML.T0043 Craft Adversarial Data | 0.31% → 44.87% robust acc (Madry AT) |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Yeom MIA, Fredrikson inversion, DP-SGD defense | T1685 ML Privacy | MIA advantage=0.42, baseline=0.10; ε=1.16 at σ=4.0 |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Secure MLOps pipeline: STRIDE (12 surfaces), RBAC, audit log, Prometheus | 12 STRIDE surfaces modeled | F1=0.54 Isolation Forest, NASA C-MAPSS |

## Security Engineering Focus

- **Threat Modeling**: STRIDE across ML pipelines; MITRE ATLAS + ATT&CK v19 mapping
- **Privacy**: Membership inference (Yeom 2018), model inversion (Fredrikson 2015), DP-SGD
- **Supply Chain**: Ed25519 model signing, SHA-256 artifact manifests, SARIF CI gates
- **LLM Security**: OWASP LLM Top 10, RAG poisoning detection, canary token tracking
- **Adversarial ML**: FGSM, PGD, C&W attacks; Madry AT on CIFAR-10 ResNet-18

## Honesty Note

All benchmark numbers are either from committed result artifacts or clearly labeled as targets/baselines. Synthetic data results are marked as such. Each repo README states what is and is not production-ready.
