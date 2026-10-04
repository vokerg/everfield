extends RefCounted

func compose(source: Variant, station_id: String = "") -> Dictionary:
    if source == null or not source.has_method("has_text") or not source.has_method("get_text") or not source.has_method("get_station") or not source.has_method("get_contract"):
        return _bad("missing public world provider")
    var contract: Variant = source.get_contract()
    if typeof(contract) != TYPE_DICTIONARY or contract.get("mystery_state") != "UNKNOWN_BY_DESIGN" or contract.get("public_record_exposes_private_information", true) != false:
        return _bad("invalid public world contract")
    var ids: Array = []
    if station_id.is_empty():
        ids = ["OW_WORLD_TITLE", "OW_WORLD_SUBTITLE", "OW_WORLD_ENTRY"]
    else:
        if not ["public_record", "material_trace", "defer_conclusion"].has(station_id):
            return _bad("unknown public station")
        var raw: Variant = source.get_station(station_id)
        if typeof(raw) != TYPE_DICTIONARY or raw.is_empty():
            return _bad("invalid station data")
        var station: Dictionary = raw
        for key in ["title_id", "prompt_id"]:
            if typeof(station.get(key)) != TYPE_STRING or String(station[key]).is_empty():
                return _bad("invalid station label")
            ids.append(station[key])
        var body_ids: Variant = station.get("body_ids", [])
        if typeof(body_ids) != TYPE_ARRAY:
            return _bad("invalid station body IDs")
        ids.append_array(body_ids)
        for key in ["exit_id", "result_id"]:
            if station.has(key):
                ids.append(station[key])
    var lines: Array = []
    for id in ids:
        if typeof(id) != TYPE_STRING or String(id).is_empty() or not source.has_text(id):
            return _bad("invalid public text ID")
        var value: Variant = source.get_text(id)
        if typeof(value) != TYPE_STRING or String(value).is_empty():
            return _bad("missing public text")
        lines.append(value)
    return {"ok": true, "text": "\n".join(lines), "lines": lines.duplicate(true), "error": ""}

func _bad(reason: String) -> Dictionary:
    return {"ok": false, "text": "[EF-PRESENTATION-INVALID] %s" % reason, "lines": [], "error": reason}
