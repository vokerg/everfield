# Issue #174 handoff — ARCH-CONVERGENCE-REM-03

## Episode identity

- mission: `ARCH-CONVERGENCE-REM-03`
- issue: #174
- branch: `planning/issue-174`
- actor/session: `arch-convergence-rem-03-gpt56sol-20260813-frontier-run`
- winning ownership claim: `5280484508`
- claim/base main: `9b84a565111428616856e5fd15b48a4760d64d20`
- immutable candidate input: Issue #163 head `d1278e755fe71a4a718618b661f94dc1a51cb285`, candidate blob `42e130f4c0faf4db181b26d9f7e3ae86e270f6f7`
- routing review: Issue #167 terminal status `5280468431`, review head `10d1648ebbabcfec76b22778903ffa23d82c3686`, review blob `552b0ef5ba4d8461c4b4236090b9e6408a391f07`
- routed findings: `ARCH-REV2-M01`, `ARCH-REV2-M02`
- revised candidate path: `docs/planning/architecture/FRONTIER-CONVERGENCE-AMENDMENT-v1.md`
- revised candidate blob after substantive commit: `4c9543671f2d650ee1c45797d1eee3c1cd3145e0`
- substantive candidate commit: `c1ba131665f40c679d17cd04d214a15d563837b4`

## Correction — ARCH-REV2-M01

Revision 2 treated expiring IntegrationUnit/global comment leases as mutation authority but could not atomically prove those generations were still current at the Git ref write. Revision 3 removes that impossible coupling.

IntegrationUnit and global lease generations remain server-time, deterministic coordination/recovery records. They still prevent duplicate preparation in the normal case and allow bounded recovery after expiry, but they are no longer represented as a credential consumed by `main` publication.

The only mutation arbiter is now an exact expected-old-ref server transaction:

```text
expected_old = A
new          = S(parent=A)
```

where `S` is the one squash commit for the immutable IntegrationUnit packet. If an expired actor and its recovery overlap continuously, both may reach publication, but at most one exact-old transaction can change `main`; the other changes zero bytes and refreshes. A unique `integration_unit_id` marker in the published commit prevents ambiguous-response or recovery paths from republishing the same unit on a later base.

Publication-relevant PolicyEpoch/schema transitions are required to be main-bound, so the same expected-old condition also catches policy authority changes rather than relying on an independently mutable comment state.

This directly closes the Issue #167 lease-liveness gap while preserving bounded stale recovery.

## Correction — ARCH-REV2-M02

Revision 3 chooses immutable terminal `H` as the sole source authority after terminalization. The source PR is a visibility/provenance surface, not a live publication input.

Consequences:

- publication materializes and integrates exact frozen `H`, never whatever the PR head happens to be later;
- later PR movement is explicitly irrelevant to publication correctness and therefore cannot create a residual read/write race;
- if exact `H` is unavailable, publication fails closed rather than falling forward to the live PR head;
- after publication, PR linkage records both `integrated_head: H` and any divergent current PR head `P`, and never claims later commits were integrated;
- post-publication PR linkage/closure failure remains a typed continuation and never causes republishing.

This removes the hybrid observational precondition found by Issue #167.

## Additional publication hardening

Current `main` now also retains parallel noncanonical architecture-review provenance from Issue #168. Revision 3 does not treat that parallel review as the routing authority for Issue #174, but it adopts the stronger safe primitive suggested by that evidence: a plain `force=false` REST ref update is not accepted as exact-base CAS.

Stage-B publication must use a server transaction that carries exact expected old object ID `A` (for example a native Git receive-pack/ref transaction with old=`A`, new=`S`) or an API with identical semantics. That transaction must reject advances, rewinds, deletion/recreation, and unrelated replacement of `main` before mutation. Normal PR merge endpoints and generic REST ref updates lacking expected-old semantics are forbidden fallbacks.

## Preserved architecture and authority boundaries

Revision 3 preserves:

- required independent scoped review and aggregate W2-REV-01 where declared;
- required verification and later canonicalization as separate gates;
- noncanonical evidence/review integration as storage only;
- negative review provenance with `acceptance_authority: NONE` and no review-of-review recursion;
- producer self-review never satisfying independent acceptance;
- immutable historical FAIL / INCONCLUSIVE / NOT_RUN / trust evidence;
- relevant compatibility drift failing closed while provably disjoint main churn may proceed;
- source/review branch immutability;
- one squash commit per eventual `main` integration;
- bounded review/remediation recursion and no authority inflation from PR existence or mergeability.

## Adversarial self-review

Revision 3 adds normative attacks for:

1. IntegrationUnit and global coordination expiry while the old actor continuously executes;
2. overlapping unrelated IntegrationUnits after global coordination recovery;
3. source PR head movement after immutable terminal H is frozen;
4. external main advance after preparation;
5. external main rewind after preparation;
6. publication-relevant PolicyEpoch transition;
7. ambiguous network result after a successful ref update;
8. PR linkage failure or a divergent live PR head after main publication.

Bounded producer self-review against the routed findings:

- `ARCH-REV2-M01`: `RESOLVED_IN_CANDIDATE`
- `ARCH-REV2-M02`: `RESOLVED_IN_CANDIDATE`
- unresolved BLOCKER: 0
- unresolved MAJOR: 0
- correction-requiring MINOR: 0

The safety argument no longer depends on an expiring comment lease being observably current at the mutation instant and no longer depends on a live PR head remaining equal to frozen H.

## Required next route

This packet remains `NONCANONICAL_ARCHITECTURE_CANDIDATE_REVISION_3`. Exactly one fresh independent/degraded-independent architecture re-review is required on the immutable terminal Issue #174 head before any canonical schema/PolicyEpoch revision, migration, verification, or activation may become eligible. The Issue #167 reviewer episode must not adjudicate its own routed remediation.

A clean future review still does not activate this candidate directly; separately scoped canonical revision/migration work must bind the actual server publication primitive, typed records, global control issue, PolicyEpoch effectiveness rule, and migration behavior before use.

## Authority boundary

No integration permission, workflow activation, canonicality, verification, readiness, production, implementation, engine selection, release, legal/provider, or merge authority is created by Issue #174. The required PR is review/provenance visibility only. Any eventual `main` integration remains separately authorized and squash-only.
