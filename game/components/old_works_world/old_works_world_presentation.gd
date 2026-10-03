extends RefCounted

const MYSTERY_REF := "MYS:FRAGMENTATION-CAUSE"
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"
const PRIVATE_INFORMATION_REF := "INFO:anwen_contested_record_provenance_gap"
const CLAIM_A_REF := "CLM:FRAGMENTATION-ACCOUNT-A"
const CLAIM_B_REF := "CLM:FRAGMENTATION-ACCOUNT-B"

const STRINGS := {
    "OW_WORLD_TITLE": "The Old Works",
    "OW_WORLD_SUBTITLE": "Inherited channels, patched routes, unfinished arguments.",
    "OW_WORLD_ENTRY": "Old stone, newer timber, and repairs from more than one hand meet in the same working yard. Nothing here explains itself in one layer.",
    "OW_WORLD_ROUTE_CUE": "The ledger table, exposed repair seam, hearing space, and project table all face the same inherited works.",
    "OW_ARCHIVE_TITLE": "Archive Ledger",
    "OW_ARCHIVE_PROMPT": "Read the public record.",
    "OW_ARCHIVE_BODY_01": "The surviving entries agree that coordinated upkeep broke apart. They do not agree that one cause explains why.",
    "OW_ARCHIVE_BODY_02": "One recorded account argues for a single dominant cause. Another rejects that reading. Both remain recorded as accounts, not findings.",
    "OW_ARCHIVE_BODY_03": "Later pages list local repairs, bypasses, and changed uses without resolving the older dispute.",
    "OW_ARCHIVE_EXIT": "The ledger gives you claims and a sequence of changes—not a verdict. Compare it with something independent, or leave the conclusion open.",
    "OW_TRACE_TITLE": "Material Trace",
    "OW_TRACE_PROMPT": "Inspect the repair seam.",
    "OW_TRACE_BODY_01": "A dressed stone channel continues beneath a later timber crossing. Their wear patterns do not match exactly.",
    "OW_TRACE_BODY_02": "Several fasteners and braces were added after the surrounding surface had already weathered. Some older fixing points are empty.",
    "OW_TRACE_BODY_03": "The trace supports a history of alteration and repeated maintenance. It does not identify a single cause for the fragmentation.",
    "OW_TRACE_EXIT": "This is independent material evidence within the inspected surface, not proof of either account.",
    "OW_DEFER_TITLE": "Leave the Cause Open",
    "OW_DEFER_PROMPT": "Record that the evidence is insufficient for a final conclusion.",
    "OW_DEFER_RESULT": "You can act on the present condition without pretending the old dispute is settled.",
    "OW_ENV_CHANNEL_PATCHWORK": "Old channel edge; later patch; another repair over that.",
    "OW_ENV_BYPASS": "A capped opening sits beside a narrower working bypass.",
    "OW_ENV_REUSED_FITTING": "A reused fitting carries marks from more than one placement.",
    "OW_ENV_LEDGER_TO_TRACE": "The ledger records repairs in general; the seam shows one place where change is physically visible.",
    "OW_ENV_TRACE_TO_HEARING": "From the repair seam, the hearing space remains in view: observation can travel into debate without becoming a verdict.",
    "OW_ENV_HEARING_TO_PROJECT": "The project table is close enough to the works to make tradeoffs concrete, but no repair plan answers the historical mystery by itself.",
}

const STATIONS := {
    "public_record": {
        "title_id": "OW_ARCHIVE_TITLE",
        "prompt_id": "OW_ARCHIVE_PROMPT",
        "body_ids": ["OW_ARCHIVE_BODY_01", "OW_ARCHIVE_BODY_02", "OW_ARCHIVE_BODY_03"],
        "exit_id": "OW_ARCHIVE_EXIT",
        "evidence_role": "DISC_ROLE:PUBLIC_RECORD",
        "relation": "PUBLIC_NONPRIVATE_RECORD_SURFACE",
    },
    "material_trace": {
        "title_id": "OW_TRACE_TITLE",
        "prompt_id": "OW_TRACE_PROMPT",
        "body_ids": ["OW_TRACE_BODY_01", "OW_TRACE_BODY_02", "OW_TRACE_BODY_03"],
        "exit_id": "OW_TRACE_EXIT",
        "evidence_role": "DISC_ROLE:MATERIAL_TRACE",
        "relation": "BOUNDED_PHYSICAL_OBSERVATION_SURFACE",
    },
    "defer_conclusion": {
        "title_id": "OW_DEFER_TITLE",
        "prompt_id": "OW_DEFER_PROMPT",
        "result_id": "OW_DEFER_RESULT",
        "relation": "EXPLICIT_LEGAL_TRUTH_DEFERRAL",
    },
}

func has_text(presentation_id: String) -> bool:
    return STRINGS.has(presentation_id)

func get_text(presentation_id: String) -> String:
    if not STRINGS.has(presentation_id):
        push_error("[EF-OW-WORLD-UNKNOWN-ID] Unknown Old Works presentation ID: %s" % presentation_id)
        return ""
    return String(STRINGS[presentation_id])

func get_station(station_id: String) -> Dictionary:
    if not STATIONS.has(station_id):
        push_error("[EF-OW-WORLD-UNKNOWN-STATION] Unknown Old Works station: %s" % station_id)
        return {}
    return (STATIONS[station_id] as Dictionary).duplicate(true)

func get_contract() -> Dictionary:
    return {
        "mystery_ref": MYSTERY_REF,
        "mystery_state": MYSTERY_STATE,
        "claim_truth_effects": {
            CLAIM_A_REF: "NONE",
            CLAIM_B_REF: "NONE",
        },
        "private_information_ref": PRIVATE_INFORMATION_REF,
        "public_record_exposes_private_information": false,
        "material_trace_may_select_causal_winner": false,
        "record_count_is_truth_strength": false,
        "visual_difference_alone_proves_independence": false,
        "truth_deferral_is_legal": true,
        "presentation_mutates_game_state": false,
        "presentation_grants_canonical_authority": false,
    }
