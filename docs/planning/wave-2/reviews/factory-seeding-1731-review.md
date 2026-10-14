# Independent security review #1733 — successor terminal ownership gate

**Verdict: CHANGES_NEEDED — 0 BLOCKER, 1 MAJOR `FSR-1733-M01`, 0 correction-requiring MINOR.** Existing source PR #1732 must stay OPEN/DRAFT/unmerged. This is a specific independently reproduced negative security finding, **not** a comprehensive CLEAN certification, integration or GitHub closure authorization.

## Frozen source, ownership, CI, canonical binding

- Required independent review Issue **#1733**, mission `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-21-REV-01`, distinct reviewer `existing-pr-successor-owner-gate-review-1733-gpt6-20261013-cph-01`, first/sole valid winning unedited CLAIM **#6137725184** created **2026-10-13T03:43:09Z**, immediately re-fetched; fresh branch `planning/issue-1733` from current **main@`a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`**.
- Canonical Planning Program Issue #1147 binding terminal **#5675066392** and program blob **`fd4cf1119c3f86acc3af620024eea72235e81ce4`**, ancestor activation **`87c85cecfa9a2ffa464c4b36816a138bf41441af`**. Latest GitHub ancestry compare at review inception: ahead 149, behind 0.
- Frozen source Issue #1731 first winning CLAIM **#6132769733** (2026-10-12T21:17:37Z); owner `STATUS(REVIEW_READY)` terminal **#6132844276** (2026-10-12T21:22:11Z), unedited/in-six-hour lease, exact OPEN/DRAFT source **PR #1732 HEAD `86bd4a61648459b7f82f0f37ff297d5db5833f9e`**, base current main. Its **28 changed files** include inherited predecessor #1718 source plus bounded correction in `tools/planning/frontier_maintenance_v4.py` blob **`721540705e0a98ce0e3e93d4f135861f2b4c58f4`** and new source handoff. Base module blob `f7dd6640210e27e18a170633ba8f8ab0d176835d`; v5 blob `510cd909192a1fd0dc5f355a701d429962b15671`. Prior independent negative source reviewer #1725 terminal #6132710550, review-only DRAFT PR #1730.
- Hosted exact-source-HEAD PR Actions **#38310017946**, read-only validate-pr Python compile/full composed v1–v7 authored self-tests **job #115013161938 SUCCESS**, mutation-capable maintain **job #115013163776 SKIPPED**. Self-authored CI does not substitute for independent review.

## FSR-1733-M01 (MAJOR): syntactically linked but unauthorized successor terminal can consume a required route

### Actual frozen code/data path

In `tools/planning/frontier_maintenance_v5.py::v5_resolved_transition_generations`, a closed factory transition's comment list is passed to `v4.semantic_generation_from_comments`. That validates the **wrapper terminal's** result SHAs against the wrapper task branch; `v4.semantic_generation_from_terminal` handles `disposition: REQUIRED_ROUTE_ALREADY_CONSUMED_BY_TERMINAL_SUCCESSOR` and `route_consumed: true`, obtains the **different successor** terminal using either `base.reconcilable_terminal(successor_number)` or the injectable `successor_terminals` map, then checks:
1. successor terminal exists, has expected `issue_number` and exact referenced `comment_id`;
2. `base.github_verified_terminal_result_heads(successor_number, successor_terminal.head_sha, successor_terminal.work_sha)` accepts each SHA as exact live `planning/issue-N` tip or behind-free ancestor.

**This confirms SHA ancestry, not terminal owner authority.** The called `base.reconcilable_terminal_from_comments` at `tools/planning/frontier_maintenance.py` lines 747–787 explicitly implements a parser/owner-reference subset: it chooses latest parsed operational comment, checks kind/state/issue/terminal actor and mission match **the ID linked CLAIM**, plus syntactic SHA. It has **no** first-valid/lowest-ID winner, six-hour server-time expiry, prefix-scoped generation, or recovery-currentness check. Separately defined `v5.terminal_owner_generation_is_current` (which reconstructs first-winner and lease) and `base.closure_authorized_terminal_from_comments` (which uses it) are **not called on this successor** in v4's `route_consumed:true` branch. The legitimate v5 terminal-no-route path does perform owner and SHA checks, showing this is a scoped gap in the semantic route-consumption alternative.

### Independent executable negative reproduction

