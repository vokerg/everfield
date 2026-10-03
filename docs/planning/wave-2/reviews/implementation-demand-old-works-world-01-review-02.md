# Review #1427 — Old Works world/evidence presentation component re-review

## Scope and authority

Fresh required review of the exact frozen Producer #1410 packet at `20284fa9171d1d6f91e3e930d627f587062485cb`, after blocking runtime-evidence Remediation #1421. This review is independent of producer actor session `frontier-drain-old-works-world-1410-gpt56sol-20261003-01` and does not mutate producer/remediation bytes or grant integration/canonical/release authority.

Canonical basis: Issue #1147 comment `5675066392`; program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`.

## Frozen identities

- producer issue / terminal: #1410 / `5969178423`
- producer head: `20284fa9171d1d6f91e3e930d627f587062485cb`
- producer PR: #1415
- component blob: `8e498156bb9a5413f53a84b14fc279c4be6c8f23`
- smoke blob: `a69e4c93960cf459544d42a160cc532d03401e5d`
- source content markdown blob: `d2140477a3107319ea47335402289e922d1e225b`
- source content YAML blob: `f80299d04765aa68c8516d4c458372f356ad3bc8`

## Findings

**Disposition: CLEAN_FOR_OLD_WORKS_WORLD_COMPONENT_PUBLICATION**

Findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR / 0 informational.

### Objectives 1–8 and 10 — PASS

Independent comparison of Producer #1410 against its base shows exactly three changed paths:
- `game/components/old_works_world/old_works_world_presentation.gd`
- `game/components/old_works_world/old_works_world_presentation_smoke.gd`
- `docs/planning/handoffs/issue-1410.md`

The component matches the reviewed #1378/#1383 content contract:
- required Old Works IDs and player-facing strings are exact;
- `MYS:FRAGMENTATION-CAUSE` remains `UNKNOWN_BY_DESIGN`;
- both fragmentation accounts have truth effect `NONE`;
- public record is explicitly nonprivate and cannot expose `INFO:anwen_contested_record_provenance_gap`;
- Material Trace is bounded/non-discriminating and cannot select a causal winner; count and visual difference are explicitly not truth strength/independence;
- explicit truth deferral remains legal;
- presentation mutation/canonical authority are both false;
- unknown presentation IDs and stations fail closed with explicit diagnostics.

No shared or sibling implementation path is changed.

### Objective 9 — PASS: exact runtime evidence independently validated

Final evidence run `37132898410`, job `111231394596`:
- job name `exact-component-smoke`, conclusion `success`;
- checkout explicitly used exact producer `20284fa9171d1d6f91e3e930d627f587062485cb`;
- workflow identity guards verified component `8e498156bb9a5413f53a84b14fc279c4be6c8f23` and smoke `a69e4c93960cf459544d42a160cc532d03401e5d`;
- reviewed Godot artifact lock resolved `4.7.1-stable`; downloaded ZIP passed SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`;
- engine banner observed: `Godot Engine v4.7.1.stable.official.a13da4feb`;
- exact smoke ran under `set -euo pipefail` and job success therefore requires Godot exit success plus sentinel grep success;
- all contract assertions passed, including fail-closed unknown ID/station behavior;
- sentinel `EVERFIELD_OLD_WORKS_WORLD_PRESENTATION_SMOKE_PASS` was observed;
- artifact `11277592564` is unexpired and reports digest `sha256:e8014308c998b668d77ece55fb08f4ca4b3ed44ab8a50a7f94ff4a58255a97c9`.

This directly resolves the sole MAJOR from Review #1416; #1416 is not self-upgraded.

## Reopen conditions

Reopen if producer head/blob/path identity changes, reviewed source bytes change, runtime evidence becomes inconsistent with the frozen producer, or publication discovers a conflicting mutation on the exact producer paths.

## Authority boundary

Clean review only. Separate current-authority re-derivation and squash-only publication are required. No final canon, live-scene fan-in acceptance, truth resolution, production/release, or empirical accessibility certification is granted.
