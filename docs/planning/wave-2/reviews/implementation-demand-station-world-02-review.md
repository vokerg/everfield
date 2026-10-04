# Required independent review — station-world metadata component

**Review mission:** `IMPLEMENTATION-DEMAND-STATION-WORLD-02-REV-01` / Issue #1512. **Independent reviewer:** `frontier-review-1512-gpt56sol-20261004-2023-01` (not the Producer #1504 nor either Verifier #1511 session); winning claim comment `5983028125`. **Disposition:** `CLEAN_FOR_STATION_WORLD_COMPONENT_PUBLICATION` for the frozen *metadata component only*, subject to separately authorized current-main compatible squash-only publication. **Severity:** 0 BLOCKER, 0 MAJOR, 0 correction-requiring MINOR.

## Authority, exact scope, and immutable inputs

- Canonical planning: Issue #1147 binding `5675066392`; `docs/planning/PLANNING-PROGRAM-v1.md` blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Source review base `main@d02bb66a134d5ec35c54782cb9b7d1d96e0db4ea`.
- Producer Issue #1504 `STATUS(REVIEW_READY)` `5978306462`; immutable branch `planning/issue-1504`, open draft PR #1509, frozen HEAD `54a4a044ea56e10bf3dd26e358ead7353fd4d438`, original base `eef8a80d538a908ea685b206d97409ac48a2092f`.
- Source PR has exactly three paths: `game/components/station_world/station_world.gd` blob `87fefab8816a2ab8795c54877299716ec86b227e`; `game/components/station_world/station_world_smoke.gd` blob `0c972e251de6e4fb1a86bbecbce757eaa56999ce`; `docs/planning/handoffs/issue-1504.md` blob `cc492f3671d884ea3e9c05995cdeab66af4b46c7`. The producer source and verification branches were inspected read-only.
- Published comparator: `game/main.gd` blob `9b406cc0a0115f0818df633eda67d69ab7779a06`; published `game/components/old_works_world/old_works_world_presentation.gd` blob `8e498156bb9a5413f53a84b14fc279c4be6c8f23`; `game/project.godot` blob `9da4153ed378945ef5e9634e0e5cae48289845d8`.
- Independently observed five-commit `eef8a80...` -> `d02bb66...` main range changes sibling traversal/presentation and review/handoff files, not `game/main.gd`, station-world root, engine lock or producer handoff. No incompatible overlap with frozen source.

## Exact station ID, metadata and presentation parity

The source explicitly iterates the `STATION_ORDER` array rather than depending on unordered map enumeration. Its five IDs occur exactly once and match original published `STATIONS`, in order. The public station data is limited to `position`, `title`, `hint`, `color` and does not add authority-bearing text. Record-by-record inspection against published `main.gd`:

| Ordered ID | Vector2 position | Fallback title | Fallback hint | Color RGB hex |
| --- | --- | --- | --- | --- |
| `public_record` | `(176,188)` | Archive Ledger | Public record — required | `6ca6c8` |
| `material_trace` | `(338,382)` | Material Trace | Independent evidence — optional | `c3a56f` |
| `defer_conclusion` | `(498,184)` | Defer Conclusion | Legal investigation alternative | `8d88ba` |
| `commons_hearing` | `(676,252)` | Commons Hearing | Negotiate shared use | `7dbb8b` |
| `project_table` | `(798,400)` | Project Table | Commit the bounded next step | `d28d7b` |

The three inspected Old Works presentation records stay separate in the published `OldWorksPresentation` provider: `_station_display` substitutes its title/prompt when available. The metadata titles/hints above are *fallbacks* only; they do not replace `OW_ARCHIVE_*`, `OW_TRACE_*` or `OW_DEFER_*` authoritative presentation text or settle the deliberately unresolved historical cause. No new station, private fact, narrative verdict or gameplay choice was introduced.

## Geometry and bounded data-only behavior

