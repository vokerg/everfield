# Planning Program v1 — Bootstrap Final Candidate

**State:** REVIEWED-CANDIDATE-BOOTSTRAP-FINAL  
**Bootstrap remediation issue:** #16  
**Authority:** NON-CANONICAL until Bootstrap Issue #5 records a valid PASS for this exact effective candidate/manifest state and Bootstrap Issue #6 performs the verified squash-only promotion and terminal activation.  
**Scope:** Pre-implementation planning only. No gameplay implementation, final engine selection, or mass implementation backlog is authorized.

## 1. Status

This candidate closes the single remaining Issue #5 blocker `V5-B08` while preserving all accepted Issue #14 corrections by immutable composition rather than restating them.

The effective Planning Program is:

1. **Normative base candidate:** `docs/planning/10-planning-program-v1-final-bootstrap-candidate.md` at Git blob `9829975eb3b8ac12b7dd8338a3569ff1a50cf309`.
2. **This overlay:** this entire file.
3. **Precedence:** this overlay overrides only the verification-lifecycle clauses explicitly named below. Every other base-candidate clause remains normative byte-for-byte.
4. **Machine contract:** `docs/planning/11-planning-program-v1-canonicalization-manifest.yaml`, composed over base manifest blob `1f062de59afcfe8496b4cff0fdff594c2d5fd50c`.

If either exact base blob is unavailable or mismatched, verification/canonicalization fails closed.

Issue #14 candidate/manifest are `SUPERSEDED_FOR_VERIFICATION`, not CANONICAL; they remain immutable provenance and the normative base of this exact composition.

## 2. Preserved base semantics

Unless overridden in Sections 3–8 below, the effective program inherits all Issue #14 behavior, including:

- BOOTSTRAP → PLANNING → later IMPLEMENTATION-READY phase separation;
- durable canonical binding using `Canonicalized by` issue + current canonical-program blob + activation-SHA ancestry;
- `CANONICAL_BINDING_MISMATCH` fail-closed recovery;
- deterministic AGENTS/START-HERE phase and entry transformation;
- schema-3 typed/closed operational comments;
- expected-parent branch mutation fencing;
- claim/orphan/handoff/stale recovery rules;
- owner/head/work fencing for task, review, verification, and integration results;
- typed external retirement for never-claimed work;
- legacy Issue #5 bootstrap bridge and Issue #6 schema-3 overlay;
- FULL and `DEGRADED_SINGLE_AGENT` independence profiles;
- review-disposition routing;
- context/evidence budgets and no-silent-truncation rule;
- bounded no-READY recovery;
- immutable adoption of the reviewed 23-mission Wave 1 graph from blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- squash-only integration;
- maximum 24 later-wave issues / 12 initially READY;
- high-throughput implementation barrier.

## 3. Verification bindings

A **verification tuple** is:

`(candidate_work_sha, manifest_identity, adopted_wave_1_contract_blob_sha, verified_base_main_sha)`.

A verification result is authoritative for Issue #6 only when:

- its candidate/manifest/adopted-Wave1 identities equal the exact effective candidate under review;
- its `verified_base_main_sha` equals current `main` at the moment Issue #6 is selected/claimed;
- it is the highest GitHub-comment-ID valid verification result for that exact candidate/manifest/adopted-Wave1/base tuple;
- result is `PASS` with zero BLOCKER and zero MAJOR findings.

An older PASS for another base is not authoritative but remains provenance.

## 4. `VERIFICATION_RESTART` — full verification after candidate change

`VERIFICATION_RESTART` is a schema-3 ownership-granting transition for a verification issue that already has a terminal verification result and now must verify a **changed candidate or manifest** after declared remediation/revision.

It is valid only when:

1. source comment is a valid terminal `VERIFICATION_STATUS` or `BOOTSTRAP_VERIFICATION_STATUS`;
2. a declared remediation/revision issue is closed/completed and produced the new candidate/manifest provenance;
3. `(new_candidate_work_sha, new_manifest_identity)` differs from the source tuple;
4. the new candidate/manifest exist on current `main` and are the exact selected verification payload;
5. `new_verified_base_main_sha == current main`;
6. `observed_head_sha` equals the current verification-task branch head;
7. contenders bind the same source/new tuple/head and lowest valid GitHub comment ID wins;
8. only the winner creates the new ownership generation.

This transition starts **full normal verification**. It does not carry forward prior PASS authority and does not permit a base-only shortcut.

The current Bootstrap Issue #5 re-entry after Issue #16 MUST use `VERIFICATION_RESTART` because the candidate/manifest change from Issue #14 to Issue #16.

## 5. `VERIFICATION_REFRESH` — unchanged candidate after base drift

`VERIFICATION_REFRESH` is a schema-3 ownership-granting transition used only when a valid PASS became stale solely because `main` advanced.

It is valid only when:

