# Planning Program v1 — Final Bootstrap Candidate

**State:** REVIEWED-CANDIDATE-FINAL-BOOTSTRAP  
**Bootstrap remediation issue:** #14  
**Authority:** NON-CANONICAL until Bootstrap Issue #5 records a valid PASS for this exact work state and Bootstrap Issue #6 performs the verified squash-only promotion and activation sequence.  
**Scope:** Pre-implementation planning only. This document does not authorize gameplay implementation, a final engine choice, or a mass implementation backlog.

## 1. Status

This candidate supersedes the Issue #11 remediation **for verification**, not for provenance. It closes:

- `V5-B03` — activation tied to current HEAD;
- `V5-B04` — root phase remained `PLAN-THE-PLAN` after canonicalization;
- `V5-B05` — no deterministic legacy-bootstrap → mature-status bridge;
- `V5-B06` — status typing/ownership/provenance remained incomplete;
- `V5-B07` — mandatory review/verification could deadlock in the recorded single-agent environment.

Exact dispositions are in `docs/planning/reviews/issue-5-reverification-finding-dispositions.md`.

The normative machine contract is `docs/planning/10-planning-program-v1-canonicalization-manifest.yaml`. A prose/manifest contradiction is a verification failure, not permission to improvise.

## 2. Phase and authority model

The project moves through:

1. **BOOTSTRAP / PLAN-THE-PLAN** — before Issue #6 terminal canonical activation.
2. **PLANNING** — canonical Planning Program v1 is active; bounded factory, technical, evaluation, and game-design planning may execute.
3. **IMPLEMENTATION-READY** — a later independently/degraded-independently verified transition may authorize high-throughput implementation.

Issue #6 promotion MUST deterministically update `AGENTS.md`, `START-HERE.md`, and this program so all authoritative entry surfaces report **PLANNING**. Gameplay/high-throughput implementation remains blocked.

## 3. Immutable inputs

- Issue #11 remediation work SHA `7ed2d734645adf93910ce60156ec8b45d528fa73`;
- Issue #11 candidate blob `5e60d827ab99fe04e8a23c4addfc59d6f418d281`;
- Issue #11 manifest blob `9ecad20d9332eb1b649dfcb16beece5cda3fa330`;
- Issue #5 second FAIL work SHA `44b93171fcd0734bf8181f75120e52d4c7873ab6`;
- reviewed Wave 1 contract source blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- Issue #14 base `main@fce7218a1e7a4b03bae04aead80f12f5039848fb`;
- repository-visible single-agent resource constraint on Issue #5 comment `5244416013`.

Repository + GitHub state outrank chat history.

## 4. Durable canonical binding

Every canonical Planning Program version has a header:

`**Canonicalized by:** <canonicalization issue>`

A fresh agent resolves the **active canonical binding**:

1. Read current `docs/planning/PLANNING-PROGRAM-v1.md`.
2. Parse its `Canonicalized by` issue reference.
3. Determine the current canonical-program Git blob SHA.
4. Fetch that issue's operational comments.
5. Select the highest-comment-ID valid terminal `INTEGRATION_STATUS` for which:
   - `canonicality == CANONICAL_PLANNING_PROGRAM`;
   - `canonical_program_blob_sha` equals the current program blob;
   - status `main_sha` is an ancestor of or equal to current `main`;
   - verification reference, squash PR/head, and base compatibility are valid.

Outcomes:

- **Exactly one selected matching binding:** that program version is active even after later unrelated squash merges move `main` forward.
- **No matching binding and the named canonicalization issue has never published any valid canonical binding:** bounded post-merge/pre-terminal activation window; only that canonicalization issue's verified post-merge steps may run.
- **No matching binding but the named issue has a prior valid canonical binding for a different program blob:** `CANONICAL_BINDING_MISMATCH`; fail closed and route to canonical recovery/reverification. Do **not** repeat the old post-merge activation sequence and do not run normal `[PLAN-v1]` work.

Current-HEAD equality is never the long-lived activation predicate.

A future canonical program revision changes the header to its own canonicalization issue and publishes a new binding.

## 5. Canonical cold-start entry

When this file is `CANONICAL` and Section 4 resolves an active binding:

