# BENCHMARK_AUDIT.md

Date: 2026-09-16

## Reproducibility policy

A benchmark is treated as current only when the dataset, configuration, seed, environment, command, artifact, and commit can be identified and the run is actually reproduced. A committed JSON result without a fresh run is a **historical committed result**.

Benchmark results are measurements, not deployment approvals or universal security guarantees.

## Audited benchmark claims

| Repository | Benchmark/evidence | Dataset/fixture | Metric | Status | Limitation |
|---|---|---|---|---|---|
| `mcp-agent-security-gateway` | self-test/performance evidence | repository fixtures | detection/self-test metrics | HISTORICAL / LIMITED | not reproduced in this audit |
| `hf-model-provenance-scanner` | fixture/incident suites | committed security fixtures | detection/false positives | VERIFIED WITH LIMITED SCOPE | percentage applies only to named fixtures/suite |
| `aws-agent-identity-guard` | IAM rule corpus/tests | synthetic/static IAM policies | findings/rule behavior | LIMITED | static policy analysis, not effective AWS permissions |
| `llm-redteam-framework` | grouped/random/OOD evaluation | generated adversarial corpus | F1/precision/recall | HISTORICAL COMMITTED RESULT | current reproduction not executed |
| `adversarial-ml-lab` | `results/cifar10_smallcnn_real.json` | CIFAR-10 | clean/robust accuracy | HISTORICAL COMMITTED RESULT | synthetic/small-model scope; current run not executed |
| `model-privacy-attacks` | Adult Income MIA CI artifact | UCI Adult Income | MIA AUC + CI | HISTORICAL COMMITTED RESULT | current reproduction not executed |
| `model-privacy-attacks` | legacy epsilon artifact `results/epsilon_verification.json` | synthetic accounting parameters | epsilon | RETIRED / UNVERIFIED | historical value from an unvalidated accountant; not a formal DP bound |
| `model-privacy-attacks` | corrected Opacus DP-SGD path | caller-supplied training data/loader | epsilon at requested delta | IMPLEMENTED, NOT BENCHMARKED HERE | actual training and accountant result must be executed and recorded |
| `mlsec-benchmark-suite` | composite scoring suite | repository-specific fixtures | per-dimension/composite | UNVERIFIED CURRENT | artifact-by-artifact reproduction required |
| `mlsec-dashboards` | committed evidence dashboards | upstream JSON artifacts | project-specific metrics | STATIC / HISTORICAL | dashboard is not live monitoring |

## Specific claim handling

### `adversarial-ml-lab`

Committed small-CNN/CIFAR-10 measurements are experiment results for that dataset, architecture, threat configuration, and seed. They must not be generalized to production robustness.

### `llm-redteam-framework`

The repository reports grouped-split F1=0.97, random-split F1=1.0, and novel-phrasing OOD F1=0.83. Those values are configuration-specific measurements. The OOD benchmark should remain paired with its dataset construction, split, seed, and test-size details.

### `model-privacy-attacks`

The Adult Income MIA artifact is an attack measurement, not a universal privacy threshold. The former hand-written epsilon value is now explicitly classified as historical/unverified and must not be cited as a formal `(epsilon, delta)` guarantee.

The formal DP-SGD implementation now delegates per-example clipping/noising and privacy accounting to Opacus. The audit did not execute a complete DP training run, so no fresh epsilon number is reported.

### `hf-model-provenance-scanner`

The repository's limitation assessment correctly narrows 100% detection claims to the named fixture/suite. Keep that scope visible whenever the number is mentioned.

### `mlsec-benchmark-suite`

The scoring framework now explicitly says composite scores are benchmark measurements. Its CI gates are benchmark gates, not production-readiness decisions.

## Fresh execution result

No portfolio-wide benchmark was executed locally. The local git client could not clone the repositories because outbound network/DNS access was unavailable in the model environment.

Where GitHub Actions executed a changed commit, those CI results are recorded in `PORTFOLIO_SECURITY_AUDIT.md`; they are not silently represented as local test runs.

## Required benchmark metadata for future runs

- repository commit SHA
- dataset name and immutable version/hash
- model architecture/checkpoint
- configuration
- random seed(s)
- Python version
- dependency lock/version set
- hardware
- exact command
- raw output artifact
- timestamp
- metric definition
- sample size and confidence interval methodology where applicable

## No fabricated performance claims

No new accuracy, recall, precision, AUC, epsilon, latency, throughput, detection rate, or coverage number was invented or inferred from source code during this audit.
