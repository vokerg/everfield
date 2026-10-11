# Issue #1654 — independent exact-head Godot verification of corrected route-history #1651

## Role / task and current outcome

**MANDATORY distinct read-only scoped verifier** `IMPLEMENTATION-VERIFY-ROUTE-HISTORY-1651-01`, independent of source remediation #1651, original producer #1627, previous required negative reviewer #1643, previous obsolete-source verifier #1635. Winning first-valid unedited schema-3 CLAIM **#6108938440**, actor `frontier-distinct-verify-route-history-1654-gpt6-20261011-1418-cph-01`. Branch `planning/issue-1654` was created from exact `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d` following immediate post-CLAIM first-winner, unedited and no-competitor recheck.

**State: FIRST REAL HOSTED EXACT-PR-HEAD EXECUTABLE PASS CONFIRMED, FINAL PR HEAD RERUN REQUIRED AFTER THIS EVIDENCE HANDOFF COMMIT.** A genuine read-only GitHub Actions pull_request workflow executed at prior verifier PR #1657 HEAD `72ae9f76f5d876da123e95d8b4e6a176ec1791b7`, run #38139013788 attempt 1 SUCCESS, job #114468796500 SUCCESS. Isolated locked Godot 4.7.1 output exactly one full-line `EVERFIELD_ROUTE_HISTORY_VIEW_PASS checks=249`, zero source suite ERROR/FAIL/parse failures, existing first playable and movement-interaction regressions PASS. Exact source HEAD, all four immutable blobs, locked official ZIP SHA and binary version checks succeeded. GitHub artifact #11701488307, `route-history-1651-38139013788-1`, size 12,902 bytes, immutable archive digest `sha256:8d60adf1ed31c114039bf2d0703869a435c22e2c423f812b813ba94a1ff1497f`, stores identity, exact raw logs, source/binary hashes and SHA256 manifest. **As this handoff modifies the PR HEAD, rerun and independently inspect the new final PR HEAD before terminalizing; first success does not certify a later head.**

## Frozen source and authority

- Source remediation #1651 first winning CLAIM #6107767990, valid HANDOFF_READY #6107844191. Open DRAFT source PR #1653 exact HEAD `e0bbde9daba1855f0b054fcc4bf023be3fb203cb`, base exact current main; **no source integration**.
- Exactly four source file identities independently checked through GitHub PR-files API:
  1. `game/components/route_history_view/route_history_view.gd` blob `8f32a8e925d8fb0765e91ef102ad0827a0b88958`;
  2. `game/tests/route_history_view/route_history_view_smoke.gd` blob `298916bbdd839e2094c4e2695e305f1142bb3e30`;
  3. `docs/planning/handoffs/issue-1627.md` blob `75b37ba2c7d38f9cf3371590ac476d80af116448`;
  4. `docs/planning/handoffs/issue-1651.md` blob `f7b1a24086672664ccbcaf39ed2fa2dacb806783`.
- Original source #1627 PR #1630 HEAD `ba8325232de970400352782e77506e5b1dfba91b` and verifier #1635 terminal #6107400681 only verified **obsolete original** source. Negative code review #1643 terminal #6107756342 demanded corrective source #1651. Its authored correction never received locked Godot execution; our new test must run exact corrected SHA, not inherit old PASS.
- Canonical program Issue #1147 terminal #5675066392, blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`; activation `87c85cecfa9a2ffa464c4b36816a138bf41441af` ancestor of main. This grants only canonical planning process authority, not implementation-readiness, engine selection, truth/consent or release.

## Exclusive changes / genuine hosted verifier specification

Branch `planning/issue-1654`, exact main-based, changes ONLY:
- `.github/workflows/verify-route-history-1651.yml` (new locked verifier, initial immutable blob `057e6c9d66848b3ea6c2495ed0e495cfc9026da8`);
- `docs/planning/handoffs/issue-1654.md` (this reconstructable handoff).

Workflow `pull_request` from verifier-only draft PR to main with `permissions: contents: read`, `ubuntu-24.04`, `actions/checkout` pinned immutable SHA, source checkout strictly `e0bbde9...`, validate exact all four Git blobs, archive reviewed provider/scene file tree identity. Engine lock file `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` blob `4a88990ae24768eb4f83a8a1311e2a830834649f`: source official Godot 4.7.1-stable Linux ZIP URL, SHA256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`; executable `4.7.1.stable.official.a13da4feb`. Download, SHA256 check before run, fail closed on mismatch.

Execute locked `godot --headless --path game --script res://tests/route_history_view/route_history_view_smoke.gd`; require actual exit=0, exactly one complete line `EVERFIELD_ROUTE_HISTORY_VIEW_PASS checks=N` with integer N>0, no `[EVERFIELD][ROUTE-HISTORY][FAIL]`, `Parse Error`, `SCRIPT ERROR` or `Assertion failed`. Also run existing `tools/implementation/run_godot_smoke.sh` and `run_godot_movement_smoke.sh` with same locked GODOT_BIN and reject failure markers. Archive raw logs, actual source/runner/verifier HEAD identities, ZIP and binary hashes/version, per-run SHA256 manifest; pin artifact upload action and preserve evidence on failure.

## Required remaining actions

1. Verifier-only draft PR #1657 to main exists with exactly two authorized changed paths. Source #1651 PR #1653 remains frozen OPEN/DRAFT and unmerged. Original successful run #38139013788 proves corrected source runtime behavior at original verifier HEAD but must not be reused as a success for any later verifier PR HEAD.
2. Inspect the genuine **final verifier-only PR HEAD** event=`pull_request` run and verify its job logs and GitHub artifact id/digest, full 249-check sentinel and two regressions, checked out source SHA and exact four blobs, Godot lock and version, artifact identity and immutable SHA manifest. Record exact final result and immutable run IDs in schema-3 terminal comment; avoid editing this handoff again after the final run.
3. With genuine PASS publish in-lease independent `VERIFICATION_STATUS(DONE,result=PASS)`, route back to source #1651 valid HANDOFF continuation for its owner REVIEW_READY and a **new genuinely independent** required security/behavior/code review. If new-head CI FAIL, record genuine negative evidence and source handoff; no fake PASS.
4. Verifier-only PR stays OPEN/DRAFT/UNMERGED; never modify source #1651, prior #1627, previous reviews/verifiers, game providers, shared CI or main from verifier role. Any later source integration requires separately owner-authorized **squash-only NONCANONICAL** gates.

No global gate is asserted against parallel public-text #1626/#1655 or factory parser remediation.
