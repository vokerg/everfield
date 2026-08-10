# Planning Program v1 — Canonical

**State:** CANONICAL  
**Canonicalized by:** Bootstrap Issue #6  
**Authority:** CANONICAL planning operating model for the current pre-implementation PLANNING phase.  
**Scope:** Pre-implementation planning only. No gameplay implementation, final engine choice, or mass implementation backlog is authorized.

## 1. Exact composition

This candidate is a narrow interpretation overlay over the exact Issue #16 payload:

- base candidate: `docs/planning/11-planning-program-v1-bootstrap-final-candidate.md` blob `d083e5bfa108360818898f9628e939f50b4f3940`;
- base manifest: `docs/planning/11-planning-program-v1-canonicalization-manifest.yaml` blob `bca34638a054d725239b936dd8232a7d274e814d`;
- adopted Wave 1 contract blob remains `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`;
- **every clause** of the exact Issue #16 candidate remains normative;
- this overlay changes only the authority/applicability of bootstrap-numbered clauses according to Section 2 and changes the canonical promotion source to this wrapper; on any other semantic conflict, the exact Issue #16 clause wins.

Issue #16 artifacts are `SUPERSEDED_FOR_VERIFICATION`, not CANONICAL. Missing or mismatched base blobs are a verification failure. No reader may invent an additional composition category such as “generic” versus “non-generic” to decide which inherited clauses apply.

## 2. Normative applicability guard

Every fresh reader MUST classify the program into exactly one interpretation state before using any bootstrap-numbered clause for work selection or state transitions.

### 2.1 `PRE_CANONICAL_BOOTSTRAP`

Condition: program header `State` is not `CANONICAL`.

Effect:

- the bootstrap chain remains operational only to produce verification/canonicalization of this candidate;
- current bootstrap Issue #5 verification and Issue #6 canonicalization rules may create eligibility exactly as specified by the verified bootstrap manifests;
- generic schema-3 rules, including `VERIFICATION_RESTART` and `VERIFICATION_REFRESH`, are active;
- normal Wave 1 `[PLAN-v1]` selection is inactive.

### 2.2 `CANONICAL_UNBOUND_ACTIVATION`

Condition: program header `State` is `CANONICAL`, but no active canonical binding resolves for the program blob under the inherited durable canonical-binding algorithm, and the named canonicalization issue has no prior valid binding for a different program blob.

Effect:

- this is only the bounded post-squash/pre-terminal activation window;
- the **only** bootstrap-numbered operational surface is the verified post-merge activation sequence of the canonicalization issue named by the header (`Bootstrap Issue #6` for this v1 bootstrap);
- no other bootstrap issue may become eligible or be replayed;
- `[PLAN-v1]` work remains inactive until terminal binding is published;
- generic schema-3 validation/canonical-binding rules remain active.

If the named canonicalization issue already has a prior valid binding for a different program blob, classify as canonical-binding mismatch/recovery, not this activation window.

### 2.3 `CANONICAL_ACTIVE`

Condition: program header `State` is `CANONICAL` and a valid active canonical binding resolves for the current canonical program blob.

Effect:

- **exactly one normal current work queue exists:** open `[PLAN-v1]` issues selected by the inherited canonical dispatcher;
- every clause whose operational subject is Bootstrap Issue #2, #3, #4, #5, #6, #11, #14, #16, or #18, or the corresponding bootstrap mission identities, is historical provenance/transition evidence only;
- such bootstrap-numbered clauses MUST NOT create eligibility, require replay, override priority, block an otherwise valid `[PLAN-v1]` selection, or reactivate completed bootstrap work;
- the presence of present-tense verbs in historical bootstrap text has no authority effect;
- generic protocol definitions remain active, including schema-3 ownership/status validation, durable canonical binding, liveness/recovery, review routing, `VERIFICATION_RESTART`, `VERIFICATION_REFRESH`, context budgets, squash-only integration, and implementation-readiness barriers;
- root `/AGENTS.md`, `docs/planning/START-HERE.md`, and the inherited canonical cold-start entry define the active selection path.

