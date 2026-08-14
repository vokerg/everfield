# Issue #306 handoff — W2-REV-ACC-18

## Episode

- Mission: `W2-REV-ACC-18`
- Task class: required scoped review
- Trust mode: `DEGRADED_INDEPENDENT`
- Winning claim: `5296759413`
- Branch: `planning/issue-306`
- Base: `e167931debe6e6fd0bdfc497cb7058644ea5d5d4`
- Review work commit: `8e95ed5a2d6efa4f84689c23f6b748c1dbe84c69`
- Review artifact: `docs/planning/wave-2/reviews/w2-rem-acc-18-scoped-review.md`
- Producer issue: #303 / `W2-REM-ACC-14`
- Producer terminal: `5296754811`
- Producer head: `09f4f3eee194b7ffa57b668db63421c8397a15b5`
- Producer work: `edd2de28df9c246066dd9db5e6b436d635157ef4`
- Producer PR: #305
- Candidate policy v13 blob: `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`
- Candidate report v13 blob: `e5f1f491a91499bef96861d2878e4fb5552a207b`

## Review disposition

`CLEAN_FOR_NONCANONICAL_INTEGRATION`

Findings in exact scoped remediation review:

```yaml
blockers: 0
majors: 0
correction_requiring_minors: 0
source_finding: W2-REV-ACC17-M01
source_finding_state: RESOLVED_BOUNDED
```

The exact v13 producer packet restores only `XAG117-CAMERA-VIEW-CHOICE` from advisory `BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE / CONSIDER` to repository-native source-faithful `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD` while preserving identity, conditional applicability, trigger, semantic payload, evidence/gap routing, sibling records, reviewed correction lineage, and inventory counts.

## Independent source evidence

Fresh first-party read on `2026-08-14`:

- `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117`
- `https://learn.microsoft.com/en-us/xbox/accessibility/guidelines`

The camera-view-choice directive remains an unqualified Implementation-guideline bullet. The XAG collection remains best-practice guidance and explicitly not a legal/compliance checklist. This supports `SHOULD` / required-if-applicable best-practice authority and rejects both advisory-only weakening and `MUST`/compliance inflation.

## Mechanical evidence

- PR #305 exact producer head: `09f4f3eee194b7ffa57b668db63421c8397a15b5`.
- PR #305 reports mergeable against current main during review.
- Current-main policy/report remain exact v12 input blobs `4c10dc8969a8080a14e8f46e0d2e126bd8a1ee5e` / `197a20ec3fd3cd859c4e7d96e51f7337ea7583d3`.
- Exact compare from current main to producer head changes only the declared producer policy, report, and Issue #303 handoff files.
- Inherited XAG 108–123 origin blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` contains the advisory target atom and sibling `REQUIRED_IF_APPLICABLE / SHOULD` XAG 117 camera directives.
- Validator v13 rejects advisory regression, mixed authority/modality drift, `MUST`/compliance inflation, target identity/trigger/applicability/semantic/evidence/gap mutation, unrelated-record mutation, and regression of reviewed XAG 112/XAG 114/XAG 115/XAG 116 corrections.
- Inventory assertions remain XAG112 `14`, XAG114 `16`, XAG108–123 `113`, inherited XAG101–107 `105`, composed XAG101–123 `218`.

## Authority boundary

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_118_123_accepted: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized_by_review_alone: false
decision_authority: false
canonicality: NOT_CANONICAL
```

This review is required review provenance only. A clean disposition permits exact producer #303/#305 to be considered by the separately authorized squash-only noncanonical integration route; it does not itself grant merge authority. Full review must later resume at XAG 118–123 before empirical accessibility can become eligible.

## Next transition

Open an exact-head draft PR containing only this review artifact and handoff, verify head/base and two-file scope, then publish terminal schema-3 `STATUS(REVIEW_READY)` on Issue #306. After terminalization, integration of producer and review provenance remains a separate owner-authorized convergence task.
