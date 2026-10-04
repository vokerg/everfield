# Issue #1487 Handoff — Exact Diagnostic Runtime Evidence

## Status
Verification-only execution packet prepared for repository-native Godot 4.7.1 runtime. **No PASS may be claimed before the final PR-head run succeeds**, observes the exact sentinel, and retains immutable run/job/log/artifact evidence.

## Canonical authority and issue chain
- mission: `IMPLEMENTATION-DEMAND-DIAGNOSTICS-01-REM-03`
- claim: Issue #1487 comment `5977067490`
- owner branch: `planning/issue-1487`
- execution base main: `16cceaf5a8d861daf8422a26024a00fb668a453b`
- active canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- source required review: Issue #1475 terminal `5972609153` / `CHANGES_NEEDED`
- source bounded reconciliation: Issue #1481 terminal `5972740200`
- source remediation draft PR: #1486
- ordinary regression `37148133947` / job `111276184554` passed but is **not** the isolated smoke.

## Exact frozen remediation packet
The verification workflow checks out **only** the frozen source head `07ccfaf655acc103436490edf703cb4b194b87f0` (not the workflow PR's own head) and hashes:
- `game/components/diagnostics/diagnostic_catalog.gd`: `f37d93783dd9d206ba6d7a4bd050c9ff8c3ad1b3`
- `game/components/diagnostics/diagnostic_catalog_smoke.gd`: `dd73c221d6764d734f630c0bef389c22eaa0d133`
- `docs/planning/handoffs/issue-1481.md`: `d2030d69ac0edc711cd3ea761ad7d28117c0c473`
- `game/project.godot`: `9da4153ed378945ef5e9634e0e5cae48289845d8`
- `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json`: `4a88990ae24768eb4f83a8a1311e2a830834649f`

## Verification-only changes
- `.github/workflows/verify-diagnostic-contract-1487.yml`, blob `ec7f2529772adb42f020a28ced7c67554ceb6c8b`
- `docs/planning/handoffs/issue-1487.md` (this file)

No frozen remediation/component, main gameplay, sibling component, or other workflow bytes are modified. This temporary PR-side workflow is **non-integrable** without separate authority.

## Required locked runtime
- repository-reviewed Godot artifact: `4.7.1-stable`
- zip SHA-256: `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`
- runtime command: `godot --headless --path game --script res://components/diagnostics/diagnostic_catalog_smoke.gd`
- required process exit: `0`
- exact success sentinel: `EVERFIELD_DIAGNOSTIC_CONTRACT_SMOKE_PASS`
- retained evidence: `issue-1487-evidence/engine.txt`, `diagnostic-contract-smoke.log`, `run-identity.txt` and GitHub Actions artifact containing all three.

## Remaining checks and forward route
1. Open an exact-head draft PR so the path-scoped `pull_request` workflow executes; check run/job **conclusion**, frozen source identity, locked engine banner/hash and sentinel.
2. Confirm immutable evidence artifact/run identity, workflow PR head and manifest, including a final run if this handoff changes.
3. If runtime PASS: terminalize `VERIFICATION_STATUS(DONE)` and route a **fresh required review** of the frozen #1481 remediation packet.
4. If runtime FAIL: preserve failure evidence and route a smallest code-remediation successor. Infrastructure failures must be repaired in verification-only scope and rerun.

No component publication, integration, gameplay, persistence/save-load, truth-resolution, canonicality, accessibility certification, production/release or legal/provider authority is granted.
