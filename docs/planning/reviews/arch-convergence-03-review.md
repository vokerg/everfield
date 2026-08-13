# ARCH-CONVERGENCE-REV-03 — Independent architecture review

**Issue:** #176  
**Reviewed issue:** #174 / `ARCH-CONVERGENCE-REM-03`  
**Reviewed head:** `dba063d20d63d74402f01e58c6a96bfd54909aa0`  
**Reviewed candidate blob:** `4c9543671f2d650ee1c45797d1eee3c1cd3145e0`  
**Reviewed PR:** #175 at exact reviewed head `dba063d20d63d74402f01e58c6a96bfd54909aa0`  
**Predecessor review:** Issue #167, terminal review head `10d1648ebbabcfec76b22778903ffa23d82c3686`, review blob `552b0ef5ba4d8461c4b4236090b9e6408a391f07`  
**Review base:** `main@9b84a565111428616856e5fd15b48a4760d64d20`  
**Trust profile:** `DEGRADED_SINGLE_AGENT_FRESH_REVIEW_EPISODE`; reviewer episode distinct from the Issue #174 producer and Issue #167 reviewer; candidate immutable and not edited here.  
**Disposition:** `PASS_FOR_CANONICAL_REVISION`  
**Findings:** 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

## Scope and method

This review cold-reconstructed the exact Revision-3 candidate and prior routed findings before considering producer rationale. It attacked the two previously open publication-authority gaps, then re-ran the surrounding convergence invariants that could be weakened by the correction: source immutability, global and per-unit recovery, checked-base compatibility, PR linkage, negative review-provenance draining, producer-self-review prohibition, aggregate review, verification/canonicalization separation, PolicyEpoch migration, and activation boundaries.

PR #175 changes only the declared architecture candidate and Issue #174 handoff. No unrelated workflow, evidence, implementation, engine, readiness, release, or production surface is modified.

## Routed finding reconciliation

### `ARCH-REV2-M01` — CLOSED

Issue #167 found that Revision 2 treated expiring IntegrationUnit/global comment generations as mutation authority even though their freshness could not be atomically coupled to the `main` ref write.

Revision 3 removes that false safety dependency rather than narrowing the read/write interval:

- IntegrationUnit and global generations are explicitly coordination/recovery records only;
- a stale actor is expected to stop cooperatively if it observes replacement, but safety does not depend on that observation;
- publication safety is delegated to one exact expected-old server transaction with `expected_old=A` and `new=S(parent=A)`;
- overlapping stale/recovery actors may both reach publication, but only one transaction can observe exact old `A`; every loser performs zero `main` mutation;
- after a success, the durable exact IntegrationUnit publication marker prevents another attempt from rebuilding/re-publishing the same unit on a later base.

This is a coherent authority model. The coordination lease determines who should work; the server ref transaction determines who can mutate `main`. There is no remaining requirement for an independently expiring comment generation to be observably current at the mutation instant.

### `ARCH-REV2-M02` — CLOSED

Issue #167 found that Revision 2 declared live PR-head equality with frozen `H` to be a publication precondition even though it was only checked observationally before the `main` mutation.

Revision 3 chooses the other coherent model allowed by the finding: immutable terminal `H` is the sole source packet authority after terminalization.

- the IntegrationUnit key binds exact frozen source work/head `H`;
- publication materializes bytes from `H`, never from the then-live PR head;
- later PR movement, closure, reopening, or deletion cannot change the packet being published;
- loss of materializability of `H` blocks publication rather than falling forward to a live head;
- post-publication PR bookkeeping records `integrated_head: H` and any divergent live head separately and cannot describe later commits as integrated.

The former source-head read/write race disappears because live PR-head equality is no longer an authority-bearing condition.

## Adversarial attack results

### A1 — exact-old publication on forward churn

Construct `S1(parent=A)` and `S2(parent=A)` for one or two IntegrationUnits. Let one actor publish first, changing `main` from `A` to `S1`.

**Result:** PASS. The second transaction presents `expected_old=A` against current `S1` and must be rejected with zero ref mutation. It cannot silently rebuild against the new base without first refreshing compatibility and proving its IntegrationUnit was not already published.

### A2 — exact-old publication on rewind / replacement

Prepare `S(parent=A)`, then move `main` to an ancestor `C`, delete/recreate the ref, or replace it by an unrelated tip before publication.

**Result:** PASS. Revision 3 explicitly requires equality with exact old object `A`, not merely a fast-forward check. A generic non-force REST ref update is expressly insufficient. Every `current_main != A` case is required to fail before mutation.

### A3 — exact primitive availability and branch policy

Attack the design by assuming the eventual runtime exposes only ordinary PR merge/squash or a GitHub REST ref update without caller-bound expected-old semantics, or by assuming the exact-old transport is rejected by branch policy/permissions.

**Result:** PASS / activation-blocked as designed. The candidate does not treat those weaker operations as substitutes and grants no direct-main-ref authority. Section 11 requires the later canonical Stage-B schema/PolicyEpoch revision to name the exact server/native API, prove repository permissions can use it without bypassing required branch policy, and verify the state-machine simulations before activation. If that capability cannot be proven, publication remains blocked; this architecture candidate itself does not claim deployability.

### A4 — continuously running stale owner

