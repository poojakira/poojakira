# Resume Metrics Evidence

This page is the central index for quantitative security-project claims used on Pooja Kiran's resume.

The resume intentionally freezes validated snapshots from the period when the application materials were prepared. Repositories may later contain more tests or newer measurements. A newer, higher total does not make the earlier snapshot false; the historical evidence remains linked below.

## MCP Agent Security Gateway

Resume values:

- **622 passing tests**
- **78% statement coverage**
- **9 MITRE ATT&CK-mapped Elastic Security detection rules**
- **21 core SIEM tests**

Evidence: https://github.com/poojakira/mcp-agent-security-gateway/blob/main/RESUME_EVIDENCE.md

The 622/78% snapshot is directly backed by successful GitHub Actions run:
https://github.com/poojakira/mcp-agent-security-gateway/actions/runs/33696855146

That run reports 622 passed and 78.41% measured statement coverage, rounded to 78% on the resume.

The repository later grew through 641 passing tests at 79.54% and 659 tests at 82%. The current verified baseline on `main` is **707 passing tests / 82.85% statement coverage** on Python 3.12, with the same suite green on Python 3.10 and 3.11. Current project/profile claims should cite the repository's `VERIFIED_METRICS.md`; the older figures above remain historical resume snapshots.

## AWS Agent Identity Guard

Resume values:

- **25 rule IDs**
- **230 passing tests**
- **p95 under 10 ms per policy**
- **more than 1,000 policies/second**

Evidence: https://github.com/poojakira/aws-agent-identity-guard/blob/main/RESUME_EVIDENCE.md

The performance figures are CI regression gates on a 500-policy synthetic benchmark, not universal production guarantees. The historical main-CI baseline is **231 passed, 3 skipped** with **1.1040 ms p95** and **1,913 policies/second**. The current verification section in `VERIFIED_METRICS.md` records **235 passed, 3 skipped** on current main and a local synthetic benchmark of **0.6935 ms p95** and **3,178 policies/second**; those newer performance values are local measurements, not production throughput.

## HF Model Provenance Scanner

Resume values:

- **195 passing tests**
- **12/12 core incident reproductions**
- **18/18 extended variants**
- **0 actionable false positives across four committed benign samples**

Evidence: https://github.com/poojakira/hf-model-provenance-scanner/blob/main/RESUME_EVIDENCE.md

The 195 figure is a committed historical Windows/Python 3.12.10 validation snapshot recorded in the runbook. Later Linux CI grew beyond that snapshot; the current verified repository baseline is **211 passed** plus **6 additional pytest subtests**, with **66.90%** statement coverage on Python 3.11/3.12. The historical 195 value remains provenance for the frozen résumé snapshot, not the current project count.

The 12/12, 18/18, and four-benign-sample claims are fixture-scoped. They are not claims of universal detection accuracy or a universal 0% false-positive rate.

## Interview rule

When discussing these numbers:

1. Call them **validated resume snapshots**.
2. If asked why GitHub currently shows a higher count, explain that the repository continued to evolve after the resume snapshot.
3. Never describe the HF four-sample result as a universal zero false-positive rate.
4. Describe the MCP nine items as **Elastic Security detection rules** that generate alerts when matched, not nine observed alert events.
5. Describe the AWS latency/throughput numbers as **CI performance gates** on the committed synthetic benchmark.
