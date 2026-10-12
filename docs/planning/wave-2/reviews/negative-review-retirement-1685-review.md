# Mandatory independent security review — corrected negative-review PR retirement #1685

**Review issue:** #1689 (`FACTORY-NEGATIVE-REVIEW-PR-RETIREMENT-01-REM-02-REV-01`)  
**Review owner claim:** GitHub comment #6130327055, created `2026-10-12T18:36:23Z`, sole unedited first CLAIM  
**Reviewer execution:** `frontier-independent-pr-retirement-audit-1689-gpt6-20261012-2035-cph-01`  
**Disposition:** **CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR (FSR-1689-M01), 0 correction-requiring MINOR.** No approval, source integration, deployment, canonicality or review self-integration.

## 1. Immutable subject and independence

The source under review is Issue #1685 first owner CLAIM #6127268023 (GitHub-created `2026-10-12T15:23:34Z`) and in-lease owner STATUS(REVIEW_READY) #6127516839 (created `2026-10-12T15:38:15Z`). Its **OPEN/DRAFT** source PR #1688 (`planning/issue-1685` -> `main`) is frozen at exact HEAD `53b298d2c2189fc9ede6137655a977f54862cd5a`, base `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`, exactly three paths:

- `tools/planning/retire_negative_review_prs.py` blob `caf8d61687874479978df9a834511b85b7a583bd`, 593 source lines;
- unchanged inherited `.github/workflows/retire-negative-review-prs.yml` blob `e141fffcbb95c02fa215ffec3c403e0e93d1fc90`;
- `docs/planning/handoffs/issue-1685.md` blob `4b1a1df398efca3c99be219ccde0eab0139efd3a`.

Author's exact-head hosted Actions run #38271419112: **SUCCESS**, `self-test` job #114886320960 SUCCESS (Python compile and authored negative regression suite), mutating `retire` job #114886392218 **SKIPPED**. These are author-authored tests, not independent acceptance. Frozen predecessor genuinely distinct negative reviewer #1679 REVIEW_STATUS(CHANGES_NEEDED) #6118961848, original required report `docs/planning/wave-2/reviews/negative-review-retirement-1676-review.md` immutable blob `747f03cd490fdf1d63a862e7c26dd35d5c7116f2`, found B01 and M01/M02. Its own reviewer-only PR #1684 and rejected predecessor sources PRs #1678/#1668 remain unmerged.

This review execution is separate from source #1685 producer, old #1676 producer, and reviewers #1669/#1679. Read-only investigation inspected actual frozen script, workflow, handoff, prior negative report, real GitHub source issue/comment/PR metadata and hosted CI; no source, prior reviewer, main or PR mutation. Active canonical binding remains Issue #1147 terminal #5675066392, `docs/planning/PLANNING-PROGRAM-v1.md` blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`; main at claim was `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`. This reviewer-only document conveys no new authority.

## 2. Previously raised falsification cases — bounded observations

**FSR-1679-B01 (same SHA, wrong task branch/fork/base/missing repository or wrong mission):** The frozen `eligibility()` now compares actual `pr.head.ref` to `planning/issue-N` and both actual `pr.head.repo.full_name` and `pr.base.repo.full_name` to the configured repository, rejecting absent/non-dictionary values. The script additionally compares the issue-contract mission to the first CLAIM and frozen terminal. The embedded negative cases cover same-SHA wrong ref, fork, wrong base repo, null head/base repo and changed issue mission. The independent structural review confirms the named previously exploited checks now reject those inputs; this statement is not a global repository-origin or issue-authorship proof.

**FSR-1679-M01 (comment-only reference invisibility):** The new `live_open_issue_references()` enumerates currently open GitHub issues (excluding PRs), re-fetches each comment list, rejects duplicate IDs, mismatched declared counts, missing text, more than 200 issues / more than 1000 comments per issue and unreadable API results; both initial and immediately-pre-PATCH `execute()` paths call it. `eligibility()` checks `comments_coverage_complete` and vetoes the exact `#N` token in issue title/body or loaded comment bodies. Thus an active comment literally containing `PR #200` is vetoed, and the tested count-mismatch aborts rather than closing. However **the accepted reference syntax is incomplete**, as found below. GitHub's final GET/scan-to-PATCH interval remains non-atomic; no claim of a conditional GitHub PR-close transaction is made.

**FSR-1679-M02 (task-specific report filename):** The issue's declared `## Mission ID` and independently declared review report file path, not just reviewer terminal `artifact_paths`, now determine the accepted mission and exact file path. Exactly two `added` files with lowercase SHA40 blob IDs are required: that exact report and `docs/planning/handoffs/issue-N.md`; the terminal's two artifact paths must match. The old colluding substitution of `unrelated-review.md` in both terminal and diff therefore fails. Missing/multiple distinct report paths and wrong mission fail closed.

**Inherited FSR-1669 safeguards:** The strict one-first-CLAIM/two-operational-record subset, same issue/branch/session/mission, unedited server-created owner and terminal, six-hour current-owner lease, age at least 72 hours, negative `REVIEW_STATUS(CHANGES_NEEDED)`, prohibited later PROGRESS/RESUME/RECOVER/HANDOFF/competing terminal, frozen source PR head and draft identity all remain structurally guarded. The main-only scheduled/dispatch `retire` job is not authorized on PR; default invocation without `--apply` is dry-run. An exception during GitHub coverage aborts processing rather than being promoted to permission.

