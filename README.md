# Pooja Kiran - ML Security Engineering

I spend most of my time thinking about how ML systems break and how to stop that from happening. My work sits at the intersection of AI and security: scanning model repositories for sketchy artifacts, hardening MCP gateways, red-teaming LLMs, hunting for poisoned training data, and testing models against privacy attacks. I also dabble in RUL forecasting and anomaly detection research on the side.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/poojakiran)
[![Email](https://img.shields.io/badge/Email-Reach%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:poojakiranbhardwaj@gmail.com)

## Evidence Policy

I treat this page as an evidence index, not a scoreboard. Every claim lives in [claims/registry.json](claims/registry.json) and rendered into [security-dashboard.html](security-dashboard.html). Documentation keyword presence does not count as an implemented control. Missing CI, signed release, coverage, SBOM, provenance, or benchmark evidence remains visible as a limitation.


## Selected Public Work

| Project | Type | Scope |
| :--- | :--- | :--- |
| [hf-model-provenance-scanner](https://github.com/poojakira/hf-model-provenance-scanner) | Research library | Model repository provenance and unsafe artifact signal scanning. |
| [mcp-security-gateway-monitor](https://github.com/poojakira/mcp-security-gateway-monitor) | Prototype service | MCP security gateway and policy-enforcement hardening work. |
| [llm-redteam-framework](https://github.com/poojakira/llm-redteam-framework) | Research library | Defensive LLM prompt-attack evaluation workflows. |
| [dataset-poisoning-detector](https://github.com/poojakira/dataset-poisoning-detector) | Research service | Dataset poisoning and anomalous-sample analysis. |
| [model-privacy-attacks](https://github.com/poojakira/model-privacy-attacks) | Research library | Model privacy attack evaluation methodology. |
| [adversarial-ml-lab](https://github.com/poojakira/adversarial-ml-lab) | Prototype research library | FGSM, PGD, C&W and robustness experiment code. |
| [PulseNet-RUL-Forecasting](https://github.com/poojakira/PulseNet-RUL-Forecasting) | Joint research service prototype | Jointly authored RUL forecasting and anomaly-serving research. |

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
