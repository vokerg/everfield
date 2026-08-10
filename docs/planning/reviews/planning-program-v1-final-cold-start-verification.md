# Planning Program v1 — Final Cold-Start Verification Attempt

## Status

**Bootstrap issue:** #5  
**Mission ID:** `BOOTSTRAP-VERIFY-05`  
**Independence mode:** `DEGRADED_SINGLE_AGENT`  
**Trust:** DEGRADED  
**Result:** **FAIL**  
**Canonicalization eligibility:** BLOCKED  
**Candidate work source:** Bootstrap Issue #14  
**Candidate blob:** `9829975eb3b8ac12b7dd8338a3569ff1a50cf309`  
**Manifest blob:** `1f062de59afcfe8496b4cff0fdff594c2d5fd50c`  
**Adopted Wave 1 blob:** `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`  
**Verified base main:** `c822934c74cc5903b057e6d081f5e0a4c3e58226`  
**Cold-start input manifest blob:** `ecd42d1060f96babe13273d7f07cbbad8fb24232`  
**Simulation artifact blob:** `ab43108d047759902f363e70a77bfe3f3741a769`

This episode used the schema-3 bootstrap bridge. `BOOTSTRAP_RESUME` comment `5244621850` created the current fenced ownership generation from legacy predecessor comment `5244618992`. The candidate and manifest under judgment remained immutable on `main`; all verification writes were confined to `planning/issue-5`.

The project has a repository-visible one-agent constraint at Issue #5 comment `5244416013`. This verification is therefore explicitly **degraded**, not represented as full independent-agent isolation. The exact cold-start input set was frozen before the final scenario matrix, and prior failure rationale was procedurally gated until initial mechanical evidence was recorded.

## Result summary

The Issue #14 remediation successfully closes V5-B03 through V5-B07:

- canonical binding survives later unrelated `main` movement;
- changed canonical program blob with an old binding fails closed instead of replaying activation;
- root entry transforms converge on PLANNING;
- legacy Issue #5 has an executable schema-3 ownership bridge and Issue #6 has an explicit schema-3 overlay;
- status/result authority is typed and current-owner/head/work fenced;
- degraded single-agent verification is explicit, bounded, evidence-heavy, and reopenable.

The adopted Wave 1 graph compiles to the intended 23 missions with 12 normal roots, no duplicate mission IDs, and no hard-dependency cycle found in the reviewed graph.

One remaining BLOCKER was found.

## V5-B08 — BLOCKER — post-PASS base drift has no deterministic re-verification transition

**Affected surfaces:** final candidate §§13, 19; manifest `bootstrap_bridge.issue_6.eligibility`, `BOOTSTRAP_VERIFICATION_STATUS`, `transition_table`, required scenario `main_advances_after_PASS_before_issue_6_claim_or_merge`.

### Failure scenario

1. Issue #5 publishes a valid `BOOTSTRAP_VERIFICATION_STATUS(PASS)` for candidate/manifest/base `A`.
2. Before Issue #6 claims, another accepted squash merge advances `main` to descendant `B`.
3. Issue #6 correctly refuses to become READY because its bootstrap overlay requires current `main == verified_base_main_sha` (`B != A`).
4. The Issue #5 verification task is terminal PASS and its one-time `BOOTSTRAP_RESUME` acquisition has already been consumed.
5. The schema defines no transition that reopens or re-acquires verification authority to bind the unchanged candidate/manifest to `B`, nor a deterministic child verification task for that purpose.
6. Bootstrap is therefore fail-closed but stranded: progress requires policy invention or external intervention.

### Why it blocks PASS

The planning factory must be able to recover autonomously from ordinary main movement. A verifier correctly invalidating stale base evidence is not sufficient if no executable path exists to create current-base evidence. The candidate itself requires the scenario to be simulated, and it currently fails.

### Required correction

Add one typed verification-refresh mechanism that:

- applies only when candidate/manifest identity is unchanged;
- binds the previous verification record, previous base, new base, and covered main range;
- creates a fresh fenced verification episode or deterministic child verification issue;
- requires the same full/degraded independence and evidence standards as verification;
- publishes a new immutable current-base verification result;
- deterministically supersedes the older base binding for Issue #6 eligibility;
- forces full normal verification if candidate/manifest identity changed.

Bounded remediation is tracked in Issue #16 — `[PLAN-BOOTSTRAP] Close post-PASS base-drift re-verification gap`.

## Scenario disposition

The detailed machine-readable matrix is `docs/planning/reviews/issue-5-final-verification-simulation.yaml`.

All required scenarios PASS except `main_advances_after_PASS_before_issue_6_claim_or_merge`, which FAILs as V5-B08. The previous V5-B03 through V5-B07 findings are regression-tested as corrected.

## Final disposition

**FAIL.** Bootstrap Issue #6 remains blocked. The Issue #14 candidate/manifest remain NON-CANONICAL and will become `SUPERSEDED_FOR_VERIFICATION` once Issue #16 produces the bounded correction.

After Issue #16 completes, Issue #5 must re-enter through the exact refresh/verification path defined by the corrected manifest and verify the resulting payload against the then-current `main`.