extends RefCounted

# Pure read-only, bounded projection. No state mutation, history provenance
# creation, narrative invention, or automatic consent/commitment.
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"
const WorldScript = preload("res://components/old_works_world/old_works_world_presentation.gd")
const ConsequenceScript = preload("res://components/commitment_consequences/commitment_consequence_presentation.gd")

# Hard input budget, and separate bounded presentation/page budget. Oversize
# snapshots are rejected explicitly rather than silently dropping events.
const MAX_HISTORY_EVENTS := 256
const PAGE_SIZE := 8
const WORLD_TITLES := {
    "PUBLIC_RECORD_REVIEWED": "OW_ARCHIVE_TITLE",
    "MATERIAL_TRACE_INSPECTED": "OW_TRACE_TITLE",
    "TRUTH_CONCLUSION_DEFERRED": "OW_DEFER_TITLE",
}
const CONSEQUENCE_TITLES := {
    "COMMITMENT_REPAIR_PILOT": "OW_CONSEQ_REPAIR_TITLE",
    "COMMITMENT_RECORDS_FIRST": "OW_CONSEQ_RECORDS_TITLE",
    "PUBLIC_COMMITMENT_DEFERRED": "OW_CONSEQ_DEFER_TITLE",
    "BOUNDED_REPAIR_PILOT_STARTED": "OW_CONSEQ_REPAIR_TITLE",
    "RECORDS_FIRST_PACKAGE_FILED": "OW_CONSEQ_RECORDS_TITLE",
}
const HEARING_OPEN_EVENT := "COMMONS_HEARING_OPENED"
const HEARING_PUBLIC_TITLE := "Commons Hearing"

func build_view(snapshot: Variant, world_source: Variant, consequence_source: Variant, page: int = 0) -> Dictionary:
    if typeof(snapshot) != TYPE_DICTIONARY or page < 0:
        return _invalid()
    var state: Dictionary = snapshot
    if state.size() != 9 or state.get("mystery_state") != MYSTERY_STATE:
        return _invalid()
    var raw_history: Variant = state.get("history")
    if typeof(raw_history) != TYPE_ARRAY:
        return _invalid()
    var history: Array = raw_history
    if history.size() > MAX_HISTORY_EVENTS:
        return _invalid()
    if not _history_consistent(state, history):
        return _invalid()
    if not _valid_public_sources(world_source, consequence_source):
        return _invalid()

    var total: int = history.size()
    var page_count: int = max(1, int(ceil(float(total) / float(PAGE_SIZE))))
    if page >= page_count:
        return _invalid()
    var start_index: int = page * PAGE_SIZE
    var end_index: int = min(start_index + PAGE_SIZE, total)
    var entries: Array = []
    var lines: Array[String] = []
    for i in range(start_index, end_index):
        var event_id: String = history[i]
        var public_title: String = _public_title(event_id, world_source, consequence_source)
        if public_title.is_empty():
            return _invalid()
        entries.append({
            "index": i + 1,
            "event_id": event_id,
            "title": public_title,
        })
        lines.append("%d. %s" % [i + 1, public_title])

    return {
        "ok": true,
        "entries": entries.duplicate(true),
        "text": "\n".join(PackedStringArray(lines)),
        "count": total,
        "page": page,
        "page_count": page_count,
        "page_size": PAGE_SIZE,
        "window_start": start_index,
        "window_end": end_index,
        "has_previous": page > 0,
        "has_next": page + 1 < page_count,
        "error": "",
        "mystery_state": MYSTERY_STATE,
    }

