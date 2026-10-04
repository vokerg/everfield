extends SceneTree

const Assembler = preload("res://components/playable_presentation/playable_presentation.gd")
const World = preload("res://components/old_works_world/old_works_world_presentation.gd")
const Hearing = preload("res://components/commons_hearing/commons_hearing_presentation.gd")
const Consequences = preload("res://components/commitment_consequences/commitment_consequence_presentation.gd")
class MutatedHearing:
    extends RefCounted
    var source: Variant
    var target_beat: String
    var target_key: String
    var replacement: Variant
    var remove_key: bool

    func _init(base_source: Variant, beat_id: String, key: String, value: Variant, erase_key: bool = false) -> void:
        source = base_source
        target_beat = beat_id
        target_key = key
        replacement = value
        remove_key = erase_key

    func get_participant(id: String) -> Dictionary:
        return source.get_participant(id)

    func get_contract() -> Dictionary:
        return source.get_contract()

    func get_line(id: String) -> Dictionary:
        var beat: Dictionary = source.get_line(id)
        if id == target_beat:
            if remove_key:
                beat.erase(target_key)
            else:
                beat[target_key] = replacement
        return beat

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var world := World.new()
    var hearing := Hearing.new()
    var consequences := Consequences.new()
    var assembled := Assembler.new(world, hearing, consequences)
    var original_world: Dictionary = world.get_contract()
    var original_hearing: Dictionary = hearing.get_contract()
    var original_consequences: Dictionary = consequences.get_contract()

    var intro: Dictionary = assembled.world_intro()
    _expect(intro["ok"] and intro["text"] == "%s\n%s\n%s" % [world.get_text("OW_WORLD_TITLE"), world.get_text("OW_WORLD_SUBTITLE"), world.get_text("OW_WORLD_ENTRY")], "world intro exactly matches published controller composition")
    var stations: Array = ["public_record", "material_trace", "defer_conclusion"]
    for id in stations:
        var view: Dictionary = assembled.old_works_station(id)
        var source_station: Dictionary = world.get_station(id)
        var expected: Array = [world.get_text(source_station["title_id"]), world.get_text(source_station["prompt_id"])]
        for body_id in source_station.get("body_ids", []):
            expected.append(world.get_text(body_id))
        for key in ["exit_id", "result_id"]:
            if source_station.has(key):
                expected.append(world.get_text(source_station[key]))
        _expect(view["ok"] and view["text"] == "\n".join(PackedStringArray(expected)), "exact source parity for station %s" % id)

    var record: Dictionary = assembled.old_works_station("public_record")
    _expect(record["text"].contains("accounts, not findings"), "archive remains contested public record")
    _expect(not record["text"].contains("anwen_contested_record_provenance_gap"), "no private provenance exposed")
    _expect(assembled.old_works_station("material_trace")["text"].contains("does not identify a single cause"), "trace remains non-discriminating")
    _expect(assembled.old_works_station("defer_conclusion")["text"].contains("without pretending"), "truth deferral remains explicit")

    var opening: Dictionary = assembled.hearing_opening()
    _expect(opening["ok"] and opening["text"].contains("Maelin Sor — Before we choose a route") and opening["text"].contains("Selka Vey — Then keep the choice bounded"), "hearing opening uses actual reviewed speakers")
    for route in ["repair_pilot", "records_first", "defer"]:
        var event: String = {"repair_pilot":"COMMITMENT_REPAIR_PILOT", "records_first":"COMMITMENT_RECORDS_FIRST", "defer":"PUBLIC_COMMITMENT_DEFERRED"}[route]
        var dialogue: Dictionary = assembled.hearing_route(route)
        var outcome: Dictionary = assembled.consequence(event)
        var combined: Dictionary = assembled.hearing_and_consequence(route, event)
        _expect(dialogue["ok"] and outcome["ok"] and combined["ok"], "bounded hearing route %s assembles" % route)
        _expect(combined["text"] == "%s\n\n%s" % [dialogue["text"], outcome["text"]], "route %s keeps exact double-newline separation" % route)
    _expect(assembled.hearing_route("defer")["text"].contains("No assent is recorded"), "no presumed consent")
    _expect(assembled.consequence("PUBLIC_COMMITMENT_DEFERRED")["text"].contains("not approval waiting to happen"), "deferral stays nonconsenting")
    _expect(assembled.consequence("BOUNDED_REPAIR_PILOT_STARTED")["text"].contains("Work beyond the pilot remains uncommitted"), "repair completion is bounded")
    _expect(assembled.consequence("RECORDS_FIRST_PACKAGE_FILED")["text"].contains("documentation does not convert either account into a finding"), "records completion cannot select a winner")

    var escaped_lines: Array = record["lines"]
    escaped_lines.clear()
    _expect(assembled.old_works_station("public_record")["lines"].size() > 0, "returned arrays cannot mutate source output")
    _expect(world.get_contract() == original_world and hearing.get_contract() == original_hearing and consequences.get_contract() == original_consequences, "injected public providers remain unchanged")
    _expect(assembled.get_contract()["mystery_state"] == "UNKNOWN_BY_DESIGN" and not assembled.get_contract()["deferral_is_consent"], "no mystery closure or implied consent")
    _expect(not assembled.old_works_station("")["ok"], "empty station ID must not select world intro")
    # Test actual route composition with provider data altered at one immutable beat.
    # The reviewed provider returns deep copies, so these cases cannot mutate it.
    var malformed_routes: Array = [
        {"route":"repair_pilot", "beat":"OW_HEARING_REPAIR_MAELIN_01", "key":"speaker_ref", "value":"CHAR:selka_vey", "label":"repair speaker swap"},
        {"route":"records_first", "beat":"OW_HEARING_RECORDS_SELKA_01", "key":"speaker_ref", "value":"CHAR:maelin_sor", "label":"records speaker swap"},
        {"route":"repair_pilot", "beat":"OW_HEARING_REPAIR_SELKA_01", "key":"phase", "value":"DEFER_NONALIGNMENT", "label":"repair phase swap"},
        {"route":"defer", "beat":"OW_HEARING_DEFER_MAELIN_01", "key":"phase", "value":"ROUTE_POSITION", "label":"deferral phase swap"},
        {"route":"records_first", "beat":"OW_HEARING_RECORDS_MAELIN_01", "key":"phase", "value":null, "remove":true, "label":"missing phase"},
        {"route":"defer", "beat":"OW_HEARING_DEFER_SELKA_01", "key":"route_scope", "value":"repair_pilot", "label":"wrong route scope"},
    ]
    for case in malformed_routes:
        var altered := MutatedHearing.new(hearing, case["beat"], case["key"], case["value"], case.get("remove", false))
        var route_view: Dictionary = Assembler.new(world, altered, consequences).hearing_route(case["route"])
        _expect(not route_view.get("ok", false), "malformed %s fails closed" % case["label"])
    _expect(hearing.get_contract() == original_hearing, "malformed provider injection leaves original contract unchanged")
    _expect(not assembled.old_works_station("private_record")["ok"], "unknown or private station fails closed")
    _expect(not assembled.hearing_route("forced")["ok"], "unknown hearing route fails closed")
    _expect(not assembled.consequence("BOGUS")["ok"], "unknown consequence fails closed")
    _expect(not assembled.hearing_and_consequence("defer", "COMMITMENT_REPAIR_PILOT")["ok"], "mismatched consequence and consent fail closed")
    _expect(not Assembler.new(RefCounted.new(), hearing, consequences).world_intro()["ok"], "missing world methods fail closed")
    _expect(not Assembler.new(world, RefCounted.new(), consequences).hearing_opening()["ok"], "missing hearing methods fail closed")
    _expect(not Assembler.new(world, hearing, RefCounted.new()).consequence("PUBLIC_COMMITMENT_DEFERRED")["ok"], "missing consequence methods fail closed")
    _finish()

func _expect(ok: bool, message: String) -> void:
    if ok:
        print("[EF-PRESENTATION][PASS] %s" % message)
    else:
        failures.append(message)
        push_error("[EF-PRESENTATION][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_PLAYABLE_PRESENTATION_SMOKE_PASS")
        quit(0)
    else:
        push_error("EVERFIELD_PLAYABLE_PRESENTATION_SMOKE_FAIL: %s" % failures)
        quit(1)
