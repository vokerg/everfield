# Issue #1099 handoff — review of factory CI rate-limit deferral

## Status
Required degraded-independent review complete. Disposition: `PASS_FOR_INTEGRATION_WITH_POST_PUBLICATION_WORKFLOW_ACCEPTANCE`.

This review is NOT_CANONICAL and grants no direct integration, verification, planning, engine-selection, implementation-readiness, release, decision, or canonical authority.

## Review ownership / basis
- Review issue: #1099 / `FACTORY-CI-REC-REV-01`
- Winning claim: `5659153875`
- Reviewer actor/session: `factory-ci-rate-limit-review-gpt56sol-20260914-01`
- Trust mode: `DEGRADED_SINGLE_AGENT`
- Review branch: `planning/issue-1099`
- Review base/current main at claim: `13272159e2d4c9921aeb410a0a85cb470eaa23d7`
- Review report work SHA: `05e100b7951e24cb999843f94cb9f17dfb412291`

## Frozen producer
- Producer Issue #1092
- Producer claim: `5659081470`
- Producer terminal: `5659110488`
- Producer PR: #1095
- Exact producer head: `9e21f1dbb6cdb29f8b796595b4985932075dd0f6`
- Substantive producer work: `7e846263fb0f37be3f43069d17d95c8a93cf8db1`
- Producer base: `1abb5fe9638b00c90180fdbae4d770e64fcbcc9c`
- Producer PR remained open/draft/mergeable at review completion.
- Exact producer files:
  - `tools/planning/frontier_maintenance.py`
  - `tools/planning/frontier_maintenance_v5.py`
  - `docs/planning/handoffs/issue-1092.md`

## Review result
0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR / 2 INFO.

The exact candidate:
- distinguishes only explicit GitHub API rate exhaustion into `GitHubRateLimitExceeded`;
- preserves generic permission/auth 403 failures as fatal;
- catches only the typed rate-limit exception in v5;
- emits `reconciliation_complete: false` and `authority_created: false` when deferring;
- leaves schema-3 ownership, review, terminal, successor, dispatch, exact-main, allowlist, and canonical authority rules unchanged;
- remains safe under partial idempotent progress and exact-main dispatch retry discovery.

Full report:
`docs/planning/reviews/factory-ci-rate-limit-deferral-review.md`

## Evidence
Pre-fix failure is reproduced on two exact-main runs:
- `34805979340` / job `103857836065`;
- `34807042279` / job `103860850516`.

Both passed compile/self-test validation and failed live PR listing with installation rate-limit 403.

Producer exact-head validation:
- run `34806810445`
- job `103860174519`
- validation head `407b2c48d5035dcf9f66fc5f945053384a5272a7`
- py_compile v1-v5: PASS
- v1-v5 self-tests: PASS
- temporary validation workflow absent from final producer diff.

## Required next route
Create one separately owned authorized integration episode bound to exact producer PR #1095/head `9e21f1dbb6cdb29f8b796595b4985932075dd0f6` and this review terminal.

That integration must:
1. freshly re-derive current main/canonical binding and reject overlapping maintenance drift;
2. require exact producer terminal/head/files and clean review identity;
3. mark #1095 ready only as the mechanical merge prerequisite;
4. squash merge only with the exact expected producer head;
5. verify the returned squash is current main;
6. inspect the exact new-main push-triggered `Everfield planning frontier maintenance` run;
7. accept only if the run succeeds with either:
   - `reconciliation_complete: true`; or
   - an explicit typed rate-limit deferral containing `deferred: true`, `deferred_reason: GITHUB_API_RATE_LIMIT`, `reconciliation_complete: false`, and `authority_created: false`.
8. reject any generic 403/unrelated failure.

The review provenance PR may remain unmerged after its result is consumed; it exists as the required exact-head review surface.
