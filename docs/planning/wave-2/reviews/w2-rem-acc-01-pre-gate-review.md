# W2-PG-REM-ACC-01 — Independent pre-gate review of W2-REM-ACC-01

**Mission:** `W2-PG-REM-ACC-01` / Issue #134  
**Reviewed mission:** `W2-REM-ACC-01` / Issue #96  
**Reviewed work/head:** `3937f65ae4eb495420d1240c2b739841aa14a037`  
**Reviewed terminal status:** Issue #96 comment `5271849637`  
**Reviewed report blob:** `b5f0669a5c9e8fc242b96eabf1a32bc21c0248ee`  
**Reviewed policy blob:** `78690cf658967b2ded35e738df125959a56f0d86`  
**Reviewed finding-disposition blob:** `78576cac9f7cdeaf2552235d19cac01cba7b099b`  
**Reviewed handoff blob:** `261cb3a15511a2dc2be4ec810b43283edfc341ee`  
**Current-source observation:** `2026-08-13`  
**Disposition:** `CHANGES_NEEDED`  
**Authority:** noncanonical pre-gate review input only; formal `W2-REV-01` remains required.

## 1. Scope and method

This review consumed Issue #96 only at its frozen terminal identity. No Issue #96 artifact or branch was modified.

The four published artifact identities were re-fetched at exact reviewed head and reproduced exactly. The policy was then attacked against its own contract and against current first-party source text for the load-bearing XAG 101/XAG 107 and Valve Deck claims. The review specifically tested whether the policy can distinguish a complete source-clause mapping from a merely asserted `ATOMICALLY_EXPANDED` page, whether exact source semantics survive normalization, whether summary-only pages stay fail-closed, and whether direct Valve checklist authority stays distinct from project-selected Proton evidence.

Current first-party sources rechecked:

- Microsoft XAG index: `https://learn.microsoft.com/en-us/xbox/accessibility/guidelines`
- Microsoft XAG 101: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101`
- Microsoft XAG 107: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107`
- Valve Steam Deck / Steam Machine compatibility review: `https://partner.steamgames.com/doc/steamhardware/compat`

The Microsoft index remains XAG v3.2, published 2023-06-08, and explicitly frames the XAGs as best-practice guidance rather than legal/compliance proof. XAG 101 and XAG 107 currently show last-updated 2026-03-04. The Valve page continues to separate compatibility checklist requirements from Proton behavior.

## 2. Confirmed strengths

The remediation correctly removes the original unsafe positive claim. Its aggregate remains:

```yaml
mapping_complete: false
blocker_id: IR-BLOCKER-ACCESSIBILITY-CURRENT
blocker_authority_state: OPEN
required_next_authority: W2-REV-01
```

XAG 102–106 and 108–123 remain `GUIDELINE_SUMMARY_ONLY`; they do not currently produce aggregate mapping PASS. Evidence requirement states remain `NOT_RUN`. The direct Valve compatibility records and `ACC-PROJECT-DECK-PROTON-01` use different authority classes, so the original Proton-authority conflation is materially corrected. No legal compliance, Valve `Verified`, empirical accessibility PASS, implementation-readiness, integration, verification, release, or canonicalization authority is created.

The exact XAG 107 controls attacked by the original pre-gate review are substantially represented: digital/analog UI navigation, single non-simultaneous UI operation, remapping, remap-label synchronization, digital equivalents, rapid/held/simultaneous-input alternatives, gesture alternatives, pointer up-event/cancel behavior, alternative digital input for gameplay-critical speech/motion, two-stick alternatives, keyboard-only path, analog sensitivity, dictation, and customization accessibility.

## 3. Findings

### PG-REM-ACC-M01 — MAJOR — `ATOMICALLY_EXPANDED` is not mechanically total and already drops required XAG 101 semantics

Issue #96 claims that the catalog construction rule prevents equivalent silent source-clause omissions and that source thresholds/required semantics are preserved. The policy's completeness contract says every source threshold or required semantic must survive in the clause record. However, the policy has no machine-checkable expected-clause inventory or source-clause manifest against which the `ATOMICALLY_EXPANDED` page flag is validated. A page can therefore be declared atomically expanded while a clause or a required semantic is absent.

