# Issue #282 handoff — W2-REM-ACC-11

## Identity

- mission: `W2-REM-ACC-11`
- issue: #282
- winning claim: `5293260434`
- actor/session: `w2-rem-acc-11-gpt56sol-20260814-1427-frontier`
- branch: `planning/issue-282`
- claim base: `main@89d6fab07dae08bb34a85fe41354050144a0d3a9`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

## Routed prerequisite

- required full review: Issue #281 / `W2-REV-ACC-11`
- winning review claim: `5293197877`
- terminal review status: `5293245321`
- exact review head: `08fee5742c95935d45fc85ab536ea56223923be0`
- review work: `9efd4fac68c96a28d63a1ee7fdbc3592ae2aba8a`
- review disposition: `CHANGES_NEEDED`
- finding: `W2-REV-ACC11-M01` / MAJOR / `SOURCE_EXCEPTION_OMISSION_AND_VALIDATOR_INCOMPLETENESS`
- exact frozen policy v9 input: `5cf18195bdfcb377aac7727b65b2d8a479ef8ac3`
- exact frozen report v9 input: `3665805bb6391bc0c7b6b27ca2f70b7f0b88aaae`
- inherited XAG 108–123 origin policy: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`

## Bounded correction

Current first-party Microsoft XAG 114 was rechecked on 2026-08-14. Its critical gameplay/settings UI reading-level guidance excludes narrative/story content and proper names or titles. The inherited atomic record omitted the `titles` exception.

Policy v10 changes exactly `XAG114-CRITICAL-TEXT-READING-LEVEL` by preserving its trigger, lower-secondary threshold, evidence/gap routing, identity, and existing exceptions, while adding:

```yaml
exceptions:
  - narrative_or_story_text
  - proper_names
  - titles
```

The v10 validator adds load-bearing rejection for omission of `titles` and for over-broad exception inflation such as `all_ui_labels`. It also rejects trigger/threshold/evidence-route drift, any unrelated v9-composed semantic change, and regression of the reviewed XAG 112 or XAG 116 corrections.

## Exact producer artifacts before handoff commit

- policy v10 commit: `0a1cb85999fb24412d687c6d282ce0d8cb095292`
- policy v10 blob: `12c1af5bd6ae88a549e575c594f8ec2afa387705`
- report v10 commit / substantive work: `33ec0cc6e967eca295cba0cb24175df75b52d03d`
- report v10 blob: `fc826cf315b0bda8308aecbc63364f6977be39d1`

## Preservation proof

- XAG 114 count: `16`
- XAG 112 count: `14`
- XAG 108–123 count: `113`
- inherited XAG 101–107 count: `105`
- composed XAG 101–123 count: `218`
- XAG 116 default-over-20-hours correction: preserved
- XAG 112 scaled-map correction: preserved
- XAG 112 all-submenus universal-return correction: preserved
- XAG 112 same-input focus-escape correction: preserved
- evidence/gap routing: unchanged
- unrelated v9 semantics: unchanged by overlay contract

Bounded producer self-review: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

## Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_114_remainder_accepted: false
untouched_xag_115_123_accepted: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authority_by_producer_alone: false
decision_authority: false
canonicality: NOT_CANONICAL
```

Issue #281 terminated early. This bounded producer packet closes only `W2-REV-ACC11-M01` **pending fresh independent scoped review**; it does not accept the unreviewed remainder, complete the full XAG 108–123 review, or make empirical accessibility work eligible.

## Required next gate

Open and freeze an exact-head draft PR for these three producer files. Then perform a fresh independent/degraded-independent scoped review of the exact v10 correction. A clean result can only make this producer packet eligible for a separately authorized squash-only noncanonical integration; after that, the full corrected XAG 108–123 review still must cover the unaccepted remainder before any empirical accessibility successor.