# Verification report

**LOCAL ONLY.** Tested source: f6221f84505443bbcaa29d9a027963505c41841a. Fixing source at report time: f6221f84505443bbcaa29d9a027963505c41841a. Hosted observations in [audit findings](AUDIT_FINDINGS.md) identify their separate source SHAs.

python scripts/verify_profile.py and python scripts/verify_metrics_manifest.py exited 0. Both assess tracked references and claims. The public primary résumé returned HTTP 200 and pdfinfo reported one letter page.

Python 3.12.14 executed both source checks. The HTTP API response confirmed the recorded CI run status and SHA. The directly linked HTML counterpart resolved to 404 from this environment.



The local workflow syntax check used actionlint 1.7.7. The Markdown lexical check inspected relative file targets. It does not establish heading fragments, external targets, or example commands. Logs and command wrappers are in the workspace audit directory.
