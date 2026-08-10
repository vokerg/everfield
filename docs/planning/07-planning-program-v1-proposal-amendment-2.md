# Planning Program v1 Proposal — Amendment 2

**State:** PROPOSED  
**Issue:** #2  
**Applies to:** `docs/planning/07-planning-program-v1-proposal.md` together with `docs/planning/07-planning-program-v1-proposal-amendment-1.md`  
**Authority:** This amendment is part of the Issue #2 proposal set and overrides the specific clauses below. It is not CANONICAL. Bootstrap Issue #3 must review the complete proposal set independently.

## 1. Why this amendment exists

A second producer self-review found two execution gaps that were not explicit enough in the base proposal plus Amendment 1:

1. non-root review/synthesis/verification/canonicalization missions needed exact context packets rather than context inferable only from prerequisites; and
2. Wave 1 needed an explicit activation barrier preventing first-wave claims before bootstrap Issue #6 has actually squash-integrated the verified canonical program into `main`.

These are corrected below. This self-review is not a substitute for bootstrap Issue #3.

## 2. Exact context packets for non-root Wave 1 missions

For every non-root mission, the always-read entry context is:

- `/AGENTS.md` from the task branch/base required by the issue;
- canonical `docs/planning/START-HERE.md`;
- the selected GitHub issue in full;
- canonical `docs/planning/PLANNING-PROGRAM-v1.md` at the exact `main` SHA recorded by the issue's Wave 1 activation barrier.

Every upstream artifact below is read at the immutable `work_sha` recorded by its prerequisite status capsule. The corresponding prerequisite issue/status capsule is authoritative for proving that the SHA and operational state are valid.

Everything else in `docs/planning/` is forbidden-by-default unless an optional retrieval trigger below is met. Prior chat history is never authoritative input.

### W1-REV-FAC

**Authoritative inputs:**

- `W1-GOV-01` output at exact `work_sha`;
- `W1-FAC-01` output at exact `work_sha`;
- `W1-FAC-02` output at exact `work_sha`;
- `W1-FAC-03` output at exact `work_sha`;
- `W1-FAC-04` output at exact `work_sha`;
- each prerequisite issue/status capsule proving `REVIEW_READY`.

**Optional retrieval trigger:** load seed/mandate documents only to verify whether a reviewed proposal contradicts or silently drops project intent.

### W1-REV-TECH

**Authoritative inputs:**

- `W1-FAC-02` output at exact `work_sha`;
- `W1-FAC-03` output at exact `work_sha`;
- `W1-FAC-04` output at exact `work_sha`;
- `W1-TEC-01` output at exact `work_sha`;
- `W1-TEC-02` output at exact `work_sha`;
- `W1-EVAL-01` output at exact `work_sha`;
- each prerequisite issue/status capsule proving `REVIEW_READY`.

**Optional retrieval trigger:** retrieve primary technical sources or seed mandates only to test a concrete claim, omission, or contradiction in the reviewed artifacts.

### W1-REV-GAME

**Authoritative inputs:**

- `W1-TEC-02` output at exact `work_sha`;
- `W1-DES-01` output at exact `work_sha`;
- `W1-DES-02` output at exact `work_sha`;
- `W1-DES-03` output at exact `work_sha`;
- `W1-EXP-01` output at exact `work_sha`;
- `W1-EVAL-01` output at exact `work_sha`;
- each prerequisite issue/status capsule proving `REVIEW_READY`.

**Optional retrieval trigger:** load the charter/game/evaluation seed mandates only to test intent preservation, Stardew-reference boundaries, or evaluator requirements.

### W1-SYN-FAC

**Authoritative inputs:**

- the five producer artifacts reviewed by `W1-REV-FAC`, each at the exact SHA reviewed;
- `W1-REV-FAC` review artifact at exact `work_sha`;
- prerequisite status capsules proving the review is complete.

**Optional retrieval trigger:** retrieve seed mandates only when a review finding or producer disagreement cannot be dispositioned from the reviewed evidence itself.

### W1-SYN-TECH

**Authoritative inputs:**

- the six producer artifacts reviewed by `W1-REV-TECH`, each at the exact SHA reviewed;
- `W1-REV-TECH` review artifact at exact `work_sha`;
- prerequisite status capsules proving the review is complete.

**Optional retrieval trigger:** retrieve primary technical evidence when a BLOCKER/MAJOR disposition depends on validating an external technical claim.

### W1-SYN-GAME

**Authoritative inputs:**

- the six producer artifacts reviewed by `W1-REV-GAME`, each at the exact SHA reviewed;
- `W1-REV-GAME` review artifact at exact `work_sha`;
- prerequisite status capsules proving the review is complete.

**Optional retrieval trigger:** retrieve seed mandates only when needed to adjudicate intent preservation or an unresolved cross-artifact conflict.

### W1-REV-CROSS

**Authoritative inputs:**

- `W1-SYN-FAC` candidate at exact `work_sha`;
- `W1-SYN-TECH` candidate at exact `work_sha`;
- `W1-SYN-GAME` candidate at exact `work_sha`;
- prerequisite status capsules proving all three are `REVIEW_READY`.

