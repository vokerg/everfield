# Frontier Convergence Amendment v1 — Architecture Candidate Revision 2

**Mission:** `ARCH-CONVERGENCE-REM-02` / Issue #163  
**Supersedes for review:** Issue #154 candidate at `57a941f98a00f0c49b29148e2d60b6febe7fb788`, blob `d04174e22a0bb2b45de622778c0b97a53106e8df`  
**Independent review input:** Issue #152 terminal `CHANGES_REQUIRED`, review head `1bbea3e446f2b6451c8eac87c9df37e04466ec80`, review blob `5eb6e513befc2706f830f91f6789b86a0041ff9b`  
**State:** `NONCANONICAL_ARCHITECTURE_CANDIDATE_REVISION_2`  
**Authority:** architecture remediation candidate only; no workflow activation, integration permission, canonicality, verification, readiness, production, implementation, release, legal/provider, or merge authority is created by this document or its PR.  
**Scope:** planning workflow convergence architecture.

## 1. Purpose and preserved architecture

The repository must converge already-completed planning work into durable memory without treating storage as acceptance or canonicality. This revision preserves the architecture already judged sound in Issue #152 and changes only the two MAJOR surfaces `ARCH-REV-M01` and `ARCH-REV-M02`.

Preserved invariants:

1. required independent scoped/aggregate review and required verification are never bypassed because a PR is mergeable;
2. `INTEGRATED_NONCANONICAL` and review-provenance integration are storage states only and cannot satisfy canonical, readiness, production, engine-selection, synthesis, release, or implementation prerequisites without a separate typed edge;
3. producer self-review can detect defects and be retained as provenance but can never satisfy independent scoped acceptance;
4. historical FAIL / INCONCLUSIVE / NOT_RUN / trust evidence is immutable across PolicyEpoch migration;
5. every `main` integration is squash-only;
6. source/review task branches remain immutable once consumed by an IntegrationUnit;
7. aggregate review remains mandatory for the cross-domain decision/synthesis/readiness scopes that declare it, but is not invented as a universal storage gate;
8. compatibility remains fail-closed for relevant path, dependency, policy, schema, or authority drift and may accept unrelated disjoint `main` churn without re-review;
9. terminal review provenance, including negative review, may drain without recursive review-of-review and always has `acceptance_authority: NONE`;
10. bounded review/remediation recursion and transition-specific dependency edges remain mandatory.

## 2. State separation and integration classes

Reviewed evidence remains:

```text
PRODUCED
  -> REVIEW_READY
  -> SCOPED_REVIEW_ACCEPTED | CHANGES_REQUIRED | INVALIDATED
  -> INTEGRATION_READY_NONCANONICAL
  -> INTEGRATED_NONCANONICAL
  -> [later aggregate review / synthesis / verification / canonicalization]
```

Review reports remain:

```text
REVIEW_IN_PROGRESS
  -> REVIEW_TERMINAL
  -> REVIEW_PROVENANCE_INTEGRATION_READY
  -> REVIEW_PROVENANCE_INTEGRATED
```

Two normal storage classes remain:

- `NONCANONICAL_EVIDENCE_PROVENANCE`: exact producer/remediation packet after valid independent/degraded-independent scoped acceptance for the exact identity and zero unresolved integration-blocking findings;
- `NONCANONICAL_REVIEW_PROVENANCE`: exact terminal review report/handoff, including `CHANGES_REQUIRED` or `INVALIDATED`, stored only as historical review provenance with no acceptance authority and no review-of-review requirement.

Both classes require exact source/PR/review identities, an active compatible PolicyEpoch, a winning IntegrationUnit generation, a winning global main-publication lease, a compatible current main snapshot, and the atomic squash publication primitive in Section 6.

## 3. IntegrationUnit — separate claim and recovery namespace

An IntegrationUnit remains a derived unit, not a new GitHub issue. Its immutable key is:

```text
integration_unit_id = H(
  integration_class,
  source_issue,
  source_work_sha,
  source_head_sha,
  source_pr,
  source_pr_head_sha,
  review_authority_ref_or_null,
  policy_epoch_ref
)
```

The source issue is the authoritative comment locus for that IntegrationUnit. Task ownership never reopens merely to integrate an immutable terminal packet.

### 3.1 IntegrationUnit ownership records

