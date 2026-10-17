# Independent adverse security review — source Issue #1800 / PR #1801

## Review identity, exact frozen source, and authority

- Reviewer Issue **#1802**, mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-20-REV-01`, distinct reviewer execution `existing-pr-distinct-fullmodule-security-1802-gpt6-20261017-01`, first sole schema-3 CLAIM **#6232161129** at GitHub `2026-10-17T09:13:34Z`. This execution is distinct from #1800 source owner `existing-pr-source-encoded-dot-html-rem-1800-gpt6-20261016-01`; the same GitHub login is not used as evidence of source/reviewer execution identity.
- Main **`7da4c2d50412fe134c8632264908560b8b7995ce`**; active canonical Issue #1147 immutable integration terminal **#5675066392**, program blob **`fd4cf1119c3f86acc3af620024eea72235e81ce4`**, activation ancestor **`87c85cecfa9a2ffa464c4b36816a138bf41441af`** (GitHub compare merge-base matches ancestor; program blob read from main).
- Frozen corrected source Issue **#1800** winning CLAIM **#6216890592**, unedited within-six-hour owner `STATUS(REVIEW_READY)` **#6217098781**. Existing **OPEN/DRAFT unmerged PR #1801** on `planning/issue-1800`, exact HEAD **`54cc76a3a33d84dfd3edf3dd80637981d6edbd8b`**, exact corrected `tools/planning/retire_negative_review_prs.py` blob **`69f47c52d4a9a45b3eb18a3f7f05a50c4670a1aa`**. Its base is the unchanged main above.
- Exact **16-path source diff** confirmed via GitHub PR files: one Python module, the source owner's handoff blob **`1e45291b091984eea56453a6f5c40c9a89adfaea`**, and **14 identical inherited non-script Git blobs** compared directly with predecessor DRAFT PR #1797. Existing source PR #1797 and negative reviewer-only PR #1799 remained untouched.
- Hosted exact-head Actions run **#38911729664**: `completed/success`, independent metadata read confirms compile/`--self-test` job **#117008971381 SUCCESS** and mutation-capable `retire` job **#117009039988 SKIPPED**. These are source-authored checks, not independent security CLEAN.

## Disposition: CHANGES_NEEDED

**0 BLOCKER; 2 MAJOR FSR-1802-M01 and FSR-1802-M02; 0 correction-requiring MINOR.** No CLEAN, safe `--apply`, integration, canonical or release authority is asserted.

### FSR-1802-M01 (MAJOR): same-scheme relative CommonMark link misses live reviewer PR veto

The source's corrected `raw_html_relative_references_pr` handles raw `<a href="https:../pull/200">` and includes an authored test for it, but **does not parse CommonMark `[review](https:../pull/200)`**. Such a Markdown link is clickable in the rendered issue/comment, and the WHATWG browser resolves the same-scheme relative URL against `https://github.com/vokerg/everfield/issues/1` to **`https://github.com/vokerg/everfield/pull/200`**. Also `[review](https:/vokerg/everfield/pull/200)` resolves to that exact PR. The intended immutable negative-review PR remains actively referenced and must not be retired.

For **exact source module** `references_pr` inspected through GitHub `fetch_file` and source PR blob:

1. Bare `#200` scanning finds nothing.
2. `PR_URL` requires `//`, which both target syntaxes lack.
3. `_RelativeHtmlAnchorParser` sees **zero raw `<a>` start tags** in CommonMark source `[review](...)`; no raw-HTML safety path runs.
4. `RELATIVE_MD_LINK_TARGET` matches the inline destination, but after delimiter/entity unescaping the relative-path gate `if not destination.startswith(("/", "./", "../")): continue` skips any destination beginning with `https:`, without browser same-scheme URL resolution.
5. Thus `references_pr` has no remaining reader that recognizes either target, including when scanning an open issue title, body, or loaded comment in `eligibility`. Initial and fresh pre-PATCH `execute(apply=True)` scans use the same predicate. A properly old otherwise eligible rejected reviewer-only draft may therefore be closed while its live reviewer PR link remains.

#### Independently executed reproduction, renderer and browser

Node.js 22.16.0 WHATWG URL:
```javascript
const base = 'https://github.com/vokerg/everfield/issues/1';
for (const s of ['https:../pull/200', 'https:/vokerg/everfield/pull/200',
                 'https:/vokerg/other/pull/200', 'https:../pull/201'])
  console.log(s, '=>', new URL(s, base).href);
```

Results:
```text
https:../pull/200 => https://github.com/vokerg/everfield/pull/200
https:/vokerg/everfield/pull/200 => https://github.com/vokerg/everfield/pull/200
https:/vokerg/other/pull/200 => https://github.com/vokerg/other/pull/200
https:../pull/201 => https://github.com/vokerg/everfield/pull/201
```

Real Markdown-it-py (`MarkdownIt('commonmark', {'html':True})`) and Mistune 3.2.1 (`mistune.create_markdown(renderer='html', escape=False)`) **both** emitted `<p><a href="https:../pull/200">review</a></p>` for `[review](https:../pull/200)`, and corresponding `href="https:/vokerg/everfield/pull/200"` for the root variant. The same independent Python probe copied the source `PR_URL` and `RELATIVE_MD_LINK_TARGET` regexes, and used stdlib `HTMLParser` on the *original Markdown input*. It observed `PR_URL=False`, raw HTML hrefs `[]`, and a relative-target candidate whose `startswith(("/", "./", "../"))` gate is `False`. The wrong-repository `https:/vokerg/other/pull/200` and wrong-PR `https:../pull/201` controls resolve to different targets, not protected PR #200.

