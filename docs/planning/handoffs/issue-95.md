# Issue #95 handoff — W2-REM-RIGHTS-01

**Mission:** `W2-REM-RIGHTS-01`  
**Issue:** #95  
**Branch:** `planning/issue-95`  
**Ownership generation:** Issue #95 comment `5271504458`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Source mission:** Issue #80 / `W2-RIGHTS-01`  
**Source work/head:** `3c262cbf767633e0ca42f6bdf387e262056b4fb0`  
**Source report blob:** `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**Source handoff blob:** `a5a9158f6bdf2164c3b848b9c1b7bcb15d165f81`  
**Source terminal status:** Issue #80 comment `5270525266`  
**Independent pre-gate review:** Issue #80 comment `5271490456`  
**Corrected report:** `docs/planning/wave-2/research/originality-rights-and-terms.md` blob `06e04f7d707b9694f58fbe9c534bc7a99f5ed14e`  
**Machine policy:** `docs/planning/wave-2/research/originality-rights-policy.yaml` blob `db2eb5fe36be4ac7ed0204832a3537db0f97e1df`  
**Finding dispositions:** `docs/planning/wave-2/reviews/w2-rights-01-pre-gate-review-dispositions.md` blob `1382500e19ab7e374f065df71248f1b15d47f007`  
**Required formal review:** `W2-REV-01`  
**Authority:** noncanonical `PLANNING_REVISION / EVIDENCE_REQUIRED`.

## Why this remediation exists

Independent pre-gate review of the immutable Issue #80 producer candidate found 0 BLOCKER / 2 MAJOR / 1 MINOR:

1. `PG-RIGHTS-M01` — the producer's originality record did not mechanically bind the Wave-1-required reference purpose, allowed/prohibited reuse, and exact current rights/terms context, permitting potential reuse across materially different reference/permission scopes.
2. `PG-RIGHTS-M02` — originality-review applicability was delegated to an undefined “risk policy,” so required evidence could differ by implementation/release-time discretion instead of compiling through the canonical evidence chain.
3. `PG-RIGHTS-m01` — stale required provider/legal evidence could derive either `UNKNOWN` or `QUARANTINED` with no deterministic precedence.

Issue #80 remains frozen and unchanged. This issue recreates only the corrected noncanonical payload.

## Completed corrections

### Exact, acyclic reference-use authority

The corrected policy uses a mechanically constructible three-stage identity chain:

```text
ReferenceUseContextRecord
  -> OriginalityReviewRecord
  -> ReferenceUseRecord
  -> ReleaseRightsAssessment
