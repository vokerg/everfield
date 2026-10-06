# Independent live Godot fan-in verification — Issue #1575

Status: **IN PROGRESS; NO VERIFICATION PASS OR INTEGRATION AUTHORITY**.

## Scope and immutable source

Required distinct verification of Issue #1545 terminal `STATUS(REVIEW_READY)` comment `6008457546`, draft source PR #1568 frozen HEAD `1de1155429bfa657dd6e60c4f5abc969fabd86d5`. Verifier actor `frontier-independent-liveverify-1575-gpt56sol-20261006-0529-01` is not original producer `frontier-live-fanin-1545-gpt56sol-20261005-1946-01` or recovery author `frontier-recover-live-fanin-1545-gpt56sol-20261006-01`. Isolation is `DEGRADED_SINGLE_AGENT_FRESH_INDEPENDENT_VERIFICATION_EPISODE`; distinguish independent execution and probe from producer CI. Own branch `planning/issue-1575` based on `main@e51703de82b9df3f5e676663d3a04fdc678bd5c6`. Canonical Issue #1147 binding `5675066392`, blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af` remain unchanged.

Frozen six source path/blob identities:

- `game/main.gd` `921ff7a1ce28ed4df4a67a7645752d7b441603f7`
- `game/smoke_test.gd` `69d58e13455106cdff2b11bca93628d956855f69`
- `game/tests/movement_interaction_smoke.gd` `b1c03b6e387b3aeeaea3302bbc2766ced567aee0`
- `.github/workflows/godot-first-playable-smoke.yml` `a41d9ec6705959e8702557fcfc10343d909749dd`
- `docs/implementation/first-playable.md` `6f6eecd3702289d7a3f3d19c10ca98f0a224ba73`
- `docs/planning/handoffs/issue-1545.md` `de234f7c511e7fd6d6fdeac5297bf0a7126f3806`.

External unchanged frozen scene `02b943321c258bb807f9496c7a270221df112b31`, source policies `0f3b32c254f00f27338202fa7f0dd53c6f2efcf8`, `d5422813a2e2bd938d9776c3f2cd12a058a9ac10`, associated smoke blobs `90c3608288426d29fefec8e7248074ab2ca4b969`, `b9ff3fdfe9feea28c980e624324f6a35d45254fd`. Upstream reviewed, independently verifier-locked component sources are separately published via source integrations #1558 / `5999902986`, #1561 / `5999904540`. These references do **not** independently certify the new scene fan-in.

## Independent method

Verifier-only nonintegrable workflow `.github/workflows/godot-independent-live-1575.yml` separately checks out the verifier's **exact review PR head** and **original frozen source head** into separate directories. It performs exact Git blob checks, downloads independently the pinned Godot `4.7.1-stable` binary with SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`, runs the ten full Godot suites and an eleventh **newly authored adversarial scene probe** `implementation-feedback-command-live-1545-probe.gd` copied only into the ephemeral checkout. Source branch, scene and policy files are never mutated in GitHub.

Adversarial probe explicitly tests real visible `Objective`, radius 88 versus 89, physical WASD near/far/near and exact public hint, E/1/2/3/R through Godot event dispatch, release/echo/physical-only/unrecognized rejection, premature hearing gate, explicit nonconsent/deferral, both commitments, outcome, reset and `UNKNOWN_BY_DESIGN`. Independent CI fails closed on failed sentinels, unexpected diagnostic push-errors, parser/assertion errors or provenance mismatches. It archives all 11 log files, exact runner/source identity, hashes, error classification and a summary.

## Historical Issue #1448 check scope

GitHub run `37351790676`, job `111904164099`, at frozen `1de1155...` failed **before Godot execution**. Its exact historical workflow still asserts `game/tests/movement_interaction_smoke.gd` blob `4c5bd980eecd47fcc620d72f4819e3dab687d059` and controller blob `b96659a1cf461a96934666293aecaa565e68579b`, whereas this authorized new source intentionally changes both. Its historical testability rejection of any `player.position =` line also conflicts with the new input-driven real-scene boundary fixtures. GitHub `main` is not branch-protected in the fetched branch metadata, but separate source integration and required-review authority remain mandatory: the failed check is not silently green, is not a runtime defect report, and a future integrator must independently recheck actual current required checks/compatibility.

## Verified exact independent run and adversarial findings

**Full independent executable PASS at the tested immutable verifier HEAD `79c7058254db5b76fcad389f7f7cd370b7cdef8b` (run `37409479958`), subject to refreshing the evidence after this report-only HEAD advancement; final new-HEAD CI result is separately recorded in the terminal owner record.**

- Run `37409479958`, event `pull_request`, attempt `1`, independent `independently-verify-source` job `112094446512`: `completed/success`. Its exact immutable original source checkout `1de1155429bfa657dd6e60c4f5abc969fabd86d5` differs from verifier PR HEAD. Git source identity checks and pinned Godot binary ZIP SHA256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` succeeded, actual engine banner `4.7.1.stable.official.a13da4feb`.
- GitHub Actions archived original ZIP **artifact `11389017029`**, name `independent-live-1575-37409479958-1`, **21,417 bytes**, GitHub-reported and independently downloaded/rehashed exact **SHA256 `62ef5e1eb002556908e5f76d0029cada7995aa71015125e2ec3bb4373050f878`**. Actual ZIP contents inspected (not inferred): **15 entries**, 11 complete logs (ten original + independent), `run-identity.txt`, `source.sha256`, `verifier-summary.txt`, `engine-errors.txt`. `run-identity.txt` explicitly repeats source HEAD, verifier HEAD, run, attempt and reviewed engine ZIP hash.
- Independent inspected suite lines: **10 distinct full-line expected PASS sentinels**. Action command 44 assertions, diagnostic contract 151, HUD objective 79, interaction-feedback 28, movement-interaction 83, playable presentation 37, session state 54, original state-machine 146, station world 73, traversal policy 44: **739 independent rerun suite assertion passes, zero failed assertions**. Eleven-suite verifier-only log contains **21 separately implemented live adversarial assertion passes**, exact `EVERFIELD_INDEPENDENT_LIVE_1575_PASS checks=21`. Total assertion passes **760**.
- **0 `[FAIL]`, 0 script/parser errors, 0 `Assertion failed`**. Precisely **two** actual Godot `ERROR: [EF-INTERACT-UNKNOWN] Unknown station: unknown_station` messages (one original state-machine negative and one movement negative) occur as expected; full archived `engine-errors.txt` confirms both. No unexplained error was waived. All required no-private-truth, explicit deferral nonconsent, W/A/S/D radius-bound real Label, actual E/1/2/3/R, physical-only/echo/release and early-choice gate tests are present and passed.
- Original frozen producer PR #1568 and source run remain unmodified. The inherited Issue #1448 failed historical old-blob equality-check workflow is disclosed above; it cannot serve as new runtime validation or proof of failure of this authorized new source. No current protected-branch integration gate was asserted. Current verified clean source here remains **noncanonical** and **unintegrated**.

**Observed independent-run disposition:** `PASS_FOR_REQUIRED_DISTINCT_FULL_SOURCE_REVIEW`; **zero blockers, zero majors, zero correction-requiring minors in the requested runtime scope**. The reviewer must independently audit actual controller/test/workflow semantics, not convert this scoped verification into review or squash permission. This PR is temporary verification provenance and must remain draft/unmerged. A valid current-owner terminal requires a successful re-run on the report's final HEAD and exact final artifact identities; any later source/branch movement requires new evidence.
