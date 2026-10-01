# Required review — bounded Godot first playable

**Review issue:** #1371  
**Mission:** `W2-GODOT-FIRST-PLAYABLE-BOOTSTRAP-01-REV-01`  
**Producer:** #1343 / terminal comment `5935515528`  
**Producer recovery ownership:** comment `5935484769`  
**Producer PR:** #1370  
**Exact producer head:** `d8796c07978ff6b91fb1b116ed26b9463f7de551`  
**Exact producer work SHA:** `81611d19b1ec3f5c4bcc3506ecc35945e4ede869`  
**Review ownership:** comment `5935524721`  
**Reviewer:** `frontier-drain-review-godot-first-playable-1371-gpt56sol-20261001-01`  
**Independence mode:** `DEGRADED_SINGLE_AGENT`  
**Disposition:** `CLEAN_FOR_BOUNDED_FIRST_PLAYABLE_INTEGRATION_REVIEW_GATE`

## Frozen identity and scope

This review judges only the exact frozen producer packet at PR #1370 head
`d8796c07978ff6b91fb1b116ed26b9463f7de551`. The producer branch was treated
as read-only.

Changed paths are exactly:

1. `.github/workflows/godot-first-playable-smoke.yml`
2. `docs/implementation/first-playable.md`
3. `docs/planning/handoffs/issue-1343.md`
4. `game/main.gd`
5. `game/main.tscn`
6. `game/project.godot`
7. `game/smoke_test.gd`
8. `tools/implementation/run_godot_smoke.sh`

The executable implementation blobs frozen for review are:

- `game/project.godot` — `9da4153ed378945ef5e9634e0e5cae48289845d8`
- `game/main.tscn` — `02b943321c258bb807f9496c7a270221df112b31`
- `game/main.gd` — `b96659a1cf461a96934666293aecaa565e68579b`
- `game/smoke_test.gd` — `38436acc78e62145952462d76bf158ee4748ae59`
- `tools/implementation/run_godot_smoke.sh` — `dab9ef4e7affde07645320071819a4dc0496fddb`

The selected-engine lock consumed by CI is
`docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` blob
`4a88990ae24768eb4f83a8a1311e2a830834649f`.

## Exact selected-engine evidence

Final-head workflow run `36890264547` is bound to branch
`planning/issue-1343` at exact head
`d8796c07978ff6b91fb1b116ed26b9463f7de551`.

The run completed successfully and produced retained artifact:

- artifact id: `11175524561`
- artifact name: `godot-first-playable-36890264547-1`
- artifact digest:
  `sha256:07d863cf1d94e8429ec71d3e8a65ff8b3381b1939c8dc0c141af730be3d45d23`

The workflow resolves the repository lock entry
`godot_4.7.1_linux_x86_64_zip`, requires version `4.7.1-stable`, downloads
the exact locked URL, and verifies SHA-256
`c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`.
The job log records `godot.zip: OK` and runtime
`4.7.1.stable.official.a13da4feb`.

The exact-head smoke log records PASS for every asserted route and terminates
with `EVERFIELD_SMOKE_PASS`.

## Main/canonical compatibility

Review claim base and review branch base are
`main@32a93df5e6f70771a28b673e1777c4c0aa223b4e`.

The producer and current main diverge from common ancestor
`3ac8ddd9468e261cea8d54c3afb9ac9dcf437251`, with ten commits on each side.
Current-main movement changes planning/readiness/content provenance paths and
`.github/workflows/planning-frontier-maintenance.yml`; none overlaps the
eight producer paths above.

PR #1370 remains open, draft, and GitHub reports it mergeable at review time.
That is compatibility evidence only; it grants no integration authority.

The active canonical binding remains Issue #1147 comment `5675066392`,
Planning Program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`,
activation `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Review attacks and results

### 1. Frozen producer identity and review visibility — PASS

Producer terminal comment `5935515528` binds the exact PR #1370 head
`d8796c07978ff6b91fb1b116ed26b9463f7de551`, work SHA
`81611d19b1ec3f5c4bcc3506ecc35945e4ede869`, final-head selected-engine run
`36890264547`, artifact `11175524561`, and required review route #1371.

PR #1370 is still an open draft PR from `planning/issue-1343` to `main`.
The review did not mutate the producer branch.

### 2. Godot 4.7.1 pin and acquisition integrity — PASS

`game/project.godot` declares Godot 4.7 feature compatibility. The runner
rejects any engine version not matching `4.7.1.stable`.

CI does not acquire a floating provider binary: it reads the reviewed repository
artifact lock, checks exact version `4.7.1-stable`, and verifies the retained
SHA-256 before execution.

The lock is explicitly TOFU evidence rather than vendor-signed identity; this
review does not upgrade that provenance.

### 3. Exact-head import/runtime smoke — PASS

Run `36890264547` imported the project and executed
`game/smoke_test.gd` at exact producer head.

