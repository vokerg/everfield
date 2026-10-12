# Issue #1703 — independent security review evidence (nonterminal)

**Status: IN_PROGRESS / NO REVIEW DISPOSITION.** This document is a bounded handoff of independently inspected evidence, **not** a PASS, CHANGES_NEEDED, verified closure authorization, or independent executable reproduction. No source or reviewer-only PR has been merged and no live mutation was run.

## Fixed source identity and preconditions

- Reviewer issue: #1703; winning unedited owner CLAIM #6131170566, `2026-10-12T19:29:23Z`; actor `frontier-independent-head-review-1703-gpt6-20261012-2130-cph-01`.
- Active canonical binding: Issue #1147 comment #5675066392; planning-program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Frozen producer #1698: first owner CLAIM #6131001591, in-lease terminal STATUS(REVIEW_READY) #6131140141 at 2026-10-12T19:27:30Z; source PR #1702 OPEN/DRAFT HEAD `7a3a67cfafb5f8f9d28ce40c6e5b10eb1f78eb9a`, base `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
- Mandatory predecessor independent negative reviewer #1691, terminal #6130964726, finding FSR-1691-B01; reviewer-only PR #1699 frozen HEAD `5208af50226b531e8c5f4287e15c7aa9bb4fb1bd`.
- Source code Git blobs: `tools/planning/frontier_maintenance.py` = `b30690ae302f28cb2295fddd0b78a882e2a71b83`; `tools/planning/frontier_maintenance_v5.py` = `413dc3a5f0e1fc707ce709f1b6730b50fa142560`.
- Authored hosted exact-source-HEAD Actions run #38297579139 SUCCESS; validate job #114972283304 SUCCESS; mutating job #114972284978 SKIPPED. This is producer evidence, **not** independent review.

## Read-only structural inspection performed

The real frozen source was read at exact ref using GitHub's file API. In v5, `handoff_head_authorized` (roughly lines 89–104) now compares the HANDOFF status's `head_sha == work_sha == lease.observed_head_sha`, and `winning_intent_for` (roughly 162–244) rejects HANDOFF intents whose observed SHA differs from the exact source handoff head. STALE candidates must match the previous generation's lease observed head and the recorded source anchor; the grant binds the lowest valid intent. `terminal_owner_generation_is_current` checks the winning owner and unexpired terminal lease.

In the closure consumer, `closure_authorized_terminal_from_comments` (base roughly 749–811) passes the actual `github_verified_recovery_source_head` callback to v5. The latter (roughly 459–486) queries the live `planning/issue-N` Git ref and either compares an exact tip or verifies that the source SHA is a strict ancestor via GitHub compare with zero behind commits. Missing or non-ancestor refs fail closed in code. `close_terminal_open_issues` (roughly 984–1014) re-reads eligibility before PATCH. These are **inspection observations**, not executable verdicts.

The live GET/compare cannot authenticate historical HEAD chronology because GitHub does not expose a branch reflog; the source documents that limitation. REST GET-to-PATCH is not atomic, and no CAS guarantee has been established. No assertion of security sufficiency follows from static inspection.

## Remaining mandatory verification before any review terminal

1. In an executable environment, import **these exact source blobs** and run actual base/v5 predicates and closure consumer with new reviewer-origin positive/negative fixtures. Specifically falsify forged unrelated HANDOFF/STALE intent+grant SHA (including same forged value in both), winning/losing intent, exact lease expiry/renewal and delayed terminals, genuine source-head ancestry, missing/divergent GitHub branch, malformed/edited comments and wrong issue/mission/branch.
2. Independently run exact v1–v7 composed regression tests against the frozen source plus explicit #1664/#1673 literal successors and v6/v7 behavior; inspect source workflow permissions and all 23 frozen changed-file blob identities against #1690 (except the two corrected scripts and new handoff).
3. If correction-requiring code failure is reproduced, record exact fixture and counts, create **one** bounded mandatory remediation successor, publish reviewer-only DRAFT exact-head PR and in-lease `REVIEW_STATUS(CHANGES_NEEDED)`. If all independent gates pass with 0 BLOCKER/MAJOR/correction-requiring MINOR, publish clean terminal `REVIEW_STATUS(REVIEW_READY)` only after reviewer-only exact-head draft PR.
4. Do not close issues/PRs, run `--apply`, touch source PR #1702, or authorize integration from this handoff.

The current reviewer environment could inspect authenticated GitHub files but could not import the entire frozen Python codebase into an isolated runnable filesystem. **Independent executable acceptance was therefore not established**, so this handoff deliberately stops short of a terminal review decision. Continue the same existing issue under the canonical HANDOFF RESUME route, not a new review task.
