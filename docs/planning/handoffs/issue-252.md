# Handoff — Issue #252 / W2-REM-ACC-05

## Identity

- Mission: `W2-REM-ACC-05`
- Issue: #252
- Branch: `planning/issue-252`
- Winning claim comment: `5290204279`
- Losing later claim comment: `5290206326`
- Actor session: `w2-rem-acc-05-gpt56sol-20260814-frontier`
- Claim/base main: `9b044059df07170f8db0f430451d15e1c6800f82`
- Substantive work commit: `c5490ae510086069da4983d6e672f9c8f9c6f314`
- v5 policy blob: `c7c3f72fb3bbd2d0e961aee94b33ce2ac93c5615`
- report blob: `932905021788ffa47609201ee559df9a8387a37c`

Both claims bind the same exact base/head and have `previous_ownership_comment_id: null`; the lower valid GitHub comment ID wins the ownership generation. Comment `5290204279` therefore controls this task.

## Immutable inputs

- Issue #247 terminal status comment: `5290154417`
- Issue #247 head/work: `fdc93c894e39e10a20dba81e910212dc56151441`
- exact Issue #247 v4 policy blob: `96a074e9c708d4ae2f86e8a70b7b4ade8202c799`
- Issue #250 terminal review comment: `5290193719`
- Issue #250 review head/work: `57bb9a75e6b2cba600d75fe74d180283712abcae`
- Issue #250 finding: `W2-REV-ACC04-M01` / MAJOR
- Issue #250 disposition: `CHANGES_NEEDED`
- Issue #250 review provenance integrated on `main@9b044059df07170f8db0f430451d15e1c6800f82`

## Bounded correction

`XAG106-PROPER-NAME-PRONUNCIATION` previously inherited this trigger from v3:

`proper_name_technical_term_or_word_of_indeterminate_language_requires_pronunciation_help`

The v5 overlay replaces only that record. The corrected trigger is:

`proper_name_or_technical_term_or_word_of_indeterminate_language_is_present`

Required semantics remain `pronunciation_mechanism_provided: true`. Evidence requirement `ACC-EV-NARRATION`, gap `ACC-GAP-XAG106`, source ID, authority class, applicability class, and clause identity are unchanged.

## Fresh source evidence

Current first-party Microsoft XAG 106 was re-read on `2026-08-14`; the page reports last updated `2026-03-04`. Its implementation guideline requires a mechanism for the player to understand how to pronounce a proper name, technical term, or word of indeterminate language. It does not add a subjective `requires_pronunciation_help` predicate.

## Mechanical guard

`ACCESSIBILITY-POLICY-VALIDATOR-v5` requires exact v4 blob `96a074e9c708d4ae2f86e8a70b7b4ade8202c799` as composition input, verifies the six Issue #243 corrections and the 77/105 inventory before patching, then replaces exactly the pronunciation record.

New semantic guards reject:

- a `requires_pronunciation_help` or equivalent subjective applicability gate;
- dropping any of the three source term classes;
- dropping the required pronunciation mechanism;
- redefining one of the six v4 correction records within this overlay.

## Preserved fail-closed state

- XAG 102–106 new atomic clauses: `77`
- composed atomic clauses: `105`
- XAG 108–123: `GUIDELINE_SUMMARY_ONLY`
- empirical accessibility evidence: `NOT_RUN`
- `mapping_complete`: `false`
- `IR-BLOCKER-ACCESSIBILITY-CURRENT`: `OPEN`
- `W2-REV-M02`: `OPEN_BOUNDED`
- implementation/readiness/release authority: none
- legal/compliance/platform certification authority: none
- verification PASS authority: none
- decision/canonical authority: none
- integration authority: none

## Finding disposition

`W2-REV-ACC04-M01`: `RESOLVED_PENDING_FRESH_REVIEW`.

This producer task does not accept itself. A fresh independent/degraded-independent scoped review must consume the exact terminal Issue #252 identities, reconstruct exact v4 plus v5, re-read current XAG 106, attack the subjective-gate / term-class / required-mechanism fixtures, and verify the six v4 corrections remain unchanged.

## Required next transition

Before terminal schema-3 `STATUS(REVIEW_READY)`, open an exact-head draft PR from `planning/issue-252` to `main` and verify its head equals terminal `head_sha`.

Then route exactly one fresh scoped review. Even a clean result only makes the corrected packet eligible for separately authorized squash-only noncanonical integration. It does not close aggregate accessibility mapping/evidence debt, readiness, implementation, release, legal/compliance, platform certification, verification PASS, decision, or canonical status.