**Optional retrieval trigger:** inspect a root proposal/review only when tracing the provenance of a concrete contradictory claim or finding disposition.

### W1-SYN-FINAL

**Authoritative inputs:**

- `W1-SYN-FAC` candidate at the exact SHA reviewed by `W1-REV-CROSS`;
- `W1-SYN-TECH` candidate at the exact SHA reviewed by `W1-REV-CROSS`;
- `W1-SYN-GAME` candidate at the exact SHA reviewed by `W1-REV-CROSS`;
- `W1-REV-CROSS` artifact at exact `work_sha`;
- prerequisite status capsules proving the cross-domain review is complete.

**Optional retrieval trigger:** inspect earlier proposals/reviews only to trace a disputed finding, evidence claim, or provenance chain.

### W1-VERIFY-01

**Authoritative inputs:**

- `W1-SYN-FINAL` canonicalization candidate at exact `work_sha`;
- `docs/planning/wave-1/synthesis/dependency-map.yaml` from that exact work state;
- the complete current `[PLAN-v1]` issue graph and latest valid structured status capsules needed to execute the required cold-start/liveness simulations;
- current `main` entry documents at the activation-barrier SHA.

**Optional retrieval trigger:** inspect earlier review/synthesis artifacts only when verifying provenance or investigating a contradiction.

### W1-CANON-01

**Authoritative inputs:**

- the exact `W1-SYN-FINAL` candidate SHA named by the verifier;
- the dependency map from the same candidate work state;
- `W1-VERIFY-01` PASS artifact at exact `work_sha`;
- current canonical entry documents on `main`;
- current first-wave issue/status state needed to retire or supersede work safely.

**Optional retrieval trigger:** inspect earlier provenance artifacts only to validate a promotion, supersession, or finding disposition.

### W1-REC-01

**Authoritative inputs:**

- canonical `docs/planning/PLANNING-PROGRAM-v1.md`;
- the complete open `[PLAN-v1]` issue graph relevant to the liveness defect;
- latest valid claim/progress/handoff/status capsules for affected missions;
- affected deterministic task branches and handoff files as required to diagnose liveness.

**Optional retrieval trigger:** inspect proposal/review/synthesis artifacts only when the liveness defect is caused by an invalidated dependency or contradictory planning decision.

## 3. Wave 1 activation barrier

The base proposal's statement that root missions become READY after Issue #6 canonicalizes the program is made operationally exact here.

Every Wave 1 issue instantiated by bootstrap Issue #6 MUST include the same hard activation prerequisite:

```yaml
wave_1_activation:
  bootstrap_issue: 6
  required_state: DONE
  required_integration_method: squash
  required_main_sha: <the squash commit produced by Issue #6 integration>
  required_canonical_program: docs/planning/PLANNING-PROGRAM-v1.md
```

Operational rules:

1. Issue #6 may create the 23 Wave 1 issues before its PR is merged only if every one is created operationally `BLOCKED` by this activation prerequisite.
2. No Wave 1 task may become `READY`, be claimed, or branch from `main` until the exact Issue #6 canonicalization PR has been squash-merged and the resulting `main` SHA is recorded on Issue #6.
3. The canonical program file must exist at that exact `main` SHA and Issue #6 must have a terminal `DONE`/canonicalization status capsule pointing to it.
4. Once those conditions hold, the activation prerequisite is satisfied automatically; each mission's remaining prerequisites determine its operational state.
5. If Issue #6 creates the issues only after merge, the same activation fields are still recorded for provenance and cold-start verification.

This prevents agents from claiming Wave 1 against a branch-only candidate or against a `main` state that does not yet contain the canonical dispatcher.

## 4. Provenance merge of the Issue #2 proposal

A squash merge of the Issue #2 proposal PR into `main` before Issue #3 review is permitted only as a **provenance integration**, not as canonicalization, when an explicit human directive authorizes that timing.

For such a provenance merge:

- all Issue #2 files retain `PROPOSED` authority;
- `/AGENTS.md` and `docs/planning/START-HERE.md` remain the active bootstrap dispatcher;
- Issue #3 remains mandatory and independently reviews the exact merged proposal set;
- Issues #4, #5, and #6 remain mandatory before Planning Program v1 can become CANONICAL;
- the provenance merge does not instantiate Wave 1 and does not authorize gameplay implementation;
- integration into `main` must still use squash merge.

This clause records integration timing only. It does not weaken the independent-review or canonicalization requirements.

## 5. Second self-review disposition

After applying Sections 2–4, the producer self-review found no remaining known BLOCKER or MAJOR defect against the Issue #2 required-output and cold-start acceptance criteria.

Known unresolved risks remain deliberately open for Issue #3 attack, including:

- comment-ordered resume serialization is not truly atomic;
- the 6-hour lease is a provisional policy choice;
- `session_id` independence is procedural rather than a strong identity boundary;
- the 23-issue first wave may still prove over-broad or incorrectly coupled;
- proposal provenance on `main` must not be mistaken for canonical authority.

The required next step after provenance integration remains bootstrap Issue #3 independent adversarial review.