A minimal reproducible renderer probe:
```python
from markdown_it import MarkdownIt
import mistune
s = '[review](https:../pull/200)'
print(MarkdownIt('commonmark', {'html': True}).render(s))
print(mistune.create_markdown(renderer='html', escape=False)(s))
```

The regression fix must parse **CommonMark inline and reference destination slots** as browser-equivalent first-party URLs, including same-scheme relative `https:` forms, while preserving foreign-host, wrong-repo, wrong-PR, code/comment and malformed-authority negatives. Apply the live-link veto to fully paged issue comments and to both initial and fresh pre-PATCH scans. Full actual source-module mocked `execute(apply=True)` no-PATCH regression and distinct review are required before CLEAN.

### FSR-1802-M02 (MAJOR): browser network-path triple/four slashes evade raw-HTML and URL readers

Real raw-HTML anchors `<a href="///github.com/vokerg/everfield/pull/200">review</a>` and `<a href="////github.com/vokerg/everfield/pull/200">review</a>` point to the first-party protected PR #200 in an HTTP(S) browser. WHATWG treats three or more leading slashes as a network-path authority; Python `urlsplit` instead reports an **empty `netloc`** and a path beginning `/github.com/...`. The corrected source's `raw_html_relative_references_pr` uses `urlsplit(candidate.replace("\\\\", "/"))`, takes the **no-netloc** branch and demands the local first-party `[owner, repository, "pull"]` path prefix. It sees `["github.com", "vokerg", "everfield", "pull", "200"]` instead and misses the PR. The other `PR_URL` reader matches the `///...` string, but also applies `urlsplit` and sees an empty host, so it skips it. Raw-HTML `HTMLParser` emits the href, yet neither reader triggers the veto. The same bypass reaches both initial and late open-issue/comment scans.

Independently executed Node 22 WHATWG:
```javascript
const base = 'https://github.com/vokerg/everfield/issues/1';
for (const s of ['///github.com/vokerg/everfield/pull/200',
                 '////github.com/vokerg/everfield/pull/200',
                 '///evil.test/vokerg/everfield/pull/200',
                 '///github.com/vokerg/everfield/pull/201'])
  console.log(new URL(s, base).href);
```
Results are first-party `https://github.com/vokerg/everfield/pull/200` for the first two positives, foreign `https://evil.test/vokerg/everfield/pull/200` for the negative-host control, and `https://github.com/vokerg/everfield/pull/201` for wrong-PR. Independent Python stdlib `urllib.parse.urlsplit` and the **copied actual source `PR_URL`** confirmed empty netloc for `///github.com...` / `////github.com...` while `PR_URL` nonetheless finds the URL-looking candidate. Tested before adding this finding; this is not approval of the separate non-operational issue comment #6232191152 that also reported a similar hypothesis.

Fix requires WHATWG-equivalent first-party network-path authority for raw `<a href>` and eligible Markdown references, with strict host/repo/PR number, protocol, credentials/port, `.diff`/`.patch`, foreign host and malformed-input controls. Independently execute whole-module `eligibility` and mocked initial/fresh `execute(apply=True)` to verify **zero PATCH** whenever live first-party triple-slash URLs occur in an active issue/comment.

## Limitations, operational boundaries and next route

I read the **entire 1,694-line source module in chunks** over the GitHub connector and independently executed both Markdown renderers, Node WHATWG URL, the verbatim source-pattern/gate probe, and verified current GitHub issue/PR/CI/blob state. **The exact Python module could not be mounted in the isolated test runtime** (raw.githubusercontent.com DNS blocked); it was **not imported or executed as one unit**. Consequently, the real full-module `references_pr` return, `eligibility`, `live_open_issue_references`, `execute(apply=True)`, API pagination, malformed/edited owners and live PATCH tests were **not independently executed**. The code-path finding is statically deterministic plus independently reproduced rendering/URL behavior; **no full-module CLEAN is claimed**. CI remains an authored control. The residual last-millisecond non-atomic GET/PATCH race also remains unproved and must be acknowledged.

**Required next route:** Materialize **one bounded mandatory correction of frozen OPEN/DRAFT source PR #1801** for FSR-1802-M01 and FSR-1802-M02 on a new source issue/branch, preserving all inherited protected blobs and changing only the source script and own handoff; get exact-final-head hosted read-only CI success with write-capable retirement skipped; require a **new genuinely distinct full-module security reviewer**. Keep #1801, #1797, #1799, and this permanently reviewer-only evidence PR OPEN/DRAFT, unmodified and **never merge reviewer-only PRs**. No mutation of GitHub issues, PR retirement, source or main, `--apply`, source integration, production or release. Any later source integration needs separately claimed explicit authority and **SQUASH ONLY**, even following CLEAN.

**Final review disposition: CHANGES_NEEDED; PR #1801 NOT INTEGRABLE.**
