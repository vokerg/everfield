# ARCH-CONVERGENCE-REV-02 — Independent architecture re-review

**Issue:** #168  
**Reviewed remediation issue:** #163 / `ARCH-CONVERGENCE-REM-02`  
**Reviewed exact work/head:** `d1278e755fe71a4a718618b661f94dc1a51cb285`  
**Reviewed candidate blob:** `42e130f4c0faf4db181b26d9f7e3ae86e270f6f7`  
**Reviewed PR:** #165, draft/open at exact head `d1278e755fe71a4a718618b661f94dc1a51cb285`  
**Prior review:** Issue #152 terminal `CHANGES_REQUIRED`, status `5280237142`, review head `1bbea3e446f2b6451c8eac87c9df37e04466ec80`  
**Review base:** `main@268f697ad788942a2b6ff373fee1d20d32715e52`  
**Trust profile:** `DEGRADED_SINGLE_AGENT`, fresh reviewer episode `arch-convergence-rev-02-gpt56sol-20260813-1425`; Issue #163 candidate immutable and not edited by this episode.  
**Disposition:** `CHANGES_REQUIRED`  
**Findings:** 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

## 1. Scope and independence

This is the mandatory fresh re-review requested by Issue #163 terminal status, not optional review churn. It treats Issue #163 and PR #165 as immutable review inputs. Issue #163 producer self-review is provenance only and supplies no acceptance authority.

At claim time the active canonical Planning Program v1 binding remained valid: Bootstrap #6 activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` was an ancestor of `main@268f697ad788942a2b6ff373fee1d20d32715e52`, and the canonical program blob remained `e3120ec203c4156328770aa86c12fbb7187966dc`. The repository branch endpoint also reported `main` as `protected: false` at this review base. That observation is material because Revision 2 relies on fast-forward semantics as an expected-base safety substitute while explicitly assuming external/human/non-protocol ref writes can occur.

The active repository directive still requires every `main` integration to be squash-only. Revision 2 is noncanonical and therefore cannot itself activate the proposed direct-ref publication mechanism.

## 2. Attack results

| # | Required attack | Result |
|---|---|---|
| 1 | Atomic expected-base/CAS-equivalent publication under external `main` mutation | **FAIL / MAJOR `ARCH-REV2-M01`.** Non-force fast-forward publication rejects ordinary forward churn but does not prove exact old-ref equality if `main` is externally rewound to an ancestor. |
| 2 | One-parent squash-only result and exact base/head binding | PASS structurally, subject to M01. `S(parent=A)` is one commit, source head `H` is immutable, unsafe PR-merge fallback is forbidden, and post-publication identity is exact. |
| 3 | Source PR head movement | PASS. `H -> H2` invalidates the exact IntegrationUnit and requires zero-mutation discard before publication. |
| 4 | Singleton global lease ledger and deterministic current-holder discovery | PASS for topology. One PolicyEpoch-bound `integration_control_issue`, one lease key, one ordered comment stream, explicit predecessor/generation records, and lowest-comment-ID contention remove the prior multi-locus ambiguity. |
| 5 | Global-lease and IntegrationUnit stale recovery | **PARTIAL / MAJOR `ARCH-REV2-M02`.** Recovery records are typed, but protected-action authority is not explicitly revoked at expiry and no mandatory last-moment lease-validity recheck is required before publication. |
| 6 | Two unrelated IntegrationUnits contend / stale holder resumes / failed publication recovery | PARTIAL subject to M02. Winner discovery and recovery tie-break are deterministic only if every holder must prove its lease is still live immediately before the protected action. |
| 7 | Relevant vs disjoint `main` churn / old packets without dependency refs | PASS. Relevant policy/path/dependency/control-surface drift fails closed; unrelated disjoint churn need not trigger blanket re-review; insufficient old refs route bounded refresh. |
| 8 | Review-provenance / producer-self-review / aggregate-review / PolicyEpoch downgrade attacks | PASS. Negative review provenance keeps `acceptance_authority: NONE`; producer self-review remains non-accepting; W2-REV-01 remains a declared aggregate authority gate; historical FAIL/INCONCLUSIVE/NOT_RUN/trust is immutable. |
| 9 | Implementability of the atomicity property | FAIL as currently stated through M01. GitHub's non-force ref update provides a fast-forward constraint, not an exact compare-old-SHA condition; stronger server-enforced ref immutability or a true expected-old-ref primitive must be part of the proof. |
| 10 | Bounded recursion / convergence | PASS as an invariant: Revision 2 correctly says a second material failure at this required re-review must route explicit recovery/escalation/replanning rather than another automatic remediation/re-review loop. |

## 3. Findings

### `ARCH-REV2-M01` — MAJOR — fast-forward publication is not an exact expected-old-ref CAS under the stated external-writer threat model

Revision 2 replaces the unsafe PR squash endpoint with construction of a one-parent squash commit `S(parent=A)` followed by a non-force update of `refs/heads/main`. This is a substantial improvement for the ordinary race it simulates: if an external actor advances `main` from checked base A to unrelated descendant B, S is not a descendant of B and a non-force update rejects before source-packet mutation.

The safety claim is nevertheless stronger than the primitive it specifies. GitHub documents a non-force reference update as ensuring that the update is a **fast-forward** update; it does not expose an expected-current-SHA parameter on that operation. Exact compare-and-swap requires the server to accept iff the old ref is exactly A.

