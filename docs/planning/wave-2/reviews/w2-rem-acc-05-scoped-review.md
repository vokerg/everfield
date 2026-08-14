# W2-REV-ACC-05 — independent scoped review of pronunciation applicability remediation

**Mission:** `W2-REV-ACC-05` / Issue #255  
**Reviewed producer:** `W2-REM-ACC-05` / Issue #252  
**Reviewed terminal status:** comment `5290245208`  
**Reviewed exact head:** `e6b2a826a29937a805273a8cc4fe436dd4970992`  
**Reviewed substantive work:** `c5490ae510086069da4983d6e672f9c8f9c6f314`  
**Reviewed PR:** #254  
**Reviewed report blob:** `932905021788ffa47609201ee559df9a8387a37c`  
**Reviewed policy v5 blob:** `c7c3f72fb3bbd2d0e961aee94b33ce2ac93c5615`  
**Reviewed handoff blob:** `9508fdf0a7ae93060b232f04d3af470062bfc22a`  
**Immutable predecessor policy v4 blob:** `96a074e9c708d4ae2f86e8a70b7b4ade8202c799`  
**Review claim:** comment `5290257961`  
**Trust profile:** `DEGRADED_SINGLE_AGENT` fresh review episode  
**Disposition:** `CLEAN_FOR_NONCANONICAL_INTEGRATION`

## 1. Frozen identity and independence

The review consumed Issue #252 only at its terminal exact identity. PR #254 remained an open draft at exact head `e6b2a826a29937a805273a8cc4fe436dd4970992`, based on `main@9b044059df07170f8db0f430451d15e1c6800f82`, and changed only the declared bounded producer surfaces:

- `docs/planning/handoffs/issue-252.md`;
- `docs/planning/wave-2/research/accessibility-current-requirements.md`;
- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`.

The producer branch was not modified by this review. Duplicate review routes #256 and #257 were externally terminalized `SUPERSEDED` in favor of the earlier valid Issue #255 claim `5290257961`; they created no competing review branch or acceptance authority.

Under the repository-visible single-agent constraint, producer assertions were treated as hypotheses rather than acceptance evidence. The review independently re-read the current first-party XAG 106 source, reconstructed the exact inherited record, compared the v5 replacement field-by-field, and re-attacked the declared semantic guards before accepting the bounded packet.

## 2. Fresh first-party XAG 106 reconstruction

Source re-read on `2026-08-14`:

- Microsoft XAG 106: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106`
- current page reports last updated `2026-03-04`;
- the implementation guideline separately requires a mechanism for the player to understand how to pronounce a proper name, technical term, or word of indeterminate language.

The source-covered term classes establish applicability for this pronunciation obligation. The implementation bullet does not add a product-side `requires_pronunciation_help` judgment before the mechanism is required.

The nearby XAG 106 guidance that treats proper names, technical terms, and words of indeterminate language as exceptions to programmatic language tagging is a different rule. It does not cancel the separate pronunciation-mechanism obligation. The reviewed v5 record keeps those semantics separate.

XAG evidence remains accessibility best-practice evidence; this review does not interpret it as legal/compliance or platform certification.

## 3. Exact inherited record versus v5 correction

The exact v3 policy blob `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4` contains:

```yaml
XAG106-PROPER-NAME-PRONUNCIATION:
  source_id: XAG-106
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  applicability: CONDITIONAL
  trigger: proper_name_technical_term_or_word_of_indeterminate_language_requires_pronunciation_help
  required_semantics:
    pronunciation_mechanism_provided: true
  evidence_requirement_refs: [ACC-EV-NARRATION]
  gap_ref: ACC-GAP-XAG106
```

Exact v4 blob `96a074e9c708d4ae2f86e8a70b7b4ade8202c799` replaces six other records and deliberately does not replace this pronunciation record. It therefore inherits the v3 pronunciation record unchanged while requiring a fresh scoped re-attack.

Exact v5 blob `c7c3f72fb3bbd2d0e961aee94b33ce2ac93c5615` replaces that record with:

```yaml
XAG106-PROPER-NAME-PRONUNCIATION:
  source_id: XAG-106
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  applicability: CONDITIONAL
  trigger: proper_name_or_technical_term_or_word_of_indeterminate_language_is_present
  required_semantics:
    pronunciation_mechanism_provided: true
  evidence_requirement_refs: [ACC-EV-NARRATION]
  gap_ref: ACC-GAP-XAG106
```

Field-by-field reconstruction therefore shows exactly one semantic correction inside the logical record: the trigger. Source identity, authority class, applicability class, required pronunciation mechanism, evidence routing, gap routing, and stable clause identity are preserved.

`W2-REV-ACC04-M01` is resolved in this exact reviewed packet: the subjective non-source gate is removed and all three source term classes remain explicit.

## 4. v4 preservation and scope attack

The exact v4 overlay has exactly six correction records:

1. `XAG102-PLATFORM-HIGH-CONTRAST-DEFAULT`;
2. `XAG104-SPEAKER-ID-REFRESH`;
3. `XAG104-PRESTART-OR-DEFAULT-ON`;
4. `XAG105-PAUSE-AUDIO-EVENTS`;
5. `XAG106-CORE-UI-NARRATION`;
6. `XAG106-CONTEXT-CHANGE-INITIATED-NARRATED`.

