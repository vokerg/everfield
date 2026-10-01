# Handoff — Issue #1343 / W2-GODOT-FIRST-PLAYABLE-BOOTSTRAP-01

## Identity

- issue: #1343
- mission: `W2-GODOT-FIRST-PLAYABLE-BOOTSTRAP-01`
- branch: `planning/issue-1343`
- ownership generation: comment `5925694231`
- producer actor: `frontier-drain-godot-first-playable-1343-gpt56sol-20261001-01`
- claim base: `main@3ac8ddd9468e261cea8d54c3afb29a76e5e9743a` **(historical claim basis; see current-main note below)**
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- selected engine: Godot `4.7.1-stable`
- selected-engine terminal: Issue #1028 comment `5651263207`
- activating readiness verifier: Issue #1367 terminal `5925681547`
- activation disposition: `PASS_READY_FOR_GODOT_FIRST_PLAYABLE`
- producer draft PR: #1370
- required implementation review/test successor: Issue #1371
- canonicality: `NOT_CANONICAL`

> Correction to the historical claim-basis line above: the exact #1343 claim base is
> `3ac8ddd9468e261cea8d54c3afb9ac9dcf437251`. Current main at this handoff
> is `9179e40e998f3535e087d7358fb29a76e5e9743a`. The only intervening main
> change is squash-publication of already-verified #1364 readiness-remediation
> provenance; it does not overlap this implementation and grants no new
> implementation authority.

## Implemented bounded slice

This packet is the smallest executable implementation of the clean-reviewed
noncanonical content slice `VS:OLD-WORKS-ACCOUNTS-01` / *Accounts at the Old
Works*. It does not canonicalize that content.

Executable behavior:

1. one bootable Godot 2D Old Works scene;
2. controllable player movement with WASD/arrows;
3. public-record investigation as the required evidence step;
4. either independent material-trace inspection or explicit truth deferral;
5. Commons Hearing gated behind that investigation predicate;
6. bounded commitment choice: repair pilot, records-first, or defer/reopen;
7. project-table completion for the two committed routes;
8. durable in-session route history and stable `EF-*` failure diagnostics;
9. world mystery remains exactly `UNKNOWN_BY_DESIGN` on every route;
10. optional/private Anwen secret is not implemented or required.

No production save/load subsystem is introduced because the bounded loop does
not require persistence to execute or review. Manual reset is demo-session
reset only and grants no production persistence semantics.

## Exact implementation artifacts at executable work head

Pre-handoff executable work head:
`81611d19b1ec3f5c4bcc3506ecc35945e4ede869`.

- `game/project.godot` — blob `9da4153ed378945ef5e9634e0e5cae48289845d8`
- `game/main.tscn` — blob `02b943321c258bb807f9496c7a270221df112b31`
- `game/main.gd` — blob `b96659a1cf461a96934666293aecaa565e68579b`
- `game/smoke_test.gd` — blob `38436acc78e62145952462d76bf158ee4748ae59`
- `tools/implementation/run_godot_smoke.sh` — blob `dab9ef4e7affde07645320071819a4dc0496fddb`
- `.github/workflows/godot-first-playable-smoke.yml` — blob `ba551ab71dd4b402def4d67d5d45e506bf0015a2`
- `docs/implementation/first-playable.md` — blob `307e9f2c2b08bf3ed03bd5da5fdab6bd0a934551`

The workflow is deliberately configured to trigger again when this handoff is
added, so the final producer head receives its own exact-head CI result.

## Selected-engine evidence and smoke

The CI path reuses the reviewed repository artifact lock
`docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` blob
`4a88990ae24768eb4f83a8a1311e2a830834649f`.

Locked Godot artifact:

- version: `4.7.1-stable`
- Linux x86_64 SHA-256:
  `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`

Pre-handoff exact-work CI:

- workflow: `Godot first-playable smoke`
- run: `36823769685`
- conclusion: `success`
- checked-out SHA: `81611d19b1ec3f5c4bcc3506ecc35945e4ede869`
- declared PR head SHA: `81611d19b1ec3f5c4bcc3506ecc35945e4ede869`
- artifact id: `11144376305`
- artifact name: `godot-first-playable-36823769685-1`
- runtime: `4.7.1.stable.official.a13da4feb`
- terminal smoke marker: `EVERFIELD_SMOKE_PASS`

