# Required Review — Factory convergence recovery-lease remediation #1151

## Disposition

**CHANGES_NEEDED**

Trust mode: `DEGRADED_SINGLE_AGENT`. Review actor `everfield-agent-review1153-gpt56sol-20260919-01` is distinct from producer actor `everfield-agent-recover1151-gpt56sol-20260919-01`. The producer branch was not edited.

Reviewed immutable packet:
- producer Issue #1151 terminal `5739787607`;
- producer head/work `52ad92145e757d7eb86a2e3b9bd94f789dafc82c`;
- draft PR #1152;
- v1 blob `37aa2162f9c0d95ad8cbed015cf9ec8aa3b0c9c0`;
- v2 blob `9c7f73a1de409fcfe22504dcdaf48a2f0dff5b6e`;
- v3 blob `87cd1a424e5db22d3be3d081aa31b87733928e25`;
- v4 blob `4a7a56ed96c3927da6481a9b3c4e53c7042d86ed`;
- v5 blob `3a0eae39a9b99a34a5b45f4f0af535b8d4e002be`;
- handoff blob `0716732f5764b5e2819120a01699f31d5b4b43d5`.

Current-main composition at review: Planning Program blob remains `fd4cf1119c3f86acc3af620024eea72235e81ce4`; v2-v4 are byte-identical to the producer packet, while producer v1/v5 are bounded modifications of unchanged current-main maintenance blobs.

## Independent execution evidence

The producer v1-v5 bytes were independently hash-checked against the frozen Git blobs. The following all passed:
- `python3 -m py_compile` across v1-v5;
- v1 `--self-test`;
- v2 `--self-test`;
- v3 `--self-test`;
- v4 `--self-test`;
- v5 `--self-test`;
- exact 21,600-second lease boundary attack;
- valid PROGRESS renewal attack;
- three-consecutive-EVIDENCE cap attack;
- HEAD_ADVANCE reset attack;
- exact 600-second ORPHAN maturity attack;
- valid pre-expiry owner-terminal displacement attack;
- current-main v2-v4 composition and exact producer PR path scope.

PR #1152 changes exactly:
1. `tools/planning/frontier_maintenance.py`;
2. `tools/planning/frontier_maintenance_v5.py`;
3. `docs/planning/handoffs/issue-1151.md`.

## Findings

### FACTORY-CONVERGENCE-06-REM-04-REV-MAJ01 — malformed terminal can suppress lawful STALE recovery

Severity: **MAJOR**.

The new v5 `valid_owner_terminal()` helper treats an earlier owner terminal as displacement based on terminal kind/state, owner generation, actor, and temporal liveness, but it does not require the terminal to satisfy the structural terminal checks already required by `v3.routable_terminal_from_comments()`: a present exact 40-hex `head_sha` and `work_sha`.

Independent reproduction:
- owner A claims at `12:00:00Z`;
- at `17:59:59Z`, a `STATUS(DONE)` for A is written with correct actor/generation/authority but **no head/work SHA**;
- at the exact lease boundary, B issues a structurally valid STALE intent and then RECOVER;
- B publishes a valid terminal.

Without the malformed A terminal, `terminal_owner_generation_is_current(...)` correctly accepts B. With the malformed A terminal present, the same function rejects B because the malformed record is incorrectly treated as authoritative displacement. The same failure reproduces with a non-40-hex terminal head.

This can strand an expired generation behind a malformed terminal record that should have zero authority effect. Required remediation: intermediate owner-terminal displacement must require the same relevant structural terminal validity as routable terminal recognition, including present exact 40-hex head/work identities, before it can block STALE recovery.

### FACTORY-CONVERGENCE-06-REM-04-REV-MIN01 — timestamp parser is broader than required RFC3339 grammar

Severity: **correction-requiring MINOR**.

`parse_github_server_time()` delegates to `datetime.fromisoformat()` after normalizing a trailing `Z`. That parser accepts ISO-8601 spellings outside the required RFC3339 grammar, including:
- `2026-09-15 12:00:00+00:00` (space separator);
- `20260915T120000+00:00` (basic form).

Both are accepted by the producer helper even though the contract requires GitHub-server RFC3339 instants and malformed required time to fail closed. Timezone-naive input is correctly rejected.

GitHub normally emits canonical RFC3339, so this is narrower than MAJ01, but the helper's authority parser does not implement the declared fail-closed grammar. Required remediation: enforce a strict RFC3339 lexical form before datetime normalization/parsing, while preserving valid fractional seconds and timezone offsets.

## Non-findings retained

The review found no defect in:
- exact lease expiry semantics;
- renewal moving the STALE boundary;
- EVIDENCE cap and HEAD_ADVANCE reset;
- exact ORPHAN maturity and later-owner invalidation;
- first-valid CLAIM / winning RESUME_INTENT / first valid grant structural composition;
- HANDOFF linkage;
- losing duplicate CLAIM/RECOVER rejection;
- stale prior-owner terminal rejection;
- exact-generation dedupe;
- explicit-successor routing;
- stable terminal-wrapper handling;
- `NONE` / `NONE_*` no-route behavior;
- v4 semantic composition;
- dispatch/recursive-suppression shape;
- typed GitHub rate-limit deferral;
- producer path ownership or authority boundaries.

## Required route

One bounded remediation must close exactly `FACTORY-CONVERGENCE-06-REM-04-REV-MAJ01` and `FACTORY-CONVERGENCE-06-REM-04-REV-MIN01`, preserve all non-findings, rerun the full exact-byte v1-v5 suite plus the two new attacks, and route a fresh required degraded-independent review.

No producer integration is authorized by this review.
