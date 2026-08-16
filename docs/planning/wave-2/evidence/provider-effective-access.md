# Effective provider development access

Mission: `W2-ENG-PROVIDER-EFFECTIVE-01` (producer Issue #373), remediated by
`W2-ENG-PROVIDER-EFFECTIVE-REM-01` (Issue #400), the recorder worktree recovery
`W2-ENG-PROVIDER-RECORDER-REM-01` (Issue #421), and the bounded recorder
publication recovery `W2-ENG-PROVIDER-RECORDER-PR-REM-01` (Issue #440).

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

The recorder's syntax check reads the trusted projection source and compiles it
in memory. It then requires a clean checkout before projection and, after
projection, requires the exact generated evidence path to be the sole worktree
change. These fail-closed guards were integrated from Issue #421 and passed in
fresh trusted-main executions after publication.

## Reviewed publication route

`.github/workflows/engine-eval-evidence-recorder.yml` never commits or pushes
generated evidence directly to `main`. Its recorder permissions are limited to
`actions: read` and `contents: write`, sufficient to inspect the exact upstream
run and publish the sanitized projection on the deterministic bounded evidence
branch:

`evidence/provider-effective-access/run-<run_id>-attempt-<run_attempt>`

The recorder itself publishes **only** that exact branch. It does not use the
Actions `GITHUB_TOKEN` to create a pull request. After the exact staged-path
check, commit, and branch push succeed, the workflow emits the branch, evidence
path, run/source identities, and an explicit handoff state declaring that a
draft PR is still required.

A separate normal repository ownership/recovery episode must then open the
draft PR from that immutable evidence branch to `main`. The full publication
boundary remains `BOUNDED_EVIDENCE_BRANCH_DRAFT_PR`: moving PR creation out of
the Actions token boundary does not weaken the required draft-PR handoff and
does not make a bare branch integrable. Workflow success never grants
integration or provider authority. Any later evidence integration still
requires separately derived current authority, a fresh exact expected-head
check, and squash-only integration.

This split is the bounded recovery from fresh post-Issue-421 execution. Trusted
main evaluator run `31959049126` succeeded at source SHA
`437b9fc60d1db8cdc2c2006096707bdb9ee8276f`; recorder run `31959057717`
successfully completed source/workflow binding, exact checkout, side-effect-free
projection-code validation, artifact download, projection, the exact
single-evidence-path worktree guard, commit, and branch push. It failed only
when its Actions token attempted REST draft-PR creation and received HTTP 403.
The already-pushed immutable branch
`evidence/provider-effective-access/run-31959049126-attempt-1` at
`ad34a0039d99efd04869ae8aeceaed2097d30924` was recovered without byte changes
as draft PR #438 by a normal repository episode. Recorder run `31959057717`
remains failed provenance; the recovery does not relabel it as workflow success.
No PAT, long-lived credential, or broader secret boundary was introduced.

## Current fresh evidence state

The recovered evidence for run `31959049126` remains fail-closed and grants no
provider unlock:

- Unity: `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION`, blocker
  `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED`;
- Unreal Engine: `NOT_CONFIGURED`, blocker
  `UNREAL_GITHUB_USERNAME_AND_TOKEN_NOT_CONFIGURED`.

Neither provider is unlocked, neither native hosted-CI path is eligible from
this evidence, and no commercial, production, legal, release, engine-selection,
integration, readiness, verification, decision, or canonical authority follows.

## Preserved authority boundaries

The remediation does not change provider independence, local-vs-hosted
evidence semantics, the scoped Unreal entitlement prerequisite, or Issue #82
provenance. It grants no provider credential, engine selection, commercial,
production, legal, release, readiness, verification-PASS, decision,
integration, or canonical authority.

Fresh required security/authority review of the exact Issue #440 remediation
packet remains mandatory before the publication-mechanism change may be
squash-published to `main`.
