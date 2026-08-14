# W2-REM-ACC-07 — restore XAG 116 default-over-20-hours exemption

**Mission:** `W2-REM-ACC-07` / Issue #264  
**Winning claim:** comment `5291862878`  
**Claim base:** `main@6eacb5b81e414686028e5a50c9250a0b80a16c94`  
**Source review:** Issue #262 terminal `CHANGES_NEEDED` comment `5290467457`, head `1992c8b65fcc45d19cf951f0265fd5272a32d315`, work `508689bcfb6172bbd46b6aa5edbe60f16f0da9b4`  
**Finding:** `W2-REV-ACC06-M01` / MAJOR  
**Immutable reviewed producer:** Issue #259 terminal comment `5290417804`, head `b8553ac83dd11193ad1f57f8b552827768ba3338`, work `14dee0852546eec43677312ce3066b811533df61`  
**Immutable v6 policy blob:** `80e278315d6b7a108d89da3f5a99086a8ef91bf7`  
**Immutable v6 report blob:** `ec901acaf36ed4d398b127eac058537e6387a92e`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope

Issue #262 independently reproduced one material source-fidelity defect in the exact Issue #259 packet. Microsoft XAG 116 provides an exception block for content-imposed time limits and explicitly includes the case where the default time limit exceeds 20 hours. Exact v6 models the other duration-modification exceptions but contains no `default_time_limit_exceeds_20_hours` predicate anywhere, while its validator can still report PASS.

This remediation uses exact v6 policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` as an immutable logical input. It replaces only the two XAG 116 records in v6 that already carry the source exception block and extends only the validator assertions/fixtures needed to make omission or inversion of the >20-hour exception rejectable.

No unrelated XAG 108–123 or inherited XAG 101–107 record is rewritten.

## 2. Fresh first-party source recheck

Microsoft XAG 116 was re-read on `2026-08-14`:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116`

The page reports last updated `2026-03-04` and remains XAG v3.2 best-practice guidance.

The current source continues to distinguish non-core-gameplay UI timing from core gameplay timing. For applicable UI time limits it preserves the existing modification alternatives:

- request a longer or absent session limit before the limit starts;
- pre-adjust to at least 10× the default;
- warn before expiry, provide at least 20 seconds for a simple extension action, and allow at least ten extensions;
- turn the time limit off.

For important on-screen element duration it preserves the alternatives of pre-adjusting to at least 10× the default or disabling the duration limit and allowing dismissal/advance on input.

The source exception block says a content-imposed time limit is exempt when at least one listed condition is true. The listed conditions include:

- a required real-time event with no alternative;
- the time limit being essential to the task;
- **the default time limit exceeding 20 hours**.

Core gameplay timing remains outside this XAG's scope.

## 3. Correction

`ACCESSIBILITY-POLICY-OVERLAY-v7` composes over the exact v6 blob and replaces only:

- `XAG116-UI-TIME-LIMIT-MODIFIABLE`;
- `XAG116-IMPORTANT-ELEMENT-DURATION-MODIFIABLE`.

The first record now carries:

```yaml
exceptions:
  - real_time_event_with_no_alternative
  - time_limit_is_essential_to_task
  - default_time_limit_exceeds_20_hours
  - core_gameplay_timing
```

The important-element duration record now carries:

```yaml
exceptions:
  - real_time_event_with_no_alternative
  - duration_is_essential_to_task
  - default_time_limit_exceeds_20_hours
  - core_gameplay_timing
```

Every pre-existing alternative, threshold, trigger, evidence reference, gap reference, and source authority class in those records is preserved. `XAG116-UI-TIME-LIMIT-ESSENTIAL-ONLY` and `XAG116-UI-TIME-LIMIT-ADVANCE-WARNING` remain exact logical inputs from v6; this bounded patch does not reinterpret unrelated XAG 116 semantics that the negative review did not find defective.

## 4. Validator hardening

`ACCESSIBILITY-POLICY-VALIDATOR-v7` first requires exact v6 reconstruction over the exact v5 blob and verifies the existing 110-record XAG 108–123 inventory / 215-record composed inventory before applying the two-record patch.

The validator now requires `default_time_limit_exceeds_20_hours` to be present as an exception in both duration-modification records and forbids it from appearing as a trigger, required semantic, or positive requirement.

Load-bearing adversarial fixtures include:

- `XAG116_DEFAULT_OVER_20_HOURS_EXCEPTION_REMOVED` → `REJECT_EXCEPTION_LOSS`;
- `XAG116_DEFAULT_OVER_20_HOURS_EXCEPTION_INVERTED_TO_REQUIREMENT` → `REJECT_EXCEPTION_INVERSION`;
- `XAG116_EXISTING_EXCEPTION_DROPPED` → `REJECT_EXCEPTION_LOSS`;
- `XAG116_MODIFICATION_ALTERNATIVE_DROPPED` → `REJECT_SEMANTIC_NARROWING`;
- `XAG116_THRESHOLD_WEAKENED` → `REJECT_THRESHOLD_DRIFT`;
- `V6_UNRELATED_RECORD_REDEFINED` → `REJECT_SCOPE_LEAKAGE`.

Fail-closed evidence and aggregate-state fixtures remain mandatory.

## 5. Preservation proof

The v7 overlay adds, removes, splits, or renames no atomic clause identity.

Preserved inventory:

- inherited XAG 101–107 atomic clauses: 105;
- XAG 108–123 atomic clauses: 110;
- XAG 116 atomic clauses: 4;
- composed XAG 101–123 atomic total: 215.

The exact v6 policy blob remains the only logical source for all records except the two declared XAG 116 corrections. Source registrations, evidence/gap records, all non-XAG116 records, and the v6 authority boundary remain unchanged.

The existing XAG 116 semantics remain preserved, including core-gameplay exclusion, real-time/no-alternative and essential-task exceptions where already source-covered, 10× adjustment, 20-second minimum action window, at least ten extensions, turn-off, and important-element disable/dismiss-or-advance behavior.

## 6. Finding disposition

`W2-REV-ACC06-M01` is **RESOLVED_PENDING_FRESH_REVIEW** in this producer packet:

- default-over-20-hours exception restored to the two source-exception-bearing duration-modification records: **YES**;
- exception-loss fixture present: **YES**;
- exception-inversion fixture present: **YES**;
- existing XAG 116 alternatives/thresholds changed: **NO**;
- unrelated v6 records rewritten: **NO**;
- XAG identity/count changed: **NO**;
- empirical accessibility PASS claimed: **NO**;
- aggregate blocker cleared: **NO**.

Bounded producer self-review finds 0 unresolved BLOCKER, 0 unresolved MAJOR, and 0 correction-requiring MINOR in this remediation scope. Producer self-review is not independent acceptance.

## 7. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

This task does not establish accessibility quality in a target build, readiness, implementation, release, legal/compliance status, platform certification, verification PASS, decision authority, integration authority, or canonical status.

## 8. Required next transition

Freeze this remediation at an exact terminal head with an exact-head draft PR to `main`, then route a fresh independent/degraded-independent scoped review of that exact packet. A CLEAN review would only make the exact corrected provenance eligible for separately authorized squash-only integration; it would not close `W2-REV-M02` or `IR-BLOCKER-ACCESSIBILITY-CURRENT`.