1. read `/AGENTS.md`;
2. read canonical `docs/planning/START-HERE.md`;
3. read current canonical Planning Program v1;
4. resolve the active binding;
5. query open `[PLAN-v1]` issues;
6. validate issue contracts and schema-3 operational comments;
7. derive prerequisites, ownership, lease, recovery, terminal state, and conflicts;
8. queue class order: recoverable/handoff → review/revision/verification/integration → new proposal/research;
9. within class: lower `priority_rank`, then lower issue number;
10. re-read selected issue immediately before ownership acquisition;
11. load only the bounded authoritative packet;
12. apply mutation fencing before every branch write;
13. commit useful state and leave structured handoff/status before stopping.

If there is a bounded activation window or binding mismatch, normal Wave 1 selection is inactive.

## 6. Core constraints

1. `main` is stable canonical base.
2. Normal task branches are `planning/issue-N`.
3. One task has at most one current valid ownership generation.
4. Writes are expected-parent/fast-forward; force-push forbidden.
5. Non-main upstream work is consumed at immutable SHA.
6. `BLOCKED`, `READY`, `ORPHANED_BRANCH`, `STALE_OWNER`, and `IN_PROGRESS` are derived.
7. Authority comments are schema-versioned, append-only, typed, and fail closed.
8. Lease age uses GitHub server time.
9. Canonicality is explicit, never inferred from merge/path/PR/closure.
10. Every `main` integration is squash-only.
11. Wave 1 issue creation happens only after Issue #6 squash SHA exists.
12. High-throughput implementation stays blocked until a later verified readiness transition.

## 7. State model

Derived:

- `BLOCKED` — hard prerequisite unsatisfied.
- `READY` — prerequisites satisfied, no terminal result, no active owner.
- `ORPHANED_BRANCH` — deterministic branch exists, no owner, mature orphan probe.
- `STALE_OWNER` — ownership/renewal lease expired with no later valid handoff/completion.
- `IN_PROGRESS` — valid current owner with unexpired lease.

Recorded result states: `HANDOFF_READY`, `REVIEW_READY`, `VERIFICATION_READY`, `DONE`, `SUPERSEDED`, `INVALIDATED`.

Review disposition and verification result are separate typed fields.

## 8. Schema-3 operational protocol

The manifest declares every field type/nullability, every registered kind, exact required/conditional fields, predecessor rules, tie rules, owner requirements, immutable work/head bindings, and downstream effects.

Normal kinds:

1. `CLAIM`
2. `ORPHAN_PROBE`
3. `RESUME_INTENT`
4. `RESUME`
5. `RECOVER`
6. `PROGRESS`
7. `STATUS`
8. `REVIEW_STATUS`
9. `VERIFICATION_STATUS`
10. `INTEGRATION_STATUS`

One-time bootstrap bridge kinds:

11. `BOOTSTRAP_RESUME`
12. `BOOTSTRAP_VERIFICATION_STATUS`

Bridge kinds are valid only for Bootstrap Issue #5 under the exact manifest overlay. They are not general workflow escapes.

Unknown kind/field, wrong type, illegal null, edited comment, wrong issue/mission/branch, stale owner, losing contention record, invalid SHA/reference, or illegal predecessor has zero authority effect.

## 9. Ownership and fencing

`CLAIM`, `BOOTSTRAP_RESUME`, `RESUME`, and `RECOVER` create ownership generations. `PROGRESS` renews an existing generation only.

Before every branch mutation:

1. re-fetch valid operational comments;
2. prove current unexpired ownership generation;
3. fetch remote head;
4. require remote head == proposed parent;
5. create commit with that parent;
6. update ref with `force=false`;
7. abort on mismatch/non-fast-forward.

Owner-authored terminal/result comments also require the current unexpired owner and exact current branch head. A stale/recovered actor cannot publish a valid terminal result using an old generation ID.

## 10. New claim and recovery

- New READY work: create deterministic branch from current main → winning `CLAIM`.
- Orphan branch: `ORPHAN_PROBE` → ten-minute server-time maturity → competing `RESUME_INTENT(ORPHAN)` → winning `RECOVER`.
- Intentional handoff: `STATUS(HANDOFF_READY)` → competing `RESUME_INTENT(HANDOFF)` → winning `RESUME`.
- Stale owner: lease expiry → competing `RESUME_INTENT(STALE)` → winning `RECOVER` if source/head still hold.

Lowest valid GitHub comment ID wins contention for one exact source/head. Only the first valid grant from the winning intent is valid.

## 11. Completion records