Used Python 3 and `dataclasses` to independently run a narrowly isolated, faithfully transcribed exact-source `reconcilable_terminal_from_comments` body on typed synthetic pre-parsed `OperationalRecord` entries, plus the exact-source successor-result decision predicate at the v4 consumption branch. The only mocked seams were operational YAML/comment-to-record parsing, a separately valid factory wrapper generation, an otherwise eligible successor issue, and `github_verified_terminal_result_heads` responding TRUE **only** when head and work are the same mocked live tip `a*40`. This keeps SHA provenance positive to isolate **owner generation** and **lease** authority; the SHA correction itself is not asserted broken.

| Synthetic successor history (#20) | Canonical expected outcome | Frozen parser + v4 semantic consumer |
| --- | --- | --- |
| CLAIM #10 actor A, then losing duplicate CLAIM #11 actor B; B posts latest `STATUS(DONE)` #12 linking #11, exact HEAD/work both equal live tip | Reject B: #10 remains first-winning owner; #11 creates no generation | **False positive:** parser returns #12, SHA authentication TRUE, wrapper returns consumed generation `(10, 2, NEXT)` |
| Sole valid CLAIM #10 at 00:00Z by A; A publishes `STATUS(DONE)` #12 at 07:00Z, head/work equal live tip, no PROGRESS renewal | Reject terminal after 6-hour lease expiry | **False positive:** parser returns #12, SHA authentication TRUE, wrapper consumes `(10, 2, NEXT)` |
| Sole valid CLAIM #10; A publishes `STATUS(DONE)` #12 at 00:05Z, exact HEAD/work equal live tip | Authorized positive control | Parser returns #12, SHA TRUE, consumed generation `(10, 2, NEXT)` |

Representative reproducible Python setup (full isolated harness exercised the two extracted function bodies):

```python
a = OperationalRecord(20,10,"2026-10-12T00:00:00Z","CLAIM","IN_PROGRESS",20,"S","A")
b = OperationalRecord(20,11,"2026-10-12T00:01:00Z","CLAIM","IN_PROGRESS",20,"S","B")
bad_b = OperationalRecord(20,12,"2026-10-12T00:02:00Z","STATUS","DONE",20,"S","B","OWNER",11,"a"*40,"a"*40)
bad_late = OperationalRecord(20,12,"2026-10-12T07:00:00Z","STATUS","DONE",20,"S","A","OWNER",10,"a"*40,"a"*40)
assert reconcilable_terminal_from_comments(20,[a,b,bad_b]) == bad_b
assert reconcilable_terminal_from_comments(20,[a,bad_late]) == bad_late
assert factory_wrapper_consumes([a,b,bad_b]) == (10,2,"NEXT")
assert factory_wrapper_consumes([a,bad_late]) == (10,2,"NEXT")
```

The wrapper's `resolved_successor_terminal_comment_id: 12` can exactly match a parser-accepted but unauthorized successor terminal. The factory thus records a source generation as `consumed` and may suppress required-next-route materialization even though the successor lacked **canonical valid owner terminal authority**.

### Independently performed vs unperformed

- **Performed:** fresh main/canonical ancestry and GitHub source/review/Actions/28-path identity checks; full exact-code read of relevant v4, base and v5 function bodies and their call paths; Python isolated target predicate reproduction above with two unauthorized synthetic cases and one valid control; review of branch-SHA verifier (returns TRUE for exact live tip without checking owner). No target GitHub issue was forged, and no production mutation performed.
- **Not performed:** import/run of the full frozen base/v2/v3/v4/v5/v6/v7 modules, complete mocked live HTTP GET/compare fault suite, full v1–v7 independent regressions or actual module `--apply`. This narrow **negative** outcome is sufficient to require correction; a complete CLEAN or universal negative-free certification is **not** claimed. The produced branch is documentation-only, not a patched source. No GitHub PATCH, ref mutation, PR close, PR merge, or game/canon/production gate change occurred.

## Exactly one mandatory successor

**Issue #1740** is materialized **BLOCKED until** this independently negative reviewer has published a reviewer-only exact-head OPEN/DRAFT two-document PR and immutable in-six-hour `REVIEW_STATUS(CHANGES_NEEDED)`. A genuinely distinct producer must inherit exact existing #1731/PR #1732 28-path source, correct only v4 and new own handoff, require **winner + current unexpired owner generation** as well as both exact live task SHA proofs for *both* fetched and injected successor terminal paths, and verify losing/stale/resumed/edited histories fail closed. Preserve proper accepted materializations and independent dispatch markers; execute exact head read-only CI, obtain **new distinct mandatory independent review** before separate authorized compatible **SQUASH-only NONCANONICAL** integration. Reviewer-only PR for #1733 **MUST NEVER MERGE**; source #1732 remains draft/unapproved/unmerged. No live closure, gameplay, readiness, engine, canonical, production or release permission.
