class_name EverfieldSessionState
extends RefCounted

const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"

const ALLOWED_HISTORY_EVENTS := {
    "PUBLIC_RECORD_REVIEWED": true,
    "MATERIAL_TRACE_INSPECTED": true,
    "TRUTH_CONCLUSION_DEFERRED": true,
    "COMMONS_HEARING_OPENED": true,
    "COMMITMENT_REPAIR_PILOT": true,
    "COMMITMENT_RECORDS_FIRST": true,
    "PUBLIC_COMMITMENT_DEFERRED": true,
    "BOUNDED_REPAIR_PILOT_STARTED": true,
    "RECORDS_FIRST_PACKAGE_FILED": true,
}

const ALLOWED_COMMITMENTS := ["", "repair_pilot", "records_first"]
const ALLOWED_OUTCOMES := ["", "BOUNDED_REPAIR_PILOT_STARTED", "RECORDS_FIRST_PACKAGE_FILED"]

var _state: Dictionary = {}

func _init() -> void:
    reset()

func reset() -> void:
    _state = {
        "record_read": false,
        "trace_inspected": false,
        "deferred_truth": false,
        "negotiation_open": false,
        "commitment": "",
        "completed": false,
        "outcome": "",
        "mystery_state": MYSTERY_STATE,
        "history": [],
    }

func snapshot() -> Dictionary:
    return _state.duplicate(true)

func set_field(field_name: String, value: Variant) -> bool:
    match field_name:
        "record_read", "trace_inspected", "deferred_truth", "negotiation_open", "completed":
            if typeof(value) != TYPE_BOOL:
                return _reject("Boolean field %s received non-boolean value." % field_name)
            _state[field_name] = value
        "commitment":
            if typeof(value) != TYPE_STRING or not ALLOWED_COMMITMENTS.has(String(value)):
                return _reject("Unsupported commitment value: %s" % String(value))
            _state[field_name] = String(value)
        "outcome":
            if typeof(value) != TYPE_STRING or not ALLOWED_OUTCOMES.has(String(value)):
                return _reject("Unsupported outcome value: %s" % String(value))
            _state[field_name] = String(value)
        "mystery_state":
            if typeof(value) != TYPE_STRING or String(value) != MYSTERY_STATE:
                return _reject("Mystery state is immutable and must remain %s." % MYSTERY_STATE)
            _state[field_name] = MYSTERY_STATE
        "history":
            return _reject("History is append-only through append_history().")
        _:
            return _reject("Unknown bounded-state field: %s" % field_name)

    _state["mystery_state"] = MYSTERY_STATE
    return true

func append_history(event_id: String) -> bool:
    if not ALLOWED_HISTORY_EVENTS.has(event_id):
        return _reject("Unsupported history event: %s" % event_id)

    var history: Array = _state["history"]
    history.append(event_id)
    _state["mystery_state"] = MYSTERY_STATE
    print("[EVERFIELD][SESSION_STATE] %s" % event_id)
    return true

func get_contract() -> Dictionary:
    return {
        "mystery_state": MYSTERY_STATE,
        "history_ordered": true,
        "snapshot_deep_copy": true,
        "transient_session_only": true,
        "filesystem_io": false,
        "save_load": false,
        "durable_persistence": false,
        "canon_authority": false,
    }

func _reject(message: String) -> bool:
    printerr("[EVERFIELD][SESSION_STATE][ERROR] %s" % message)
    return false
