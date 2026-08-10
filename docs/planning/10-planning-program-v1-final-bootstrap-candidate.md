# Planning Program v1 — Final Bootstrap Candidate

**State:** REVIEWED-CANDIDATE-FINAL-BOOTSTRAP  
**Bootstrap remediation issue:** #14  
**Authority:** NON-CANONICAL until Bootstrap Issue #5 records a valid PASS for this exact work state and Bootstrap Issue #6 performs the verified squash-only promotion and activation sequence.  
**Scope:** Pre-implementation planning only. This document does not authorize gameplay implementation, a final engine choice, or a mass implementation backlog.

## 1. Status

This candidate supersedes the Issue #11 remediation **for verification** while preserving Issue #11 as immutable provenance. It closes the five boundary defects found by the second Issue #5 cold-start pass:

- `V5-B03` — activation incorrectly tied to current HEAD;
- `V5-B04` — root `AGENTS.md` phase remained `PLAN-THE-PLAN` after canonicalization;
- `V5-B05` — no deterministic legacy-bootstrap → mature-status bridge;
- `V5-B06` — mature status typing/ownership/provenance was incomplete;
- `V5-B07` — mandatory review/verification could deadlock in the recorded single-agent environment.

Exact dispositions are in `docs/planning/reviews/issue-5-reverification-finding-dispositions.md`.

The normative machine-readable contract is `docs/planning/10-planning-program-v1-canonicalization-manifest.yaml`. When prose and manifest disagree, verification MUST fail rather than invent policy.

## 2. Authority and phase model

There are three distinct states:

1. **BOOTSTRAP / PLAN-THE-PLAN** — current state before Issue #6 canonical activation completes.
2. **PLANNING** — canonical Planning Program v1 is active and bounded planning missions may execute.
3. **IMPLEMENTATION-READY** — a later independently verified decision may authorize high-throughput implementation. Planning Program v1 does not make that decision.

Issue #6 promotion MUST deterministically update the root entry documents so `AGENTS.md`, `START-HERE.md`, and this program all report **PLANNING** after activation. No stale `PLAN-THE-PLAN` phase declaration may remain authoritative after Issue #6 terminal activation.

## 3. Immutable provenance inputs

This candidate consumes:

- Issue #11 remediation work SHA `7ed2d734645adf93910ce60156ec8b45d528fa73`;
- Issue #11 candidate blob `5e60d827ab99fe04e8a23c4addfc59d6f418d281`;
- Issue #11 manifest blob `9ecad20d9332eb1b649dfcb16beece5cda3fa330`;
- Issue #5 second FAIL report work SHA `44b93171fcd0734bf8181f75120e52d4c7873ab6`;
- reviewed Wave 1 contract source blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- remediation base `main@fce7218a1e7a4b03bae04aead80f12f5039848fb`;
- repository-visible single-agent resource constraint recorded on Bootstrap Issue #5 comment `5244416013`.

No prior conversation is project authority.

## 4. Canonical binding — durable across later main movement

A canonical Planning Program file contains a header field naming the issue that canonicalized that exact program version:

`**Canonicalized by:** <issue reference>`

A fresh agent resolves the **active canonical binding** as follows:

1. Read current `docs/planning/PLANNING-PROGRAM-v1.md` and parse its `Canonicalized by` issue reference.
2. Compute/read the current canonical-program Git blob SHA.
3. Fetch that canonicalization issue's operational comments.
4. Select its valid terminal `INTEGRATION_STATUS` whose:
   - `canonicality == CANONICAL_PLANNING_PROGRAM`;
   - `canonical_program_blob_sha` equals the current canonical-program blob;
   - `main_sha` is an ancestor of or equal to current `main`;
   - referenced verification and squash merge are valid.
5. If exactly one latest valid binding exists, bootstrap/canonicalization for that program version is complete even when current `main` has advanced through later unrelated squash merges.
6. If the canonical program header names a canonicalization issue but no valid matching binding exists, the repository is in that issue's bounded post-merge/pre-terminal activation window. Only that canonicalization issue's verified post-merge activation steps may proceed; normal liveness recovery and normal `[PLAN-v1]` work remain inactive.

Current-HEAD equality is **not** an activation predicate after canonicalization.

A future canonical program revision MUST update the `Canonicalized by` header and publish a new terminal `INTEGRATION_STATUS`; the new binding supersedes the old program version by identity rather than by guessed recency.

## 5. Canonical cold-start entry

When the file is `CANONICAL` and the active canonical binding in Section 4 resolves, a fresh planning agent MUST:

1. read `/AGENTS.md`;
2. read `docs/planning/START-HERE.md`;
3. read the current canonical program;
4. resolve the active canonical binding;
5. query open `[PLAN-v1]` issues;
6. validate issue contracts and schema-3 operational comments;
7. derive prerequisites, ownership, lease, recovery, terminal state, and conflicts;
8. prefer queue classes: recoverable/handoff → review/revision/verification/integration → new proposal/research;
9. within a class choose lower `priority_rank`, then lower issue number;
10. re-read the selected issue immediately before claim/resume/recovery;
11. load only its bounded context packet;
12. apply the mutation fence before every branch write;
13. leave committed handoff/status before stopping.

If the file is non-canonical, or its active binding does not resolve, normal Wave 1 selection is inactive.

## 6. Core constraints

1. `main` is the stable canonical base.
2. Normal task branches are deterministic: `planning/issue-N`.
3. One task has at most one valid ownership generation.
4. Branch writes are expected-parent/fast-forward only; force-push is forbidden.
5. Upstream non-main work is consumed by immutable SHA.
6. `BLOCKED`, `READY`, `ORPHANED_BRANCH`, and `STALE_OWNER` are derived states.
7. Operational authority is schema-versioned, append-only, and fail-closed.
8. Lease age uses GitHub server time, never a self-authored timestamp.
9. Canonicality is explicit and cannot be inferred from PR, merge, issue closure, or path alone.
10. Every integration into `main` is squash-only.
11. Wave 1 is created only after Issue #6's squash commit exists.
12. Gameplay/high-throughput implementation remains blocked until a later verified implementation-readiness decision.

## 7. State model

Derived states:

- `BLOCKED` — at least one hard prerequisite is unsatisfied.
- `READY` — prerequisites satisfied, no terminal result, no active valid owner.
- `ORPHANED_BRANCH` — deterministic branch exists, no valid ownership grant, mature orphan probe.
- `STALE_OWNER` — latest ownership/renewal lease expired without later valid completion/handoff/terminal result.
- `IN_PROGRESS` — current valid ownership generation with unexpired lease.

Recorded result states:

- `HANDOFF_READY`;
- `REVIEW_READY`;
- `VERIFICATION_READY`;
- `DONE`;
- `SUPERSEDED`;
- `INVALIDATED`.

Review disposition and verification result are typed fields, not overloaded state names.

## 8. Schema-3 operational protocol

The complete registry is `operational_capsules` in the manifest. Every field has a declared type and nullability. Unknown kinds, unknown authority fields, illegal nulls, malformed values, edited comments, invalid predecessors, stale-owner result publications, losing contention records, and invalid SHAs fail closed.

Normal operational kinds:

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

Bootstrap bridge kind:

11. `BOOTSTRAP_VERIFICATION_STATUS`

The bridge kind is valid only for Bootstrap Issue #5 under the exact bridge contract in the manifest. It does not become a general escape hatch.

## 9. Ownership and mutation fence

`CLAIM`, `RESUME`, and `RECOVER` create ownership generations. `PROGRESS` may renew but cannot create a generation.

Before **every** task-branch mutation:

1. re-fetch valid operational comments;
2. prove the actor holds the current unexpired ownership generation;
3. fetch remote task-branch head;
4. require it equals the exact proposed commit parent;
5. create the commit from that parent;
6. update the ref with `force=false` only;
7. abort on any mismatch/non-fast-forward.

Every owner-authored `STATUS`, `REVIEW_STATUS`, `VERIFICATION_STATUS`, and `INTEGRATION_STATUS` publication also requires the current unexpired owner generation and exact current branch head unless the manifest explicitly declares an external-authority path.

## 10. Claim/resume/recovery

### New work

Derived READY + absent deterministic branch → create branch from current main → `CLAIM` → re-fetch → only winning valid grant may edit.

### Orphan branch

Branch exists without owner → `ORPHAN_PROBE`; after ten GitHub-server minutes, valid `RESUME_INTENT(reason=ORPHAN)` contenders compete; lowest valid comment ID wins; winner may `RECOVER` if source/head still match.

### Intentional handoff

`STATUS(HANDOFF_READY)` → competing `RESUME_INTENT(reason=HANDOFF)` → lowest valid intent → one valid `RESUME`.

### Stale owner

Expired owner → competing `RESUME_INTENT(reason=STALE)` → lowest valid intent → one valid `RECOVER` if stale condition/head still hold.

## 11. Task/review/verification completion

- Root producer → owner-authored `STATUS(REVIEW_READY)` bound to exact `work_sha` and `head_sha`.
- Domain synthesis → `STATUS(REVIEW_READY)`.
- Final synthesis → `STATUS(VERIFICATION_READY)`.
- Review → current-owner `REVIEW_STATUS` bound to its own review `work_sha/head_sha` and exact reviewed input SHAs.
- Normal verification → current-owner `VERIFICATION_STATUS` bound to its own report `work_sha/head_sha`, candidate/manifest/base tuple, and independence profile.
- Bootstrap Issue #5 verification → bridge `BOOTSTRAP_VERIFICATION_STATUS` because its branch predates schema 3.
- Integration → current-owner `INTEGRATION_STATUS` after squash, bound to verification record, PR/head/base/main SHA, canonical artifacts, and canonicality result.

