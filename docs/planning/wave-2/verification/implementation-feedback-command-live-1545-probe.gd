extends SceneTree

# Fresh verifier-owned adversarial probe. Loaded into frozen producer checkout only in
# an ephemeral GitHub Actions workspace; never added to the producer PR or main.
var failures: Array[String] = []
var checks: int = 0

func _init() -> void:
    call_deferred("_run")

func _check(ok: bool, message: String) -> void:
    checks += 1
    if ok:
        print("[EF-INDEPENDENT-1575][PASS] " + message)
    else:
        failures.append(message)
        push_error("[EF-INDEPENDENT-1575][FAIL] " + message)

func _event(keycode: int, pressed: bool, echo: bool = false, physical_code: int = -1) -> void:
    var e := InputEventKey.new()
    e.keycode = keycode
    e.physical_keycode = keycode if physical_code == -1 else physical_code
    e.pressed = pressed
    e.echo = echo
    Input.parse_input_event(e)
    Input.flush_buffered_events()

func _tap(keycode: int) -> void:
    _event(keycode, true)
    _event(keycode, false)

func _run() -> void:
    var packed := load("res://main.tscn") as PackedScene
    _check(packed != null, "frozen real scene loads")
    if packed == null:
        _finish()
        return
    var game: Variant = packed.instantiate()
    get_root().add_child(game)
    await process_frame
    var player := game.get_node_or_null("Player") as Node2D
    var objective := game.get_node_or_null("Objective") as Label
    _check(player != null and objective != null, "real Player and visible Objective nodes")
    if player == null or objective == null:
        _finish()
        return
    _check(player.position == Vector2(92, 286), "original spawn coordinates preserved")
    var display: Dictionary = game._station_display("public_record", game.station_world.get_station("public_record"))
    var hint := "[E] %s — %s" % [display["title"], display["hint"]]
    game.reset_slice()
    player.position = Vector2(88, 188)
    game._refresh_nearby_hint()
    _check(game._nearest_station_id() == "public_record" and objective.text == hint,
        "real Label includes radius 88 exactly")
    player.position = Vector2(87, 188)
    game._refresh_nearby_hint()
    _check(game._nearest_station_id().is_empty() and objective.text == str(game.get_hud_view()["objective"])
        and not objective.text.contains("[E]"), "radius 89 clears prompt and restores live HUD")
    player.position = Vector2(176, 188)
    game._refresh_nearby_hint()
    _check(objective.text == hint, "near return displays exact approved label")

    game.reset_slice()
    _event(KEY_D, true)
    _event(KEY_W, true)
    game._process(0.4)
    _event(KEY_W, false)
    _event(KEY_D, false)
    _check(player.position.distance_to(Vector2(176, 188)) <= 88.0 and objective.text == hint,
        "real WASD input reaches visible station hint")
    _tap(KEY_E)
    await process_frame
    var state: Dictionary = game.get_game_state()
    _check(state.get("record_read") == true and (state.get("history", []) as Array).count("PUBLIC_RECORD_REVIEWED") == 1,
        "real E interacts once and release cannot replay")

    _event(KEY_D, true)
    game._process(0.95)
    _event(KEY_D, false)
    _check(game._nearest_station_id().is_empty() and not objective.text.contains("[E]")
        and objective.text == str(game.get_hud_view()["objective"]), "real near to far clears stale E")
    _event(KEY_A, true)
    game._process(0.95)
    _event(KEY_A, false)
    _check(game._nearest_station_id() == "public_record" and objective.text == hint,
        "real far to near reopens exact hint")

    game.reset_slice()
    var before: Dictionary = game.get_game_state()
    _event(KEY_E, false)
    _event(KEY_E, true, true)
    _event(KEY_E, false)
    _event(0, true, false, KEY_E)
    _event(0, false, false, KEY_E)
    _event(KEY_Q, true)
    _event(KEY_Q, false)
    await process_frame
    _check(game.get_game_state() == before,
        "echo, release, unknown and physical-key-only events cannot forge actions")
    _tap(KEY_1)
    await process_frame
    _check(str(game.get_game_state().get("commitment", "")) == ""
        and (game.get_node("Diagnostic") as Label).text.begins_with("[EF-GATE-NEGOTIATION]"),
        "premature choice cannot pass hearing state gate")
    _check(game.interact_with("public_record") and game.interact_with("defer_conclusion")
        and game.interact_with("commons_hearing"), "approved public record and nonconsent fixture")
    _tap(KEY_3)
    await process_frame
    state = game.get_game_state()
    _check(state.get("commitment") == "" and not state.get("negotiation_open", true)
        and state.get("mystery_state") == "UNKNOWN_BY_DESIGN"
        and (state.get("history", []) as Array).has("PUBLIC_COMMITMENT_DEFERRED"),
        "key 3 defers, does not consent or disclose private truth")
    _check(game.interact_with("commons_hearing"), "deferral hearing can be deliberately reopened")
    _tap(KEY_2)
    await process_frame
    _check(game.get_game_state().get("commitment") == "records_first",
        "key 2 selects records-first only after reopened hearing")
    _check(game.interact_with("project_table") and game.get_game_state().get("completed") == true
        and game.get_game_state().get("outcome") == "RECORDS_FIRST_PACKAGE_FILED",
        "records completion retains exact public outcome")
    _tap(KEY_R)
    await process_frame
    _check(player.position == Vector2(92, 286) and game.get_game_state().get("commitment") == ""
        and not game.get_game_state().get("completed", true)
        and not objective.text.contains("Press R to reset."), "real R restores spawn, state and HUD")

    _check(game.interact_with("public_record") and game.interact_with("material_trace")
        and game.interact_with("commons_hearing"), "repair-route prerequisites")
    _tap(KEY_1)
    await process_frame
    _check(game.get_game_state().get("commitment") == "repair_pilot",
        "key 1 selects only approved repair commitment")
    _check(game.interact_with("project_table")
        and game.get_game_state().get("outcome") == "BOUNDED_REPAIR_PILOT_STARTED"
        and game.get_game_state().get("mystery_state") == "UNKNOWN_BY_DESIGN",
        "repair completion bounded; unresolved private truth preserved")
    _finish()

func _finish() -> void:
    for key in [KEY_W, KEY_A, KEY_S, KEY_D, KEY_UP, KEY_LEFT, KEY_DOWN, KEY_RIGHT]:
        _event(key, false)
    if failures.is_empty():
        print("EVERFIELD_INDEPENDENT_LIVE_1575_PASS checks=%d" % checks)
        quit(0)
        return
    push_error("EVERFIELD_INDEPENDENT_LIVE_1575_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
