# Independent adversarial security review — Issue #1776 / source PR #1775

**Disposition:** CHANGES_NEEDED — **0 BLOCKER, 2 MAJOR (FSR-1776-M01, FSR-1776-M02), 0 correction-requiring MINOR**. This is a genuinely distinct mandatory reviewer episode, not the source-author episode. It is **not** a CLEAN or integration approval.

## Frozen identity and evidence authority

- Repository/main observed before claim: `vokerg/everfield` `7da4c2d50412fe134c8632264908560b8b7995ce`.
- Canonical Issue #1147 unedited `INTEGRATION_STATUS(DONE)` comment #5675066392, promoted program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Source Issue #1773 first `CLAIM` #6187358832 at 2026-10-15T07:58:17Z, owner `STATUS(REVIEW_READY)` #6187477771 at 08:05:40Z (inside six-hour GitHub-server lease; unedited), distinct actor `browser-authority-remediation-1773-gpt6-20261015-cph-01`.
- Frozen **OPEN/DRAFT** source PR #1775 base `main@7da4c2d`, HEAD/work `13fea3d90fa2e439df1373c8c448c8eb26046d3e`; corrected Python blob `610c923de03d238984a8f5e50af62be43404e0d9`. Exact ten changed paths verified against GitHub PR files API: one retirement script, eight inherited unchanged paths, and one owner handoff.
- Frozen exact-head Actions #38702950145 read-only `self-test` #116315304648 **SUCCESS**, write-capable `retire` #116315357559 **SKIPPED**. Source-authored CI is not independent adversarial proof.
- Reviewer branch `planning/issue-1776` created from current main; sole first unedited `CLAIM` #6188279896 at 2026-10-15T08:52:58Z, immediately rechecked against complete issue comments and branch. Actor `independent-newline-url-review-1776-gpt6-20261015-cph-01` differs from source #1773 and predecessor #1769.
- Review-only changes: this report and `docs/planning/handoffs/issue-1776.md`. PR #1775 and all source/review predecessor branches remain untouched.

## FSR-1776-M01 — MAJOR: multiline CommonMark relative PR-link targets bypass both retirement reference scans

**Frozen exact code:** `tools/planning/retire_negative_review_prs.py` lines 98–113, 158–175, 184–273, 346–376 (consumer), 495–553 (live complete comments and fresh pre-PATCH rescan).

The relative destination detector is constrained to a horizontal `[ \\t]*` gap after `]` + `(` or a reference-definition colon:

~~~python
RELATIVE_MD_LINK_TARGET = re.compile(
    r"(?:\]\([ \t]*|(?m:^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*))"
    r"(?:<([^<>\n]+)>|([^\s<>()]+))"
)
~~~

CommonMark permits a line ending between that delimiter and its relative destination. The frozen absolute `PR_URL` detector requires a `//` authority and correctly does not see these relative paths, and no literal `#200` appears. As a result, the two source patterns both return **no match** for all six positive attacks below, even though independently rendered Markdown navigates to the genuine first-party PR. The absolute/relative scanners are the *only* PR-link recognition paths in frozen `references_pr` beyond `#N`, so its verdict on each constructed value is false.

~~~text
[review](
../pull/200)

[review]( 
../pull/200)

[review](
<../pull/200>)

[review](
/vokerg/everfield/pull/200)

[review]:
../pull/200

[review]
~~~

The fourth also works with a CRLF before the root-relative target. Both **markdown-it-py** and **Mistune 3.2.1** rendered every tested multiline attack as a valid `<a href=...>` anchor. Resolved against `https://github.com/vokerg/everfield/issues/1`, the destination for each is `https://github.com/vokerg/everfield/pull/200`. Browser path resolution is not an inference from a textual substring: both parsers' parsed HREFs independently matched the resolved PR URL.

### Reproducible read-only independent witness

Environment in this execution: Python 3, `markdown_it` and Mistune 3.2.1. The following is a compact reproducer of the **verbatim two scanner regexes extracted from the immutable source**, compared against both real Markdown parsers. Unlike a full frozen-module import, this is an isolated cross-parser scanner/control-flow witness; **no full-module or live `execute(apply=True)` execution is claimed by this reviewer**.

~~~python
import re
from urllib.parse import urljoin
from html.parser import HTMLParser
from markdown_it import MarkdownIt
import mistune

absolute = re.compile(r"""(?<![A-Za-z0-9+.:/-])(?:https?:)?//[^\s<>\[\](){}"'\x60]+""", re.I)
relative = re.compile(
    r"(?:\]\([ \t]*|(?m:^[ \t]{0,3}\[[^\]\n]+\]:[ \t]*))"
    r"(?:<([^<>\n]+)>|([^\s<>()]+))"
)
class Hrefs(HTMLParser):
    def __init__(self): super().__init__(); self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.extend(v for k,v in attrs if k == "href")
base = "https://github.com/vokerg/everfield/issues/1"
target = "https://github.com/vokerg/everfield/pull/200"
attacks = [
    "[review](\n../pull/200)",
    "[review]( \n../pull/200)",
    "[review](\r\n/vokerg/everfield/pull/200)",
    "[review](\n<../pull/200>)",
    "[review]:\n../pull/200\n\n[review]",
    "[review]:\n/vokerg/everfield/pull/200\n\n[review]",
]
for item in attacks:
    assert not absolute.findall(item) and not relative.findall(item)
    for rendered in (MarkdownIt().render(item), mistune.html(item)):
        h = Hrefs(); h.feed(rendered)
        assert target in [urljoin(base, v) for v in h.hrefs], repr(item)
print("Six validated first-party clickable PR-reference scanner bypasses")
~~~

