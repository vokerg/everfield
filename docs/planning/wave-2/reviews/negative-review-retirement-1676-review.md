# Issue #1679 — Genuinely distinct mandatory independent adversarial review of PR retirement source #1676

**Disposition: CHANGES_NEEDED — 1 BLOCKER, 2 MAJOR, 0 correction-requiring MINOR.** No security acceptance, integration or deployment authority.

## Frozen sources, exact claims and independent scope

- Current `main` at review start: `8f8223b0c58956bbc888760ef14f63fa79d2117d`. Active canonical Planning Program v1: Issue #1147 binding comment #5675066392, file blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Mandatory corrective source Issue #1676 `STATUS(REVIEW_READY)` terminal #6118444170, independently claimed by `frontier-retirement-security-remediate-1676-gpt6-20261012-0820-cph-01` under first CLAIM #6118395790. Source DRAFT PR #1678 exact HEAD `d8f580233307b919167fa9e80e9e69b7d3ae24d4`; exactly three paths: `tools/planning/retire_negative_review_prs.py` immutable blob `a155ecf0c48ba9f49ae906a00d737ced7e1fc0a3`, unchanged `.github/workflows/retire-negative-review-prs.yml` blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`, `docs/planning/handoffs/issue-1676.md` blob `08988e9487925e4795d9c652bdf6164fc64f3fdf`.
- Authored PR-head Actions run #38208828431: `self-test` job #114678215180 SUCCESS, mutating `retire` job #114678243295 SKIPPED. No `--apply` executed in this review, and authored CI is not an independent security assessment.
- Prior independent negative review #1669 terminal #6118352033 found 1 BLOCKER + 3 MAJOR in original source #1667 / frozen DRAFT PR #1668. Source #1676 fixes the previously documented generic unlinked RESUME/CLAIM, stale pre-PATCH snapshots, broad handoff-prefix acceptance and conflicting later status examples, but newly inspected boundaries remain unsafe.
- Reviewer #1679 first winning immutable schema-3 CLAIM #6118874788, actor `frontier-independent-pr-retirement-audit-1679-gpt6-20261012-0820-cph-01`, is a genuinely different execution from #1676's author, earlier #1667 producer, and earlier #1669 reviewer. Review branch `planning/issue-1679` is from exact current main, and owns review report and own handoff only.

## Independent falsification method and observed results

Read all 422 lines of frozen source Python, its own GitHub workflow, source/negative-review handoffs, review task contract, and actual immutable GitHub PR/owner/CI metadata. Executed the source `StrictLoader`, `operational`, `timestamp` and `eligibility` predicates **transcribed without security-relevant changes** from immutable source blob into an isolated Python 3 + PyYAML 6.0.3 local harness; no GitHub writes. The test's baseline duplicates the source's valid two-comment reviewer-only negative fixture: one properly formed CLAIM for Issue #199, in-lease owner-authored negative REVIEW_STATUS, completed closed issue, 10-day-old review, draft PR #200 targeted to main with exact SHA and two added review files. All results below are returns from the eligibility predicate, not speculative GitHub PATCH success:

```text
baseline negative reviewer-only PR                               True
PR HEAD branch planning/issue-777, not planning/issue-199          True  <-- false positive
PR HEAD repository vokerg/other-fork, not vokerg/everfield          True  <-- false positive
report unrelated-review.md despite required review-report name    True  <-- false positive
currently open issue refers to PR #200 only in its comment         True  <-- false positive
```

The source-authored self-test does NOT exercise these variants: it changes PR SHA, generic wrong file path `unrelated.md` (without the allowed `-review.md` suffix), or issue *body* reference, but never actual task branch, repo identity, wrong-pattern-compliant report, or open issue comments. For independent reproduction directly from a checkout of source PR #1678 at the specified HEAD, `runpy.run_path("tools/planning/retire_negative_review_prs.py")["eligibility"]` loads the original predicate without executing `--apply`. Using the existing source `self_test` baseline as above, apply these exact separate mutations:

```python
# A: freeze terminal/owner/head SHA but point the GitHub PR at another branch.
bad_pr = {**pr, "head": {**pr["head"], "ref": "planning/issue-777"}}
assert eligibility(bad_pr, issue, [claim, terminal], files, [], now)[0]

# B: same branch and hash, but from a different repo/fork.
bad_pr = {**pr, "head": {**pr["head"],
          "repo": {"full_name": "vokerg/other-fork"}}}
assert eligibility(bad_pr, issue, [claim, terminal], files, [], now)[0]

# C: report file is not the report required by the REVIEW ISSUE contract;
# change both GitHub changed-file record and terminal artifact_paths to
# the same misleading but syntactically allowed file name.
bad_path = "docs/planning/wave-2/reviews/unrelated-review.md"
bad_files = [{**files[0], "filename": bad_path}, files[1]]
bad_terminal = {**terminal,
    "body": terminal["body"].replace(files[0]["filename"], bad_path)}
assert eligibility(pr, issue, [claim, bad_terminal], bad_files, [], now)[0]

# D: an open remediation issue comments on the reviewer PR, not issue body.
open_with_comment_only = [{
    "number": 300, "title": "Still active remediation",
    "body": "Needs review diff preserved",
    "comments": [{"body": "Do not retire reviewer PR #200"}],
}]
assert eligibility(pr, issue, [claim, terminal], files,
                   open_with_comment_only, now)[0]
```

