# 2026 ML Security Portfolio Audit

Date: 2026-05-23

## Market Signal

Senior ML Security / AI Security roles are screening for a hybrid profile:

- AppSec and threat modeling applied to LLM, RAG, agentic, and ML platform systems
- cloud and infrastructure security: IAM, Kubernetes, containers, CI/CD, secrets, telemetry
- model supply-chain controls: unsafe serialization, signing, provenance, SBOM, CI gates
- detection and response: high-signal logs, detections, response playbooks, rollback
- adversarial ML, privacy attacks, prompt injection, model/data poisoning, model extraction
- clear communication about tradeoffs, false positives, latency, cost, and operational limits

## Repo Triage

| Priority | Repos | Action |
| --- | --- | --- |
| P0 | Model-Supply-Chain-Auditor, LLM-Guard-Scanner | Flagship ML security repos. Current work added provenance/policy gating and broader deterministic scanner tests; next step is SARIF/code-scanning evidence and larger eval corpora. |
| P1 | Adversarial-Robustness-Toolkit, ML-Privacy-Attacks, Secure-ML-platform | Keep visible as foundational ML security proof. Adversarial repo now emits measured JSON/Markdown/SVG reports; remaining repos still need fresh verification. |
| P2 | production-ml-platform, docquery, RTX-OOM-Guard, coderev-agents | Supporting platform/systems evidence. Security relevance must stay explicit and limited; recent changes removed inflated claims and added fail-closed or trust-boundary controls. |
| P3 | Aerospace/CubeSat/Mission/ESG/Orbital/PulseNet/Pooja_Portfolio | De-emphasize. These show breadth but dilute the ML security story if treated as flagship work. |

## Credibility Risks Found

- Several repo descriptions used "Green CI" or exact metrics without enough public context in the description itself. Do not use those claims until current GitHub Actions and checked-in artifacts support them.
- Archived repos are still useful, but recruiters may treat archived projects as stale unless the profile explains why they are archived.
- Some READMEs contain mojibake from encoding corruption. This damages polish and should be fixed repo by repo.
- `PulseNet-RUL-Forecasting` local README appears NUL-filled and has stale failed security-test artifacts. Do not feature it until cleaned.
- `Aerospace-Trajectory-Simulator` has a surrogate speedup claim that conflicts with its benchmark artifact. Remove or regenerate before using that metric.
- `ESG-Carbon-Telemetry` has a committed development secret placeholder and unreproduced benchmark claims. Keep de-emphasized.
- `Secure-ML-platform` public description claims real NASA data and F1=0.78, while README states synthetic fixture data and F1=0.14 on fixture data. Public description must be corrected.
- `Adversarial-Robustness-Toolkit` local verification now passes and the README describes measured reports, but public About/Actions must still be checked before claiming green CI.
- `LLM-Guard-Scanner` local verification now passes and README/code disagreement was reduced, but semantic bypass limits remain real and documented.
- `Model-Supply-Chain-Auditor` is the strongest flagship after adding provenance policy gates, but it still needs code-scanning workflow evidence before being called production-ready.
- `coderev-agents` had unverified fine-tuning/model/W&B/benchmark claims removed and now shows agentic trust-boundary controls; it remains a prototype, not a production review system.
- Some repos use demo-grade controls: regex prompt scanning, single-file hash chains, in-memory rate limits, synthetic data. These are acceptable only when clearly labeled.
- A profile claiming "top candidate" is weaker than a profile showing verified artifacts, tests, threat models, and limitations.

## Highest-Impact Next Changes

1. Model-Supply-Chain-Auditor: add GitHub code-scanning SARIF workflow and a threat model mapped to OWASP, MITRE ATLAS, and NIST AI RMF.
2. LLM-Guard-Scanner: add benchmark corpus, jailbreak/obfuscation bypass tests, false-positive report, and severity taxonomy.
3. docquery: extend RAG security tests for indirect prompt injection, retrieval poisoning, source isolation, and citation integrity.
4. production-ml-platform: add security architecture doc for model registry authz, rollback, auditability, and drift incident response.
5. Profile README: keep all claims evidence-based and remove unverifiable performance numbers. Completed for current profile README.
6. PulseNet-RUL-Forecasting: restore README text, remove stale failed outputs, rerun tests, and publish current security-test result.
7. Aerospace-Trajectory-Simulator: regenerate surrogate benchmark or delete the speedup claim.
8. Public GitHub About fields: remove "Green CI", unverifiable metrics, and "production" wording until current Actions and artifacts support them.

## Recruiter Positioning

Lead with:

- "I build security controls around ML systems."
- "I can implement and test controls, not just talk about AI governance."
- "My repos document limitations and failure modes."

Do not lead with:

- generic "AI/ML enthusiast"
- synthetic aerospace demos
- unverified live demos or metrics
- claims that regex or guardrails solve prompt injection
