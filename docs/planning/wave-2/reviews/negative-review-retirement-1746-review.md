# Required independent adversarial review — #1746 / existing DRAFT PR #1751

**Review task:** Issue #1752, mission `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-10-REV-01`.  
**Reviewer:** `everfield-independent-relative-pr-retirement-review-1752-gpt6-20261013-cph-01`, sole schema-3 CLAIM #6138410324 (2026-10-13T04:43:53Z), independent execution from original security reviewer #1743 and corrective author #1746.  
**Frozen source:** Issue #1746, owner `STATUS(REVIEW_READY)` #6138235974, OPEN/DRAFT PR #1751 `planning/issue-1746`, exact HEAD `a7e9bf33f9ca3f07b8173aa96a20967e978db344`. Source script `tools/planning/retire_negative_review_prs.py` Git blob `75d344971a17d53a1cce689744ddbf24dad230d0`; six changed paths. Never modify source.  
**Baseline at reviewer claim:** current `main=f94c765de066c5aae53f8872e7857939de2bbbd4`, Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.  
**Verified source CI:** exact source-head GitHub Actions #38346443555 SUCCESS, `self-test` job #115128874383 SUCCESS, mutation-only `retire` job #115128927879 SKIPPED. Green source CI is not independent security review.

## Disposition

**CHANGES_NEEDED — 0 BLOCKER / 1 MAJOR (FSR-1752-M01) / 0 correction-requiring MINOR.** Not CLEAN; do not publish or enable retirement, promote canonicality or merge this reviewer-only PR. Required bounded successor Issue **#1756** is opened with no claimant, and remains blocked until this review's terminal. The prior distinct negative review Issue #1743 FSR-1743-M01 exposed a different relative-link omission; source #1746 corrected it, but the numeric alias defect is new.

## FSR-1752-M01 — MAJOR: real GitHub decimal aliases bypass the live-reference veto

**GitHub identity witness, observed live through connected GitHub reads on 2026-10-13:** each request below resolved to actual PR **#1751** and canonical `https://github.com/vokerg/everfield/pull/1751`, with matching source HEAD `a7e9bf33f9ca3f07b8173aa96a20967e978db344`:

| Requested real URL | Actual GitHub PR |
| --- | --- |
| `https://github.com/vokerg/everfield/pull/01751` | #1751 |
| `https://github.com/vokerg/everfield/pull/+1751` | #1751 |
| `https://api.github.com/repos/vokerg/everfield/pulls/01751` | #1751 |
| `https://api.github.com/repos/vokerg/everfield/pulls/+1751` | #1751 |

**Frozen production source and independent predicate execution:** independently transcribed exact `PR_URL`, `RELATIVE_MD_LINK_TARGET` and `references_pr` (source lines 98–217) into a separate offline Python runtime, preserving the same standard-library normalization and equality predicates. Compared `references_pr(candidate, 1751)`. All four canonical direct/relative controls returned **True**; all **eight** numeric-alias cases below returned **False**, even though the first four exact full URLs resolve live to PR #1751 and the latter four describe same-repository alias link destinations:

| Active issue text candidate | Actual frozen predicate |
| --- | --- |
| `https://github.com/vokerg/everfield/pull/01751` | False |
| `https://api.github.com/repos/vokerg/everfield/pulls/01751` | False |
| `https://github.com/vokerg/everfield/pull/+1751` | False |
| `https://api.github.com/repos/vokerg/everfield/pulls/+1751` | False |
| `[review](../pull/01751)` | False |
| `[review](/vokerg/everfield/pull/01751.diff)` | False |
| `[review](../pull/+1751)` | False |
| `[review](/vokerg/everfield/pull/+1751.patch)` | False |

Four distinct negative controls returned False as desired: `https://github.com/vokerg/everfield/pull/17510`, `https://github.com/vokerg/other/pull/01751`, `https://evil.invalid/vokerg/everfield/pull/01751`, `[review](../pull/17510)`. Canonical exact `1751` path variants and normal relative links correctly returned True. Thus correct host/repo and numeric boundaries are currently enforced, but GitHub-accepted representations of the same integer are not recognized.

