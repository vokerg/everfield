# Frontier Convergence Stage-B PolicyEpoch v2 — Candidate

**Mission:** `ARCH-CONVERGENCE-CANON-01` / Issue #181  
**State:** `NONACTIVE_POLICY_EPOCH_CANDIDATE`  
**Producer base:** `main@082740ff455b2dd81966bdb06a413000d2e704bc`  
**Revision-3 provenance:** Issue #174, reviewed candidate blob `4c9543671f2d650ee1c45797d1eee3c1cd3145e0`, squash-integrated as noncanonical provenance.  
**Independent review provenance:** Issue #176 exact head `d723b791fee6c4ffcf509f5dd7b21657da57e08d`, disposition `PASS_FOR_CANONICAL_REVISION`, review blob `56a3a07a0265ee8ea2e07cd7786197ce6d3b2813`, squash-integrated as noncanonical review provenance.  
**Current canonical authority:** unchanged Planning Program v1 / Issue #6 binding.  

This document is a **candidate for a future PolicyEpoch only**. It does not change the current canonical binding, activate Stage-B, authorize a `main` publication, satisfy verification, or grant readiness, production, implementation, release, engine, legal/provider, or gameplay authority.

## 1. Preserved authority invariants

Stage-B may become active only through a later, separately recorded activation transition after independent verification. Until then, every rule below is inert candidate text.

If activated, Stage-B MUST preserve all of the following:

1. required independent scoped review is never replaced by producer self-review;
2. declared aggregate review and verification gates remain typed prerequisites and are never inferred from mergeability or storage state;
3. `INTEGRATED_NONCANONICAL` and review-provenance integration are storage/provenance states only;
4. negative review provenance always has `acceptance_authority: NONE` and is never recursively reviewed merely because it was integrated;
5. historical PASS/FAIL/INCONCLUSIVE/NOT_RUN results, trust mode, provenance, and exact reviewed identities are immutable across PolicyEpoch migration;
6. every `main` integration remains exactly one squash publication; source/review task branches remain immutable once consumed;
7. canonicality, readiness, production, implementation, release, engine selection, and legal/provider authority remain separate typed transitions;
8. policy/schema/authority changes relevant to publication are effective only when bound to `main` by a verified PolicyEpoch activation record;
9. relevant path/dependency/policy drift fails closed; only mechanically provable disjoint drift may be treated as compatible;
10. no repository API or UI convenience action may substitute for a missing safety property.

## 2. Candidate PolicyEpoch identity and activation

Candidate epoch name:

```yaml
policy_epoch_name: PLAN-STAGE-B-v2
policy_epoch_state: CANDIDATE_INACTIVE
producer_issue: 181
producer_base_main_sha: 082740ff455b2dd81966bdb06a413000d2e704bc
revision3_blob: 4c9543671f2d650ee1c45797d1eee3c1cd3145e0
review_issue: 176
review_head_sha: d723b791fee6c4ffcf509f5dd7b21657da57e08d
review_disposition: PASS_FOR_CANONICAL_REVISION
```

The immutable activated identity MUST be created only later and MUST bind:

- exact Issue #181 terminal `work_sha == head_sha`;
- exact PolicyEpoch document blob;
- exact migration manifest blob;
- exact independent verification issue/head/report blob and PASS disposition;
- exact activation commit and its parent main SHA;
- exact `effective_from_main_sha`;
- exact integration-control issue;
- fixed coordination TTL values;
- publication primitive and verified capability evidence.

No candidate commit, PR, or noncanonical integration makes the epoch effective. If any identity is absent or inconsistent, `policy_epoch_state = INACTIVE`.

## 3. Immutable source authority

For every integration unit, the only source packet authority after terminalization is exact terminal commit `H`:

```text
H = terminal source_head_sha = terminal source_work_sha
```

A live PR is provenance/UI only after `H` is frozen. PR movement, closure, reopening, or deletion cannot change the accepted packet.

An `integration_unit_id` MUST bind at least:

