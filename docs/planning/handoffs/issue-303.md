# Issue #303 handoff — W2-REM-ACC-14

## Ownership and frozen inputs

- Winning claim: `5296717456`
- Actor/session: `w2-rem-acc-14-gpt56sol-20260814-2020-frontier`
- Branch: `planning/issue-303`
- Claim/base main: `7631dee0a166c91e383a8c2e7bd641b46e6b9821`
- Canonical Planning Program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Source review: Issue #302 / `W2-REV-ACC-17`
- Source review winning claim: `5296669009`
- Source review terminal: `5296708193`
- Source review head/work: `6327b6b6708f5159b20e37ffe5b348963bd5d8bb` / `1e33561de0e2afa76836910cd947b06934c0cfd4`
- Source review disposition: `CHANGES_NEEDED`
- Finding: `W2-REV-ACC17-M01 / MAJOR / SOURCE_MODALITY_WEAKENING_AND_ACCEPTANCE_AUTHORITY_DRIFT`
- Exact input policy v12 blob: `4c10dc8969a8080a14e8f46e0d2e126bd8a1ee5e`
- Exact input report v12 blob: `197a20ec3fd3cd859c4e7d96e51f7337ea7583d3`
- Inherited XAG 108–123 origin blob: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`

## Bounded correction

Fresh first-party Microsoft XAG 117 was re-read on `2026-08-14` at `https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117` (page last updated `2026-03-04`). The camera-view-choice directive is an unqualified item under Implementation guidelines.

The inherited atom `XAG117-CAMERA-VIEW-CHOICE` is corrected only from:

- `authority_class: BEST_PRACTICE_RECOMMENDED_IF_APPLICABLE`
- `source_modality: CONSIDER`

to:

- `authority_class: BEST_PRACTICE_REQUIRED_IF_APPLICABLE`
- `source_modality: SHOULD`

The atom identity, `XAG-117` source id, `CONDITIONAL` applicability, trigger `game_supports_first_person_or_third_person_camera_presentation`, semantic payload `first_person_and_third_person_view_choice_available: true`, evidence `ACC-EV-XAG117`, and gap `ACC-GAP-XAG117` remain unchanged.

The correction does not require every title to introduce both camera paradigms and does not inflate the XAG best-practice directive into `MUST`, legal/compliance, or platform-certification authority.

## Mechanical coverage

`ACCESSIBILITY-POLICY-VALIDATOR-v13` adds load-bearing witnesses that:

- accept required-if-applicable + `SHOULD`;
- reject recommended-only + `CONSIDER`;
- reject mixed advisory regressions;
- reject `MUST`/compliance inflation;
- reject identity, trigger, applicability, semantic, evidence/gap, or unrelated-record mutation.

Preserved inventory: XAG 112 `14`, XAG 114 `16`, XAG 108–123 `113`, inherited XAG 101–107 `105`, composed XAG 101–123 `218`.

Reviewed XAG 112, XAG 114, both XAG 115 corrections, and XAG 116 correction remain immutable preservation inputs.

## Producer self-review

- unresolved BLOCKER: `0`
- unresolved MAJOR: `0`
- correction-requiring MINOR: `0`
- `W2-REV-ACC17-M01`: `RESOLVED_PENDING_FRESH_SCOPED_REVIEW`

Producer self-review is not independent review. A fresh independent/degraded-independent scoped review of the exact terminal packet is mandatory before integration eligibility.

## Fail-closed state

- empirical accessibility: `NOT_RUN`
- `mapping_complete: false`
- `IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN`
- `W2-REV-M02: OPEN_BOUNDED`
- full corrected XAG 108–123 review: incomplete
- XAG 118–123: unaccepted by Issue #302
- production/readiness/release authority: false
- legal/compliance authority: false
- platform certification authority: false
- verification-PASS authority: false
- integration authority by producer: false
- canonical authority: false

## Branch work identity

- First substantive work commit: `edd2de28df9c246066dd9db5e6b436d635157ef4`
- Policy v13 blob: `3dcdaa400ffd43cea390c331f5b4f8ea62750a5c`
- Report v13 blob: `e5f1f491a91499bef96861d2878e4fb5552a207b`

After this handoff commit, open an exact-head draft PR to `main`, verify the PR head/base and three-file bounded scope, then publish terminal schema-3 `STATUS(REVIEW_READY)` binding the final head and exact artifact blobs.