**Root cause:** the absolute path loop at lines 169–181 and relative destination loop at 203–216 compare a lowercased/percent-decoded path segment directly to `str(number)`, `str(number)+'.diff'`, or `str(number)+'.patch'`. They do not canonicalize the exact GitHub PR route decimal segment `01751` or `+1751` despite both spelling variants being accepted by real GitHub. URL host/port safety logic is not itself the defect. Strict comparisons are necessary for foreign references but are not sufficient for actual first-party alias identity.

**Actual dangerous consumers:** `eligibility` source lines 294–313 iterates each active non-PR issue's title, body and every fully fetched comment and vetoes only if `references_pr` returns True. Both initial `execute(apply=True)` scan (lines 486–505) and the fresh pre-PATCH `eligibility` call (lines 506–529) reuse exactly this vulnerable predicate. Consequently an otherwise eligible 72h-aged negative reviewer-only draft with an active issue link expressed as `[review](../pull/01751)` can pass both scans and reach `PATCH state=closed` despite that live reference. There was **NO real remote --apply, PATCH or PR closure**. This is a code-path counterexample based on a real URL identity witness and extracted predicate, not a claim of having closed a live PR.

**Security consequence and priority:** mandatory MAJOR, because the retirement tool's stated safety invariant is that no linked active review PR may be automatically closed; it is silently defeated without malformed GitHub data or failing CI. Do not classify as incidental Markdown formatting. A correction must parse authentic first-party PR route IDs as bounded decimal aliases **after** host/repo/port/route checks, without accepting similar-number prefixes/suffixes, malicious host/userinfo, foreign repositories, invalid or ambiguous encodings.

## What was inspected; limits of this negative verdict

- Checked frozen six-path source diff identity and exact current source Git blob, owner #1746 terminal, independent predecessor #1743 finding, and hosted exact-head source CI success / mutating job skipped.
- Inspected source `operational` YAML authority parsing, `eligibility` owner Claim/terminal/branch/head/changed two-file packet/72h grace checks (lines 219–404), `live_open_issue_references` complete issue/comment pagination/count checks (438–483) and `execute` initial and fresh pre-PATCH rechecks (486–529). The linked-reference failure is upstream of both rechecks, independently reproduced. Other owner/lease/changed-path validations may be sound, but they cannot save a live-reference invariant once an aged candidate satisfies them.
- Reviewed authored source `self_test` coverage (lines 533 onward): it includes baseline relative Markdown positives/negatives and mock two-snapshot apply, but no leading-zero/`+` numeric alias witness. Source's genuine hosted selftest PASS is therefore consistent with the counterexample.
- **Independently executed exact extracted reference predicate**, with actual GitHub live route resolution and positive/negative controls, but **did not independently execute the complete `eligibility`/mocked `execute(apply=True)` source module** in this negative-review episode. The two-snapshot path was independently inspected, not falsely represented as executed. This negative proof suffices for CHANGES_NEEDED, not a comprehensive clean audit. The residual non-atomic pre-PATCH GitHub TOCTOU race remains separately acknowledged in source comments, not counted as a new finding here.
- Neither this reviewer nor its CI has authority to close any PR, modify frozen #1751/#1742/#1748, integrate, publish canonicality, or declare automation production safe.

## Required continuation

Existing mandatory bounded successor [Issue #1756](https://github.com/vokerg/everfield/issues/1756), `FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-11`, is the **only** new corrective root for FSR-1752-M01; it must not be claimed before the exact reviewer terminal, then needs separately owned scope, real full exact-head CI and a fresh independent security review. The reviewer-only PR for Issue #1752 includes only this report and its handoff, is OPEN/DRAFT and **MUST NEVER MERGE**. Frozen source PR #1751 remains review-ready only at its older head, **NOT clean-reviewed**, unmerged and unauthorized for live apply. All eventual main publication is separately owner-authorized current-main-compatible **SQUASH-only NONCANONICAL**.
