# Issue #145 handoff — W2-PG-REM-RIGHTS-04

## Episode identity

- mission: `W2-PG-REM-RIGHTS-04`
- issue: `#145`
- branch: `planning/issue-145`
- actor session: `w2-pg-rem-rights-04-gpt56sol-20260813-1000`
- base main: `042d140b5d2e0b951da4528e1867514983418d6f`
- ownership claim comment: `5277701964`
- reviewed remediation: Issue #142 terminal comment `5277675462`
- reviewed exact work/head: `4b61b276bb28bb114a650e003a7a5d0aeb77411a`
- reviewed exact fixture Git blob: `39fcdc292cd37661a061c6d3027715106b3a3d27`

## Review result

Independent pre-gate disposition is `CHANGES_NEEDED` with:

- BLOCKER: 0
- MAJOR: 1
- MINOR: 0
- finding: `PG-REM4-RIGHTS-M01`
- routed remediation: Issue #148 / `W2-REM-RIGHTS-05`

The finding is a derived-state fail-closed defect. The exact Issue #142 `derive_state()` code validates every `material_triggers` member against the closed domain but does not reject duplicate set-like members before `set(material_triggers)` and the final authority decision. With every requirement `REQUIRED` and every evidence state `SATISFIED`, duplicate non-quarantine triggers such as `TERMS_AMBIGUITY` or `SCOPE_AMBIGUITY` currently derive `CLEAR / ALL_REQUIRED_EVIDENCE_SATISFIED` instead of exact `UNKNOWN / POLICY_UNRESOLVED`.

The producer's 462-case malformed scalar matrix does not exercise duplicate trigger lists; it only substitutes one trigger member at a time. The 802,816 valid-domain audit cannot exercise duplicates because trigger collections are generated as unique bit-mask subsets. Both declared cardinalities independently reconcile from the exact source, but neither closes this malformed structural case.

The full review is recorded in `docs/planning/wave-2/reviews/w2-rem-rights-04-pre-gate-review.md`.

## Preserved boundaries

The review found no second BLOCKER/MAJOR in the inspected closed scalar/hash/index surface. Existing typed guards protect compiler domain scalars, record-type dispatch, authority record closed fields, requirement values, SourceEvidenceRoot kinds/IDs, and derived evidence-state values from unhashable/wrong-type use before membership or indexing. Issue #95 remains immutable parallel provenance, and Issues #129/#141/#142 remain immutable predecessor/review inputs.

Issue #148 is routing only and remains unclaimed by this reviewer episode. It must consume this review only after the terminal Issue #145 status freezes the exact review head. After #148 remediation, one fresh independent pre-gate review is required; if clean, the rights lane must proceed directly to formal `W2-REV-01` rather than spawn optional review churn.

This review grants no legal clearance, release approval, provider permission, production/readiness, implementation, integration, verification, release, merge, or canonicalization authority. Any eventual integration remains separately authorized and squash-only.

## Terminalization requirement

Before Issue #145 publishes terminal schema-3 `STATUS(REVIEW_READY)`, an open draft PR from this exact branch to `main` must exist and its head must equal terminal `head_sha`. The terminal issue capsule is authoritative for the final head, artifact blobs, and PR binding.