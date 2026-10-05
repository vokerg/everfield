extends SceneTree
## Isolated Godot 4.7.1 policy smoke; shared live-scene testing belongs to #1545.
const Policy = preload("res://components/interaction_feedback/interaction_feedback_policy.gd")
const HudModel = preload("res://components/hud_objectives/hud_objective_model.gd")
const SessionState = preload("res://components/session_state/session_state.gd")

var failures: Array[String] = []


func _init() -> void:
    call_deferred("_run")


func _run() -> void:
    var model := HudModel.new()
    var state: Dictionary = SessionState.new().snapshot()
    var hud: Dictionary = model.build_view(state)
    var ids := ["public_record", "material_trace", "defer_conclusion", "commons_hearing", "project_table"]
    var display := {"title": "Archive Ledger", "hint": "Review the public record."}
    var original_hud := hud.duplicate(true)
    var original_display := display.duplicate(true)
    var original_ids := ids.duplicate(true)

    _expect(hud.get("valid", false) and hud.get("phase") == "INVESTIGATE_RECORD",
        "fixture is the real published HudObjectiveModel")
    var far_first: Dictionary = Policy.objective_view(hud, "", {}, ids)
    _expect(far_first.get("ok", false) and not far_first.get("nearby", true)
        and far_first.get("objective") == hud["objective"], "far starts with reviewed phase objective")
    var near: Dictionary = Policy.objective_view(hud, "public_record", display, ids)
    _expect(near.get("ok", false) and near.get("nearby", false)
        and near.get("objective") == "[E] Archive Ledger — Review the public record.",
        "nearby uses exact injected approved display")
    var far_after_near: Dictionary = Policy.objective_view(hud, "", {}, ids)
    _expect(far_after_near.get("objective") == hud["objective"]
        and not String(far_after_near.get("objective")).contains("[E]"),
        "near to far clears stale E invitation")
    var near_again: Dictionary = Policy.objective_view(hud, "public_record", display, ids)
    _expect(near_again == near, "far to near returns identical approved prompt")
    _expect(hud == original_hud and display == original_display and ids == original_ids,
        "all injected inputs retain value identity and are not mutated")

    var ready_state: Dictionary = state.duplicate(true)
    ready_state["record_read"] = true
    ready_state["deferred_truth"] = true
    var hearing_hud: Dictionary = model.build_view(ready_state)
    _expect(hearing_hud.get("phase") == "GO_TO_HEARING", "explicit truth defer is not a finding or assent")
    _expect(Policy.objective_view(hearing_hud, "", {}, ids).get("objective") == hearing_hud["objective"],
        "phase objective survives distant interaction")
    _expect(Policy.objective_view(hearing_hud, "commons_hearing",
        {"title": "Commons Hearing", "hint": "Open hearing."}, ids).get("nearby", false),
        "nearby hearing prompt is an interaction hint, not a commitment")

    var complete_state: Dictionary = ready_state.duplicate(true)
    complete_state["commitment"] = "repair_pilot"
    complete_state["outcome"] = "BOUNDED_REPAIR_PILOT_STARTED"
    complete_state["completed"] = true
    var completed: Dictionary = model.build_view(complete_state)
    _expect(completed.get("valid", false) and completed.get("phase") == "COMPLETE",
        "completion fixture accepted by reviewed HUD model")
    var completed_far: Dictionary = Policy.objective_view(completed, "", {}, ids)
    var completed_near: Dictionary = Policy.objective_view(completed, "public_record", display, ids)
    _expect(completed_far.get("objective") == String(completed["objective"]) + " Press R to reset.",
        "complete phase restores exactly existing reset instruction")
    _expect(completed_near.get("objective") == completed_far.get("objective")
        and not completed_near.get("nearby", true),
        "completion/reset precedence never hides behind E hint")
    var after_reset: Dictionary = Policy.objective_view(model.build_view(state), "", {}, ids)
    _expect(after_reset.get("objective") == hud["objective"]
        and not String(after_reset.get("objective")).contains("Press R to reset."),
        "reset objective is back to reviewed investigation phase")

    _reject(Policy.objective_view(null, "", {}, ids), "null HUD fails closed")
    _reject(Policy.objective_view([], "", {}, ids), "non-dictionary HUD fails closed")
    var invalid_hud: Dictionary = model.build_view({"record_read": true})
    _reject(Policy.objective_view(invalid_hud, "public_record", display, ids),
        "invalid HUD cannot fabricate E invitation or phase")
    var forged_hud := hud.duplicate(true)
    forged_hud["mystery_state"] = "SOLVED"
    _reject(Policy.objective_view(forged_hud, "public_record", display, ids),
        "forged mystery status fails closed")
    forged_hud = hud.duplicate(true)
    forged_hud["phase"] = "UNREVIEWED_NEW_ROUTE"
    _reject(Policy.objective_view(forged_hud, "public_record", display, ids),
        "unknown phase cannot invent station action")
    forged_hud = hud.duplicate(true)
    forged_hud["objective"] = 123
    _reject(Policy.objective_view(forged_hud, "public_record", display, ids),
        "malformed objective fails closed")
    _reject(Policy.objective_view(hud, 1, display, ids), "non-string nearest ID fails closed")
    _reject(Policy.objective_view(hud, "rogue_station", display, ids),
        "unknown nearest station ID fails closed")
    _reject(Policy.objective_view(hud, "public_record", {}, ids),
        "missing title and hint cannot display E")
    _reject(Policy.objective_view(hud, "public_record", {"title": "", "hint": "x"}, ids),
        "empty title cannot display E")
    _reject(Policy.objective_view(hud, "public_record", {"title": "X", "hint": 4}, ids),
        "malformed hint cannot display E")
    _reject(Policy.objective_view(hud, "public_record", display, "not_ids"),
        "malformed ID collection rejected")
    _reject(Policy.objective_view(hud, "public_record", display, []),
        "empty ID collection rejected")
    _reject(Policy.objective_view(hud, "public_record", display, ["public_record", "public_record"]),
        "duplicate IDs rejected")
    _expect(hud == original_hud and display == original_display and ids == original_ids,
        "invalid queries cannot mutate HUD/StationWorld snapshots or infer consent")
    _finish()


func _reject(result: Dictionary, description: String) -> void:
    _expect(result.get("ok", true) == false and not String(result.get("error", "")).is_empty()
        and not String(result.get("objective", "")).contains("[E]")
        and not result.get("nearby", true), description)


func _expect(condition: bool, description: String) -> void:
    if condition:
        print("[EF-INTERACTION-FEEDBACK][PASS] %s" % description)
        return
    failures.append(description)
    push_error("[EF-INTERACTION-FEEDBACK][FAIL] %s" % description)


func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_INTERACTION_FEEDBACK_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_INTERACTION_FEEDBACK_SMOKE_FAIL count=%d failures=%s"
        % [failures.size(), failures])
    quit(1)
