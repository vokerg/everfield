# Frontier Convergence Amendment v1 — Architecture Candidate Revision 3

**Mission:** `ARCH-CONVERGENCE-REM-03` / Issue #174  
**Immutable candidate input:** Issue #163 head `d1278e755fe71a4a718618b661f94dc1a51cb285`, candidate blob `42e130f4c0faf4db181b26d9f7e3ae86e270f6f7`  
**Routing review:** Issue #167 terminal `CHANGES_REQUIRED`, review head `10d1648ebbabcfec76b22778903ffa23d82c3686`, review blob `552b0ef5ba4d8461c4b4236090b9e6408a391f07`  
**Routed findings:** `ARCH-REV2-M01`, `ARCH-REV2-M02`  
**State:** `NONCANONICAL_ARCHITECTURE_CANDIDATE_REVISION_3`  
**Authority:** architecture remediation candidate only. This document does not activate a protocol, authorize integration, satisfy review or verification, or grant canonicality, readiness, production, implementation, release, legal/provider, engine, or merge authority.

## 1. Purpose and preserved invariants

Revision 3 preserves the convergence architecture already accepted as sound by prior review and changes the publication-authority boundary required by Issue #167.

The following invariants remain mandatory:

1. required independent scoped review, aggregate review where declared, and required verification are never bypassed because a PR is mergeable;
2. `INTEGRATED_NONCANONICAL` and review-provenance integration are storage states only and cannot satisfy canonical, readiness, production, engine-selection, synthesis, release, or implementation prerequisites without a separate typed edge;
3. producer self-review is provenance only and never substitutes for independent scoped acceptance;
4. historical FAIL / INCONCLUSIVE / NOT_RUN / trust evidence is immutable across PolicyEpoch migration;
5. every `main` integration is one squash commit only;
6. source and review task branches remain immutable once consumed by an IntegrationUnit;
7. aggregate review remains mandatory for governed cross-domain decision/synthesis/readiness scopes but is not invented as a universal storage gate;
8. relevant path, dependency, policy, schema, or authority drift fails closed while provably unrelated disjoint `main` churn may be compatible without re-review;
9. terminal positive or negative review provenance may drain without recursive review-of-review and always has `acceptance_authority: NONE`;
10. bounded review/remediation recursion and transition-specific dependency edges remain mandatory.

## 2. Immutable source authority: terminal head H, not a live PR head

`ARCH-REV2-M02` is closed by choosing one coherent source-authority model.

For an IntegrationUnit, the immutable source authority is the exact terminal task/review identity already accepted for storage:

```text
H = terminal source_head_sha == terminal source_work_sha
```

The IntegrationUnit key binds that frozen identity:

```text
integration_unit_id = H(
  integration_class,
  source_issue,
  source_work_sha,
  source_head_sha,
  source_pr_or_null,
  reviewed_identity_or_null,
  policy_epoch_ref
)
```

A source PR is a visibility/provenance surface. Its live head is not publication authority after terminalization.

Normative rules:

1. derivation requires a valid terminal source/review record that freezes exact `H` and any required review authority;
2. publication constructs bytes from exact immutable commit `H`, never from the PR's then-current head;
3. later movement, closure, reopening, or deletion of the PR does not silently change `H` and does not authorize later commits;
4. if exact `H` or a required reviewed identity can no longer be materialized and verified, publication is `PUBLICATION_BLOCKED`; there is no fallback to the live PR head;
5. a PR-head equality check may be recorded as diagnostic provenance but is not a safety precondition for publishing `H`;
6. PR UI bookkeeping after publication must explicitly distinguish `H` from any later live PR head, as specified in Section 8.

This removes the read/write gap identified by `ARCH-REV2-M02`: source-head movement is deliberately irrelevant to the immutable packet being integrated rather than an observational precondition that can become false immediately after a read.

## 3. IntegrationUnit coordination and bounded recovery

An IntegrationUnit remains a separately coordinated unit on the source issue; it does not reopen producer task ownership and grants no source-branch mutation authority.

Stage-B schema may retain typed records such as:

```yaml
kind: INTEGRATION_CLAIM
integration_unit_id: <exact id>
generation: <positive integer>
predecessor_generation_comment_id: <comment id or null>
actor_session_id: <id>
source_issue: <N>
source_head_sha: <H>
policy_epoch_ref: <exact ref>
observed_main_sha: <sha>
lease_seconds: <PolicyEpoch fixed value>
state: IN_PROGRESS
```

