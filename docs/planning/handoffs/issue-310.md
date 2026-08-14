# Issue #310 handoff — W2-REM-ACC-15

## Ownership and frozen inputs

- Winning claim: `5296883667`
- Actor/session: `w2-rem-acc-15-gpt56sol-20260814-2039-frontier`
- Branch: `planning/issue-310`
- Producer base: `main@65d4eb8144e33d8e247c0dc0a688f6811a4225bb`
- Canonical Planning Program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Immutable input policy v13 blob: `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`
- Immutable input report v13 blob: `e5f1f491a91499bef96861d2878e4fb5552a207b`
- Source required-review issue: #308 / `W2-REV-ACC-19`
- Source-review winning claim: `5296830252`
- Source-review terminal: `5296868370`
- Source-review exact head/work: `024efaa4cc97b5af6e669cf9100b5172a2096bd4` / `ed51563510cee7cd24463a6d1a169ec3f0f2ea3e`
- Source finding: `W2-REV-ACC19-M01 / MAJOR / EXAMPLE_TO_REQUIREMENT_PROMOTION_AND_FEATURE_EXISTENCE_INFLATION`
- Source review PR #311 is separate review provenance. Its integration is not a prerequisite for this exact terminal finding and was not touched by this producer.

## Producer output

- Policy: `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`
- Policy v14 blob: `33c4fdcde1c28ed2623496b04d2d376d4aac190b`
- Report: `docs/planning/wave-2/research/accessibility-current-requirements.md`
- Report v14 blob: `b8c5cb0e7394b21f99ca9e09275cd145d59bba1b`
- Substantive producer work SHA: `71b3fddda8d8133514574775848b19b401a2f0d1`
- Finding state in producer packet: `RESOLVED_PENDING_FRESH_SCOPED_REVIEW`

## Exact bounded correction

The inherited atom `XAG120-COMM-NOTIFICATION-SETTINGS` keeps its identity, XAG 120 source, `BEST_PRACTICE_REQUIRED_IF_APPLICABLE / SHOULD` authority, conditional applicability, trigger `communication_notifications_are_available`, evidence `ACC-EV-XAG120`, and gap `ACC-GAP-XAG120`.

The corrected semantic contract is:

- applicable notification-management UI/settings remain required to be accessible;
- the source examples of notification display-duration adjustment and notification on/off controls are no longer universal product-feature-existence requirements;
- when either example control exists, its UI remains inside the accessibility obligation and must not fail open;
- absence of either example control does not independently fail XAG 120;
- no communication or notification feature is invented where the title does not offer it.

`ACCESSIBILITY-POLICY-VALIDATOR-v14` includes positive no-feature-invention fixtures and negative fixtures for inaccessible existing controls, example promotion, scope leakage, preserved-correction regression, empirical evidence inflation, and aggregate-state inflation.

## Preservation and self-review

Preserved reviewed lineage:

- XAG 112 navigation corrections;
- XAG 114 `titles` reading-level exception;
- XAG 115 stored-data operator;
- XAG 115 permanent-action conjunction;
- XAG 115 no-button-hold semantics;
- XAG 116 default-over-20-hours/timing correction;
- XAG 117 camera-view required-if-applicable `SHOULD` correction.

Preserved exact inventory:

- XAG 112 = `14`;
- XAG 114 = `16`;
- XAG 108–123 = `113`;
- inherited XAG 101–107 = `105`;
- composed XAG 101–123 = `218`.

Bounded producer self-review: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** within this exact remediation scope. Producer self-review does not substitute for required independent review.

## Required review routing

- Exactly one required scoped review successor was routed: Issue #313 / `W2-REV-ACC-20`.
- #313 is `BLOCKED_PENDING_PRODUCER_TERMINAL` until this issue publishes terminal `STATUS(REVIEW_READY)` binding the exact producer head/work/blobs/PR.
- Review must independently re-read current XAG 120 and attack both feature-existence inflation and accessibility weakening for controls that exist.
- A clean #313 review may create only separately authorized noncanonical squash-integration eligibility for this exact remediation.

## Remaining authority boundary

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_121_123_accepted_by_issue_308: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized_by_producer: false
canonicality: NOT_CANONICAL
```

No empirical-accessibility successor is eligible. XAG 121–123 remain unaccepted. No readiness, implementation, release, legal/compliance, platform certification, verification-PASS, decision, integration, or canonical authority is created by this producer packet.

## Next transition

Open and verify an exact-head draft producer PR containing only policy v14, report v14, and this handoff, then publish terminal schema-3 `STATUS(REVIEW_READY)` with exact identities and successor #313. The mandatory scoped review must occur before any integration eligibility.