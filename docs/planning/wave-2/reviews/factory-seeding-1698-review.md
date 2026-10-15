# Issue #1703 — independent security review evidence (nonterminal)

**Status: CHANGES_NEEDED — 0 BLOCKER / 1 MAJOR FSR-1703-M01 / 0 correction-requiring MINOR.** The initial material was a nonterminal handoff; the distinct continuation below adds a **negative** security disposition based on a concrete code-path witness, not a clean verification or full-module independent acceptance. No source or reviewer-only PR has been merged and no live mutation was run.

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


---

## Continuation after HANDOFF_READY #6131254239 — independent security disposition

**Continuation identity:** new owner `frontier-resume-factory-security-1703-gpt6-20261012-2143-cph-01` after sole `RESUME_INTENT` #6131404287 and valid `RESUME` #6131408354, both immutable, source handoff #6131254239 at draft review HEAD `f635014eb23888546a88799edae65758371f3e19`. Current main remains `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`, active canonical program binding unchanged. This is a continuation **of the same mandatory review Issue #1703**, not an optional second review.

**Disposition: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR FSR-1703-M01, 0 correction-requiring MINOR.** The submitted source packet is not security accepted and must not be integrated.

### FSR-1703-M01 (MAJOR) — unauthenticated terminal result SHA can close an inauthentic owner terminal

**Frozen exact code blobs:** base `tools/planning/frontier_maintenance.py` SHA `b30690ae302f28cb2295fddd0b78a882e2a71b83`; v5 `tools/planning/frontier_maintenance_v5.py` SHA `413dc3a5f0e1fc707ce709f1b6730b50fa142560`, both from unchanged source PR #1702 HEAD `7a3a67cfafb5f8f9d28ce40c6e5b10eb1f78eb9a`.

The base `reconcilable_terminal_from_comments()` (lines ~705–745) checks `head_sha`/`work_sha` **only for syntactic SHA40** and same owner/actor/mission identity. `closure_authorized_terminal_from_comments()` (lines ~749–810) validates sole ownership, branch-name strings, trusted complete capsule parsing and lease, but does **not fetch the task branch tip or compare either terminal result SHA with that tip**. Its v5 `terminal_owner_generation_is_current()` (lines ~59–334) verifies the recovery **source** SHA via `transition_head_verifier` only for HANDOFF/STALE winners. For a direct CLAIM→DONE path the final acceptance expression checks winning generation/lease and absence of prior HANDOFF/terminal, **not `terminal.head_sha`, `terminal.work_sha` or live task-ref provenance**. `close_terminal_open_issues()` (base ~984–1013) immediately rechecks the same incomplete predicate before `PATCH`, so a fresh GET does not repair a deterministic missing terminal-head check. The old FSR-1691-B01 HEAD-authentication fix applies to recovery-source intents, not this terminal-result branch.

**Independent executable claim-only predicate-path reproduction** (local Python standard library, copied exact relevant owner/terminal acceptance expressions and syntactic base terminal parser subpath, with mocked immutable record intake and clock): issue #104, first/sole claim at 2026-10-12T10:00:00Z, `planning/issue-104` actual live tip `A = a×40`, claimant actor `author-a`, `observed_head_sha=A`, terminal status DONE 1 hour later with correct `ownership_generation_comment_id=1`. Tested:

| Variant | Observed extracted-path authorization | Correct rule |
| --- | --- | --- |
| Terminal `head_sha=A, work_sha=A` | **True** | accept if other gates pass |
| Terminal `head_sha=B, work_sha=B`, `B=b×40` unrelated to live tip `A` | **True (unsafe)** | reject or fail closed |
| Terminal submitted by different actor | False | reject |
| Terminal with wrong task branch | False | reject |
| Terminal after 6-hour owner lease | False | reject |

The **frozen code has no terminal result SHA check in these paths**, making the second result the security bypass. Its consequences are storage closure of an issue that has no proven task result at the claimed SHA and potential loss of eligible continuation/recovery. This does **not** grant an external user the owner role; the witness assumes the same legitimately authenticated owner with an inaccurate or forged terminal result.

**Evidence limits:** The executable test is an extracted exact claim-only code-path reproduction with mocked record parsing, **not** an import of entire frozen modules. Full independent v1–v7 executable regression, real-module mocked GitHub GET/compare, all inherited blob diffs and a live destructive PATCH were **not** performed by this continuation. Producer hosted Actions run #38297579139 and jobs #114972283304 (SUCCESS) / #114972284978 (SKIPPED) were verified independently at source HEAD but remain authored tests, not independent approval. The prior nonterminal reviewer handoff correctly noted incomplete executable acceptance. The finding is based on direct code-path inspection plus the negative/positive control witness above; no clean verdict is implied.

**Correction and route:** Exactly one bounded **required** corrective [Issue #1711](https://github.com/vokerg/everfield/issues/1711) exists, blocked until this frozen reviewer-only PR and immutable negative terminal. Validate the completed terminal `head_sha` and `work_sha` against authenticated current branch/ref+commit ancestry in the actual storage closure consumer and applicable transition terminal consumers; fail closed for missing, moved, diverged or ambiguous task ref. Preserve legitimate no-op owner terminals and proper renewal/handoff/recovery tests; authenticate independently against real corrected source and rerun full v1–v7. Last-millisecond GET/PATCH remains non-atomic and cannot be claimed solved. After corrected producer exact-HEAD CI, require a **NEW genuinely distinct mandatory independent code/security review**; only its clean result could unlock separate owner-authorized current-main-compatible **SQUASH-only NONCANONICAL** source integration. No source/reviewer PR merge, no factory --apply, no canonicality, gameplay, engine/readiness or production/release authorization.

**Reviewer path policy:** The updated review branch/PR may contain *only* this report and `docs/planning/handoffs/issue-1703.md`; both are permanently reviewer-only **non-integrable**. Do not change #1698/PR #1702 source, predecessors, or main.