# Independent security review — Issue #1772 / frozen source PR #1771

**Mission:** `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-13-REV-01`  
**Disposition:** **CHANGES_NEEDED** — 0 BLOCKER, **1 MAJOR FSR-1772-M01**, 0 separate correction-requiring MINOR.  
**Reviewer ownership:** sole first unedited schema-3 CLAIM [#6187042214](https://github.com/vokerg/everfield/issues/1772#issuecomment-6187042214), actor `independent-ordered-dot-review-1772-gpt6-20261015-cph-01`, based on `main@7da4c2d50412fe134c8632264908560b8b7995ce`. This is a separate review episode from the producers of #1769/#1765.
**Canonical control:** Issue #1147 [binding #5675066392](https://github.com/vokerg/everfield/issues/1147#issuecomment-5675066392), program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af` (verified by ancestor compare at the review base). No canonical or integration status is inferred from this review.

## Frozen reviewed identity and provenance

- Source owner Issue #1769 schema-3 first CLAIM #6177153290 at 2026-10-14T19:59:39Z and immutable `STATUS(REVIEW_READY)` #6177247211 at 2026-10-14T20:04:38Z — both unedited, well within six-hour generation lease; issue already closed as completed. Frozen source [draft PR #1771](https://github.com/vokerg/everfield/pull/1771) is OPEN, DRAFT, unmerged, base `main@7da4c2d50412fe134c8632264908560b8b7995ce`, branch `planning/issue-1769` HEAD `1a224210fb402cabfaa2230c9b8521d29f62de85`. The owner terminal records this exact work/head/PR identity.
- GitHub's source PR files API returned nine exact added paths. Its retirement module blob is `b7aec6e8b5be095dad495623dc3dcf7f345ad92c` (Git tree verified same). The seven inherited predecessor blobs listed in #1769 handoff match the source PR file list; the eighth inherited script is the only corrected source, plus #1769's own handoff.
- Hosted [workflow run #38628771703](https://github.com/vokerg/everfield/actions/runs/38628771703) executes at that same frozen head. Read-only `self-test` job #116074661902 SUCCESS, with compile/self-test step SUCCESS; mutating `retire` job #116074767408 SKIPPED. These are source-authored tests, **not** genuinely independent security approval.

## FSR-1772-M01 — MAJOR: WHATWG-normalized Unicode host bypasses live PR-reference veto

**Affected exact source:** `tools/planning/retire_negative_review_prs.py`, immutable blob above, lines **158–264** (`references_pr`), especially **184–196**: `PR_URL.finditer(text)` captures the first-party-looking URL; the parser computes `urllib.parse.unquote(url.hostname or "").casefold().rstrip(".")`, then `continue` when outside `{"github.com", "api.github.com"}`. This normalization does **not** perform the browser's WHATWG host parsing/IDNA mapping. The alternate relative Markdown scanner at lines 236–264 ignores targets starting `https://` and cannot rescue the missed absolute URL. A valid link without literal `#200` misses the first quick-mention check.

**Independent cross-parser reproduction** (PR #200 used as an otherwise reference-free example; issue #1772 reviewer does not operate on PR #200):

| Live GitHub Markdown link destination | Node 22 WHATWG `new URL(...).hostname` | Frozen source `urlsplit + unquote + casefold + rstrip` hostname |
| --- | --- | --- |
| `https://github。com/vokerg/everfield/pull/200` | `github.com` | `github。com` |
| `https://github．com/vokerg/everfield/pull/0200` | `github.com` | `github．com` |
| `https://github｡com/vokerg/everfield/pull/+0200` | `github.com` | `github｡com` |
| `https://github%E3%80%82com/vokerg/everfield/pull/200.patch` | `github.com` | `github。com` |
| `https://api.github%EF%BD%A1com/repos/vokerg/everfield/pulls/0200` | `api.github.com` | `api.github｡com` |

The three Unicode dot-equivalents are U+3002 IDEOGRAPHIC FULL STOP, U+FF0E FULLWIDTH FULL STOP, U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP. `github%E3%80%82com` and `api.github%EF%BD%A1com` are escaped representations of two of these. A separate exact-extracted `PR_URL` and `hostname` predicate reproduction in Python confirms **all five** are matched by the URL regex but fail the source's first-party predicate. Canonical `github.com` remains recognized, and a foreign `github.evil.example` remains correctly non-first-party.

**Clickable link evidence:** independent Python `markdown-it-py` and Mistune Markdown renders accept the Unicode-host Markdown inline links: the former normalizes several to ASCII `github.com` in the generated `href`, while the latter percent-escapes the Unicode dot. Node WHATWG parses either rendered form to the real first-party host. This is a browser-resolvable first-party PR link, not just visually similar text.

**Consequence:** In `eligibility` lines 341–360, an open issue title, body or fully paged comment containing only one of these references can return a false absence of active references. `execute(apply=True)` lines 533–575 invokes the same `eligibility` and `references_pr` for both its initial and fresh pre-PATCH scan. Rechecking with an unchanged defective predicate cannot veto this live reference. A 72-hour-old otherwise eligible reviewer-only draft could be closed in violation of the mandatory active-reference safety guard. No live `--apply`, network write, PR PATCH/closure, or demonstration on a real eligible PR was performed.

**Scope and limits:** The actual frozen source was fetched and inspected, including exact code, file identities and its authorization consumer paths. Independent local executions covered the *exact extracted URL recognition/hostname predicates*, Node WHATWG URL resolution and two Markdown-rendering libraries, **not the entire 1265-line frozen module** or a full-module `eligibility`/`execute` mock. Consequently no module-wide CLEAN coverage, race elimination or production-safe execution is asserted. The negative finding is deterministic at a prerequisite gate and sufficient for CHANGES_NEEDED; an independent full-module integration witness is required of the corrected successor.

## Disposition and required next route

**CHANGES_NEEDED (FSR-1772-M01, 1 MAJOR).** Source #1771 must remain DRAFT, unmerged, unchanged, noncanonical and without live retirement/close authority. Reviewer-only evidence PR for #1772 must **never merge**.

The single bounded mandatory corrective successor is [Issue #1773](https://github.com/vokerg/everfield/issues/1773), blocked on the terminal negative review of this issue. It must inherit all nine frozen #1771 blobs, preserve eight byte-identically, change only the retirement module, add its own handoff, correct browser-equivalent host parsing conservatively, exercise actual full-module title/body/comment and both read-only/mocked pre-PATCH vetoes with foreign-origin negative controls, run fresh exact-head compile/self-test CI, and receive a **new genuinely distinct security review**. Any eventual source storage integration needs separate owner authorization and expected-head-compatible **squash-only NONCANONICAL** publication; no review evidence alone grants it.

## Reproduction commands (safe and read-only)

```js
for (const h of ["github。com", "github．com", "github｡com",
                 "github%E3%80%82com", "api.github%EF%BD%A1com"]) {
  const path = h.startsWith("api.") ? "/repos/vokerg/everfield/pulls/0200" :
                                     "/vokerg/everfield/pull/0200";
  console.log(h, new URL("https://" + h + path).hostname);
}
```

```python
import re, urllib.parse
PR_URL = re.compile(r"(?<![A-Za-z0-9+.:/-])(?:https?:)?//[^\s<>\[\](){}\"'\x60]+", re.I)
for h in ["github。com", "github．com", "github｡com", "github%E3%80%82com",
          "api.github%EF%BD%A1com", "github.com", "github.evil.example"]:
    route = "/repos/vokerg/everfield/pulls/0200" if h.startswith("api.") else "/vokerg/everfield/pull/0200"
    text = f"[review](https://{h}{route})"
    m = PR_URL.search(text)
    hostname = urllib.parse.unquote(urllib.parse.urlsplit(m.group(0)).hostname or "").casefold().rstrip(".")
    print(h, hostname, hostname in {"github.com", "api.github.com"})
```
