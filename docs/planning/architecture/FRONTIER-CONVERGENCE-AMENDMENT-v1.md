# Frontier Convergence Amendment v1 — Architecture Candidate Revision 1

**Mission:** ARCH-CONVERGENCE-REM-01 / Issue #154  
**Supersedes for review:** Issue #150 candidate at `87eda58762af6dc2235b4f7a04f5d47286fc3b0c`  
**State:** NONCANONICAL_ARCHITECTURE_CANDIDATE_REVISION_1  
**Authority:** Project-owner-directed architecture repair candidate. This document has no canonical, verification, readiness, production, or merge authority by authorship or PR existence.  
**Scope:** Planning workflow architecture only.

## 1. Problem and target

The planning factory currently produces, reviews, and remediates work faster than it converges completed work into durable repository state on `main`.

The architecture must separate three different authorities:

1. **review/decision authority** — whether an exact claim may be trusted for a declared scope;
2. **integration eligibility** — whether exact artifacts may be squash-integrated as durable repository memory;
3. **canonical/readiness authority** — whether integrated material becomes a canonical decision, production dependency, implementation-readiness input, or other promoted authority.

The canonical foundation already says scheduler readiness applies only to edges relevant to the target task/decision/scope and rejects an unrelated `all empirical work complete` mega-gate. Aggregate Wave-2 review may remain required for cross-domain synthesis/readiness decisions, but unrelated completed evidence must not be forced to remain indefinitely on transient branches solely because that aggregate decision is not yet ready.

This revision also closes producer self-review findings `ARCH-SR-M01` through `ARCH-SR-M04`: integration ownership must be concretely claimable, unrelated `main` churn must not cause refresh storms, review provenance itself must drain, and producer self-review must never masquerade as independent scoped acceptance.

## 2. Non-negotiable invariants

1. Required independent review is never bypassed because a PR is mergeable.
2. Verification required by a canonicalization/readiness/decision route is never bypassed merely to move files to `main`.
3. Integration does not imply correctness, canonicality, production readiness, engine selection, implementation authority, or synthesis acceptance.
4. Historical evidence/results are immutable facts. A new directive or policy epoch never rewrites old FAIL/INCONCLUSIVE/NOT_RUN evidence into PASS.
5. Every `main` integration is squash-only.
6. Exact source/review head, work, PR, policy, and provenance identities remain mandatory.
7. Disposable planning-experiment code remains non-production unless separately promoted through a verified promotion route.
8. Aggregate cross-domain review remains mandatory for every decision/synthesis/readiness scope that explicitly requires it.
9. This candidate does not replace the active canonical binding.
10. A losing task or integration claimant never mutates its protected surface.
11. Producer self-review has zero independent scoped-acceptance authority.
12. A protocol-compliant integration actor never merges without a current integration-unit lease and the short-lived global `main` integration lease defined below.

## 3. State separation

For reviewed evidence:

```text
PRODUCED
  -> REVIEW_READY
  -> SCOPED_REVIEW_ACCEPTED | CHANGES_REQUIRED | INVALIDATED
  -> INTEGRATION_READY_NONCANONICAL
  -> INTEGRATED_NONCANONICAL
  -> [later aggregate review / synthesis / verification / canonicalization]
  -> CANONICAL or another typed promoted authority
```

For review reports themselves:

```text
REVIEW_IN_PROGRESS
  -> REVIEW_TERMINAL
  -> REVIEW_PROVENANCE_INTEGRATION_READY
  -> REVIEW_PROVENANCE_INTEGRATED
```

`INTEGRATED_NONCANONICAL` and `REVIEW_PROVENANCE_INTEGRATED` are repository-memory states only. They do not satisfy synthesis, readiness, canonicalization, production, or decision prerequisites unless another explicit typed edge says so.

## 4. Review classes and scoped acceptance

Every review episode is exactly one of:

- `REQUIRED_SCOPED_REVIEW`;
- `REQUIRED_AGGREGATE_REVIEW`;
- `OPTIONAL_ADDITIONAL_REVIEW`.

