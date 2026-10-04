extends RefCounted

const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"

const REQUIRED_FIELDS := [
    "record_read",
    "trace_inspected",
    "deferred_truth",
    "negotiation_open",
    "commitment",
    "completed",
    "outcome",
    "mystery_state",
    "history",
]

const ALLOWED_COMMITMENTS := ["", "repair_pilot", "records_first"]

func build_view(state: Dictionary, station_metadata: Dictionary = {}) -> Dictionary:
    var validation_error := _validate_state(state)
    if not validation_error.is_empty():
        return _fail_closed(validation_error)

    var record_read := bool(state["record_read"])
    var trace_inspected := bool(state["trace_inspected"])
    var deferred_truth := bool(state["deferred_truth"])
    var negotiation_open := bool(state["negotiation_open"])
    var commitment := String(state["commitment"])
    var completed := bool(state["completed"])
    var outcome := String(state["outcome"])
    var investigation_ready := record_read and (trace_inspected or deferred_truth)

    var archive_title := _station_title(station_metadata, "public_record", "Archive Ledger")
    var trace_title := _station_title(station_metadata, "material_trace", "Material Trace")
    var defer_title := _station_title(station_metadata, "defer_conclusion", "Defer Conclusion")
    var hearing_title := _station_title(station_metadata, "commons_hearing", "Commons Hearing")
    var project_title := _station_title(station_metadata, "project_table", "Project Table")

    var phase := ""
    var objective := ""

    if completed:
        phase = "COMPLETE"
        objective = "Loop complete: %s." % outcome
    elif not record_read:
        phase = "INVESTIGATE_RECORD"
        objective = "Investigate: reach %s and review the public record." % archive_title
    elif not investigation_ready:
        phase = "INVESTIGATE_CORROBORATE_OR_DEFER"
        objective = "Investigate: inspect %s OR explicitly use %s." % [trace_title, defer_title]
    elif negotiation_open:
        phase = "HEARING_OPEN"
        objective = "%s: [1] repair pilot · [2] records-first · [3] defer commitment." % hearing_title
    elif commitment.is_empty():
        phase = "GO_TO_HEARING"
        objective = "Negotiate: reach %s and open the hearing." % hearing_title
    else:
        phase = "GO_TO_PROJECT_TABLE"
        objective = "Commit: reach %s to complete the bounded loop." % project_title

    return {
        "valid": true,
        "phase": phase,
        "objective": objective,
        "status": _status_line(record_read, trace_inspected, deferred_truth, commitment),
        "mystery_state": MYSTERY_STATE,
    }

func _validate_state(state: Dictionary) -> String:
    for field in REQUIRED_FIELDS:
        if not state.has(field):
            return "missing required field: %s" % field

    for field in ["record_read", "trace_inspected", "deferred_truth", "negotiation_open", "completed"]:
        if typeof(state[field]) != TYPE_BOOL:
            return "field %s must be bool" % field

    for field in ["commitment", "outcome", "mystery_state"]:
        if typeof(state[field]) != TYPE_STRING:
            return "field %s must be String" % field

    if typeof(state["history"]) != TYPE_ARRAY:
        return "field history must be Array"

    var mystery_state := String(state["mystery_state"])
    if mystery_state != MYSTERY_STATE:
        return "mystery_state must remain %s" % MYSTERY_STATE

    var commitment := String(state["commitment"])
    if not ALLOWED_COMMITMENTS.has(commitment):
        return "unsupported commitment: %s" % commitment

    var record_read := bool(state["record_read"])
    var trace_inspected := bool(state["trace_inspected"])
    var deferred_truth := bool(state["deferred_truth"])
    var negotiation_open := bool(state["negotiation_open"])
    var completed := bool(state["completed"])
    var outcome := String(state["outcome"])
    var investigation_ready := record_read and (trace_inspected or deferred_truth)

    if negotiation_open and not investigation_ready:
        return "negotiation_open requires an investigation-ready state"
    if negotiation_open and not commitment.is_empty():
        return "negotiation_open cannot coexist with a commitment"
    if not commitment.is_empty() and not investigation_ready:
        return "commitment requires an investigation-ready state"
    if completed and negotiation_open:
        return "completed state cannot keep negotiation open"

    if completed:
        if commitment.is_empty():
            return "completed state requires a commitment"
        if commitment == "repair_pilot" and outcome != "BOUNDED_REPAIR_PILOT_STARTED":
            return "repair_pilot completion requires BOUNDED_REPAIR_PILOT_STARTED"
        if commitment == "records_first" and outcome != "RECORDS_FIRST_PACKAGE_FILED":
            return "records_first completion requires RECORDS_FIRST_PACKAGE_FILED"
    elif not outcome.is_empty():
        return "non-completed state cannot expose a completion outcome"

    return ""

func _status_line(record_read: bool, trace_inspected: bool, deferred_truth: bool, commitment: String) -> String:
    return "Record:%s  Trace:%s  Deferred truth:%s  Commitment:%s  Mystery:%s" % [
        _flag(record_read),
        _flag(trace_inspected),
        _flag(deferred_truth),
        commitment if not commitment.is_empty() else "none",
        MYSTERY_STATE,
    ]

func _fail_closed(reason: String) -> Dictionary:
    return {
        "valid": false,
        "phase": "INVALID_STATE",
        "objective": "[EF-HUD-STATE] Invalid bounded session state: %s. Progress is not inferred." % reason,
        "status": "Record:unknown  Trace:unknown  Deferred truth:unknown  Commitment:unknown  Mystery:%s" % MYSTERY_STATE,
        "mystery_state": MYSTERY_STATE,
        "error": reason,
    }

func _station_title(station_metadata: Dictionary, station_id: String, fallback: String) -> String:
    if not station_metadata.has(station_id):
        return fallback
    var raw_entry: Variant = station_metadata[station_id]
    if typeof(raw_entry) != TYPE_DICTIONARY:
        return fallback
    var entry := raw_entry as Dictionary
    var raw_title: Variant = entry.get("title", "")
    if typeof(raw_title) != TYPE_STRING:
        return fallback
    var title := String(raw_title).strip_edges()
    return title if not title.is_empty() else fallback

func _flag(value: bool) -> String:
    return "yes" if value else "no"
