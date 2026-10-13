# Proprietary Licensing and Contribution Controls — October 13, 2026

> **READ THE [LICENSE](../LICENSE) FIRST.** This is a fact-checked engineering/change-status report, **not a legal opinion**, independent security certification, code audit, or guaranteed anti-copy protection.

## Owner and repository IDs

Connected owner `poojakira`, GitHub user ID `90021441`. Only that owner's account and its **20 repositories** were used. Each repository ID below was retrieved from the authorized GitHub inventory. Repository name/ID pairs are for traceability, not identity or copyright certification.

| Repository | GitHub repository ID | Contributor-policy PR | Status at time of report |
| --- | --- | --- | --- |
| `PulseNet-RUL-Forecasting` | `1144890505` | [#96](https://github.com/poojakira/PulseNet-RUL-Forecasting/pull/96) | merged |
| `poojakira` | `1185591185` | [#35](https://github.com/poojakira/poojakira/pull/35) | merged |
| `mcp-agent-security-gateway` | `1296742217` | [#130](https://github.com/poojakira/mcp-agent-security-gateway/pull/130) | merged |
| `hf-model-provenance-scanner` | `1296924027` | [#75](https://github.com/poojakira/hf-model-provenance-scanner/pull/75) | awaiting CI |
| `dataset-poisoning-detector` | `1297030364` | [#90](https://github.com/poojakira/dataset-poisoning-detector/pull/90) | merged |
| `model-privacy-attacks` | `1297083816` | [#52](https://github.com/poojakira/model-privacy-attacks/pull/52) | merged |
| `llm-redteam-framework` | `1297084181` | [#63](https://github.com/poojakira/llm-redteam-framework/pull/63) | merged |
| `adversarial-ml-lab` | `1298836838` | [#62](https://github.com/poojakira/adversarial-ml-lab/pull/62) | merged |
| `unified-ml-security-platform` | `1304457284` | [#55](https://github.com/poojakira/unified-ml-security-platform/pull/55) | merged |
| `attack-v19-core` | `1309398318` | [#45](https://github.com/poojakira/attack-v19-core/pull/45) | merged |
| `attack-detection-engine` | `1309398846` | [#35](https://github.com/poojakira/attack-detection-engine/pull/35) | merged |
| `mlsec-benchmark-suite` | `1316615336` | [#35](https://github.com/poojakira/mlsec-benchmark-suite/pull/35) | merged |
| `aws-agent-identity-guard` | `1319550579` | [#56](https://github.com/poojakira/aws-agent-identity-guard/pull/56) | merged |
| `ml-security-command-center` | `1319966233` | [#17](https://github.com/poojakira/ml-security-command-center/pull/17) | merged |
| `mlsec-dashboards` | `1321196861` | [#47](https://github.com/poojakira/mlsec-dashboards/pull/47) | merged |
| `poojakira.github.io` | `1321308766` | [#15](https://github.com/poojakira/poojakira.github.io/pull/15) | merged |
| `Pooja_Kiran_Portfolio_Website` | `1337687918` | [#113](https://github.com/poojakira/Pooja_Kiran_Portfolio_Website/pull/113) | merged |
| `pooja_carrier-website` | `1338052403` | [#43](https://github.com/poojakira/pooja_carrier-website/pull/43) | merged |
| `OS-Resource-Management-Simulator-Dockerized-Flask-Application` | `1402366088` | [#8](https://github.com/poojakira/OS-Resource-Management-Simulator-Dockerized-Flask-Application/pull/8) | merged |
| `SentinelMesh-AI-Control-Plane` | `1403833631` | [#3](https://github.com/poojakira/SentinelMesh-AI-Control-Plane/pull/3) | merged |

## On-main baseline — verified

- All 20 default branches are `main`. The same custom proprietary `LICENSE` file exists in all 20, with blob SHA `0cc5b47ccc747f9be0dcfb600dfb84920e62dc63`.
- All 20 root README files begin with **READ THIS LICENSE**.
- Initial licenses: 11 MIT, 4 Apache-2.0, 1 existing proprietary, and 4 absent. All 19 first-round licensing PRs merged, with prior license grants preserved and historical texts archived for the previous MIT/Apache repositories.
- 14 repositories are public; 6 are private. Repository visibility was not modified.
- Contributor access: owner-maintained, no unsolicited external source, asset or documentation contributions. Written permission plus a separate contributor rights arrangement is required for new invited work. This policy is not a substitute for enforceable signed agreements.

## Follow-up remediation

- Added a new `CONTRIBUTING.md` to repositories that lacked one; updated existing contribution guides to make development instructions usable only by expressly authorized contributors.
- `mcp-agent-security-gateway`: replaced Rust `license = "MIT"` with `license-file = "LICENSE"` and added `rust/LICENSE`. Changed only licensing metadata and contributor documentation. No Cerberus pilot, identity, baseline, runtime, credentials, or deployment files were changed.
- `hf-model-provenance-scanner`: corrects the stale Apache license label in `RUNBOOK.md`.
- `adversarial-ml-lab`: removes the obsolete sentence licensing future contributions as MIT.
- `attack-v19-core`: corrects `THIRD_PARTY_NOTICES.md` from proposed to current status while retaining MITRE rights.
- `PulseNet-RUL-Forecasting`: clarifies that a historic 2025 copyright notice cannot backdate Git provenance and that prior grants survive.

## Access and enforceability limitations

A public GitHub repository can still be viewed and forked through GitHub under its Terms of Service. A proprietary notice cannot technically disable screenshots, local copies or cloning; copyright remedies depend on rights ownership, jurisdiction, conduct and applicable legal exceptions. Valid MIT/Apache-2.0 rights given for earlier code versions are not retroactively revoked. Libraries, data, fonts, model artifacts, third-party contributions and other assets that are not owned by Pooja Kiran are **not** brought under exclusive ownership by this notice. Taking the 14 public repositories private would affect discoverability and potentially website/deployment workflows and was **not** authorized or performed.

## Assurance and incomplete work

- GitHub PR changed-path checks performed: docs, license metadata and attribution files only. This does **not** establish a full per-line security audit.
- GitHub CI success is confirmed where PR workflow runs returned completed successful checks; some private repos returned no PR workflow runs. No universal CI certification is claimed.
- Full chain-of-title verification, all-history author/contributor review, lawyer review, independently reviewed approvals, future-version SPDX/SBOM audit, actual license enforcement, and line-by-line review of every source file remain **unverified**.
- Desktop Commander device was reported offline during the review, so a separate local multi-agent execution was not possible. Connected GitHub checks were parallelized but were not independent human or autonomous-agent audits.

**Do not assert that prior open-source rights are revoked or that public source code cannot be copied in practice.**
