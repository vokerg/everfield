# FACTORY-CI-REC-REV-01 — Frontier maintenance rate-limit deferral review

## Disposition

**PASS_FOR_INTEGRATION_WITH_POST_PUBLICATION_WORKFLOW_ACCEPTANCE**

Trust mode: `DEGRADED_SINGLE_AGENT`.

Finding counts:
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- INFO: 2

This review judges only Issue #1092 / PR #1095 at exact producer head `9e21f1dbb6cdb29f8b796595b4985932075dd0f6`. It grants no integration, verification, planning, engine-selection, implementation-readiness, release, decision, or canonical authority.

## Frozen judged identity

- Producer issue: #1092 / `FACTORY-CI-REC-01`
- Producer claim: `5659081470`
- Producer terminal: `5659110488`
- Producer branch: `planning/issue-1092`
- Exact producer head: `9e21f1dbb6cdb29f8b796595b4985932075dd0f6`
- Substantive work SHA: `7e846263fb0f37be3f43069d17d95c8a93cf8db1`
- Draft PR: #1095
- Producer base: `1abb5fe9638b00c90180fdbae4d770e64fcbcc9c`
- Current review base/main: `13272159e2d4c9921aeb410a0a85cb470eaa23d7`
- Current-main drift from producer base is path-disjoint: only Issue #1089 content-review provenance files changed.
- PR #1095 remained open, draft, exact-head, and mergeable at review freeze.

Exact producer diff contains only:
1. `tools/planning/frontier_maintenance.py`
2. `tools/planning/frontier_maintenance_v5.py`
3. `docs/planning/handoffs/issue-1092.md`

## Failure reproduction basis

Two independent exact-main workflow episodes demonstrate the same pre-fix defect:
- run `34805979340`, job `103857836065`, main `1abb5fe9638b00c90180fdbae4d770e64fcbcc9c`;
- run `34807042279`, job `103860850516`, main `13272159e2d4c9921aeb410a0a85cb470eaa23d7`.

Both pass compile/self-test validation and then fail live reconciliation on the PR-list request with HTTP 403 and GitHub message `API rate limit exceeded for installation`.

## Adversarial review

### R1 — Classification narrowness: PASS

The new classifier requires both:
- HTTP status in `{403, 429}`; and
- an explicit rate-limit phrase in the GitHub response message: `api rate limit exceeded` or `secondary rate limit`.

A generic permission response such as `Resource not accessible by integration` remains a plain fatal `RuntimeError`. The producer regression test asserts that it is not `GitHubRateLimitExceeded`.

The classifier does not turn every 403 or every 429 into a successful deferral. This is the required fail-closed direction.

### R2 — Demonstrated failure coverage: PASS

The exact demonstrated message `API rate limit exceeded for installation` matches the explicit `api rate limit exceeded` marker after lower-casing. The producer self-test constructs that exact response shape and requires `GitHubRateLimitExceeded`.

### R3 — Exception boundary: PASS

The v5 entry point catches only `base.GitHubRateLimitExceeded`. It does not catch the parent `RuntimeError`, `Exception`, malformed response errors, unsafe route errors, permission failures, or unrelated logic errors. Those continue to escape `main()` and fail the workflow.

The shared `request()` function still raises on every HTTP error; the only semantic distinction is the typed subclass for explicit rate exhaustion.

### R4 — No false completion or authority: PASS

On a typed deferral, v5 emits:
- `deferred: true`
- `deferred_reason: GITHUB_API_RATE_LIMIT`
- `reconciliation_complete: false`
- `authority_created: false`

and an Actions warning. The normal completed path now explicitly emits `reconciliation_complete: true`.

No schema-3 status, terminal record, review result, verification result, integration record, or canonical binding is synthesized by the deferral path. Exit code 0 therefore means “build infrastructure deferred safely”, not “frontier reconciliation completed”.

### R5 — Partial-run / replay safety: PASS