```

`ReferenceUseContextRecord` is content-addressed before review over candidate/reference identities, origin/reference class, purpose, allowed/prohibited reuse, provider/license/current-rights refs, exact release scope, policy/evidence requirement, and freshness refs.

`OriginalityReviewRecord` binds that exact context and the exact compiled evidence/check/result identity. After the review exists, the final `ReferenceUseRecord` is content-addressed over `context_ref + originality_review_ref`; release assessment consumes that final identity. Changing purpose, reuse permission, evidence, scope, or review therefore creates a new final identity.

A `LicenseOrPermissionRecord` minimum evidence shape is also defined so missing/ambiguous permission or unsatisfied obligations cannot support `CLEAR`.

### Deterministic originality applicability

`ORP-RISK-v1` compiles these evidence kinds to `REQUIRED | CONDITIONAL | NOT_APPLICABLE` before execution/assessment:

- exact identity;
- normalized identity;
- known-reference comparison;
- near-duplicate evidence;
- targeted external search;
- judgment review; and
- qualified legal review.

Missing policy, unknown origin/reference class, missing release scope, or no matching rule yields `UNKNOWN_POLICY`. An unresolved conditional trigger is treated as `REQUIRED`. Per evidence kind, `REQUIRED > CONDITIONAL > NOT_APPLICABLE`. `NOT_RUN` remains an execution result and cannot alias `NOT_APPLICABLE`.

Rules are bounded by origin/reference class so direct third-party assets depend on exact license authority rather than similarity scores, confidential/restricted material remains restricted absent exact authority, named-style/expression-specific references receive stronger evidence, and public-domain claims require exact basis/jurisdiction rather than age/public visibility shortcuts.

### Deterministic state derivation

Release-sensitive state precedence is:

```text
RESTRICTED > QUARANTINED > UNKNOWN > CLEAR
```

- known scope/prohibited-use/permission-limit facts -> `RESTRICTED`;
- unresolved material conflicts/risks -> `QUARANTINED`;
- stale/missing/incomplete/unknown required evidence or unsatisfied required originality evidence -> `UNKNOWN`;
- `CLEAR` only if no higher-precedence condition matches and all required evidence/freshness/obligations are satisfied.

Stale required evidence alone is exactly `UNKNOWN(STALE_REQUIRED_EVIDENCE)`. Historical prior assessment remains retained; a separate stronger active conflict can still yield `QUARANTINED`, and a known explicit scope restriction can yield `RESTRICTED`.

## Current-source recheck

The remediation independently rechecked the producer's load-bearing current first-party OpenAI, GitHub, and U.S. Copyright Office sources on 2026-08-12 before preserving their normalized facts. No material drift requiring a different planning-policy conclusion was found.

The corrected report remains deliberately conditional: it does not establish which OpenAI/GitHub account/customer contract governs any future Everfield release-content episode, does not infer legal clearance from provider output allocation, and does not generalize the U.S.-specific Copyright Office research into a global copyright conclusion.

## Self-review correction before handoff

Cold producer self-review found and corrected one defect in an intermediate remediation draft: the first model content-addressed the final `ReferenceUseRecord` over an originality review that itself pointed back to the same final record, creating a hash-identity cycle.

The final payload rejects that construction. It uses the acyclic context -> review -> final-record sequence above and includes explicit self-check `SC-R00`. Superseded intermediate draft blobs remain only as branch history and are **not** acceptance evidence.

## Mechanical self-checks

Final machine policy includes:

- `SC-R00` context -> review -> final record is acyclic;
- `SC-R01` changed reference purpose requires new context/review/final record;
- `SC-R02` changed release scope requires new context/review/final record;
- `SC-R03` no matching policy rule -> unknown policy, no clear;
- `SC-R04` unresolved conditional trigger -> required;
- `SC-R05` stale terms only after prior clear -> unknown + stale reason + prior assessment retained;
- `SC-R06` stale terms + material-similarity conflict -> quarantined with both facts retained;
- `SC-R07` explicit license-scope restriction -> restricted;
- `SC-R08` low similarity score + missing license -> no clear.

These are policy conformance cases, not evidence that a future implementation has been built or verified.

## Final self-review against Issue #95

- source candidate/status/review provenance exact: **PASS**;
- `PG-RIGHTS-M01` corrected with exact acyclic reference-use binding: **PASS**;
- `PG-RIGHTS-M02` corrected with exact precompiled applicability policy: **PASS**;
- `PG-RIGHTS-m01` corrected with reason-coded deterministic state precedence: **PASS**;
- required evidence remains in requirement -> check-plan -> evidence -> satisfaction chain: **PASS**;
- retained artifacts continue to use Wave-1 `ArtifactIdentity`: **PASS**;
- current-source claims remain bounded/conditional and freshness-sensitive: **PASS**;
- provider assignment/similarity/public visibility shortcuts cannot clear release: **PASS**;
- no unsupported legal conclusion: **PASS**;
- no release, implementation-readiness, or canonicalization authority claimed: **PASS**;
- formal independent review remains `W2-REV-01`: **PASS**;
- unresolved BLOCKER: **0**;
- unresolved MAJOR: **0**;
- correction-requiring MINOR: **0**.

## Remaining open questions

The exact provider/account contract for future generation episodes, actual third-party licenses and obligations, calibrated media-specific similarity mechanisms, artifact/scope triggers requiring qualified legal interpretation, target jurisdictions/storefronts, protected handling for confidential licenses/legal analysis, and formal aggregate Wave-2 review remain open by design.

## Downstream routing

After a clean cold branch review and exact terminal `STATUS(REVIEW_READY)`, this corrected payload should supersede the frozen Issue #80 producer payload as the substantive `W2-RIGHTS-01` input for later `W2-REV-01`, while Issue #80 remains immutable historical provenance.

This handoff does **not** authorize a PR merge or `main` integration. Any eventual `main` integration remains squash-only and requires the repository's declared review/verification/integration authority. This remediation itself creates no legal/release/implementation-readiness/canonicalization authority.
