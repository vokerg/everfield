# Issue #1155 handoff — terminal validity and strict RFC3339 recovery

## State

Bounded remediation of required Review #1153 findings `FACTORY-CONVERGENCE-06-REM-04-REV-MAJ01` and `FACTORY-CONVERGENCE-06-REM-04-REV-MIN01`.

The task is owned by schema-3 CLAIM comment `5740221969` on branch `planning/issue-1155`. It reconstructs the exact reviewed producer semantics from Issue #1151 head `52ad92145e757d7eb86a2e3b9bd94f789dafc82c` on a fresh branch rooted at `main@dd2a8418b820800ad96a44afed175b373b94a933`.

## Frozen authority and provenance

- active canonical binding: Issue #1147 terminal `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- source producer: Issue #1151 terminal `5739787607`, head `52ad92145e757d7eb86a2e3b9bd94f789dafc82c`, PR #1152
- source required review: Issue #1153 terminal `5740219045`, review head `af6deba4d56d5fb899beda4802aba240d3b7ec16`, PR #1154
- current main at finalization re-check: `f21f926cc271db191128fe3a735ca0ff9fa1f5d9`
- the only change from the task base to that current main is Issue #1153 review/handoff provenance; maintenance v1/v5 on main remain blobs `2256d10c22b27e9952072875f7fb9a14ef8e25cc` and `63c37ff752a1f10a7e00e0818b56463e7089459f`

## Work present

Only the two authorized maintenance files plus this handoff are changed.

### MAJ01 — malformed owner-terminal displacement

`tools/planning/frontier_maintenance_v5.py` now requires an intermediate owner terminal used to suppress STALE recovery to carry both `head_sha` and `work_sha` as present exact 40-hex values, in addition to the pre-existing kind/state/authority/generation/actor/lease checks.

Deterministic attacks cover missing head, missing work, malformed head, and malformed work. In every case the malformed pre-expiry terminal has zero displacement authority and a lawful exact-boundary STALE recovery can win.

### MIN01 — strict RFC3339 GitHub server time

`tools/planning/frontier_maintenance.py` now applies a strict RFC3339 lexical gate before `datetime.fromisoformat`. It accepts canonical Z, fractional seconds, numeric offsets, and RFC3339's case-insensitive `T`/`Z`; it rejects naive timestamps, space-separated ISO forms, basic ISO forms, and malformed values.

## Verification state

The exact repository bytes for all five maintenance layers were reconstructed from their GitHub Git blobs and independently re-hashed locally before execution.

Branch code blob identities at the pre-handoff code head:

- v1: `316e85d688b2a8a7f52657ad8cd1ce198d6e19e0`
- v2: `9c7f73a1de409fcfe22504dcdaf48a2f0dff5b6e`
- v3: `87cd1a424e5db22d3be3d081aa31b87733928e25`
- v4: `4a7a56ed96c3927da6481a9b3c4e53c7042d86ed`
- v5: `d43e198f83bea2ab6c498bba7b62e47a3b24c1eb`

Executed successfully on those exact bytes:

```text
python3 -m py_compile frontier_maintenance.py frontier_maintenance_v2.py frontier_maintenance_v3.py frontier_maintenance_v4.py frontier_maintenance_v5.py
python3 frontier_maintenance.py --self-test
python3 frontier_maintenance_v2.py --self-test
python3 frontier_maintenance_v3.py --self-test
python3 frontier_maintenance_v4.py --self-test
python3 frontier_maintenance_v5.py --self-test
```

All commands PASS. No GitHub Actions run is attached to the branch.

After this handoff commit establishes the final branch head, the code blobs must be re-fetched/re-hashed and the complete compile plus v1-v5 self-test suite must be re-run before publishing `STATUS(REVIEW_READY)`.

## Next required action

Open an exact-head draft PR and publish owner-authoritative `STATUS(REVIEW_READY)` only after final exact-head verification. Route exactly one fresh required degraded-independent review of Issue #1155 before any integration.

## Authority boundary

`NOT_CANONICAL`. This remediation grants no integration, verification-PASS, implementation-readiness, engine-selection, release, production, decision, or canonical authority. Any later integration remains separately authorized and squash-only.
