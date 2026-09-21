# Public Repository Provenance Ledger

This ledger records the earliest defensible year for the public repositories in this account. It deliberately separates **repository inception** from older publications, datasets, incidents, standards, and academic work.

## Method

A year is accepted only when supported by one of the following:

- a reachable Git commit for the repository;
- a dated pre-Git artifact that clearly names the same project or a direct precursor;
- a course/project document with direct lineage to the repository;
- another inspectable artifact whose date and identity are independently attributable.

Background dates such as CVEs, papers cited by the code, dataset release years, test timestamps, copied changelog dates, and standards versions are not treated as project dates.

**Git history is not backdated.** If older lineage is ever proven later, it should be documented as pre-Git provenance rather than by rewriting commit timestamps.

## Results

| Repository | Earliest reachable commit | Earliest defensible year | Proof |
|---|---|---:|---|
| `poojakira` | 2026-03-21 · `f490bfe69b82` | **2026** | [PROVENANCE.md](PROVENANCE.md) |
| `mcp-agent-security-gateway` | 2026-07-10 · `ef0d7ceb42fb` | **2026** | [repo provenance](https://github.com/poojakira/mcp-agent-security-gateway/blob/main/PROVENANCE.md) |
| `hf-model-provenance-scanner` | 2026-07-10 · `7099591d86f5` | **2026** | [repo provenance](https://github.com/poojakira/hf-model-provenance-scanner/blob/main/PROVENANCE.md) |
| `dataset-poisoning-detector` | 2026-07-11 · `f70842e3fdc9` | **2026** | [repo provenance](https://github.com/poojakira/dataset-poisoning-detector/blob/main/PROVENANCE.md) |
| `llm-redteam-framework` | 2026-07-11 · `b89c8785307b` | **2026** | [repo provenance](https://github.com/poojakira/llm-redteam-framework/blob/main/PROVENANCE.md) |
| `adversarial-ml-lab` | 2026-07-11 · `db779b116181` | **2026** | [repo provenance](https://github.com/poojakira/adversarial-ml-lab/blob/main/PROVENANCE.md) |
| `unified-ml-security-platform` | 2026-07-17 · `d8bab3d069a8` | **2026** | [repo provenance](https://github.com/poojakira/unified-ml-security-platform/blob/main/PROVENANCE.md) |
| `attack-v19-core` | 2026-07-22 · `60943d673b3b` | **2026** | [repo provenance](https://github.com/poojakira/attack-v19-core/blob/main/PROVENANCE.md) |
| `mlsec-benchmark-suite` | 2026-07-29 · `5a5d7cf59566` | **2026** | [repo provenance](https://github.com/poojakira/mlsec-benchmark-suite/blob/main/PROVENANCE.md) |
| `aws-agent-identity-guard` | 2026-08-01 · `b4799d64eeef` | **2026** | [repo provenance](https://github.com/poojakira/aws-agent-identity-guard/blob/main/PROVENANCE.md) |
| `mlsec-dashboards` | 2026-08-03 · `31f5ad481323` | **2026** | [repo provenance](https://github.com/poojakira/mlsec-dashboards/blob/main/PROVENANCE.md) |
| `Pooja_Kiran_Portfolio_Website` | 2026-08-17 · `818e84b61976` | **2026** | [repo provenance](https://github.com/poojakira/Pooja_Kiran_Portfolio_Website/blob/main/PROVENANCE.md) |

## Chronology correction found during the audit

`dataset-poisoning-detector/CHANGELOG.md` originally labeled versions 0.1.0 and 0.2.0 as January 2024. Repository history shows the changelog was first committed on 2026-07-11. The unsupported labels were corrected to 2026-07-11 while preserving the Git history.

## Earlier work is real, but separate

The absence of pre-2026 Git provenance for the repositories above does **not** erase earlier academic work. It only means that older work should not be used to backdate unrelated repositories.

Publicly verifiable antecedent work includes:

- KSCST 46th Series SPP (2022–23), project reference **46S_BE_5506**, “Connecting Rural Communities Through CubeSats: AI Based Model for E-Learning in Remote Areas.”
- **Smart Charge Pro**, IOSR-JCE, July–August 2023, DOI **10.9790/0661-2504010108**.
- **A Personalized E-Learning System Using Reinforcement Learning Through Satellite**, IEEE INDICON 2023, DOI **10.1109/INDICON59947.2023.10440852**.

Those items can support a truthful career/research timeline, but they are not evidence that these 2026 security repositories existed in 2022–2024.

**Audit date:** 2026-09-21
