# Issue #1740 — Correct successor owner authority for existing PR #1732

## Scope and provenance
Mandatory bounded correction of FSR-1733-M01 in genuinely independent CHANGES_NEEDED review Issue #1733 terminal comment 6137771042, review-only OPEN/DRAFT PR #1741 frozen HEAD 8f50aa35321cdcd7a722b405e710a46e4a514c77. Source #1731 OPEN/DRAFT PR #1732 frozen HEAD 86bd4a61648459b7f82f0f37ff297d5db5833f9e; its owner STATUS(REVIEW_READY) #6132844276 was source-authored, and its exact-head v1-v7 CI passed but was NOT independent review. This task's sole first CLAIM is #6137941667, GitHub-created 2026-10-13T04:01:16Z, actor existing-pr-successor-owner-remediate-1740-gpt6-20261013-cph-01, branch planning/issue-1740 from main a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c. Active canonical Issue #1147 binding #5675066392; planning program blob fd4cf1119c3f86acc3af620024eea72235e81ce4 and activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af.

## Exactly bounded changed-path envelope
The original 28 changed file paths of PR #1732 were inherited using their exact Git blobs in first task commit 73eba224b55c13ae0019e85ca23f53fdfc9d9b19, based on then-current main. Only inherited `tools/planning/frontier_maintenance_v4.py` was modified; this own handoff `docs/planning/handoffs/issue-1740.md` is the sole additional path, yielding maximum 29 paths relative to main. Frozen review and source branches/PRs untouched. All 27 other inherited blobs unchanged.

## Finding and corrective behavior
The prior `route_consumed: true` branch of `v4.semantic_generation_from_terminal` accepted a parser-only `base.reconcilable_terminal` or caller-injected `successor_terminals` object, then verified only branch ancestry of HEAD/WORK. A losing claimant or terminal seven hours after its first CLAIM could authenticate the same Git SHAs but have **no schema-3 ownership authority**; this incorrectly erased mandatory successor liveness.

The correction consumes the route only if a fresh, complete GitHub successor comment read is accepted by existing `base.closure_authorized_terminal_from_comments`. That validator enforces unedited trusted operational records, unique IDs, schema-3 first-winning prefix-scoped owner, HANDOFF/STALE/ORPHAN recovery and HEAD_ADVANCE rules, six-hour immutable GitHub-created-at lease, and both result SHA GitHub branch/ancestor evidence. The wrapper's exact successor issue/comment binding remains required, and any supplied successor map must exactly equal the authenticated live terminal. Errors, partial/untrusted snapshots, mismatch, losing/expired owners fail closed. The existing independent SHA verification is intentionally retained as defense in depth.

Actual v4 self-tests now exercise the strict closure consumer using read-only mocked task refs, real generated GitHub-style operational comments and positive first owner, losing duplicate claimant, expired owner, injected mismatch, edited terminal, unavailable pagination, with preserved v1–v7 composed tests and positive exact SHA cases. These are author tests, NOT independent acceptance; see GitHub Actions exact-final-head result and owner terminal evidence for authoritative statuses.

## Required next gates and stop conditions
1. Keep this source PR OPEN/DRAFT with exact 29-path diff; run hosted exact-final-head read-only Python compile and complete v1–v7 composed regression tests; mutation-capable maintain job must be SKIPPED. Correct own source if tests fail, then test the new exact final head.
2. Only after checks pass may the winning in-lease owner record schema-3 STATUS(REVIEW_READY) against exact PR/head, explicitly noting no independent security certification or integration.
3. Materialize/route to a **genuinely different required adversarial code/security review** that executes actual full corrected code and tests owner, recovery, lease and injected bypasses. A renamed actor inside this execution is not distinct.
4. Only a separate authorized current-main expected-head-compatible **SQUASH-only NONCANONICAL** integration route may publish source later. No live --apply, GitHub PATCH/closure, retire, main integration, engine, gameplay/readiness, canon, release, or production authority here.

Neither source-authored hosted green CI nor an open draft PR are merger authority. Review-only PRs must never be merged.
