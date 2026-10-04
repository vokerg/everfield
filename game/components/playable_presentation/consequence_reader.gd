extends RefCounted

const EVENTS := {
    "COMMITMENT_REPAIR_PILOT": ["repair_pilot", "selection"],
    "COMMITMENT_RECORDS_FIRST": ["records_first", "selection"],
    "PUBLIC_COMMITMENT_DEFERRED": ["defer", "selection"],
    "BOUNDED_REPAIR_PILOT_STARTED": ["repair_pilot", "completion"],
    "RECORDS_FIRST_PACKAGE_FILED": ["records_first", "completion"],
}

func compose(source: Variant, event_id: String) -> Dictionary:
    if not EVENTS.has(event_id):
        return _bad("unknown public consequence")
    if source == null or not source.has_method("get_event") or not source.has_method("get_text") or not source.has_method("get_contract"):
        return _bad("missing consequence provider")
    var contract: Variant = source.get_contract()
    if typeof(contract) != TYPE_DICTIONARY or contract.get("mystery_state") != "UNKNOWN_BY_DESIGN" or contract.get("deferral_is_consent_in_waiting", true) != false:
        return _bad("invalid consequence contract")
    var raw: Variant = source.get_event(event_id)
    if typeof(raw) != TYPE_DICTIONARY:
        return _bad("malformed public event")
    var event: Dictionary = raw
    var scope: Array = EVENTS[event_id]
    var ids: Variant = event.get("ids")
    if event.get("route") != scope[0] or event.get("phase") != scope[1] or typeof(ids) != TYPE_ARRAY or ids.is_empty():
        return _bad("invalid consequence scope")
    var lines: Array = []
    for id in ids:
        if typeof(id) != TYPE_STRING or String(id).is_empty():
            return _bad("invalid consequence text ID")
        var value: Variant = source.get_text(id)
        if typeof(value) != TYPE_STRING or String(value).is_empty():
            return _bad("missing consequence line")
        lines.append(value)
    return {"ok": true, "text": "\n".join(lines), "lines": lines.duplicate(true), "error": ""}

func _bad(reason: String) -> Dictionary:
    return {"ok": false, "text": "[EF-PRESENTATION-INVALID] %s" % reason, "lines": [], "error": reason}
