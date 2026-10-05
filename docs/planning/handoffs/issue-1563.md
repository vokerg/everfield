# Issue #1563 — bounded content demand intake for implementation #1545

## Identity and scope
Mission: W2-CONTENT-DEMAND-FROM-IMPLEMENTATION-1545. Actor: frontier-content-intake-1563-20261005-1747.
Winning ownership: 5999913595 (GitHub created_at/updated_at both 2026-10-05T17:46:04Z).
Base/inspected main: 6d601848c4c29734f319e47611390303fd351ed3.
Canonical binding: #1147 / 5675066392; program fd4cf1119c3f86acc3af620024eea72235e81ce4; activation 87c85cecfa9a2ffa464c4b36816a138bf41441af is an ancestor.
Owner directives #84 / 5511637902 and 5889817307 permit bounded implementation-fed content, prohibit speculative CONT-08.
Routing only; NOT_CANONICAL; no gameplay, review, verification or publication authority.

## Result
NO_NEW_CONTENT_DEMAND_EXISTING_REVIEWED_CONTENT_COVERS_1545.
No source issues created. No successor is required for this bounded intake.
This conclusion applies only to the unchanged five-station, three-choice #1545 interface.

## Evidence versus inference
Read the actual source #1545 contract and inspected current main controller, station metadata, HUD model, all three public narrative providers, corrected presentation assembler, and their published required review reports.
#1545 requires preservation of approved titles/hints, phase objectives, E/1/2/3/R mapping, deferral, both completion routes, reset and UNKNOWN_BY_DESIGN. Its mutable scope excludes narrative providers and both published component roots.
Its two concrete defects are stale proximity text on near-to-far movement and hardcoded action decoding. They require implementation selection/dispatch and live tests, not new narrative text.
Static source inspection supports content availability; it does not prove live HUD behavior or runtime/accessibility readiness.

| Concrete demand | Existing exact source at inspected main | Coverage |
| --- | --- | --- |
| Five station IDs and hearing/project prompts | StationWorld 87fefab8816a2ab8795c54877299716ec86b227e | public_record, material_trace, defer_conclusion, commons_hearing, project_table; all titles/hints populated |
| Three Old Works station titles/prompts | old_works_world_presentation.gd 8e498156bb9a5413f53a84b14fc279c4be6c8f23 | OW_ARCHIVE_TITLE/PROMPT, OW_TRACE_TITLE/PROMPT, OW_DEFER_TITLE/PROMPT; controller resolves these exact IDs |
| Far/near, hearing and completion objectives | hud_objective_model.gd 59480c7b8c7f3f8161cd261fb195704f8299679f | six phase objectives, explicit 1/2/3 choices, completion outcome; controller/policy retain Press R to reset |
| Proximity selection without new text | interaction_feedback_policy.gd 0f3b32c254f00f27338202fa7f0dd53c6f2efcf8 | formats existing title/hint; returns supplied HUD objective off radius and completion reset suffix |
| Exact five action mappings | action_command_policy.gd d5422813a2e2bd938d9776c3f2cd12a058a9ac10 | existing E/1/2/3/R commands; no new content route |
| Hearing voices, refusal and three public choices | commons_hearing_presentation.gd 9682c47ee2c84ea42417651d0ca2e4f30ebf78b2 | reviewed Maelin/Selka opening and repair_pilot, records_first, defer; no implied consent |
| Selected/completed consequences and explicit noncommitment | commitment_consequence_presentation.gd 419688e17515bf5f67b383182c0b6330111ce4be | five existing event mappings, deferral history/reopening text, inert reassessment hooks |
| Public text composition | playable_presentation.gd ba819915fc55e444d54d46671892cea35cb6b3cf | same reviewed providers, route/event agreement and fail-closed assembly |

Source controller: game/main.gd 1b38126daed3db76f3c398f01c5d8cb375fa25cf.
Published corrected presentation review: #1528 report e6d5cdabee62a51a22ab524a587caa0157d081b0, CLEAN_FOR_CORRECTED_PLAYABLE_PRESENTATION_COMPONENT_PUBLICATION. It preserves original world/consequence readers plus corrected hearing validation; the rejected #1515 candidate is not substituted.
Published hearing re-review #1440 report 08b917fa23156156e9e0830a010937789daebd32 and consequence re-review #1428 report 2f79b66dd8b5060385ae0f8f37d5eaeedef9ed5c bind the provider identities above to clean required reviews.
Earlier intake #1401 covered source #1371, not #1545; its no-op is provenance, not a substitute for this fresh source inspection.
Current open frontier at selection: #1545 shared fan-in; #1558/#1561 source integrations owned; #1556 repair owned; #1562 review blocked pending producer terminal. No independent live content root duplicates this intake.

## Alternatives and dependencies
Creating world, character, dialogue or consequence roots now would duplicate populated reviewed contracts. Retain existing content and let #1545 perform its owned live-controller integration and exact locked-engine acceptance.
Both pure components have separately squash-published blobs on inspected main (6736f046335819ac3ca293ba54336fd0de7cbb40 and 6d601848c4c29734f319e47611390303fd351ed3); their integration terminal authority must still be independently consumed by #1545. This intake does not declare #1545 READY.
No new lore, station, participant, choice, truth resolution, or consent effect is recommended.

## Remaining risks, evaluation and reopen conditions
The long deferral hint and public presentation viewport remain empirical display leads, not demonstrated missing-content defects. Do not rewrite reviewed text from static length alone.
#1545 must retain its independent live near-to-far/reset/phase/choice tests and required review; standalone source presence cannot certify actual scene behavior.
Reopen content demand only for a demonstrated missing string/route, required content inconsistency, reproducible live-view/playtest failure needing bounded editorial change, changed implementation interface or explicit bounded product question.
Private Anwen information remains excluded; UNKNOWN_BY_DESIGN and nonconsent remain unchanged. No new independent critique is required for this explicitly permitted routing NO_OP; any future authored content requires its own declared independent review and publication gates.

## Durable continuation
Only this handoff is authored. Exact branch/PR/head and terminal comment are published on #1563. No content or gameplay files changed and no main integration is requested.