- `Rect2(36,90,888,414)` world bounds; floor four vertices `(22,74),(938,74),(938,516),(22,516)` and fill `172129` are exactly preserved.
- Six WalkPath vertices `(92,286),(176,188),(338,382),(498,184),(676,252),(798,400)`, width `9`, palette `34444e`, and station marker four points `(-20,-20),(20,-20),(20,20),(-20,20)` match original.
- Label position `(-74,-52)`, label size `(148,44)`, initial player spawn `(92,286)` are unchanged. All positions, bounds and palette are static and deterministic.
- `class_name EverfieldStationWorld extends RefCounted`; read-only station IDs/metadata/layout contract methods. No `Node` inheritance, scene creation, input processing, movement, session state, diagnostic emission, public narrative strings, filesystem/network or persistence authority. Source-only error reporting on unknown/invalid station uses `printerr`, which is not a gameplay diagnostics registration authority.
- `get_station_ids()` builds a fresh typed `Array[String]`; `get_station()` deep-duplicates the dictionary; `get_stations()` builds a fresh dictionary of copied entries; `get_layout()` constructs fresh geometry arrays; `get_contract()` obtains a new ID array. Invalid/unknown IDs fail closed with `{}`; `lookup_station(Variant)` checks `TYPE_STRING` before dispatch. Callers cannot mutate shared station records, ID order or layout through returned values.

## Executable smoke and verifier adjudication

- I inspected all assertions in immutable smoke blob `0c972e251de6e4fb1a86bbecbce757eaa56999ce` against the published literal fixture. It checks each ID/order/cardinality/field, all floor/path/marker/bounds/spawn values, `RefCounted`, copy isolation under tampered ID arrays, records, nested dictionary, station removal and packed geometry, and null/int/unknown/empty/wrong-case negative lookup guards. The negative tests require empty results and unchanged subsequent source data. The finish path requires zero accumulated failures and exit `0` for exact `EVERFIELD_STATION_WORLD_SMOKE_PASS`, otherwise failure diagnostics and exit `1`.
- Verifier Issue #1511 terminal `VERIFICATION_STATUS(DONE)` comment `5983018696` is explicitly bound to **final** verifier-only PR #1517 head `6f52d9114fbe665b5f01ccc9da65b57f48d8b45f` with only its two owned workflow/handoff paths. Its workflow blob `e966bf3f96d99a8be601c213dbce2b49b903fa68` checks out frozen producer *full SHA*, confirms source/project/main/lock Git blob hashes, SHA-256-locks Godot ZIP `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` and version `4.7.1.stable.official.a13da4feb` before isolated runtime execution.
- Independently fetched GitHub Actions run `37224153861` (pull_request, final head), job `111500236050`, attempt `1`: each exact-checkout/hash/locked engine/smoke/artifact step completed `success`; decoded job logs explicitly show `godot.zip: OK`, reviewed engine version, 73 actual `[EF-STATION-WORLD-SMOKE][PASS]` results, zero `[FAIL]`, exact success sentinel, no Godot parser/script failure, and successful process exit. This is the isolated station smoke, not unrelated first-playable CI.
- Final GitHub artifact `11310629764`, 1,832 bytes, immutable digest `sha256:953cbdb9db1cf5555e1ee5ce1f2904e438c7d60e35f94b2084527f51b584248c`, belongs to the exact run/head. The verifier records decoded log SHA-256 `48c68f9df5b1f5f93cb6ef3e3d450d17a3a81c1646fdcd9d20d2f9620830418b`. Older verifier run `37190887391` was successful but is not substituted for final-head evidence.

## Independent adversarial findings, constraints and next gate

**Findings:** 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR. No unexpected metadata difference, authority leak, source mutation, missing executable check, opaque assertion substitution, changed toolchain, sibling root edit or incompatible main overlap found. Scope is deliberately a static metadata provider, not integrated controller behavior. The existing playable and sibling roots remain as published and retain their own review/provenance status.

**Disposition:** `CLEAN_FOR_STATION_WORLD_COMPONENT_PUBLICATION` for exactly frozen #1504/PR #1509, but this review is not an integration task. Producer `REVIEW_READY`, verifier PASS, open draft PR, or this clean disposition alone must not be promoted into publication. The next permissible action is *separately authorized*, compatible current-main, exact-source-head, **squash-only noncanonical component publication**, with its own durable integration record and no temporary verifier-workflow merger. Subsequent #1507 shared station/traversal/presentation fan-in must be independently re-derived after all three siblings are properly clean-reviewed and published. No controller/gameplay, truth/canon, persistence, accessibility, readiness, production or release decision is made.

**Review-owned paths only:** this report and `docs/planning/handoffs/issue-1512.md`. Reviewer session `frontier-review-1512-gpt56sol-20261004-2023-01`; no mutation to Producer #1504, Verifier #1511 or current playable. **Reopen** on changed producer bytes, failed/invalidated exact verifier evidence, newly discovered parity flaw, altered canonical binding, overlapping later main mutation, or an actual new authority-bearing dependency.