Canonical Stage-B schema MUST define the following typed records in the separate integration namespace:

```yaml
kind: INTEGRATION_CLAIM
integration_unit_id: <exact id>
generation: <positive integer>
predecessor_generation_comment_id: <comment id or null>
actor_session_id: <id>
source_issue: <N>
source_pr: <N>
source_pr_head_sha: <sha>
policy_epoch_ref: <exact ref>
observed_main_sha: <sha>
lease_seconds: <PolicyEpoch fixed value>
state: IN_PROGRESS
```

```yaml
kind: INTEGRATION_RECOVERY_CLAIM
integration_unit_id: <exact id>
generation: <previous generation + 1>
stale_generation_comment_id: <exact expired claim id>
predecessor_generation_comment_id: <exact prior generation id>
actor_session_id: <id>
lease_seconds: <same PolicyEpoch rule>
state: RECOVERING
```

Terminal/continuation records are typed as `INTEGRATION_STATUS` with one of:

```text
INTEGRATED_NONCANONICAL
MAIN_PUBLISHED_PR_CLOSE_PENDING
REFRESH_REQUIRED
PUBLICATION_BLOCKED
ABANDONED
INVALIDATED
```

Rules:

1. all IntegrationUnit contenders read the same source-issue comment stream;
2. `integration_unit_id` is the contention key;
3. lease start time is the winning claim comment's GitHub server `created_at`; expiry is exactly `created_at + PolicyEpoch.integration_unit_lease_seconds`; client clocks are non-authoritative;
4. among otherwise valid concurrent claims for the same predecessor generation, the lowest GitHub comment ID wins;
5. the claimant MUST immediately refetch the authoritative comments and prove its generation is the winner before touching protected integration state;
6. an unexpired winning generation excludes all new claims and recovery claims;
7. recovery is valid only after server-time expiry with no terminal/renewal record that keeps that generation live, and MUST reference the exact stale generation;
8. concurrent recovery claims against the same stale generation use the same lowest-comment-ID winner rule; losers abort;
9. a recovered generation permanently supersedes the stale owner for protected integration actions even if the stale actor later resumes;
10. source/review branches are immutable throughout; IntegrationUnit ownership grants no branch mutation authority;
11. a terminal `INTEGRATED_NONCANONICAL`, `ABANDONED`, or `INVALIDATED` closes that generation; `REFRESH_REQUIRED`, `PUBLICATION_BLOCKED`, and `MAIN_PUBLISHED_PR_CLOSE_PENDING` are typed continuation states with exact next-action rules and do not create another issue by default.

A PolicyEpoch may define bounded renewal records, but renewal must be server-time based, reference the live generation, be discoverable from the same comment stream, and may not revive an already superseded generation.

## 4. Canonical global integration-control ledger

`ARCH-REV-M02` is closed by requiring one globally discoverable control surface for every protocol-controlled publication to `refs/heads/main`.

The canonical Stage-B schema/PolicyEpoch MUST contain exactly one field:

```yaml
integration_control_issue: <repository issue number>
```

That issue is the sole authoritative ledger for `MAIN_INTEGRATION_LEASE` records for the active PolicyEpoch. Every actor discovers it by resolving the active canonical binding -> active PolicyEpoch -> `integration_control_issue`; actors MUST NOT choose a per-source issue, PR thread, local file, chat state, or another ad-hoc comment stream as an equivalent lease authority.

The singleton contention key is exactly:

```text
repo:vokerg/everfield:refs/heads/main
```

### 4.1 Global lease records

The ledger state machine MUST support:

```yaml
kind: MAIN_INTEGRATION_LEASE_CLAIM
lease_key: repo:vokerg/everfield:refs/heads/main
generation: <positive integer>
predecessor_generation_comment_id: <comment id or null>
integration_unit_id: <exact id>
integration_generation_comment_id: <winning IntegrationUnit claim id>
actor_session_id: <id>
observed_main_sha: <sha>
lease_seconds: <PolicyEpoch fixed short value>
state: HELD
```

and typed recovery/terminal records:

```text
MAIN_INTEGRATION_LEASE_RECOVERY_CLAIM
MAIN_INTEGRATION_LEASE_RELEASED
MAIN_INTEGRATION_LEASE_ABANDONED
MAIN_INTEGRATION_LEASE_COMMITTED
```

