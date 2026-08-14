# Issue #287 handoff — W2-REV-ACC-13

## Identity

- Mission: `W2-REV-ACC-13`
- Task class: required full-review continuation / recovery
- Branch: `planning/issue-287`
- Winning claim: Issue #287 comment `5293624794`
- Claim base: `main@ca56ff61fb383435f4d68cfc83fe9e3eb2bd1594`
- Reviewer actor/session: `w2-rev-acc-13-gpt56sol-20260814-1505-frontier`
- Trust profile: `DEGRADED_SINGLE_AGENT`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

The claim was the sole valid claim at the immediate ownership re-check. The branch was created from exact current main before review mutation.

## Frozen reviewed mapping

- Current review base: `ca56ff61fb383435f4d68cfc83fe9e3eb2bd1594`
- Current policy v10 blob: `12c1af5bd6ae88a549e575c594f8ec2afa387705`
- Current report v10 blob: `fc826cf315b0bda8308aecbc63364f6977be39d1`
- Inherited XAG 108–123 origin policy blob: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`
- Controlling early-negative review: Issue #281 terminal `5293245321`
- Bounded XAG 114 remediation: Issue #282 terminal `5293294510`, integration status `5293554714`
- Clean scoped review of exact remediation: Issue #285 terminal `5293359630`, integration status `5293590999`

## Review artifact

- `docs/planning/wave-2/reviews/w2-rem-acc-13-full-mapping-review.md`
- Review artifact blob: `bb310eefcf88d67aef71e971064ff12e0edb48ab`
- First substantive review commit: `04ed012577d85eba5d060fe88a5d89b192163e57`
- Disposition: `CHANGES_NEEDED`

## Continuation coverage before early termination

Issue #281 explicitly left the remainder of XAG 114 and XAG 115–123 unaccepted after its XAG 114 title-exception finding. This episode resumed that sequence.

Fresh Microsoft XAG 114 re-read confirmed the post-reading-level visual-preview remainder: provide a visual simulation showing how a setting affects the UI, with realistic game-environment context when possible. The inherited `XAG114-SETTING-EFFECT-PREVIEW` record preserves that required/recommended split. Combined with Issue #285's exact clean title-exception review, no new XAG 114 remainder finding is routed here.

The continuation then reached XAG 115 and established one reproducible MAJOR. Per the task's early-negative rule, later XAG 115 surfaces and XAG 116–123 remain unaccepted by this episode.

## Material finding

### `W2-REV-ACC13-M01` — MAJOR / OPEN_BOUNDED

Fresh current first-party Microsoft XAG 115 review establishes this stored-data protection rule: when a player action will delete or modify stored data they control, provide an opportunity to **review and correct the data or completely reverse the action before committing it**.

The inherited current composed record is:

```yaml
XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE:
  trigger: player_action_deletes_or_modifies_player_controlled_stored_data
  required_semantics:
    opportunity_to_review_or_correct_or_reverse_before_commit: true
```

The source's operator structure is `(review AND correct) OR complete_reverse`; the mapping weakens it to `review OR correct OR reverse`.

A review-only flow can therefore satisfy the mapped record even though it offers neither correction nor complete reversal/cancellation. The inherited validator has no load-bearing XAG 115 oracle that rejects review-only or correction-only candidates while accepting the two source-valid alternatives. v9 and v10 explicitly preserve unrelated inherited semantic records, so this defect remains in the current composition.

This is `SOURCE_LOGICAL_OPERATOR_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`. `CLEAN_FOR_EMPIRICAL_ACCESSIBILITY_SUCCESSOR` is unavailable.

## Routed successor

- Issue #288 / `W2-REM-ACC-12`
- State at creation: `BLOCKED_PENDING_REVIEW_TERMINAL`
- Scope: only repair `XAG115-DATA-MODIFICATION-REVIEW-CORRECT-REVERSE` so the machine-readable contract represents `(review AND correct) OR complete_reverse` and make operator weakening mechanically rejectable.
- Required fixtures: reject review-only; reject correction-only; accept review+correct; accept complete reversal/cancellation.
- Preserve identity, trigger, source modality, evidence/gap routing, all unrelated XAG semantics, and reviewed XAG 112/XAG 114/XAG 116 corrections.
- Do not broaden into the separate XAG 115 permanent/destructive-action or button-hold records without an independently established finding.
- Fresh independent/degraded-independent scoped review remains mandatory after remediation.
- A later full-review continuation remains required for all XAG 115–123 remainder not accepted by this early-negative episode.

## Preserved aggregate state

```yaml
review_disposition: CHANGES_NEEDED
blockers: 0
majors: 1
correction_requiring_minors: 0
finding_id: W2-REV-ACC13-M01
finding_state: OPEN_BOUNDED
full_review_terminated_early: true
xag_114_remainder_reviewed_without_new_finding: true
xag_115_remainder_accepted: false
xag_116_123_accepted_by_this_continuation: false
full_xag_108_123_review_complete: false
empirical_accessibility_successor_eligible: false
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authority_created: false
canonicality: NOT_CANONICAL
```

## Required next

1. Open an exact-head draft PR containing only this review and handoff provenance.
2. Verify PR head/base/changed-file scope.
3. Publish terminal schema-3 `STATUS(REVIEW_READY)` on Issue #287 with disposition `CHANGES_NEEDED`, exact reviewed identities, review/handoff blobs, finding `W2-REV-ACC13-M01`, and successor #288.
4. Do not derive an empirical accessibility successor from this review.
5. After terminalization, Issue #288 is the blocking-remediation continuation if unowned and otherwise eligible.

This handoff records noncanonical negative review provenance only. It grants no empirical accessibility PASS, mapping completion, full corrected XAG 108–123 acceptance, readiness/implementation/release, legal/compliance status, platform certification, verification PASS, integration authority, decision authority, or canonical authority.