A durable-evidence task must identify a `review_scope_id` or equivalent unambiguous bounded scope. Required scoped review consumes exact immutable producer/remediation identities relevant to that scope.

Scoped dispositions are:

- `PASS_FOR_NONCANONICAL_INTEGRATION`;
- `CHANGES_REQUIRED`;
- `INVALIDATED`.

### 4.1 Producer self-review is not acceptance

Producer self-review may:

- detect defects;
- route remediation;
- be retained as provenance;
- improve the packet presented to an independent reviewer.

Producer self-review MUST NOT satisfy `PASS_FOR_NONCANONICAL_INTEGRATION`, even if a later policy permits some raw producer provenance to be stored on `main`. Any policy that permits raw producer provenance must label that operation as a distinct provenance-only class and must not call it independent review or scoped acceptance.

A required scoped PASS must come from a separately valid independent or canonically permitted degraded-independent review episode with exact reviewed identities and trust profile.

## 5. Integration classes

This architecture defines two normal noncanonical integration classes.

### 5.1 `NONCANONICAL_EVIDENCE_PROVENANCE`

Integrates an exact producer/remediation candidate after scoped acceptance.

Eligibility requires:

1. source candidate is terminal and immutable;
2. required scoped review has valid `PASS_FOR_NONCANONICAL_INTEGRATION` for the exact source identity;
3. no unresolved BLOCKER/MAJOR applies to that scope;
4. integration-blocking MINOR findings, if declared, are resolved;
5. active PolicyEpoch explicitly permits the artifact/path class;
6. source PR head equals accepted terminal head;
7. noncanonical compatibility check in Section 8 passes against current `main`;
8. integration actor wins the integration-unit claim and global main-integration lease;
9. merge is squash-only;
10. result is explicitly `canonicality: NONCANONICAL`, `production_authority: NONE`, `readiness_authority: NONE`.

### 5.2 `NONCANONICAL_REVIEW_PROVENANCE`

Integrates a terminal review report/handoff as durable review history. This class exists specifically so review PRs do not accumulate forever after they have served their judgment role.

Eligibility requires:

1. review task has a valid terminal review result at exact review work/head;
2. PR, if one exists, is exact-head and restricted to the review task's declared review/handoff surface;
3. active policy permits review-provenance storage;
4. compatibility check passes;
5. integration actor wins the integration-unit claim and global main-integration lease;
6. merge is squash-only.

No review-of-review is required merely to store a terminal review report as provenance. Its integration means only: “this exact review episode happened and is retained.” It does not mean the review was correct, does not accept the reviewed candidate, and grants no canonical/readiness/production authority.

A terminal review with `CHANGES_REQUIRED` or `INVALIDATED` may still be integrated under this class because preserving a negative review is provenance, not acceptance.

If a required-review PR exists, the dispatcher should normally drain that review-provenance integration before the accepted source evidence integration. If no review PR exists, the protocol MUST NOT create a redundant PR solely to satisfy this ordering; the immutable terminal review record remains the authority reference.

## 6. IntegrationUnit — mandatory claimable transition

`ARCH-SR-M01` is closed by making integration a normal derived ownership namespace, not an informal “separately eligible route.”

Canonical schema revision MUST define an `IntegrationUnit` keyed by the exact tuple:

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

An `IntegrationUnit` is derived `READY` when its class-specific eligibility predicate is true and no active integration owner exists.

### 6.1 Integration ownership namespace

Integration ownership is separate from task-branch ownership. Terminalizing a producer/reviewer task does not need to reopen its task owner.

Canonical schema revision MUST add an integration acquisition transition equivalent to:

```yaml
kind: INTEGRATION_CLAIM
integration_unit_id: <exact id>
integration_class: <typed class>
source_issue: <N>
source_pr: <N>
source_pr_head_sha: <sha>
policy_epoch_ref: <exact ref>
actor_session_id: <id>
observed_main_sha: <sha>
state: IN_PROGRESS
```

Rules:

1. claim is posted on the source issue for the unit;
2. contention key is `integration_unit_id`, not current-main SHA;
3. lowest valid competing GitHub comment ID wins under the canonical contention rule;
4. immediately after posting a claim, the actor re-fetches authoritative comments and proves it won;
5. only the winner may acquire the main-integration lease or call the merge operation;
6. integration ownership grants **no source-branch mutation authority**;
7. source/review branches remain immutable at accepted heads;
8. stale integration ownership uses the normal lease/recovery principles in a separate integration namespace;
9. no new GitHub issue is created merely to make an already-ready IntegrationUnit claimable.

This makes integration visible to the normal frontier without expanding the issue graph per merge.

## 7. Global short-lived `main` integration lease

`ARCH-SR-M02` also exposes a TOCTOU problem: GitHub mergeability is evaluated against a moving base, and multiple agents can otherwise validate different snapshots and merge concurrently.

Canonical schema revision MUST define one short-lived global `MAIN_INTEGRATION_LEASE` namespace for protocol-controlled merges to `main`.

Properties:

- it serializes only the narrow compatibility-check + squash-merge critical section;
- it does not serialize producer/review/verification work;
- acquisition uses deterministic comment contention and a short recoverable lease;
- an integration actor acquires it only after winning its IntegrationUnit claim;
- while a valid lease exists, other protocol-compliant actors MUST NOT merge to `main`;
- immediately after acquisition, the actor re-fetches current `main`, recomputes compatibility, re-fetches PR head, and then performs the squash merge;
- the resulting squash commit parent must equal the `main` SHA checked inside the lease;
- if an external actor advances `main` despite the lease, the integration actor fails closed, records the mismatch, and routes recovery/compatibility review rather than pretending its earlier check covered the new base.

This is a protocol mutex around the non-atomic GitHub read/merge boundary, not a general project lock.

## 8. Noncanonical compatibility under `main` churn

Unrelated `main` advancement MUST NOT force automatic re-review. Conversely, overlapping or authority-changing drift must fail closed.

For an IntegrationUnit, compute:

- `reviewed_base_main_sha` — source base used by the accepted packet;
- `current_main_sha` — current `main` inside the global integration lease;
- `source_path_set` — exact paths changed by the source PR;
- `intervening_path_set` — exact paths changed on `main` between reviewed base and current main;
- `compatibility_dependency_refs` — exact policy/schema/content dependencies declared by the source contract/review packet.

Compatibility is `COMPATIBLE_DISJOINT` without re-review only when all are true:

1. reviewed base is an ancestor of current `main`;
2. source/review work/head identities are unchanged;
3. active canonical binding still resolves;
4. active PolicyEpoch governing the unit is unchanged;
5. `source_path_set ∩ intervening_path_set` is empty;
6. no declared `compatibility_dependency_ref` changed identity;
7. no canonical control surface governing ownership/review/integration for the unit changed incompatibly;
8. PR remains mergeable at the exact expected head.

If these conditions hold, unrelated squash integrations are not a reason to refresh or re-review.

Compatibility is `REFRESH_REQUIRED` when any relevant path, dependency, policy, schema, or semantic authority changed. Refresh is bounded to the affected scope; it MUST NOT restart unrelated reviews merely because `main` advanced.

If migration encounters an old packet that did not declare enough compatibility dependencies to prove disjoint safety, it fails closed into one bounded compatibility review/refresh rather than assuming safety or globally reverifying the wave.

## 9. Integration terminal record

After a successful squash, the integration owner publishes a typed terminal record bound to the integration ownership generation.

Minimum semantic fields:

```yaml
kind: INTEGRATION_STATUS
integration_unit_id: <id>
integration_generation_comment_id: <claim id>
integration_class: NONCANONICAL_EVIDENCE_PROVENANCE | NONCANONICAL_REVIEW_PROVENANCE
source_issue: <N>
source_work_sha: <sha>
source_head_sha: <sha>
review_authority_ref: <typed ref or null>
policy_epoch_ref: <typed ref>
pr: <N>
pr_head_sha: <sha>
checked_base_main_sha: <sha>
main_sha: <squash sha>
canonicality: NONCANONICAL
production_authority: NONE
readiness_authority: NONE
acceptance_authority: <SCOPED_REVIEW_REF | NONE>
```

