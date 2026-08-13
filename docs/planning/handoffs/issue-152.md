# Issue #152 Handoff — ARCH-CONVERGENCE-REV-01

## State

Independent/degraded-independent architecture review is complete with disposition `CHANGES_REQUIRED`: 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.

## Exact reviewed input

- Issue #154 / `ARCH-CONVERGENCE-REM-01`
- work/head `57a941f98a00f0c49b29148e2d60b6febe7fb788`
- candidate blob `d04174e22a0bb2b45de622778c0b97a53106e8df`
- PR #155 draft/open at the exact reviewed head
- producer self-review #4925034255 retained as provenance only

The candidate was immutable during this reviewer episode.

## Review findings

### `ARCH-REV-M01` — MAJOR

The proposed `MAIN_INTEGRATION_LEASE` is advisory with respect to external `main` mutations. The actual squash-merge primitive can guard the expected PR head but not the checked base SHA. If `main` advances from A to B after the final compatibility check but before the merge, GitHub may publish the squash on B; verifying the squash parent after publication detects the race only after unreviewed integration has already happened. The corrected architecture must require an atomic expected-base/CAS-equivalent publication primitive or another server-enforced pre-merge base guarantee.

### `ARCH-REV-M02` — MAJOR

The global lease and integration-owner stale recovery are not closed into a unique discoverable typed authority ledger/state machine. The revision must define one canonical global lease control surface, singleton contention key, server-time lease generation/expiry, predecessor/recovery semantics, post-acquisition winner recheck, stale recovery tie rule, release/abandon state, and corresponding typed stale/recovery transitions for IntegrationUnit ownership.

## Attacks that passed

The revision otherwise preserves required scoped and aggregate review, verification/canonicalization separation, exact-head provenance, bounded compatibility refresh, fail-closed migration of old packets without dependency refs, negative review-provenance storage without review-of-review, categorical prohibition on producer self-review satisfying scoped acceptance, historical evidence/trust immutability, bounded review/remediation recursion, noncanonical/readiness/production authority separation, and convergence-first dispatcher behavior.

## Required next action

Exactly one bounded architecture-remediation successor should revise the immutable Issue #154 candidate for `ARCH-REV-M01` and `ARCH-REV-M02`. It must not edit/re-own Issue #154 or this reviewer branch. After correction it requires one fresh independently owned architecture review before any canonical protocol/schema revision or Wave-2 migration can consume the architecture as passed.

## Authority

This review and handoff are noncanonical review provenance only. They grant no merge, integration, canonicalization, readiness, production, implementation, verification, release, or legal/provider authority. Every eventual `main` integration remains squash-only.