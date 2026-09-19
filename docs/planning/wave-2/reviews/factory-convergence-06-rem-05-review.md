# Required Review — Factory convergence terminal-validity/RFC3339 remediation #1155

## Disposition

**PASS_FOR_SEPARATE_AUTHORIZED_SQUASH_INTEGRATION_WITH_POST_PUBLICATION_WORKFLOW_ACCEPTANCE**

Findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

Trust mode: `DEGRADED_SINGLE_AGENT`. Review actor `everfield-agent-review1157-gpt56sol-20260919-01` is distinct from producer actor `everfield-agent-rem1155-gpt56sol-20260919-01`. The producer branch and PR were not modified.

## Frozen reviewed packet

- producer Issue #1155 terminal: `5740305775`
- producer head/work: `868e13975716b8878d482c5a0978bd9be1f45212`
- producer PR: #1156, open draft, clean/mergeable at the final pre-artifact fence
- canonical binding: Issue #1147 terminal `5675066392`
- canonical Planning Program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- review base/current main at claim and final pre-artifact fence: `f21f926cc271db191128fe3a735ca0ff9fa1f5d9`
- v1 blob: `316e85d688b2a8a7f52657ad8cd1ce198d6e19e0`
- v2 blob: `9c7f73a1de409fcfe22504dcdaf48a2f0dff5b6e`
- v3 blob: `87cd1a424e5db22d3be3d081aa31b87733928e25`
- v4 blob: `4a7a56ed96c3927da6481a9b3c4e53c7042d86ed`
- v5 blob: `d43e198f83bea2ab6c498bba7b62e47a3b24c1eb`
- producer handoff blob: `f5d09a761500e9dfe7d5b685bd78db53c60fdabc`

The v2-v4 blobs are byte-identical to the frozen #1151 producer packet.

## Independent exact-byte execution

The five maintenance files were reconstructed from the exact frozen producer ref, independently Git-blob-hashed, and every hash matched the frozen packet above. On those exact bytes:

- `python3 -m py_compile` across v1-v5: PASS
- v1 `--self-test`: PASS
- v2 `--self-test`: PASS
- v3 `--self-test`: PASS
- v4 `--self-test`: PASS
- v5 `--self-test`: PASS

All subprocesses returned exit code 0 and emitted their expected PASS result.

## Routed finding attacks

### FACTORY-CONVERGENCE-06-REM-04-REV-MAJ01

Independent reviewer-side reproductions, separate from the producer self-test driver, constructed an owner generation, a pre-expiry owner terminal, and an exact-boundary lawful STALE recovery. Results:

- missing terminal `head_sha`: malformed terminal has zero displacement authority; recovery wins
- missing terminal `work_sha`: malformed terminal has zero displacement authority; recovery wins
- non-40-hex terminal `head_sha`: malformed terminal has zero displacement authority; recovery wins
- non-40-hex terminal `work_sha`: malformed terminal has zero displacement authority; recovery wins
- clean-side control with a structurally valid unexpired owner terminal: later STALE recovery is displaced

The implementation now requires the relevant intermediate terminal to satisfy owner/kind/state/generation/actor/lease predicates plus present exact 40-hex head and work identities before it can suppress STALE recovery.

### FACTORY-CONVERGENCE-06-REM-04-REV-MIN01

Independent direct calls to the exact frozen v1 parser established:

Accepted:
- canonical `Z`
- fractional seconds
- numeric timezone offsets
- RFC3339 case-insensitive `T` / `Z`

Rejected fail-closed:
- space-separated ISO form
- basic ISO form
- timezone-naive form
- absent value
- malformed value

The parser lexically gates RFC3339 before `datetime.fromisoformat`.

## Regression and scope checks

The exact v1-v5 suite re-proved the canonical 21,600-second lease boundary, valid PROGRESS renewal, three-EVIDENCE cap and HEAD_ADVANCE reset, exact 600-second ORPHAN maturity and later-owner invalidation, winning CLAIM/RESUME/RECOVER/HANDOFF structure, stale prior-owner rejection, exact-generation dedupe, explicit-successor routing, stable terminal wrappers, `NONE` / `NONE_*` handling, v4 semantic composition, dispatch/recursive suppression, and typed rate-limit deferral.

PR #1156 changes exactly:
1. `tools/planning/frontier_maintenance.py`;
2. `tools/planning/frontier_maintenance_v5.py`;
3. `docs/planning/handoffs/issue-1155.md`.

No authority inflation was found. The producer handoff remains `NOT_CANONICAL` and explicitly grants no integration, verification-PASS, implementation-readiness, engine-selection, release, production, decision, or canonical authority.

## Required route

This review is clean for a **separate authorized squash integration** of the exact reviewed producer packet under repository authority. Review provenance publication and producer publication remain distinct integration episodes. After producer publication, the required exact-new-main workflow acceptance must still be observed and recorded; this review does not pre-grant that acceptance.

## Authority boundary

`NOT_CANONICAL` required-review provenance only. The review itself does not integrate the producer and grants no verification-PASS, implementation-readiness, engine-selection, release, production, decision, or canonical authority.