```text
hash(
  policy_epoch_id,
  integration_class,
  source_issue,
  source_work_sha,
  source_head_sha,
  source_pr_or_null,
  reviewed_identity_or_null,
  exact_path_set,
  declared_dependency_set
)
```

If exact `H`, required review authority, or the accepted path/dependency packet cannot be reconstructed, the unit is `MIGRATION_BLOCKED` or `PUBLICATION_BLOCKED`; there is no fallback to a live PR head or an inferred successor commit.

## 4. Closed coordination schema

Task-branch ownership remains governed by the current planning protocol. Stage-B adds a distinct integration coordination namespace and does not reopen producer task ownership.

### 4.1 IntegrationUnit coordination

Allowed states:

```text
UNCLAIMED
INTEGRATION_PREPARING
INTEGRATION_RECOVERING
PREPARED
PUBLICATION_BLOCKED
REFRESH_REQUIRED
MAIN_PUBLISHED_BOOKKEEPING_PENDING
INTEGRATED_NONCANONICAL
ABANDONED
```

A coordination claim binds `integration_unit_id`, actor/session, generation, predecessor generation, observed main SHA, fixed TTL, and server-created comment identity. Lowest valid GitHub comment ID wins same-generation contention. Recovery requires an exact expired/stale predecessor and increments generation deterministically.

Coordination grants work ownership only. It is never the authority consumed by the Git ref mutation.

### 4.2 Global coordination surface

If Stage-B is later activated, the single globally discoverable coordination surface for this epoch is proposed as:

```yaml
integration_control_issue: 181
control_namespace: PLAN-STAGE-B-v2/MAIN_INTEGRATION_COORDINATION
singleton_key: repo:vokerg/everfield:refs/heads/main
```

Issue #181 task-ownership comments are not control-ledger records. Only schema-valid comments in `control_namespace` count. A future activation verifier MUST confirm that using this durable issue as the ledger is operationally unambiguous; otherwise activation fails and a revised candidate must bind another exact issue.

Candidate fixed TTLs:

```yaml
integration_unit_coordination_ttl_seconds: 900
global_coordination_ttl_seconds: 300
```

TTL and comment-generation state are liveness/work-throttling controls only. Expiry or overlap cannot weaken publication safety.

## 5. Compatibility authority

Every publication preparation freezes checked base `A = current main` and derives compatibility from:

- exact active PolicyEpoch at `A`;
- exact terminal source/review identities;
- exact source path set;
- exact declared dependency/control-surface identities;
- source reviewed base main SHA;
- intervening path/dependency/policy changes through `A`.

Allowed outcomes:

```text
COMPATIBLE_EXACT
COMPATIBLE_DISJOINT
REFRESH_REQUIRED
MIGRATION_BLOCKED
PUBLICATION_BLOCKED
ALREADY_INTEGRATED
```

`COMPATIBLE_DISJOINT` requires mechanical proof that the reviewed base is an ancestor of `A`, governing PolicyEpoch is unchanged, exact source/review identities are unchanged, source and intervening paths are disjoint, declared dependencies are unchanged, and the immutable `H` packet applies without undeclared transformation.

Missing legacy dependency information is not evidence of disjointness. It routes fail-closed under the migration manifest.

## 6. Publication attempt

A prepared attempt binds:

```yaml
kind: PUBLICATION_ATTEMPT
publication_attempt_id: <immutable id>
integration_unit_id: <exact id>
policy_epoch_id: <exact active id>
source_head_sha: <H>
checked_base_main_sha: <A>
squash_commit_sha: <S>
integration_coordination_generation_comment_id: <id>
global_coordination_generation_comment_id: <id>
state: PREPARED
```

`S` MUST have exactly one parent `A`. Its tree MUST equal `A` plus exactly the accepted source packet at immutable `H`, including typed additions/modifications/deletions/renames and no undeclared paths. The commit message MUST include exact source/review/PolicyEpoch identities and a unique machine-readable `integration_unit_id` publication marker.

## 7. Sole publication safety primitive

