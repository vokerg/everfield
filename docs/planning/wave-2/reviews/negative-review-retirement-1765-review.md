# Independent security review — Issue #1768 of source #1765 / PR #1767

**Disposition: CHANGES_NEEDED.** **0 BLOCKER / 1 MAJOR (FSR-1768-M01) / 0 correction-requiring MINOR.**
**Mandatory bounded successor:** Issue #1769 (blocked until this review's valid immutable terminal).
**Authority:** independent reviewer task `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-12-REV-01`, branch `planning/issue-1768`; reviewer-only documentary PR, **NEVER MERGE**.

## Scope, frozen identity, provenance

- Canonical current-main base at claim: `7da4c2d50412fe134c8632264908560b8b7995ce`; Issue #1147 binding comment `5675066392`, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, canonical activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` (ancestral).
- Source issue #1765 first winning CLAIM `6153424697` created `2026-10-13T19:25:48Z`; exact-head REVIEW_READY `6153516451` created `2026-10-13T19:30:57Z`, unedited and within its six-hour lease. The source PR #1767 remains OPEN/DRAFT, `planning/issue-1765` HEAD `4a529940ff24c10c6295606b42de884999e48d14`, base `main`.
- Exactly eight source diff paths checked against GitHub PR files. Six unchanged Git blobs match frozen #1760, and one prior script `4d8e5bec3b1a152af5ef5a78e3728cdf7b3c03c3` becomes corrected script `a80b080dccbed14ed76fc8b8ec8121ded9bb7ca6`; one new source #1765 handoff.
- Hosted exact-head workflow `38455070860`: read-only `self-test` job `115495578556` **success** at source HEAD; mutating `retire` job `115495652976` **skipped**. This is producer-authored regression evidence, **not** independent proof of security correctness or integration authority.

## FSR-1768-M01 (MAJOR): double dot-segment normalization in different orders is not browser-equivalent

**Code path:** In immutable source blob `a80b080dccbed14ed76fc8b8ec8121ded9bb7ca6`, the `references_pr` **relative CommonMark target** branch first computes `urllib.parse.urljoin(issue_base, destination)` (Python removes literal `..` segments), then computes `browser_path_segments(resolved.path)` (Python unquotes and removes encoded dot segments). A browser uses one ordered WHATWG path algorithm for both escaped and unescaped dot segments; applying the two different algorithms in sequence can discard an encoded segment before it has the intended effect. The resulting source prefix comparison misses a real first-party PR URL.

**Exact independent reproduction**, on Python and Node.js 22 WHATWG `new URL` (network-free), with base `https://github.com/vokerg/everfield/issues/1` and target `../issues/tmp/%2e%2e/../pull/+0200`:

| Stage | Result |
| --- | --- |
| Actual rendered Markdown | `[review](../issues/tmp/%2e%2e/../pull/+0200)` |
| Browser WHATWG `new URL(target, base).href` | `https://github.com/vokerg/everfield/pull/+0200` |
| Python `urllib.parse.urljoin(base, target)` | `https://github.com/vokerg/everfield/issues/tmp/pull/+0200` |
| Frozen source `browser_path_segments(urlsplit(urljoin(...)).path)` | `['vokerg','everfield','issues','tmp','pull','+0200']` |
| Exact extracted source relative-slot predicate, `pr_segment_matches` and encoded-path guard | **False for PR #200** |

Independently executed the exact extracted production relative Markdown matching logic and `browser_path_segments`/alias predicate with this fixture and three variants. No evidence was inferred from source-authored tests alone. The direct absolute-path handler behaves differently and is not evidence of coverage for the relative handler.

| Variant target | Browser WHATWG URL | Source extracted relative-slot verdict |
| --- | --- | --- |
| `../issues/tmp/%2e%2e/../pull/+0200` | `https://github.com/vokerg/everfield/pull/+0200` | False |
| `../issues/tmp/.%2E/../pull/200` | `https://github.com/vokerg/everfield/pull/200` | False |
| `../issues/tmp/%2E./../pull/0200` | `https://github.com/vokerg/everfield/pull/0200` | False |
| `../issues/tmp/%2e%2e/../pull/200.patch` | `https://github.com/vokerg/everfield/pull/200.patch` | False |

**Mechanism:** Browser first removes `tmp` for encoded `%2e%2e`, then removes `issues` for raw `..`; the source's pre-pass `urljoin` instead removes the encoded segment and raw `..` together, leaving `tmp`. Numeric `+0200`, `0200`, canonical `200` and `.patch` are already acknowledged as PR #200 aliases in the source contract.

**Security consequence:** The single `references_pr` check is called on every active issue title/body/comment in `eligibility`. `execute(apply=True)` invokes the same `eligibility` at both initial and immediately-before-PATCH scans, so a *stable* active issue reference of this form is not vetoed by either scan. An otherwise authentic, negative-reviewed, sufficiently aged reviewer-only draft could be closed despite an active GitHub issue linking to it. This finding does **not** claim that any live PR was actually closed or that the mocked end-to-end PATCH path was executed.

## Test limits, other gates and non-authority

This review inspected the actual frozen source's URL logic, eligibility call sites, complete paginated active issue scanner, double-scan `execute(apply=True)` control flow, and the CI workflow. The independent runtime witness executed an **exact extracted production predicate**, not the entire frozen 1209-line module: the reviewer environment did not have the GitHub connector's source bytes available as a local executable file. In particular, no independent full-module mocked end-to-end execution, ownership-collision fuzzing or pagination-failure regression was represented as complete. Since a concrete MAJOR defect was already reproduced, the verdict is CHANGES_NEEDED regardless of those uncompleted positive-approval tests. No `--apply`, live API PATCH, issue closure, reviewer-source mutation or integration occurred.

Source tests, owner lease, frozen HEAD, six inherited blobs and positive CI are not substitutes for browser equivalence. The read-only workflow does not automatically authorize closure. A final fresh API scan and a later PATCH are not atomic even after this defect is fixed; the residual last-millisecond race remains an explicit limitation.

## Exactly one blocking successor and correction scope

Issue **#1769** is the single mandatory scoped remediation, blocked until this issue's valid negative terminal. It must inherit frozen #1767's eight files, preserve seven exact Git blobs, alter only `tools/planning/retire_negative_review_prs.py`, and add its own handoff. Fix relative URL normalization with **one ordered WHATWG-equivalent dot-segment reduction** (or fail closed for ambiguous first-party escaped-dot references) *before* any Python `urljoin` normalization can erase encoded dot path information. Add independent-WHATWG oracle tests and full-module mocked `eligibility`/first-and-fresh `execute(apply=True)` regressions with zero PATCH for each active title/body/comment link; retain strict origin/repo/port/alias/lease/72-hour/pagination controls. Exact-head read-only CI, fresh distinct required code/security review, and later separately owner-authorized current-main-compatible **SQUASH-only NONCANONICAL** integration remain mandatory.

**No source PR merge authorization, reviewer-only PR merge, canonicality, production, release, gameplay authority, or live retirement is conferred by this negative review.**