- Root/domain synthesis → owner `STATUS(REVIEW_READY)` with exact work/head.
- Final synthesis → owner `STATUS(VERIFICATION_READY)`.
- Review → owner `REVIEW_STATUS` with own work/head, reviewed input SHAs, disposition, findings, independence profile.
- Normal verification → owner `VERIFICATION_STATUS` with own work/head, exact candidate/manifest/base tuple, simulation artifact, independence profile.
- Bootstrap Issue #5 → `BOOTSTRAP_RESUME` creates a real schema-3 owner from its exact legacy HANDOFF predecessor; that owner writes verification artifacts and then publishes `BOOTSTRAP_VERIFICATION_STATUS`.
- Integration → owner `INTEGRATION_STATUS` after squash, bound to verification record, own work/head, PR/head/base/main SHA, compatibility evidence, canonical artifacts, and canonicality result.

## 12. External retirement

`STATUS.authority_mode` is:

- `OWNER` — current owner required; `ownership_generation_comment_id` and `head_sha` non-null.
- `EXTERNAL` — only `SUPERSEDED|INVALIDATED`; ownership ID is null; typed external authorization required; `head_sha` may be null only if branch does not exist.

Thus never-claimed stale work can be retired without fabricated ownership.

## 13. Bootstrap bridge

### Issue #5

The existing `planning/issue-5` branch predates schema 3. The manifest overlays mission ID `BOOTSTRAP-VERIFY-05` and defines an exact legacy `STATUS(HANDOFF_READY)` predecessor shape.

Valid verifier acquisition is a competing schema-3 `BOOTSTRAP_RESUME` against that exact predecessor/head. Lowest valid comment ID wins and creates a normal fenced ownership generation. All subsequent Issue #5 report/simulation/handoff writes use the mutation fence.

Final `BOOTSTRAP_VERIFICATION_STATUS` requires current bridge owner, exact report work/head, exact candidate/manifest/Wave1/base tuple, zero BLOCKER/MAJOR for PASS, and a valid independence profile.

### Issue #6

Issue #6 has no existing branch. The manifest overlays mission ID `BOOTSTRAP-CANON-06`. A valid Issue #5 bridge PASS plus exact current-main equality with the PASS base makes Issue #6 READY; it enters schema 3 through normal `CLAIM` and remains schema-3-owned through terminal integration.

Issue #6 `INTEGRATION_STATUS` may reference the bootstrap verification kind. No other issue receives bootstrap bridge privileges.

## 14. Independence modes

### FULL_INDEPENDENT_CONTEXT

Requires a distinct execution context without producer private context, exact cold-start input manifest, producer-role exclusions, candidate-edit prohibition, and independent evidence acquisition.

### DEGRADED_SINGLE_AGENT

The initial program records the repository-visible single-agent constraint at Issue #5 comment `5244416013`. While active, mandatory review/verification may use degraded mode only when:

1. a new role episode/actor-session is used;
2. candidate under judgment is immutable for that episode;
3. reviewer/verifier never edits the candidate it judges;
4. a cold-start input manifest fixes exact repository/GitHub inputs before judgment;
5. fresh adversarial/mechanical evidence is acquired before prior rationale is reconciled;
6. report labels trust as `DEGRADED`;
7. self-authored assertion alone cannot satisfy evidence checks;
8. defects route to a separate remediation issue/branch/episode;
9. resource-constraint comment ID is recorded;
10. `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE` is mandatory reopen condition.

This is a liveness fallback, not full independence. A later repository-visible owner/canonical governance decision enabling multiple or isolated agents disables degraded mode.

## 15. Review routing

- `PASS_FOR_SYNTHESIS` → declared synthesis may become eligible.
- `CHANGES_REQUIRED` → declared synthesis/revision may become eligible and must disposition findings.
- `INVALIDATED` → only declared recovery/replanning may become eligible.

Review completion without allowed disposition unlocks nothing.

## 16. Context and evidence budget

Always read: `/AGENTS.md`, canonical `START-HERE`, selected issue, canonical program, issue-declared authoritative packet. Other planning context is forbidden-by-default unless a declared trigger is met.

Root Review Index ≤4,000 UTF-8 chars. Simultaneously mandatory review/synthesis packet ≤100,000 UTF-8 chars; if known context window <200,000 chars, cap at 50%. Unknown window → 100,000 fallback. Silent truncation forbidden.

Artifacts distinguish observed evidence, inference, recommendation/decision, and assumption.

## 17. No-READY liveness

When no normal READY work exists:

1. active owner can unblock graph → live;
2. handoff/mature orphan/stale owner → recover;
3. eligible review/revision/verification/integration → execute;
4. otherwise classify cycle/orphan prerequisite/invalidated dependency/missing transition/corrupted status.

