# Mandatory independent security review: corrected source Issue #1780 / PR #1781

**Disposition: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR (FSR-1782-M01), 0 correction-requiring MINOR.** A concrete new active-reference veto failure precludes CLEAN. This reviewer is a separate execution from both corrected source #1780 owner and earlier producer #1773.

## Authority and exact frozen snapshot

- Then-current `main`: `7da4c2d50412fe134c8632264908560b8b7995ce`.
- Canonical Issue #1147 unedited integration terminal comment #5675066392; active Planning Program v1 Git blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Source #1780 first sole `CLAIM` comment #6188479971 at 2026-10-15T09:04:32Z; immutable owner `STATUS(REVIEW_READY)` #6188662267 at 09:14:33Z, within six-hour lease; actor `existing-retirement-commonmark-correction-1780-gpt6-20261015-cph-01`.
- Frozen `planning/issue-1780`, source **OPEN/DRAFT** PR #1781 HEAD/work `2db5c8eb4fa1877358986950113d7b3ba9f6477a`, base current main, corrected complete Python module Git blob `eaea88e3acd63c2660058e7b5f2d1f81d50b090b`. GitHub verified exactly **11 paths**: inherited workflow and eight prior handoffs byte-identical with PR #1775, plus changed script and new handoff `docs/planning/handoffs/issue-1780.md` blob `6402bd2df2f1abf85a784a17c8a727fd7e8a04ce`.
- Corrected source hosted exact HEAD Actions run #38711151552: read-only Python compile/full-module `--self-test` job #116342554020 **SUCCESS**, write-capable `retire` #116342615381 **SKIPPED**. Previous authored red run #38710943897 was not accepted as PASS.
- Prior genuinely independent negative review Issue #1776 terminal #6188416710 / evidence-only OPEN/DRAFT PR #1778 at `d5f38c331c28682aeab411e9350d92b1b3bdbe33`; 2 MAJOR fixes (multiline Markdown relative destinations and balanced parenthesized absolute URLs). #1778 MUST NEVER MERGE.
- Reviewer Issue #1782 first/sole schema-3 `CLAIM` #6188705779 at 2026-10-15T09:16:52Z; new current-main branch `planning/issue-1782`. First ownership and exact branch SHA rechecked immediately. Own exactly this report and `docs/planning/handoffs/issue-1782.md`; do not alter source PR.

## FSR-1782-M01 — MAJOR: balanced-parenthesis **relative** CommonMark links still evade retirement veto

The source corrected the **absolute** scanner `PR_URL` (roughly lines 103–107) for parentheses but did not extend its distinct **relative Markdown target scanner** (lines 115–118). Frozen corrected exact scanner:

~~~python
RELATIVE_MD_LINK_TARGET = re.compile(
    r"(?:\]\([ \t]*(?:\r?\n[ \t]*)?|(?m:^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*(?:\r?\n[ \t]*)?))"
    r"(?:<([^<>\n]+)>|([^\s<>()]+))"
)
~~~

The non-angle capture `([^\\s<>()]+)` stops at the first balanced path parenthesis. In the legitimate CommonMark inline destination `[review](../(z)/../pull/200)` it captures **only `../`**, not the following `(z)/../pull/200`. The absolute scanner sees **no** `//` authority, and there is **no** `#200` fallback. `browser_path_segments` only receives the truncated candidate, so `references_pr(text, 200)` can falsely return `False`.

This does not require unusual encoding or forged GitHub data: parenthesized path segments and subsequent `..` resolution are supported by browser URLs. Markdown-it-py 4.2.0 (CommonMark-compatible) renders the full clickable href `../(z)/../pull/200`; it resolves from `https://github.com/vokerg/everfield/issues/1` to `https://github.com/vokerg/everfield/pull/200`. Two additional independently rendered positive variants are `[review](/vokerg/everfield/(z)/../pull/200)` and `[review]: ../(z)/../pull/200\n\n[review]`. **Both** Markdown-it and Mistune 3.2.1 render the reference-definition variant to the full live PR destination; Mistune does not preserve the ordinary inline link's balanced destination, which is a parser-dependent rendering distinction and **not** evidence of safety in GitHub/CommonMark.

### Independently executed, reproducible read-only witness

The following is executable with Python 3 and `markdown-it-py==4.2.0`. It uses the **exact frozen corrected source's two scanner regexes** (from blob above) rather than inventing a new pattern; the browser-equivalent URL resolution and actual renderer output are independently checked. The identical scanner patterns are the entire URL-candidate discovery used by the frozen consumer.

~~~python
import re
from html.parser import HTMLParser
from urllib.parse import urljoin
from markdown_it import MarkdownIt

absolute = re.compile(
    r"""(?<![A-Za-z0-9+.:/-])(?:https?:)?//[^\s<>\[\]{}"'\x60]+""", re.I)
