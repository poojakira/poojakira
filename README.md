# Pooja Kiran - ML Security Engineering

I spend most of my time thinking about how ML systems break and how to stop that from happening. My work sits at the intersection of AI and security: scanning model repositories for sketchy artifacts, hardening MCP gateways, red-teaming LLMs, hunting for poisoned training data, and testing models against privacy attacks. I also dabble in RUL forecasting and anomaly detection research on the side.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/poojakiran)
[![Email](https://img.shields.io/badge/Email-Reach%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:poojakiranbhardwaj@gmail.com)

## Evidence Policy

I treat this page as an evidence index, not a scoreboard. Every claim lives in [claims/registry.json](claims/registry.json) and is rendered into [security-dashboard.html](security-dashboard.html). Documentation keyword presence does not count as an implemented control. Missing CI, signed release, coverage, SBOM, provenance, or benchmark evidence remains visible as a limitation.

## Live Dashboards

All project dashboards are hosted at: **[poojakira.github.io/mlsec-dashboards](https://poojakira.github.io/mlsec-dashboards/)**

Each dashboard shows real evidence data from benchmark runs — scan results, detection metrics, performance numbers.

## Selected Public Work

| Project | Type | Dashboard |
| :--- | :--- | :--- |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Model supply chain scanner | [Dashboard](https://poojakira.github.io/mlsec-dashboards/hf-model-provenance-scanner/) |
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | MCP tool-call firewall (51% detection rate) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/mcp-security-gateway-monitor/) |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Prompt injection detector (F1=0.93) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/llm-redteam-framework/) |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Training data anomaly flagging (ROC-AUC ~0.54) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/dataset-poisoning-detector/) |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Membership inference + extraction attacks | [Dashboard](https://poojakira.github.io/mlsec-dashboards/model-privacy-attacks/) |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | FGSM/PGD/C&W attack + defense evaluation | [Dashboard](https://poojakira.github.io/mlsec-dashboards/adversarial-ml-lab/) |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | ICS/OT equipment RUL prediction (F1=0.54) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/PulseNet-RUL-Forecasting/) |
| [attack-v19-core](https://github.com/poojakira/attack-v19-core) | MITRE ATT&CK v19 data models | [Dashboard](https://poojakira.github.io/mlsec-dashboards/attack-v19-core/) |
| [attack-detection-engine](https://github.com/poojakira/attack-detection-engine) | 5-source telemetry detection (42 rules) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/attack-detection-engine/) |
| [aws-agent-identity-guard](https://github.com/poojakira/aws-agent-identity-guard) | IAM policy linter for AI agents | [Dashboard](https://poojakira.github.io/mlsec-dashboards/aws-agent-identity-guard/) |
| [unified-ml-security-platform](https://github.com/poojakira/unified-ml-security-platform) | Architecture spec (not a running platform) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/unified-ml-security-platform/) |
| [mlsec-benchmark-suite](https://github.com/poojakira/mlsec-benchmark-suite) | Benchmark runner (smoke tests only) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/mlsec-benchmark-suite/) |
| [ml-security-command-center](https://github.com/poojakira/ml-security-command-center) | Aggregate status view (simulated data) | [Dashboard](https://poojakira.github.io/mlsec-dashboards/ml-security-command-center/) |

## Technical Focus

- Model supply chain: artifact safety, provenance checks, repository risk signals, SBOM-oriented workflows
- LLM and agent security: prompt-injection evaluation, tool-call inspection, exfiltration and PII-leak detection
- Adversarial ML: attack implementation, invariant testing, robustness evaluation design
- Data security: poisoning detection, drift analysis, webhook/API hardening
- Secure serving: authentication, authorization, rate limiting, audit logging, service health checks
- Evidence systems: reproducible benchmark contracts, claim registries, immutable source/data/config identifiers

## Research and Publications

**Cybersecurity Innovation Researcher - TEM 598 Technology Innovation Lab, Arizona State University x Honeywell Aerospace Innovation Hub.**
Contributed to a graduate research practicum exploring AI and cybersecurity challenges for aerospace systems.

- **Personalized E-learning System Using Reinforcement Learning Through Satellite**  
  IEEE Xplore, 2024: https://ieeexplore.ieee.org/document/10440852
- **Smart Charge Pro Empowering Future Mobility With Advanced Safety And Efficiency In Electric Vehicle Charging Infrastructure**  
  IOSR Journal of Computer Engineering, 2023: https://www.iosrjournals.org/iosr-jce/pages/25(4)Series-1.html

## Maintenance

```powershell
py -3.12 -m pip install -r requirements-dev.txt
py -3.12 -m pytest
python -m pytest
python tools/validate_claims.py
python tools/build_security_dashboard.py
```

Scheduled validation checks claim freshness and external links. It opens an issue when evidence becomes stale or unreachable; it never silently edits public claims.

## Contact

- Location: Greater Phoenix Area, AZ
- Visa: F-1 OPT; H-1B sponsorship needed
- Target roles: ML Security Engineer, AI Security Engineer, Applied ML Security Engineer
- Email: [poojakiranbhardwaj@gmail.com](mailto:poojakiranbhardwaj@gmail.com)
- GitHub: [github.com/poojakira](https://github.com/poojakira)
- LinkedIn: [linkedin.com/in/poojakiran](https://linkedin.com/in/poojakiran)

*Last updated: July 2026. Claims are limited to public, inspectable evidence recorded in the claim registry.*
