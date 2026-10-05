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

    var player := game.get_node_or_null("Player") as Node2D
    var diagnostic := game.get_node_or_null("Diagnostic") as Label
    var objective := game.get_node_or_null("Objective") as Label
    _expect(player != null, "player node exists")
    _expect(diagnostic != null, "diagnostic label exists")
    _expect(objective != null, "real visible HUD objective label exists")
    if player == null or diagnostic == null or objective == null:
        _finish()
        return

    _expect(player.position.is_equal_approx(Vector2(92, 286)), "player starts at bounded playable start")

    game.reset_slice()
    _expect(not game.interact_nearest(), "interaction fails outside INTERACT_RADIUS")
    _expect(diagnostic.text.begins_with("[EF-INTERACT-RANGE]"), "out-of-range interaction fails visibly")

    var movement_start := player.position
    _press_key(KEY_D)
    _press_key(KEY_W)
    game._process(0.4)
    _release_key(KEY_W)
    _release_key(KEY_D)

    _expect(player.position.x > movement_start.x, "synthetic D key moves player right through gameplay input path")
    _expect(player.position.y < movement_start.y, "synthetic W key moves player up through gameplay input path")
    _expect(player.position.distance_to(Vector2(176, 188)) <= 88.0, "input-driven movement reaches Archive Ledger interaction radius")
    var record_display: Dictionary = game._station_display(
        "public_record", game.station_world.get_station("public_record")
    )
    var expected_hint := "[E] %s — %s" % [record_display["title"], record_display["hint"]]
    _expect(objective.text == expected_hint, "actual WASD movement renders exact reviewed public station hint")
    _tap_action(KEY_E)
    await process_frame
    var moved_state: Dictionary = game.get_game_state()
    _expect(moved_state.get("record_read", false) == true, "actual input E event interacts only after valid proximity")
    _expect((moved_state.get("history", []) as Array).count("PUBLIC_RECORD_REVIEWED") == 1,
        "E release does not replay nearest station interaction")

    _press_key(KEY_D)
    game._process(0.95)
    _release_key(KEY_D)
    _expect(game._nearest_station_id().is_empty(), "real D movement leaves every station radius")
    _expect(objective.text == String(game.get_hud_view()["objective"])
        and not objective.text.contains("[E]"), "actual near to far movement clears stale E and restores live phase")
    _press_key(KEY_A)
    game._process(0.95)
    _release_key(KEY_A)
    _expect(game._nearest_station_id() == "public_record", "real A movement returns to Archive Ledger radius")
    _expect(objective.text == expected_hint, "actual far to near movement restores exactly reviewed E prompt")

    game.reset_slice()
    _press_key(KEY_A)
    _press_key(KEY_W)
    game._process(10.0)
    _release_key(KEY_W)
    _release_key(KEY_A)
    _expect(player.position.is_equal_approx(Vector2(36, 90)), "negative movement clamps to minimum world bounds")

    game.reset_slice()
    _press_key(KEY_D)
    _press_key(KEY_S)
    game._process(10.0)
    _release_key(KEY_S)
    _release_key(KEY_D)
    _expect(player.position.is_equal_approx(Vector2(924, 504)), "positive movement clamps to maximum world bounds")

    game.reset_slice()
    _expect(not game.interact_with("unknown_station"), "unknown interaction surface fails closed")
    _expect(diagnostic.text.begins_with("[EF-INTERACT-UNKNOWN]"), "unknown interaction surface fails visibly")

    # Send events through Godot's real input dispatch, not decoder-only calls:
    # action release, echo, physical-only forgery, early consent, deferral,
    # both commitments and scene R reset must retain original state gates.
    game.reset_slice()
    var before_rejected: Dictionary = game.get_game_state()
    _send_action_event(KEY_E, false)
    _send_action_event(KEY_E, true, true)
    _send_action_event(KEY_E, false)
    _send_action_event(0, true, false, KEY_E)
    _send_action_event(0, false, false, KEY_E)
    _send_action_event(KEY_Q, true)
    _send_action_event(KEY_Q, false)
    await process_frame
    _expect(game.get_game_state() == before_rejected,
        "release, echo, physical-only E and unmapped Q never forge an action")
    _tap_action(KEY_1)
    await process_frame
    _expect(game.get_game_state().get("commitment", "") == "",
        "real input 1 cannot authorize commitment before hearing")
    _expect(diagnostic.text.begins_with("[EF-GATE-NEGOTIATION]"),
        "early invalid real input choice produces existing reviewed gate diagnostic")

    _expect(game.interact_with("public_record"), "physical-key scene fixture reads public record")
    _expect(game.interact_with("defer_conclusion"), "physical-key scene fixture defers truth finding")
    _expect(game.interact_with("commons_hearing"), "physical-key scene fixture opens approved hearing")
    _tap_action(KEY_3)
    await process_frame
    var deferred: Dictionary = game.get_game_state()
    _expect(deferred.get("commitment") == "" and not deferred.get("negotiation_open", true),
        "real 3 key explicitly defers public commitment rather than implying consent")
    _expect((deferred.get("history", []) as Array).has("PUBLIC_COMMITMENT_DEFERRED"),
        "real deferral key appends only reviewed public nonconsent history")
    _expect(deferred.get("mystery_state") == "UNKNOWN_BY_DESIGN",
        "nonconsent path cannot promote mystery truth")
    _expect(game.interact_with("commons_hearing"), "approved hearing may reopen after key-3 deferral")
    _tap_action(KEY_2)
    await process_frame
    _expect(game.get_game_state().get("commitment") == "records_first",
        "real 2 key invokes reviewed records-first choice only when hearing open")
    _expect(game.interact_with("project_table"), "records-first key selection closes actual bounded scene loop")
    _press_key(KEY_D)
    _press_key(KEY_W)
    game._process(0.4)
    _release_key(KEY_W)
    _release_key(KEY_D)
    _expect(player.position.distance_to(Vector2(176, 188)) <= 88.0,
        "completed player reaches actual station radius by physical input movement")
    game._refresh_nearby_hint()
    _expect(objective.text == String(game.get_hud_view()["objective"]) + " Press R to reset."
        and not objective.text.contains("[E]"), "completed nearby scene suppresses E and retains original R reset")
    _tap_action(KEY_R)
    await process_frame
    _expect(player.position.is_equal_approx(Vector2(92, 286))
        and game.get_game_state().get("commitment") == ""
        and not game.get_game_state().get("completed", true),
        "real R key resets bounded state and actual player spawn")
    _expect(objective.text == String(game.get_hud_view()["objective"])
        and not objective.text.contains("Press R to reset."), "real R key restores exact reviewed phase objective")

    _expect(game.interact_with("public_record"), "repair-input fixture reads approved record")
    _expect(game.interact_with("material_trace"), "repair-input fixture reviews independent trace")
    _expect(game.interact_with("commons_hearing"), "repair-input fixture opens bounded hearing")
    _tap_action(KEY_1)
    await process_frame
    _expect(game.get_game_state().get("commitment") == "repair_pilot",
        "real 1 key commits only the approved repair route during hearing")
    _expect(game.interact_with("project_table"), "repair-input fixture closes playable loop")
    _expect(game.get_game_state().get("outcome") == "BOUNDED_REPAIR_PILOT_STARTED",
        "real repair route cannot invent an unreviewed consequence")

    _finish()