relative = re.compile(
    r"(?:\]\([ \t]*(?:\r?\n[ \t]*)?|(?m:^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*(?:\r?\n[ \t]*)?))"
    r"(?:<([^<>\n]+)>|([^\s<>()]+))")
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.extend(v for k, v in attrs if k == "href")
base = "https://github.com/vokerg/everfield/issues/1"
target = "https://github.com/vokerg/everfield/pull/200"
bad = [
    "[review](../(z)/../pull/200)",
    "[review](/vokerg/everfield/(z)/../pull/200)",
    "[review]: ../(z)/../pull/200\n\n[review]",
]
for case in bad:
    assert not absolute.findall(case)
    captures = relative.findall(case)
    assert captures and all("/pull/200" not in "".join(g) for g in captures)
    rendered = MarkdownIt().render(case)
    links = Links()
    links.feed(rendered)
    assert target in [urljoin(base, href) for href in links.hrefs]
assert relative.findall("[review](../pull/200)")[0][1] == "../pull/200"
print("3 live first-party PR targets evade frozen relative scan; direct control detected")
~~~

**Actual independent observations:** all three first-party positives above navigated to `/vokerg/everfield/pull/200` in Markdown-it, but relative scanner extracted truncated `../` or `/vokerg/everfield/`, never the PR route; absolute scanner found zero candidates. A normal `[review](../pull/200)` single-line control was recognized. Benign/wrong-target controls `[review](../(z)/../pull/201)` and `[review](/vokerg/other/(z)/../pull/200)` rendered into distinct non-target URLs and must **not** be indiscriminately vetoed. `[review](<../(z)/../pull/200>)` is an already recognized angle-delimited positive control because the alternate angle capture permits `(`) and `)`. The discrepancy is therefore caused by target syntax, not an unavailable parser feature.

### Actual consumer impact

Frozen `eligibility` calls the same `references_pr` on active issue title+body and complete loaded comments; a valid live PR reference can pass the gate unrecognized. Frozen `execute(apply=True)` performs an initial `eligibility`, then a fresh complete open-issue scan and another `eligibility` immediately before PATCH, **using the same false-negative predicate**. Therefore an otherwise aged, validly rejected reviewer-only draft **may be closed while an active issue still links to it**. This is a conditional consequence of actual source control flow, **not** a claim that a real PATCH or PR closure occurred. Corrected authored CI tests do not include this relative-parenthesized CommonMark form.

### Proof boundary

The review executed **actual frozen scanner regexes** transcribed verbatim, both installed Markdown parsers and genuine Python URL resolution; inspected complete GitHub-hosted corrected function and the actual `eligibility`/fresh-pre-PATCH call path. The full 68 KB corrected source module and its live mocked `execute(apply=True)` were **not independently imported/executed** here, so no comprehensive CLEAN or broad regression certification is asserted; the reproduced MAJOR alone suffices for `CHANGES_NEEDED`. Hosted source self-test is author evidence, not independent code-security approval.

## Required **one** bounded mandatory correction (no competing source branch)

After this reviewer publishes immutable exact-HEAD `REVIEW_STATUS(CHANGES_NEEDED)`, materialize exactly one corrective successor issue for **FSR-1782-M01**. A new claimant must rederive main, canonical binding, first-valid ownership, exact frozen source PR and review terminal before claim; create fresh `planning/issue-THIS` from then-current main. Inherit exact **11-path** PR #1781 source packet, keep **ten** path blobs unchanged, change **only** `tools/planning/retire_negative_review_prs.py`, and add new own handoff (12-path packet at unchanged main). Never touch original source, reviewer evidence branches, workflow, main, game or canon.

The bounded correction must recognize genuine balanced-parenthesis **relative** inline and reference-definition destinations (both repo- and root-relative) with CommonMark/browser resolution, including `(z)/../`, LF/CRLF, aliases, suffixes, nonangle/angle forms and their combinations; preserve all inherited IDNA Unicode/encoded host, extra-slash, escaped entities, dot segments, explicit port, foreign-host/wrong-repo/wrong-PR/benign negatives, first/fresh fully paged open-issue veto, owner lease and 72-hour grace. Test **complete actual corrected module** `references_pr`, `eligibility`, paged reader and initial/fresh mocked `execute(apply=True)` with zero PATCH for linked targets and no over-veto for safe foreign/other PRs. Require exact corrected HEAD hosted read-only compile and `--self-test` **SUCCESS**, mutating job **SKIPPED**, exact-head OPEN/DRAFT source PR, immutable in-lease owner `STATUS(REVIEW_READY)`, and **new genuinely distinct mandatory security review**. Even clean review does not grant integration: any source acceptance requires a separately owner-authorized then-current-main exact-head compatible **SQUASH-only NONCANONICAL** route.

No live apply, PATCH, PR closure, self-certification, reviewer PR merge, canonicality, implementation-readiness, production or release permission. Review-only PR remains open/draft unmerged. Unknown safety/contract ambiguity must fail closed; no global gates invented outside scoped contract.
