# W2-REM-RIGHTS-01 — Pre-gate finding dispositions

**Remediation issue:** #95 / `W2-REM-RIGHTS-01`  
**Source producer:** #80 / `W2-RIGHTS-01`  
**Source work/head:** `3c262cbf767633e0ca42f6bdf387e262056b4fb0`  
**Source report blob:** `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**Producer terminal status:** `5270525266`  
**Independent pre-gate review:** `5271490456`  
**Corrected report blob:** `11d34de5859ad85d7df825590eab9dd51b00c6f7`  
**Machine-readable policy blob:** `aaee1e14ee6d5a2ca55447e56611f0bfc58e8de6`  
**Authority:** noncanonical bounded remediation; formal `W2-REV-01` remains required.

## Disposition summary

| Finding | Severity | Disposition | Corrected evidence |
|---|---:|---|---|
| `PG-RIGHTS-M01` | MAJOR | ACCEPTED / CORRECTED | exact `ReferenceUseRecord` identity binds candidate/reference identities, purpose, allowed/prohibited reuse, provider/license/current-rights evidence, release scope, policy/requirement, originality review, and freshness; `OriginalityReviewRecord` + `ReleaseRightsAssessment` consume it |
| `PG-RIGHTS-M02` | MAJOR | ACCEPTED / CORRECTED | exact `ORP-RISK-v1` compiles `REQUIRED | CONDITIONAL | NOT_APPLICABLE` originality evidence before assessment; unknown/unmatched/unknown conditional trigger fails closed; output binds an exact check plan/evidence requirement |
| `PG-RIGHTS-m01` | MINOR | ACCEPTED / CORRECTED | deterministic `RESTRICTED > QUARANTINED > UNKNOWN > CLEAR` precedence; stale evidence alone -> `UNKNOWN(STALE_REQUIRED_EVIDENCE)`; prior assessment retained; independent stronger triggers retain their higher state |

## PG-RIGHTS-M01

### Finding

Wave-1 §18 requires originality/reference-use records to bind candidate `ArtifactIdentity`, reference purpose, allowed/prohibited reuse, similarity/adversarial evidence, and current rights/terms research. The frozen Issue #80 `OriginalityReviewRecord` did not bind purpose/reuse/current-rights context, leaving a reuse/alias gap across materially different reference-use scopes.

### Correction

Policy blob `aaee1e14ee6d5a2ca55447e56611f0bfc58e8de6` introduces `ReferenceUseRecord` with a content-addressed identity over all authority-bearing fields. A change to candidate/reference identity, purpose, allowed/prohibited reuse, provider/license/current-rights evidence, release scope, risk policy, evidence requirement, originality review, or freshness refs requires a new record identity.

The corrected `OriginalityReviewRecord` includes `reference_use_record_ref`, and the corrected `ReleaseRightsAssessment` consumes `reference_use_record_refs`. Thus an originality result cannot be mechanically transplanted from factual research to direct incorporation, from one permission set to another, or from one release scope to another merely because candidate bytes are unchanged.

A bounded `LicenseOrPermissionRecord` minimum shape is also defined so license/permission refs have exact authority source, version/grant date, allowed/prohibited uses, obligations, scope, recheck, and immutable evidence.

### Mechanical checks

- `SC-R01`: same originality result + changed reference purpose -> reject reuse; new `ReferenceUseRecord` required.
- `SC-R02`: same originality result + changed release scope -> reject reuse; new `ReferenceUseRecord` required.
- `SC-R08`: low similarity score + missing license -> no `CLEAR`.

**Disposition:** corrected; no residual MAJOR in remediation scope.

## PG-RIGHTS-M02

### Finding

The source candidate said originality review was “optional/required by risk policy” but did not identify/version that policy or define deterministic applicability. That allowed release-time discretion outside the canonical requirement -> plan -> evidence -> satisfaction chain.

### Correction

Policy blob `aaee1e14ee6d5a2ca55447e56611f0bfc58e8de6` defines `ORP-RISK-v1` with explicit evidence kinds, reference/origin-class rules, conditional triggers, and compilation semantics. Applicability is resolved before originality execution/release assessment.

Fail-closed cases are explicit:

- missing policy -> `UNKNOWN_POLICY`;
- unknown origin/reference class -> `UNKNOWN_POLICY`;
- missing exact release scope for release-sensitive use -> `UNKNOWN_POLICY`;
- no matching rule -> `UNKNOWN_POLICY`;
- unknown conditional-trigger truth -> treat as `REQUIRED`.

When multiple rules apply, `REQUIRED > CONDITIONAL > NOT_APPLICABLE` wins per evidence kind. The generated `OriginalityCheckPlan` binds policy, exact evidence requirement, candidate, reference-use record, scope, applicable rule IDs, applicability results, and conditional-trigger resolutions. `NOT_APPLICABLE` is decided before execution; `NOT_RUN` remains an unsatisfied execution result.

The policy keeps tool/algorithm selection and qualified legal interpretation conditional where appropriate; it does not turn a planning policy into a legal oracle.

### Mechanical checks

- `SC-R03`: no matching rule -> `UNKNOWN_POLICY_AND_NO_CLEAR`.
- `SC-R04`: unresolved conditional trigger -> `REQUIRED`.

**Disposition:** corrected; no residual MAJOR in remediation scope.

## PG-RIGHTS-m01

### Finding

The source candidate had stale required provider/legal evidence as both a mandatory `UNKNOWN` and mandatory `QUARANTINED` trigger without deterministic precedence.

### Correction

The policy defines reason-coded state precedence:

1. `RESTRICTED` for known scope/prohibited-use/permission-limit facts;
2. `QUARANTINED` for active unresolved material conflicts/risks;
3. `UNKNOWN` for stale/missing/incomplete/unknown evidence or policy and unsatisfied required originality evidence;
4. `CLEAR` only if no higher state matches and all required evidence is satisfied/current.

Stale evidence alone is exactly `UNKNOWN(STALE_REQUIRED_EVIDENCE)`. Historical `CLEAR` is retained by `prior_assessment_ref`; it is not rewritten. A separate active material-similarity/conflict trigger yields `QUARANTINED`, retaining the stale-evidence fact; an explicit narrower permission can yield `RESTRICTED`.

### Mechanical checks

- `SC-R05`: stale terms only after prior clear -> `UNKNOWN` + stale reason + prior assessment retained.
- `SC-R06`: stale terms + material-similarity conflict -> `QUARANTINED`, both facts retained.
- `SC-R07`: explicit license-scope restriction -> `RESTRICTED`.

**Disposition:** corrected; no correction-requiring MINOR remains in remediation scope.

## Source recheck

The remediation independently rechecked the producer's load-bearing current first-party OpenAI, GitHub, and U.S. Copyright Office source claims on 2026-08-12 before preserving them. No material source drift requiring a changed policy conclusion was found. Exact account/product/contract applicability remains conditional and must be captured per generation/storage epoch; this task does not establish Everfield legal clearance.

## Residual authority and downstream routing

This remediation supersedes Issue #80 only as the substantive corrected W2-RIGHTS-01 input for later `W2-REV-01`. Issue #80 remains immutable provenance. No formal independent `REVIEW_STATUS`, release decision, implementation-readiness transition, or canonicalization is claimed here.

**Remediation finding count after correction:** 0 BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR.