Rules:

1. lease start is the winning ledger comment's GitHub server `created_at`; expiry is `created_at + PolicyEpoch.main_integration_lease_seconds`; client time is ignored;
2. only the winner of a live IntegrationUnit generation may contend for the global lease;
3. all valid claims for the same predecessor global generation contend on the singleton lease key and lowest GitHub comment ID wins;
4. immediately after posting, the claimant MUST refetch the global ledger and prove it is the winning unexpired generation before entering the publication critical section;
5. a live generation excludes all other protocol actors from `main` publication;
6. stale recovery is valid only after server-time expiry and must reference the exact stale global generation; concurrent recovery claims against it use lowest-comment-ID winner semantics;
7. a recovery winner supersedes the stale holder, which must abort if it resumes;
8. `RELEASED`, `ABANDONED`, and `COMMITTED` each reference the exact winning generation and close it; the next claimant uses that closed generation as predecessor;
9. every actor derives the current holder by folding the one canonical ledger in comment-ID order under these rules; there is no second authority surface;
10. the global lease is a narrow protocol mutex, not a safety substitute for the atomic expected-base publication primitive below. External/human/non-protocol writes are assumed possible and are handled safely by Section 6.

## 5. Compatibility under current-main churn

Inside a winning global lease, the actor re-resolves:

- active canonical binding and active PolicyEpoch;
- exact source/review/PR identities;
- `reviewed_base_main_sha`;
- current `main` SHA `A`;
- exact source path set;
- intervening path set from reviewed base to `A`;
- declared compatibility dependency refs and canonical control surfaces.

`COMPATIBLE_DISJOINT` is allowed without re-review only when:

1. reviewed base is an ancestor of `A`;
2. all source/review work/head identities and the expected PR head are unchanged;
3. canonical binding and governing PolicyEpoch are unchanged;
4. source paths and intervening paths are disjoint;
5. no declared compatibility dependency changed identity;
6. no governing ownership/review/integration control surface changed incompatibly;
7. the exact source change can be applied to `A` without conflict or undeclared path mutation.

Relevant path/dependency/policy/schema/authority drift is `REFRESH_REQUIRED`. An old packet that lacks enough declared dependencies to prove disjoint compatibility also fails closed to one bounded compatibility review/refresh. Unrelated `main` churn alone is not a global re-review trigger.

## 6. Atomic expected-base squash publication

`ARCH-REV-M01` is closed by replacing the unsafe read-then-GitHub-merge operation with a CAS-equivalent publication primitive. The canonical protocol MUST NOT use an API that can silently retarget the squash onto a newer base after the final compatibility check.

Let `A` be the exact `main` SHA checked inside the winning global lease and `H` the exact expected source PR head.

### 6.1 Construct one squash result

After the final compatibility and exact-head checks, the integration actor deterministically constructs exactly one commit `S` such that:

1. `S` has exactly one parent and that parent is `A`;
2. `S`'s tree is `A` plus exactly the source PR's accepted path changes at immutable head `H`, including typed additions/modifications/deletions/renames and no undeclared paths;
3. source/review branches are not rewritten;
4. the commit message records source issue, PR, exact source/work/head, review authority ref if any, IntegrationUnit id/generation, PolicyEpoch ref, and `canonicality: NONCANONICAL`;
5. `S` is therefore the single squash commit representing the accepted packet, irrespective of the number of commits on the task branch.

Before publication, the actor refetches PR head and current `main`. If PR head != `H` or current main != `A`, it discards `S`, makes zero main mutation, releases/abandons the global lease as typed, and returns to exact-head/compatibility derivation.

### 6.2 Server-enforced expected-base publication

Publication is an update of `refs/heads/main` from `A` to `S` using a **non-force ref update** or another server-enforced primitive with the same safety property:

> the server must accept the write only if the current `main` tip can fast-forward to the exact one-parent commit `S(parent=A)`; if `main` advanced after the check, publication fails before changing `main`.

Because `S` is a direct child of `A`, any external advance `A -> B` before the ref update makes `S` non-fast-forward from `B`. A non-force update must therefore reject the publication. This is the required CAS-equivalent expected-base guard.

Normative rules:

