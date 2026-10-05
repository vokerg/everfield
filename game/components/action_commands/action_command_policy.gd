extends RefCounted
## Pure action-command policy extracted from the published first-playable controller.
## The caller owns physical InputEvent delivery, state gating, diagnostics and dispatch.
## Outputs are fresh typed dictionaries, never actions executed by this component.

const ACTION_INTERACT := "interact"
const ACTION_CHOOSE_COMMITMENT := "choose_commitment"
const ACTION_RESET := "reset"


static func decode_event(event: Variant) -> Dictionary:
    # Preserve _unhandled_key_input's exact keycode, pressed and echo semantics.
    # Do not accept fabricated keycode dictionaries or physical-only key matches.
    if not (event is InputEventKey):
        return _reject("NOT_KEY_EVENT")
    var key_event: InputEventKey = event as InputEventKey
    if not key_event.pressed:
        return _reject("NOT_PRESSED")
    if key_event.echo:
        return _reject("ECHO")

    match key_event.keycode:
        KEY_E:
            return _accept(ACTION_INTERACT)
        KEY_1:
            return _accept(ACTION_CHOOSE_COMMITMENT, "repair_pilot")
        KEY_2:
            return _accept(ACTION_CHOOSE_COMMITMENT, "records_first")
        KEY_3:
            return _accept(ACTION_CHOOSE_COMMITMENT, "defer")
        KEY_R:
            return _accept(ACTION_RESET)
        _:
            return _reject("UNMAPPED_KEY")


static func _accept(action: String, choice: String = "") -> Dictionary:
    return {"ok": true, "action": action, "choice": choice, "error": ""}


static func _reject(reason: String) -> Dictionary:
    return {"ok": false, "action": "", "choice": "", "error": reason}
