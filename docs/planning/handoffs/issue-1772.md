# Issue #1772 — independent ordered-dot source security review handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-13-REV-01`.  
**Source:** Issue #1769, frozen OPEN/DRAFT PR #1771, exact HEAD `1a224210fb402cabfaa2230c9b8521d29f62de85`, retirement script Git blob `b7aec6e8b5be095dad495623dc3dcf7f345ad92c`.  
**Reviewer ownership:** sole first schema-3 CLAIM #6187042214, actor `independent-ordered-dot-review-1772-gpt6-20261015-cph-01`, first observed fresh `main@7da4c2d50412fe134c8632264908560b8b7995ce`. No rival claims on immediate recheck.  
**Canonical:** Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Result

**MANDATORY INDEPENDENT SECURITY REVIEW = CHANGES_NEEDED**, 0 BLOCKER / **2 MAJOR FSR-1772-M01, FSR-1772-M02** / 0 separately correction-requiring MINOR.

At exact source lines 184–196, `references_pr` treats `urlsplit.hostname`, percent-unquote and casefold as complete hostname proof, but browser WHATWG host parsing additionally recognizes Unicode/escaped dot-equivalent characters as ASCII separators. The valid Markdown active reference `[review](https://github。com/vokerg/everfield/pull/200)` (and U+FF0E, U+FF61, escaped-host and API variants) navigates to `github.com` while the source predicate skips it as a foreign host. Both initial and fresh pre-PATCH live-title/body/comment scans share the bypass. Independently reproduced second MAJOR **FSR-1772-M02**: absolute CommonMark links with extra special-scheme authority slashes such as `[review](https:////github.com/vokerg/everfield/pull/+0200)` navigate to the first-party PR under WHATWG, while `urlsplit(...).hostname` is `None`, so the same predicate falsely excludes it. Both markdown-it-py and Mistune render clickable anchors. Initial targeted evidence at source PR #1771 comment #6187091546 was verified in this distinct review execution; it is not an additional operational reviewer. The exact independently reproduced predicate and Node 22 WHATWG browser and Markdown renderer evidence, all controls, source/CI identity, limits and remediation are in `docs/planning/wave-2/reviews/negative-review-retirement-1769-review.md`.

Reviewer **did not** execute the complete 1265-line source module in an independent runtime and did not test any live apply/PATCH. Negative disposition is limited to one independently proven critical safety-gate defect, not an assertion of complete test coverage. Source-hosted exact-head CI #38628771703 self-test job #116074661902 SUCCESS and mutating job #116074767408 SKIPPED are provenance only.

## Single required corrective successor

[Issue #1773](https://github.com/vokerg/everfield/issues/1773) is materialized, strictly blocked on this issue's valid negative terminal. Distinct next claimant must start from then-current main; inherit all nine source #1771 paths, retain eight blobs exactly, correct only the script, add only #1773 handoff. Require actual full-module independent tests/mocks with browser-equivalent IDNA/host, active reference first/fresh vetoes, zero PATCH, non-first-party controls, exact-head hosted success, new genuinely independent required review. No other new work is justified.

This reviewer branch owns **exactly two paths**: the review report above and `docs/planning/handoffs/issue-1772.md`. Publish OPEN/DRAFT evidence PR of its exact final HEAD before terminal `REVIEW_STATUS`. Reviewer-only PR must **never merge**. Source #1771 stays OPEN/DRAFT, frozen and unmerged. Negative review, issue closure, PR draft, tests or mergeability **never** grant source integration, live retirement, canonicality, implementation, production or release authority. Eventual accepted source integration requires separate owner authority and current-main-compatible SQUASH-only NONCANONICAL publication.

## Continuation

Record exact final reviewer branch work/head SHA and new draft PR number in immutable schema-3 `REVIEW_STATUS(CHANGES_NEEDED)` on #1772, with `required_next_route: MATERIALIZE_BOUNDED_BLOCKING_CORRECTION_EXISTING_ISSUE_1773_OF_FSR_1772_M01_AND_M02_THEN_NEW_REQUIRED_INDEPENDENT_SECURITY_REVIEW_BEFORE_SEPARATE_SQUASH_ONLY_NONCANONICAL_INTEGRATION`. Reconcile terminal issue to GitHub CLOSED completed; do not merge this review PR. No source or main mutations.
