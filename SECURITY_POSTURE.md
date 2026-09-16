# SECURITY_POSTURE.md

Date: 2026-09-16

This document classifies what each security/ML-security repository actually does. The categories are capability classes, not quality scores.

## Runtime enforcement

### `mcp-agent-security-gateway`

A runtime MCP security gateway with a protected API, policy evaluation, and client-side guard middleware. The client sends `X-API-Key` when configured, defaults to fail-closed for availability failures, and treats explicit upstream authorization denials as blocking.

### `unified-ml-security-platform`

An authenticated integration gateway that routes to configured internal services. The proxy uses an explicit request-header allowlist and injects the gateway's internal API key rather than forwarding caller-controlled authentication headers.

**Limitation:** service identity is still based on a shared key across configured services.

## Static analysis

### `aws-agent-identity-guard`

Static AWS IAM policy analysis focused on agent permissions and risky constructs. It must not be described as determining effective AWS account permissions without AWS-side/runtime evaluation.

### `hf-model-provenance-scanner`

Static model/repository provenance analysis. Suspicious provenance indicators are evidence for review, not proof of maliciousness or compromise.

## Detection

### `dataset-poisoning-detector`

Anomaly/poisoning detection service with authenticated REST and WebSocket boundaries in current source.

### `attack-detection-engine`

ATT&CK-mapped detection engine. Current effectiveness claims remain configuration/dataset dependent.

Detection metrics must be scoped to the specific dataset, fixtures, attack types, and evaluation method.

## Adversarial testing / red teaming

### `llm-redteam-framework`

Offline prompt-injection evaluation and detector testing. Protected API endpoints fail closed when the API secret is missing. The detector verdict is not itself a secure downstream execution boundary.

### `adversarial-ml-lab`

Adversarial ML attack and robustness measurement harness for classifier experiments. It is a research/benchmark environment, not a universal robustness guarantee or independently validated production platform.

## Privacy/security research

### `model-privacy-attacks`

Membership-inference and privacy-defense research. Formal DP-SGD is limited to the corrected Opacus-backed path and requires the actual accountant result for a specific training configuration. The NumPy mechanism demonstration is explicitly non-formal.

## Threat intelligence / data foundation

### `attack-v19-core`

Versioned ATT&CK v19 data/model foundation. It is a data/model package, not itself a runtime enforcement boundary.

## Benchmarking / evidence

### `mlsec-benchmark-suite`

Benchmark and scoring infrastructure. Composite scores are measurements under declared benchmark conditions; they are not production-readiness determinations.

## Observability / integration

### `mlsec-dashboards`

Static evidence dashboard layer. It can display committed benchmark/security evidence; it is not itself enforcement.

### `ml-security-command-center`

Static source-inventory/portfolio command-center surface. It counts source declarations and records revisions; it does not execute the tests it inventories and does not measure security effectiveness.

## Audit/ML utility within non-security ML project

### `PulseNet-RUL-Forecasting`

Primarily an ML forecasting project. Its audit ledger now provides tamper-evident local hash chaining and explicit corruption/persistence failure handling. It does not establish tamper-proof or distributed immutable logging.

## Security-boundary model

For every runtime security component, the expected flow is:

```text
Input
  -> Authentication
  -> Authorization
  -> Validation
  -> Policy evaluation
  -> Enforcement
  -> Logging/evidence
  -> Response
```

The audit specifically identified and corrected cases where authentication, enforcement, or trust-boundary handling did not match documented semantics.

## Evidence rule

A security capability is considered stronger when the implementation, caller enforcement, tests, configuration, and documentation all agree. Static code presence alone is not treated as proof that the control is effective in deployment.
