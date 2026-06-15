# 2026 Seeking SSE AI Infrastructureing Execution Plan

Date: 2026-05-23

This is not a brag document. It is a work plan for turning the portfolio into evidence that can survive senior ML security review.

## Non-Negotiable Claim Policy

- No "green CI" claim unless the current default-branch GitHub Actions run is passing.
- No latency, throughput, F1, AUROC, or robustness number unless the repo contains the command and output artifact needed to reproduce it.
- No "production-grade" label for demo systems.
- No synthetic-data result marketed as real-world performance.
- No prompt-injection, RAG, or agent-security claim without tests that show both detected and missed cases.

## Portfolio Architecture Target

| Layer | Required proof |
| --- | --- |
| LLM/RAG security | Prompt-injection tests, retrieval poisoning tests, citation integrity checks, source isolation, output DLP, policy decisions, audit logs. |
| Model supply chain | Artifact scanners, unsafe serialization detection, signature verification, provenance policy gates, SBOM, dependency audit, SARIF output. |
| Secure inference | Authn/authz, rate limits, request validation, model version pinning, rollback, timeout/retry behavior, structured logs, tracing. |
| Adversarial ML | Attack implementations, defense evaluation, measured reports, failure cases, documented limits. |
| Privacy/security research | Membership inference, model inversion, extraction scenarios, DP limits, threat models. |
| Cloud/platform | Docker, Kubernetes/Helm, Terraform, OIDC, least privilege, network policies, secrets handling, image scanning/signing. |
| Reliability | Health checks, load tests, failure injection, runbooks, SLO-oriented metrics, alert rules. |

## Immediate Engineering Backlog

| Priority | Repo | Work |
| --- | --- | --- |
| P0 | Model-Supply-Chain-Auditor | Add SARIF upload workflow, SBOM generation, policy gate examples, threat model mapped to OWASP/MITRE/NIST. |
| P0 | LLM-Guard-Scanner | Add adversarial prompt corpus, RAG poisoning fixtures, severity taxonomy, measured bypass report, CI artifacts. |
| P1 | docquery | Add RAG security tests, source authorization checks, citation-integrity tests, OpenTelemetry spans, security architecture doc. |
| P1 | production-ml-platform | Add architecture threat model, explicit authz model, rollback incident runbook, queue-backed inference path, policy checks. |
| P1 | Secure-ML-platform | Correct public metadata, refresh tests, document dataset limits, add adversarial/security regression tests if repo stays featured. |
| P2 | RTX-OOM-Guard | Keep as GPU-systems research. Add measured benchmark artifacts only after local commands reproduce them. |
| P2 | ML-Privacy-Attacks | Refresh archived repo or clearly label as historical privacy-security work. |
| P3 | Aerospace/demo repos | De-emphasize unless rebuilt around security, telemetry integrity, incident response, or ML assurance. |

## End-to-End Flagship Lab

Build or consolidate one repo that demonstrates:

1. RAG ingestion with source authorization, document integrity hashes, poisoned-document detection, and citation enforcement.
2. Inference API with OIDC/JWT validation, per-tenant rate limits, audit logs, timeout/retry controls, and model version pinning.
3. Queue-backed batch inference with bounded concurrency and backpressure.
4. Model artifact gate using scanner, signature, provenance, SBOM, and policy-as-code.
5. Observability through OpenTelemetry traces, Prometheus metrics, structured JSON logs, alert rules, and runbooks.
6. Kubernetes deployment with Helm, network policies, non-root containers, resource limits, pod security, and secret references.
7. Terraform for a minimal cloud footprint with least-privilege IAM and environment isolation.
8. Security tests for prompt injection, RAG poisoning, jailbreaks, secret exfiltration, API abuse, dependency risk, and rollback behavior.

## Verification Standard

Each featured repo must expose:

- `make test` or equivalent local verification
- lint and type checks
- security-specific tests
- CI workflow with least-privilege permissions
- reproducible example commands
- checked-in docs for architecture, threat model, limitations, and operational controls
- no stale claims in README, About field, or docs

## Hiring Positioning

Lead with implemented security controls and verified artifacts:

- "I build and test security gates around ML systems."
- "I document bypasses and limits instead of pretending controls are complete."
- "My strongest repos cover model supply chain, LLM application security, adversarial ML, and secure serving controls."

Do not lead with unverified metrics, generic AI claims, or aesthetic portfolio language.