1. `force=true` is forbidden;
2. a normal PR squash-merge endpoint lacking expected-base/CAS semantics is forbidden as fallback;
3. branch-protection, permission, policy, or ref-update rejection is `PUBLICATION_BLOCKED` and causes zero source-packet mutation on `main`;
4. after a successful ref update, refetch `main` and require exact `main == S`;
5. only then publish the global lease `COMMITTED` record and IntegrationUnit main-publication status;
6. any mismatch is a protocol failure/recovery condition, never retroactive permission.

If repository settings make a non-force direct ref update unavailable, the protocol must fail closed and route a canonical publication-mechanism remediation. It must not downgrade to the unsafe merge endpoint.

### 6.3 PR linkage and closure

After `main == S` is confirmed, the actor writes a provenance comment to the source PR containing `S`, IntegrationUnit/generation, and the exact source/review identities, then closes the PR through the repository API. The PR is not treated as independently merged authority; the one-parent commit `S` is the squash integration record.

If PR comment/closure fails after `main` publication, the IntegrationUnit enters `MAIN_PUBLISHED_PR_CLOSE_PENDING`; the main publication is not repeated or reverted merely to repair UI bookkeeping. A continuation actor verifies exact `main == S`, completes PR linkage/closure, then terminalizes `INTEGRATED_NONCANONICAL`. This preserves convergence without pretending a post-publication PR-close failure invalidates repository bytes.

## 7. Integration terminal record

A successful integration terminal record binds:

```yaml
kind: INTEGRATION_STATUS
integration_unit_id: <id>
integration_generation_comment_id: <winning id>
integration_class: NONCANONICAL_EVIDENCE_PROVENANCE | NONCANONICAL_REVIEW_PROVENANCE
source_issue: <N>
source_work_sha: <sha>
source_head_sha: <sha>
review_authority_ref: <typed ref or null>
policy_epoch_ref: <typed ref>
pr: <N>
pr_head_sha: <sha>
checked_base_main_sha: <A>
squash_commit_sha: <S>
squash_parent_sha: <A>
global_lease_generation_comment_id: <winning global lease id>
publication_primitive: EXPECTED_BASE_NONFORCE_REF_UPDATE
canonicality: NONCANONICAL
production_authority: NONE
readiness_authority: NONE
acceptance_authority: <SCOPED_REVIEW_REF | NONE>
state: INTEGRATED_NONCANONICAL
```

For review provenance, `acceptance_authority` is always `NONE`.

## 8. Adversarial state-machine simulations

The following simulations are normative acceptance tests for Stage-B schema/tooling.

### S1 — two unrelated IntegrationUnits contend globally

Units U1 and U2 each have valid source-issue IntegrationUnit ownership. Both read global generation G and post global lease claims referencing G. The lower valid GitHub comment ID wins. The loser discovers the winner on mandatory recheck and performs no compatibility or publication mutation under the lease.

Expected: exactly one global holder; no split-brain authority across source issues.

### S2 — stale global holder recovery

Winner L is silent beyond `created_at(L) + main_integration_lease_seconds` with no closing record. Two recovery claims reference exact stale L. Lowest valid recovery comment ID becomes generation L+1; the other aborts. If L resumes, it sees a superseding generation and cannot publish.

Expected: deterministic bounded stale recovery.

### S3 — stale IntegrationUnit owner recovery

The same server-time/explicit-predecessor rule is applied on the source issue for the IntegrationUnit generation. Recovery winner supersedes the stale task-independent integration owner without reopening producer task ownership.

Expected: one typed integration owner and no vague delegation to task-ownership principles.

### S4 — external `main` advance after final check

Actor checks compatible `main=A`, constructs `S(parent=A)`. External actor advances `main` to B before publication. Non-force ref update `main -> S` is rejected because S is not a descendant of B.

Expected: zero source-packet mutation on `main`; actor re-derives compatibility against B. This directly closes `ARCH-REV-M01`.

### S5 — source PR head movement

Actor holds the global lease but PR head changes H -> H2 before publication. Final exact-head check fails and S is discarded.

Expected: zero main mutation; old IntegrationUnit cannot silently consume H2 because its identity includes H.

### S6 — disjoint versus relevant main churn

Disjoint A0 -> A changes no source path/dependency/policy/control-surface identity: compatibility may be `COMPATIBLE_DISJOINT`. Relevant churn changes a source path or declared dependency: compatibility is `REFRESH_REQUIRED`.

