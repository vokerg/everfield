extends SceneTree
## Exact isolated Godot 4.7.1-stable action-command contract smoke.
## --headless --path game --script res://components/action_commands/action_command_smoke.gd

const Policy = preload("res://components/action_commands/action_command_policy.gd")

var failures: Array[String] = []


func _init() -> void:
    call_deferred("_run")


func _run() -> void:
    var policy: Variant = Policy.new()
    _expect(policy is RefCounted and not (policy is Node), "action-command policy has no Node, Input or game-state ownership")

    _accept(KEY_E, "interact", "", "E maps only to nearest-interaction command")
    _accept(KEY_1, "choose_commitment", "repair_pilot", "1 maps only to original repair-pilot choice")
    _accept(KEY_2, "choose_commitment", "records_first", "2 maps only to original records-first choice")
    _accept(KEY_3, "choose_commitment", "defer", "3 preserves explicit nonconsent deferral choice")
    _accept(KEY_R, "reset", "", "R maps only to original reset command")

    for code in [KEY_E, KEY_1, KEY_2, KEY_3, KEY_R]:
        _reject(Policy.decode_event(_key(code, false)), "NOT_PRESSED", "release for %s never dispatches" % str(code))
        _reject(Policy.decode_event(_key(code, true, true)), "ECHO", "echo for %s never dispatches" % str(code))

    for movement_key in [KEY_W, KEY_A, KEY_S, KEY_D, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN]:
        _reject(Policy.decode_event(_key(movement_key)), "UNMAPPED_KEY", "WASD/arrows are movement only %s" % str(movement_key))
    for other_key in [0, KEY_Q, KEY_ENTER, KEY_SPACE, KEY_ESCAPE, KEY_4, KEY_F]:
        _reject(Policy.decode_event(_key(other_key)), "UNMAPPED_KEY", "unknown/unsupported key is inert %s" % str(other_key))

    var mouse := InputEventMouseButton.new()
    mouse.pressed = true
    _reject(Policy.decode_event(mouse), "NOT_KEY_EVENT", "mouse presses cannot impersonate input-key commands")
    var action := InputEventAction.new()
    action.action = "ui_accept"
    action.pressed = true
    _reject(Policy.decode_event(action), "NOT_KEY_EVENT", "action injection cannot trigger a gameplay command")
    _reject(Policy.decode_event({"keycode": KEY_E, "pressed": true, "echo": false}), "NOT_KEY_EVENT", "dictionary forged as event cannot dispatch")
    _reject(Policy.decode_event("E"), "NOT_KEY_EVENT", "text is not accepted as a keyboard event")
    _reject(Policy.decode_event(null), "NOT_KEY_EVENT", "null input fails closed")
    _reject(Policy.decode_event(1544), "NOT_KEY_EVENT", "integer input fails closed")

    var physical_only: InputEventKey = _key(0)
    physical_only.physical_keycode = KEY_E
    _reject(Policy.decode_event(physical_only), "UNMAPPED_KEY", "physical-only E must not alter original keycode semantics")
    var modified: InputEventKey = _key(KEY_E)
    modified.ctrl_pressed = true
    _expect(Policy.decode_event(modified) == _valid("interact", ""), "modifier state preserves original keycode-only behavior")
    _expect(modified.keycode == KEY_E and modified.pressed and modified.ctrl_pressed and not modified.echo, "input event remains immutable to policy")

    var copied_event: InputEventKey = _key(KEY_1)
    var first: Dictionary = Policy.decode_event(copied_event)
    first["action"] = "forged_consent"
    first["choice"] = "unreviewed_route"
    first["ok"] = false
    first["error"] = "pretend_ok"
    var next: Dictionary = Policy.decode_event(copied_event)
    _expect(next == _valid("choose_commitment", "repair_pilot"), "returned result is a fresh independent dictionary")
    _expect(copied_event.keycode == KEY_1 and copied_event.pressed and not copied_event.echo, "source event is unmodified by decoded result")
    var rejected: Dictionary = Policy.decode_event({"keycode": KEY_3})
    rejected["ok"] = true
    rejected["action"] = "choose_commitment"
    rejected["choice"] = "repair_pilot"
    _reject(Policy.decode_event({"keycode": KEY_3}), "NOT_KEY_EVENT", "malformed result mutations cannot confer future consent")
    _expect(Policy.decode_event(_key(KEY_3)) == _valid("choose_commitment", "defer"), "only original public deferral route can be decoded from 3")

    _finish()


func _key(code: int, pressed_value: bool = true, echo_value: bool = false) -> InputEventKey:
    var event := InputEventKey.new()
    event.keycode = code
    event.pressed = pressed_value
    event.echo = echo_value
    return event


func _valid(action: String, choice: String) -> Dictionary:
    return {"ok": true, "action": action, "choice": choice, "error": ""}


func _accept(code: int, expected_action: String, expected_choice: String, description: String) -> void:
    _expect(Policy.decode_event(_key(code)) == _valid(expected_action, expected_choice), description)


func _reject(result: Dictionary, error_code: String, description: String) -> void:
    _expect(result == {"ok": false, "action": "", "choice": "", "error": error_code}, description)


func _expect(condition: bool, description: String) -> void:
    if condition:
        print("[EF-ACTION-COMMAND][PASS] %s" % description)
        return
    failures.append(description)
    push_error("[EF-ACTION-COMMAND][FAIL] %s" % description)


func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_ACTION_COMMAND_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_ACTION_COMMAND_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
