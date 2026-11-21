# Audit findings

## Repository state

Default branch main is e6fb795820de8cf16fed9c6fdbabf937e62f5d43. Review started at e6fb795820de8cf16fed9c6fdbabf937e62f5d43. The collected inventory contains 46 pull requests, 4 issues and 1 Git tags. The public Releases API returned zero release records.

### Open pull requests

- [#50 Reframe GitHub profile as Software Engineer | AI Agents & Application Security](https://github.com/poojakira/poojakira/pull/50)
- [#47 ci: bump actions/setup-python from 7.0.0 to 7.1.0](https://github.com/poojakira/poojakira/pull/47)



### Open issues

No open issues in the collected inventory.



### Hosted runs in collected history

- Success on 7cf9fbe4cb733e9b3e9d91f191b2832c997d815b, 2026-11-20T01:48:25Z. [Security Hygiene](https://github.com/poojakira/poojakira/actions/runs/44656255440)
- Failure on 4be5f2180ef149ad98bb689a3abc6fd3f10b511e, 2026-11-20T01:47:44Z. [Profile CI](https://github.com/poojakira/poojakira/actions/runs/44656173132)

Historical Profile CI failure 44656173132 executed the profile evidence verification step. Category B. A later run passed on a different commit.

## Confirmed defects

| ID | Severity | Affected file and lines | Root cause, impact and remediation | Status |
|---|---|---|---|---|
| PROFILE-01 | Low | README.md:12–55 | The profile emphasized the legacy résumé links and labeled Aegis coverage as statements. The profile now links the generated résumé and uses the archive’s line-coverage terminology. The evidence index and parity checker agree. | Implemented locally |
| PROFILE-02 | Low | README.md and RESUME_METRICS_EVIDENCE.md | The queued CI HTML page returned HTTP 404. The public actions API returned the exact head, queued status and empty conclusion for the same run ID. The profile and index now link to the verified API record. | Implemented locally |

## Residual risk

The profile describes exact archived draft snapshots. Static checks cannot establish that each external asset remains available or that a project is ready for deployment.

The review includes the named PRs, selected source, local workflow syntax, relative file targets in Markdown, and the executed checks in [verification](VERIFICATION_REPORT.md). Complete source review, historical per-run root cause classification and validation of all operational documentation remain incomplete.
