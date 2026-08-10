# Planning Program v1 Proposal — Amendment 1

**State:** PROPOSED  
**Issue:** #2  
**Applies to:** `docs/planning/07-planning-program-v1-proposal.md` at or after commit `397882a0ececfba907d885e70c899469b1ba6c4f`  
**Authority:** This amendment is part of the Issue #2 proposal set and overrides the specific clauses below. It is not CANONICAL. Issue #3 must review the base proposal and this amendment together.

## 1. Why this amendment exists

A producer self-check found several execution ambiguities after the base proposal was committed. They are corrected here rather than hidden in chat history. Issue #4 should fold these corrections into a single reviewed candidate.

## 2. Operational state derivation overrides Section 9.3

`BLOCKED` and `READY` are **derived eligibility states**, not manual gates that require another agent to post a transition.

For every cold start, operational state is computed from:

1. the issue contract and hard prerequisites;
2. immutable prerequisite status/work SHAs;
3. the latest valid ownership/progress/handoff/terminal capsule;
4. branch existence and lease validity.

Rules:

- An issue created as `BLOCKED` becomes operationally `READY` automatically when all hard prerequisites are satisfied and it has no valid active owner or terminal status.
- A stale `BLOCKED` label or old status capsule must not keep a dependency-satisfied issue blocked.
- A `READY` label must not override an unsatisfied hard prerequisite.
- `IN_PROGRESS`, `HANDOFF_READY`, `REVIEW_READY`, `CHANGES_REQUESTED`, `VERIFICATION_READY`, `INTEGRATION_READY`, `DONE`, `SUPERSEDED`, and `INVALIDATED` are taken from the latest valid structured capsule and then checked against current prerequisites.
- Labels are views only until automation can enforce them.

This derived-state rule is what allows pre-instantiated review/synthesis issues to become eligible without a human or dedicated status-flipping agent.

## 3. Exact context-path rule for Section 11

Every basename-only planning input in the base proposal resolves under `docs/planning/`.

Issue #6 MUST expand every generated first-wave issue to full repository paths. For example, `00-project-charter.md` becomes `docs/planning/00-project-charter.md`.

For all first-wave missions:

- `/AGENTS.md`, canonical `docs/planning/START-HERE.md`, and the selected GitHub issue are always-read entry context;
- the issue's listed authoritative inputs are then read at the exact branch/SHA required by the issue;
- every other planning document is forbidden-by-default context unless an explicit optional retrieval trigger is met;
- upstream non-main artifacts are referenced by mission ID, path, and immutable `work_sha`, never only by a moving branch name.

After bootstrap canonicalization, the exact canonical Planning Program v1 path is:

`docs/planning/PLANNING-PROGRAM-v1.md`

Issue #6 must materialize the verified candidate there and update `docs/planning/START-HERE.md` to point to it. The Issue #2 proposal artifacts remain provenance and should be marked SUPERSEDED or clearly non-operational, not silently treated as the canonical entry document.

## 4. Universal root-mission acceptance criteria

Every root mission in Section 11.2 is `REVIEW_READY` only when all of the following are true:

- its exact output path exists on the deterministic task branch;
- it follows proposal/research schema 10.1;
- scope and non-goals are explicit;
- assumptions, observed evidence, inference, and recommendations are distinguishable;
- material alternatives are represented fairly;
- current external technical/legal/tool claims use authoritative sources or are explicitly deferred;
- empirical uncertainty is converted into bounded experiments/spikes rather than invented facts;
- interfaces, dependencies, and conflict surfaces are explicit;
- observability/evaluation and failure modes are explicit;
- open questions and reopen conditions are explicit;
- required critique mission(s) are named;
- no undefined current-wave mission is silently instantiated from discovered work;
- the task handoff/status records exact branch, substantive `work_sha`, and final branch `head_sha` through the two-part handoff/status protocol;
- a PR targeting `main` exists for diff visibility unless the issue contract explicitly documents why no PR is useful.

## 5. First-wave mission count and priority ranks

Issue #6 instantiates exactly **23 unique Wave 1 mission issues**, including `W1-REC-01` exactly once:

- 12 root proposal missions;
- 3 domain adversarial reviews;
- 3 domain synthesis missions;
- 1 cross-domain adversarial review;
- 1 final synthesis/dependency-map mission;
- 1 cold-start/coherence verification mission;
- 1 canonicalization/integration mission;
- 1 liveness recovery service mission.

Exact non-root `priority_rank` values are:

