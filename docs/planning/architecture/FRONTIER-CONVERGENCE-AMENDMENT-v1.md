# Frontier Convergence Amendment v1 — Architecture Candidate

**Mission:** ARCH-CONVERGENCE-01 / Issue #150  
**State:** NONCANONICAL_ARCHITECTURE_CANDIDATE  
**Authority:** Project-owner-directed architecture repair candidate. This document has no canonical, verification, readiness, production, or merge authority by authorship or PR existence.  
**Scope:** Planning workflow architecture only.

## 1. Problem statement

The current planning factory is capable of producing, reviewing, and remediating work faster than it converges completed work into durable repository state on `main`.

The failure is not simply that agents ignore integration. The deeper mismatch is between three different concepts that are currently too easy to conflate:

1. **review/decision authority** — whether a claim may be trusted for a decision;
2. **integration eligibility** — whether an exact reviewed artifact may be squash-integrated to `main` as durable repository memory;
3. **canonicality/readiness authority** — whether integrated material becomes a canonical decision, implementation dependency, production input, or readiness transition.

The canonical foundation already requires typed dependency edges and says scheduler readiness applies only to edges relevant to the target task/decision/scope; it explicitly rejects an `all empirical work complete` global mega-gate. At the same time, the live Wave-2 aggregate review W2-REV-01 requires the complete Wave-2 evidence packet before the aggregate review can run. That aggregate gate is appropriate for cross-domain synthesis/readiness judgment, but it must not implicitly become the storage/integration gate for every unrelated completed evidence packet.

A second failure mode is recursive graph expansion. Optional/pre-gate review can find a correction, create a remediation successor, which can then receive another optional/pre-gate review, creating a potentially unbounded chain even when the relevant scoped acceptance obligation could already be resolved by a required review route.

A third failure mode is claim contention. Read-then-claim is inherently racy under parallel agents. The protocol already provides deterministic contention semantics; agents must treat a claim attempt as provisional until they re-read the authoritative comments and prove they won.

## 2. Non-negotiable invariants

This amendment MUST preserve all of the following:

1. Required independent review is never bypassed merely because GitHub reports a PR mergeable.
2. Verification required by a canonicalization/readiness/decision route is never bypassed merely to move files to `main`.
3. Integration does not imply canonicality, correctness, production readiness, engine selection, or implementation authority.
4. Historical evidence/results are immutable facts. A new directive or policy epoch does not rewrite an old FAIL/INCONCLUSIVE/NOT_RUN into PASS.
5. Every `main` integration is squash-only.
6. Exact head/work/base/provenance bindings remain mandatory.
7. Disposable planning-experiment code remains non-production unless separately promoted under a verified promotion route.
8. Aggregate cross-domain review remains mandatory where a cross-domain synthesis/readiness/decision contract requires it.
9. The active canonical binding is not silently replaced by this candidate.
10. A losing claim contender never mutates the task branch.

## 3. Architectural separation of states

The workflow SHALL model these states separately:

```text
PRODUCED
  -> REVIEW_READY
  -> SCOPED_REVIEW_ACCEPTED | CHANGES_REQUIRED | INVALIDATED
  -> INTEGRATION_READY_NONCANONICAL
  -> INTEGRATED_NONCANONICAL
  -> [later aggregate review / synthesis / verification / canonicalization]
  -> CANONICAL or other typed terminal authority
```

`INTEGRATION_READY_NONCANONICAL` is an integration eligibility state, not an evidence result and not a canonicality result.

An artifact may be `INTEGRATED_NONCANONICAL` while remaining:

- unverified for a later decision;
- non-production;
- noncanonical;
- blocked from synthesis/readiness;
- subject to later aggregate review;
- reopenable if later evidence invalidates it.

This is intentional. `main` is repository memory as well as the canonical base. Durable provenance integration and canonical promotion are separate operations.

## 4. Scoped acceptance route

### 4.1 Review scope