and:

```yaml
kind: INTEGRATION_RECOVERY_CLAIM
integration_unit_id: <exact id>
generation: <previous generation + 1>
stale_generation_comment_id: <exact expired claim id>
predecessor_generation_comment_id: <exact prior generation id>
actor_session_id: <id>
state: RECOVERING
```

Server-time creation, fixed TTL, exact predecessor references, lowest-valid-comment-ID contention, immediate winner recheck, and bounded stale recovery are retained.

### 3.1 Coordination is not mutation authority

`ARCH-REV2-M01` is closed by removing the impossible requirement that an expiring comment lease remain atomically current at the Git ref mutation boundary.

IntegrationUnit claims and recoveries are **coordination credentials only**. They control who should perform expensive preparation and who may start a recovery attempt; they are not a server-enforced credential consumed by the `main` ref update.

Therefore:

1. a claimant MUST win and recheck its coordination generation before beginning protected preparation;
2. expiry permits bounded recovery so the system never waits indefinitely for a silent actor;
3. a stale actor that observes expiry or a recovery generation MUST cooperatively stop before starting new preparation;
4. safety does **not** rely on the stale actor observing that supersession before its already-prepared Git publication attempt;
5. if stale and recovery actors overlap, the exact-old-ref publication transaction in Section 7 is the sole mutation arbiter; at most one can change `main`;
6. after one publication succeeds, every other attempt for that IntegrationUnit must recognize the durable `integration_unit_id` publication marker on refreshed `main` and terminalize/abandon without republishing it on a newer base.

Recovery is thus bounded without pretending that an independently expiring comment record can be atomically coupled to a Git ref write.

## 4. Global main-publication coordination ledger

The active Stage-B PolicyEpoch still binds exactly one globally discoverable `integration_control_issue`, and the singleton coordination key remains:

```text
repo:vokerg/everfield:refs/heads/main
```

The ledger retains server-time generations, deterministic contention, fixed TTL, exact predecessor references, stale recovery, and typed close records such as `RELEASED`, `ABANDONED`, and `COMMITTED`.

### 4.1 Global lease semantics

The global lease is a **coordination throttle**, not the cryptographic/server-side authority to mutate `main`.

Normative consequences:

1. normally only the winner performs compatibility analysis and constructs a publication attempt;
2. expiry permits another IntegrationUnit to recover global coordination even if the former actor is still running;
3. a stale actor that observes recovery stops cooperatively, but safety remains correct if it misses that observation and attempts publication;
4. overlapping attempts, whether for the same or different IntegrationUnits, are serialized by the exact expected-old-ref server transaction in Section 7;
5. the loser of that transaction performs zero `main` mutation and must refresh from the resulting `main`; it may continue only if the source unit remains unintegrated and a fresh compatibility derivation authorizes another attempt;
6. the ledger remains valuable for convergence, work avoidance, diagnostics, and bounded recovery, but no claim of "still-current lease authority at the mutation instant" appears in the safety proof.

This explicitly covers both IntegrationUnit and global generations under `ARCH-REV2-M01`.

## 5. Main-bound policy and compatibility authority

Publication-relevant policy/schema changes must themselves be main-bound so that the Git expected-base condition can protect them.

A Stage-B PolicyEpoch MUST have an immutable identity and an `effective_from_main_sha`. Any change that affects publication eligibility, integration classes, compatibility dependencies, source-authority semantics, or the permitted publication primitive becomes effective only through a new main-bound PolicyEpoch/canonical binding transition.

Comment ledgers may coordinate work, but they may not create a safety-critical policy change whose effectiveness is invisible to `main`.

For checked base `A`, compatibility is derived from:

- active canonical binding and PolicyEpoch effective at `A`;
- exact frozen source/review identities including `H`;
- reviewed base main SHA;
- exact source path set;
- intervening path set through `A`;
- declared dependency/control-surface identities.

`COMPATIBLE_DISJOINT` requires the reviewed base to be an ancestor of `A`, exact source/review identities unchanged, governing PolicyEpoch unchanged through `A`, source/intervening paths disjoint, declared dependencies unchanged, and the exact `H` packet applicable to `A` without undeclared mutation.

Relevant drift is `REFRESH_REQUIRED`. A packet that lacks enough declared dependencies to prove compatibility fails closed to bounded refresh/review.

## 6. Publication attempt construction