A stale or superseded writer cannot publish a valid terminal result merely by naming an old ownership comment.

## 12. External retirement/invalidation

`STATUS` has explicit `authority_mode`:

- `OWNER` — requires current unexpired owner generation and exact branch head.
- `EXTERNAL` — ownership generation MUST be null and a typed `external_authorization_comment_id` MUST reference a valid review/integration result that authorizes `SUPERSEDED` or `INVALIDATED`.

This permits deterministic retirement of never-claimed stale work without fabricating ownership.

## 13. Bootstrap bridge

### 13.1 Issue #5 legacy verification branch

Existing `planning/issue-5` predates schema 3. It MUST NOT be forced through an impossible synthetic schema-3 ownership history.

The manifest assigns:

- bridge mission ID `BOOTSTRAP-VERIFY-05`;
- exact branch `planning/issue-5`;
- accepted legacy source status comment(s);
- exact `BOOTSTRAP_VERIFICATION_STATUS` fields and validation rules.

A bridge PASS is valid only when:

- exact candidate/manifest/adopted-Wave1/base tuple is bound;
- report `work_sha/head_sha` exist on `planning/issue-5`;
- BLOCKER and MAJOR counts are zero;
- the selected independence mode is valid;
- the source legacy handoff/status is the declared bridge predecessor;
- no later FAIL/blocking status supersedes the verified episode.

### 13.2 Issue #6 schema-3 canonicalizer

Issue #6 has not been claimed. The manifest overlays a bootstrap contract:

- mission ID `BOOTSTRAP-CANON-06`;
- branch `planning/issue-6`;
- schema-3 `CLAIM` from current verified base when Issue #5 bridge PASS is valid;
- schema-3 ownership thereafter;
- terminal `INTEGRATION_STATUS` may reference `BOOTSTRAP_VERIFICATION_STATUS` rather than normal `VERIFICATION_STATUS`.

No other bootstrap issue receives this bridge authority.

## 14. Independence modes

### 14.1 Full independent mode

Use when a distinct execution context without producer private context is available. It requires machine-visible context/run provenance when exposed, producer-role exclusions, and independent evidence acquisition.

### 14.2 Degraded single-agent mode