The v5 composition contract loads the exact v4 blob by SHA, verifies those six records as the immutable logical input, and then replaces only `XAG106-PROPER-NAME-PRONUNCIATION`. The v5 patch section contains no redefinition of any of the six v4 correction records.

Result: `V4_CORRECTION_REDEFINED` is rejected by scope and exact-base identity, and no Issue #247 correction regresses in this reviewed overlay.

## 5. Mechanical/adversarial re-attack

The v5 contract uses exact trigger equality plus explicit required-semantics and exact-base assertions. Recomputing each bounded adversarial mutation gives:

| Attack | Required failure condition | Review result |
|---|---|---|
| `SUBJECTIVE_PRONUNCIATION_APPLICABILITY_GATE` | any added subjective predicate makes the trigger differ from the one exact allowed trigger | `REJECT_INVENTED_PRECONDITION` — PASS |
| `PRONUNCIATION_TERM_CLASS_DROPPED` | dropping any proper-name / technical-term / indeterminate-language class makes the trigger differ from the exact allowed trigger | `REJECT_SEMANTIC_NARROWING` — PASS |
| `PRONUNCIATION_MECHANISM_DROPPED` | `pronunciation_mechanism_provided` must remain exactly `true` | `REJECT_REQUIRED_SEMANTIC_LOSS` — PASS |
| `V4_CORRECTION_REDEFINED` | exact v4 blob is the composition input and the six correction records may not be redefined by v5 | `REJECT_SCOPE_LEAKAGE` — PASS |
| `UPGRADE_XAG108_123_WITHOUT_INVENTORY` | summary-only state must remain unchanged | `REJECT_ATOMIC_EXPANSION` — PASS |
| `CLAIM_EMPIRICAL_PASS_WITH_NOT_RUN_EVIDENCE` | empirical evidence must remain `NOT_RUN` | `REJECT_EVIDENCE_STATE` — PASS |
| `SET_MAPPING_COMPLETE_TRUE` | aggregate mapping must remain false | `REJECT_AGGREGATE_STATE` — PASS |

The exact trigger-equality assertion is stronger than searching only for the literal old substring: any equivalent extra subjective applicability condition would change the one accepted trigger and fail the contract.

## 6. Inventory, reference, and aggregate-state verification

The v5 overlay does not add, remove, split, or rename an atomic clause. Exact bounded inventory remains:

- XAG 102: `12`;
- XAG 103: `8`;
- XAG 104: `29`;
- XAG 105: `5`;
- XAG 106: `23`;
- new XAG 102–106 total: `77`;
- inherited XAG 101/XAG 107: `28`;
- composed atomic total: `105`.

The pronunciation record retains `ACC-EV-NARRATION` and `ACC-GAP-XAG106`; no reference is dropped by the correction. The exact source record stays in the XAG 106 expected inventory.

Fail-closed aggregate state remains:

```yaml
xag_108_123: GUIDELINE_SUMMARY_ONLY
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
production_implementation_ready: false
integration_authorized_by_producer: false
canonicality: NOT_CANONICAL
```

No empirical accessibility PASS is created and no aggregate blocker is cleared by this review.

## 7. PR #254 cold inspection

PR #254 was re-fetched during review and remained:

- open;
- draft;
- mergeable at observation time;
- base `main` at `9b044059df07170f8db0f430451d15e1c6800f82`;
- exact reviewed head `e6b2a826a29937a805273a8cc4fe436dd4970992`;
- bounded to the producer handoff, accessibility report, and accessibility policy.

The packet repeatedly preserves `NOT_RUN`, `mapping_complete: false`, the OPEN aggregate blocker, `W2-REV-M02: OPEN_BOUNDED`, and absence of integration/canonical authority. No accessibility-PASS, readiness, implementation, release, legal/compliance, platform-certification, verification-PASS, decision, integration, or canonical authority inflation was found.

Mergeability and draft state are not treated as authority.

## 8. Disposition

```yaml
review_disposition: CLEAN_FOR_NONCANONICAL_INTEGRATION
findings: []
blockers: 0
majors: 0
correction_requiring_minors: 0
reviewed_packet_accepted: true
reviewed_packet_integration_eligible: true
integration_authorized_by_this_review: false
W2-REV-ACC04-M01: RESOLVED
pronunciation_source_reattack: PASS
v5_overlay_scope: PASS
subjective_gate_fixture: PASS
term_class_fixture: PASS
pronunciation_mechanism_fixture: PASS
v4_six_corrections_preserved: PASS
xag_102_106_inventory: PASS_77
composed_atomic_inventory: PASS_105
reference_integrity: PASS
xag_108_123: GUIDELINE_SUMMARY_ONLY
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
production_implementation_ready: false
canonicality: NOT_CANONICAL
```

This clean scoped result makes only the exact Issue #252 packet eligible for a **separately authorized, squash-only, noncanonical provenance integration** under the repository's current convergence authority. It does not itself authorize a merge, does not make the packet canonical, and does not close aggregate accessibility evidence/mapping debt or `W2-REV-M02`.

## 9. Authority boundary

This review creates noncanonical review provenance only. It grants no empirical accessibility PASS, implementation readiness, production authority, release authority, legal/compliance status, platform certification, aggregate verification PASS, decision authority, merge authority, or canonical authority. Any integration into `main` remains a distinct authority decision and must be squash-only.