func _history_consistent(state: Dictionary, history: Array) -> bool:
    # A recognized event ID is NOT proof it actually happened. Reconstruct the
    # published main.gd state transition contract and compare ALL current state
    # fields. This guards contradictory/deceptive snapshots but is not a
    # cryptographic attestation of an otherwise self-consistent forged object;
    # the eventual fan-in must supply genuine SessionState.snapshot() only.
    for key in ["record_read", "trace_inspected", "deferred_truth", "negotiation_open", "completed"]:
        if typeof(state.get(key)) != TYPE_BOOL:
            return false
    if typeof(state.get("commitment")) != TYPE_STRING or typeof(state.get("outcome")) != TYPE_STRING:
        return false
    var replay := {
        "record_read": false,
        "trace_inspected": false,
        "deferred_truth": false,
        "negotiation_open": false,
        "commitment": "",
        "completed": false,
        "outcome": "",
    }
    for event in history:
        if typeof(event) != TYPE_STRING:
            return false
        match String(event):
            "PUBLIC_RECORD_REVIEWED":
                replay["record_read"] = true
            "MATERIAL_TRACE_INSPECTED":
                replay["trace_inspected"] = true
            "TRUTH_CONCLUSION_DEFERRED":
                if not replay["record_read"]:
                    return false
                replay["deferred_truth"] = true
            "COMMONS_HEARING_OPENED":
                if not replay["record_read"] or (not replay["trace_inspected"] and not replay["deferred_truth"]):
                    return false
                replay["negotiation_open"] = true
            "COMMITMENT_REPAIR_PILOT", "COMMITMENT_RECORDS_FIRST", "PUBLIC_COMMITMENT_DEFERRED":
                if not replay["negotiation_open"]:
                    return false
                if event == "COMMITMENT_REPAIR_PILOT":
                    replay["commitment"] = "repair_pilot"
                elif event == "COMMITMENT_RECORDS_FIRST":
                    replay["commitment"] = "records_first"
                else:
                    replay["commitment"] = ""
                replay["negotiation_open"] = false
            "BOUNDED_REPAIR_PILOT_STARTED", "RECORDS_FIRST_PACKAGE_FILED":
                var expected_commitment := "repair_pilot" if event == "BOUNDED_REPAIR_PILOT_STARTED" else "records_first"
                if replay["commitment"] != expected_commitment:
                    return false
                replay["completed"] = true
                replay["outcome"] = event
            _:
                return false
    for key in replay:
        if state.get(key) != replay[key]:
            return false
    return true

func _valid_public_sources(world_source: Variant, consequence_source: Variant) -> bool:
    if typeof(world_source) != TYPE_OBJECT or typeof(consequence_source) != TYPE_OBJECT:
        return false
    # The contract flags alone are trivially spoofed. Only the exact reviewed
    # scripts, not a method-compatible arbitrary object/subclass, may supply
    # the title text. Actual getters remain the sole source of public strings.
    if not is_instance_valid(world_source) or not is_instance_valid(consequence_source):
        return false
    if world_source.get_script() != WorldScript or consequence_source.get_script() != ConsequenceScript:
        return false
    var world_contract: Variant = world_source.get_contract()
    var consequence_contract: Variant = consequence_source.get_contract()
    if typeof(world_contract) != TYPE_DICTIONARY or typeof(consequence_contract) != TYPE_DICTIONARY:
        return false
    if world_contract.get("mystery_state") != MYSTERY_STATE or world_contract.get("public_record_exposes_private_information", true) != false:
        return false
    if world_contract.get("presentation_mutates_game_state", true) != false:
        return false
    if consequence_contract.get("mystery_state") != MYSTERY_STATE or consequence_contract.get("deferral_is_consent_in_waiting", true) != false:
        return false
    if consequence_contract.get("direct_history_mutation", true) != false:
        return false
    return true

func _public_title(event_id: String, world_source: Variant, consequence_source: Variant) -> String:
    if WORLD_TITLES.has(event_id):
        var world_title_id: String = WORLD_TITLES[event_id]
        if not world_source.has_text(world_title_id):
            return ""
        var world_value: Variant = world_source.get_text(world_title_id)
        return String(world_value) if typeof(world_value) == TYPE_STRING else ""
    if CONSEQUENCE_TITLES.has(event_id):
        var consequence_title_id: String = CONSEQUENCE_TITLES[event_id]
        var consequence_value: Variant = consequence_source.get_text(consequence_title_id)
        return String(consequence_value) if typeof(consequence_value) == TYPE_STRING else ""
    if event_id == HEARING_OPEN_EVENT:
        # Exact already-published Commons Hearing heading, not new prose.
        return HEARING_PUBLIC_TITLE
    return ""

func _invalid() -> Dictionary:
    return {
        "ok": false,
        "entries": [],
        "text": "[EF-ROUTE-HISTORY-INVALID] Public route history unavailable.",
        "count": 0,
        "page": 0,
        "page_count": 0,
        "page_size": PAGE_SIZE,
        "window_start": 0,
        "window_end": 0,
        "has_previous": false,
        "has_next": false,
        "error": "invalid public history source or state",
        "mystery_state": MYSTERY_STATE,
    }
