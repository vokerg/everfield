# ARCH-CONVERGENCE-REV-01 — Independent architecture review

**Issue:** #152  
**Reviewed producer/remediation issue:** #154 / `ARCH-CONVERGENCE-REM-01`  
**Reviewed exact work/head:** `57a941f98a00f0c49b29148e2d60b6febe7fb788`  
**Reviewed candidate blob:** `d04174e22a0bb2b45de622778c0b97a53106e8df`  
**Reviewed PR:** #155, draft/open at exact head `57a941f98a00f0c49b29148e2d60b6febe7fb788`  
**Review base:** `main@b5dd922b3170361403ee3fb02376febf737da5cc`  
**Trust profile:** `DEGRADED_SINGLE_AGENT`, fresh reviewer episode `arch-convergence-rev-01-gpt56sol-20260813-1404`; candidate immutable and not edited by this episode.  
**Disposition:** `CHANGES_REQUIRED`  
**Findings:** 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

## 1. Scope and independence

This review treats Issue #154 and PR #155 as immutable input. Producer self-review #4925034255 and the superseded Issue #150 / PR #151 self-review are provenance only and provide no independent acceptance authority.

The active canonical Planning Program binding was re-resolved before claim and remained active at review start. Current canonical authority continues to require schema-3 task ownership, required review/verification, explicit canonicality, and squash-only `main` integration. Wave-1 foundations continue to make dependency edges transition-specific and to forbid an unrelated global empirical mega-gate. Issue #84 / `W2-REV-01` remains the required aggregate cross-domain review for its declared synthesis/readiness scope. Human convergence directive `5277825639` authorizes preferential squash integration of clean reviewed bounded packets only as noncanonical provenance and explicitly forbids bypassing required remediation/review/verification/readiness/canonicalization gates.

## 2. Attack results

| # | Required attack | Result |
|---|---|---|
| 1 | Scoped noncanonical integration bypasses governing review/verification | PASS. Evidence integration requires exact independent/degraded-independent scoped acceptance; verification for later canonical/readiness routes is not converted into storage authority. |
| 2 | Aggregate review remains mandatory for cross-domain synthesis/readiness/decision | PASS. Sections 2, 3 and 10 preserve explicit aggregate-decision edges; Issue #84 is not rewritten into a storage mega-gate. |
| 3 | `IntegrationUnit` + `INTEGRATION_CLAIM` claimability without reopening task/new issue | PASS at architecture level. The unit has a separate ownership namespace, exact key, source-issue claim locus, loser-aborts semantics, and no source-branch mutation authority. |
| 4 | Deterministic contention and recovery for IntegrationUnit ownership | PARTIAL / MAJOR via `ARCH-REV-M02`. Claim contention is deterministic, but stale/recovery semantics are delegated only to “normal lease/recovery principles” and are not closed for the separate integration namespace. |
| 5 | Global `MAIN_INTEGRATION_LEASE` liveness, stale recovery, merge TOCTOU | FAIL / MAJOR via `ARCH-REV-M01` and `ARCH-REV-M02`. The advisory lease does not provide an atomic expected-base precondition to the actual squash merge, and the global lease ledger/recovery contract is not uniquely specified. |
| 6 | Compatibility false positives/negatives under main churn | PASS subject to M01 correction. Ancestor, exact identity, path-disjointness, dependency refs, policy/binding and control-surface checks are appropriately fail-closed; old packets without enough refs route bounded refresh. The remaining unsafe window is between final compatibility check and merge. |
| 7 | Migration of old packets lacking compatibility refs | PASS. It fails closed to bounded compatibility review/refresh rather than assuming disjoint safety or globally reverifying the wave. |
| 8 | `NONCANONICAL_REVIEW_PROVENANCE` leakage / negative review / recursive review | PASS. Review provenance has `acceptance_authority: NONE`; negative reviews may be stored without review-of-review and cannot accept the reviewed candidate. |
| 9 | Producer self-review downgrade | PASS. Section 4.1 categorically forbids producer self-review from satisfying `PASS_FOR_NONCANONICAL_INTEGRATION`. |
| 10 | PolicyEpoch downgrade / history rewriting | PASS. Mapping may change future authority under an explicit reviewed policy epoch but old FAIL/INCONCLUSIVE/NOT_RUN and trust states are not rewritten. |
| 11 | Ambiguous scope/dependency hides blocker | PASS with fail-closed migration rule. Durable evidence requires a bounded review scope; undeclared old compatibility dependencies do not default to safe. |
| 12 | Review/remediation recursion loophole | PASS. Default pre-aggregate recursion is finite; a second blocking re-review routes recovery/escalation/replanning instead of another automatic remediation loop. |
| 13 | Noncanonical/review-provenance state accidentally satisfies canonical/readiness/production | PASS. State separation and terminal fields expressly carry `canonicality: NONCANONICAL`, `production_authority: NONE`, `readiness_authority: NONE`; review provenance also carries no acceptance authority. |
| 14 | Dispatcher starves required review/verification while chasing integration | PASS for the bounded factory model. Ready integrations outrank new work and required review, but new producer work is lower priority and the active wave/task graph is finite; integration cannot recursively create per-merge issues. Recovery/verification needed to unlock integration remains above expansion. |
| 15 | Actual Wave-2 convergence / PR accumulation | PASS directionally. Exact-head producer PR reuse plus separately drainable review-provenance PRs removes the principal stranded-PR mechanism once a valid canonical revision/migration activates it. This review does not treat the noncanonical candidate as already active. |