Stage-B permits publication only through a **server-enforced exact-old-ref transaction** whose update request carries:

```text
ref          = refs/heads/main
expected_old = A
new          = S
```

The server MUST accept only if the current ref is exactly `A` at commit time. Every mismatch—including forward advance, rewind, deletion/recreation, or replacement by an unrelated tip—MUST result in zero `main` mutation.

The candidate concrete implementation route is authenticated native Git push/receive-pack semantics, where the push protocol's ref update command carries `old-id new-id refname`. Official Git pack-protocol and `git-receive-pack` documentation describe that old/new ref update shape. GitHub's official documentation supports authenticated Git pushes over HTTPS/SSH. These facts establish a plausible implementation class, **not repository-specific activation capability**.

Capability references for independent verification:

- `https://git-scm.com/docs/pack-protocol` — push update request uses `old-id new-id name`;
- `https://git-scm.com/docs/git-receive-pack` — receive-pack updates remote refs and exposes old/new object identities;
- `https://docs.github.com/en/get-started/git-basics/about-remote-repositories` — GitHub supports authenticated Git push over HTTPS/SSH.

### 7.1 Capability is fail-closed

This producer host does not possess an independently demonstrated native Git transport credential/path for `vokerg/everfield`; therefore:

```yaml
candidate_publication_primitive: GIT_RECEIVE_PACK_EXACT_OLD_REF
repository_capability_state: UNPROVEN_PENDING_INDEPENDENT_VERIFICATION
```

Independent verification MUST prove, using an authorized non-destructive/scratch-ref probe or equivalent authoritative evidence, that the concrete repository credential/transport:

1. can invoke authenticated native Git push/receive-pack;
2. rejects a stale exact old object ID before changing the target ref;
3. can enforce all applicable repository rules/permissions without bypassing them;
4. can publish the exact one-parent squash object without a fallback endpoint that lacks expected-old semantics.

If any item cannot be proven, activation disposition is `PUBLICATION_CAPABILITY_BLOCKED` and Stage-B remains inactive.

Forbidden fallbacks unless separately proven to expose equivalent expected-old semantics:

- generic REST ref update with only `force=false`;
- ordinary PR merge/squash endpoint;
- force push;
- read-current-main then write-new-main sequences without server-enforced expected-old binding.

## 8. Publication outcomes and recovery

Allowed publication outcomes:

```text
PUBLISHED_EXACT
EXPECTED_OLD_MISMATCH
POLICY_OR_PERMISSION_BLOCKED
TRANSPORT_FAILED_NO_PUBLICATION
TRANSPORT_AMBIGUOUS
ALREADY_PUBLISHED_MARKER_FOUND
```

After any success response, refetch `main` and require exact `main == S` before terminal publication bookkeeping.

After a failed or ambiguous response, first refetch `main` and search for the exact unique integration marker. If exact `S`/marker proves the unit already published, continue bookkeeping without republishing. Otherwise treat the attempt as failed, release/abandon coordination as appropriate, refresh compatibility, and never automatically rebuild on a newer base until `ALREADY_INTEGRATED` is disproven.

Coordination expiry may create overlapping preparers, but the exact-old server transaction is the sole mutation arbiter. At most one attempt from checked base `A` can change `main`.

## 9. PR divergence and bookkeeping

After exact publication of frozen `H` as `S`:

- if current PR head equals `H`, record the equality and close/link the visibility PR according to repository policy;
- if PR head differs from `H`, record `PR_DIVERGED_FROM_FROZEN_HEAD`, both exact identities, and never claim later PR commits were integrated;
- comment/closure failure is `MAIN_PUBLISHED_BOOKKEEPING_PENDING`, not permission to republish or revert;
- review provenance remains `acceptance_authority: NONE` even after storage integration.

## 10. Fail-closed migration

The companion `FRONTIER-CONVERGENCE-MIGRATION-v2.yaml` is normative candidate input for migration classification.

Every pre-Stage-B packet is classified without rewriting historical evidence:

