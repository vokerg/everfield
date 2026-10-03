# Issue #1414 handoff — playable presentation fan-in

## Mission

`IMPLEMENTATION-INCREMENT-OLD-WORKS-PRESENTATION-01`

Owner claim: issue comment `5972420430`  
Branch: `planning/issue-1414`  
Base main: `849642087297f8b8c83e5bda927aa6ce9d5ef899`  
Canonical binding: Issue #1147 comment `5675066392`  
Canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`

## Freshly verified prerequisites at claim

All four required clean-reviewed publications are ancestors of the base and their expected component/test blobs were verified directly on the base:

- Old Works world/evidence publication #1436 / Producer #1410:
  - publication main `77ba0cfc166a1c63841f3cd318d9c0beb46ed60c`
  - component `8e498156bb9a5413f53a84b14fc279c4be6c8f23`
  - smoke `a69e4c93960cf459544d42a160cc532d03401e5d`
- Commons Hearing Producer #1411:
  - publication main `37829af0c80d2a561f3ce74da75088a7835ec02b`
  - component `9682c47ee2c84ea42417651d0ca2e4f30ebf78b2`
  - smoke `0ebbccebf03e12386ba8fd31f593aade200b4323`
- Commitment consequences Producer #1412:
  - publication main `7aad6e736ba08e42f49b06b04fcad9d7feff5a41`
  - component `419688e17515bf5f67b383182c0b6330111ce4be`
  - smoke `9eed8bc5be54863b18e70475b16e5472c7679dd1`
- Remediated movement interaction publication #1451 / Remediation #1448:
  - publication main `a45f3cc247e0095e9bcf1542088c649310ea7f6b`
  - movement smoke `4c5bd980eecd47fcc620d72f4819e3dab687d059`
  - runner `e913b8996052f6e21616d58b29cc132f2684eda5`
  - locked-Godot runtime PASS: run `37136453216`, job `111241865360`

## Fan-in changes

Only the issue-owned shared fan-in surface is changed:

- `game/main.gd`
  - instantiates the three published presentation components;
  - renders reviewed Old Works station text;
  - renders reviewed Maelin/Selka hearing beats;
  - renders reviewed repair, records-first, and explicit-deferral consequences;
  - preserves existing state-machine guards, history, movement semantics, and `UNKNOWN_BY_DESIGN`.
- `game/smoke_test.gd`
  - asserts exact visible presentation text from all three components;
  - exercises repair-pilot;
  - exercises truth-deferral, public commitment deferral, hearing reopen, and records-first completion;
  - checks private provenance is not exposed and mystery state never resolves.
- `.github/workflows/godot-first-playable-smoke.yml`
  - runs the state-machine smoke and clean-remediated movement/proximity smoke together;
  - retains exact Godot 4.7.1 lock/hash verification and immutable evidence upload.
- `docs/implementation/first-playable.md`
  - documents the integrated reviewed presentation and test contract.
- this handoff.

`game/main.tscn` remains unchanged because the visible presentation surface is created deterministically by `game/main.gd`; no component source/test packet is rewritten.

## Required validation before terminal handoff

The exact final branch head must receive authoritative repository CI under locked Godot `4.7.1-stable` proving:

1. state-machine smoke exits 0 with `EVERFIELD_SMOKE_PASS`;
2. movement/proximity smoke exits 0 with `EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS`;
3. both repair-pilot and records-first/defer investigation routes complete;
4. reviewed Old Works, Commons Hearing, and consequence presentation assertions execute successfully;
5. fail-closed unknown/out-of-range interaction checks remain green.

A draft PR at the exact terminal head is required before `REVIEW_READY`. The next route is one fresh independent required review with allowed clean disposition `CLEAN_FOR_OLD_WORKS_PRESENTATION_INCREMENT_INTEGRATION`.

## Authority boundary

Bounded gameplay fan-in only. No final canon, mystery resolution, production/release, empirical accessibility certification, legal/provider authority, or integration authority is created here. Main integration remains a separate exact-head squash-only decision after clean required review.
