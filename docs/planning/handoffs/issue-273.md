# Issue #273 handoff — W2-REV-ACC-09

## Identity

- Mission: `W2-REV-ACC-09`
- Task class: required scoped accessibility review
- Branch: `planning/issue-273`
- Winning claim: Issue #273 comment `5293008919`
- Claim base: `main@ed26280a4fd409d499a7a5e50248e980ee125dba`
- Reviewer actor/session: `w2-rev-acc-09-gpt56sol-20260814-1358-frontier`
- Trust profile: `DEGRADED_SINGLE_AGENT`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

## Frozen reviewed producer

- Issue #270 terminal comment: `5292997562`
- Producer exact head: `284b9b2723f07f828202f3ce053d7eaae51e7e89`
- Producer substantive work: `1a2a97fb5561c3ec9cd1db151db18f104f2040dd`
- Producer PR: #272, draft/open/mergeable, exact head `284b9b2723f07f828202f3ce053d7eaae51e7e89`
- Producer policy v8 blob: `f1d07ef936f6187529ffc1e84d3fd2f2b4f06b96`
- Producer report v8 blob: `260abddcec26584c62a3bb213ac6e6ea0f90ad0a`
- Producer handoff blob: `c1faf3dcc92fc6610901faffde9f7f296cf2dff8`
- Immutable integrated v7 policy blob: `4cf9113bc6c4c663db360594e54b5403cc9e5588`
- Source negative review: Issue #269 terminal `5292556689`, finding `W2-REV-ACC08-M01`

## Review artifact

- `docs/planning/wave-2/reviews/w2-rem-acc-09-scoped-review.md`
- Review artifact blob: `1d1cc79741111f4adb97350916af5670fb396410`
- Substantive review work boundary: `791a3991c135a4a2d842f86242a88eaeda172a26`
- Disposition: `CHANGES_NEEDED`

## Review result

Fresh first-party XAG 112 and exact producer v8-over-v7 reconstruction found the scaled/zoomed-map correction, same-input focus-escape correction, identity/count arithmetic, preserved XAG 116 >20-hour correction, and fail-closed aggregate state clean within this bounded review.

One material defect remains:

### `W2-REV-ACC09-M01` — MAJOR / OPEN_BOUNDED

The first-party submenu obligation applies to **all submenus**. Exact v8 names this correctly in its source-recheck summary, but `XAG112-SUBMENU-PERSISTENT-RETURN-LINK` reduces the atomic contract to `trigger: submenu_exists` plus singular `persistent_return_link_present: true`. Its semantic assertion remains non-universal, and the fixture set has no partial-coverage witness where one of multiple submenus lacks the return path.

Therefore exact v8 can satisfy its declared machine-readable contract without proving every applicable submenu has a persistent return path. `CLEAN_FOR_NONCANONICAL_INTEGRATION` is unavailable for Issue #270 / PR #272.

## Routed successor

- Issue #275 / `W2-REM-ACC-09`
- Scope: only make the existing submenu record universally quantify every applicable submenu and make partial submenu coverage mechanically rejectable.
- Preserve main-menu vs initial-interactive-screen as alternatives.
- Preserve both other Issue #270 XAG 112 additions unchanged.
- Preserve XAG counts at 14 / 113 / 218 and inherited count 105.
- Preserve exact v7 XAG 116 correction and all fail-closed state.
- Fresh independent/degraded-independent scoped review remains mandatory after remediation.

Issue #275 was created blocked pending this review's terminal `CHANGES_NEEDED`; it must not be claimed before that terminal state is durably published.

## Duplicate-route note

Issue #274 was a duplicate `W2-REV-ACC-09` route created after #273. It terminalized `SUPERSEDED` without a branch, claim, or substantive work after recognizing #273 as the earlier valid route. Do not use #274 as review authority.

## Preserved aggregate state

```yaml
review_disposition: CHANGES_NEEDED
blockers: 0
majors: 1
correction_requiring_minors: 0
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
producer_integration_eligible: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authority_created: false
canonicality: NOT_CANONICAL
```

## Required next

1. Open and bind an exact-head draft PR for this review provenance.
2. Publish terminal schema-3 `STATUS(REVIEW_READY)` on Issue #273 with exact review/handoff blobs, exact PR head, finding `W2-REV-ACC09-M01`, disposition `CHANGES_NEEDED`, and successor #275.
3. Do not integrate producer PR #272 on the basis of this review.
4. After terminalization, Issue #275 becomes the blocking-remediation continuation if unowned and otherwise eligible.
5. Even after a future clean bounded fix, a fresh full corrected XAG 108–123 review remains required for untouched XAG 113–123 before any empirical accessibility successor.

This review creates noncanonical negative review provenance only. It grants no empirical accessibility PASS, mapping completion, full corrected-mapping acceptance, implementation/readiness/release authority, legal/compliance status, platform certification, verification PASS, integration authority, decision authority, or canonical authority.