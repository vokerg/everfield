# Issue #808 handoff — Unity S3 v5 artifact liveness remediation

## Mission
`W2-ENG-TECH-UNITY-S3-V5-ARTIFACT-LIVENESS-REM-01`

## Frozen source / routing
- base/current-main at claim: `eb81d354931c67ef2193f5242e49ee181a270b8c`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- source terminal: Issue #801 comment `5511384835`
- source route: `OBSERVE_EXISTING_EXACT_MAIN_RUN_33642634779_AND_ROUTE_ONLY_IF_ARTIFACT_PUBLICATION_FAILURE_RECURS`
- recurrence run/job: `33642634779` attempt 1 / `100289313431`
- recurrence runner: `everfield-unity-mac` / id `21`

## Observed recurrence
The exact existing main run reproduced the prior failure class. Exact-SHA/runner fencing, deterministic self-tests, pinned Unity `6000.5.6f1`, native S3 execution, and sanitized validation all passed. `actions/upload-artifact` then failed with `403 Forbidden: job is completed`; the run has zero artifacts.

GitHub's job record reports `started_at=2026-09-02T14:54:01Z` and `completed_at=2026-09-02T15:04:02Z`, while runner-reported native execution continued until `15:10:21Z` and upload ran afterward. Issue #801's prior failed attempt shows the same server-completed-before-runner-finished shape. The successful first attempt completed native execution in about 23 seconds and uploaded normally. The workflow already has `timeout-minutes: 30`, so this remediation does not change timeout policy.

## Bounded change
Owned workflow: `.github/workflows/unity-s3-v5-lineage-evaluator.yml`.

The native producer step now:
1. fails closed unless macOS `caffeinate` is present: `command -v caffeinate >/dev/null`;
2. runs only the long lineage producer invocation under `caffeinate -i`;
3. leaves the producer arguments, post-production validator, sanitized-shape assertion, and pinned upload action unchanged.

The `caffeinate` assertion is scoped to the producer process lifetime because the producer is passed directly as the utility executed by `caffeinate`; no background inhibitor survives the command.

## Producer verification
At remediation commit `4fd4897425c00233c0eb3826cf4411a4c62b11d8`:
- compare against frozen main is `ahead 1 / behind 0`, merge base exactly frozen main;
- changed paths: exactly `.github/workflows/unity-s3-v5-lineage-evaluator.yml`;
- workflow diff size: additions `2`, deletions `1`, changes `3`;
- fetched branch workflow confirms exactly one `command -v caffeinate >/dev/null` guard and the native invocation `caffeinate -i python3 tools/planning/unity_s3_v5_lineage.py`;
- repository/ref/event/current-main/runner gates are unchanged;
- `runs-on: [self-hosted, macOS, ARM64, everfield-unity]` is unchanged;
- `permissions: contents: read` is unchanged;
- checkout and upload-artifact action SHAs are unchanged;
- `timeout-minutes: 30` is unchanged;
- Unity version and lineage producer/validator semantics are unchanged;
- no producer-branch Unity dispatch was performed.

## Required next gate
Fresh independent/degraded-independent security/authority review of the exact immutable producer head and draft PR. Review must verify liveness-guard scoping/fail-closed behavior and prove no trust, permission, evidence, workflow-trigger, runner-identity, or authority expansion. A clean review may grant only `PASS_FOR_INTEGRATION`; integration remains a separate squash-only episode.

## Authority
`NOT_CANONICAL`. This remediation does not create durable Unity comparison evidence, provider PASS, verification PASS, engine selection/readiness, integration authority, or canonical authority.
