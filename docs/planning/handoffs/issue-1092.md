# Issue #1092 handoff — factory CI rate-limit recovery

## Status
Producer complete and ready for fresh required review. NOT_CANONICAL and not authorized for integration by this handoff.

## Frozen basis
- Issue: #1092 / `FACTORY-CI-REC-01`
- winning ownership comment: `5659081470`
- branch: `planning/issue-1092`
- base/current main at producer freeze: `1abb5fe9638b00c90180fdbae4d770e64fcbcc9c`
- substantive work SHA: `7e846263fb0f37be3f43069d17d95c8a93cf8db1`
- post-validation cleanup head before this handoff: `97c905530ec085ada852c3e27ae57b8a73ebc558`
- failing main workflow run: `34805979340`
- failing job: `103857836065`

## Demonstrated defect
The current-main maintenance workflow passed compile/self-test validation, then failed live reconciliation on the first PR-list request because the installation token had exhausted the GitHub API core limit:

`HTTP 403: API rate limit exceeded for installation`

That is a transient capacity condition rather than a planning-authority, permission, syntax, or self-test failure, but the prior implementation classified every HTTP error as a fatal `RuntimeError`.

## Bounded repair
Changed only:
- `tools/planning/frontier_maintenance.py`
- `tools/planning/frontier_maintenance_v5.py`

The shared wrapper now:
- exposes `GitHubRateLimitExceeded`;
- classifies only HTTP 403/429 responses whose GitHub message contains an explicit rate-limit marker;
- preserves generic HTTP 403 responses as fatal `RuntimeError`;
- adds deterministic positive/negative classification self-tests.

The v5 live entry point now catches only `GitHubRateLimitExceeded`, emits a GitHub Actions warning plus structured JSON with:
- `deferred: true`
- `deferred_reason: GITHUB_API_RATE_LIMIT`
- `reconciliation_complete: false`
- `authority_created: false`

and exits 0 so transient installation-rate exhaustion does not make the repository build red. All unrelated API failures still propagate and fail the job.

If rate exhaustion occurs after idempotent maintenance mutations have started, the run may be partially progressed but never claims reconciliation completion; a later event/scheduled run resumes from repository/GitHub state.

## Exact validation
Temporary branch-only validation workflow was added, executed, and removed before producer freeze.

Validation run: `34806810445`  
Job: `103860174519`  
Validated head: `407b2c48d5035dcf9f66fc5f945053384a5272a7`

Results:
- `python3 -m py_compile` for frontier maintenance v1-v5: PASS
- v1 self-test: PASS
- v2 self-test: PASS
- v3 self-test: PASS
- v4 self-test: PASS
- v5 self-test: PASS

After validation, temporary `.github/workflows/issue-1092-validation.yml` was removed. Final producer diff before handoff contains only the two maintenance Python paths above.

## Self-review
0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

Key checks:
- generic permission-denied 403 remains fatal;
- only typed rate-limit exhaustion is deferred;
- no route, terminal, ownership, review, verification, integration, exact-main, or canonicalization predicate was weakened;
- deferred output explicitly says reconciliation is incomplete and no authority was created;
- route registry remains empty on current main;
- no gameplay, engine-selection, implementation-readiness, release, decision, verification-PASS, or canonical authority is created.

## Required next route
Fresh degraded-independent required review of the exact final producer head/diff. Review must attack:
1. false-positive classification of permission/auth failures as rate limits;
2. false-negative handling of the demonstrated installation rate-limit payload;
3. whether success-on-deferral could be mistaken for reconciliation completion or authority;
4. partial-run/idempotence safety;
5. unchanged generic failure behavior;
6. exact two-code-path scope and validation provenance.

Only a clean review may route a separate squash-only integration episode. Integration must require post-publication inspection of the exact new-main `Everfield planning frontier maintenance` run.