The first CI attempt, run `36823653096`, failed before Godot execution because
the GitHub contents API did not preserve executable mode on the shell runner.
The workflow was corrected to invoke the script through `bash`, use a visible
evidence directory, and checkout/record the exact PR head. No gameplay code was
changed by that CI remediation.

## Smoke assertions

The exact selected-engine run independently exercised:

- main scene loads;
- interaction, commitment, and diagnostic APIs exist;
- controllable player node exists;
- negotiation fails closed before investigation;
- public-record + material-trace + repair-pilot route completes;
- repair route preserves unresolved mystery and observable history;
- public-record + explicit truth-deferral + records-first route completes;
- records-first defer route does not fabricate material-trace evidence;
- commitment fails closed before negotiation;
- unknown station fails visibly;
- terminal marker `EVERFIELD_SMOKE_PASS`.

## Reviewed content boundary

Implementation consumes only the bounded clean-reviewed authored-content surface
published on main:

- Markdown blob: `5e94bdb0ca6146bab93264fc8e6763590aa289d2`
- corrected YAML blob: `8d341d534ef4a27929aaabdf5b81a6d5ff86b80e`
- remediation review #449 terminal: `5308612900`
- remediation publication #444 terminal: `5308648741`

The implementation intentionally does not settle
`MYS:FRAGMENTATION-CAUSE`, require the private Anwen secret, invent a
`GameTimePolicy`, or create shipping/canonical content authority.

## Preserved fail-closed debt

Still ungranted/open:

- empirical accessibility evidence remains `NOT_RUN` / false;
- production accessibility and release clearance;
- full-production/provider controls;
- production hardening and deployment;
- final shipping OS/hardware/storefront commitments;
- Steam Deck Verified/certification claims;
- legal/commercial/provider authority at affected boundaries;
- final canonical content;
- production save/load/persistence semantics;
- release authority and integration authority.

## Required next route

Issue #1371 /
`W2-GODOT-FIRST-PLAYABLE-BOOTSTRAP-01-REV-01` is materialized as the required
fresh implementation review/test successor and remains blocked pending #1343's
exact terminal packet.

The reviewer must use a fresh ownership episode distinct from the producer,
freeze the exact PR/head/artifacts, independently exercise or inspect the
selected-engine smoke evidence, cold-review the diff, and reject any scope or
authority inflation.

Allowed review dispositions are:

- `CLEAN_FOR_BOUNDED_FIRST_PLAYABLE_INTEGRATION_REVIEW_GATE`;
- `CHANGES_NEEDED`;
- `INVALIDATED`.

A clean review satisfies only the implementation review/test gate. Integration
remains separate and squash-only.

## Producer authority boundary

At producer terminal:

- executable first-playable candidate: **yes**;
- selected-engine smoke PASS: required on the final head;
- producer self-review as integration authority: **no**;
- integration authority: **false**;
- production/release/legal/provider/certification authority: **false**;
- empirical accessibility PASS: **false**;
- canonical content/final canon: **false**;
- canonicality: `NOT_CANONICAL`.


## Recovery continuation — 2026-10-01

The original producer ownership generation at comment `5925694231` expired without a terminal record after its exact implementation packet and final-head CI had already been published. The task was recovered through winning STALE intent `5935482390` and RECOVER generation `5935484769` by actor `frontier-drain-recover-godot-first-playable-1343-gpt56sol-20261001-02`.

Recovery cold-inspection found the inherited executable packet unchanged at pre-recovery head `5aefb403b35bde1ab754b9feca2916e3f5b4ea03`, PR #1370 still open/draft, and exact-head workflow run `36823961380` successful with retained artifact `11144396689` (digest `sha256:f856686e0c8bdd9b3bad275961e6a4ff34d98f1a9807827b0f75a2bc46ddea97`). No gameplay or implementation semantics were changed during recovery. This handoff-only recovery commit intentionally retriggers the selected-engine smoke workflow; terminal REVIEW_READY is permitted only after that new exact-head run succeeds.

Current-main movement through `32a93df5e6f70771a28b673e1777c4c0aa223b4e` consists of separate planning/readiness/content provenance and does not itself grant integration, canonical, production, release, accessibility, provider, legal, or certification authority. Fresh Issue #1371 review must independently re-check compatibility at its own claim/terminal time.
