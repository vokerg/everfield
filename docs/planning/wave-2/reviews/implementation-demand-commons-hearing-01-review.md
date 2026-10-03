# Required review — Commons Hearing dialogue presentation component

## Review identity

- review issue: #1418
- mission: `IMPLEMENTATION-DEMAND-COMMONS-HEARING-01-REV-01`
- task class: `REQUIRED_REVIEW / IMPLEMENTATION_COMPONENT_DIALOGUE_PRESENTATION`
- reviewer branch: `planning/issue-1418`
- winning claim: comment `5970742137`
- reviewer actor: `frontier-drain-commons-review-1418-gpt56sol-20261003-01`
- review base: `dcabab2a2f903a42ae55d6965511cf9207b0f0c6`
- canonical binding: Issue #1147 comment `5675066392`
- canonical program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical activation: `87c85cecfa9a2ffa464c4b36816a138bf41441af`
- canonicality: `NOT_CANONICAL`

The producer branch was treated as immutable throughout this review.

## Frozen producer identity

Judged producer: Issue #1411 / `IMPLEMENTATION-DEMAND-COMMONS-HEARING-01`.

- producer ownership generation: comment `5970329047`
- terminal `STATUS(REVIEW_READY)`: comment `5970379802`
- producer branch: `planning/issue-1411`
- exact producer head: `a610b00ed03282cc079cca4d4f9430ddd54e9bf0`
- draft PR: #1417
- PR state at review: open / draft
- PR head: `a610b00ed03282cc079cca4d4f9430ddd54e9bf0`
- PR base SHA: `848acba1bba430170265b56d3f2de71b3268b7df`
- changed files: exactly 3

Exact producer blobs:

1. `game/components/commons_hearing/commons_hearing_presentation.gd`
   - `9682c47ee2c84ea42417651d0ca2e4f30ebf78b2`
2. `game/components/commons_hearing/commons_hearing_presentation_smoke.gd`
   - `0ebbccebf03e12386ba8fd31f593aade200b4323`
3. `docs/planning/handoffs/issue-1411.md`
   - `98a8400e11a86c63dc32ce2b3bb28c8978a17c13`

No shared gameplay, workflow, project, content-source, or sibling-component path appears in PR #1417.

## Reviewed content authority

The clean-reviewed #1379/#1387 source artifacts are present on current main with the exact declared identities:

- Markdown: `docs/planning/wave-2/content/demand/commons-hearing-participants-01.md`
  - blob `119dc87954a20514fc10cdd90d3037accc26e660`
- YAML: `docs/planning/wave-2/content/demand/commons-hearing-participants-01.yaml`
  - blob `bd369b547558648aae3dd2e02f929e0c44b331f3`

The prior required content review remains clean for bounded consumption. This implementation review does not upgrade that content to final canon.

## Adversarial review

### 1. Participant identity — CLEAN

The component exposes exactly the two reviewed presentation identities:

- `OW_HEARING_PARTICIPANT_MAELIN_01` -> `CHAR:maelin_sor`
- `OW_HEARING_PARTICIPANT_SELKA_01` -> `CHAR:selka_vey`

No third participant, office, faction membership, representation, exclusive standing, or legitimacy grant is introduced.

### 2. Dialogue source parity — CLEAN

All ten implementation-facing dialogue beat IDs from the reviewed YAML occur in the component, and all ten player-facing strings match byte-for-byte. Review found 10/10 matches and zero mismatches.

The component preserves opening, repair-pilot, records-first, defer/nonalignment, and refusal presentation without inventing additional line authority.

### 3. Refusal, deferral, and nonalignment — CLEAN

All ten beats set `required_for_progression: false`. Refusal beats also carry `hidden_gate: false` and `consent_effect: NONE`.

The contract explicitly states `deferral_is_consent_in_waiting: false`; no hidden progression debt or delayed-consent semantics are introduced.

### 4. Relationship/social authority — CLEAN

The component declares:

- `direct_relationship_mutation: false`
- `universal_popularity_or_relationship_scalar: false`
- `relationship_state_grants_information_access: false`

