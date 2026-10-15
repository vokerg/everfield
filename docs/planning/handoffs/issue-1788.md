# Issue #1788 — Escaped CommonMark destination source correction

## Owner and current source

Mission FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-17. Sole first winning owner CLAIM #6200549253; actor_session_id existing-pr-retirement-source-1788-escape-parser-gpt6-20261015-01; branch planning/issue-1788 based on main 7da4c2d50412fe134c8632264908560b8b7995ce. Current canonical Planning Program v1 Issue #1147 terminal #5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af.

Frozen inherited existing source Issue #1784 PR #1785 exact HEAD 35d3c224ca2c9416fd51e319fddddcd835c78736, module blob f37efe00be06cf4a993177f6fcd7e4d7e2c5f495. Genuinely distinct rejected review Issue #1786 terminal REVIEW_STATUS(CHANGES_NEEDED) #6200409825, reviewer-only DRAFT PR #1787 HEAD 1ff9106322a90998b0e4cff07e1bf239d2706788; its FSR-1786-M01 is 1 MAJOR. Never merge either reviewer-only or frozen negative source draft.

## Bounded correction and invariant

Correct only tools/planning/retire_negative_review_prs.py; add this new handoff. Inherit the other ELEVEN exact Git blob identities of source PR #1785, including unchanged workflow and earlier task handoffs, yielding exactly thirteen changed paths against unchanged current main.

FSR-1786-M01: CommonMark \\) in an inline relative link is literal right-parenthesis URL data and must NOT terminate its destination. Frozen code HTML-unescaped then removed punctuation backslashes before delimiter balancing. Corrected code preserves HTML-unescaped, still-escaped raw Markdown for relative target tokenization. Within inline targets, an escaped ASCII punctuation pair advances past both characters without changing parenthesis depth; only an actual unescaped unmatched right-parenthesis closes the destination. After locating the true delimiter, normalize backslash-escaped punctuation in the destination to feed the same strict path/repository/number validation. The original normalized copy continues to drive absolute GitHub authority and #number references; reference definitions also decode escapes after capture. Keep LF/CRLF, balanced path dots, aliases, encoded authorities and foreign/wrong PR negatives.

Added source-authored regression cases for positive escaped-parenthesis non-angle links (including root-relative, decimal alias +0200.diff, 0200.patch and nested escaped parentheses, LF and reference-definition cases) and corresponding foreign/wrong-number negatives, verifying references_pr and eligibility title/body/live comment veto. Existing actual mocked execute(apply=True) positive/fresh no-PATCH tests remain. Do not claim source-authored fixtures are independent adversarial evidence.

## Verification and handoff

Exact-final-HEAD GitHub Actions PR compile/full --self-test must be SUCCESS, mutating retire job SKIPPED, before current owner may publish in-six-hour-lease STATUS(REVIEW_READY). This document is not that status. Require genuinely distinct new adversarial full-module independent review of the exact PR before any separately authorized expected-HEAD/current-main-compatible SQUASH-only NONCANONICAL integration. No source self-review, live --apply, GitHub PATCH/PR retirement, canonicality, engine/gameplay/readiness, production or release authority. The source and reviewer predecessor PRs are frozen, unmerged, untouched.
