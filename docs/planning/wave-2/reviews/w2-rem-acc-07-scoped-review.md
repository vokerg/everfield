# W2-REV-ACC-07 — scoped review of XAG 116 exception remediation

**Mission:** `W2-REV-ACC-07` / Issue #267  
**Trust profile:** `DEGRADED_SINGLE_AGENT` fresh reviewer episode  
**Review claim:** comment `5291946901`  
**Reviewed producer:** Issue #264 / `W2-REM-ACC-07`  
**Reviewed terminal status:** comment `5291899588`  
**Reviewed exact head:** `0fe6607a0560ce546b7dbedf99ce5394c00345df`  
**Reviewed substantive work:** `d1ea503eb065d6235f006d7a58fb175775d4f65e`  
**Reviewed PR:** #266  
**Reviewed policy v7 blob:** `4cf9113bc6c4c663db360594e54b5403cc9e5588`  
**Reviewed report blob:** `1a1ec00e6b8143d7f233d58ecc3889d8f7c1550f`  
**Reviewed handoff blob:** `05ecc5967d22f16fc0c22afa07dc1d93131fa53c`  
**Immutable predecessor policy v6 blob:** `80e278315d6b7a108d89da3f5a99086a8ef91bf7`  
**Source negative review:** Issue #262 terminal comment `5290467457`, finding `W2-REV-ACC06-M01` / MAJOR  
**Disposition:** `CLEAN_FOR_NONCANONICAL_INTEGRATION`

## 1. Frozen identity and independence boundary

This review consumed the producer only at Issue #264's terminal exact identity. The reviewer episode is distinct from producer actor session `w2-rem-acc-07-gpt56sol-20260814-1138-frontier`; Issue #264 and PR #266 were treated as immutable read-only inputs.

At cold start, `main` remained `6eacb5b81e414686028e5a50c9250a0b80a16c94`, the canonical program blob remained `e3120ec203c4156328770aa86c12fbb7187966dc`, and canonical activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` remained an ancestor of current main. PR #266 was re-fetched open, draft, mergeable, `planning/issue-264 -> main`, exact head `0fe6607a0560ce546b7dbedf99ce5394c00345df`, base `main@6eacb5b81e414686028e5a50c9250a0b80a16c94`.

A direct compare of producer base to exact producer head shows exactly three changed paths:

- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`;
- `docs/planning/wave-2/research/accessibility-current-requirements.md`;
- `docs/planning/handoffs/issue-264.md`.

No producer mutation was performed during this review.

## 2. Fresh first-party source reconstruction

Microsoft XAG 116 was re-read independently on `2026-08-14` before reconciling producer rationale:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116`

The current page reports last updated `2026-03-04` and remains XAG v3.2 accessibility best-practice guidance, not legal/compliance certification.

Load-bearing source semantics independently reproduced:

- the guideline applies to UI timing outside core gameplay mechanics;
- applicable UI time limits are expected to provide a way to modify the limit;
- the listed modification mechanisms include a longer/no session limit before start, pre-adjustment to at least 10x the default, a warning with at least a 20-second simple-action extension window and at least ten extensions, or turning the limit off;
- important-element duration can be pre-adjusted to at least 10x or disabled so the element can be dismissed/advanced on input;
- a content-imposed time limit is exempt from the relevant modification expectation when at least one exception holds: required real-time event/no alternative, essential-to-task, or default time limit exceeding 20 hours;
- core gameplay timing is outside the XAG's scope.

The source examples and note describe exception effect in terms of not requiring the ability to extend or adjust the time limit. Within the exact v6 atomic model, the real-time and essential-task exception set was already attached to the two modification/duration records rather than the separate essential-only and advance-warning records. Fresh source review found no basis for this bounded M01 correction to broaden the exception patch beyond those two source-exception-bearing modification records.

This review is scoped to the terminal M01 remediation. It does not claim exhaustive re-adjudication of all pre-existing v6 XAG 108-123 atomization choices that Issue #262 explicitly left unexhausted after its negative early termination.

## 3. Exact v6 reproduction of the defect

Exact predecessor policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7` contains four XAG 116 atomic identities:

1. `XAG116-UI-TIME-LIMIT-ESSENTIAL-ONLY`;
2. `XAG116-UI-TIME-LIMIT-ADVANCE-WARNING`;
3. `XAG116-UI-TIME-LIMIT-MODIFIABLE`;
4. `XAG116-IMPORTANT-ELEMENT-DURATION-MODIFIABLE`.

The two modification records reproduce the source-derived real-time/essential/core-gameplay exception model, but exact v6 contains no `default_time_limit_exceeds_20_hours` predicate anywhere.

For `XAG116-UI-TIME-LIMIT-MODIFIABLE`, exact v6 has:

```yaml
exceptions:
  - real_time_event_with_no_alternative
  - time_limit_is_essential_to_task
  - core_gameplay_timing
```

For `XAG116-IMPORTANT-ELEMENT-DURATION-MODIFIABLE`, exact v6 has:

```yaml
exceptions:
  - real_time_event_with_no_alternative
  - duration_is_essential_to_task
  - core_gameplay_timing
```

The Issue #262 finding therefore reproduces independently: v6 cannot represent the source's default-over-20-hours exemption.

## 4. Exact v7 logical delta attack

Exact v7 policy blob `4cf9113bc6c4c663db360594e54b5403cc9e5588` is an overlay over exact v6 rather than a wholesale redefinition of the XAG 108-123 inventory.

Its composition contract replaces exactly:

- `XAG116-UI-TIME-LIMIT-MODIFIABLE`;
- `XAG116-IMPORTANT-ELEMENT-DURATION-MODIFIABLE`.

The only source-semantic addition to each replacement is:

