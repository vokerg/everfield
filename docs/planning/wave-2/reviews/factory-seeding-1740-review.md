# Independent required security review — corrected factory successor authority PR #1744

**Mission:** FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-22-REV-01 (Issue #1745).  
**Disposition:** **CHANGES_NEEDED**; **0 BLOCKER, 1 MAJOR (FSR-1745-M01), 0 correction-requiring MINOR**. This is *negative evidence*, **not** a comprehensive CLEAN certification.  
**Reviewer execution:** `existing-pr-distinct-factory-security-review-1745-gpt6-20261013-cph-01`, not source #1740 owner `existing-pr-successor-owner-remediate-1740-gpt6-20261013-cph-01`, predecessor #1731 owner, nor previous #1733 reviewer.

## Immutable inputs and authority

- Current main at review: `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`.
- Active canonical program: blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; canonical issue #1147 terminal binding #5675066392; activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.
- Review source: Issue #1740 first-owner CLAIM #6137941667, owner `STATUS(REVIEW_READY)` #6138019245, **OPEN/DRAFT PR #1744** exact HEAD `f2acdb1d7c81d08ce192bf86c4ee55e63a4b8826`.
- Corrected v4 `tools/planning/frontier_maintenance_v4.py` exact Git blob `50e3586dd1135c277e808572cc65cc4e9c6a0277`. Its 28-path inherited precursor is #1731 / PR #1732 frozen HEAD `86bd4a61648459b7f82f0f37ff297d5db5833f9e`, negative separate reviewer #1733 terminal #6137771042 and reviewer-only PR #1741. #1740 modifies only corrected v4 and adds own handoff to the inherited 28 paths (29 total).
- Exact-head source-authored GitHub Actions #38344794933 SUCCESS, read-only v1–v7 validation job #115123558785 SUCCESS; mutating maintenance job #115123559998 SKIPPED. Authored CI is not independent security review.

## FSR-1745-M01 — MAJOR: transition *wrapper* owner is never authenticated before route consumption

The FSR-1733-M01 fix correctly adds a fresh, strict `base.closure_authorized_terminal_from_comments(successor_number, ...)` gate for the **referenced successor** on the `route_consumed:true` path (frozen v4 lines 121–151). However it leaves the **transition wrapper's own** authentication path unchanged:

1. `v4.semantic_resolved_transition_generations` (lines 176–190) fetches a closed transition issue's GitHub comments and calls `semantic_generation_from_comments`.
2. `v4.semantic_generation_from_comments` (lines 155–173) calls only `base.reconcilable_terminal_from_comments(number, comments)` followed by `base.github_verified_terminal_result_heads(number, terminal.head_sha, terminal.work_sha)`; it **never calls** `base.closure_authorized_terminal_from_comments` or `v5.terminal_owner_generation_is_current` for this **wrapper**.
3. The exact base implementation `reconcilable_terminal_from_comments` (blob `f7dd6640210e27e18a170633ba8f8ab0d176835d`, lines 747–787) checks latest parsed terminal, OWNER-looking actor/mission/owner comment linkage and syntactically valid head/work SHAs. It **does not** reconstruct the lowest-valid CLAIM winner or six-hour GitHub created_at owner lease. Its source docstring calls it a deliberately limited subset.
4. `v4.semantic_generation_from_terminal` (lines 64–94) checks wrapper declared issue, kind, state, owner-mode *label*, source issue/comment/disposition/route but **does not** validate the wrapper's current owner. The `EXACT_REQUIRED_REVIEW_SUCCESSOR_MATERIALIZED` branch (lines 96–109) returns the source generation before any successor terminal closure check. The `REQUIRED_ROUTE_ALREADY_CONSUMED_BY_TERMINAL_SUCCESSOR` branch can also return that generation after **authenticating a genuine successor**, while the wrapper remains invalid.
5. `v4.materialize_missing_transitions` (lines 196–215) uses semantic resolved generations in `v2.source_generation_consumed`; therefore false wrapper terminal acceptance can suppress materialization of an otherwise required successor.

A valid SHA from a real GitHub branch tip/ancestor is independent of whether **the actor who published the wrapper's terminal** was the valid, unexpired owner; Git commit authenticity does not repair schema-3 temporal/contender authority.

### Independently reproduced bounded counterexamples

The reviewer transcribed the **exact conditional owner-linkage predicate** from frozen `base.reconcilable_terminal_from_comments` lines 747–787 into a read-only Python fixture with already-parsed `OperationalRecord`-shaped records, injecting `records` at the upstream parser boundary. Each terminal used a true 40-hex `head_sha`/`work_sha`, same wrapper issue #30, `kind: STATUS`, `state: DONE`, `authority_mode: OWNER`, and matching actor/mission for its referenced CLAIM. Console results:

```text
good parser accepts terminal: 50 owner: 40
losing_duplicate_claim parser accepts terminal: 50 owner: 45
seven_hour_expired_claim parser accepts terminal: 50 owner: 40
```

- **Losing duplicate**: first claimant #40 at 00:00:00Z, later claimant #45 at 00:00:05Z, terminal #50 at 00:00:10Z references #45; parser accepts although #45 is the losing owner.
- **Expired**: sole claimant #40 at 00:00:00Z; terminal #50 at 07:00:10Z references #40; parser accepts despite the canonical 21,600-second lease ending at 06:00:00Z.
- **Valid control**: first claimant #40 at 00:00:00Z, terminal #50 at 00:00:10Z references #40; parser accepts.

A second source-byte structural inspection of frozen v4 confirmed that the consuming wrapper function invokes the parser-only and SHA checks, **not** strict closure, and that wrapper authority is absent from the direct `semantic_generation_from_terminal` entry path. For each negative counterexample, a genuine branch-authenticated SHA plus matching materialized successor issue would continue through the source branch and mark the source generation resolved even though schema-3 authority forbids the wrapper's terminal. A genuine strict successor could also be supplied for the other disposition; this fix only protects the successor.

**Test limitation:** The above is a bounded extracted-source predicate reproduction and frozen source control-flow analysis, **not** an independently imported full v1–v7 suite, GitHub-mutating end-to-end execution, nor a claim that all security invariants were exhaustively tested. The full source-authored hosted suite succeeded, but independent CLEAN certification is prohibited because this MAJOR remains. No live `--apply`, GitHub PATCH, PR close or merge was run.

## Required bounded correction / disposition

**CHANGES_NEEDED: 1 MAJOR FSR-1745-M01.** Introduce fresh, complete, unedited GitHub-comment-based first-winner/current-owner/lease/HEAD-proof validation for the **transition wrapper** on both public consuming entry paths (`semantic_generation_from_comments` and direct `semantic_generation_from_terminal`, including injected terminal), while retaining the existing strict validation of the actual successor. Ensure that a caller-supplied terminal cannot bypass fresh wrapper authentication. Test true first owner, losing duplicate, expired terminal, invalid STALE/ORPHAN/PROGRESS/HANDOFF, complete pagination, moved Git ref and same-tip/ancestor SHA, both allowed dispositions and real successors, against full imported v1–v7 source. Fail closed on incomplete or ambiguous evidence.

Single successor **Issue #1747**, `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-23`, is materialized but **BLOCKED until** this review's immutable terminal and reviewer-only exact-head OPEN/DRAFT PR are present. It alone may inherit #1744 source into a fresh issue-scoped branch, correct only v4 plus new handoff, run final-head read-only CI, and route a **new genuinely distinct mandatory review**. No integration even after a clean review without a separate owner-authorized main-compatible **SQUASH-only NONCANONICAL** route. Reviewer-only draft evidence must **never be merged**.
