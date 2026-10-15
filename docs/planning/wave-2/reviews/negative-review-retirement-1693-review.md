# Mandatory independent security review — #1693 / PR #1696

**Reviewer issue:** #1697, mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-03-REV-01`. **Disposition: CHANGES_NEEDED** — **0 BLOCKER, 1 MAJOR (FSR-1697-M01), 0 correction-requiring MINOR**. Reviewer execution `frontier-distinct-retirement-review-1697-gpt6-20261012-2115-cph-01`, independent of producer #1693, prior source #1685 and negative reviewers #1689/#1679/#1669. No source mutation, live `--apply`, or PR closure.

## Exact frozen authority and evidence

- Current `main` at review: `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`, matching exact source PR base. Active canonical program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, bound by Issue #1147 immutable comment `5675066392`; activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` is an ancestor. These do not confer implementation or integration authority.
- Producer Issue #1693 first valid, unedited owner `CLAIM` #6130818930 at GitHub server 2026-10-12T19:07:41Z, followed by a losing later same-generation competitor #6130822618 at 19:07:55Z. In-lease immutable `STATUS(REVIEW_READY)` #6130920426 at 19:13:57Z. No valid later owner generation found. The earlier first-winner, not the losing later claimant, controls the handoff.
- Frozen `OPEN/DRAFT` source PR #1696, `planning/issue-1693` to `main`, exact HEAD `cb3c41aa82775e02066c99d4a901c9653a97c63f`. GitHub changed-file API shows exactly **three ADDED** paths: `tools/planning/retire_negative_review_prs.py` SHA `368570e79f733646f44bbb42bbd617ed04407093`; `.github/workflows/retire-negative-review-prs.yml` SHA `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`; and `docs/planning/handoffs/issue-1693.md` SHA `9bf39460dbf2ea52f95fbb607cf89b1f0285195c`.
- Hosted GitHub Actions `pull_request` run #38296025245 is SUCCESS at exact HEAD `cb3c41...`: compile/full authored `--self-test` job #114967192815 SUCCESS; mutating `retire` job #114967259110 SKIPPED. This confirms configured authored tests but **is not independent acceptance**.
- Reproduced prior independent negative #1689 terminal #6130426848 (FSR-1689-M01, 0 BLOCKER/1 MAJOR/0 MINOR), reviewer-only draft PR #1692 HEAD `dd03686faee4640df7d164d0f5643dfa329948d2`. Prior source #1685 frozen PR #1688 HEAD `53b298d2c2189fc9ede6137655a977f54862cd5a` remains unaccepted.

## FSR-1697-M01 — first-party PR references with HTTPS port and diff/patch suffix bypass the closure veto (MAJOR)

**Exact implementation location:** `tools/planning/retire_negative_review_prs.py`, source blob `368570e...`, `references_pr()` lines 97–133, especially netloc comparisons 124–129 and path components 123, 130–132. Active open-issue `title`/`body`/`live_comments` rely on this result in `eligibility()` lines 211–230. `execute(apply=True)` calls the same flawed predicate for the initial pass and immediate pre-PATCH scan (lines 403–451); re-reading does not repair a deterministic missed reference.

**Independent executable reproduction:** In a Python 3 stdlib-only harness, transcribed the actual frozen `PR_URL` and `references_pr()` implementation verbatim (not a call to the whole downloaded source, unavailable to this reviewer runtime). Ran 15 positive/negative URL fixtures against PR #200; 11 matched intended safe behavior and **four expected reference vetoes returned False**:

