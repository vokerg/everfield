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
    _expect(player != null, "player node exists")
    _expect(diagnostic != null, "diagnostic label exists")
    if player == null or diagnostic == null:
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
    _expect(game.interact_nearest(), "interaction succeeds after input-driven movement reaches valid station")
    var moved_state: Dictionary = game.get_game_state()
    _expect(moved_state.get("record_read", false) == true, "nearest interaction after movement executes Archive Ledger")

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

    _finish()

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
