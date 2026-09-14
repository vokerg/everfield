# Required Review — FACTORY-CONVERGENCE-06-REM-02

## Disposition

`CHANGES_NEEDED`

Trust mode: `DEGRADED_SINGLE_AGENT`.

Judged immutable packet: Issue #1116 terminal `5659634282`, PR #1117, exact head `a6e173649909fa9fee679916d882f7ed0ab0ffc8`, corrected v5 blob `477bc36ea788867cf2744f4f9b9ccfb161c875b6`.

## Scope and evidence

The review inspected the exact #1116 v5 source and the canonical schema-3 ownership rules. The candidate correctly improves two cases from #1114: losing later duplicate CLAIM/RECOVER contenders do not automatically replace a winning owner, and a syntactically reconstructed later recovery can supersede an earlier owner. The frozen v3 route classifier and the two-path remediation scope are not changed by #1116.

No full patched v1→v5 execution PASS is claimed. Exact-new-main push-triggered workflow acceptance remains mandatory after any later clean publication.

## Finding

### FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01 — reconstructed RECOVER validity omits stale/orphan temporal predicates

Severity: **MAJOR**.

`terminal_owner_generation_is_current()` reconstructs a `RECOVER` winner from trusted operational records, but for `recovery_reason: STALE` it checks only source linkage, previous-owner linkage, winning intent identity, actor/head tuple, and ordering. It never proves the prior ownership lease actually expired before the stale recovery. For `ORPHAN`, it checks an `ORPHAN_PROBE` source but never proves the canonical ten-minute server-time maturity predicate.

Canonical Planning Program v1 requires stale-owner recovery only after lease expiry and orphan recovery only after a mature orphan probe. Unknown/wrong predecessor or losing contention records have zero authority effect. Therefore the new liveness consumer can treat a schema-3-invalid premature `RECOVER` as the winning ownership generation. That can reject a still-valid prior owner's terminal or consume a terminal authored by an invalid recovery generation, reintroducing incorrect liveness suppression rather than merely failing closed.

This is correction-requiring and blocks the allowed clean-integration disposition.

## Required remediation

1. Reconstruct recovery ownership only from grants satisfying the canonical temporal validity predicates: STALE must prove lease expiry at the relevant GitHub server-time boundary; ORPHAN must prove the required probe maturity interval.
2. Preserve the #1116 winning-intent, actor/head/source, current-generation, first-valid-grant, losing-contender, HANDOFF, and predecessor-shape checks.
3. Add deterministic negative controls for premature STALE recovery and premature ORPHAN recovery; neither may supersede the current/no-owner state or make its terminal consumable.
4. Preserve existing positive controls for valid mature recovery, losing duplicate CLAIM/RECOVER, stale prior-owner rejection, no-route classification, exact-generation isolation, semantic composition, and authority boundaries.
5. Route one fresh required degraded-independent review of the corrected exact packet. Do not claim full patched v1→v5 execution unless actually run.

## Finding counts

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0

## Authority boundary

`NOT_CANONICAL`. Review provenance only. No integration, verification-PASS, implementation-readiness, engine-selection, release, decision, or canonical authority.
