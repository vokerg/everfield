extends SceneTree

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var packed := load("res://main.tscn") as PackedScene
    _expect(packed != null, "main scene loads")
    if packed == null:
        _finish()
        return

    var game: Variant = packed.instantiate()
    get_root().add_child(game)
    await process_frame

    _expect(game.has_method("interact_with"), "interaction API exists")
    _expect(game.has_method("choose_commitment"), "commitment API exists")
    _expect(game.has_method("get_game_state"), "state diagnostics API exists")
    _expect(game.get_node_or_null("Player") != null, "controllable player node exists")

    _expect(not game.interact_with("commons_hearing"), "negotiation fails closed before investigation")
    _expect(game.interact_with("public_record"), "public record route works")
    _expect(game.interact_with("material_trace"), "material trace route works")
    _expect(game.interact_with("commons_hearing"), "negotiation opens after evidence")
    _expect(game.choose_commitment("repair_pilot"), "repair-pilot commitment works")
    _expect(game.interact_with("project_table"), "repair-pilot loop closes")

    var repair_state: Dictionary = game.get_game_state()
    _expect(repair_state.get("completed", false) == true, "repair route marks loop complete")
    _expect(repair_state.get("outcome", "") == "BOUNDED_REPAIR_PILOT_STARTED", "repair route has exact bounded outcome")
    _expect(repair_state.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "repair route does not settle world mystery")
    var repair_history: Array = repair_state.get("history", [])
    _expect(repair_history.size() >= 5, "repair route leaves observable state history")

    game.reset_slice()
    _expect(game.interact_with("public_record"), "record can be replayed after reset")
    _expect(game.interact_with("defer_conclusion"), "explicit defer is a legal investigation alternative")
    _expect(game.interact_with("commons_hearing"), "defer route still reaches negotiation")
    _expect(game.choose_commitment("records_first"), "records-first commitment works")
    _expect(game.interact_with("project_table"), "records-first loop closes")

    var records_state: Dictionary = game.get_game_state()
    _expect(records_state.get("completed", false) == true, "records-first route marks loop complete")
    _expect(records_state.get("outcome", "") == "RECORDS_FIRST_PACKAGE_FILED", "records-first route has exact bounded outcome")
    _expect(records_state.get("trace_inspected", true) == false, "records-first defer route does not fabricate material-trace evidence")
    _expect(records_state.get("deferred_truth", false) == true, "records-first defer route preserves explicit truth deferral")
    _expect(records_state.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "records-first route does not settle world mystery")

    game.reset_slice()
    _expect(not game.choose_commitment("repair_pilot"), "commitment fails closed before negotiation")
    _expect(not game.interact_with("unknown_station"), "unknown interaction surface fails visibly")

    _finish()

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_SMOKE_PASS")
        quit(0)
        return

    push_error("EVERFIELD_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
