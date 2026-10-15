# Issue #1786 — Independent existing-PR security review handoff

## Mission and ownership

- Mission: FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-16-REV-01.
- Reviewer session: existing-pr-1785-independent-escaped-paren-review-1786-gpt6-20261015-01, first sole CLAIM comment #6200343353; immediate winner recheck found no competing claims.
- Branch: planning/issue-1786, based on current main 7da4c2d50412fe134c8632264908560b8b7995ce.
- Canonical Issue #1147 binding #5675066392; canonical file blob fd4cf1119c3f86acc3af620024eea72235e81ce4, main descends from activation 87c85cecfa9a2ffa464c4b36816a138bf41441af.
- Source: Issue #1784, exact owner terminal #6199646481; OPEN/DRAFT PR #1785 exact HEAD 35d3c224ca2c9416fd51e319fddddcd835c78736; exact retirement module blob f37efe00be06cf4a993177f6fcd7e4d7e2c5f495.
- Exact source hosted CI #38787787954 SUCCESS (read-only #116604176152 SUCCESS, write-capable retire #116604277944 SKIPPED). No independent CLEAN from authored CI.

## Review result

**CHANGES_NEEDED: 0 BLOCKER / 1 MAJOR FSR-1786-M01 / 0 correction-requiring MINOR.**

Markdown backslash-escaped right parentheses are normalized too early by the frozen retirement module. This destroys the escape/literal distinction before a balancing scanner decides where an inline destination ends. A live, clickable same-repo reviewer PR #200 link written as [review](../a\)b/../pull/200) renders by both markdown-it-py and Mistune to ../a)b/../pull/200 and resolves under Node WHATWG to https://github.com/vokerg/everfield/pull/200. The exact frozen source's preprocessing/regex/depth loop sees ../a, so references_pr returns FALSE. The issue-title/body/comment scanner and fresh pre-PATCH scanner both call this detector. This is a concrete negative code-path finding, NOT a full module acceptance verdict.

Detailed report and reproduction boundaries: docs/planning/wave-2/reviews/negative-review-retirement-1784-review.md. Both reviewer documents are the only branch-specific new files; this branch changes no source, CI, main, or inherited PR.

## Verification scope

Performed read-only exact SHA/blob/path/PR/owner/CI inspection and local independent CommonMark renderer, WHATWG, and extracted-source-loop reproductions. Did NOT independently import/run the complete 71 KB source module, execute full eligibility/live pagination/mock apply, or perform any live PR retirement/PATCH. Hosted authored CI is recorded only as authored evidence.

## Required next route

One bounded mandatory source correction of FSR-1786-M01 in the existing PR #1785 lineage. Preserve frozen producer and reviewer branches, workflow and prior source handoff blobs. Correct only the retirement script and add the successor's own handoff in a NEW task/PR with valid sole owner claim, exact-head hosted source CI and a new genuinely distinct full-module adversarial review. After any clean review, source integration still requires separately authorized then-current-main/expected-head-compatible **squash-only NONCANONICAL** integration. The reviewer-only evidence PR MUST NEVER MERGE.

## Status and safety

Issue #1786 to be terminalized with a valid in-six-hour-lease REVIEW_STATUS(CHANGES_NEEDED) after exact-head OPEN/DRAFT two-path reviewer PR exists. Do not treat this handoff alone as terminal authority. No source edit, live --apply, GitHub PATCH/closure, main write, integration, canon, engine/readiness, production or release authority.