func _tap_action(keycode: int) -> void:
    _send_key(keycode, true)
    _send_key(keycode, false)

func _send_action_event(keycode: int, pressed: bool, echo: bool = false,
        physical_keycode: int = -1) -> void:
    var event := InputEventKey.new()
    event.keycode = keycode
    event.physical_keycode = keycode if physical_keycode == -1 else physical_keycode
    event.pressed = pressed
    event.echo = echo
    Input.parse_input_event(event)
    Input.flush_buffered_events()

func _press_key(keycode: int) -> void:
    _send_key(keycode, true)

func _release_key(keycode: int) -> void:
    _send_key(keycode, false)

func _send_key(keycode: int, pressed: bool) -> void:
    var event := InputEventKey.new()
    event.keycode = keycode
    event.physical_keycode = keycode
    event.pressed = pressed
    event.echo = false
    Input.parse_input_event(event)
    # Godot 4.7.1 defaults use_accumulated_input=true, so synthetic events are
    # buffered. Flush before production _process queries Input.is_key_pressed.
    Input.flush_buffered_events()
    _expect(
        Input.is_key_pressed(keycode) == pressed,
        "flushed synthetic key state matches key=%d pressed=%s" % [keycode, pressed]
    )

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-MOVEMENT-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-MOVEMENT-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    for keycode in [KEY_W, KEY_A, KEY_S, KEY_D, KEY_UP, KEY_LEFT, KEY_DOWN, KEY_RIGHT]:
        _release_key(keycode)

    if failures.is_empty():
        print("EVERFIELD_MOVEMENT_INTERACTION_SMOKE_PASS")
        quit(0)
        return

    push_error("EVERFIELD_MOVEMENT_INTERACTION_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
