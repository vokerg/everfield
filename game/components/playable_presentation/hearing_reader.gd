extends RefCounted

const ROUTE_BEATS := {
    "repair_pilot": ["OW_HEARING_REPAIR_MAELIN_01", "OW_HEARING_REPAIR_SELKA_01"],
    "records_first": ["OW_HEARING_RECORDS_MAELIN_01", "OW_HEARING_RECORDS_SELKA_01"],
    "defer": ["OW_HEARING_DEFER_MAELIN_01", "OW_HEARING_DEFER_SELKA_01"],
}

func compose(source: Variant, route: String = "") -> Dictionary:
    if source == null or not source.has_method("get_participant") or not source.has_method("get_line") or not source.has_method("get_contract"):
        return _bad("missing public hearing source")
    var contract: Variant = source.get_contract()
    if typeof(contract) != TYPE_DICTIONARY or contract.get("mystery_state") != "UNKNOWN_BY_DESIGN" or contract.get("deferral_is_consent_in_waiting", true) != false or contract.get("private_information_required", true) != false:
        return _bad("invalid hearing contract")
    var maelin: Dictionary = _participant(source, "OW_HEARING_PARTICIPANT_MAELIN_01", "CHAR:maelin_sor")
    var selka: Dictionary = _participant(source, "OW_HEARING_PARTICIPANT_SELKA_01", "CHAR:selka_vey")
    if maelin.is_empty() or selka.is_empty():
        return _bad("missing reviewed participants")
    var lines: Array = []
    if route.is_empty():
        var a: Dictionary = _line(source, "OW_HEARING_OPEN_MAELIN_01", "CHAR:maelin_sor", "OPENING")
        var b: Dictionary = _line(source, "OW_HEARING_OPEN_SELKA_01", "CHAR:selka_vey", "OPENING")
        if a.is_empty() or b.is_empty():
            return _bad("invalid opening beats")
        lines = ["Commons Hearing", "%s — %s" % [maelin["display_name"], a["text"]], "%s — %s" % [selka["display_name"], b["text"]], "Refusal, deferral, and nonalignment remain legal outcomes."]
    else:
        if not ROUTE_BEATS.has(route):
            return _bad("unknown hearing route")
        lines = ["Commons Hearing — %s" % route.replace("_", " ")]
        for id in ROUTE_BEATS[route]:
            var raw: Variant = source.get_line(id)
            if typeof(raw) != TYPE_DICTIONARY:
                return _bad("invalid route beat")
            var beat: Dictionary = raw
            var who := ""
            match beat.get("speaker_ref", ""):
                "CHAR:maelin_sor":
                    who = String(maelin["display_name"])
                "CHAR:selka_vey":
                    who = String(selka["display_name"])
            if who.is_empty() or beat.get("route_scope") != route or typeof(beat.get("text")) != TYPE_STRING or String(beat["text"]).is_empty():
                return _bad("unknown speaker or missing route beat")
            lines.append("%s — %s" % [who, beat["text"]])
    return {"ok": true, "text": "\n".join(PackedStringArray(lines)), "lines": lines.duplicate(true), "error": ""}

func _participant(source: Variant, id: String, ref: String) -> Dictionary:
    var raw: Variant = source.get_participant(id)
    if typeof(raw) != TYPE_DICTIONARY:
        return {}
    var value: Dictionary = raw
    if value.get("character_ref") != ref or typeof(value.get("display_name")) != TYPE_STRING or String(value["display_name"]).is_empty():
        return {}
    return value

func _line(source: Variant, id: String, ref: String, phase: String) -> Dictionary:
    var raw: Variant = source.get_line(id)
    if typeof(raw) != TYPE_DICTIONARY:
        return {}
    var value: Dictionary = raw
    if value.get("speaker_ref") != ref or value.get("phase") != phase or typeof(value.get("text")) != TYPE_STRING or String(value["text"]).is_empty():
        return {}
    return value

func _bad(reason: String) -> Dictionary:
    return {"ok": false, "text": "[EF-PRESENTATION-INVALID] %s" % reason, "lines": [], "error": reason}