```yaml
- default_time_limit_exceeds_20_hours
```

inside `exceptions`.

The cold field-by-field attack reproduced all pre-existing load-bearing semantics unchanged:

- UI trigger remains `non_core_gameplay_ui_interaction_has_time_limit`;
- UI `modification_alternatives_minimum` remains `1`;
- longer/no-session alternative remains present;
- pre-adjustment remains at least 10x;
- expiry extension action window remains at least 20 seconds;
- simple-action extension remains present with minimum ten uses;
- turn-off alternative remains present;
- real-time/no-alternative, essential-task, and core-gameplay exception tokens remain present;
- important-element trigger remains `important_element_has_display_duration_limit`;
- important-element alternatives remain at least-10x pre-adjustment or disable-duration/dismiss-or-advance-on-input;
- evidence ref remains `ACC-EV-XAG116` and gap ref remains `ACC-GAP-XAG116`.

The overlay explicitly preserves `XAG116-UI-TIME-LIMIT-ESSENTIAL-ONLY` and `XAG116-UI-TIME-LIMIT-ADVANCE-WARNING` as exact logical v6 inputs and preserves every non-XAG116 v6 record/source/evidence/gap record.

No clause identity is added, removed, split, or renamed. The four-record XAG 116 identity set is preserved.

## 5. Exception inversion / loss attack

The v7 semantic contract requires the new predicate to appear as an exception in both replacement records and explicitly forbids it as a trigger, required semantic, or positive requirement.

The load-bearing adversarial fixtures are sufficient for this bounded defect:

```yaml
XAG116_DEFAULT_OVER_20_HOURS_EXCEPTION_REMOVED: REJECT_EXCEPTION_LOSS
XAG116_DEFAULT_OVER_20_HOURS_EXCEPTION_INVERTED_TO_REQUIREMENT: REJECT_EXCEPTION_INVERSION
XAG116_EXISTING_EXCEPTION_DROPPED: REJECT_EXCEPTION_LOSS
XAG116_MODIFICATION_ALTERNATIVE_DROPPED: REJECT_SEMANTIC_NARROWING
XAG116_THRESHOLD_WEAKENED: REJECT_THRESHOLD_DRIFT
V6_UNRELATED_RECORD_REDEFINED: REJECT_SCOPE_LEAKAGE
```

Independent mutation reasoning against the declared validator contract gives the expected fail-closed results:

- deleting the >20-hour token violates a required semantic assertion and the declared loss fixture;
- moving the token into a trigger/positive requirement violates the explicit placement assertion and inversion fixture;
- deleting an existing exception, modification alternative, or weakening a threshold violates its dedicated preservation assertion/fixture;
- redefining an unrelated v6 record violates exact-input composition and `REJECT_SCOPE_LEAKAGE`.

This is a machine-readable policy-contract/mechanical review, not empirical execution against a target build. No target-build accessibility evidence is inferred from these validator-contract results.

## 6. Inventory and aggregate fail-closed attack

Exact v6 declares:

- XAG 101-107 inherited clauses: `105`;
- XAG 108-123 new clauses: `110`;
- XAG 116 clauses: `4`;
- composed XAG 101-123 clauses: `215`.

Because v7 replaces two existing identities without adding/removing/splitting identities and requires exact v6 reconstruction before applying the patch, the bounded composition preserves `110` and `215`. The review found no hidden identity expansion in the v7 overlay.

The fail-closed state remains explicit and internally consistent:

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

The v7 authority boundary also keeps readiness, implementation, release, legal/compliance, platform certification, verification PASS, decision, canonical, and integration authority false.

## 7. Findings and disposition

No correction-requiring defect was found in the bounded Issue #264 remediation.

```yaml
review_disposition: CLEAN_FOR_NONCANONICAL_INTEGRATION
review_scope: W2-REV-ACC06-M01_REMEDIATION_ONLY
findings: []
blockers: 0
majors: 0
correction_requiring_minors: 0
W2-REV-ACC06-M01: RESOLVED_FOR_THIS_EXACT_PACKET
xag116_default_over_20_hours_exception: PASS
xag116_exception_placement: PASS_BOUNDED
xag116_exception_loss_guard: PASS_CONTRACT
xag116_exception_inversion_guard: PASS_CONTRACT
xag116_existing_exceptions: PRESERVED
xag116_existing_modification_alternatives: PRESERVED
xag116_existing_thresholds: PRESERVED
xag116_atomic_clause_count: 4
xag_108_123_atomic_clause_count: 110
composed_atomic_clause_count: 215
producer_pr_scope: PASS_THREE_FILES
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
production_implementation_ready: false
integration_authorized_by_review: false
canonicality: NOT_CANONICAL
review_exhaustiveness: BOUNDED_M01_REMEDIATION_REVIEW
```

Exact Issue #264 / PR #266 is therefore **clean for separately authorized squash-only noncanonical integration** of this bounded remediation provenance. That is integration eligibility, not integration authority.

## 8. Authority boundary / next transition

This review grants no empirical accessibility PASS, mapping completion, implementation/readiness/release authority, legal/compliance status, platform certification, verification PASS, merge/integration authority, decision authority, or canonical status.

`IR-BLOCKER-ACCESSIBILITY-CURRENT` and `W2-REV-M02` remain open/fail-closed. Issue #259 / PR #261 remains rejected by Issue #262; this scoped review does not retroactively convert the rejected v6 producer packet into an accepted packet.

The next convergence step, after this review itself is terminalized and its exact provenance is visible in a draft PR, is a fresh authority re-derivation. If repository authority permits, exact reviewed Issue #264 / PR #266 may be squash-integrated as noncanonical remediation provenance without upgrading any aggregate accessibility/readiness/canonical state. Integration must remain a separate act and squash-only.