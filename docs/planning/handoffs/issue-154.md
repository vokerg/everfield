# Issue #154 Handoff — ARCH-CONVERGENCE-REM-01

## State

Producer remediation is complete and ready for independent architecture review once the exact-head draft PR is open.

## Source

- superseded-for-review candidate: Issue #150 / PR #151 head `87eda58762af6dc2235b4f7a04f5d47286fc3b0c`
- producer self-review on PR #151: review `4924996821`

## Findings closed

- `ARCH-SR-M01` — replaced informal integration route with mandatory derived `IntegrationUnit`, separate integration ownership namespace, exact contention key, `INTEGRATION_CLAIM`, loser-aborts, and no source-branch mutation authority.
- `ARCH-SR-M02` — added explicit disjoint-main compatibility predicate plus a short-lived global `MAIN_INTEGRATION_LEASE` around current-main compatibility check and squash merge.
- `ARCH-SR-M03` — added `NONCANONICAL_REVIEW_PROVENANCE` so terminal review PRs can themselves drain to `main` as provenance without recursive review-of-review or acceptance authority.
- `ARCH-SR-M04` — producer self-review is now categorically forbidden from satisfying independent scoped acceptance; any raw producer provenance policy must use a distinct provenance-only class with `acceptance_authority: NONE`.

## Preserved invariants

- aggregate review remains required for governed cross-domain synthesis/readiness/decision scopes;
- verification/canonicalization gates are not bypassed;
- historical evidence is not rewritten by migration;
- all main integration remains squash-only;
- noncanonical integration never grants production/readiness/canonical authority;
- task and integration claim races both require post-attempt winner verification.

## Required next action

Independently review the revised exact candidate. The review must attack IntegrationUnit liveness, global integration-lease recovery/TOCTOU, disjoint compatibility correctness, review-provenance authority leakage, PolicyEpoch migration, recursion bounds, and preservation of aggregate/canonical gates.

## Canonicality

This revision remains NONCANONICAL. Neither this handoff nor its PR grants integration/canonicalization authority.