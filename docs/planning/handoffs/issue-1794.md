# Handoff — Issue #1794 independent existing-PR security review

## Task identity and authority

- Mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-18-REV-01`; reviewer actor `existing-pr-distinct-html-anchor-security-review-1794-gpt6-20261016-prg-01`, genuinely distinct from Issue #1792 producer.
- First, sole winning immutable schema-3 CLAIM: Issue #1794 comment `6211280155`, GitHub server `2026-10-16T08:22:14Z`; branch `planning/issue-1794` based on `main@7da4c2d50412fe134c8632264908560b8b7995ce`. Recheck current owner, main and head before any further action.
- Canonical Issue #1147 binding terminal `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. This review has no canonicalization or integration authority.
- Frozen existing source Issue #1792 first CLAIM `6211042106`, immutable in-lease owner terminal `STATUS(REVIEW_READY)` `6211125437`; OPEN/DRAFT source PR #1793 exact HEAD `dd0afd5de2961eaf1db2e7b8e235da2d9b5bd346`, base `7da4c2d50412fe134c8632264908560b8b7995ce`, module blob `b3d03feab7b74eeca15ea1fd97bf2242ab7fcacd`; 14 paths with 12 protected inherited blobs.
- Exact frozen source CI run `38872158799` SUCCESS, `self-test` job `116878549980` SUCCESS, write-capable `retire` `116878603449` SKIPPED; authored tests are not independent acceptance.
- Previous negative reviewer Issue #1790 terminal `6210947527`; frozen predecessor source PR #1789 and reviewer-only PR #1791 not modified.

## Independent finding and evidence

**CHANGES_NEEDED: 0 BLOCKER / 1 MAJOR FSR-1794-M01 / 0 correction-requiring MINOR.** The source `references_pr` treats bare `#N`, absolute/protocol-relative GitHub URLs, and Markdown inline/reference destinations as references, but does not interpret clickable **raw HTML relative** anchors. The active GitHub issue/comment `<a href="../pull/200">review</a>` yields the same clickable `href` through markdown-it-py 4.2.0 and Mistune 3.2.1, and Node 22 WHATWG resolves it against an issue page to `https://github.com/vokerg/everfield/pull/200`; the frozen source's exact three entry predicates all miss it. Root-relative and traversing relative HTML anchors likewise miss. Positive absolute HTML / ordinary Markdown controls match, while foreign repo, wrong PR and innocent paths do not refer to target PR. Both initial and fresh pre-PATCH source vetoes depend on this same parser.

Independent detailed reproducible evidence is in `docs/planning/wave-2/reviews/negative-review-retirement-1792-review.md` Git blob `97d2b97d28174da067d63bb666a2bcd145a11f5b`. **Scope limitation:** this execution ran two independent Markdown renderers, Node WHATWG resolution and faithfully extracted exact-source entry-predicate evaluation; it did **not** independently execute the full ~75KB Python module or mocked `execute(apply=True)`. Hence **negative security finding only, never CLEAN**. No actual GitHub `--apply`, PATCH, close, source rewrite, merge or main change. GET/PATCH race remains non-atomic.

## Required continuation

Reviewer-owned packet is **exactly** this handoff and the independent review report, both additions on `planning/issue-1794`. Publish an OPEN/DRAFT exact-head reviewer-only PR and an immutable in-six-hour-lease `REVIEW_STATUS(CHANGES_NEEDED)`; that reviewer PR **MUST NEVER MERGE**. Materialize only ONE required bounded existing-source-PR #1793 correction to FSR-1794-M01: conservatively recognize first-party PR links in raw HTML relative hrefs with exact repo/number boundaries and wrong-target/foreign controls. Preserve frozen protected packet, rerun hosted exact-head full source CI with mutation job SKIPPED, and require a **new genuinely distinct independent full-module security review**. No source integration before CLEAN plus separate current-main-compatible owner-authorized **SQUASH-only NONCANONICAL** publication. No gameplay, engine, implementation-readiness, production, release or canonical authority.