**Independent test output:** 7 positive cases (one single-line recognized baseline, six multiline misses); six foreign/wrong-repo/wrong-PR/benign negative controls; both parser outputs independently checked in each case. Every multiline positive had 0 absolute and 0 relative regex matches. The single-line `[review](../pull/200)` was detected by the relative scanner (positive baseline). No GitHub PATCH, live `--apply`, PR close, workflow dispatch, or source mutation was executed.

### Mechanism and impact

`eligibility` iterates **each open issue title + body and each fully loaded comment**, calling precisely `references_pr(..., number)`. When that detector is false for an otherwise live reference, the active-issue veto cannot trigger. `execute(apply=True)` recomputes `eligibility` with a **fresh** `live_open_issue_references` snapshot immediately before PATCH, but uses the **same false-negative predicate**. Thus a reviewer-only draft that otherwise satisfies author/terminal/age/branch/path checks **can be closed while an active issue still links to it**. This is a bounded conditional risk, not evidence that a real PR was closed. Existing 72-hour grace and complete pagination do not correct it.

The fixed SOURCE #1773 self-tests cover previously reported Unicode-dot host and extra-solidus authorities, but the tested positive HREF syntax here was omitted. Authored exact-head CI therefore does not resolve this independently falsified property.

## FSR-1776-M02 — MAJOR: valid balanced-parenthesis URL dots bypass absolute reference scanner

**Additional independent finding, same frozen Python blob and same initial/fresh consumer:** `PR_URL` at lines 98–101 excludes both literal parentheses. A CommonMark destination with a **balanced** parenthesized path segment remains a valid navigable href, and the browser removes that segment when it processes a subsequent `..` path segment. The scanner sees only the first-party host prefix before `(`, **not** the actual `/pull/200` route after normalization.

Reproduced read-only in Python 3 with the actual frozen regex bodies, Markdown-it, Mistune, and Node v22 WHATWG `new URL`:

~~~text
[review](<https://github.com/(z)/../vokerg/everfield/pull/200>)
  -> https://github.com/vokerg/everfield/pull/200

[review](<https://api.github.com/(z)/../repos/vokerg/everfield/pulls/0200>)
  -> https://api.github.com/repos/vokerg/everfield/pulls/0200
~~~

Markdown-it and Mistune both produce a complete clickable anchor from the **angle-delimited** destinations above; Markdown-it additionally accepts the balanced ordinary inline form. The exact frozen `PR_URL` matches **only `https://github.com/`** or **`https://api.github.com/`**. `RELATIVE_MD_LINK_TARGET` can read an angle-delimited absolute destination but ignores it due to the explicit `startsWith(("/", "./", "../"))` equivalent in Python (`destination.startswith`); no `#200` fallback. The frozen function's first-party route parser therefore never receives the complete navigated URL.

Node's WHATWG normalized destinations were independently observed as shown; wrong repository `/vokerg/other/pull/200`, wrong PR `/pull/201`, and foreign host `https://evil.test/(z)/../vokerg/everfield/pull/200` correctly resolve to non-target destinations. This is not a blanket rule that all parenthesized URLs are PR references.

The resulting **same conditional unsafe close** can occur both in initial active-issue references and the fresh pre-PATCH recheck because both use the shared `references_pr` implementation. No actual full-module mock or live PATCH was conducted. A separate nonoperational issue comment #6188333199 also recorded the candidate; the reviewer independently executed the Markdown renderer, frozen scanner, and WHATWG normalization checks before assigning this second MAJOR.

### Required bounded corrective route

1. Materialize **one mandatory source correction for **both FSR-1776-M01 and FSR-1776-M02**** from the exact frozen PR #1775 packet only after this review's valid immutable terminal, not an optional review or speculative unrelated PR. Future owner freshly re-derives then-current `main`, canonical binding, original source/review identity, lease, branch, comments, and exclusive claim winner.
2. Preserve all **ten** exact existing source PR paths and nine unchanged blobs; change **only** `tools/planning/retire_negative_review_prs.py` to handle legitimate CommonMark line-end whitespace (and related reference-definition target start) **and** browser-normalized first-party balanced-parenthesis path segments, then add one new owner handoff. Do not loosen foreign-origin, repo, PR-number, unsafe encodings, active-issue and complete-comment checks.
3. Test actual corrected `references_pr`, `eligibility` and mocked `execute(apply=True)` for initial and fresh pre-PATCH issue-title/body/paged-comments veto, with zero PATCH for each multiline and balanced-parenthesis positive, and preservation of negative controls and six-hour owner/72-hour age gates. Run full module compile/self-test and hosted exact-head read-only CI with mutating retire job SKIPPED; publish exact-head OPEN/DRAFT source PR and owner `STATUS(REVIEW_READY)`.
4. Demand a **new genuinely distinct required adversarial review** before even considering separately owner-authorized **SQUASH-only NONCANONICAL** source integration. No reviewer-only evidence PR may merge. Do not run live retirement, change main/canonical, or claim production/readiness authority.

## Proof limits, alternatives, and reopen conditions

This is an adverse result based on exact frozen parser text, independent executable Markdown parser/HREF controls, and static consumer-path inspection—not a clean certification of the full ~65 KB script or proof that its full mocked execute path has run in this reviewer environment. Source-authored hosted CI was observed, not independently rerun. These two independently falsified MAJORs each prohibit CLEAN despite untested surfaces. Reopen only after a fresh corrected exact-head source, real full-module/consumer adversarial tests, and a genuinely independent repeat review. Do not infer that the two original #1772 findings or other attack surfaces have obtained global clean certification.
