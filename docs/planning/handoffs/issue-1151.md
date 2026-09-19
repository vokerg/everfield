# Issue #1151 handoff — canonical recovery lease timing

## State

Recovered continuation under schema-3 STALE recovery on 2026-09-19. Current recovery generation is Issue #1151 comment `5739724719`; winning STALE intent is `5739724011`; recovered source lease anchor is PROGRESS comment `5693468470`. The branch was recovered at exact head `afc98f3d55e67d9360a7eecdc3e67a04edb2eff9`.

## Frozen authority

- active canonical binding: Issue #1147 terminal `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- current main immediately before this final remediation commit: `222692312193cb9633ba22859a311c7c70189af7`
- post-activation main changes are confined to unrelated character-content/review provenance; current-main maintenance v1/v5 blobs remain `2256d10c22b27e9952072875f7fb9a14ef8e25cc` and `63c37ff752a1f10a7e00e0818b56463e7089459f`
- source review: Issue #1118 terminal `5659656349`
- finding: `FACTORY-CONVERGENCE-06-REM-02-REV-MAJ01`
- task branch: `planning/issue-1151`
- draft PR: #1152

## Work present

The remediation changes only `tools/planning/frontier_maintenance.py` and `tools/planning/frontier_maintenance_v5.py`, plus this handoff. v2-v4 remain unchanged.

The v1 layer adds canonical GitHub-server RFC3339 parsing, the 21,600-second ownership lease, valid PROGRESS renewal reconstruction with the three-consecutive-EVIDENCE cap and HEAD_ADVANCE reset, immutable renewal evidence validation, and exact 600-second ORPHAN maturity.

The v5 layer composes those temporal predicates into winning CLAIM/RESUME/RECOVER reconstruction. STALE recovery is accepted only after exact lease expiry of the current generation; ORPHAN recovery is accepted only after exact probe maturity with no valid owner. Premature attempts have zero authority effect.

Final self-review found and corrected one in-scope temporal displacement case: a valid owner-authored terminal published while the current generation is unexpired must block later STALE recovery from that ended generation. The bounded fix now recognizes that displacement while preserving the canonical exact-boundary rule: an attempted owner terminal created exactly at expiry is itself non-authoritative and therefore does not block a lawful later STALE recovery. Deterministic attack cases cover both sides of that boundary.

## Verification state

The earlier recovered branch source was reconstructed from the GitHub connector and each v1-v5 local file was verified byte-for-byte against its Git blob SHA before execution. `py_compile` and all v1-v5 self-tests passed on that exact source. After the final bounded terminal-displacement correction, local `py_compile` and the complete nested v1-v5 self-test suite also pass.

This handoff is committed together with the bounded v5 correction. After that final branch head exists, the exact repository blobs must be re-fetched/re-hashed and the complete compile plus v1-v5 self-test suite must be run once more before publishing `STATUS(REVIEW_READY)`. The authoritative final exact-head result belongs in the producer terminal comment.

No GitHub Actions run is attached to the producer branch. Absence of CI does not create review or integration authority.

## Next required action

On the exact final branch head, verify branch/blob identity, run full `py_compile` and v1-v5 self-tests, re-check current main/canonical binding/ownership/PR draft and changed paths, and confirm self-review is 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR. Then publish producer `STATUS(REVIEW_READY)` routing exactly one fresh required degraded-independent review. Do not integrate before that required review.

## Authority boundary

`NOT_CANONICAL`. No integration, verification-PASS, implementation-readiness, engine-selection, release, production, decision, or canonical authority. Any later publication remains separately authorized and squash-only.