Every task contract that can produce durable planning evidence MUST identify a `review_scope_id` or an equivalent unambiguous bounded scope.

A required scoped review consumes only the exact producer/remediation chain relevant to that scope, at immutable work/head identities.

A scoped review disposition is one of:

- `PASS_FOR_NONCANONICAL_INTEGRATION`
- `CHANGES_REQUIRED`
- `INVALIDATED`

Existing review dispositions MAY be mapped into this model by a new policy epoch only when the mapping is explicit and does not strengthen the historical review result. For example, an existing clean independent review with zero BLOCKER/MAJOR/correction-requiring MINOR may be recognized as satisfying the scoped review obligation if its exact reviewed identities and independence requirements match the new policy. A self-review cannot be silently upgraded to independent review.

### 4.2 Integration eligibility predicate

An exact candidate becomes `INTEGRATION_READY_NONCANONICAL` only when all are true:

1. the exact task/remediation candidate is terminal and immutable;
2. all review obligations declared for **noncanonical integration of that scope** are satisfied;
3. no unresolved BLOCKER or MAJOR applies to that integrated scope;
4. any correction-requiring MINOR declared integration-blocking by contract is resolved;
5. the current policy epoch explicitly permits noncanonical integration for the artifact classes/paths involved;
6. the PR head equals the accepted terminal head;
7. the PR base/compatibility check against current `main` passes, or an explicitly required refresh/reverification route has passed;
8. the integration actor has current typed integration authority;
9. the merge is squash-only;
10. the resulting integration record labels canonicality as noncanonical unless a separate verified canonicalization route says otherwise.

GitHub mergeability alone satisfies none of these authority predicates.

## 5. Aggregate review is not a storage mega-gate

W2-REV-01 or any successor aggregate review MAY remain a hard prerequisite for:

- cross-domain synthesis;
- cross-domain tradeoff decisions;
- engine/runtime selection;
- implementation-readiness decisions;
- canonical promotion where the contract requires the aggregate packet.

It MUST NOT be interpreted as a prerequisite for noncanonical integration of an unrelated scoped evidence packet unless the scoped task contract explicitly proves that the aggregate review is semantically required for that packet's storage/integration safety.

Dependency rule:

> Scheduler readiness applies only to dependency edges relevant to the target transition.

Therefore:

- a `BLOCKS_SYNTHESIS` or `BLOCKS_READINESS` edge does not automatically become `BLOCKS_NONCANONICAL_INTEGRATION`;
- an aggregate `REVIEW_OF` edge does not automatically block scoped provenance integration;
- cross-domain review remains required before the cross-domain decision it governs.

This preserves the canonical foundation's prohibition on an unrelated `all empirical work complete` mega-gate.

## 6. Dispatcher: convergence before expansion

The dispatcher SHALL rank eligible work by lifecycle effect before ordinary producer expansion.

Recommended class order:

```text
1. recovery / continuation of already-owned or recoverable work
2. authorized integration of already-accepted exact work
3. verification/refresh required to unlock such integration
4. remediation/revision of a currently blocking finding
5. required scoped/aggregate review that unlocks an existing chain
6. synthesis/canonicalization required by an existing chain
7. existing producer work
8. optional/additional review
9. new task creation
```

Within a class, existing canonical priority/tie rules continue to apply unless a later reviewed policy changes them.

An action is **graph-expanding** when its normal completion creates another required issue/branch/review/remediation node. Graph-expanding work is not automatically convergence work merely because it is downstream of an existing issue.

A graph-expanding optional review MUST NOT outrank an eligible action that can terminalize/integrate/unblock an existing chain.

## 7. Required review versus optional/additional review

Every review episode MUST be typed as one of:

- `REQUIRED_SCOPED_REVIEW`
- `REQUIRED_AGGREGATE_REVIEW`
- `OPTIONAL_ADDITIONAL_REVIEW`

The scheduler MUST NOT treat these as equivalent.