This state persists across later unrelated squash merges while the inherited canonical binding remains valid by program-blob identity plus activation-SHA ancestry.

## 3. Bootstrap-clause classification

A clause is `BOOTSTRAP_NUMBERED` when its state-transition, eligibility, or next-action subject is one of the fixed bootstrap issues/missions listed in Section 2.3. References used solely as immutable provenance, evidence identifiers, source SHAs, historical examples, or definitions do not become operational merely because they contain a bootstrap issue number.

In `CANONICAL_ACTIVE`, `BOOTSTRAP_NUMBERED` clauses have authority effect `PROVENANCE_ONLY`.

The guard is semantic authority, not a text-deletion heuristic: it deliberately allows the canonical file to retain bootstrap provenance while making its post-activation authority deterministic.

## 4. Generic verification lifecycle remains active

The Issue #16 definitions of `VERIFICATION_RESTART` and `VERIFICATION_REFRESH` remain generic schema-3 mechanisms after canonical activation:

- changed candidate/manifest after a terminal verification result requires `VERIFICATION_RESTART` and a full new verification episode;
- unchanged candidate with stale-base PASS may use `VERIFICATION_REFRESH`, followed by the full required verification suite;
- candidate change can never use refresh;
- current-base, exact-payload result selection remains mandatory.

After `CANONICAL_ACTIVE`, these mechanisms apply only to tasks/contracts that the canonical `[PLAN-v1]` graph or a later canonical revision actually declares. The historical Bootstrap Issue #5 examples do not themselves create future work.

## 5. Canonicalization and work selection

Issue #6 may promote this wrapper mechanically using the exact manifest transformations, then complete its verified post-merge activation sequence. The applicability guard is body content and survives promotion unchanged.

Post-terminal simulation requirement:

1. promoted file is `State: CANONICAL`;
2. matching terminal canonical binding resolves;
3. interpretation state becomes `CANONICAL_ACTIVE`;
4. bootstrap-numbered clauses are `PROVENANCE_ONLY`;
5. root entry documents and this program expose exactly one normal queue: open `[PLAN-v1]`;
6. no Bootstrap Issue #2–#6/#11/#14/#16/#18 clause can require repetition or override that queue.

## 6. Preserved corrections and barriers

All V5-B03 through V5-B08 corrections remain inherited from exact Issue #16/base blobs: durable binding after later merges, one PLANNING phase across entry surfaces, closed typed schema-3 authority, legacy bootstrap bridge, explicit degraded-single-agent verification mode, deterministic restart/refresh liveness, current-base verification selection, bounded context/liveness/review rules, reviewed 23-mission Wave 1, wave governors, and squash-only integration.

High-throughput gameplay implementation remains blocked until a later independently verified implementation-readiness decision. Nothing in this guard weakens that barrier.

## 7. Verification and reopen conditions

Issue #5 must verify this exact candidate work state, manifest identity, Issue #16/base blobs, adopted Wave 1 blob, current `main`, mechanical promotion, all inherited scenarios, and the post-terminal canonical-reader scenario above.

Reopen if:

- a fresh canonical reader can derive more than one current normal queue;
- a bootstrap-numbered clause can regain authority in `CANONICAL_ACTIVE` without a new canonical revision;
- the activation window authorizes anything beyond the named canonicalizer post-merge sequence;
- generic restart/refresh is accidentally disabled after activation;
- canonical-binding mismatch can be mistaken for the activation window;
- any V5-B03–V5-B08 regression reappears;
- stronger multi-agent/isolation capability becomes available and the DEGRADED independence fallback can be tightened.

PASS remains forbidden with unresolved BLOCKER/MAJOR. Candidate remains NON-CANONICAL until verified Issue #5 PASS plus Issue #6 squash promotion and terminal binding.