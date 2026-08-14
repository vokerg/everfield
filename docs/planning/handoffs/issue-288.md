# Issue #288 handoff — W2-REM-ACC-12

## Identity

- Mission: `W2-REM-ACC-12`
- Task class: blocking bounded remediation
- Branch: `planning/issue-288`
- Winning claim: Issue #288 comment `5294237608`
- Claim base: `main@d8445512718e00c8f223f9249b433b471ac2b70c`
- Producer actor/session: `w2-rem-acc-12-gpt56sol-20260814-1601-frontier`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

The claim was the sole valid claim at the immediate ownership re-check. Every branch mutation was preceded by an ownership and expected-head re-check.

## Controlling review and immutable input

- Required full-review continuation: Issue #287 / `W2-REV-ACC-13`
- Review winning claim: `5293624794`
- Review terminal: `5293661376`
- Review disposition: `CHANGES_NEEDED`
- Finding: `W2-REV-ACC13-M01` / MAJOR / `SOURCE_LOGICAL_OPERATOR_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`
- Review exact head: `539f8bfe35f0b25854cc7d740bbf3ca8b215d829`
- Review work: `04ed012577d85eba5d060fe88a5d89b192163e57`
- Review provenance PR: #289, squash-integrated at `main@d8445512718e00c8f223f9249b433b471ac2b70c`
- Immutable policy v10 blob: `12c1af5bd6ae88a549e575c594f8ec2afa387705`
- Immutable report v10 blob: `fc826cf315b0bda8308aecbc63364f6977be39d1`
- Inherited XAG 108–123 origin policy blob: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`

Current first-party Microsoft XAG 115 was re-observed on 2026-08-14 at `https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/115`; the page remains XAG v3.2 / last updated 2026-03-04 and retains the stored-data rule requiring an opportunity to review and correct the data or completely reverse the action before committing it.

## Remediation packet

First substantive work commit: `9b41312ef86bfb68a31e6b0dc0177d8512fe1a7b`.

Artifacts:

- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`
  - v11 overlay blob: `b57c0aae729085c672ae9746179d76afb866a721`
- `docs/planning/wave-2/research/accessibility-current-requirements.md`
  - v11 report blob: `cb6b2ba3d1226c912874a89a369e9acf7912a034`
- this handoff

The v11 overlay changes only `XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE` plus minimum validator/report metadata. The corrected machine-readable operator is equivalent to:

```text
(review AND correct) OR complete_reverse_or_cancel
```

and is represented as `any_of(all_of(review, correction), complete_reverse_or_cancel)`.

## Load-bearing oracles

The remediation requires all four witnesses:

1. review only → reject;
2. correction only → reject;
3. review + correction → pass;
4. complete reversal/cancellation → pass.

Adversarial fixtures also reject accepting either incomplete path, rejecting either complete source-valid path, changing trigger/evidence/gap routing, changing unrelated XAG 115 semantics, regressing reviewed XAG 112/XAG 114/XAG 116 corrections, changing aggregate counts, or inflating fail-closed authority state.

## Preservation and self-review

Producer-side comparison from claim base through the substantive report commit showed exactly two modified files: the accessibility policy and report, with no unrelated path changes. The subsequent handoff adds only this provenance file.

Preserved identity/count state:

```yaml
xag_114_atomic_clause_count: 16
xag_112_atomic_clause_count: 14
xag_108_123_atomic_clause_count: 113
inherited_xag_101_107_atomic_clause_count: 105
composed_xag_101_123_atomic_clause_count: 218
```

Bounded producer self-review result:

```yaml
finding: W2-REV-ACC13-M01
finding_state: RESOLVED_PENDING_FRESH_SCOPED_REVIEW
unresolved_blockers: 0
unresolved_majors: 0
correction_requiring_minors: 0
scope_leakage_found: false
producer_self_review_substitutes_independent_review: false
```

## Preserved fail-closed authority state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_115_remainder_accepted: false
xag_116_123_accepted_by_issue_287: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

## Required next

A fresh independent/degraded-independent scoped review of this exact v11 remediation packet is mandatory. That review must treat this producer branch as immutable input, re-check the source operator and all four witnesses, and verify that no unrelated XAG semantics or fail-closed state changed.

A clean scoped review may only make this exact producer packet eligible for a separately authorized squash-only noncanonical integration decision. It does not accept the XAG 115–123 remainder left unreviewed by Issue #287 and does not create empirical accessibility, readiness, verification-PASS, decision, or canonical authority.