For `NONCANONICAL_REVIEW_PROVENANCE`, `acceptance_authority` is always `NONE`.

The exact schema/field typing must be added through the canonical schema/manifest revision before activation.

## 10. Aggregate review is not a storage mega-gate

Aggregate review such as W2-REV-01 may remain a hard prerequisite for:

- cross-domain synthesis;
- cross-domain tradeoff decisions;
- engine/runtime selection;
- implementation-readiness decisions;
- canonical promotion where explicitly required.

It MUST NOT automatically become a prerequisite for `NONCANONICAL_EVIDENCE_PROVENANCE` or `NONCANONICAL_REVIEW_PROVENANCE` integration of an unrelated scope.

Dependency edges are transition-specific:

- `BLOCKS_SYNTHESIS` does not imply `BLOCKS_NONCANONICAL_INTEGRATION`;
- `BLOCKS_READINESS` does not imply `BLOCKS_NONCANONICAL_INTEGRATION`;
- aggregate `REVIEW_OF` does not imply a storage gate unless the contract explicitly declares a safety dependency for that integration transition.

Cross-domain review remains mandatory before the cross-domain decision it governs.

## 11. Dispatcher — convergence before expansion

Eligible work is ranked by lifecycle effect before ordinary expansion:

```text
1. recovery / continuation
2. authorized IntegrationUnits already READY
3. verification/compatibility refresh required to unlock a blocked IntegrationUnit
4. remediation/revision of a blocking finding
5. required scoped/aggregate review that unlocks an existing chain
6. synthesis/canonicalization required by an existing chain
7. existing producer work
8. optional/additional review
9. new task creation
```

Within a class, existing canonical priority/tie rules continue unless a later reviewed policy changes them.

An optional graph-expanding review MUST NOT outrank eligible integration, integration-unblocking compatibility work, blocking remediation, or required review.

## 12. Bounded scoped review/remediation recursion

Default pre-aggregate budget for one lineage:

```text
producer candidate
  -> one required scoped review
  -> if blocking findings: one bounded remediation successor
  -> one required re-review of corrected exact candidate
```

After re-review:

- PASS -> evidence IntegrationUnit may become READY;
- persistent/new blocking finding -> declared recovery/escalation/replanning route;
- INVALIDATED -> stop lineage and route replacement/replanning;
- optional additional review requires an explicit reopen predicate/risk budget and cannot preempt eligible convergence work.

A canonical contract may define another finite budget, but unbounded `review -> remediation -> review -> remediation` generation is invalid.

Aggregate review later in the lifecycle is a separate obligation and is not counted against this scoped budget.

## 13. Existing Wave-2 migration / PolicyEpoch

Activation requires a reviewed PolicyEpoch or equivalent canonical directive state containing:

1. exact effective-from `main` SHA;
2. exact canonical amendment/schema identity;
3. affected mission IDs or deterministic selector;
4. mapping of old task review requirements into scoped-integration versus aggregate-decision obligations;
5. permitted evidence/review artifact path classes;
6. forbidden canonical/production promotions;
7. migration rule for existing frozen heads and draft PRs;
8. compatibility dependency mapping for old packets;
9. explicit preservation of historical evidence/result meaning.

### 13.1 Existing clean independent reviews

A migration compiler may recognize an existing review as satisfying scoped acceptance only if:

- exact reviewed identity matches;
- review was genuinely independent/degraded-independent under the applicable protocol;
- its evidence/trust profile is at least as strong as the new scoped obligation;
- no unresolved integration-blocking finding exists;
- the new policy does not require evidence the historical review never collected.

This is a mapping of authority, not a rewrite of history.

### 13.2 Existing `CHANGES_REQUIRED` chains

Unresolved BLOCKER/MAJOR remains blocking for evidence integration. The bounded remediation route continues until scoped findings are resolved, invalidated, or replanned.

### 13.3 Existing producer-only `REVIEW_READY`

Producer self-review never becomes scoped independent acceptance under this amendment. If a human/project policy separately authorizes storage of raw producer provenance, that must be a distinct provenance-only integration class with `acceptance_authority: NONE`; it cannot be mapped to `PASS_FOR_NONCANONICAL_INTEGRATION`.

