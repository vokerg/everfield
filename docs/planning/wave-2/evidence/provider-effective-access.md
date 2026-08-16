# Effective provider development access

Mission: `W2-ENG-PROVIDER-EFFECTIVE-01` (producer Issue #373), remediated by
`W2-ENG-PROVIDER-EFFECTIVE-REM-01` (Issue #400).

This packet separates lawful development execution from commercial, production,
legal, licensing, release, integration, decision, and canonical authority. A
provider is unlocked only by its own validated native path. Unity and Unreal are
never combined into one prerequisite, and the historical Issue #82 set of 50
`NOT_RUN` cells remains immutable.

## Current bootstrap observations

- The `engine-eval` GitHub Environment remains the credential boundary for
  trusted `main`. Version variables remain `UNITY_EDITOR_VERSION=6000.5.6f1`
  and `UNREAL_ENGINE_VERSION=5.8`.
- Unity service-account authentication is a valid identity probe, but it does
  not itself establish a portable Personal-license entitlement for an
  ephemeral GitHub-hosted runner.
- The durable local Unity `6000.5.6f1` S3 N1/N2/FI1 result remains local
  development evidence only. It does not become GitHub-hosted CI validation.
- Unreal Epic/GitHub entitlement and a dedicated package-read credential remain
  scoped prerequisites only for actual credentialed Unreal execution.
  Non-secret Unreal CI/container/native-S3 preparation remains eligible.

## Trusted execution identity

`.github/workflows/engine-eval-credentialed.yml` uses only `contents: read`,
runs only for the trusted repository on `main` in `engine-eval`, and checks out
the exact event `github.sha`. Before any provider secret is consumed, it fails
closed unless the checkout identity equals that trusted-main event SHA.

The downstream recorder accepts only a successful `push` run for trusted
`main`. It queries the GitHub Actions API and binds the run to the exact
workflow id and path
`.github/workflows/engine-eval-credentialed.yml`, the exact run attempt, and
the exact upstream `head_sha`. It then checks out that upstream SHA and executes
`tools/planning/record_provider_effective_access.py` from that same code
identity. The projected evidence records the workflow identity, source head,
projection-code SHA, and observed publication-base main SHA. Artifact content
is treated only as data and is never executed.

## Reviewed publication route

`.github/workflows/engine-eval-evidence-recorder.yml` no longer commits or
pushes generated evidence directly to `main`. Its write permission is limited
to staging the sanitized projection on a deterministic bounded evidence branch:

`evidence/provider-effective-access/run-<run_id>-attempt-<run_attempt>`

The recorder then opens a draft PR to `main`. The generated PR is an immutable
evidence handoff, not an integration decision. It explicitly requires the
repository ownership/review protocol and a separately authorized squash-only
integration with a fresh exact expected-head check. Workflow success never
grants integration authority.

## Preserved authority boundaries

The remediation does not change provider independence, local-vs-hosted
evidence semantics, the scoped Unreal entitlement prerequisite, or Issue #82
provenance. It grants no provider credential, engine selection, commercial,
production, legal, release, readiness, verification-PASS, decision,
integration, or canonical authority.

Fresh required review of the exact remediation packet remains mandatory before
`PASS_BOUNDED_PROVIDER_EFFECTIVE_ACCESS`.