`W1-REC-01` is single-use recovery for case 4 and cannot waive review/verification/canonicalization/squash integration.

A **new** canonicalization issue named by the program header with no prior valid binding is an activation window, not normal liveness. A prior binding for a different current blob is `CANONICAL_BINDING_MISMATCH` and requires recovery/reverification.

## 18. First-wave graph

Reviewed Wave 1 contracts are adopted immutably from Issue #4 manifest blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`, only sections:

- `issue_compiler`;
- `universal_root_acceptance`;
- `wave_1`;
- `non_root_optional_retrieval`;
- `next_wave_candidate_schema`.

Old bootstrap verification/canonicalization clauses are not adopted.

Initial graph is exactly 23 missions: 12 roots, 3 domain reviews, 3 domain syntheses, cross review, final synthesis, verifier, canonicalizer, recovery.

Issue #6 creates/validates them after its squash SHA exists. They remain blocked until terminal canonical binding is published; then 12 roots become derived READY.

## 19. Verification and canonicalization

Issue #5 PASS binds exact:

- Issue #14 candidate work SHA;
- Issue #14 manifest identity;
- adopted Wave 1 blob;
- verified base main SHA;
- verification report work/head;
- simulation artifact blob;
- independence profile.

Issue #6 claim requires current main == PASS verified base. Before merge it rechecks expected PR head and typed base compatibility evidence. Any drift must be explicitly reverified; otherwise integration is invalid.

Issue #6 applies only manifest-enumerated program/entry transformations. Every main merge is squash-only.

Post-squash Issue #6:

1. obtains squash main SHA;
2. verifies promoted program and root entry transforms;
3. computes canonical program blob;
4. instantiates/validates exactly 23 Wave 1 issues with activation SHA;
5. posts mission-ID→issue mapping;
6. posts terminal schema-3 `INTEGRATION_STATUS(canonicality=CANONICAL_PLANNING_PROGRAM)`.

Only step 6 creates active canonical binding and activates normal Wave 1 selection.

## 20. Root entry transformation

Verified Issue #6 transformation:

- replace `AGENTS.md` title;
- replace `AGENTS.md` `## Status` section;
- replace `AGENTS.md` `## Current Phase` section with PLANNING rules;
- replace `AGENTS.md` `## Mandatory Cold-Start Entry Point` section;
- replace `START-HERE.md` entirely;
- promote this candidate to `PLANNING-PROGRAM-v1.md` using exact header substitutions and byte-identical remainder.

Every source interval/literal must match exactly once or canonicalization fails.

## 21. Backlog retirement / wave governor

Obsolete work is superseded/invalidated/closed with provenance; unselected candidates remain data.

Per later activation: maximum 24 new issues, maximum 12 initially READY. Compiler validates unique IDs, acyclic hard dependencies, ownership conflicts, review routes, output collisions, activation prerequisites.

## 22. Observability

Track cold-start/binding failures, invalid capsules by type/reason, duplicate claims/intents, orphan/stale recovery, mutation-fence aborts, stale terminal attempts, handoff reconstruction, context packet sizes, review findings/escapes, degraded-independence uses, liveness incidents, retirement/creation, base-drift invalidations, non-squash attempts.

No single metric is a quality oracle.

## 23. Reopen conditions

Reopen if:

- fresh agent cannot resolve exactly one active binding;
- later main movement re-enters completed bootstrap;
- current program blob disagrees with its prior binding;
- entry files disagree on phase;
- bootstrap bridge needs invented policy;
- any schema field lacks deterministic type/null semantics;
- stale writers can publish terminal results;
- degraded mode increases escaped defects or hides trust loss;
- multiple/isolated agents become available;
- context budget repeatedly induces shallow review;
- useful READY frontier collapses;
- wave governors starve work or fail to control WIP;
- later explicit human directive supersedes a binding constraint.

## 24. Bootstrap provenance

`#2 proposal → #3 review → #4 candidate → #5 FAIL → #11 remediation → #5 FAIL → #14 final remediation → #5 verification → #6 canonicalization`

Before active canonical binding, bootstrap issue state controls the queue. After active binding, Issues #2–#6, #11, and #14 are provenance only.

## 25. Downstream gate

Issue #14 completion unblocks only Issue #5 re-verification. Valid PASS unblocks Issue #6. Issue #6 terminal binding unblocks Wave 1.

Nothing here authorizes gameplay implementation.