## 3. Findings

### ARCH-REV-M01 — MAJOR — post-merge parent validation cannot fail closed against an external `main` race

Section 7 says the actor acquires the global lease, re-fetches `main`, recomputes compatibility, re-fetches the PR head, performs the squash merge, and then requires the resulting squash commit parent to equal the checked `main` SHA. It also says an external actor advancing `main` despite the lease causes the integration actor to fail closed and record a mismatch.

That is not fail-closed for the actual repository mutation. The available GitHub squash-merge primitive can bind the expected **PR head SHA**, but it has no expected **base/main SHA** argument. Therefore this interleaving remains possible:

1. protocol actor wins the IntegrationUnit and advisory global lease;
2. it checks `main=A` and proves the packet compatible with A;
3. an external/human/non-protocol actor advances `main` to B;
4. the protocol actor submits the squash merge with the still-correct expected PR head;
5. GitHub may merge on top of B;
6. only after the write does the actor discover that the squash parent is B rather than A.

If A→B touched a relevant policy/dependency/path but did not make the PR mechanically unmergeable, the source packet has now landed on `main` without the Section 8 compatibility predicate ever being evaluated against B. Recording a post-merge mismatch is recovery evidence, not prevention; the unauthorized integration already occurred. That violates the candidate’s own exact-base compatibility invariant and the Issue #152 TOCTOU attack requirement.

**Required correction:** the canonical architecture must require an integration primitive with an atomic expected-base precondition, not merely a post-merge parent assertion. Acceptable designs include an equivalent compare-and-swap publication path that constructs the squash result with parent A and advances `main` only if `main` is still A, or another server-enforced mechanism that proves the checked base cannot change before publication. Expected PR head checking remains required but is insufficient by itself. If no such primitive is available, the protocol must fail closed before calling the merge operation rather than relying on after-the-fact detection.

### ARCH-REV-M02 — MAJOR — the global lease and integration-recovery authority are not closed into one discoverable typed ledger

Section 6 closes normal IntegrationUnit contention well enough to identify where claims live: each `INTEGRATION_CLAIM` is posted on its source issue and keyed by `integration_unit_id`. Section 7, by contrast, requires one global `MAIN_INTEGRATION_LEASE` namespace with deterministic comment contention and stale recovery but never fixes the shared authority surface, acquisition/generation record, expiry basis, predecessor/recovery fields, winner-discovery rule across unrelated source issues, or terminal release/abandon record. Section 6 similarly says stale IntegrationUnit ownership uses normal lease/recovery “principles” in a separate namespace without defining the typed recovery transition for that namespace.

Because the merge mutex is global across unrelated source issues, leaving its authoritative comment locus to Stage-B improvisation is safety- and liveness-relevant: two implementations can each be locally schema-valid yet inspect different comment streams, or an expired holder can remain ambiguous because there is no exact generation/predecessor rule. The architecture review cannot prove deterministic winner selection or stale-lease recovery from the current candidate alone.

**Required correction:** define, at architecture level, one canonical discoverable ledger/control surface for all `MAIN_INTEGRATION_LEASE` contenders plus the minimum typed acquisition/recovery/release state machine. It must specify the singleton contention key, GitHub-server-time lease/expiry semantics, exact generation/predecessor references, immediate post-acquisition winner recheck, stale recovery tie rule, and how every integration actor discovers the authoritative current holder. Define corresponding typed stale/recovery transitions for `IntegrationUnit` ownership rather than referring only to normal task-ownership principles. Exact schema field syntax may remain a Stage-B job, but the authority topology and state machine must not.

## 4. Reconciled strengths

The revision materially closes the four producer-self-review defects from PR #151:

- `ARCH-SR-M01`: integration is now a derived claimable unit with separate ownership and no source-branch mutation authority;
- `ARCH-SR-M02`: unrelated `main` churn no longer forces blanket refresh and semantic/control-surface drift fails closed;
- `ARCH-SR-M03`: terminal review provenance is independently drainable without recursive review-of-review or candidate acceptance;
- `ARCH-SR-M04`: producer self-review cannot become scoped acceptance.

It also preserves the core authority separation the project needs: durable storage is not canonicality, aggregate W2-REV-01 remains a decision gate rather than a universal storage gate, historical evidence is immutable, and every eventual `main` integration remains squash-only.

## 5. Disposition and downstream

`CHANGES_REQUIRED` because `ARCH-REV-M01` and `ARCH-REV-M02` are MAJOR and directly affect merge safety/liveness. The candidate is **not invalidated**; both findings are bounded architectural corrections. Exactly one remediation successor must revise Issue #154’s immutable candidate without editing it, then return through one fresh independent architecture review. No canonical protocol/schema revision or Wave-2 migration may consume this exact candidate as passed architecture.

This review grants no merge, integration, canonicalization, readiness, production, implementation, verification, release, or legal/provider authority.