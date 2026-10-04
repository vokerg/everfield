extends RefCounted

func compose(source: Variant, station_id: String = "") -> Dictionary:
    if source == null or not source.has_method("get_contract") or not source.has_method("get_station") or not source.has_method("has_text") or not source.has_method("get_text"):
        return _error()
    var contract: Variant = source.get_contract()
    if typeof(contract) != TYPE_DICTIONARY or contract.get("mystery_state") != "UNKNOWN_BY_DESIGN" or contract.get("public_record_exposes_private_information", true):
        return _error()
    var ids: Array = ["OW_WORLD_TITLE", "OW_WORLD_SUBTITLE", "OW_WORLD_ENTRY"]
    if not station_id.is_empty():
        if not ["public_record", "material_trace", "defer_conclusion"].has(station_id):
            return _error()
        var raw: Variant = source.get_station(station_id)
        if typeof(raw) != TYPE_DICTIONARY:
            return _error()
        var station: Dictionary = raw
        ids = [station.get("title_id"), station.get("prompt_id")]
        var bodies: Variant = station.get("body_ids", [])
        if typeof(bodies) != TYPE_ARRAY:
            return _error()
        ids.append_array(bodies)
        for key in ["exit_id", "result_id"]:
            if station.has(key):
                ids.append(station[key])
    var lines: Array = []
    for id in ids:
        if typeof(id) != TYPE_STRING or String(id).is_empty() or not source.has_text(id):
            return _error()
        var value: Variant = source.get_text(id)
        if typeof(value) != TYPE_STRING or String(value).is_empty():
            return _error()
        lines.append(value)
    return {"ok": true, "text": "\n".join(PackedStringArray(lines)), "lines": lines.duplicate(true), "error": ""}

func _error() -> Dictionary:
    return {"ok": false, "text": "[EF-PRESENTATION-INVALID] Invalid public Old Works text.", "lines": [], "error": "invalid public world"}
