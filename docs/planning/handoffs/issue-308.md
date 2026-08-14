# Issue #308 handoff — W2-REV-ACC-19

## Ownership and contention

- Winning claim: `5296830252`
- Actor/session: `w2-rev-acc-19-gpt56sol-20260814-2031-frontier`
- Trust mode: `DEGRADED_INDEPENDENT`
- Branch: `planning/issue-308`
- Review base: `main@65d4eb8144e33d8e247c0dc0a688f6811a4225bb`
- Canonical Planning Program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Current integrated policy v13 blob: `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`
- Current integrated report v13 blob: `e5f1f491a91499bef96861d2878e4fb5552a207b`
- Inherited XAG 108–123 origin blob: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`
- Duplicate Issue #309 was independently created for the same mission/base/scope. Its claim `5296831044` is later than winning claim `5296830252`; Issue #309 was durably closed as duplicate with recovery comment `5296849298`. No task-branch edits from #309 are authoritative for this mission.

## Frozen predecessor lineage

- Issue #302 terminal required review: `5296708193`, head `6327b6b6708f5159b20e37ffe5b348963bd5d8bb`, work `1e33561de0e2afa76836910cd947b06934c0cfd4`, disposition `CHANGES_NEEDED`, terminal boundary XAG 117.
- Issue #303 producer terminal: `5296754811`, head `09f4f3eee194b7ffa57b668db63421c8397a15b5`, work `edd2de28df9c246066dd9db5e6b436d635157ef4`; integrated squash at `e8c30602e94e857ffb52d05a72e9b2c3615bd581`, integration claim `5296792164`, status `5296800479`.
- Issue #306 terminal scoped review: `5296785707`, head `c89a507b7c01be3f3c611718923859a2967fd3d3`, work `8e95ed5a2d6efa4f84689c23f6b748c1dbe84c69`, disposition `CLEAN_FOR_NONCANONICAL_INTEGRATION`; integrated squash at `65d4eb8144e33d8e247c0dc0a688f6811a4225bb`, integration claim `5296798277`.
- Current v13 changes only the XAG 117 camera-view authority/modality metadata relative to v12 and preserves every other composed semantic record and fail-closed state.

## Review output

- Review artifact: `docs/planning/wave-2/reviews/w2-rem-acc-19-full-mapping-review.md`
- Review artifact blob: `0e896c17fa20dc7cc9260ae02ddd6dc8aa167080`
- Substantive review work SHA: `ed51563510cee7cd24463a6d1a169ec3f0f2ea3e`
- Disposition: `CHANGES_NEEDED`
- Unresolved BLOCKER: `0`
- Unresolved MAJOR: `1`
- Correction-requiring MINOR: `0`
- Terminal boundary: XAG 120 communication-notification settings; XAG 121–123 remain unaccepted.

## Finding

`W2-REV-ACC19-M01 / MAJOR / EXAMPLE_TO_REQUIREMENT_PROMOTION_AND_FEATURE_EXISTENCE_INFLATION`

Fresh Microsoft XAG 120 requires the necessary UI/settings used to configure communication experiences to be accessible and introduces concrete notification controls as examples. The inherited current atom `XAG120-COMM-NOTIFICATION-SETTINGS` is triggered whenever `communication_notifications_are_available` and then requires `notification_duration_adjustable_when_timed: true` plus `notifications_can_be_turned_on_or_off: true` as product capabilities. This promotes example settings into universal required feature existence and can false-fail an implementation whose existing notification-management controls are accessible but which does not provide one or both example capabilities.

No earlier material finding was established in the XAG 118 photosensitivity or XAG 119 STT/TTS attacks. The episode validly stops at the first reproducible MAJOR and does not claim acceptance of XAG 121–123.

## Successor routing

- Exactly one bounded remediation successor was created: Issue #310 / `W2-REM-ACC-15`.
- Issue #310 remains `BLOCKED_PENDING_REVIEW_TERMINAL` until this issue publishes terminal `STATUS(REVIEW_READY)` binding the exact finding and terminal head.
- Required correction is limited to `XAG120-COMM-NOTIFICATION-SETTINGS` plus minimum validator/report metadata: keep accessibility of applicable notification-management UI normative, while gating concrete duration/toggle semantics on those controls existing or representing them as source examples/recommendations.
- Fresh independent/degraded-independent scoped review of the exact remediation is mandatory before any integration eligibility.

## PR freeze

- Draft review PR: `#311`.
- PR base branch: `main`.
- PR base/head before terminal: `65d4eb8144e33d8e247c0dc0a688f6811a4225bb` / `b1bdc400638a5e035e68dc70393b6cbadb3959c3`.
- `main` remained exact `65d4eb8144e33d8e247c0dc0a688f6811a4225bb` through the compatibility check.
- PR #311 recalculated `mergeable: true`, remains `draft: true`, and its changed-file set is exactly the two declared review-provenance files.
- Mergeability is compatibility only. This review does not grant its own integration authority.

## Remaining boundary

- XAG 121–123: unaccepted by this review episode.
- Empirical accessibility: `NOT_RUN`.
- `mapping_complete: false`.
- `IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN`.
- `W2-REV-M02: OPEN_BOUNDED`.
- Full corrected XAG 108–123 review: incomplete.
- No readiness, implementation, release, legal/compliance, platform certification, verification-PASS, integration, decision, or canonical authority.

## Next transition

Publish terminal schema-3 `STATUS(REVIEW_READY)` with disposition `CHANGES_NEEDED`, finding `W2-REV-ACC19-M01`, exact work/head/blob identities, draft PR #311, successor #310, and the XAG 121–123 unaccepted boundary. Any later review-provenance integration remains separately authorized and squash-only.