# Mandatory independent security review #1729 — escaped CommonMark punctuation

**Disposition: CHANGES_NEEDED. 0 BLOCKER, 1 MAJOR `FSR-1729-M01`, 0 correction-requiring MINOR.** This is a negative security review of EXISTING draft source PR #1728, NOT a clean acceptance or permission to close/merge any PR.

## Frozen authority and identity
- Reviewer task #1729 mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-08-REV-01`; first valid unedited CLAIM **#6137588181** at GitHub server **2026-10-13T03:32:26Z**, actor `existing-pr-backslash-url-review-1729-gpt6-20261013-cph-01`, branch `planning/issue-1729`, fresh main `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. Immediately re-read issue comments and confirmed the sole/winning first ownership record.
- Current canonical program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, Issue #1147 binding terminal #5675066392, activated at `87c85cecfa9a2ffa464c4b36816a138bf41441af`. GitHub commit ancestry comparison to main returned `ahead=149, behind=0`; canonical file blob on main matches.
- Frozen producer #1726 first owner CLAIM #6132484379 (2026-10-12T20:57:39Z), owner `STATUS(REVIEW_READY)` #6132556759 (2026-10-12T21:02:41Z), both unedited and in the 6-hour lease. OPEN DRAFT PR **#1728**, exact HEAD **`c51789012237523d7ac01f70b3e34f10dfc6191e`**, base current main, 4 paths. Source script blob **`61250b824784c468de335915fa10c1814dc4d26d`**; inherited workflow `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`; previous handoff `088bb6afd8651c941ba1045d3ffab9b10da5d4c1`. Only source code, workflow and two handoffs comprise diff.
- Exact-head Actions #38307924510, read-only self-test job #115006348760 SUCCESS, mutating retire job #115006413984 SKIPPED. Authored CI is not independent security acceptance.

## FSR-1729-M01 (MAJOR): a rendered live PR link escapes both closure vetoes
At exact HEAD, `tools/planning/retire_negative_review_prs.py::references_pr` first applies `html.unescape(text)`, then scans `PR_URL` and strips backslash escapes only for `\\/`. **CommonMark resolves other punctuation escapes in destinations too**, including escaped scheme colon, hostname dot, suffix dot and query `?`. A Markdown link can therefore render as a live first-party GitHub PR URL but not be recognized by the raw-text closure predicate.

An independent Python 3 reproduction used the **verbatim URL regular expression and decision flow independently transcribed from the retrieved exact-source `PR_URL` / `references_pr` function**, with `REPO=vokerg/everfield`. Each link was rendered separately through `markdown_it` 4.2.0 and `mistune` 3.2.1. Both renderers agreed on the shown href, while the frozen predicate returned the stated outcome:

| Markdown source inside `[review](...)` | Rendered href (both renderers) | `references_pr(raw, 200)` |
| --- | --- | --- |
| `https\\://github.com/vokerg/everfield/pull/200` | `https://github.com/vokerg/everfield/pull/200` | **False — bypass** |
| `https://github\\.com/vokerg/everfield/pull/200` | `https://github.com/vokerg/everfield/pull/200` | **False — bypass** |
| `https://api.github\\.com/repos/vokerg/everfield/pulls/200` | `https://api.github.com/repos/vokerg/everfield/pulls/200` | **False — bypass** |
| `https://github.com/vokerg/everfield/pull/200\\.diff` | `https://github.com/vokerg/everfield/pull/200.diff` | **False — bypass** |
| `https://github.com/vokerg/everfield/pull/200\\.patch` | `https://github.com/vokerg/everfield/pull/200.patch` | **False — bypass** |
| `https://github.com/vokerg/everfield/pull/200\\?tab=files` | `https://github.com/vokerg/everfield/pull/200?tab=files` | **False — bypass** |
| `https://github.com/vokerg/everfield/pull\\/200` | `https://github.com/vokerg/everfield/pull/200` | **True — previous fix works** |
| `https://github.com/vokerg/everfield/pull/200` | same | **True — positive control** |

The exact caller in `eligibility` checks the open issue's **title + body**, then all fully loaded **comment bodies**, via this same predicate. `execute(apply=True)` re-requests PR, issue, comments, files and open issues, and calls **the same `eligibility`** for the late pre-PATCH scan. Thus any of the above bypass payloads placed in an active issue title/body/comment can evade *both* snapshots. The bypass does not defeat every other owner/age/identity check, but it invalidates the required veto for an otherwise eligible negative reviewer-only draft.

### Reproduction and scope limits
Read-only operations: GitHub exact source fetch and four-file patch inspection; independent Python 3 reproduction of the extracted URL predicate using `re`, `html`, `urllib.parse`; independent MarkdownIt/Mistune rendering. Representative command structure:

```sh
python3 - <<'PY'
# Independently transcribe exact-source PR_URL and references_pr into an
# isolated read-only harness; set REPO='vokerg/everfield'.
# For each case, print (raw, references_pr(raw,200),
#                      MarkdownIt().render(raw), mistune.html(raw)).
PY
```

Results: six renderable first-party target-PR variants missed, two legitimate positives recognized. Independently **inspected but NOT executed**: complete 955-line source module import, comprehensive owner/72-hour regression suite, mocked full `execute(apply=True)` test, and actual live Github closure. The causal vulnerability is in the independently exercised source predicate and its directly inspected shared callers; this negative finding is **not** a claim of comprehensive clean certification or a proof of all other paths.

**No live `--apply`, GitHub PATCH, reviewer/source branch mutation, PR closure, main merge, or authorization upgrade occurred.** A final GET/PATCH non-atomic interval remains even after this particular URL fix.

## Required next route and authority
Exactly one BLOCKED bounded corrective successor, **Issue #1738**, exists for `FSR-1729-M01`; only after this issue's **immutable in-lease REVIEW_STATUS(CHANGES_NEEDED)** and its own exact-head reviewer-only OPEN DRAFT PR may a genuinely distinct next producer claim it. Correct the *existing* #1728 source logic by inheriting exact source code/workflow/handoffs, changing the URL predicate/tests in the successor's own branch and adding its own handoff; retain strict first-party GitHub/API authority, numeric PR boundaries, HTML entities, punctuation escape mixtures, all active issue locations and first+late zero-PATCH mocks. Require source CI, then yet another distinct required security review. Only independent CLEAN and separate authorization may permit a current-main compatible **SQUASH-only NONCANONICAL** source publication. The reviewer-only PR of #1729 must **never merge**, and #1728 remains draft/unmerged and **not approved**. No canon/readiness/production/release authority.
