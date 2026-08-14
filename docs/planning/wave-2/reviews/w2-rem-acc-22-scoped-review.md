# W2-REV-ACC-22 — scoped review of XAG 122 named accessible support-method remediation

## Review identity

- Mission: `W2-REV-ACC-22`
- Issue: `#321`
- Winning claim: `5297104041`
- Actor/session: `w2-rev-acc-22-gpt56sol-20260814-2103-frontier`
- Trust mode: `DEGRADED_INDEPENDENT`
- Review branch/base: `planning/issue-321` from `main@1d902f7e78b3537020dec01c9bb2516016f21fc0`
- Canonical Planning Program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

The claim was immediately re-fetched before branch mutation and no earlier valid claimant existed. This review is distinct from Issue #319 production and Issue #316 full-review work.

## Frozen producer and source-review inputs

Producer packet:

- Issue `#319` / `W2-REM-ACC-16`
- winning producer claim `5297064545`
- terminal `STATUS(REVIEW_READY)` comment `5297097682`
- terminal producer head `8f56a8da6fec83e8ff8eb38780d29c4340f73691`
- first substantive work `bf9e96aaa261c75f78f30cf1229e71c9581d27e1`
- draft PR `#320`
- candidate policy v15 blob `bba27a68a6922751c4b2c1ccdc3a6c164ac3a2dd`
- candidate report v15 blob `b46e924dff194a61993d445ad66cbee5fb79d1df`
- producer handoff blob `627a4b94ff10fcca8729f3b477b13b13d97942fe`

Immutable v14 inputs on current `main`:

- policy blob `33c4fdcde1c28ed2623496b04d2d376d4aac190b`
- report blob `b8c5cb0e7394b21f99ca9e09275cd145d59bba1b`
- inherited XAG 108–123 origin policy blob `80e278315d6b7a108d89da3f5a99086a8ef91bf7`

Source full-review provenance:

- Issue `#316` / `W2-REV-ACC-21`
- winning claim `5297013118`
- terminal review `5297053703`
- exact review head/work `ec7c3fd306649ece3968c612e01847c50bf4bc55` / `e0304f34365cd6c6ff40a9eb61a3ef1827e66519`
- disposition `CHANGES_NEEDED`
- finding `W2-REV-ACC21-M01 / MAJOR / SOURCE_NAMED_SUPPORT_METHOD_SET_WEAKENING`
- affected atom `XAG122-MULTIPLE-ACCESSIBLE-SUPPORT-METHODS`
- accepted in that episode: all six XAG 121 records and `XAG122-SUPPORT-NO-EXTRA-COST`
- still unaccepted: XAG 123.

## Fresh first-party source recheck

Re-read Microsoft Xbox Accessibility Guideline 122 on `2026-08-14` from the current Microsoft Learn page:

`https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/122`

The page identifies XAG 122 as **Accessible customer support**, reports a last-updated date of `2026-03-04`, and places the following directive in the Implementation guidelines:

- multiple accessible methods **should** be made available to contact support;
- the directive names phone, TTY, email, and chat with `including` language;
- the names occur inside that directive rather than in a separately qualified example-only list.

The parent Xbox Accessibility Guidelines page characterizes the XAGs as best practices and explicitly says they are not intended as a compliance/legal-validation checklist. The repository-native `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD` authority therefore remains the correct bounded mapping; this review does not promote XAG 122 to `MUST`, legal/compliance, or platform-certification authority.

## Exact producer-scope attack

PR #320 is draft, mergeable at review time, based on `main@1d902f7e78b3537020dec01c9bb2516016f21fc0`, and freezes exact head `8f56a8da6fec83e8ff8eb38780d29c4340f73691`.

The changed-file set is exactly three files:

- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`
- `docs/planning/wave-2/research/accessibility-current-requirements.md`
- `docs/planning/handoffs/issue-319.md`

Current `main` still carries the exact v14 policy/report input blobs. The producer v15 composition contract binds those exact immutable inputs and the inherited XAG 108–123 origin, then replaces only the inherited semantic treatment of `XAG122-MULTIPLE-ACCESSIBLE-SUPPORT-METHODS` plus the minimum producer/report/validator metadata needed to make the correction auditable.

No XAG identity is added, removed, split, or renamed by the bounded overlay.

## Atom reconstruction and source fidelity

The inherited atom carries:

```yaml
XAG122-MULTIPLE-ACCESSIBLE-SUPPORT-METHODS:
  source_id: XAG-122
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: customer_support_is_offered
  required_semantics:
    multiple_accessible_support_methods_available: true
    supported_examples:
      - phone
      - tty
      - email
      - chat
  evidence_requirement_refs:
    - ACC-EV-XAG122
  gap_ref: ACC-GAP-XAG122
```

That encoding admits the defect reproduced by Issue #316: an unspecified plurality can satisfy the load-bearing requirement while one or more source-named support methods are missing or inaccessible.

The v15 patch preserves atom identity, source, authority, modality, applicability, trigger, evidence, and gap, while replacing the example-only treatment with:

```yaml
required_semantics:
  multiple_accessible_support_methods_available: true
  required_accessible_support_methods:
    - phone
    - tty
    - email
    - chat
