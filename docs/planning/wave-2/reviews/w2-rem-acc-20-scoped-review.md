# W2-REV-ACC-20 — scoped review of XAG 120 notification-example remediation

## Review identity

- Mission: `W2-REV-ACC-20`
- Issue: `#313`
- Winning claim: `5296928986`
- Actor/session: `w2-rev-acc-20-gpt56sol-20260814-2044-frontier`
- Trust mode: `DEGRADED_INDEPENDENT`
- Review branch/base: `planning/issue-313` from `main@6bdf6c54ce3100f9b9af0adb99e7745c1c8c4b89`
- Canonical Planning Program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

A later competing claim, `5296931537`, does not own this task because the valid claim above has the lower comment id. The task branch was re-fetched after that race and remained exactly at the claimed base before review mutation.

## Frozen producer and source-review inputs

Producer:

- Issue `#310` / `W2-REM-ACC-15`
- producer claim `5296883667`
- unedited terminal `STATUS(REVIEW_READY)` `5296923822`
- terminal producer head `95d139901e193086892a9c7e745476f6cad399da`
- substantive work `71b3fddda8d8133514574775848b19b401a2f0d1`
- draft PR `#314`
- v14 policy blob `33c4fdcde1c28ed2623496b04d2d376d4aac190b`
- v14 report blob `b8c5cb0e7394b21f99ca9e09275cd145d59bba1b`
- producer handoff blob `2aba65996bb21344471f75ebea5c4876f10706ec`

Immutable v13 inputs on current `main`:

- policy blob `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`
- report blob `e5f1f491a91499bef96861d2878e4fb5552a207b`

Source required review:

- Issue `#308` / `W2-REV-ACC-19`
- winning claim `5296830252`
- terminal review `5296868370`
- exact review head/work `024efaa4cc97b5af6e669cf9100b5172a2096bd4` / `ed51563510cee7cd24463a6d1a169ec3f0f2ea3e`
- disposition `CHANGES_NEEDED`
- finding `W2-REV-ACC19-M01 / MAJOR / EXAMPLE_TO_REQUIREMENT_PROMOTION_AND_FEATURE_EXISTENCE_INFLATION`
- affected atom `XAG120-COMM-NOTIFICATION-SETTINGS`
- terminal boundary: XAG 120; XAG 121–123 remain unaccepted.

## Fresh first-party source recheck

Re-read Microsoft Xbox Accessibility Guideline 120 on `2026-08-14` from the current Microsoft Learn page:

`https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/120`

The page identifies XAG 120 as communication experiences and reports a last-updated date of `2026-03-04`.

The load-bearing source semantics are:

1. The implementation guidance is scoped to games that offer player-to-player communication experiences.
2. Necessary UI for enabling or managing settings that affect communication should be accessible.
3. Notification-management menus/settings are followed by examples, including notification display-duration adjustment and turning certain notifications on/off.
4. Those examples describe settings whose UI/path must be accessible when the settings exist; the source does not turn both examples into universal requirements that every communicating title implement those product features.
5. Navigation to and interaction with settings that affect communication remain subject to applicable accessibility guidance.

This independently reproduces the source-side defect identified by `W2-REV-ACC19-M01` and supports the producer's bounded correction direction.

## Exact producer-scope attack

Comparing producer base `65d4eb8144e33d8e247c0dc0a688f6811a4225bb` to producer head `95d139901e193086892a9c7e745476f6cad399da` yields exactly three changed files:

- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`
- `docs/planning/wave-2/research/accessibility-current-requirements.md`
- `docs/planning/handoffs/issue-310.md`

The producer PR freezes the same exact head and the same three-file scope. Current `main@6bdf6c54ce3100f9b9af0adb99e7745c1c8c4b89` still carries the exact v13 policy/report input blobs; the intervening recovery-provenance integration does not mutate the accessibility mapping inputs.

The v14 composition contract loads the exact v13 policy/report blobs and changes the semantic encoding of one inherited atom, `XAG120-COMM-NOTIFICATION-SETTINGS`, plus the minimum producer/report/validator metadata needed to make that correction auditable. No sibling XAG 120 identity is added, removed, split, or renamed by this overlay.

## Atom reconstruction and fidelity

The following identity and authority fields remain unchanged from v13:

- atom: `XAG120-COMM-NOTIFICATION-SETTINGS`
- source: `XAG-120`
- authority: `BEST_PRACTICE_REQUIRED_IF_APPLICABLE`
- source modality: `SHOULD`
- applicability: `CONDITIONAL`
- trigger: `communication_notifications_are_available`
- evidence: `ACC-EV-XAG120`
- gap: `ACC-GAP-XAG120`

The v13 payload universally encoded three required semantics once the trigger applied: accessible notification settings, adjustable notification duration, and notification on/off capability. The v14 payload keeps `notification_settings_accessible: true` as the applicable obligation, but moves the two source examples into conditional semantics:

- if a duration-adjustment control exists, that control must be accessible;
- if a notification on/off control exists, that control must be accessible;
- absence of either example control does not independently fail the atom and does not require the title to invent that feature.

This resolves the feature-existence inflation without weakening accessibility for controls that actually exist.

## Required attack results

| Attack | Result | Basis |
| --- | --- | --- |
| Exact producer terminal identity | PASS | Terminal `5296923822` is unedited and binds head/work/PR/v14 blobs exactly. |
| First-party XAG 120 re-read | PASS | Microsoft uses notification duration/on-off under example framing while keeping necessary communication-setting UI accessibility load-bearing. |
| Bounded v14-over-v13 scope | PASS | Exact producer compare has only policy, report, and handoff; overlay changes XAG 120 semantic encoding plus review/validator metadata. |
| Atom/source/authority/modality preservation | PASS | Identity, `XAG-120`, required-if-applicable best-practice `SHOULD`, `CONDITIONAL`, trigger, evidence, and gap are unchanged. |
| No-feature-invention positive case | PASS | v14 fixture accepts notifications + accessible management UI with neither example control present. |
| Existing duration-control accessibility | PASS | Present-and-accessible passes; present-but-inaccessible is rejected. |
| Existing notification-toggle accessibility | PASS | Present-but-inaccessible is rejected. |
| Example-to-requirement regression | PASS | Universal requirement for both example controls is explicitly rejected. |
| Conditional product scope | PASS | Overlay does not require adding communication, notification, duration, or toggle features absent from title scope. |
| Reviewed correction preservation | PASS | v14 declares exact v13 as immutable input and preserves reviewed XAG 112, 114, 115, 116, and 117 contracts; no unrelated semantic record is redefined by the bounded overlay. |
| Inventory preservation | PASS | XAG 112=`14`; XAG 114=`16`; XAG 108–123=`113`; inherited XAG 101–107=`105`; composed XAG 101–123=`218`. |
| Fail-closed aggregate state | PASS | Empirical accessibility remains `NOT_RUN`; mapping incomplete; aggregate blockers open; XAG 121–123 unaccepted; no stronger authority is claimed. |

## Mechanical load-bearing checks

`ACCESSIBILITY-POLICY-VALIDATOR-v14` contains explicit fixtures for both sides of the remediation:

- accessible notification-management with neither example control present -> `PASS`;
- existing accessible duration control -> `PASS`;
- existing inaccessible duration control -> reject;
- existing inaccessible notification toggle -> reject;
- universal feature-existence promotion of both examples -> reject;
- inaccessible notification-management settings -> reject.

Adversarial fixtures also reject identity, trigger, authority/modality, evidence/gap, unrelated-record, preserved-correction, evidence-state, aggregate-state, and full-review-scope drift.

## Preservation and authority boundary

The reviewed correction lineage remains fail-closed through XAG 117. The exact inventories remain:

- XAG 112: `14`
- XAG 114: `16`
- XAG 108–123: `113`
- inherited XAG 101–107: `105`
- composed XAG 101–123: `218`

The review does **not** establish any of the following:

```yaml
xag_121_123_accepted: false
full_xag_108_123_review_complete: false
empirical_accessibility_evidence: NOT_RUN
empirical_accessibility_successor_eligible: false
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
readiness_authority: false
implementation_authority: false
release_authority: false
legal_or_compliance_authority: false
platform_certification_authority: false
verification_pass_authority: false
decision_authority: false
integration_authority_by_review_alone: false
canonicality: NOT_CANONICAL
```

PR mergeability, draft state, or this review result cannot substitute for a separately authorized integration episode. Any main integration remains squash-only and must re-freeze then-current `main`, exact producer head, compatibility, and integration ownership.

## Findings and disposition

```yaml
review_disposition: CLEAN_FOR_NONCANONICAL_INTEGRATION
findings:
  blockers: 0
  majors: 0
  correction_requiring_minors: 0
finding_state: RESOLVED_BOUNDED_REVIEWED
reviewed_finding: W2-REV-ACC19-M01
reviewed_atom: XAG120-COMM-NOTIFICATION-SETTINGS
```

No material defect remains in the exact Issue #310 remediation scope. The producer packet is clean for the separately authorized squash-only noncanonical integration route. This review does not itself authorize integration and does not accept XAG 121–123.

After an authorized integration of the producer and required-review provenance as repository routing permits, full XAG 108–123 review must continue from the still-unaccepted XAG 121–123 remainder before empirical accessibility work can become eligible.
