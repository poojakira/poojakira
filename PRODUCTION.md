# Production Operating Contract

## Repository role

This repository is the public GitHub profile and evidence index for `poojakira`. It is **not** an application runtime: it does not expose an API, database, authentication system, payment flow, webhook receiver, or upload endpoint.

## Release objective

Keep public profile claims, security documentation, and evidence links accurate, reviewable, and reproducible.

## Required gates

A change to `main` is considered release-ready only when these checks pass:

- **Profile CI**
- **Production Gate**
- **Documentation Integrity**
- **Security Hygiene**

The repository security scanner rejects tracked secret files, high-confidence provider-token literals, unpinned third-party Actions, write-enabled workflow permissions, unsafe workflow triggers, and checkout steps that persist credentials.

## Public-data rules

- Do not commit secrets, private keys, service-account files, access tokens, passwords, or local environment files.
- Do not publish private/internal URLs or unsupported security claims.
- Quantitative claims must link to repository-level evidence and identify their scope.
- Use HTTPS for external links.
- Do not use Git-history rewrites to manufacture provenance.

## Dependency and workflow policy

- GitHub Actions are pinned to immutable 40-character commit SHAs.
- Workflow permissions remain read-only.
- `actions/checkout` uses `persist-credentials: false`.
- Dependabot monitors GitHub Actions weekly.
- CODEOWNERS assigns the repository to `@poojakira`.

## Recovery

There is no mutable production database to restore. Rollback is source-control based: identify the last known-good commit, revert the bad change, and require the normal CI gates to pass. See [RUNBOOK.md](RUNBOOK.md).

## Security scope

The full control matrix is in [SECURITY_CHECKLIST.md](SECURITY_CHECKLIST.md). Application controls such as RLS, SQL injection defense, CORS, rate limiting, password hashing, payment idempotency, and upload validation are marked N/A because this repository does not contain those runtime surfaces.

## GitHub-hosted control still required

The `main` branch currently reports as unprotected and no repository ruleset is configured. Repository-admin settings should require pull requests, passing checks, conversation resolution, and block force pushes/deletion. This control cannot be enabled from repository files alone.