After compatibility against exact `main=A`, an actor constructs exactly one publication attempt:

```yaml
kind: PUBLICATION_ATTEMPT
publication_attempt_id: <unique immutable id>
integration_unit_id: <exact id>
source_head_sha: <H>
checked_base_main_sha: <A>
policy_epoch_ref: <exact ref effective at A>
integration_coordination_generation_comment_id: <id>
global_coordination_generation_comment_id: <id>
state: PREPARED
```

The coordination generation IDs are provenance, not mutation credentials.

The actor deterministically constructs one commit `S` such that:

1. `S` has exactly one parent, `A`;
2. `S`'s tree is `A` plus exactly the accepted source packet at immutable `H`, including typed additions/modifications/deletions/renames and no undeclared paths;
3. source/review branches are not rewritten;
4. the commit message records source issue, exact source work/head `H`, source PR if any, review authority ref if any, IntegrationUnit ID, publication attempt ID, PolicyEpoch ref, and `canonicality: NONCANONICAL`;
5. the commit message contains a machine-readable unique integration marker for `integration_unit_id`, used to prevent re-publication after an ambiguous post-write failure.

Before sending the ref transaction, the actor may refetch `main` for work avoidance. A mismatch may abort early, but correctness does not depend on that ordinary read.

## 7. Atomic exact-old-ref squash publication

The publication safety primitive is an **exact expected-old-ref transaction**, not merely an observational read followed by a REST ref update.

The server transaction must encode:

```text
update refs/heads/main
expected_old = A
new          = S
```

and accept iff the server's current `refs/heads/main` is exactly `A` when the ref transaction is committed.

A permitted implementation is a native Git receive-pack/ref transaction whose update command carries exact old object ID `A` and new object ID `S`, or another server-enforced API with identical exact-old semantics. A generic GitHub REST ref update that does not bind an expected old object ID is not sufficient merely because it is `force=false`.

Normative rules:

1. `S` remains a one-parent squash commit with parent `A`;
2. the server must reject with zero ref mutation for **any** current-main mismatch, including `A -> B` advance, `A -> C` rewind to an ancestor, deletion/recreation, or replacement by an unrelated tip;
3. `force=true` without exact expected-old semantics is forbidden;
4. a normal PR merge/squash endpoint lacking exact expected-base semantics is forbidden as fallback;
5. branch-protection, permission, policy, transport, or expected-old mismatch is `PUBLICATION_BLOCKED`/`REFRESH_REQUIRED` as appropriate and changes no source bytes on `main`;
6. after success, refetch `main` and require exact `main == S` before publishing `COMMITTED`/integration status;
7. after a failed or ambiguous response, first fetch `main`: if the unique `integration_unit_id` marker proves exact `S` is already the current/ancestor publication for this unit, continue bookkeeping without republishing; otherwise treat the attempt as failed and refresh;
8. never rebuild the same IntegrationUnit automatically on a newer base without first proving it was not already published.

Because the exact-old check is enforced inside the ref transaction, an expired coordination lease, concurrent recovery, external advance, or external rewind cannot create two successful publications from the same checked base. This is the sole mutation-arbitration proof required by `ARCH-REV2-M01`.

## 8. PR linkage when H and the live PR diverge

After exact `main == S` is confirmed, PR state is bookkeeping only.

If a source PR exists:

1. refetch its current head `P`;
2. always post provenance stating that exact terminal `H` was integrated as `S` and that no commits after `H` were integrated;
3. if `P == H`, the PR may be closed through the repository API after the provenance comment;
4. if `P != H`, record `PR_DIVERGED_FROM_FROZEN_HEAD`, explicitly state `integrated_head: H` and `current_pr_head: P`, and close only as a non-merged/superseded visibility surface or leave it open for separately scoped later work according to repository UI policy; it must never be described as though `P` was integrated;
5. a moved PR does not cause the actor to switch from `H` to `P`;
6. comment/closure failure after successful main publication becomes `MAIN_PUBLISHED_PR_CLOSE_PENDING` or `MAIN_PUBLISHED_PR_DIVERGED_PENDING`; continuation verifies `S` and completes UI bookkeeping without republishing.

This makes PR movement harmless to publication correctness and prevents later commits from being accidentally represented as integrated.

## 9. Terminal integration record

A successful terminal record binds the actual publication rather than claiming lease freshness at the mutation instant:

```yaml
kind: INTEGRATION_STATUS
integration_unit_id: <id>
publication_attempt_id: <id>
integration_class: NONCANONICAL_EVIDENCE_PROVENANCE | NONCANONICAL_REVIEW_PROVENANCE
source_issue: <N>
source_work_sha: <sha>
source_head_sha: <H>
review_authority_ref: <typed ref or null>
policy_epoch_ref: <typed ref effective at A>
pr: <N or null>
checked_base_main_sha: <A>
squash_commit_sha: <S>
squash_parent_sha: <A>
publication_primitive: EXACT_OLD_REF_TRANSACTION
integration_coordination_generation_comment_id: <id>
global_coordination_generation_comment_id: <id>
observed_pr_head_at_linkage: <sha or null>
pr_head_relation: MATCHED_FROZEN_H | DIVERGED_FROM_FROZEN_H | NO_PR
canonicality: NONCANONICAL
production_authority: NONE
readiness_authority: NONE
acceptance_authority: <SCOPED_REVIEW_REF | NONE>
state: INTEGRATED_NONCANONICAL
```

For review provenance, `acceptance_authority` is always `NONE`.

## 10. Normative adversarial simulations

Stage-B implementation/review must reproduce at least these state-machine attacks.

### S1 — IntegrationUnit expires while old actor continuously executes

Actor U1 wins IntegrationUnit generation I1 and global coordination G1, prepares `S1(parent=A)`, then both coordination TTLs expire. Recovery actor U2 acquires I2/G2 while U1 never pauses. U1 and U2 may both attempt exact-old publication.

Expected: coordination recovery is not blocked; exactly one exact-old `A -> S` transaction succeeds; the loser changes no main bytes and discovers the winner by refreshing main/integration marker. No claim that comment-generation freshness was atomically checked at mutation time is needed.

### S2 — two unrelated IntegrationUnits overlap after global expiry

U1 prepares `S1(parent=A)`. Its global coordination expires and U2 prepares `S2(parent=A)` for a different unit.

Expected: exactly one expected-old transaction succeeds. The loser refreshes against the new main and re-derives compatibility; no split-brain main publication occurs.

### S3 — source PR advances after H is frozen

Terminal authority freezes `H`; PR later advances to `P != H` before or during publication.

Expected: the constructed commit contains exactly H's accepted packet. Publication is unaffected by P. Post-publication provenance records both H and P and never claims P was integrated.

### S4 — external main advance after preparation

Actor prepares `S(parent=A)` and an external actor advances main to B.

Expected: server rejects because current old ref is B, not A; zero packet mutation.

### S5 — external main rewind after preparation

Actor prepares `S(parent=A)` and an external actor rewinds main to ancestor C.

Expected: exact-old server transaction rejects because current old ref is C, not A, even though `C -> S` could otherwise be fast-forward. A plain non-force REST update is insufficient.

### S6 — publication-relevant PolicyEpoch changes

A new effective PolicyEpoch is activated through a main-bound transition after attempt base A.

Expected: main is no longer A, so the exact-old transaction fails; actor must refresh under the new epoch.

### S7 — ambiguous network result after successful ref update

Server commits `A -> S`, but the client loses the response.

Expected: client fetches main and the unique integration marker. If S/unit is present, it performs bookkeeping only and must not publish the unit again.

### S8 — PR linkage failure or divergent PR after main publication

Main is exactly S but PR comment/closure fails, or current PR head is P != H.

Expected: typed pending state; no republish/revert. Continuation binds H/S/P precisely and completes UI bookkeeping without claiming P was integrated.

## 11. Stage-B activation and migration boundary

Revision 3 remains noncanonical. One fresh independent architecture re-review is required on the exact immutable Revision-3 head.

Only a later, separately scoped canonical schema/PolicyEpoch revision may activate these semantics. That later work must:

1. define the exact typed coordination, recovery, publication-attempt, pending, and terminal records;
2. bind the one global control issue and fixed server-time TTLs;
3. define the exact native/server API that supplies `expected_old=A` atomic ref semantics and prove repository permissions can use it without bypassing required branch policy;
4. bind PolicyEpoch effectiveness to main identity;
5. migrate old IntegrationUnits fail-closed when immutable H, compatibility dependencies, or publication markers cannot be proven;
6. preserve historical outcomes and trust metadata exactly;
7. verify all simulations in Section 10 before activation.

No direct-main-ref operation, integration, migration, verification, canonicalization, readiness, production, implementation, or release action is authorized by this candidate itself.
