# Portfolio Security Posture

Date: 2026-09-16

## Runtime enforcement

### `mcp-agent-security-gateway`

Security gateway with protected production API, policy evaluation, and tool-call guard middleware. The client now sends an API key when configured and defaults to fail-closed on gateway transport failure.

### `unified-ml-security-platform`

Authenticated gateway that routes requests to internal services. The proxy now uses an explicit request-header allowlist and injects the gateway's internal API key rather than forwarding caller-controlled authentication headers.

**Limitation:** service identity is still based on a shared key across configured services.

## Static analysis

### `aws-agent-identity-guard`

Static AWS IAM policy analysis focused on agent permissions and risky constructs. It should not be described as determining effective account permissions without AWS-side evaluation.

### `hf-model-provenance-scanner`

Static model/repository provenance analysis. A suspicious provenance indicator is not proof of malware or compromise.

## Detection

- `dataset-poisoning-detector`: anomaly/poisoning detection service with authenticated REST and WebSocket boundaries in current source.
- `attack-detection-engine`: ATT&CK-mapped detection engine.

Detection accuracy is dataset/configuration dependent and must not be generalized from fixture results.

## Adversarial testing

### `llm-redteam-framework`

Offline prompt-injection evaluation and detector testing. The API now fails closed when its API secret is missing.

### `adversarial-ml-lab`

Adversarial ML attack and robustness measurement harness for CIFAR-10/classifier experiments. It is a benchmark/research harness, not a universal robustness guarantee.

## Privacy/security research

### `model-privacy-attacks`

Membership-inference and privacy-defense research. The previous aggregate-gradient pseudo-DP implementation was replaced with an Opacus-backed preparation path. Formal DP should only be claimed from an actual accountant result for a specific training configuration.

## Threat intelligence/data foundation

### `attack-v19-core`

Versioned ATT&CK v19 data/model foundation. It is a data/model package, not itself a runtime enforcement boundary.

## Benchmarking/evidence

### `mlsec-benchmark-suite`

Benchmark/evidence infrastructure. Results are measurements under specified configurations and require reproducibility metadata before being presented as current.

## Observability/integration

- `mlsec-dashboards`: dashboard/visualization layer.
- `ml-security-command-center`: integration/command-center surface.

These should not be represented as independent security enforcement merely because they display security findings.

## Non-security ML

`PulseNet-RUL-Forecasting` is primarily an ML forecasting project and should not be counted as evidence of security-control implementation.

## Security-boundary model

For runtime security components, the expected flow is:

```text
Input
  -> Authentication
  -> Authorization
  -> Validation
  -> Policy evaluation
  -> Enforcement
  -> Logging
  -> Response
```

The audit specifically found and corrected gaps where authentication, enforcement, or trust-boundary handling did not match the documented security semantics.