The frozen packet contains a concrete instance. Current XAG 101 text-spacing guidance states that the 80-character (40 CJK) line-width bound is measured when text is resized to 100 percent and that spaces are excluded from the character count. The policy's `XAG101-TEXT-BLOCK-SPACING` record retains the numeric 80/40 bounds but omits both measurement conditions. Yet `guideline_inventory.XAG-101.expansion_state` is `ATOMICALLY_EXPANDED`, and the self-review reports the attacked XAG 101 clauses as mechanically covered.

This is not a cosmetic omission. An implementation with 80 non-space glyphs plus spaces can be evaluated differently from a raw-character-count implementation, and evaluating at a non-100-percent text scale changes the test basis. The policy therefore fails its own exact-semantic preservation predicate while retaining the page-level atomic-completeness assertion.

The same structural weakness means a wholly missing source clause cannot be detected from the packet itself: `ATOMICALLY_EXPANDED` is a trusted declaration, not a derived result from an expected source-clause set. The current aggregate happens to remain false because other pages are summary-only, but the mechanism required to prevent a future false positive is incomplete.

**Required correction:** add an explicit expected source-clause inventory/schema for each page claimed atomically expanded and a mechanically deterministic validator that derives page expansion/completeness from that inventory. Correct the XAG 101 line-width record to retain the 100-percent measurement condition and exclusion of spaces, and add adversarial fixtures proving removal of either condition fails validation.

### PG-REM-ACC-M02 — MAJOR — direct Valve controller checklist mapping omits a current required criterion

The remediation correctly separates direct Valve checklist authority from project-selected Proton evidence, but the direct checklist mapping is incomplete in a way that can under-specify compatibility evidence.

Current Valve compatibility requirements state both that the default controller configuration must access all content and that players must not need to change an in-game setting to enable controller support or that configuration. `ACC-DECK-01` records only `default_controller_configuration_accesses_all_content`. No other direct Valve record captures the no-settings-enable requirement.

This omission matters because an evidence run could satisfy the mapped `ACC-DECK-01` predicate after manually enabling controller support while still failing Valve's direct compatibility requirement. The packet explicitly presents these records as the current direct Valve checklist requirements relevant to the selected Deck target; leaving a required criterion unbound is therefore a material evidence-mapping defect.

The project-selected Proton record itself remains correctly typed and must remain separate.

**Required correction:** add a direct Valve requirement/evidence predicate for controller support/default configuration being usable without an in-game setting change, bind it to exact evidence, and add a negative fixture or mechanical check showing that manual enablement cannot satisfy the direct compatibility mapping.

## 4. Current-source drift result

No material drift was found in the source facts that the frozen remediation actually encodes correctly:

- XAG remains v3.2 and non-legal best-practice guidance.
- XAG 101 still carries the 18 px PC/VR 1080p default target, 200% scaling guidance, font/style/spacing/case/alignment guidance, including the omitted line-width measurement details described in `PG-REM-ACC-M01`.
- XAG 107 still carries the remap/input alternatives, keyboard-only path, ±50% analog-sensitivity range, pointer activation/cancellation, dictation, and customization-accessibility guidance represented by the policy.
- Valve still requires controller support/default configuration, correct glyphs, controller-usable text input, 30 fps at 800p default Deck performance, no device-compatibility warning, launcher compatibility, supported Deck resolution, and the 9 px minimum text height at 1280x800; Valve also still documents Proton as the Windows compatibility layer used when no native Linux build is selected.

The review does not treat absence of a visible Valve page-last-updated field as evidence of freshness; the facts above were re-observed directly on 2026-08-13.

## 5. Disposition and routing

**Disposition: `CHANGES_NEEDED` — 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR.**

Both original Issue #81 pre-gate findings are directionally corrected, but Issue #96 is not clean enough to enter formal W2 review as a mechanically total source-clause packet because its atomic-completeness mechanism trusts an unverified page flag and its direct Valve checklist mapping omits one current required controller criterion.

Exactly one bounded successor is routed: Issue #135 / `W2-REM-ACC-02`. That successor is blocked until this review freezes at valid terminal `STATUS(REVIEW_READY)` and must preserve the current fail-closed aggregate, OPEN accessibility blocker, Valve/Proton authority split, and formal `W2-REV-01` requirement.

This review does not authorize edits to frozen Issue #96, accessibility/legal certification, a Valve compatibility result, production/readiness, implementation, integration, verification, release, merge, or canonicalization. Any eventual `main` integration remains separately authorized and squash-only.
