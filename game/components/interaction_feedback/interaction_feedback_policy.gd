extends RefCounted
## Pure objective selection after the controller has sampled nearest station.
## This policy owns no Input, Label, session data, or station proximity calculations.
## The controller injects the exact HudObjectiveModel view and StationWorld IDs.
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"
const PHASES := [
    "INVESTIGATE_RECORD",
    "INVESTIGATE_CORROBORATE_OR_DEFER",
    "GO_TO_HEARING",
    "HEARING_OPEN",
    "GO_TO_PROJECT_TABLE",
    "COMPLETE",
]
const INVALID_OBJECTIVE := "[EF-HUD-STATE] Invalid bounded session state. Progress is not inferred."


static func objective_view(
    hud_view: Variant, nearest_station_id: Variant,
    station_display: Variant, station_ids: Variant
) -> Dictionary:
    if not (hud_view is Dictionary):
        return _reject("INVALID_HUD_VIEW")
    var hud := hud_view as Dictionary
    if typeof(hud.get("valid")) != TYPE_BOOL or not hud["valid"]:
        return _reject("INVALID_HUD_VIEW")
    if typeof(hud.get("objective")) != TYPE_STRING or String(hud["objective"]).is_empty():
        return _reject("INVALID_HUD_OBJECTIVE")
    if typeof(hud.get("status")) != TYPE_STRING or not String(hud["status"]).contains(MYSTERY_STATE):
        return _reject("INVALID_HUD_STATUS")
    if typeof(hud.get("mystery_state")) != TYPE_STRING or hud["mystery_state"] != MYSTERY_STATE:
        return _reject("INVALID_MYSTERY_STATE")
    if typeof(hud.get("phase")) != TYPE_STRING or not PHASES.has(hud["phase"]):
        return _reject("INVALID_HUD_PHASE")
    if typeof(nearest_station_id) != TYPE_STRING:
        return _reject("INVALID_NEAREST_STATION")
    if not (station_ids is Array):
        return _reject("INVALID_STATION_IDS")
    var ids := station_ids as Array
    if ids.is_empty():
        return _reject("EMPTY_STATION_IDS")
    var seen := {}
    for station_id in ids:
        if typeof(station_id) != TYPE_STRING or String(station_id).is_empty() or seen.has(station_id):
            return _reject("MALFORMED_STATION_IDS")
        seen[station_id] = true

    var base_objective := String(hud["objective"])
    var phase := String(hud["phase"])
    # Completion always retains the controller's previously published R reset
    # suffix; a nearby marker must not conceal the end-of-loop status.
    if phase == "COMPLETE":
        return _result(base_objective + " Press R to reset.", false, phase)
    if String(nearest_station_id).is_empty():
        return _result(base_objective, false, phase)
    if not seen.has(nearest_station_id):
        return _reject("UNKNOWN_NEAREST_STATION")

    # The controller supplies only reviewed StationWorld/OldWorks display text.
    # This policy neither looks it up nor rewrites it.
    if not (station_display is Dictionary):
        return _reject("INVALID_STATION_DISPLAY")
    var display := station_display as Dictionary
    if typeof(display.get("title")) != TYPE_STRING or typeof(display.get("hint")) != TYPE_STRING:
        return _reject("INVALID_STATION_DISPLAY")
    var title := String(display["title"])
    var hint := String(display["hint"])
    if title.strip_edges().is_empty() or hint.strip_edges().is_empty():
        return _reject("EMPTY_STATION_DISPLAY")
    return _result("[E] %s — %s" % [title, hint], true, phase)


static func _result(objective: String, nearby: bool, phase: String) -> Dictionary:
    return {"ok": true, "objective": objective, "nearby": nearby, "phase": phase}


static func _reject(reason: String) -> Dictionary:
    # Invalid metadata never turns into an actionable key hint or a valid
    # completion. The live controller may surface its existing error policy.
    return {"ok": false, "error": reason, "objective": INVALID_OBJECTIVE, "nearby": false}