`OPTIONAL_ADDITIONAL_REVIEW` may be useful for adversarial quality, but it cannot indefinitely preempt integration or a required review route.

A task may not create an optional/additional review successor solely because:

- a draft PR exists;
- another reviewer is idle;
- the formal aggregate review is blocked on unrelated scopes;
- further scrutiny could theoretically find something.

Optional review creation requires an explicit reopen predicate, unresolved risk budget item, or contract-declared review budget.

## 8. Bounded review/remediation recursion

For one scoped candidate lineage, the default pre-aggregate recursion budget is:

```text
producer candidate
  -> at most one required scoped review episode
  -> if blocking findings: one bounded remediation successor
  -> one required re-review of the corrected exact candidate
```

After that re-review:

- PASS -> scoped integration may become eligible;
- blocking finding persists -> route to the task's declared recovery/escalation/replanning predicate;
- INVALIDATED -> stop the lineage and route declared replacement/replanning;
- optional additional review requires an explicit new risk/reopen predicate and MUST NOT preempt an eligible convergence action.

A canonical task contract may define a stricter or larger finite budget, but unbounded `review -> remediation -> review -> remediation` generation is invalid.

The budget does **not** cap required aggregate review later in the lifecycle; aggregate review is a distinct obligation for its declared decision scope.

## 9. Existing Wave-2 migration / PolicyEpoch

This amendment does not retroactively reinterpret existing Wave-2 history by fiat.

Activation requires a reviewed `PolicyEpoch` (or equivalent canonical directive state) containing:

1. exact effective-from `main` SHA;
2. exact amendment/canonical policy identity;
3. affected mission IDs or a deterministic selector;
4. mapping from existing task review requirements to:
   - scoped noncanonical-integration review obligation;
   - aggregate synthesis/readiness review obligation;
5. exact artifact/path classes permitted for noncanonical integration;
6. forbidden production/canonical promotions;
7. migration rule for existing draft PRs and frozen work heads;
8. compatibility/rebase/refresh rule when `main` has advanced;
9. explicit statement that prior review/evidence results retain their historical meaning.

### 9.1 Existing clean independent reviews

A migration compiler MAY recognize an existing independent review as satisfying the new scoped review obligation only if:

- exact reviewed candidate identity matches;
- the independence profile satisfies the new obligation;
- disposition has no unresolved integration-blocking finding;
- the new policy does not demand evidence that the historical review never collected.

Recognition is a policy mapping, not rewriting the old record.

### 9.2 Existing `CHANGES_NEEDED` chains

A lineage with unresolved BLOCKER/MAJOR remains blocked from scoped integration. The current remediation chain continues until the scoped blocking findings are resolved or the lineage is invalidated/replanned.

### 9.3 Existing producer-only `REVIEW_READY`

Producer self-review alone cannot become independent scoped acceptance unless the active policy explicitly allows that trust mode for that specific noncanonical integration class. Canonical/readiness decisions remain subject to their stronger review/verification requirements.

## 10. Integration actor and record

The canonical protocol SHOULD introduce a normal integration route that is claimable when an exact candidate derives `INTEGRATION_READY_NONCANONICAL`.

The integration actor MUST:

1. start from current `main`;
2. re-resolve canonical binding and active policy epoch;
3. fetch exact accepted producer/remediation/review identities;
4. verify current PR head equals accepted head;
5. verify changed paths are within the authorized integration surface;
6. verify no unresolved scoped blocking finding;
7. verify current-main compatibility requirement;
8. squash-merge only;
9. record resulting `main_sha`, PR, source head/work, review authority, policy epoch, and canonicality result;
10. never infer canonical/readiness/production authority from the merge.

Suggested typed terminal result:

```yaml
kind: INTEGRATION_STATUS
integration_class: NONCANONICAL_EVIDENCE_PROVENANCE
source_issue: <N>
source_work_sha: <sha>
source_head_sha: <sha>
review_authority_ref: <typed ref>
policy_epoch_ref: <typed ref>
pr: <N>
pr_head_sha: <sha>
base_main_sha: <sha>
main_sha: <squash sha>
canonicality: NONCANONICAL
production_authority: NONE
readiness_authority: NONE
```

The exact schema requires canonical schema/manifest revision before activation.

## 11. Claim contention rule

Parallel agents MUST assume a race exists between frontier read and claim publication.

For a new READY task:

1. re-read issue/branch state immediately before claim;
2. publish the schema-valid claim attempt;
3. immediately re-fetch authoritative operational comments and branch head;
4. apply the canonical contention rule to all competing valid claim attempts for that source/head;
5. only the winning claim may mutate the task branch;
6. a losing contender MUST abandon the branch untouched and re-derive the frontier.

The scheduler prompt may repeat this rule, but authority belongs in the protocol because wording alone cannot make read-then-write atomic.

## 12. Review-visibility PR semantics

The existing requirement for an open draft PR before terminal `REVIEW_READY` may remain.

Its semantics SHALL remain:

- review/provenance visibility only at creation;
- no automatic canonicality or integration authority;
- exact-head binding mandatory.

However, once a separately valid scoped review + policy epoch derives `INTEGRATION_READY_NONCANONICAL`, the same exact-head PR MAY become the integration surface. No redundant PR is required merely to create a new integration object.

## 13. Rollout plan

Activation should be staged:

### Stage A — independent architecture review

Attack this candidate for:

- accidental review bypass;
- hidden canonicality promotion;
- unsafe stale-base integration;
- ambiguous scope boundaries;
- policy-epoch downgrade attacks;
- review-recursion budget loopholes;
- incompatibility with schema-3 ownership/contention;
- conflicts with Wave-2 contracts.

### Stage B — canonical protocol revision

If review passes, produce a versioned canonical-program/schema amendment implementing:

- typed review classes;
- integration eligibility;
- dispatcher ordering;
- recursion budget;
- migration PolicyEpoch;
- integration record schema;
- claim post-attempt race check.

Canonical binding must be updated through the existing verified canonicalization route; editing `PLANNING-PROGRAM-v1.md` in this producer branch is intentionally forbidden.

### Stage C — Wave-2 migration compiler

Compile existing Wave-2 missions/PRs into the new policy epoch without changing historical evidence. Derive which lineages are:

- immediately eligible for scoped review;
- already scoped-review accepted;
- still blocked on remediation;
- integration-ready;
- aggregate-review-only blocked.

### Stage D — drain before expansion

After activation, agents first consume eligible recovery/integration/verification/remediation/required-review backlog before optional review or new proposal creation.

## 14. Reopen / failure conditions

Reopen this architecture if any of the following occurs:

1. noncanonical integration can accidentally satisfy a canonical/readiness prerequisite;
2. an unrelated scope can still block noncanonical integration without an explicit dependency edge;
3. review/remediation recursion remains unbounded;
4. migration upgrades historical trust/evidence without new evidence;
5. integration can proceed with stale/mismatched head/work/base;
6. claim losers can mutate branches;
7. aggregate review is bypassed for a decision it actually governs;
8. policy epoch can silently weaken evidence requirements without provenance;
9. disposable experiment code can become a production dependency through noncanonical integration;
10. main churn causes integration validity to become ambiguous rather than fail closed/refresh.

## 15. Expected effect

This architecture changes the factory from:

```text
produce -> optional review -> remediation -> optional review -> ... -> global aggregate gate -> eventual integration
```

into:

```text
produce
  -> required scoped review
  -> bounded remediation/re-review if needed
  -> noncanonical integration when authorized
  -> later aggregate review/synthesis/verification for the decisions that actually need them
```

The intended result is higher frontier convergence without weakening evidence authority: completed reviewed work becomes durable repository memory earlier, while canonical/readiness decisions remain protected by their required aggregate review and verification gates.