```

This is source-faithful for the current XAG 122 wording: each named method becomes a load-bearing member of the mapped support-method set when customer support is offered, while the entire requirement remains best-practice `SHOULD` guidance.

`XAG122-SUPPORT-NO-EXTRA-COST` is not redefined by the overlay and remains an immutable preservation contract from the exact v14 composition.

## Required attack results

| Attack | Result | Basis |
| --- | --- | --- |
| Exact producer terminal identity | PASS | Terminal `5297097682` binds head/work/PR and v15 blobs exactly. |
| PR head/base/scope | PASS | PR #320 freezes head `8f56a8d…`, base `1d902f7…`, and exactly the declared policy/report/handoff files. |
| First-party XAG 122 re-read | PASS | Current Microsoft guidance says multiple accessible methods should be available, including phone, TTY, email, and chat. |
| Best-practice authority | PASS | XAG corpus is best-practice guidance, not a legal/compliance checklist; v15 preserves `SHOULD`. |
| Bounded v15-over-v14 composition | PASS | v15 binds exact v14 policy/report and changes the named-method treatment for one inherited atom plus audit/validator metadata. |
| Atom/source identity | PASS | `XAG122-MULTIPLE-ACCESSIBLE-SUPPORT-METHODS` / `XAG-122` unchanged. |
| Authority/modality/applicability | PASS | `BEST_PRACTICE_REQUIRED_IF_APPLICABLE`, `SHOULD`, `CONDITIONAL`, and `customer_support_is_offered` preserved. |
| Evidence/gap routing | PASS | `ACC-EV-XAG122` and `ACC-GAP-XAG122` preserved. |
| All named methods accessible | PASS | v15 fixture with phone + TTY + email + chat is the positive witness. |
| Phone omitted | PASS | Explicit negative fixture rejects omission. |
| TTY omitted | PASS | Explicit negative fixture rejects omission. |
| Email omitted | PASS | Explicit negative fixture rejects omission. |
| Chat omitted | PASS | Explicit negative fixture rejects omission. |
| Unrelated-method substitution | PASS | web-form/postal-mail plurality is explicitly rejected as named-set weakening. |
| Authority inflation | PASS | `MUST` / compliance mutation is explicitly rejected. |
| No-extra-cost sibling preservation | PASS | v15 declares it byte-logically unchanged and rejects mutation as scope leakage. |
| XAG 121 accepted-scope preservation | PASS | all six accepted XAG 121 records are immutable preservation inputs and mutation is explicitly rejected. |
| Reviewed XAG 108–120 corrections | PASS | XAG 112, 114, 115, 116, 117, and 120 reviewed contracts remain declared preservation invariants. |
| Inventory preservation | PASS | XAG 112=`14`; XAG 114=`16`; XAG 108–123=`113`; inherited XAG 101–107=`105`; composed XAG 101–123=`218`. |
| Fail-closed aggregate state | PASS | XAG 123 remains unaccepted; empirical accessibility remains `NOT_RUN`/ineligible; mapping incomplete; blockers open. |

## Mechanical load-bearing checks

`ACCESSIBILITY-POLICY-VALIDATOR-v15` makes the correction mechanically reviewable rather than descriptive-only:

- phone + TTY + email + chat accessible -> `PASS`;
- each individual named-method omission -> `REJECT_NAMED_SUPPORT_METHOD_OMISSION`;
- unrelated methods substituted for the source-named set -> `REJECT_NAMED_SUPPORT_METHOD_SET_WEAKENING`;
- source authority inflated to `MUST` / compliance -> `REJECT_AUTHORITY_INFLATION`;
- leaving the named methods as example-only metadata -> reject;
- mutation of the no-extra-cost sibling, atom identity, trigger, authority/modality, evidence/gap route, any accepted XAG 121 record, or any unrelated v14-composed record -> reject;
- regression of reviewed XAG 112/114/115/116/117/120 corrections -> reject;
- claiming XAG 123 acceptance, empirical PASS, or `mapping_complete: true` -> reject.

The positive and negative witnesses close the exact false-PASS path identified by `W2-REV-ACC21-M01`: an unspecified plurality can no longer substitute for an omitted source-named method.

## Preservation and fail-closed authority boundary

The exact inventories remain:

- XAG 112: `14`
- XAG 114: `16`
- XAG 108–123: `113`
- inherited XAG 101–107: `105`
- composed XAG 101–123: `218`

The review preserves the following state:

```yaml
xag_121_review: ACCEPTED_NO_MATERIAL_FINDING_BY_ISSUE_316
xag122_support_no_extra_cost: NO_MATERIAL_FINDING_BY_ISSUE_316
xag_123_review: UNACCEPTED
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

PR mergeability, draft state, producer `REVIEW_READY`, or this review disposition do not independently grant integration authority. Any integration must be a separate, freshly owned, squash-only episode under repository authority.

## Findings and disposition

```yaml
review_disposition: CLEAN_FOR_NONCANONICAL_INTEGRATION
findings:
  blockers: 0
  majors: 0
  correction_requiring_minors: 0
finding_state: RESOLVED_BOUNDED_REVIEWED
reviewed_finding: W2-REV-ACC21-M01
reviewed_atom: XAG122-MULTIPLE-ACCESSIBLE-SUPPORT-METHODS
```

No material defect remains in the exact Issue #319 remediation scope. The producer packet is clean for consideration by the separately authorized squash-only noncanonical integration route.

This review does not itself authorize a merge, does not accept XAG 123, and does not make empirical accessibility work eligible. After authorized publication of the producer/review chain as repository routing permits, the required full XAG 108–123 review must resume from the still-unaccepted XAG 123 remainder before any empirical-accessibility successor can be derived.