### 13.4 Existing review PRs

Terminal review PRs may be compiled into `NONCANONICAL_REVIEW_PROVENANCE` IntegrationUnits. This allows negative and positive review reports to drain to `main` without recursively requiring another review of the review.

## 14. Task-claim contention

For ordinary task ownership, parallel agents treat claim publication as provisional:

1. re-read issue/branch state immediately before claim;
2. publish schema-valid claim attempt;
3. immediately re-fetch authoritative comments and branch head;
4. apply canonical contention rule;
5. only winner mutates task branch;
6. loser leaves branch untouched and re-derives frontier.

Integration contention follows the separate IntegrationUnit namespace in Section 6.

## 15. Review-visibility PR semantics

Draft PR at task `REVIEW_READY` remains visibility/provenance only and grants no authority by existence.

Once a valid scoped review + PolicyEpoch derives an evidence IntegrationUnit, the same exact-head producer PR is the merge surface; a redundant “integration PR” is forbidden unless compatibility remediation actually creates a new candidate.

A review PR, when present, is independently drainable through `NONCANONICAL_REVIEW_PROVENANCE` and does not need a review-of-review.

## 16. Rollout

### Stage A — independent architecture review

Independently attack this revised exact candidate for:

- acceptance/review bypass;
- hidden canonicality promotion;
- IntegrationUnit ownership deadlock;
- main-integration lease liveness and TOCTOU;
- stale-base compatibility false positives/refresh storms;
- review-provenance self-certification leakage;
- PolicyEpoch downgrade attacks;
- scope/dependency ambiguity;
- recursion loopholes;
- conflicts with current schema-3 and Wave-2 contracts.

### Stage B — canonical protocol/schema revision

Only after PASS, produce a versioned canonical revision implementing:

- review classes;
- IntegrationUnit + `INTEGRATION_CLAIM` ownership namespace;
- global short-lived `MAIN_INTEGRATION_LEASE`;
- compatibility predicate;
- integration classes/terminal schema;
- dispatcher ordering;
- recursion budget;
- migration PolicyEpoch;
- task/integration post-claim race checks.

Canonical binding changes only through the existing verified canonicalization route.

### Stage C — Wave-2 migration compiler

Compile existing Wave-2 missions/PRs into the new PolicyEpoch without rewriting historical evidence. Derive exactly which are:

- scoped review needed;
- scoped review accepted;
- remediation blocked;
- review-provenance integration-ready;
- evidence integration-ready;
- aggregate-decision-only blocked.

### Stage D — drain before expansion

After activation, agents drain recovery/integration/compatibility/remediation/required-review backlog before optional review or new proposal creation.

## 17. Reopen conditions

Reopen if any of the following occurs:

1. noncanonical integration satisfies canonical/readiness/production authority accidentally;
2. an unrelated scope blocks integration without an explicit relevant edge;
3. review/remediation recursion remains unbounded;
4. migration upgrades historical trust/evidence without new authority;
5. integration proceeds with mismatched head/work/policy/base;
6. IntegrationUnit or task claim losers can mutate protected surfaces;
7. aggregate review is bypassed for a decision it governs;
8. producer self-review can satisfy scoped acceptance;
9. review-provenance integration can be mistaken for acceptance of the reviewed candidate;
10. unrelated `main` churn forces repeated global refresh/re-review;
11. concurrent protocol-controlled merges can race around the compatibility check;
12. stale global integration lease can strand `main` integration without canonical recovery.

## 18. Expected effect

The factory moves from:

```text
produce -> optional review -> remediation -> optional review -> ... -> global aggregate gate -> eventual integration
```

to:

```text
produce
  -> required scoped review
  -> bounded remediation/re-review if needed
  -> drain review provenance
  -> claim exact evidence IntegrationUnit
  -> short main-integration critical section
  -> noncanonical squash integration
  -> later aggregate review/synthesis/verification only for decisions that require them
```

The result is earlier durable repository memory and fewer stranded PRs without weakening independent review, verification, canonicality, readiness, or production gates.
