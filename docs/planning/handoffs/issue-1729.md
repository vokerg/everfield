# Issue #1729 — mandatory independent negative security review handoff

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-08-REV-01`. **Actor:** `existing-pr-backslash-url-review-1729-gpt6-20261013-cph-01`. First valid schema-3 CLAIM **#6137588181**, GitHub 2026-10-13T03:32:26Z, immediately rechecked as sole winning claim. Task branch `planning/issue-1729` from `main@a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.

## Exact frozen producer and active canon

Existing source #1726 first CLAIM #6132484379, valid unedited in-lease REVIEW_READY terminal #6132556759; source PR **#1728** OPEN/DRAFT, exact HEAD **`c51789012237523d7ac01f70b3e34f10dfc6191e`**, four paths only, source script blob `61250b824784c468de335915fa10c1814dc4d26d`. Authored exact-head CI #38307924510 SUCCESS, self-test #115006348760 SUCCESS, mutating retire #115006413984 SKIPPED. These do **not** count as independent clean review. Active canonical Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`; fresh GitHub compare main ancestry ahead=149, behind=0.

## Negative finding and evidence

**REVIEW_STATUS(CHANGES_NEEDED): 0 BLOCKER, 1 MAJOR `FSR-1729-M01`, 0 correction-requiring MINOR.** The frozen `references_pr` only normalizes backslash-escaped slashes. CommonMark Markdown URL destinations can also escape colon, host period, suffix period and question mark. Independently transcribed/executed the actual frozen Python `PR_URL` / `references_pr` predicate: six test cases were false negatives for the target PR #200; MarkdownIt 4.2.0 and Mistune 3.2.1 each rendered clickable valid first-party GitHub PR URLs. Escaped slash and ordinary direct URL were correctly positive. Source's live open issue title/body/comment scan and its second pre-PATCH recheck consume this same predicate, so this is a consequential closure-veto gap.

Full evidence and exact limits: `docs/planning/wave-2/reviews/negative-review-retirement-1726-review.md`. The **only two reviewer-owned new files** are that report and `docs/planning/handoffs/issue-1729.md`. Independent full module import/mocked apply suite was not executed; that prevents CLEAN but does not invalidate specific negative proof. No live `--apply`, PR closure, GitHub PATCH, source edits, merge or production action.

## Required continuation

Exactly one mandatory bounded blocked corrective successor [#1738](https://github.com/vokerg/everfield/issues/1738) was created for FSR-1729-M01, specifically to remediate **existing** PR #1728. It must remain unclaimed until this review's exact-head reviewer-only OPEN/DRAFT PR and immutable in-six-hour-lease `REVIEW_STATUS(CHANGES_NEEDED)` terminal. Later a genuinely distinct owner inherits the source packet on a fresh branch; independently tests all punctuation/HTML-entity combinations in actual module with safe mocked zero-PATCH rechecks; hosts exact-head read-only CI and obtains yet another genuinely independent mandatory review. Any later authorized main integration is SQUASH-only NONCANONICAL, never from this reviewer-only PR. Prior frozen PRs stay draft/unmerged.

Before terminal, re-derive main, source draft/head, claim comment and six-hour owner lease, actual two-file branch diff, reviewer-only PR exact head and report/handoff blobs. Publish terminal with exact work/head, source terminal and PR, one finding, successor #1738 and no integration authority. Maintain the original independent evidence and source identity for future recovery.