Let U1 win IntegrationUnit/global coordination, prepare from `A`, then let both leases expire. U2 wins recovery while U1 never observes supersession; both reach publication.

**Result:** PASS. Lease freshness is not mutation authority. Both attempts can be well-formed, but the exact-old ref transaction serializes the mutation. One can change `main`; the other performs zero mutation and must refresh. No split-brain publication or indefinite recovery wait is required.

### A5 — two unrelated IntegrationUnits after global recovery

Let U1 and U2 prepare distinct one-parent squash commits from the same `A` after global coordination recovery overlaps.

**Result:** PASS. Exactly one `A -> S` transaction can succeed. The losing unit refreshes against the new main and re-derives compatibility. Global coordination remains a work-avoidance/liveness throttle rather than a second mutation credential.

### A6 — source PR advances after terminal `H`

Freeze terminal `H`; then advance the source branch/PR to `P != H` before publication, during publication, or before PR close bookkeeping.

**Result:** PASS. `P` is not a publication input. Exact `H` remains the only packet authority, and PR bookkeeping has typed `MATCHED_FROZEN_H` versus `DIVERGED_FROM_FROZEN_H` outcomes. A divergent PR cannot make commits after `H` appear integrated.

### A7 — ambiguous network result after successful mutation

Let the server commit `A -> S` and lose the client response.

**Result:** PASS. The actor must first fetch `main` and prove exact `S` / the exact IntegrationUnit marker is already present before performing bookkeeping. It is forbidden to automatically rebuild the same unit on a newer base without proving non-publication. This bounds duplicate integration after an ambiguous response.

### A8 — post-publication PR linkage failure

Let `main == S` succeed, then fail the PR provenance comment or closure step, including a live PR head that has diverged from `H`.

**Result:** PASS. The candidate assigns typed pending states and continuation semantics. Recovery verifies the already-published `S` and finishes bookkeeping without republishing or rewriting source evidence.

### A9 — relevant versus disjoint `main` churn

Attack compatibility with path overlap, dependency/control-surface drift, PolicyEpoch/schema drift, missing dependency declarations, and provably unrelated disjoint changes.

**Result:** PASS. Relevant or unprovable drift fails closed to refresh/review; disjoint churn can remain compatible when the reviewed base is an ancestor, exact source/review identities are unchanged, governing PolicyEpoch is unchanged, paths are disjoint, dependencies are unchanged, and the exact `H` packet remains applicable.

### A10 — publication-policy race

Attempt to change publication semantics or the permitted primitive outside the `main` identity used for compatibility.

**Result:** PASS within the Stage-B model. Revision 3 requires publication-relevant policy/schema changes to become effective through a main-bound PolicyEpoch/canonical transition. A later effective epoch necessarily changes `main`, so an attempt prepared against old `A` cannot pass the exact-old transaction.

### A11 — negative review provenance and recursive authority

Integrate a terminal negative review as storage provenance, then attempt to use that integration to satisfy acceptance, canonicality, readiness, production, synthesis, or implementation prerequisites, or recursively require review of the review artifact itself.

**Result:** PASS. Review provenance retains `acceptance_authority: NONE`; `INTEGRATED_NONCANONICAL` is a storage state only; producer self-review remains provenance only; review-of-review is not created.

### A12 — aggregate review / verification / canonicality downgrade

Attempt to use scoped noncanonical integration or this architecture review to replace formal aggregate Wave-2 review, required verification, canonicalization, readiness, or production authorization.

**Result:** PASS. The candidate preserves these as separate typed gates and explicitly grants none of those authorities.

### A13 — activation by integration alone

Attempt to integrate the noncanonical candidate or this review provenance and immediately use Stage-B coordination/publication records.

**Result:** PASS. Revision 3 has an explicit mechanically discoverable activation boundary: only a later separately scoped canonical schema/PolicyEpoch revision may define and activate the records, global control issue, exact publication API, permissions, main-bound epoch semantics, migration, and simulation verification.

## Scope / authority inspection of PR #175

PR #175 is open, draft, mergeable, and exact-head at the reviewed `dba063d20d63d74402f01e58c6a96bfd54909aa0`. Its changed-file set is limited to:

- `docs/planning/architecture/FRONTIER-CONVERGENCE-AMENDMENT-v1.md`;
- `docs/planning/handoffs/issue-174.md`.

The PR body and candidate both state that the packet is a noncanonical architecture candidate, requires this fresh review, and grants no integration, activation, canonicalization, verification, readiness, production, implementation, release, legal/provider, engine, or merge authority. No scope leakage or authority inflation was found.

## Disposition

`PASS_FOR_CANONICAL_REVISION`.

Revision 3 closes `ARCH-REV2-M01` and `ARCH-REV2-M02` without reopening the previously accepted convergence invariants. The exact-old publication primitive is not treated as currently available authority: proving the concrete server/native mechanism and repository permission/branch-policy compatibility remains a mandatory part of the later canonical Stage-B revision and verification route.

This pass makes a **separately scoped canonical protocol/schema/PolicyEpoch revision and migration/verification route** eligible to be considered under the repository frontier. It does not activate Revision 3 and does not itself authorize integration of the candidate, direct `main` mutation, migration, verification, canonicalization, readiness, production, implementation, release, legal/provider action, engine selection, or any bypass of required review.
