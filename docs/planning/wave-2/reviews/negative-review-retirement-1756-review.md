# Mandatory independent security review — source #1756 / PR #1760

**Review Issue:** #1761, mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-11-REV-01`.  
**Distinct reviewer execution:** `independent-security-review-1761-gpt6-20261013-cph-01`; sole GitHub first-owner CLAIM #6153307345, timestamp 2026-10-13T19:19:13Z. This is not the producer execution for #1756 and has never mutated source #1760.  
**Claim-time main:** `7da4c2d50412fe134c8632264908560b8b7995ce`; active Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.  
**Frozen source:** owner #1756 CLAIM #6152331066 and exact-head `STATUS(REVIEW_READY)` #6152466745, OPEN/DRAFT PR #1760 branch `planning/issue-1756`, exact HEAD `480f1618be0b8a6e19c1777b7cda2cce042dc29e`, full Python module Git blob `4d8e5bec3b1a152af5ef5a78e3728cdf7b3c03c3` (1177 lines). Changed file count **7**: workflow + four prior handoffs + this task's handoff + source script (see source terminal).  
**Source CI:** run #38447296157 on exact final HEAD, job #115468889078 `self-test` SUCCESS, mutation-only job #115468963822 `retire` SKIPPED. This is author-written self-test evidence, not independent security acceptance.

## Disposition

**CHANGES_NEEDED — 0 BLOCKER / 1 MAJOR FSR-1761-M01 / 0 correction-requiring MINOR.**

A browser-recognized, live first-party PR URL can escape the linked-open-issue retirement veto. The frozen source is NOT clean reviewed and MUST NOT be squash-merged or enabled for `--apply`. The reviewer-only draft PR for #1761 contains **only this report and its own handoff** and MUST NEVER MERGE. The bounded mandatory successor is [#1765](https://github.com/vokerg/everfield/issues/1765), blocked until valid terminal review.

## FSR-1761-M01 — percent-encoded dot segment and Python/browser resolution divergence (MAJOR)

**Root cause:** Source `unsafe_encoded_pr_path` (around lines 114–118) conservatively rejects malformed `%` escapes or encoded `/`, `\\` and `%`, but allows encoded `.` (`%2e`). The relative CommonMark link path (around lines 196–216) uses `urllib.parse.urljoin(issue_base,destination)`, then `urllib.parse.unquote(resolved.path)` and direct path-prefix comparison. Python's `urljoin` leaves encoded dot segments in place when normalizing. Browsers use WHATWG URL processing, which treats `%2e%2e`, `.%2e` and `%2e.` as parent-directory segments *before navigation*. Thus the browser lands on a same-repository PR route that the Python reference predicate does not recognize. The direct absolute-URL parser also fails if the encoded-dot segment appears before `/pull/` because it compares path prefixes before browser-like dot normalization.

**Independent reproduction:** Reobserved frozen `references_pr`, `pr_segment_matches` and `unsafe_encoded_pr_path` directly from the 1177-line source; reproduced the exact reference predicates in an isolated Python runtime, preserving the regex, unescaping, percent checks and relative `urljoin`/prefix logic. Separately evaluated the exact destinations against Node's standard WHATWG `new URL(destination, 'https://github.com/vokerg/everfield/issues/1')` semantics. No network writes.

| Active issue Markdown link | Frozen `references_pr(..., 200)` | WHATWG browser destination |
| --- | --- | --- |
| `[review](../pull/+0200)` (control) | **True** | `/vokerg/everfield/pull/+0200` |
| `[review](../issues/%2e%2e/pull/+0200)` | **False** | `/vokerg/everfield/pull/+0200` |
| `[review](../issues/.%2e/pull/0200)` | **False** | `/vokerg/everfield/pull/0200` |
| `[ref]: ../issues/%2E./pull/0200` | **False** | `/vokerg/everfield/pull/0200` |
| `[review](/vokerg/everfield/issues/%2E%2E/pull/0200)` | **False** | `/vokerg/everfield/pull/0200` |
| `[review](../issues/%252e%252e/pull/0200)` (ambiguous-control) | **True** | encoded path retained; conservatively vetoed |

The exact relative Python routine for `../issues/%2e%2e/pull/+0200` produces path segments `['vokerg','everfield','issues','..','pull','+0200']`, rather than expected `['vokerg','everfield','pull','+0200']`. Both `unsafe_encoded_pr_path` and relative match return False, so `references_pr` returns False. The WHATWG browser yields `https://github.com/vokerg/everfield/pull/+0200`, the same route as the recognized control. The same finding applies to a real source PR number, not merely the fixture `200`. Independently confirmed against the connected live GitHub API that numeric aliases `+01760` and `01760` both resolve to exact existing canonical PR #1760.

**Dangerous consumer:** `eligibility` checks complete active issue titles, bodies and loaded comments with `references_pr`. Its negative result permits continued evaluation of an otherwise eligible old rejected reviewer-only draft. `execute(apply=True)` calls the same predicate both in the first scan and again in the fresh pre-PATCH scan; therefore a stable encoded-dot live reference is invisible in **both** scans. This can result in `PATCH state=closed` while a live issue still links to that PR. **No real PATCH, closure or `--apply` was performed.** One contrary witness suffices to reject the safety invariant regardless of other valid owner/lease/provenance checks.

## Additional inspected surfaces, verification limits

- Read the full source module text (all 1177 lines by ranges), including `StrictLoader`, `operational` comment validation, single-owner/terminal/72h `eligibility`, bounded `paged` and `live_open_issue_references`, entire `execute` dual-snapshot pre-PATCH call path, authored `self_test`, and main guard. No separate owner/provenance defect is asserted.
- Compared source #1760 against its declared exact seven-file PR scope; checked first winning owner claim, unedited in-lease REVIEW_READY, source head blob identity, GitHub Actions job results, and canonical binding on unchanged main.
- Independently executed the **exact reference predicate as transcribed**, standard-library URL semantics and WHATWG browser counterexample. Did **not** represent the independently transcribed snippet as executing the **entire frozen Python module**, or claim that the authored CI tested this new case. No independent full-`execute(apply=True)` test was run in this episode; negative result is supported by code-path inspection and the path-identity counterexample, not by a fabricated comprehensive PASS.
- The existing unavoidable microsecond GitHub check/PATCH race is separately documented in source and is not counted as FSR-1761-M01. Other failure modes remain outside the scope of this bounded negative verdict.

## Required successor and nonauthority

Only new corrective issue [#1765](https://github.com/vokerg/everfield/issues/1765) covers **FSR-1761-M01**. It is BLOCKED until this review publishes matching immutable schema-3 `REVIEW_STATUS(CHANGES_NEEDED)`. A new sole owner on fresh main must inherit all seven frozen source paths from #1760 with **six blob identities unchanged**, patch only `tools/planning/retire_negative_review_prs.py`, add own handoff, add full actual-module regression tests with both first and second mocked pre-PATCH scans, obtain exact-final-head hosted CI and yet **another genuinely distinct** mandatory security review. Safest bounded defense is fail-closed for ambiguous first-party encoded-dot path rather than guessing routing equivalence. Source and reviewer-only draft must remain unmerged until later separately authorized current-main expected-head **SQUASH-only NONCANONICAL** publication of a clean-reviewed correction. No live retirement, canon, production, release, gameplay, or readiness authority here.
