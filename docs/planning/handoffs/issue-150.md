# Issue #150 Handoff — ARCH-CONVERGENCE-01

## State

Architecture repair candidate is producer-complete and ready for independent review after the mandatory draft PR is opened at the exact terminal branch head.

## Produced

- `docs/planning/architecture/FRONTIER-CONVERGENCE-AMENDMENT-v1.md`

## What the candidate changes conceptually

- separates scoped review authority, noncanonical integration eligibility, and later canonical/readiness authority;
- prevents aggregate cross-domain review from implicitly becoming an unrelated evidence-storage mega-gate;
- defines `INTEGRATION_READY_NONCANONICAL` / `INTEGRATED_NONCANONICAL` semantics;
- moves convergence work ahead of optional graph-expanding review/new-task creation without bypassing required review or verification;
- bounds scoped review/remediation recursion;
- requires a new PolicyEpoch/migration compiler for existing Wave-2 work instead of rewriting historical evidence;
- defines post-claim re-read/loser-aborts behavior for contention races;
- preserves squash-only integration, exact-head provenance, independent review, aggregate review for governed decisions, and canonical verification.

## Deliberately not changed

- no edit to canonical `docs/planning/PLANNING-PROGRAM-v1.md`;
- no edit to canonical binding;
- no current Wave-2 evidence/result is upgraded;
- no existing PR is granted merge authority;
- no implementation/readiness/engine/canonical decision is authorized.

## Required next action

Independent architecture review must attack the candidate before any canonical protocol/schema revision or Wave-2 migration is activated. Review should specifically test review-bypass risk, stale-base integration, policy-epoch downgrade attacks, scope ambiguity, recursion loopholes, aggregate-review preservation, and schema-3 contention compatibility.

## Integration/canonicality

This branch/PR is review/provenance visibility only. Any eventual `main` integration is squash-only and follows the separately valid architecture-review/canonicalization route. The candidate remains NONCANONICAL until that route succeeds.
