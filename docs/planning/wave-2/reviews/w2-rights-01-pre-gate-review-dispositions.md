# W2-REM-RIGHTS-01 — Pre-gate finding dispositions

**Remediation issue:** #95 / `W2-REM-RIGHTS-01`  
**Source producer:** #80 / `W2-RIGHTS-01`  
**Source work/head:** `3c262cbf767633e0ca42f6bdf387e262056b4fb0`  
**Source report blob:** `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**Producer terminal status:** `5270525266`  
**Independent pre-gate review:** `5271490456`  
**Corrected report blob:** `06e04f7d707b9694f58fbe9c534bc7a99f5ed14e`  
**Machine-readable policy blob:** `db2eb5fe36be4ac7ed0204832a3537db0f97e1df`  
**Authority:** noncanonical bounded remediation; formal `W2-REV-01` remains required.

## Disposition summary

| Finding | Severity | Disposition | Corrected evidence |
|---|---:|---|---|
| `PG-RIGHTS-M01` | MAJOR | ACCEPTED / CORRECTED | acyclic `ReferenceUseContextRecord -> OriginalityReviewRecord -> ReferenceUseRecord`; final record binds exact pre-review purpose/reuse/rights context plus exact review and is consumed by release assessment |
| `PG-RIGHTS-M02` | MAJOR | ACCEPTED / CORRECTED | exact `ORP-RISK-v1` compiles `REQUIRED | CONDITIONAL | NOT_APPLICABLE` originality evidence before assessment; unknown/unmatched/unknown conditional trigger fails closed; output binds exact check plan/evidence requirement |
| `PG-RIGHTS-m01` | MINOR | ACCEPTED / CORRECTED | deterministic `RESTRICTED > QUARANTINED > UNKNOWN > CLEAR` precedence; stale evidence alone -> `UNKNOWN(STALE_REQUIRED_EVIDENCE)`; prior assessment retained; independent stronger triggers retain their higher state |

## PG-RIGHTS-M01

### Finding

Wave-1 §18 requires originality/reference-use records to bind candidate `ArtifactIdentity`, reference purpose, allowed/prohibited reuse, similarity/adversarial evidence, and current rights/terms research. The frozen Issue #80 `OriginalityReviewRecord` did not bind purpose/reuse/current-rights context, leaving a reuse/alias gap across materially different reference-use scopes.

### Correction

Policy blob `db2eb5fe36be4ac7ed0204832a3537db0f97e1df` uses an acyclic three-stage construction:

1. `ReferenceUseContextRecord` is content-addressed **before review** over candidate/reference identities, origin/reference class, purpose, allowed/prohibited reuse, provider/license/current-rights evidence, exact release scope, policy/evidence requirement, and freshness refs.
2. `OriginalityReviewRecord` binds that exact context plus its compiled check/evidence identities and results.
3. After the review identity exists, final `ReferenceUseRecord` is content-addressed over `context_ref + originality_review_ref`. `ReleaseRightsAssessment` consumes this final identity.

Changing any context field requires a new context, review, and final reference-use identity. Changing the review also changes the final identity. The review does **not** point back to the final record, so the identities are mechanically constructible rather than circular.

A bounded `LicenseOrPermissionRecord` minimum shape is also defined so license/permission refs have exact authority source, version/grant date, allowed/prohibited uses, obligations, scope, recheck, and immutable evidence.

### Mechanical checks

- `SC-R00`: context -> review -> final record constructs acyclic identities.
- `SC-R01`: changed reference purpose -> reject reuse; new context/review/final record required.
- `SC-R02`: changed release scope -> reject reuse; new context/review/final record required.
- `SC-R08`: low similarity score + missing license -> no `CLEAR`.

**Disposition:** corrected; no residual MAJOR in remediation scope.

## PG-RIGHTS-M02

### Finding

The source candidate said originality review was “optional/required by risk policy” but did not identify/version that policy or define deterministic applicability. That allowed release-time discretion outside the canonical requirement -> plan -> evidence -> satisfaction chain.

### Correction

Policy blob `db2eb5fe36be4ac7ed0204832a3537db0f97e1df` defines `ORP-RISK-v1` with explicit evidence kinds, reference/origin-class rules, conditional triggers, and compilation semantics. Applicability is resolved before originality execution/release assessment.

Fail-closed cases are explicit:

- missing policy -> `UNKNOWN_POLICY`;
- unknown origin/reference class -> `UNKNOWN_POLICY`;
- missing exact release scope for release-sensitive use -> `UNKNOWN_POLICY`;
- no matching rule -> `UNKNOWN_POLICY`;
- unknown conditional-trigger truth -> treat as `REQUIRED`.

When multiple rules apply, `REQUIRED > CONDITIONAL > NOT_APPLICABLE` wins per evidence kind. The generated `OriginalityCheckPlan` binds policy, exact evidence requirement, candidate, exact context, scope, applicable rule IDs, applicability results, and conditional-trigger resolutions. `NOT_APPLICABLE` is decided before execution; `NOT_RUN` remains an unsatisfied execution result.

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

## Producer self-review correction inside remediation

An initial remediation draft made the final `ReferenceUseRecord` content-address over `originality_review_ref` while also making the review point to that final record. Cold self-review identified the hash-identity cycle before handoff. The corrected policy/report now use the acyclic context -> review -> final record sequence and add `SC-R00` explicitly. The superseded draft blobs are branch history only and are not acceptance evidence.

## Source recheck

The remediation independently rechecked the producer's load-bearing current first-party OpenAI, GitHub, and U.S. Copyright Office source claims on 2026-08-12 before preserving them. No material source drift requiring a changed policy conclusion was found. Exact account/product/contract applicability remains conditional and must be captured per generation/storage epoch; this task does not establish Everfield legal clearance.

## Residual authority and downstream routing

This remediation supersedes Issue #80 only as the substantive corrected W2-RIGHTS-01 input for later `W2-REV-01`. Issue #80 remains immutable provenance. No formal independent `REVIEW_STATUS`, release decision, implementation-readiness transition, or canonicalization is claimed here.

**Remediation finding count after correction:** 0 BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR.