The catch surrounds the whole live maintenance sequence, so exhaustion can occur before any mutation or after conservative mutations have begun. The pre-existing mutation surfaces are designed for repository/GitHub-state reconstruction and idempotent retry:
- terminal issue closure re-derives trusted owner-bound schema-3 terminal state;
- rejected draft PR retirement re-evaluates explicit rejection criteria;
- transition creation first searches/reuses exact source generations;
- redundant transition retirement re-derives exact-generation consumption;
- direct registered workflow dispatch checks exact-main fresh runs and generation-bound dispatch markers before retry.

A notable dispatch edge case is safe: if GitHub accepted an exact-main workflow dispatch but the subsequent marker write is rate-limited, the next run checks `matching_fresh_run()` / exact-main run outcome before attempting a duplicate dispatch. The patch does not weaken those controls.

Current `.github/planning-frontier-routes.json` is empty, so the active failing episode has no privileged dispatch path at all.

### R6 — Existing trust/authority gates: PASS

The producer diff does not alter:
- trusted author associations;
- immutable-comment checks;
- schema-3 parsing;
- owner linkage;
- terminal-state qualification;
- REVIEW_READY routing;
- rejected-PR matching;
- successor/generation binding;
- exact-main workflow registration rules;
- route allowlist loading;
- dispatch generation checks;
- squash-only integration policy.

The exception handling is operational availability behavior only.

### R7 — Validation provenance: PASS

Producer validation run `34806810445`, job `103860174519`, completed successfully at validation head `407b2c48d5035dcf9f66fc5f945053384a5272a7`.

Observed results:
- Python compilation for frontier maintenance v1-v5: PASS;
- v1 self-test: PASS;
- v2 self-test: PASS;
- v3 self-test: PASS;
- v4 self-test: PASS;
- v5 self-test: PASS.

The temporary validation workflow was subsequently removed. PR #1095's final changed-file list contains exactly the three frozen producer paths and no temporary workflow.

### R8 — Scope and current-main compatibility: PASS

No engine, gameplay, content, readiness, release, or canonical files are changed. Current main advanced only through two path-disjoint Issue #1089 review-provenance files, and PR #1095 remains mergeable. No overlapping maintenance implementation supersedes the candidate.

## INFO findings

### INFO-01 — Green deferral is intentionally not reconciliation success

Consumers of the Actions check must use the structured output/log warning when they need to distinguish `reconciliation_complete: true` from a safe rate-limit deferral. This is intentional and is materially safer than red CI for transient installation quota exhaustion, but integration acceptance must inspect the exact new-main run rather than merely seeing a green check.

### INFO-02 — Post-publication acceptance remains mandatory

Branch validation proves compilation and deterministic self-tests, not production GitHub-token behavior. After squash publication, the exact new-main `Everfield planning frontier maintenance` run must complete successfully and show one of:
- normal reconciliation with `reconciliation_complete: true`; or
- typed rate-limit deferral with `deferred: true`, `deferred_reason: GITHUB_API_RATE_LIMIT`, `reconciliation_complete: false`, and `authority_created: false`.

Any generic 403 or unrelated failure must still make that run fail.

## Integration boundary

This clean review authorizes only creation of a separately owned integration episode for exact producer PR #1095/head `9e21f1dbb6cdb29f8b796595b4985932075dd0f6`, subject to fresh current-main compatibility checks.

Integration must:
1. re-fetch current main, producer terminal, review terminal, PR head/files/mergeability, and canonical binding;
2. reject producer drift or overlapping main changes;
3. mark the producer PR ready only as a mechanical merge prerequisite;
4. squash merge only with the exact expected producer head;
5. verify the returned squash SHA becomes current main;
6. inspect the exact push-triggered maintenance run for that new main;
7. terminalize only after the post-publication acceptance condition above is satisfied.

No review-provenance PR needs to be merged to grant this bounded review result; repository/GitHub state must preserve the exact review terminal and draft provenance surface.