| Active issue title/body/comment text | Observed `references_pr(text, 200)` | Required safe outcome |
| --- | --- | --- |
| `https://github.com/vokerg/everfield/pull/200` | True | veto |
| `https://api.github.com/repos/vokerg/everfield/pulls/200` | True | veto |
| `https://github.com/vokerg/everfield/pull/200/files` | True | veto |
| `https://github.com/vokerg/everfield/pull/200?tab=files#discussion` | True | veto |
| `https://github.com:443/vokerg/everfield/pull/200` | **False** | **veto** |
| `https://api.github.com:443/repos/vokerg/everfield/pulls/200` | **False** | **veto** |
| `https://github.com/vokerg/everfield/pull/200.diff` | **False** | **veto** |
| `https://github.com/vokerg/everfield/pull/200.patch` | **False** | **veto** |
| `https://github.com/vokerg/other/pull/200` | False | permit as unrelated |
| `https://github.com.evil.test/vokerg/everfield/pull/200` | False | permit as unrelated |
| `https://github.com/vokerg/everfield/pull/2000` | False | permit as unrelated |
| `https://github.com/vokerg/everfield/pull/200abc` | False | permit as unrelated |
| `https://github.com/vokerg/everfield/issues/200` | False | permit as unrelated |
| `Preserve #200` | True | veto |
| `No live PR references` | False | permit as unrelated |

`urlsplit(...).netloc` retains `:443`, so strict equality to `github.com` or `api.github.com` fails. For direct GitHub `.diff` and `.patch` links, the component is `200.diff` or `200.patch` rather than the required `200`. These are unambiguous references to GitHub PR #200. The owner script's own green tests cover `/files`, query, fragments, lookalike hosts and `#200`, but not these variants.

**Security impact:** With an otherwise proven aged, negative reviewer-only draft and an active open issue referring to that PR solely through one of these equivalent URLs, `live_open_issue_references()` can have perfectly complete title/body/comment coverage yet `eligibility()` wrongly returns eligible. The second read also wrongly returns eligible and the code can issue the `PATCH state=closed` despite a live explicit reference. This defeats the code's conservative storage-retirement condition. It is a **MAJOR correction-requiring finding**; no actual PR was closed by this review.

**Required correction:** A single bounded new source episode should classify first-party PR URLs by normalized trustworthy hostname and port, expressly recognizing safe default HTTPS `:443`, and GitHub's PR `.diff`/`.patch` endpoints without conflating `/pull/2000`, `/pull/200abc`, foreign repository, attacker host, or issue URLs. On malformed/ambiguous potential first-party URLs fail closed rather than infer nonreference. Re-test matched active issue title, body, loaded comments and immediate pre-PATCH changed-comment veto with both bypasses, alongside legitimate no-reference positive and incomplete pagination, wrong/edited counts, duplicates, wrong head/fork/base, exact report path/SHA, competing authority, strict YAML and 72-hour lease. Keep no-atomicity admission; no live `--apply`.

## Other examined gates and limitations

Static code inspection plus the hosted CI confirms that reviewer-only PRs are restricted to owner-authored, open/unmerged DRAFT with task-named head ref, exact same repository for head/base, precise two-added-path report and handoff, task-contract mission/report, issue closed/completed and simple two-record owner/negative-review history. Operational capsule parsing checks trusted owner login/association and unedited timestamps; the negative terminal must precede the exact six-hour lease expiry; >=72h grace is required. Active issue/comment count, page completion and duplicate IDs reject uncertain reads. A later status or extra ownership/progress record in review issue makes this conservative subset ineligible. These checks address the predecessor attack classes FSR-1679-B01/M01/M02 and FSR-1669-B01/M01/M02/M03 for this bounded subset; no independent full-source/test-suite execution is claimed here.

Remaining structural limitation (not a distinct correction-requiring finding): GitHub GET/scan-to-PATCH is **non-atomic**; new references can appear after the final scan. The source explicitly acknowledges this; no CAS close guarantee is claimed.

## Disposition and routing

**CHANGES_NEEDED: 0 BLOCKER / 1 MAJOR (FSR-1697-M01) / 0 correction-requiring MINOR.** Do **not** integrate source #1696 or reviewer-only evidence PR. The exact source is NOT security accepted, NOT canonical, NOT production/readiness authorized. Materialize **exactly one mandatory bounded remediation of FSR-1697-M01** on a separately owned, fresh-main task branch, require exact-head nonmutating CI then a NEW genuinely independent mandatory adversarial review. Only a future clean terminal review plus separate authorized current-main-compatible **SQUASH-only NONCANONICAL** integration route can publish source.