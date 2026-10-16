# Issue #1790 — independent reviewer handoff

**Mission:** FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-17-REV-01
**Owner/session:** existing-pr-distinct-retirement-security-review-1790-gpt6-20261016-prg-01
**Claim:** immutable Issue #1790 CLAIM #6210843821 (2026-10-16T07:56:49Z; first sole owner; six-hour generation)
**State:** reviewer security finding proven; CHANGES_NEEDED (1 MAJOR FSR-1790-M01), no independent CLEAN
**Branch:** planning/issue-1790 from main 7da4c2d50412fe134c8632264908560b8b7995ce
**Review diff surface:** OPEN/DRAFT reviewer-only PR #1791 (https://github.com/vokerg/everfield/pull/1791), exactly 2 added paths. Its final HEAD is authenticated in Issue #1790 terminal REVIEW_STATUS; reviewer-only PR **MUST NEVER MERGE**.

## Source/provenance

- Active canonical Issue #1147 binding #5675066392; program blob fd4cf1119c3f86acc3af620024eea72235e81ce4; activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af.
- Existing corrected source Issue #1788 first winning CLAIM #6200549253, unedited in-lease terminal REVIEW_READY #6200656618.
- Existing DRAFT source PR #1789 exact head d89cc524e7aece029246e3670a121d4ae8b9e810; script blob bd2e1e28c2ea52ca5fee0f5001fd6ab5dd40c606; handoff blob c6440a022a1354bd4c669ebfab00059700af7d71; 13 paths and eleven inherited frozen Git blobs all independently matched source head.
- Hosted run #38794980778 SUCCESS, read-only full-self-test #116628878743 SUCCESS; write-capable retire #116628942623 SKIPPED.
- Predecessor rejected source #1785 and reviewer-only PR #1787 remain unmodified; do not merge.

## Reproducible security finding

FSR-1790-M01: at source lines 182, 263-288, HTML character references are decoded **before** true Markdown inline-link delimiter recognition. Thus [review](../a&#41;b/../pull/200) is a rendered clickable href ../a)b/../pull/200 resolving to https://github.com/vokerg/everfield/pull/200 (independent markdown-it-py, Mistune, Node WHATWG), but frozen detector truncates the candidate at decoded ) and sees only ../a. Same defect in initial and fresh pre-PATCH live-issue reference veto through shared references_pr. Full witness, controls, reasoning, limitations and exact source lines: docs/planning/wave-2/reviews/negative-review-retirement-1788-review.md.

Negative review does NOT claim independent full-module/mock apply execution, comprehensive clean security, integration permission or live retirement. One deterministic independently reproduced active-link false negative suffices for CHANGES_NEEDED; any future clean verdict still requires exact full-module independent test.

## Continuation and route

Required-next-route: MATERIALIZE_ONE_BOUNDED_EXISTING_SOURCE_PR_1789_HTML_ENTITY_DELIMITER_CORRECTION_FSR_1790_M01_THEN_EXACT_HEAD_CI_AND_NEW_DISTINCT_REQUIRED_FULL_MODULE_SECURITY_REVIEW.

1. Keep this reviewer-only PR OPEN/DRAFT, never merge, and keep source PR #1789 frozen/unmerged.
2. After terminal issue status, materialize exactly one bounded correction of the **existing source PR chain**. Fix structural delimiter identification before HTML entity decoding, with matching false-positive/false-negative controls and actual initial/fresh mocked execute(apply=True) veto with zero PATCH.
3. Exact-final-HEAD authored CI SUCCESS / mutating job SKIPPED, owner valid REVIEW_READY, **new distinct full-module independent review**, and only then separately owner-authorized compatible squash-only NONCANONICAL integration if CLEAN.
4. No new gameplay/engine/readiness/canonical/release/production decision, live --apply or GitHub PATCH/close.

**Evidence integrity:** GitHub comments first-winner and server-time checked; no independent live PR close attempted. The complete corrected source module was retrieved via connected GitHub repository and its critical parser, eligible candidate and pre-PATCH paths inspected; import/execute of whole source module was not available in this reviewer environment and is explicitly not claimed.
