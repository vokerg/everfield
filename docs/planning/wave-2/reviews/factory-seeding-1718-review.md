# Mandatory independent security review #1725 — successor terminal SHA authority

**Disposition: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR FSR-1725-M01, 0 correction-requiring MINOR.** This is a **bounded independent negative review of existing draft PR #1723**; it is neither clean acceptance nor integration/canonical authorization.

## Frozen identities and gates
- Task: Issue #1725, mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-20-REV-01`. First winning owner CLAIM #6132616875, actor `existing-pr-independent-semantic-sha-review-1725-gpt6-20261012-cph-01`, distinct from producer #1718 `frontier-semantic-sha-remediation-1718-gpt6-20261012-2211-cph-01` and prior #1716 reviewer. Claim immediately rechecked before own branch.
- Fresh base main `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`; active canonical #1147 binding `5675066392`, blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Source Issue #1718 first winning CLAIM #6131797314 at GitHub 2026-10-12T20:10:28Z, unedited owner STATUS(REVIEW_READY) #6131910505 at 20:18:05Z (within six-hour lease), OPEN/DRAFT PR #1723 exact HEAD `186bb42292d2cb43c6c623073e4929e576a90e50`, 27 authorized changed paths and unchanged main base.
- Exact corrected script blobs: base `tools/planning/frontier_maintenance.py` `f7dd6640210e27e18a170633ba8f8ab0d176835d`, v2 `b94e9e3544c79b158157f32b876212a0b1d43542`, v4 `1939d0be22389fa93575335e8ed622ecda2822c4`, v5 `510cd909192a1fd0dc5f355a701d429962b15671`. Other inherited code and handoffs reviewed for path-level envelope; no source edits.
- Source authored exact-head Actions run #38303093661 SUCCESS, full v1–v7 compile/self-test job #114990519060 SUCCESS, mutating maintain job #114990520354 SKIPPED. **Authored evidence is not independent clean review.**

## FSR-1725-M01 (MAJOR): a terminal-backed *successor* can consume an unverified GitHub result SHA

The correction authenticates both HEAD/work SHAs of the **factory transition wrapper's** own terminal in v4 `semantic_generation_from_comments` and v2 `schema_terminal_resolution_from_comments`. But the real `route_consumed: true` branch in frozen `tools/planning/frontier_maintenance_v4.py::semantic_generation_from_terminal` retrieves the **referenced successor's** terminal by `base.reconcilable_terminal(successor_number)`, then checks **only** `successor_terminal.comment_id == resolved_successor_terminal_comment_id`. The helper does **not** call `base.github_verified_terminal_result_heads(successor_number, successor_terminal.head_sha, successor_terminal.work_sha)`, and the caller's SHA check is applied to `transition_issue.number`, not the successor. The base `reconcilable_terminal_from_comments` checks syntactic SHA40/owner linkage, not live branch ancestry.

Reachable production chain:

```text
v5.v5_resolved_transition_generations(closed, recent)
  -> v4.semantic_generation_from_comments(wrapper, comments, issues_by_number)
       -> base.reconcilable_terminal_from_comments(wrapper) [syntax/owner]
       -> base.github_verified_terminal_result_heads(wrapper_id, wrapper_head, wrapper_work) [correct]
       -> v4.semantic_generation_from_terminal(wrapper, wrapper_terminal, ...)
            disposition = REQUIRED_ROUTE_ALREADY_CONSUMED_BY_TERMINAL_SUCCESSOR
            route_consumed = true
            -> base.reconcilable_terminal(successor_id) [syntax only]
            -> successor_terminal.comment_id == bound_comment_id [only]
            -> returns consumed source generation [incorrect for forged successor SHAs]
```

For a trusted closed wrapper with authenticated head/work and a trusted eligible existing successor #20, use wrapper terminal comment #4 for `source_issue: 10`, `source_terminal_comment_id: 2`, `source_required_route: NEXT`, `resolved_successor_issue: 20`, `resolved_successor_terminal_comment_id: 50`, `route_consumed: true`. Give successor #20 a valid-looking owner-linked terminal comment #50 but `head_sha = f * 40` and `work_sha = e * 40`, neither related to the live `planning/issue-20` branch. Base's parser can return that terminal, but it is **not GitHub-authenticated**. Current code consumes generation `(10, 2, NEXT)` and can suppress/misclassify required successor work. Merely checking wrapper result SHA does not authenticate a different issue's result.

### Independent executable negative witness (isolated exact source body)

I independently retrieved the **frozen exact GitHub v4 function body**, copied it verbatim into Python 3 with minimal stubs for imported dependencies, and executed the `route_consumed` branch using the fixture above. The `base.reconcilable_terminal` test stub returned successor terminal #50 with deliberately unrelated 40-hex head/work. A branch verifier mock was instrumented to reject them and count calls.

```text
consumed_generation= (10, 2, 'NEXT')
forged_successor_head= ffffffff forged_work= eeeeeeee
result_SHA_verification_calls= []
```

The negative is demonstrated by the actual extracted function's return value and zero calls to successor SHA validation, together with independently inspected on-disk caller and parser logic. No GitHub live endpoint mutation, PATCH or PR closure occurred.

**Precision limit:** This is an independently executed **verbatim isolated function with mocked dependencies**, not an import/run of the *entire* corrected source module or full v1–v7 regression suite. I do **not** claim full-module independent verification, all matrix cases, broader security completeness, or zero further vulnerabilities. Exact-source authored CI cannot supply that missing independent assurance. A concrete correction-requiring MAJOR already prohibits CLEAN.

## Bounded necessary correction and downstream authority
Require a single distinct bounded source remediation of PR #1723: when a semantic `route_consumed` claim depends on a successor terminal, authenticate **both successor terminal SHA fields against that successor's own live task branch**, fail closed on a deleted/moved/unknown/diverged ref or GitHub errors, and retain genuine independently authorized non-terminal dispatch-marker resolution. Test branch-exact, behind-free ancestor and separate forged HEAD/work/both, bad refs and compare, owner/lease/HANDOFF/STALE/ORPHAN, original FSR-1691/1703/1716 fixes and composed v1–v7 read-only. Newly scoped source must be separately reviewed.

This reviewer owns only the new report and `docs/planning/handoffs/issue-1725.md`, with reviewer-only OPEN/DRAFT PR **never merge**. No self-review/source changes, live apply/PATCH, PR retirement, integration, canon, gameplay-readiness, release or production authorization.
