extends SceneTree

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var script := load("res://components/commons_hearing/commons_hearing_presentation.gd")
    _expect(script != null, "Commons Hearing presentation component loads")
    if script == null:
        _finish()
        return

    var presentation: Variant = script.new()
    _expect(presentation.has_method("get_participant"), "participant lookup API exists")
    _expect(presentation.has_method("get_line"), "dialogue lookup API exists")
    _expect(presentation.has_method("get_lines_for_route"), "route lookup API exists")
    _expect(presentation.has_method("get_contract"), "invariant contract API exists")

    var maelin: Dictionary = presentation.get_participant("OW_HEARING_PARTICIPANT_MAELIN_01")
    _expect(maelin.get("character_ref", "") == "CHAR:maelin_sor", "Maelin participant identity is exact")
    _expect(maelin.get("hearing_role", "") == "AFFECTED_BURDEN_VOICE", "Maelin bounded hearing role is exact")
    _expect(maelin.get("representation_asserted", true) == false, "Maelin presentation grants no representation")

    var selka: Dictionary = presentation.get_participant("OW_HEARING_PARTICIPANT_SELKA_01")
    _expect(selka.get("character_ref", "") == "CHAR:selka_vey", "Selka participant identity is exact")
    _expect(selka.get("hearing_role", "") == "BOUNDED_PROCEDURE_VOICE", "Selka bounded hearing role is exact")
    _expect(selka.get("office_asserted", true) == false, "Selka presentation grants no office")

    var opening: Dictionary = presentation.get_line("OW_HEARING_OPEN_MAELIN_01")
    _expect(opening.get("text", "") == "Before we choose a route, name who carries the work if the Old Works fail again.", "Maelin opening line is exact")

    var defer_line: Dictionary = presentation.get_line("OW_HEARING_DEFER_SELKA_01")
    _expect(defer_line.get("phase", "") == "DEFER_NONALIGNMENT", "deferral line remains explicit nonalignment")
    _expect(defer_line.get("text", "") == "No assent is recorded. Reopen the hearing only when someone chooses to.", "Selka deferral line is exact")

    var refusal: Dictionary = presentation.get_line("OW_HEARING_REFUSE_MAELIN_01")
    _expect(refusal.get("phase", "") == "REFUSAL", "refusal remains an explicit legal beat")
    _expect(refusal.get("hidden_gate", true) == false, "refusal is not a hidden progression gate")
    _expect(refusal.get("consent_effect", "unexpected") == "NONE", "refusal grants no consent effect")

    var repair_lines: Array = presentation.get_lines_for_route("repair_pilot")
    _expect(_contains_beat(repair_lines, "OW_HEARING_REPAIR_MAELIN_01"), "repair route includes Maelin burden position")
    _expect(_contains_beat(repair_lines, "OW_HEARING_REPAIR_SELKA_01"), "repair route includes Selka bounded-procedure position")
    _expect(_contains_beat(repair_lines, "OW_HEARING_REFUSE_MAELIN_01"), "refusal remains available on repair route")

    var defer_lines: Array = presentation.get_lines_for_route("defer")
    _expect(_contains_beat(defer_lines, "OW_HEARING_DEFER_MAELIN_01"), "defer route includes Maelin nonalignment beat")
    _expect(_contains_beat(defer_lines, "OW_HEARING_DEFER_SELKA_01"), "defer route includes Selka nonalignment beat")

    var contract: Dictionary = presentation.get_contract()
    _expect(contract.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "fragmentation mystery remains UNKNOWN_BY_DESIGN")
    _expect(contract.get("participant_count", 0) == 2, "exactly two reviewed slice participants are exposed")
    _expect(contract.get("dialogue_beat_count", 0) == 10, "exactly ten reviewed dialogue beats are exposed")
    _expect(contract.get("deferral_is_consent_in_waiting", true) == false, "deferral is not consent in waiting")
    _expect(contract.get("direct_relationship_mutation", true) == false, "presentation does not mutate relationships")
    _expect(contract.get("universal_popularity_or_relationship_scalar", true) == false, "no universal popularity or relationship scalar is introduced")
    _expect(contract.get("private_information_required", true) == false, "private provenance gap is not required")
    _expect(contract.get("presentation_mutates_game_state", true) == false, "presentation component is inert")
    _expect(contract.get("presentation_grants_canonical_authority", true) == false, "presentation grants no canonical authority")

    _expect(presentation.get_participant("OW_HEARING_PARTICIPANT_UNKNOWN").is_empty(), "unknown participant fails closed")
    _expect(presentation.get_line("OW_HEARING_UNKNOWN_LINE").is_empty(), "unknown dialogue beat fails closed")
    _expect(presentation.get_lines_for_route("unknown_route").is_empty(), "unknown route fails closed")

    _finish()

func _contains_beat(lines: Array, beat_id: String) -> bool:
    for line in lines:
        if line is Dictionary and String(line.get("beat_id", "")) == beat_id:
            return true
    return false

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-COMMONS-HEARING-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-COMMONS-HEARING-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_COMMONS_HEARING_PRESENTATION_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_COMMONS_HEARING_PRESENTATION_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
