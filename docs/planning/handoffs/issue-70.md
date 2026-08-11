# Issue #70 handoff — W2-GH-01

## Mission state

- Mission: `W2-GH-01`
- Issue: #70
- Branch: `planning/issue-70`
- Ownership generation / claim comment: `5251309873`
- Base: `e4b7ee0a2699a57216146e99b990ab64edaae1d1`
- Evidence work SHA: `9b5bb4cb46aacb511d3ba46e782123090da9caa5`
- Primary artifact: `docs/planning/wave-2/evidence/github-cas-lock-experiment.md`
- Result for mature GitHub multi-ref lock/CAS adoption: `INCONCLUSIVE`
- Current authority: canonical schema-3 remains authoritative.

## Complete

- Re-derived canonical binding and Wave 2 frontier from repository/GitHub state.
- Left already-owned W2-AUTH-01 (#69) untouched and claimed exactly W2-GH-01 (#70).
- Refreshed current GitHub capability claims from official GitHub documentation.
- Executed actual-repository ref experiments for duplicate creation, non-force stale-writer fencing, recovery lineage, namespace scan reconciliation, unordered multi-ref circular wait surrogate, current ruleset/permission state, and post-squash ref persistence.
- Recorded observed vs inferred evidence, alternatives, recommendation, risks, reopen conditions, and downstream review route in the primary artifact.
- No production/gameplay implementation performed.
- No canonical ownership mechanism changed.
- No `main` integration or PR created; required downstream review is `W2-REV-01`.

## Retained experiment evidence

Experimental refs intentionally remain visible because the available execution connector does not expose ref deletion:

- `planning/issue-70-exp-lease` -> `d346a57d4281fad028f2a1de4264dbdd864c1a5c`
- `planning/issue-70-exp-lock-a` -> `e4b7ee0a2699a57216146e99b990ab64edaae1d1`
- `planning/issue-70-exp-lock-b` -> `e4b7ee0a2699a57216146e99b990ab64edaae1d1`

Additional immutable attempt commits:

- generation 0: `b9b1409eaa3c82ee7acf301cc3616fbac599d035`
- stale sibling: `04d5727e0e4d74c56dd6b61fa83122797794061d`
- recovery sibling/current experimental lease head: `d346a57d4281fad028f2a1de4264dbdd864c1a5c`

## Checks / evidence summary

- Duplicate exact ref create: rejected `422 Reference already exists`.
- Recovery advances ref, stale divergent sibling update with `force=false`: rejected `422 Update is not a fast forward`.
- Matching-ref scan reconstructs lease ref at recovery head.
- Naive unordered two-ref acquisition surrogate leaves each logical contender holding one ref and blocked on the other.
- Repository rulesets observed: `[]`.
- Connected actor permission: `admin`; ordinary-agent permission enforcement remains untested.
- Prior canonicalization task branch `planning/issue-43` remains after squash/main advance and diverges; cleanup is not implicit.

## Known limitations / remaining uncertainty

The following required surfaces did not receive empirical PASS and are why the mature-adoption result is `INCONCLUSIVE`:

- true concurrent races with isolated credentials;
- server-time lease expiry/renew/recovery timing;
- deliberate webhook/event loss/reordering;
- active ruleset enforcement and bypass behavior under non-admin credentials;
- executable GraphQL `createCommitOnBranch(expectedHeadOid)` comparison;
- actual ref delete/GC/recovery races.

The sequential/same-credential experiments must not be promoted into stronger distributed-correctness claims.

## Next recommended action

`W2-REV-01` should consume the exact evidence work SHA above after its declared prerequisites become review-ready. It should specifically attack concurrency overclaiming, admin/bypass assumptions, multi-ref ordering/rollback, event-loss versus pull-reconciliation semantics, and retained-ref GC safety.

No independent integration action is eligible from this mission. If any later reviewed artifact is integrated into `main`, the project-wide squash-only rule remains mandatory.