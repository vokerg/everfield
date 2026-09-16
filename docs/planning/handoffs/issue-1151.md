# Issue #1151 handoff — canonical recovery lease timing

## State

Recovered continuation under schema-3 STALE recovery on 2026-09-16. Current recovery generation is Issue #1151 comment `5693459961`; winning STALE intent is `5693458788`; recovered generation is original CLAIM `5675133391`.

## Frozen authority

- active canonical binding: Issue #1147 terminal `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation/current main at recovery: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- source review: Issue #1118 terminal `5659656349`
- finding: `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01`
- task branch: `planning/issue-1151`
- recovered pre-handoff head: `9f203b2f00aee30af7817a3f18ed986e09b78682`
- draft PR: #1152, base `main`, exact recovered head above before this handoff-only commit

## Work present

The branch modifies only `tools/planning/frontier_maintenance.py` and `tools/planning/frontier_maintenance_v5.py` before this handoff. It adds canonical GitHub-server timestamp parsing, the 21,600-second ownership lease, PROGRESS renewal/EVIDENCE-cap reconstruction, 600-second ORPHAN maturity, and composes temporal predicates into v5 winning-owner recovery reconstruction. Deterministic attack cases are embedded in the maintenance self-tests.

The stale continuation also corrected PR #1152 back to draft state, as required for the review surface.

## Verification state

Repository/GitHub identity checks completed: branch is six commits ahead / zero behind canonical activation main before this handoff; PR #1152 is open, draft, mergeable, and its pre-handoff diff contains exactly the two maintenance paths. No GitHub Actions run is attached to the recovered head.

A local clone/test attempt from this execution environment could not run because outbound DNS to `github.com` is unavailable. Therefore this continuation does **not** claim the required v1-v5 self-test / `py_compile` acceptance as freshly executed. Do not publish `REVIEW_READY` until those exact-head checks are run and pass.

## Next required action

Run on the exact new branch head after this handoff commit:

`python3 -m py_compile tools/planning/frontier_maintenance.py tools/planning/frontier_maintenance_v5.py`

and current-main v1-v5 maintenance self-tests. If all pass, re-check ownership, main, branch head, PR draft/head/files, and finding closure; then publish terminal `STATUS(REVIEW_READY)` routing exactly one fresh required degraded-independent review. If any check fails, remediate only within Issue #1151 owned paths and re-run the full bounded suite.

## Authority boundary

`NOT_CANONICAL`. No integration, verification-PASS, implementation-readiness, engine-selection, release, production, decision, or canonical authority. Any later main publication remains separately authorized and squash-only.
