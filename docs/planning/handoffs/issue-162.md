# Issue #162 handoff — W2-REM-RIGHTS-06

## State

Bounded remediation for Issue #159 finding `PG-REM5-RIGHTS-M01`.

The Issue #148 duplicate-trigger semantic correction is preserved unchanged. The only correction is evidence reconstructability: the exact Issue #142 predecessor fixture is now retained in the resulting tree and loaded by adjacent path rather than by task-branch Git-object reachability.

## Exact inputs

- current base main: `373cdafef7825455f50993f67b5220c08b0e774e`
- Issue #148 exact head/work: `91545c6121a3cf071df524fd17e5e2978f7a65b2`
- Issue #159 terminal review head/work: `34bd6004ae0940f35a6bc647aab82d80ba5101a0`
- Issue #159 finding: `PG-REM5-RIGHTS-M01`
- Issue #142 predecessor fixture Git blob: `39fcdc292cd37661a061c6d3027715106b3a3d27`
- Issue #142 predecessor exact-byte SHA-256: `6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5`

## Resulting packet

- `docs/planning/wave-2/evidence/originality-rights-policy-fixtures.py`
- `docs/planning/wave-2/evidence/originality-rights-policy-fixtures-predecessor-issue-142.py`
- `docs/planning/wave-2/research/originality-rights-and-terms.md`
- `docs/planning/wave-2/reviews/w2-rem-rights-04-pre-gate-review-dispositions.md`
- `docs/planning/handoffs/issue-162.md`

Corrected wrapper pre-commit identity:
- Git blob `441a17ba2ea19681bf87439f6d4f252e2e21cd9e`
- SHA-256 `09a823d975ecd677bd4eaad162287d539781b05d7e8950d04932f593ed03e71d`

The retained predecessor path must resolve to exact Git blob `39fcdc292cd37661a061c6d3027715106b3a3d27`.

## Producer self-review

- `PG-REM5-RIGHTS-M01`: `RESOLVED`
- unresolved BLOCKER: `0`
- unresolved MAJOR: `0`
- correction-requiring MINOR: `0`

The computational tail after loading the predecessor bytes is byte-identical to Issue #148. The correction does not alter T01–T16, the 468 malformed/structural cases, duplicate-trigger fail-closed semantics, stale/quarantine precedence, or the 802,816-tuple valid-domain audit.

## Next required action

One fresh independently owned pre-gate review is mandatory on the exact terminal Issue #162 head. It must verify the retained predecessor path/blob/byte SHA, execute from a fresh main-only style checkout without hidden refs, reproduce the deterministic evidence, and attack for scope or authority leakage. A clean result proceeds to formal `W2-REV-01`; optional review churn is not authorized.

This handoff grants no legal/release/readiness/implementation/integration/verification/canonicalization authority. Any eventual `main` integration is separately authorized and squash-only.
