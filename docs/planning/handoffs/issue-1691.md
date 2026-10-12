# Issue #1691 — independent mandatory factory review handoff

**Mission:** `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-17-REV-01`  
**Owner CLAIM:** #6130840978, `2026-10-12T19:09:07Z`, first valid and in-lease.  
**Reviewer session:** `frontier-factory-liveness-adversarial-review-1691-gpt6-20261012-2110-cph-01`.  
**Main base:** `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. Canonical Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`.  
**Frozen producer:** #1683 terminal #6130231359, OPEN/DRAFT source PR #1690 HEAD `3d849fb1b3b7bd1d2601f152c30cb367183decfa`.  
**Prior negative predecessor:** independent #1677 terminal #6118813482, rejected source PR #1675.

## Independent review result

**CHANGES_NEEDED** — 1 BLOCKER `FSR-1691-B01`, 0 separate MAJOR, 0 correction-requiring MINOR. Source v5 terminal ownership reconstruction accepts a different intent/grant SHA than the genuine HANDOFF or STALE source head, and the base terminal issue closer delegates to it before mutating storage. A re-read of the same predicate does not authenticate the false head. Immutable evidence/report path:
`docs/planning/wave-2/reviews/factory-seeding-1683-review.md`.

Independently inspected full relevant source predicates in `tools/planning/frontier_maintenance.py`, `frontier_maintenance_v5.py` and comparison with `frontier_maintenance_v7.py`; checked hosted exact final-head PR run #38291158170 (validate #114951321601 SUCCESS, mutating #114951323791 SKIPPED); compared all 19 inherited blobs exactly with PR #1675; verified the actual #1664/#1673 terminal source identities and exact new factory successor route bindings. Ran independent **predicate-level modeled** negative witness; did not run full original source import, live maintenance, any PATCH, nor claim empirical full composed v1–v7 independent execution.

## Scope, state and continuation

Reviewer-owned files ONLY: the above report and this handoff. No gameplay, source, predecessor, PR-close, main or workflow mutation. OPEN/DRAFT reviewer-only PR to be linked on Issue #1691 terminal at exact HEAD; it must remain **unmerged**. Required single bounded remediation successor is **#1698**, blocked pending exact schema-3 terminal of this review and then independent first-winner ownership. Correction must bind handoff/stale recovery head to the authenticated source generation and reject unrelated 40-hex SHA; exercise direct real-module negative and legitimate positive fixtures, maintain 6h/600s liveness, HEAD_ADVANCE, recent pre-PATCH proof and composed v1–v7 suite, then hosted exact-final-head CI and **new genuinely distinct required security review**. A clean result still needs separately claimed, current-main compatible expected-head **squash-only NONCANONICAL** source publication.

No authorization to merge #1690 or any reviewer-only PR, run mutating --apply, automatically close stale drafts using this unreviewed source, canonize, select engine, or claim production/release authority.
