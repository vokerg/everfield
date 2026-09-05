# Fresh security/authority review — Issue #862 / PR #876

## Frozen target

- Producer Issue: #862
- Producer PR: #876
- Exact judged head: `32bb15e85320365f876b879cc916c35520f91201`
- Predecessor review: #859, terminal `CHANGES_NEEDED`
- Predecessor finding: `W2-ENG-TECH-UNITY-S3-V5-RECORDER-TRIGGER-REM02-REV-M01`
- Review trust mode: `DEGRADED_SINGLE_AGENT`

## Disposition

`PASS_FOR_INTEGRATION`

Findings: 0 blocker, 0 major, 0 correction-requiring minor, 0 informational.

This disposition is integration eligibility for the exact judged producer head only. It is not integration authority and grants no native/provider PASS, verification PASS, engine selection/readiness, decision, release, or canonical authority.

## Security/authority attacks

### 1. Token placement, lifetime, and persistence

The two recorder checkouts remain `persist-credentials: false`. The repository token is added only to the final GitHub-hosted publication step as `GH_TOKEN: ${{ github.token }}`. The step derives an HTTP Basic header in a shell variable and supplies it to exactly one `git push` via process-scoped `GIT_CONFIG_COUNT` / `GIT_CONFIG_KEY_0` / `GIT_CONFIG_VALUE_0` environment values. The header is not embedded in the remote URL and is not written to local Git configuration. `set -euo pipefail` is used without xtrace, and the derived shell variable is unset immediately after the push.

Result: clean.

### 2. Hosted-vs-native authority separation

The native Unity lineage job remains under the evaluator workflow's read-only `contents: read` default and remains on `[self-hosted, macOS, ARM64, everfield-unity]`. The post-lineage dispatch-control job is GitHub-hosted and receives only `actions: write`. The recorder is a separate GitHub-hosted workflow with `actions: read` plus `contents: write`. No repository-content write token is introduced on the persistent native Unity job.

Result: clean.

### 3. Exact predecessor failure mode

The producer validator now requires exactly two non-persisting checkouts and forbids `persist-credentials: true`. Its negative controls mutate the recorder back to the exact unauthenticated plain-push topology by deleting the bounded auth region and restoring `git push origin "HEAD:refs/heads/$EVIDENCE_BRANCH"`; that mutation is required to fail validation. A second negative control turns one checkout into credential-persisting mode and is also required to fail.

Exact-blob deterministic execution of the validator returned `unity-s3-v5 recorder trigger temporal/static contract: PASS`.

Result: clean; predecessor MAJOR is remediated.

### 4. Publication bounds

The recorder still creates exactly one run/attempt evidence branch, stages exactly one generated evidence path, has no direct-main push, reports `draft_pr_created_by_workflow: False`, requires a later normal ownership episode to open any evidence PR, and reports `integration_authority: False`.

Result: clean.

### 5. Exact identity and terminality gates

The already-reviewed separate-run topology is preserved: exact run id, attempt, workflow identity/path, repository, branch, event, source head, terminal success, current-main equality, recorder-workflow SHA equality, exact artifact name/run binding, exact projection-code head, bounded polling, and a final immediate recheck before publication. The evaluator/source-gate blobs are unchanged from the predecessor reviewed head.

Result: clean.

### 6. Authority inflation

Neither deterministic validation nor publication mechanics executes native Unity or creates evidence that can establish provider PASS, comparison PASS, verification PASS, engine selection/readiness, decision, release, or canonicality. Those authorities remain false/absent in the producer handoff and PR description.

Result: clean.

## Required next route

Materialize exactly one separately authorized squash-only integration issue for producer Issue #862 / PR #876 exact head `32bb15e85320365f876b879cc916c35520f91201`, after rechecking current `main`, exact head immutability, absence of superseding remediation, and conflicts. Review provenance itself does not need publication merely to authorize the producer integration.