```text
W1-REC-01       5   (eligible only on the liveness condition)
W1-REV-FAC    210
W1-REV-TECH   220
W1-REV-GAME   230
W1-SYN-FAC    310
W1-SYN-TECH   320
W1-SYN-GAME   330
W1-REV-CROSS  410
W1-SYN-FINAL  510
W1-VERIFY-01  610
W1-CANON-01   710
```

Queue-class precedence from Section 9.1 still outranks the numeric rank: recoverable work first, then ready review/revision/verification/integration, then new proposal work. `priority_rank` resolves ordering within a class.

## 6. Downstream corrections for root missions

The base proposal accidentally mentioned future empirical missions as if they were direct current-wave downstream nodes. That is corrected as follows:

- `W1-TEC-01` directly unblocks only `W1-REV-TECH`, then `W1-SYN-TECH` through the declared review path. Engine spike missions are **next-wave candidates only** and may be instantiated only if `W1-SYN-FINAL` includes them and `W1-CANON-01` accepts them after verification.
- `W1-DES-02` directly unblocks only `W1-REV-GAME`, then `W1-SYN-GAME` through the declared review path. Balance-simulation missions are **next-wave candidates only** under the same final-synthesis/canonicalization rule.

No root mission may self-create those later missions.

## 7. Exact bootstrap-chain output paths

To remove ambiguity between the current bootstrap issues, use these paths unless a later reviewed candidate explicitly replaces them:

- Issue #2 proposal set:
  - `docs/planning/07-planning-program-v1-proposal.md`
  - `docs/planning/07-planning-program-v1-proposal-amendment-1.md`
- Issue #3 adversarial review:
  - `docs/planning/reviews/issue-2-adversarial-review.md`
- Issue #4 reviewed synthesis candidate:
  - `docs/planning/08-planning-program-v1-reviewed-candidate.md`
  - `docs/planning/reviews/issue-3-finding-dispositions.md`
- Issue #5 cold-start verification:
  - `docs/planning/reviews/planning-program-v1-cold-start-verification.md`
- Issue #6 canonical active program:
  - `docs/planning/PLANNING-PROGRAM-v1.md`
  - plus the required root entry-point updates and first-wave issue instantiation.

Issue #5 PASS must name the exact Issue #4 candidate `work_sha`. Issue #6 must verify that SHA before canonicalization.

## 8. Canonicalization mission output contract

`W1-CANON-01` has an explicit provenance/report output in addition to modifying canonical locations:

`docs/planning/wave-1/canonicalization-report.md`

Minimum report fields/sections:

```text
Status
Verified W1-SYN-FINAL work_sha
W1-VERIFY-01 PASS work_sha
Canonical artifacts promoted and destination paths
Deferred/non-canonical artifacts retained
Superseded artifacts/instructions
Next-wave issues instantiated (mission IDs + issue numbers)
Obsolete work retired/closed
Remaining implementation-readiness blockers
Integration PR number
Expected head SHA checked before merge
Squash merge result/main SHA
Reopen conditions
```

The report cannot claim the final `main` SHA from inside the pre-merge commit; after squash merge the integration agent must post the resulting `main` SHA to the canonicalization issue/PR status and, if a later provenance update is warranted, do so as separate reviewed work rather than bypassing the squash-only rule.

## 9. Recovery mission artifact schema

`W1-REC-01` uses `docs/planning/wave-1/recovery/liveness-recovery.md` with one dated/identified episode section per activation. Each episode contains:

```text
Episode/session ID
Trigger time
Observed graph snapshot
Why normal READY/recoverable work was absent
Failure classification: CYCLE | ORPHAN | INVALIDATED_DEPENDENCY | MISSING_TRANSITION | OTHER
Affected mission IDs and immutable SHAs
Smallest remediation proposed/applied
Work retired/split/reopened
Resulting eligible path(s)
Evidence/checks
Risks introduced
Reopen/escalation conditions
```

The recovery service may restore planning liveness but may not waive independent review, verification, canonicalization, or squash-only integration.

## 10. Review requirement created by this amendment

Issue #3 should treat this amendment itself as an attack surface, especially:

- whether derived `READY/BLOCKED` state is deterministic from repository + GitHub state;
- whether the 23-issue bounded graph is still too large or improperly coupled;
- whether the 6-hour lease and comment-ordered resume tie-break are safe enough for temporary planning;
- whether the canonical location and bootstrap paths remove ambiguity without creating parallel sources of authority;
- whether `W1-REC-01` can be reused without concurrent resume races or policy bypass;
- whether the canonicalization report and post-merge status preserve reconstructable squash provenance.