The initial canonical program records a repository-visible resource constraint: the project currently has one available agent (Bootstrap Issue #5 comment `5244416013`). While that constraint is active, required review/verification may use `DEGRADED_SINGLE_AGENT` only if all of the following hold:

1. a new role episode/`actor_session_id` is used;
2. the candidate under test is immutable during the verification episode;
3. the verifier/reviewer does not edit the candidate it is judging;
4. a cold-start input manifest lists exact repository/GitHub inputs before judgment;
5. fresh adversarial/mechanical evidence is recorded before reconciling prior rationale/findings;
6. result artifacts explicitly say independence is degraded;
7. self-authored assertion alone cannot satisfy evidence checks;
8. any defect routes to a separate remediation issue/branch/episode;
9. the result records the resource-constraint comment ID;
10. `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE` is a mandatory reopen condition.

This mode is a liveness fallback, **not** full independence. Factory/trust planning must prioritize stronger isolation. A later repository-visible owner directive or canonical governance decision that provides multiple/isolated agents disables this degraded mode.

## 15. Review disposition routing

- `PASS_FOR_SYNTHESIS` → declared synthesis may become eligible.
- `CHANGES_REQUIRED` → declared synthesis/revision may become eligible and must disposition findings.
- `INVALIDATED` → only declared recovery/replanning may become eligible.

Review completion alone never unlocks downstream work without an allowed disposition.

## 16. Context and evidence budget

Always read:

- `/AGENTS.md`;
- canonical `START-HERE.md`;
- selected issue;
- canonical program;
- issue-declared authoritative packet.

Everything else is forbidden-by-default unless a declared retrieval trigger is satisfied.

Every root proposal has a Review Index ≤4,000 UTF-8 characters. Simultaneously mandatory review/synthesis context is capped at 100,000 UTF-8 characters; if a known execution context is smaller than 200,000 characters, cap at 50% of that window. Unknown window → deterministic 100,000 fallback. Silent truncation is forbidden.

Evidence, inference, recommendation/decision, and assumption are explicitly separated.

## 17. No-READY liveness

When no normal READY task exists:

1. active owner can unblock graph → graph live;
2. handoff/mature orphan/stale owner → recover;
3. eligible review/revision/verification/integration → execute;
4. otherwise classify cycle, orphan prerequisite, invalidated dependency, missing transition, or corrupted status.

`W1-REC-01` is a single-use recovery task for case 4 and cannot waive review/verification/canonicalization/squash integration.

A canonical program with no active binding is a bounded canonicalization activation window, not a normal liveness defect.

## 18. First-wave mission graph

Wave 1 contracts are immutably adopted from Issue #4 manifest blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`, limited to:

- `issue_compiler`;
- `universal_root_acceptance`;
- `wave_1`;
- `non_root_optional_retrieval`;
- `next_wave_candidate_schema`.

Issue #4 bootstrap verification/canonicalization clauses are not adopted.

Initial graph: 23 missions — 12 roots, 3 domain reviews, 3 domain syntheses, cross review, final synthesis, verifier, canonicalizer, and one recovery task.

Issue #6 creates them **after** its squash commit using that concrete activation SHA. They remain operationally blocked until Issue #6 terminal integration binding is published. Then the 12 roots become derived READY.

## 19. Canonicalization

Issue #5 PASS binds:

- exact Issue #14 candidate work SHA;
- exact Issue #14 manifest identity;
- adopted Wave 1 source blob;
- verified base main SHA;
- simulated generated issue graph;
- verification report work/head SHA;
- explicit independence mode/provenance.

Issue #6 may only apply transformations enumerated in the verified manifest. Immediately before merge it rechecks expected head and verified base/current-main compatibility. Base drift requires an explicit typed compatibility/reverification evidence record.

Every main integration is squash-only.

After squash, Issue #6:

1. obtains squash `main_sha`;
2. verifies promoted program + entry transformations at that SHA;
3. records canonical program blob identity;
4. instantiates/validates exactly 23 Wave 1 issues with the activation SHA;
5. posts mission-ID→issue mapping;
6. posts terminal schema-3 `INTEGRATION_STATUS` with `canonicality=CANONICAL_PLANNING_PROGRAM`.

Only step 6 activates normal Wave 1 selection.

## 20. Root entry transformation

Issue #6's verified manifest deterministically transforms root entry state by section boundaries:

- replace `AGENTS.md` `## Status` section;
- replace `AGENTS.md` `## Current Phase` section with `PLANNING` rules;
- replace `AGENTS.md` `## Mandatory Cold-Start Entry Point` section;
- replace `docs/planning/START-HERE.md` entirely with canonical entry text;
- promote this candidate to `docs/planning/PLANNING-PROGRAM-v1.md` with only verified header substitutions and otherwise byte-identical body.

Every section replacement MUST match exactly one source heading interval or canonicalization fails.

## 21. Backlog retirement and next-wave governor

Obsolete work is `SUPERSEDED`/`INVALIDATED` or closed with provenance. Unselected candidates remain data, not active issues.

Per later activation:

- max 24 newly instantiated issues;
- max 12 initially READY issues.

Compiler validates unique IDs, acyclic hard dependencies, ownership conflicts, review routes, output collisions, and activation prerequisites.

## 22. Observability

Track at minimum:

- cold-start success/failure;
- active canonical-binding resolution failures;
- invalid capsules by kind/reason/type;
- duplicate claims/intents/grants;
- orphan/stale recovery;
- mutation-fence aborts;
- stale terminal-publication attempts;
- handoff reconstruction;
- context packet size/splits;
- review findings/escape rate;
- degraded-independence uses;
- liveness incidents;
- retired/created work;
- base-drift invalidations;
- non-squash integration attempts.

No single metric is a quality oracle.

## 23. Risks and reopen conditions

Reopen this program when any of the following holds:

- a fresh agent cannot resolve exactly one active canonical binding;
- a later main merge incorrectly re-enters bootstrap activation;
- root entry files disagree on phase;
- bootstrap bridge requires invented policy;
- any schema field lacks deterministic type/null semantics;
- stale writers can publish terminal results;
- degraded independence hides or increases escaped defects;
- multiple agents or isolated execution contexts become available;
- context budgets repeatedly induce shallow review;
- useful READY frontier collapses;
- wave governors starve useful work or fail to control WIP;
- a later explicit human directive supersedes a binding constraint.

## 24. Bootstrap provenance invariant

The authority chain is provenance:

`#2 proposal → #3 review → #4 candidate → #5 FAIL → #11 remediation → #5 FAIL → #14 final bootstrap remediation → #5 verification → #6 canonicalization`

Before this file is canonical, open bootstrap issue state controls the queue. After this file is canonical **and** its active canonical binding resolves, bootstrap Issues #2–#6, #11, and #14 are provenance only.

## 25. Downstream gate

Completion of Issue #14 unblocks only Bootstrap Issue #5 re-verification. A valid PASS unblocks Issue #6. Issue #6 terminal activation unblocks the first bounded planning wave.

No transition in this chain authorizes gameplay implementation.