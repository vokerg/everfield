# W2-REM-ACC-16 — correct XAG 122 named accessible support-method weakening

**Mission:** `W2-REM-ACC-16` / Issue #319  
**Winning claim:** comment `5297064545`  
**Claim base:** `main@39bda0cc8cfce8273e1e425efd72ec760dc0b4a4`  
**Required full-review continuation:** Issue #316 winning claim `5297013118`, terminal `CHANGES_NEEDED` comment `5297053703`, review head `ec7c3fd306649ece3968c612e01847c50bf4bc55`, work `e0304f34365cd6c6ff40a9eb61a3ef1827e66519`  
**Finding:** `W2-REV-ACC21-M01` / MAJOR — `SOURCE_NAMED_SUPPORT_METHOD_SET_WEAKENING`  
**Immutable producer input:** policy v14 blob `33c4fdcde1c28ed2623496b04d2d376d4aac190b`, report v14 blob `b8c5cb0e7394b21f99ca9e09275cd145d59bba1b`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope and source binding

Issue #316 resumed the still-unaccepted XAG 121–123 mapping remainder. It accepted all six XAG 121 records with no material finding, attacked `XAG122-SUPPORT-NO-EXTRA-COST` with no material finding, then terminalized early on the second XAG 122 atom. XAG 123 therefore remains unaccepted.

Fresh first-party Microsoft XAG 122 was re-read on `2026-08-14`:

- `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/122`
- XAG v3.2 lineage; page last updated `2026-03-04`.

The Implementation guidelines state that multiple accessible methods should be available to contact support, including phone, TTY, email, and chat. The four named methods are inside the source `SHOULD` directive rather than introduced as a separate illustrative example list.

## 2. Exact inherited defect

The exact inherited atom resolved through v14 is:

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

The identity, source, best-practice authority, `SHOULD` modality, conditional applicability, trigger, evidence route, and gap route are not the finding. The defect is that the source-named method set is modeled as `supported_examples`. A candidate can satisfy the only load-bearing semantic—an unspecified plurality—while omitting one or more of phone, TTY, email, or chat.

## 3. Bounded v15 correction

The v15 overlay changes only the semantic treatment of that named set:

```yaml
XAG122-MULTIPLE-ACCESSIBLE-SUPPORT-METHODS:
  source_id: XAG-122
  authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE
  source_modality: SHOULD
  applicability: CONDITIONAL
  trigger: customer_support_is_offered
  required_semantics:
    multiple_accessible_support_methods_available: true
    required_accessible_support_methods:
      - phone
      - tty
      - email
      - chat
  evidence_requirement_refs:
    - ACC-EV-XAG122
  gap_ref: ACC-GAP-XAG122
```

This makes each source-named method mechanically load-bearing when customer support is offered while preserving XAG 122 as accessibility best-practice `SHOULD` guidance. It does not create legal/compliance, platform-certification, or `MUST` authority.

`XAG122-SUPPORT-NO-EXTRA-COST` remains unchanged.

## 4. Load-bearing mechanical oracles

`ACCESSIBILITY-POLICY-VALIDATOR-v15` requires all four source-named methods and rejects substitution:

| Candidate | Expected |
| --- | --- |
| phone + TTY + email + chat accessible | `PASS` |
| phone omitted | `REJECT_NAMED_SUPPORT_METHOD_OMISSION` |
| TTY omitted | `REJECT_NAMED_SUPPORT_METHOD_OMISSION` |
| email omitted | `REJECT_NAMED_SUPPORT_METHOD_OMISSION` |
| chat omitted | `REJECT_NAMED_SUPPORT_METHOD_OMISSION` |
| unrelated plurality such as web form + postal mail substitutes for named set | `REJECT_NAMED_SUPPORT_METHOD_SET_WEAKENING` |
| mapping inflates source to `MUST`/compliance authority | `REJECT_AUTHORITY_INFLATION` |

Additional adversarial assertions reject mutation of the atom identity, trigger, authority/modality, evidence/gap routing, `XAG122-SUPPORT-NO-EXTRA-COST`, any XAG 121 record accepted by Issue #316, any previously reviewed correction, or any unrelated v14-composed record.

## 5. Preservation proof

The v15 overlay consumes exact v14 as immutable input and replaces only the XAG 122 named-method semantic encoding described above.

Preserved review lineage includes:

- XAG 112 navigation corrections;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data `(review AND correct) OR complete reverse/cancel` operator;
- XAG 115 permanent/destructive-action `review AND confirmation AND undo` conjunction;
- XAG 115 no-button-hold record;
- XAG 116 reviewed timing correction;
- XAG 117 camera-view required-if-applicable / `SHOULD` correction;
- XAG 120 notification-management accessibility without example-feature existence inflation;
- all six XAG 121 records accepted by Issue #316;
- XAG 122 no-extra-cost support atom.

Inventory remains unchanged:

- XAG 112: **14** atomic records;
- XAG 114: **16** atomic records;
- XAG 108–123: **113** atomic records;
- inherited XAG 101–107: **105** atomic records;
- composed XAG 101–123: **218** atomic records.

No identity is added, removed, split, or renamed.

## 6. Finding disposition and producer self-review

`W2-REV-ACC21-M01` is **RESOLVED_PENDING_FRESH_SCOPED_REVIEW** in this producer packet:

- unspecified plurality still sufficient while source-named methods are absent: **NO**;
- phone load-bearing: **YES**;
- TTY load-bearing: **YES**;
- email load-bearing: **YES**;
- chat load-bearing: **YES**;
- unrelated methods can substitute for omitted source-named methods: **NO**;
- atom identity/source/authority/modality/applicability/trigger changed: **NO**;
- evidence or gap route changed: **NO**;
- no-extra-cost atom changed: **NO**;
- accepted XAG 121 scope changed: **NO**;
- reviewed XAG 108–120 corrections changed: **NO**;
- atomic counts changed: **NO**;
- `MUST`, legal/compliance, or platform-certification authority invented: **NO**;
- XAG 123 acceptance claimed: **NO**;
- empirical accessibility eligibility or PASS claimed: **NO**.

Bounded producer self-review finds **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR** in this exact remediation scope. Producer self-review does not satisfy the mandatory fresh independent/degraded-independent scoped review.

## 7. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
empirical_accessibility_successor_eligible: false
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_121_review: ACCEPTED_NO_MATERIAL_FINDING_BY_ISSUE_316
xag_123_review: UNACCEPTED
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

This bounded repair does not accept XAG 123, make empirical accessibility evidence eligible, clear aggregate blockers, create readiness/implementation/release authority, or grant verification, integration, decision, or canonical authority.

## 8. Required next transition

Freeze this exact remediation in an exact-head draft PR and perform a fresh independent/degraded-independent scoped review. That review must independently re-read current XAG 122, verify each source-named support method is load-bearing, attack omission/substitution and authority inflation, prove identity/trigger/evidence/gap/no-extra-cost/XAG 121 preservation, and verify inventory/fail-closed invariants.

A clean scoped review may make this exact producer packet eligible only for the separately authorized squash-only noncanonical integration route. After the bounded correction chain is integrated as authorized, the required full mapping review must resume from the still-unaccepted XAG 123 remainder before any empirical-accessibility successor can be derived.
