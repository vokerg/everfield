# Required Review — Old Works Presentation Fan-In (#1471)

## Review subject

- Producer: #1414 / `IMPLEMENTATION-INCREMENT-OLD-WORKS-PRESENTATION-01`
- Producer terminal: comment `5972486055`
- Frozen producer head: `69759e142d59ffe36326f8b07cd92118d556ee1c`
- Producer PR: #1468 (draft, exact head)
- Producer base: `849642087297f8b8c83e5bda927aa6ce9d5ef899`
- Review claim: #1471 comment `5972540614`
- Canonical binding: #1147 comment `5675066392`
- Canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`

This review treats the producer branch and all published component packets as read-only.

## Exact diff and packet identity

The producer diff contains exactly five authorized paths:

1. `.github/workflows/godot-first-playable-smoke.yml`
2. `docs/implementation/first-playable.md`
3. `docs/planning/handoffs/issue-1414.md`
4. `game/main.gd`
5. `game/smoke_test.gd`

Exact reviewed producer blobs:

- workflow: `2ea3f631d4ecbf2b19adaa26895b3201e54b2f0b`
- implementation doc: `53a689cc493703d52eb98045287e0f08c2d457b0`
- producer handoff: `4c60e2641d430d0aac78dd964cae206ba87be0bb`
- `game/main.gd`: `4ea6ab02de1fa8bfde2d976b0f3f551dc8f40b97`
- `game/smoke_test.gd`: `d67e5bcce5b86931d45082ab6af29214f692d852`

Shared files outside the authorized diff remain unchanged at the producer head:

- `game/main.tscn`: `02b943321c258bb807f9496c7a270221df112b31`
- `game/project.godot`: `9da4153ed378945ef5e9634e0e5cae48289845d8`

Consumed published packet identities also match exactly:

- Old Works presentation: `8e498156bb9a5413f53a84b14fc279c4be6c8f23`
- Commons Hearing presentation: `9682c47ee2c84ea42417651d0ca2e4f30ebf78b2`
- Commitment consequences presentation: `419688e17515bf5f67b383182c0b6330111ce4be`
- Movement/proximity smoke: `4c5bd980eecd47fcc620d72f4819e3dab687d059`
- Movement runner: `e913b8996052f6e21616d58b29cc132f2684eda5`

No published component source/test packet is rewritten by the fan-in.

## Independent runtime-evidence validation

Repository Actions evidence was independently re-read for exact producer head `69759e142d59ffe36326f8b07cd92118d556ee1c`:

- workflow run: `37146274187` — `success`
- job: `111270773311` / `smoke` — `success`
- Actions checkout log explicitly fetches and checks out `69759e142d59ffe36326f8b07cd92118d556ee1c`
- reviewed Godot artifact: `4.7.1-stable`
- reviewed ZIP SHA-256: `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`
- checkout log records `godot.zip: OK`
- engine banner: `Godot Engine v4.7.1.stable.official.a13da4feb`
- state-machine sentinel: `EVERFIELD_SMOKE_PASS`
- movement/proximity sentinel: `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`
- evidence artifact: `11282870193`
- evidence artifact digest: `sha256:a83237df22cf5e705db17016861cfaf32486b3c68d2ff2a2bf200633ba62a07e`

The workflow retains exact reviewed-artifact lock/hash verification, runs both smoke surfaces with `set -euo pipefail`, and uploads run identity plus implementation hashes.

## Acceptance review

1. **Old Works presentation consumption — PASS.** `game/main.gd` preloads the published Old Works component, derives Archive Ledger / Material Trace / deferral text from its reviewed station/text APIs, and the exact smoke asserts reviewed non-resolution prose.

2. **Private provenance boundary — PASS.** The public-record presentation consumes only reviewed public text; the smoke explicitly rejects exposure of `anwen_contested_record_provenance_gap`. The published component contract also records `public_record_exposes_private_information: false`.

3. **Material Trace remains non-discriminating — PASS.** The displayed reviewed trace text explicitly says it does not identify a single fragmentation cause. No fan-in logic converts material difference, count, or custody into truth.

4. **Commons Hearing integration — PASS.** The fan-in displays reviewed Maelin Sor / Selka Vey opening and route beats from the published component. Existing investigation and commitment gates remain the state-transition authority.

5. **Consequence presentation — PASS.** Repair-pilot, records-first, and explicit public deferral consume the published consequence component. Selection/completion presentation is separate from state mutation.

6. **Deferral/nonconsent/reopen semantics — PASS.** Choosing `defer` clears commitment, closes the hearing, appends `PUBLIC_COMMITMENT_DEFERRED`, and presents reviewed nonconsent text. A later commitment requires a fresh `commons_hearing` interaction; prior history is retained and asserted by smoke.

7. **Mystery/truth boundary — PASS.** `MYS:FRAGMENTATION-CAUSE` remains represented as `UNKNOWN_BY_DESIGN` throughout reset, investigation, commitment, and completion. Both executable committed routes assert the invariant. No presentation component grants truth or canonical authority.

8. **Published components remain inert/read-only — PASS.** Exact blob identity matches the separately published reviewed packets. The fan-in calls presentation lookup APIs; it does not modify component sources or assign them gameplay-state authority.

9. **Locked-Godot runtime evidence — PASS.** The exact producer head, artifact lock/hash, engine identity, state-machine smoke, and movement/proximity smoke were independently validated from the Actions run/job/log/artifact records above.

10. **Diff hygiene — PASS.** Exactly five authorized fan-in paths changed. `game/main.tscn`, `game/project.godot`, and all consumed component/test packets are unchanged.

11. **Executable route and fail-closed coverage — PASS.** The state-machine smoke completes repair-pilot and the explicit-truth-deferral → public-commitment-deferral → hearing-reopen → records-first route without fabricating trace evidence. Unknown station/commitment guards remain fail closed; the separately executed movement smoke covers out-of-range interaction and real input-driven proximity behavior.

12. **CI wiring — PASS.** The workflow verifies the repository lock and SHA-256, imports/runs under Godot 4.7.1, executes state-machine plus movement/proximity coverage in the same job, and captures immutable evidence.

## Findings

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- informational: 1

Informational: this is still a bounded noncanonical implementation increment. Successful executable review does not establish production/release readiness, empirical accessibility certification, legal/provider authority, final canon, or historical truth resolution.

## Disposition

`CLEAN_FOR_OLD_WORKS_PRESENTATION_INCREMENT_INTEGRATION`

This disposition is limited to the exact frozen Producer #1414 head and establishes only the review gate required for a separately claimed, freshly re-derived squash integration. It is not integration authority by itself.
