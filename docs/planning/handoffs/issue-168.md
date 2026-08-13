# Issue #168 Handoff — ARCH-CONVERGENCE-REV-02

## State

Mandatory fresh/degraded-independent architecture re-review is complete with disposition `CHANGES_REQUIRED`: 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

This is the required re-review after Issue #163's bounded remediation of Issue #152 findings. It is therefore the second material review failure in this architecture lineage; do not automatically create another ordinary remediation -> re-review loop. Route bounded architecture recovery/escalation/replanning first.

## Exact reviewed input

- Issue #163 / `ARCH-CONVERGENCE-REM-02`
- work/head `d1278e755fe71a4a718618b661f94dc1a51cb285`
- candidate blob `42e130f4c0faf4db181b26d9f7e3ae86e270f6f7`
- handoff blob `c146afbdd8e232319583df0c8371ea0c013e1e73`
- draft PR #165 at exact reviewed head
- prior Issue #152 review status `5280237142`, head `1bbea3e446f2b6451c8eac87c9df37e04466ec80`

The candidate was immutable throughout this review episode.

## Review findings

### `ARCH-REV2-M01` — MAJOR — non-force fast-forward update is not exact old-ref CAS

Revision 2's `S(parent=A)` + non-force `refs/heads/main -> S` publication correctly rejects ordinary external forward churn from A to a divergent descendant B. It does not prove `current_main == A` at the atomic write boundary.

GitHub's reference-update contract for `force=false` is a fast-forward constraint. If an external actor force-rewinds `main` from A to an ancestor C in the check-to-publication window, C -> S remains a fast-forward, so publication can succeed even though the checked base A was no longer the live ref. At review base `main@268f697ad788942a2b6ff373fee1d20d32715e52`, GitHub reported the branch as unprotected, so Revision 2 cannot rely on an unstated no-force/no-bypass invariant.

Recovery must bind either a true server-enforced expected-old-ref compare-and-swap primitive or an independently verified append-only/no-force/no-delete/no-bypass branch/ruleset guarantee that makes every possible external ref transition after A a descendant of A. The exact rule identity and bypass surface must be part of the Stage-B proof. Otherwise publication fails closed.

### `ARCH-REV2-M02` — MAJOR — lease expiry does not itself revoke protected-action authority

Revision 2 now has one global ledger plus typed deterministic generation/recovery records. It still lacks a normative requirement that expiry automatically ends protected-action authority and that the holder must re-prove a live winning global lease **and** live IntegrationUnit generation immediately before protected publication.

A holder can win/recheck once, spend past expiry constructing the publication, then race a recovery winner or publish after expiry before recovery is posted. The ref publication primitive may serialize bytes, but the protocol mutex/authority claim has expired or split.

Recovery must define one lease-validity predicate in both namespaces. Immediately before publication/protected state mutation, refetch authoritative records and prove exact generation is current winner, server time is before expiry, no superseding recovery/terminal record exists, and the corresponding IntegrationUnit generation remains live. Failure means zero protected mutation and continuation/recovery. Stage-B simulations must include expiry without recovery and an expiry/recovery race at publication time.

## Attacks that passed

- one-parent deterministic squash construction and exact immutable source-head binding, subject to M01's publication guard;
- source PR head movement fails closed;
- one PolicyEpoch-discoverable global lease ledger and deterministic contention topology;
- relevant versus disjoint `main` compatibility and fail-closed old-packet dependency migration;
- negative review-provenance storage with `acceptance_authority: NONE` and no review-of-review;
- categorical prohibition on producer self-review satisfying independent scoped acceptance;
- aggregate W2-REV-01 preservation for governed synthesis/readiness/decision authority;
- PolicyEpoch historical outcome/trust immutability;
- separation of noncanonical storage from readiness/production/canonical authority;
- no unsafe fallback to an ordinary PR merge endpoint.

## Required next action

Route one bounded **architecture recovery/escalation/replanning** decision, not another automatic ordinary remediation/re-review cycle. That recovery must choose and prove the actual expected-base publication mechanism / branch-rule prerequisites and make lease liveness a mandatory protected-action precondition. Only after that explicit recovery decision may a further correction/review topology be instantiated.

Do not edit/re-own Issue #163 or its branch. Do not treat Revision 2 as passed architecture. Do not begin canonical Stage-B migration/activation from this candidate.

## Authority

This handoff and its review are noncanonical architecture-review provenance only. They grant no workflow activation, candidate integration authority, canonicalization, readiness, production, implementation, verification, release, legal/provider, engine, or direct-main-ref authority. Every current `main` integration remains governed by the active squash-only repository directive.