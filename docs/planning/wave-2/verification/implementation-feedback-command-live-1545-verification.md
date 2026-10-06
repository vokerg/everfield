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

## Results and disposition (pending exact independent run)

- Producer-run `37351790608` / job `111904164303` / ZIP `11362154579` with published SHA `c649e09288f021f9d5af2bc7776e9b77d33de1146b54c294b0c8457c1d0ecf42`: **inherited evidence only**, not independent PASS.
- Fresh independent run/job/attempt, downloaded complete artifact checksum, per-suite pass markers and adversarial outcome: **PENDING**.
- Finding counts/disposition and exact terminal verifier branch HEAD: **PENDING**.
- Any blocking failure routes bounded producer remediation/reverification. A full independent PASS requires an observed successful source-HEAD-locked executable and genuine retained artifact; never infer one from this document, workflow existence or PR mergeability.

No source integration, required full independent *code review*, canonicality, private Anwen truth, consent reinterpretation, accessibility, engine readiness, release, production or legal authority is conferred.