1. source is a valid terminal PASS (`VERIFICATION_STATUS` or `BOOTSTRAP_VERIFICATION_STATUS`);
2. source candidate/manifest/adopted-Wave1 identities are unchanged on current `main`;
3. `old_verified_base_main_sha` is a strict ancestor of `new_verified_base_main_sha`;
4. `new_verified_base_main_sha == current main`;
5. current selected candidate/manifest tuple exactly equals the source tuple;
6. `observed_head_sha` equals current verification-task branch head;
7. contenders bind the same source/new base/head and lowest valid GitHub comment ID wins;
8. only the winner creates the new ownership generation.

After acquisition, the verifier MUST run the full required cold-start/adversarial scenario set against the new base with a new independence profile episode and new immutable evidence artifacts. `VERIFICATION_REFRESH` is therefore a liveness transition, **not** a compatibility waiver or reduced test suite.

If candidate or manifest identity changed, `VERIFICATION_REFRESH` is invalid and `VERIFICATION_RESTART`/normal full verification is required.

## 6. Refreshed/restarted result publication

After either transition:

- the new ownership generation is subject to the ordinary mutation fence;
- verification report and simulation artifacts are written under that generation;
- final `VERIFICATION_STATUS` / `BOOTSTRAP_VERIFICATION_STATUS` must bind the new current branch head/work SHA, exact candidate tuple, current verified base, and a valid FULL or DEGRADED independence profile;
- old verification results remain immutable provenance;
- authoritative binding selection uses the highest valid result for the exact current tuple/base.

A FAIL routes to bounded remediation. A PASS may unlock canonicalization only while its base remains current.

## 7. Base movement state machine

For an exact candidate/manifest tuple:

```text
verification PASS at base A
        |
        | main unchanged
        v
Issue #6 may become READY

verification PASS at base A
        |
        | main advances to descendant B before Issue #6 claim
        v
PASS(A) becomes non-authoritative for selection
        |
        v
VERIFICATION_REFRESH(source=PASS(A), new_base=B)
        |
        v
full verification evidence under new owner
        |
        +--> PASS(B) -> Issue #6 may become READY while main==B
        |
        +--> FAIL(B) -> bounded remediation
```

If candidate/manifest changes at any point, use `VERIFICATION_RESTART`; a refresh is invalid.

## 8. Issue #6 selection override

The Issue #14 bootstrap overlay rule "current main equals Issue #5 verified base" is refined to:

1. select the highest-ID valid `BOOTSTRAP_VERIFICATION_STATUS` whose candidate/manifest/adopted-Wave1 tuple equals the current effective candidate and whose `verified_base_main_sha == current main`;
2. require that selected result is PASS with zero BLOCKER/MAJOR;
3. only then derive Issue #6 READY and allow normal schema-3 CLAIM.

If no current-base PASS exists:

- unchanged candidate + older PASS on ancestor base → verification refresh is the next recovery surface;
- changed candidate/manifest → full verification restart is the next surface;
- current-base FAIL → declared remediation is the next surface.

No human gate or invented compatibility policy is required.

## 9. Canonicalization

Issue #6 mechanically promotes **this** candidate wrapper to `docs/planning/PLANNING-PROGRAM-v1.md` using the overlay manifest's exact header replacements. The promoted canonical file continues to normatively compose the exact Issue #14 base candidate blob plus this overlay.

Root AGENTS/START-HERE transformations, canonical binding, post-merge Wave 1 instantiation, terminal `INTEGRATION_STATUS`, and squash-only rules are inherited unchanged from the exact Issue #14 base manifest unless the overlay manifest explicitly replaces them.

## 10. Verification requirement

Bootstrap Issue #5 must verify:

- this exact candidate work SHA;
- this overlay manifest identity;
- exact base candidate blob `9829975eb3b8ac12b7dd8338a3569ff1a50cf309`;
- exact base manifest blob `1f062de59afcfe8496b4cff0fdff594c2d5fd50c`;
- adopted Wave 1 blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- current main base;
- `VERIFICATION_RESTART` and `VERIFICATION_REFRESH` races, ownership fencing, evidence requirements, tuple selection, and stale-result behavior;
- all regression scenarios V5-B03 through V5-B07.

PASS remains prohibited with any unresolved BLOCKER/MAJOR.

## 11. Risks and reopen conditions

Retain every Issue #14 reopen condition and additionally reopen if:

- a stale-base PASS can still strand the graph;
- a candidate change can incorrectly use `VERIFICATION_REFRESH`;
- two refresh/restart contenders can both become owners;
- an older verification result can override a newer exact-current-base result;
- refresh evidence is materially weaker than normal verification;
- base movement repeatedly causes churn that warrants scheduler-level integration locks.

`MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE` remains a mandatory reopen condition for degraded independence.

## 12. Downstream gate

Completion of Issue #16 unblocks only Bootstrap Issue #5 full re-verification of this new effective candidate. A valid exact-current-base PASS may unblock Issue #6. Issue #6 terminal canonical binding then activates Wave 1.

Nothing here authorizes gameplay implementation.