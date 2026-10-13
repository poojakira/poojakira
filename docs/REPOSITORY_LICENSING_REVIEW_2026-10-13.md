# Repository Licensing Review — 2026-10-13

> **READ THIS LICENSE BEFORE COPYING, USING, MODIFYING, OR REDISTRIBUTING.** This inventory is a licensing review, not a legal opinion, audit certification, or assertion that previously granted open-source rights can be revoked.

## Verified account and scope

- Connected GitHub login: `poojakira` (GitHub user ID `90021441`). No other owner or account was used.
- Repositories inventoried: **20**, all owned by `poojakira`, default branch `main`.
- Main-branch root LICENSE inventory at the beginning of the review: **11 MIT**, **4 Apache-2.0**, **1 proprietary**, **4 missing**.
- A read-only file-tree inventory and first-page sample of up to 100 recent commits per repository were inspected. This **does not establish complete source-level correctness, chain of title, full contributor history, or testing**.
- No independent subagents or third-party counsel were engaged; checks were coordinated through the connected account and are not equivalent to independent peer reviews.

## Proposed restrictive license

The draft LICENSE is proprietary and All Rights Reserved for original owner-controlled material. It does not grant copying, adaptation, redistribution, use in other products, or commercial deployment without express prior written permission, subject to GitHub's Terms of Service and applicable law. It reserves no rights in third-party works and does not revoke valid prior grants. Making code public still permits viewing and forking under GitHub's platform rules.

## Repository-by-repository change status

| Repo | Main-license status before work | Review branch / PR |
| --- | --- | --- |
| PulseNet-RUL-Forecasting | Apache-2.0 | [#95](https://github.com/poojakira/PulseNet-RUL-Forecasting/pull/95), draft |
| poojakira | No root LICENSE | [#33](https://github.com/poojakira/poojakira/pull/33), draft |
| mcp-agent-security-gateway | MIT | [#128](https://github.com/poojakira/mcp-agent-security-gateway/pull/128), draft |
| hf-model-provenance-scanner | Apache-2.0 | [#74](https://github.com/poojakira/hf-model-provenance-scanner/pull/74), draft |
| dataset-poisoning-detector | MIT | [#89](https://github.com/poojakira/dataset-poisoning-detector/pull/89), draft |
| model-privacy-attacks | MIT | [#51](https://github.com/poojakira/model-privacy-attacks/pull/51), draft |
| llm-redteam-framework | MIT | [#61](https://github.com/poojakira/llm-redteam-framework/pull/61), draft |
| adversarial-ml-lab | MIT | [#61](https://github.com/poojakira/adversarial-ml-lab/pull/61), draft |
| unified-ml-security-platform | Apache-2.0 | [#53](https://github.com/poojakira/unified-ml-security-platform/pull/53), draft |
| attack-v19-core | MIT | [#43](https://github.com/poojakira/attack-v19-core/pull/43), draft |
| attack-detection-engine | No root LICENSE; pyproject said MIT | [#32](https://github.com/poojakira/attack-detection-engine/pull/32), draft |
| mlsec-benchmark-suite | Apache-2.0 | [#33](https://github.com/poojakira/mlsec-benchmark-suite/pull/33), draft |
| aws-agent-identity-guard | MIT | [#54](https://github.com/poojakira/aws-agent-identity-guard/pull/54), draft |
| ml-security-command-center | MIT | [#16](https://github.com/poojakira/ml-security-command-center/pull/16), draft |
| mlsec-dashboards | MIT | [#44](https://github.com/poojakira/mlsec-dashboards/pull/44), draft |
| poojakira.github.io | No root LICENSE | [#14](https://github.com/poojakira/poojakira.github.io/pull/14), draft |
| Pooja_Kiran_Portfolio_Website | No root LICENSE | [#110](https://github.com/poojakira/Pooja_Kiran_Portfolio_Website/pull/110), draft |
| pooja_carrier-website | MIT | [#42](https://github.com/poojakira/pooja_carrier-website/pull/42), draft |
| OS-Resource-Management-Simulator-Dockerized-Flask-Application | MIT | [#7](https://github.com/poojakira/OS-Resource-Management-Simulator-Dockerized-Flask-Application/pull/7), draft |
| SentinelMesh-AI-Control-Plane | Already proprietary | LICENSE and README committed directly to main |

All 19 draft PRs are **unmerged**. Their contents remain proposals, not current main-branch licensing changes.

## Review evidence and boundaries

- Each proposed LICENSE and README notice was checked on the corresponding work branch. **All 20 reviewed README variants begin with the requested READ THIS LICENSE notice**.
- The 19 pull-request changed-file inventories were checked. They affect only LICENSE, README, historical license archives, package metadata, or the known third-party notice; no production source, CI workflow, pilot config, credentials or deployment files were edited through these PRs.
- For the gateway/Cerberus PR specifically, changed paths were `LICENSE`, `README.md` and `docs/license-history/LICENSE-BEFORE-2026-10-13.txt` only. Cerberus pilot/runtime/identity/baseline material was not changed.
- Seven PRs were initially marked mergeable but `unstable` by GitHub while the main CI workflow was still in progress. Their then-visible documentation, security-hygiene and production gates were successful. That was not a completed CI signoff.
- Up to 100 latest commits per repository were sampled; the sample included an `audit-reviewer` author in PulseNet and an `AI Agent` author in attack-v19-core. Authorship alone does not prove ownership or identify who controls copyright. Earlier commits were not exhaustively reviewed.
- Third-party notices in the Career OS repository and MITRE ATT&CK attribution were preserved; attack-v19's own license description was corrected in its third-party notice.

## Mandatory pre-merge review gates

- [ ] **Copyright/license counsel:** confirm chain of title, third-party rights, existing public releases and contributor grants; no retroactive revocation claims.
- [ ] **Senior security engineer:** confirm no protected Cerberus material or deployment/secret change; verify no accidental source-level modifications in each PR.
- [ ] **Senior build/release engineer:** run packaging validation, active CI, and check Python metadata/license-file inclusion for affected distributions.
- [ ] **Documentation reviewer:** verify badges, README, LICENSE, historical notices, package metadata and related .md documents agree.
- [ ] **Independent reviewer:** review the diff and approve each PR; leave as draft until verified.
- [ ] **Owner:** decide whether public repository visibility is compatible with preventing copying. A written license alone cannot physically prevent access or forking.

Do not describe this work as a completed legal certification, complete line-by-line audit, or fully tested product-wide remediation.