Expected: no blanket re-review storm and no semantic false-positive.

### S7 — publication primitive unavailable

Compatibility passes, but branch protection/permission rejects non-force main ref update.

Expected: zero main mutation, `PUBLICATION_BLOCKED`, global lease released/abandoned, no fallback merge endpoint.

### S8 — failure after successful publication

`main` becomes exact S, but PR closure fails. IntegrationUnit records `MAIN_PUBLISHED_PR_CLOSE_PENDING`. A continuation verifies exact S and closes/linkes the PR without republishing S.

Expected: no duplicate integration and deterministic frontier continuation.

## 9. Dispatcher and convergence

Lifecycle ranking remains:

```text
1. recovery / continuation
2. already-ready authorized IntegrationUnits
3. verification/compatibility work required to unlock integration
4. remediation/revision of blocking findings
5. required scoped/aggregate review
6. synthesis/canonicalization for an existing chain
7. existing producer work
8. optional/additional review
9. new task creation
```

Global lease contention is not a reason to create another task. A blocked publication primitive is recovery/remediation work; optional review may not preempt it.

## 10. Bounded review/remediation recursion

Default pre-aggregate lineage remains:

```text
producer -> required scoped review
         -> if blocking: one bounded remediation
         -> one required re-review
```

A second material failure after the required re-review routes explicit recovery/escalation/replanning rather than an unbounded automatic review/remediation loop. Aggregate review later is a separate declared obligation.

## 11. PolicyEpoch / migration requirements

Canonical activation of this architecture requires a separately reviewed schema/PolicyEpoch that binds at minimum:

1. effective-from main SHA and exact architecture/schema identities;
2. exact `integration_control_issue`;
3. fixed `integration_unit_lease_seconds` and `main_integration_lease_seconds`;
4. affected mission selector and permitted evidence/review path classes;
5. mapping of historical reviews into scoped integration authority without rewriting trust/history;
6. compatibility dependency mapping for old packets and fail-closed refresh when insufficient;
7. exact typed IntegrationUnit/global-lease generation, recovery, renewal, release, abandon, publication, PR-close-pending, and terminal records;
8. the allowed server-enforced publication primitive and proof that it preserves one-parent squash-only semantics under branch protection;
9. explicit prohibition on unsafe merge-endpoint fallback when expected-base publication is unavailable;
10. explicit preservation of aggregate review, verification, readiness, canonicality, production, and historical-evidence gates.

No actor may use Revision 2 as if those Stage-B changes were already active.

## 12. Finding disposition and self-review

### `ARCH-REV-M01` — RESOLVED in candidate architecture

The unsafe post-merge base assertion is replaced by a pre-mutation CAS-equivalent publication rule: construct one squash commit `S(parent=A)` and advance `main` only by non-force ref update/server primitive that rejects an external `main` advance before mutation. Unsafe PR merge fallback is forbidden.

### `ARCH-REV-M02` — RESOLVED in candidate architecture

The active PolicyEpoch binds exactly one `integration_control_issue`; all global lease actors read/write that same ledger. Both global lease and separate IntegrationUnit ownership now have explicit server-time lease, generation/predecessor, immediate winner recheck, lowest-comment-ID contention, typed stale recovery, supersession, and terminal state rules.

Producer self-review/adversarial simulation against S1-S8 finds:

- unresolved BLOCKER: 0;
- unresolved MAJOR: 0;
- correction-requiring MINOR: 0.

The earlier `ARCH-SR-M01` through `ARCH-SR-M04` closures remain intact: claimable IntegrationUnits, disjoint-main compatibility, drainable review provenance, and categorical producer-self-review prohibition are preserved.

## 13. Stopping and authority boundary

This exact Revision 2 must be frozen on Issue #163 with a handoff and exact-head draft PR before terminal `STATUS(REVIEW_READY)`. One fresh independently owned architecture review is mandatory. The Issue #152 reviewer episode must not adjudicate this remediation.

No canonical protocol/schema revision, migration, IntegrationUnit execution, global lease acquisition, direct main-ref publication, or workflow activation is authorized merely because this candidate exists or passes producer self-review. Any eventual main integration remains separately authorized and squash-only.