Counterexample under Revision 2's own assumption that external/human/non-protocol ref writes are possible:

1. reviewer-compatible integration actor holds valid IntegrationUnit/global-lease authority, evaluates `main=A`, checks immutable PR head H, and constructs `S(parent=A)`;
2. an external actor force-rewinds `main` from A to an ancestor C after the final read but before the protocol publication call;
3. `C -> S` is still a valid fast-forward because A (and therefore S) descends from C;
4. the protocol actor's non-force update can therefore succeed even though the live ref is no longer the exact base A whose state was checked;
5. the publication silently restores the A lineage plus the packet, crossing an external ref mutation the protocol never re-evaluated.

This is not theoretical under the reviewed repository state: the branch endpoint reported current `main` as unprotected at review base, and the candidate does not require a server-enforced no-force/no-delete/no-bypass invariant as part of the publication proof. The candidate forbids **its own** actor from `force=true`, which is not sufficient to constrain external writers.

**Required recovery/replanning correction:** the safety contract must require **exact old-ref equality**, not merely fast-forwardability. Either use a server primitive that atomically compares `refs/heads/main == A` while updating to S, or make an independently verified server-enforced append-only/no-force/no-delete/no-bypass policy on `main` a prerequisite such that every possible external transition after A is a descendant of A and therefore causes the proposed S update to reject. The Stage-B proof must bind the exact repository rule/ruleset identity and bypass surface, not assume it. If neither guarantee exists, publication must fail closed rather than claim CAS-equivalence.

### `ARCH-REV2-M02` — MAJOR — lease expiry is not yet a mandatory protected-action precondition

Revision 2 now defines one global ledger, GitHub-server-time start/expiry, deterministic contention, explicit recovery claims, and permanent supersession. That closes the prior authority-locus ambiguity. It does not, however, state the critical complementary rule: **a holder loses protected-action authority automatically when its lease expires, and must re-prove a still-live winning lease immediately before each protected action—especially the final ref publication.**

The current text requires an immediate winner recheck after posting a claim. It later says recovery becomes valid after expiry and a recovery winner supersedes a stale holder. Those are not equivalent to making expiry itself revoke publication authority.

Race:

1. L wins the global lease and passes the post-claim winner recheck;
2. L spends long enough on compatibility/tree construction that its lease expires;
3. R validly posts and wins a recovery generation, or L simply reaches publication after expiry before R posts;
4. absent a normative final `lease_is_live` proof, L can proceed using the once-valid generation while R also has recovery authority, or while no live lease exists;
5. the ref CAS/fast-forward check may still serialize bytes, but the protocol's singleton authority guarantee has split or silently expired.

The same issue applies to the separate IntegrationUnit ownership lease. A stale actor must not be able to rely on a historical post-claim winner check once the server-time lease deadline has passed.

**Required recovery/replanning correction:** define one normative lease-validity predicate for both namespaces. Expiry itself must revoke protected-action authority. Immediately before the final compatibility-dependent publication—and before any other state mutation declared protected by the lease—the actor must refetch the authoritative ledger/comment stream and prove: (a) its exact generation is still the current winner, (b) GitHub server time is strictly before its authoritative expiry, (c) no valid recovery/superseding generation or terminal close invalidates it, and (d) its IntegrationUnit generation is likewise live. If this proof fails, the actor performs zero protected mutation and re-enters continuation/recovery. The same rule must be included in Stage-B normative tests, including an expiry-with-no-recovery case and an expiry/recovery race immediately before publication.

## 4. Reconciled improvements and preserved strengths

Revision 2 genuinely closes most of Issue #152's prior `ARCH-REV-M02` problem: there is now one discoverable global ledger and deterministic, typed generation/recovery topology for both IntegrationUnit and merge-lease ownership. It also materially improves `ARCH-REV-M01` by separating deterministic squash construction from publication, forbidding unsafe fallback to the PR merge endpoint, and requiring zero-mutation failure on ordinary forward base churn.

The earlier `ARCH-SR-M01` through `ARCH-SR-M04` closures remain intact. IntegrationUnits are separately claimable without reopening producer tasks; compatibility can distinguish unrelated churn; terminal negative review provenance can drain without recursive review-of-review; and producer self-review cannot become scoped acceptance. Aggregate review, verification, canonicality, readiness, production, and historical-evidence boundaries remain separated.

## 5. Disposition and bounded next route

`CHANGES_REQUIRED` because `ARCH-REV2-M01` and `ARCH-REV2-M02` are MAJOR safety/authority findings. Revision 2 is not invalidated: both defects are narrow, mechanically describable, and preserve the architecture's overall direction.

This episode is the **required re-review after the first bounded remediation**. Revision 2 itself states that a second material failure at this point must route explicit recovery/escalation/replanning rather than another automatic remediation/re-review loop. Accordingly this review does **not** create another routine remediation successor. The next valid route is one bounded architecture-recovery/replanning decision that chooses and proves the actual publication/branch-protection/CAS mechanism and closes lease-expiry authority semantics before any further review cycle is instantiated.

No canonical Stage-B protocol/schema revision, migration, integration mechanism activation, direct `main` ref publication, readiness, production, implementation, verification, release, legal/provider, or other stronger authority may consume this exact candidate as passed architecture.