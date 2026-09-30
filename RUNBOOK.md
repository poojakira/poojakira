# Repository Security and Recovery Runbook

**Repository:** `poojakira/poojakira`

## Normal release path

1. Make a small change on a review branch.
2. Open a pull request into `main`.
3. Require the Profile CI, Production Gate, Documentation Integrity, and Security Hygiene workflows to pass.
4. Review public claims and links before merge.
5. Merge without rewriting historical commits.

## Secret exposure

If a real token, password, private key, or credential is ever committed:

1. **Revoke or rotate it immediately.** Removing the file does not invalidate an exposed credential.
2. Remove the secret from the current branch.
3. Determine whether it exists in reachable Git history.
4. If history contains the secret, rewrite the affected history with an approved history-cleaning tool and coordinate any force update carefully.
5. Re-run the security-hygiene workflow.
6. Review GitHub secret-scanning alerts if available.
7. Document the incident without reproducing the secret.

## Broken main / rollback

This repository has no runtime database or mutable application state. Recovery is therefore source-control based.

1. Identify the last known-good commit with all required checks passing.
2. Prefer `git revert` of the bad change so history remains auditable.
3. Push the revert through the normal CI gates.
4. Confirm README rendering and linked evidence after the revert.
5. Do not backdate or silently rewrite provenance to hide an incident.

## CI failure

- **Security Hygiene:** inspect the reported file/action/pattern and remove the unsafe content or workflow setting.
- **Profile CI:** restore required evidence files or correct retired/unsupported profile claims.
- **Production Gate:** remove unresolved placeholders or merge markers.
- **Documentation Integrity:** fix incomplete or conflicting public documentation.

Do not bypass a failing gate merely to make `main` green.

## GitHub account / repository recovery

Git history is the primary recovery record. For stronger disaster recovery, maintain an independent authenticated mirror or offline clone outside the same GitHub account. This repository does not currently create an independent off-platform backup automatically.

## Branch protection

The intended `main` policy is:

- require pull requests before merge;
- require the four repository checks to pass;
- prevent force pushes and branch deletion;
- require conversation resolution;
- restrict bypasses.

This setting is administered by GitHub repository settings and is not encoded by a file in this repository.