Participant records deny office/representation authority. The component is presentation-only and does not introduce a universal approval/popularity/relationship scalar.

### 5. Mystery, truth, private information, and canon — CLEAN

`MYS:FRAGMENTATION-CAUSE` remains exactly `UNKNOWN_BY_DESIGN`.

`INFO:anwen_contested_record_provenance_gap` is only named as the private-information reference; `private_information_required: false` and the component exposes no secret payload or secret-access grant.

The contract denies direct game-state mutation, legitimacy, representation, and canonical authority.

### 6. Failure behavior — CLEAN

Unknown participant IDs, dialogue IDs, and routes all fail closed with stable explicit diagnostics and empty return values:

- `EF-COMMONS-HEARING-UNKNOWN-PARTICIPANT`
- `EF-COMMONS-HEARING-UNKNOWN-LINE`
- `EF-COMMONS-HEARING-UNKNOWN-ROUTE`

### 7. Smoke coverage design — CLEAN STATICALLY

The exact smoke source has the declared blob `0ebbccebf03e12386ba8fd31f593aade200b4323`, loads the exact component path, exercises participant/line/route APIs, checks refusal/deferral and authority guards, checks fail-closed behavior, exits nonzero on failure, and emits `EVERFIELD_COMMONS_HEARING_PRESENTATION_SMOKE_PASS` only on a zero-failure path.

### 8. Mandatory exact runtime evidence — MAJOR

The review contract requires Godot 4.7.1 headless execution of the exact component smoke with successful exit and sentinel `EVERFIELD_COMMONS_HEARING_PRESENTATION_SMOKE_PASS`.

The only workflow run associated with exact producer head `a610b00ed03282cc079cca4d4f9430ddd54e9bf0` found during review is:

- run `37131795409`
- job `111228190568`
- workflow `Godot first-playable smoke`
- conclusion: `success`

That evidence is non-satisfying for this acceptance item. The job log shows the smoke step invoking:

`bash tools/implementation/run_godot_smoke.sh`

and the runtime trace is from:

`res://smoke_test.gd`

The log does not execute `res://components/commons_hearing/commons_hearing_presentation_smoke.gd` and does not establish the required component sentinel. Therefore exact component runtime PASS is not proven.

This is a verification-evidence gap, not a demonstrated producer-code defect. No producer mutation is justified without exact runtime evidence.

### 9. Producer path isolation — CLEAN

PR #1417 changes exactly:

- `docs/planning/handoffs/issue-1411.md`
- `game/components/commons_hearing/commons_hearing_presentation.gd`
- `game/components/commons_hearing/commons_hearing_presentation_smoke.gd`

No shared gameplay, workflow, project, content-source, or sibling-component path is changed.

## Findings

- BLOCKER: 0
- MAJOR: 1
  - Mandatory exact-head Godot 4.7.1 runtime execution of the Commons Hearing component smoke is not proven. Existing successful run `37131795409` executes only the generic first-playable smoke.
- correction-requiring MINOR: 0
- informational: 0

## Required remediation

Issue #1429 is the bounded runtime-evidence successor. It must preserve the exact frozen producer identity and obtain authoritative execution evidence for:

`Godot_v4.7.1-stable_linux.x86_64 --headless --path game --script res://components/commons_hearing/commons_hearing_presentation_smoke.gd`

with process exit 0 and sentinel `EVERFIELD_COMMONS_HEARING_PRESENTATION_SMOKE_PASS`.

The producer files remain read-only in that verification episode. PASS evidence must route to a fresh required re-review rather than self-upgrading this review.

## Disposition

`CHANGES_NEEDED`

Static review is otherwise clean. The disposition is driven solely by the missing mandatory exact-component runtime evidence and applies only to producer head `a610b00ed03282cc079cca4d4f9430ddd54e9bf0` and the exact producer blobs above.

No producer publication, live-scene integration, final character/social canon, relationship mutation, production/release, empirical accessibility certification, integration, verification-PASS, or canonical authority is granted.