No test requires a forged GitHub API response, lease renewal, a direct collaborator compromise, or a live destructive request. These are accepted *structural* false positives within the claimed fail-closed eligibility policy.

## FSR-1679-B01 — BLOCKER: PR identity is not the review task's actual branch or repository

At `retire_negative_review_prs.py::eligibility` (~lines 105–127, 176–226), the source authenticates only PR `number`, `title` `[#issue]`, `user.login`, `base.ref`, draft state and `head.sha`. The immutable COMMENT's task branch is checked internally against `planning/issue-{issue}`, but **the actual GitHub PR's `head.ref` and `head.repo.full_name` are never compared to that branch and `vokerg/everfield`**. The frozen SHA can be the tip of multiple refs (Git permits identical tip commits), or from another repository/fork. A similarly titled, owner-authored draft from a different branch can satisfy all checks and be closed without proving it is the reviewed task branch.

This violates exact-task-branch ownership and the “only proven reviewer-only draft PR” authority boundary. There is no GitHub PATCH conditional expected-head safeguard in this script; the head-SHA recheck only confirms the *same potentially wrong* ref still has the expected tip.

**Correction:** require PR `head.ref == planning/issue-{review issue}`, `head.repo.full_name == vokerg/everfield`, `base.repo.full_name == vokerg/everfield`, and independently authenticate the actual review issue's source/task identity, not its `[PLAN-v1]` prefix alone. Reject null/inconsistent repo metadata, wrong branch or unknown GitHub origin before even considering state mutation. Test exact same-SHA/wrong-ref and fork branch cases, not only head drift.

## FSR-1679-M01 — MAJOR: live open-issue comments are invisible to the active PR-reference veto

At `eligibility` (~lines 130–136), the sole active-work veto searches only the `title` and `body` of each open issue. The preceding `execute` pre-PATCH live refresh (~lines 287–293) correctly re-fetches open *issue objects*, but never any open issue's **comments**, hence even its “fresh veto” cannot see a comment on an otherwise generic active remediation issue that directly names the review PR. The exact fourth fixture returns `True`.

The task contract requires preserving the reviewer-only draft while any live issue **references that PR**; GitHub operational records, remediation links and continuation notes frequently live in comments. An issue's body may predate the linked review PR. Closing its requested review surface while the issue comment explicitly needs it violates the preservation rule. The last-millisecond GitHub non-atomicity is acknowledged and not scored separately; this is a deterministic missing-read issue **before** the PATCH.

**Correction:** authenticate a complete, fresh open issue reference set including comment references before closing; use a conservative bounded candidate-specific lookup or fail closed if API coverage/pagination/rate limit is unknown. Update acceptance fixtures for references in issue body **and** later issue comments and for changes between scan and pre-PATCH. Do not treat a stale pre-PATCH body-only list as exhaustive.

## FSR-1679-M02 — MAJOR: report naming checks the directory pattern, not the review contract

At `eligibility` (~lines 144–164, 191–224), the script requires its handoff `docs/planning/handoffs/issue-N.md`, exactly two **added** paths and SHA40 file objects, and a report matching the generic regex `docs/planning/wave-2/reviews/*-review.md`. It also requires the same two paths in the terminal's `artifact_paths`. But it does **not** read or authenticate the task review issue's *named* report requirement (e.g. #1679 demands `negative-review-retirement-1676-review.md`, and prior #1669 demanded `negative-review-retirement-1667-review.md`). An unrelated but pattern-compliant `unrelated-review.md` can be declared in terminal and PR files and accepted; the third independent fixture demonstrates exactly that. A SHA40-looking string and self-referential terminal cannot prove the artifact is the **authorized task report**.

**Correction:** link the report path to the issue contract's actual expected file identity, plus file SHA/status and immutable reviewer terminal `artifact_paths`; reject wrong-pattern-compliant as well as wrong-directory cases. Do not invent generic global naming conventions; bind to the named issue's exact required report path.

## Proven positives and absence of other authority

The new strict PyYAML loader rejects obvious duplicate-string authority keys, YAML aliases and explicit tags; owner/terminal in-lease single-CLAIM requirement rejects unlinked RESUME, extra PROGRESS and competing claims; the new mutating path refreshes PR, review issue, comments, changed files and open issue objects. The workflow is read-only on `pull_request` and may mutate only on a separately squash-published main schedule/dispatch. The run/job evidence corroborates hosted producer tests, **not** independent proof. No source or main mutation occurred here, and this review does not assert every schema-3/YAML/TOCTOU path is exhaustively audited.

## Negative terminal and next exact route

**CHANGES_NEEDED — 1 BLOCKER FSR-1679-B01, 2 MAJOR FSR-1679-M01/M02, 0 correction-requiring MINOR.** No CLEAN, verification PASS, deployment or merge granted. Existing rejected original source #1667/PR #1668, former independent reviewer #1669/PR #1674, new corrected source #1676/PR #1678 and reviewer-only PR associated with this report must remain frozen/DRAFT/UNMERGED as applicable.

Materialize exactly **one** scoped mandatory follow-on remediation of B01/M01/M02 from current main in a **different source execution**, restricted to `tools/planning/retire_negative_review_prs.py`, its owned handoff and unchanged inherited workflow; all predecessor PR branches frozen. Require authored exact-final-head read-only CI, then a **new genuinely distinct required adversarial security review**, and only if clean a separately owner-authorized, current-main-compatible, expected-head **SQUASH-only NONCANONICAL source publication**. No game/content, canonical, readiness, engine, truth/consent, accessibility, production or release authority.
