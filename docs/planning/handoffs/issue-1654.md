# Issue #1654 — independent exact-head Godot verification of corrected route-history #1651

## Role / task and current outcome

**MANDATORY distinct read-only scoped verifier** `IMPLEMENTATION-VERIFY-ROUTE-HISTORY-1651-01`, independent of source remediation #1651, original producer #1627, previous required negative reviewer #1643, previous obsolete-source verifier #1635. Winning first-valid unedited schema-3 CLAIM **#6108938440**, actor `frontier-distinct-verify-route-history-1654-gpt6-20261011-1418-cph-01`. Branch `planning/issue-1654` was created from exact `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d` following immediate post-CLAIM first-winner, unedited and no-competitor recheck.

**State: VERIFICATION_IN_PROGRESS, NOT PASS UNTIL REAL FINAL-HEAD HOSTED RUN / JOB / ARTIFACT EVIDENCE IS INSPECTED.** The GitHub Actions workflow is authored independently but its existence is not executable proof. If a genuine source error appears, publish negative proof and hand off to source #1651; never invent a PASS.

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

1. Open `planning/issue-1654` **DRAFT verifier-only PR** against main, ensure only the two exclusive file paths. Record exact final PR head; recheck live main/canonical and source PR exact HEAD.
2. Inspect genuine FINAL-verifier-PR-HEAD event=`pull_request` run and verify job, source checkout identity, exact four Git source blobs, exact Godot ZIP SHA and binary version, isolated sentinel/existing regression logs, artifact ID/digest and immutable manifest.
3. If PASS with real run evidence: update this handoff, commit final evidence on verifier branch and repeat CI for final verifier HEAD (if handoff advances), inspect again; only then post unedited in-lease schema-3 `VERIFICATION_STATUS(DONE,result=PASS)` referencing true run/job/artifact and route source #1651 valid HANDOFF continuation for its own evidence-driven REVIEW_READY, followed by a **new genuinely independent** required code/security review. If FAIL: publish actual failure evidence and owner `STATUS(HANDOFF_READY)` with precise source correction route; no fake PASS.
4. Verifier-only PR remains OPEN/DRAFT/UNMERGED; NEVER modify source #1651, prior #1627, previous reviews/verifiers, game providers, shared CI or main from verifier role. No source integration/canon/gameplay/production authority. Any later source integration needs separate owner authorized **squash-only NONCANONICAL** gates.

No global gate is asserted against parallel public-text #1626/#1655 or factory parser remediation.