Observed PASS assertions include:

- main scene loads;
- interaction, commitment, and diagnostics APIs exist;
- controllable player node exists;
- negotiation fails closed before investigation;
- public-record + material-trace + repair-pilot completes;
- public-record + explicit truth-deferral + records-first completes;
- records-first defer route does not fabricate material-trace evidence;
- both committed routes preserve `UNKNOWN_BY_DESIGN`;
- commitment fails closed before negotiation;
- unknown interaction surface fails visibly.

Terminal marker: `EVERFIELD_SMOKE_PASS`.

### 4. Real boot scene and player movement — PASS

`game/project.godot` boots `res://main.tscn`; that scene instantiates
`game/main.gd`.

`main.gd` creates a visible Player node, reads WASD/arrow input every frame,
applies normalized movement at bounded speed, and clamps position to world
bounds. This is a real executable movement surface, not a prose-only placeholder.

Informationally, the headless smoke verifies player presence rather than
simulating directional input; movement behavior is therefore additionally
confirmed by cold static inspection of the exact script.

### 5. Bounded Old Works gameplay loop — PASS

The exact implementation surface is limited to the clean-reviewed
`VS:OLD-WORKS-ACCOUNTS-01` consumption path:

1. required public record;
2. independent material trace or explicit truth deferral;
3. Commons Hearing only after the investigation predicate;
4. repair-pilot, records-first, or explicit commitment deferral;
5. Project Table completion only for a committed route.

The implementation does not expand into production quest architecture,
shipping systems, or unrelated gameplay.

### 6. Mystery/truth separation — PASS

`MYSTERY_STATE` is fixed to `UNKNOWN_BY_DESIGN`.

Public records, material traces, truth deferral, hearing choice, and completion
only append route/state events. None changes the mystery state or promotes a
claim to canonical truth.

Both smoke routes explicitly assert the mystery remains
`UNKNOWN_BY_DESIGN`.

### 7. Private-secret isolation — PASS

The executable code contains no private-secret gate and no private Anwen secret
dependency. The run documentation explicitly states that the optional/private
secret is not required or implemented in this bootstrap.

The bounded loop is therefore solvable without hidden/private information.

### 8. Observable fail-closed guards — PASS

The exact script exposes stable `EF-*` diagnostics and returns failure without
state promotion for:

- hearing before investigation;
- truth deferral before required record review;
- Project Table before commitment;
- commitment before an open hearing;
- unsupported commitment choice;
- unknown interaction surface;
- interaction outside station range.

Unknown-surface and unsupported-choice failures also emit Godot errors. Other
guards remain visible in HUD/log diagnostics and leave the gated state
unchanged.

### 9. State/history preservation and reset boundary — PASS

Ordinary progression appends route events into `state["history"]`; later
hearing/commitment actions do not erase prior events.

Choosing commitment deferral appends `PUBLIC_COMMITMENT_DEFERRED`, clears only
the current commitment, and allows a later hearing without rewriting history.

`reset_slice()` clears the bounded demo session and is explicitly documented
as demo-session reset only. No production persistence semantics are claimed.

### 10. Save/load claim discipline — PASS

The bounded loop does not require persistence to execute or review. The packet
therefore omits a production save/load system and explicitly retains production
persistence as deferred debt.

No save/load or production persistence PASS is claimed.

### 11. Scope and authority boundaries — PASS

The packet explicitly withholds:

- empirical accessibility PASS;
- production hardening/authority;
- provider/commercial authority;
- shipping-platform commitment;
- release packaging/authority;
- legal/certification authority;
- final canon/canonical content authority;
- integration authority.

This review does not upgrade any of those states.

### 12. Diff hygiene and hidden-payload inspection — PASS

PR #1370 changes exactly eight text-source/document/workflow paths. No generated
binary, vendored dependency payload, release artifact, credential file, secret
material, unrelated architecture, or broad repository mutation appears in the
reviewed diff.

The engine binary is acquired transiently in CI from the separately reviewed
lock and is not committed to the producer packet.

## Findings

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- informational: 1

Informational note: headless smoke confirms a Player node and all gameplay
guards/routes, while directional input/motion itself is confirmed by exact-script
inspection rather than synthesized input events. This does not impair the
bounded review objective because the movement implementation is explicit,
bootable, selected-engine-imported, and the required executable scene passes.

## Disposition

`CLEAN_FOR_BOUNDED_FIRST_PLAYABLE_INTEGRATION_REVIEW_GATE`

This satisfies only the required implementation review/test gate for the exact
frozen #1343 packet. It does **not** authorize integration of PR #1370, remove
its draft state, grant canonicality, establish empirical accessibility PASS,
create production/release/provider/legal/certification authority, or settle
final canon.

Any later integration episode must separately re-derive current main, exact
reviewed producer identity, compatibility, ownership, integration authority,
and expected head. Any integration into `main` remains squash-only.
