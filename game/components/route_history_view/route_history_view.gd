extends RefCounted

# Read-only projection of already-approved public session events.
# The scene owns display/input; this model never changes SessionState or prose.
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"
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

func build_view(snapshot: Variant, world_source: Variant, consequence_source: Variant) -> Dictionary:
    if typeof(snapshot) != TYPE_DICTIONARY:
        return _invalid()
    var state: Dictionary = snapshot
    if state.get("mystery_state") != MYSTERY_STATE:
        return _invalid()
    var raw_history: Variant = state.get("history")
    if typeof(raw_history) != TYPE_ARRAY:
        return _invalid()
    if not _valid_public_sources(world_source, consequence_source):
        return _invalid()

    var entries: Array = []
    var lines: Array[String] = []
    for event in raw_history:
        if typeof(event) != TYPE_STRING:
            return _invalid()
        var event_id: String = event
        var public_title: String = _public_title(event_id, world_source, consequence_source)
        if public_title.is_empty():
            # Never echo unknown or private event values to the player.
            return _invalid()
        entries.append({
            "index": entries.size() + 1,
            "event_id": event_id,
            "title": public_title,
        })
        lines.append("%d. %s" % [entries.size(), public_title])

    return {
        "ok": true,
        "entries": entries.duplicate(true),
        "text": "\n".join(PackedStringArray(lines)),
        "count": entries.size(),
        "error": "",
        "mystery_state": MYSTERY_STATE,
    }

func _valid_public_sources(world_source: Variant, consequence_source: Variant) -> bool:
    if typeof(world_source) != TYPE_OBJECT or typeof(consequence_source) != TYPE_OBJECT:
        return false
    if not world_source.has_method("get_contract") or not world_source.has_method("has_text") or not world_source.has_method("get_text"):
        return false
    if not consequence_source.has_method("get_contract") or not consequence_source.has_method("get_text"):
        return false

    var world_contract: Variant = world_source.get_contract()
    var consequence_contract: Variant = consequence_source.get_contract()
    if typeof(world_contract) != TYPE_DICTIONARY or typeof(consequence_contract) != TYPE_DICTIONARY:
        return false
    if world_contract.get("mystery_state") != MYSTERY_STATE or world_contract.get("public_record_exposes_private_information", true) != false:
        return false
    if consequence_contract.get("mystery_state") != MYSTERY_STATE or consequence_contract.get("deferral_is_consent_in_waiting", true) != false:
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
        # Exact already-published heading from the Commons Hearing reader.
        return HEARING_PUBLIC_TITLE
    return ""

func _invalid() -> Dictionary:
    return {
        "ok": false,
        "entries": [],
        "text": "[EF-ROUTE-HISTORY-INVALID] Public route history unavailable.",
        "count": 0,
        "error": "invalid public history source or state",
        "mystery_state": MYSTERY_STATE,
    }
