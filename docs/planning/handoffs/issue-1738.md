# Issue #1738 — CommonMark escaped-punctuation PR-retirement safety handoff

## Scope and provenance
- Mandatory bounded correction of existing draft source PR #1728 / Issue #1726 frozen head `c51789012237523d7ac01f70b3e34f10dfc6191e`, script blob `61250b824784c468de335915fa10c1814dc4d26d`.
- Independent reviewer Issue #1729 `REVIEW_STATUS(CHANGES_NEEDED)` #6137634646; reviewer-only draft PR #1739 frozen head `7c8b3667443479172e5275d74586984e12ac9fdc`; MAJOR `FSR-1729-M01`.
- Sole winning owner CLAIM #6137872988 for #1738, session `existing-pr-escaped-punctuation-remediation-1738-gpt6-20261013-cph-01`; branch `planning/issue-1738`, main base `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`; canonical #1147 binding #5675066392, blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`.
- First task commit `e5d08eaa7330861f4ddd4f547c0306cc53aeb1af` inherits the exact four-file frozen #1726 packet. Corrective commit changes only `tools/planning/retire_negative_review_prs.py` and adds this handoff. Five paths in task diff.

## Correction and tests
Normalize CommonMark backslash-escaped ASCII punctuation after HTML named/numeric entity decoding and before parsing candidate URLs; retain inherited strict scheme, host, port, repository, path, numeric PR identity and suffix checks. The inherited escaped-slash handling is subsumed.
Expand actual module `--self-test` with scheme-colon, host-dot, query, suffix, HTTP, scheme-relative and HTML-entity/backslash combinations; verify title/body/fully loaded-comment vetoes, foreign-host/repo/numeric controls, and both first and fresh pre-PATCH `execute(apply=True)` mocked snapshots reject linked PR retirement with zero PATCH.

## Evidence, limits and continuation
- Hosted exact-final-head `validate-pr` compilation and full-module self-test PASS, mutating retire job SKIPPED, are REQUIRED before owner `STATUS(REVIEW_READY)`. No local live `--apply` or real PATCH has been run.
- No source independent-clean-review, integration, canonicality, engine/readiness, gameplay, production or release authority. The GitHub GET-to-PATCH race is non-atomic.
- Next: open exact-head DRAFT PR and check hosted read-only CI; publish terminal `STATUS(REVIEW_READY)` only on actual evidence; then a genuinely distinct mandatory adversarial security review of this exact head. Later publication, if authorized, must be separately owner-claimed current-main-compatible **squash-only NONCANONICAL**.
- Frozen source PR #1728 and reviewer-only PR #1739 are untouched, DRAFT, and not merge-authorized.