## 3. FSR-1689-M01 — MAJOR: a live canonical PR URL bypasses the reference veto

**Location:** frozen source script `eligibility()`, at the active-reference loop (around lines 160–180), and `live_open_issue_references()` (around lines 310–360), read from exact blob `caf8d61687874479978df9a834511b85b7a583bd`.

The code correctly loads every open issue comment, but defines its *sole* PR-reference recognizer as:

```python
marker = re.compile(rf"(?<![0-9])#{number}(?![0-9])")
# only marker.search(issue["title"] + "\n" + issue["body"])
# or marker.search(each_comment["body"]) can veto retirement
```

This accepts `#200` but does **not** accept GitHub's normal standalone canonical PR URL `https://github.com/vokerg/everfield/pull/200`, the `/pull/200/files` URL, or the API `/pulls/200` URL. All three are direct unambiguous references to PR #200, not incidental issue-number prose, and can occur as the *only* live comment or body reference. An open task can therefore explicitly depend on the review surface by linking the PR without the literal `#200` token and yet receive **no veto**.

**Independently executed read-only Python 3 reproduction of the exact frozen regular expression** (no GitHub mutations):

```python
import re
number = 200
marker = re.compile(rf"(?<![0-9])#{number}(?![0-9])")
assert marker.search("Do not retire reviewer PR #200")
assert not marker.search("Keep https://github.com/vokerg/everfield/pull/200")
assert not marker.search("https://api.github.com/repos/vokerg/everfield/pulls/200")
assert not marker.search("https://github.com/vokerg/everfield/pull/200/files")
```

All assertions passed. For a direct eligibility falsification from a frozen source checkout, the existing `self_test()` baseline has an otherwise eligible issue #199, PR #200, canonical negative reviewer CLAIM/terminal, two added review files, and aged source. Immediately after its `active` fixture is defined, add **only to a temporary read-only checkout**:

```python
canonical_link = {
    **active,
    "body": "This active task requires the review surface",
    "live_comments": [
        {"id": 1, "body": "Keep https://github.com/vokerg/everfield/pull/200"}
    ],
}
assert ok(opened=[canonical_link])  # unsafe accepted result
```

The original `ok(opened=[active])` is false for `PR #200`; this otherwise identical complete-coverage `canonical_link` instead passes the source's exact marker test and reaches the final positive eligibility return. This is a control-flow deduction backed by direct regex execution, **not** a claim that the entire frozen script was executed in the review runtime, nor that a destructive GitHub PATCH was attempted. The pre-PATCH fresh scan repeats the same incomplete marker, so freshness and pagination do not repair it.

**Impact / severity:** **MAJOR**, correction-requiring. Once aged 72 hours, a known-negative but still required reviewer-only draft could be retired despite a live issue/comment linking exactly to that PR via the normal GitHub URL. This violates the explicit policy “do not retire while any live issue references the review PR” and removes an active review surface from the open PR queue. The fact GitHub PRs retain closed provenance does not permit knowingly bypassing the preservation gate.

**Required bounded correction:** Recognize exact repository-qualified GitHub PR URLs (web `/pull/N` and API `/pulls/N`, including `/files` or fragment/query suffixes where unambiguous), as well as `#N`, in both active issue bodies and comments. Do not interpret arbitrary similar numbers, foreign repository links, issue URLs, or substrings such as `/pull/2000` as this PR. Keep all complete-count fail-closed pagination, ambiguity/unknown API aborts, fresh immediate pre-PATCH reads and non-atomicity warning. Add negative regression fixtures for canonical-link-only references in body **and** live comments and a genuinely eligible no-reference positive; preserve all previously passing B01/M01/M02/FSR-1669 cases.

## 4. Disposition / next exact route

**REVIEW_STATUS(CHANGES_NEEDED): 0 BLOCKER, 1 MAJOR FSR-1689-M01, 0 correction-requiring MINOR.** This single reproducible correction-requiring failure prohibits `REVIEW_READY`/CLEAN for the source, despite authored exact-head CI success and improvements over #1676.

Materialize only **one** new bounded mandatory corrective source route for FSR-1689-M01, based on freshly rederived main and separately claimed ownership. The eligible correction may own `tools/planning/retire_negative_review_prs.py` and its new issue-specific handoff while inheriting the exact workflow blob unchanged from #1688; do not mutate source #1685/#1688, predecessor negative source/reviewer branches or main. Require hosted exact-final-head **read-only** compile/regressions with mutating job SKIPPED and a **fresh genuinely independent required security reviewer**, different from that corrective author and this reviewer. Only a future CLEAN review can feed separately owner-authorized expected-HEAD/current-main compatible **squash-only NONCANONICAL** source integration.

The reviewer-only PR for this report remains permanently DRAFT/UNMERGED. No immediate `--apply`, canonical promotion, implementation/gameplay, engine/readiness, accessibility, truth/consent, release or production authority is created.
