# Independent security review of Issue #1784 / PR #1785

**Verdict: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR (FSR-1786-M01), 0 correction-requiring MINOR.**

## Authority and frozen inputs

- Reviewer task: Issue #1786, mission FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-16-REV-01, distinct first CLAIM #6200343353; reviewer branch planning/issue-1786 based on main 7da4c2d50412fe134c8632264908560b8b7995ce.
- Frozen producer: Issue #1784 first claim #6188911555, winning STALE recovery #6199483999, exact in-lease STATUS(REVIEW_READY) #6199646481; OPEN/DRAFT source PR #1785 HEAD 35d3c224ca2c9416fd51e319fddddcd835c78736.
- Exact source Git blob tools/planning/retire_negative_review_prs.py: f37efe00be06cf4a993177f6fcd7e4d7e2c5f495. Exactly 12 PR paths, 10 inherited unchanged identities, corrected module and own handoff.
- Authored hosted CI run #38787787954: read-only compile/self-test #116604176152 SUCCESS; mutation-capable retire #116604277944 SKIPPED. Authored PASS does not count as independent security review.
- Canonical planning binding Issue #1147 terminal #5675066392, program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af. No source merge or live retirement authority.

## FSR-1786-M01 — escaped right parenthesis in relative CommonMark link bypasses active-issue PR reference veto

**Severity: MAJOR, correction required.**

At frozen source lines 179–180, references_pr globally decodes CommonMark backslash-escaped ASCII punctuation before attempting to identify the end of an inline Markdown destination. At lines 259–274, RELATIVE_MD_LINK_TARGET captures the non-angle destination and an unescaped depth counter treats the first unmatched closing parenthesis as the Markdown delimiter. Because the escape marker has already been erased, a literal escaped closing parenthesis within the URL is incorrectly treated as a delimiter. The remainder of a valid live PR link is discarded before path normalization and numeric PR matching.

Minimal cross-renderer witness in an active issue body, title, or comment:

~~~markdown
[review](../a\)b/../pull/200)
~~~

Independent local execution on 2026-10-15:

| Check | Observed |
| --- | --- |
| markdown-it-py CommonMark renderer | href="../a)b/../pull/200" |
| Mistune renderer | href="../a)b/../pull/200" |
| Node WHATWG new URL(href, "https://github.com/vokerg/everfield/issues/1") | https://github.com/vokerg/everfield/pull/200 |
| Exact frozen source preprocessing (lines 179–180) | strips the escape before delimiter matching |
| Frozen relative-target regex/depth logic (lines 116–119 and 259–274) | extracts ONLY "../a" rather than "../a)b/../pull/200" |
| Frozen absolute URL and hash readers | no // first-party authority, no #200 |
| Resulting source predicate for PR 200 | FALSE, although rendered browser navigation reaches that PR |

The same failure occurs with a balanced-looking path such as [review](../(z\))/../pull/200) under markdown-it: href="../(z))/../pull/200" resolves to PR #200, but the normalized source truncates the destination to "../(z)". The simpler ../a\)b case is the primary proof because **both independent Markdown renderers agree**.

Independent controls:
- [review](../(z)/../pull/200) resolves to the live PR and survives the source delimiter scan; this is the source-authored positive family.
- [review](../pull/201) resolves to a DIFFERENT PR and must not veto PR #200.
- [review](https://evil.example/pull/200) has a foreign origin and must not be reinterpreted as a relative same-repository PR link.
- A second escaped punctuation witness, [review](../a\)b/../pull/200), confirms the false-negative is not dependent on nested balanced parentheses.

The bug is security-relevant to the exact retirement operation: eligibility invokes references_pr over every open issue title/body and fully paginated comments at source lines 394–397. execute(apply=True) calls eligibility again on a fresh active-issue snapshot immediately before PATCH at lines 598–602. Both scans reuse the same false-negative, so the second read cannot veto a linked reviewer PR. This is an **inference from inspected call sites**, not a claim that a live close/PATCH was executed.

## Reproducibility and limits

Reproduction used installed markdown-it-py and Mistune to render the raw CommonMark, Node WHATWG URL to resolve actual hrefs, and an independently authored Python harness transcribing the frozen source's precise normalization/relative regex/depth loop without changing its order. Both raw rendered href and truncated source destination were printed. This proves the narrow adverse predicate path; **the complete approximately 71 KB module was not independently imported or executed**, and neither actual eligibility, paged() nor execute(apply=True) was run in a complete mocked environment. The independently authored test harness is not a full-module assertion. GitHub's actual Markdown renderer was not executed; two independent CommonMark renderers and the browser URL oracle support the concrete impact. No live GitHub API PATCH or PR closure occurred.

A CLEAN verdict is impossible because the specific MAJOR finding stands, irrespective of authored green CI. Other safety guarantees (72-hour grace, 6-hour ownership, exact two files, complete pagination, pre-PATCH non-atomicity) were statically inspected but not independently fully certified. No unobserved defects are asserted as additional counts.

## Required bounded correction and continuation

Materialize exactly one mandatory successor for FSR-1786-M01 on a NEW source task branch based on then-current main, inheriting frozen PR #1785's complete 12-path source evidence packet byte-identically except the retirement module and a new task-specific handoff. Fix destination parsing so escaped parentheses retain their literal URL meaning while actual closing delimiters end the link. Do not simply reject every unrelated foreign link or remove fail-closed ambiguity safeguards. Preserve balanced nested parentheses, entities, LF/CRLF, URL aliases, encoded-dot and host controls, strict wrong-PR/foreign-origin negatives.

Correction owner must independently run the entire exact corrected Python module including references_pr, eligibility, paged active comments and fully mocked initial + fresh pre-PATCH execute(apply=True) with **zero PATCH** for live links, plus positive safely eligible controls, then hosted exact-head read-only compile/full self-tests with retire SKIPPED. Publish exact-head owner REVIEW_READY and obtain a genuinely distinct mandatory security review. Only after CLEAN may a separately claimed, compatible, expected-HEAD, **squash-only NONCANONICAL** integration be considered.

This is a reviewer-only evidence artifact. The review PR MUST NEVER MERGE; source PR #1785 stays OPEN/DRAFT, frozen, and not accepted. No live --apply, main write, source edits, canonicality, gameplay/engine/readiness, production or release authority.