- `MIGRATABLE_EXACT` only when exact terminal `H`, source/review authority, path/dependency set, historical trust/results, and publication marker state are reconstructable;
- `MIGRATABLE_PROVEN_DISJOINT` only with equivalent proof plus current-main compatibility;
- `ALREADY_INTEGRATED_NONCANONICAL` only with durable exact main publication evidence;
- otherwise `MIGRATION_BLOCKED_REFRESH_REQUIRED`.

Migration never converts negative/inconclusive evidence to PASS, never infers an independent review, and never makes a storage state satisfy synthesis/readiness/canonicality.

## 11. Mandatory independent verification suite

A fresh verifier distinct from this producer and from Issue #176 review MUST freeze the Issue #181 terminal candidate and execute/reason through all of the following before any activation:

1. two same-base publishers for one IntegrationUnit — at most one exact-old update succeeds;
2. two unrelated IntegrationUnits after coordination expiry — at most one update from base `A` succeeds;
3. stale owner and recovered owner overlap — coordination may overlap but mutation cannot split-brain;
4. source PR advances after frozen `H` — published packet remains exactly `H`;
5. external `main` forward advance after preparation — zero mutation;
6. external `main` rewind after preparation — zero mutation;
7. delete/recreate or unrelated replacement of `main` after preparation — zero mutation;
8. relevant path/dependency/policy drift — `REFRESH_REQUIRED`;
9. mechanically disjoint drift — may remain compatible only with complete dependency proof;
10. transport failure before update — zero mutation and bounded retry;
11. ambiguous response after successful update — marker discovery prevents duplicate publication;
12. PR close/link failure or divergent PR head — bookkeeping continuation only;
13. negative review-provenance drain — no acceptance/canonical/readiness authority;
14. producer self-review downgrade attack — rejected;
15. legacy packet with missing immutable `H`, review authority, dependency fields, or publication marker — migration blocks;
16. historical FAIL/INCONCLUSIVE/NOT_RUN/trust records survive migration byte-for-byte or identity-equivalent as declared;
17. concrete GitHub publication capability/permission probe proves stale-old rejection and repository-policy compatibility;
18. activation record changes PolicyEpoch effectiveness only through exact verified main-bound identity.

PASS requires zero BLOCKER/MAJOR and no correction-requiring MINOR, plus concrete publication capability `PROVEN`.

## 12. Activation boundary

Only a later, separately scoped activation task may bind this candidate as canonical. Its prerequisites MUST include:

```yaml
candidate_issue: 181
candidate_terminal_state: REVIEW_READY
candidate_exact_work_head: <exact sha>
candidate_policy_doc_blob: <exact blob>
candidate_migration_blob: <exact blob>
verification_issue: <exact issue>
verification_disposition: PASS
publication_capability_state: PROVEN
current_canonical_binding_revalidated: true
activation_main_parent_sha: <exact current main>
```

The activation transition MUST produce a durable canonical binding/PolicyEpoch record and must itself respect the repository's review, verification, authority, and squash-only publication rules. If current main, policy, permissions, or candidate identities drift incompatibly before activation, activation fails closed and is re-derived.

Activation of Stage-B would grant only the workflow/protocol authority explicitly defined by the verified epoch. It would not grant application implementation readiness, production release, engine selection, legal/provider clearance, gameplay authority, or domain decisions.

## 13. Producer self-review

Producer self-review result for this bounded candidate:

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0

Checks performed:

- current canonical entry documents are not edited;
- Revision-3 and Issue #176 identities are exact and immutable inputs;
- exact-old mutation semantics are preserved without treating coordination leases as mutation credentials;
- native Git transport is named only as a candidate implementation class, while repository-specific capability remains explicitly unproven and activation-blocking until independent verification;
- migration is fail-closed and cannot rewrite historical authority/evidence;
- independent verification and a separate activation transition are mandatory;
- no readiness/production/release/engine/legal/gameplay authority is claimed.

Producer self-review is provenance only and cannot satisfy the required independent Stage-B verification.