extends SceneTree

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var script := load("res://components/hud_objectives/hud_objective_model.gd")
    _expect(script != null, "HUD objective/status view-model loads")
    if script == null:
        _finish()
        return

    var model: Variant = script.new()
    _expect(model is RefCounted, "view-model has no scene/node ownership")

    var initial := _state()
    _view(model, initial, "INVESTIGATE_RECORD", "Archive Ledger")

    var trace_before_record := _state()
    trace_before_record["trace_inspected"] = true
    _view(model, trace_before_record, "INVESTIGATE_RECORD", "Archive Ledger")

    var record_only := _state()
    record_only["record_read"] = true
    _view(model, record_only, "INVESTIGATE_CORROBORATE_OR_DEFER", "Material Trace")

    var record_trace := _state()
    record_trace["record_read"] = true
    record_trace["trace_inspected"] = true
    var trace_view: Dictionary = _view(model, record_trace, "GO_TO_HEARING", "Commons Hearing")
    _expect(String(trace_view.get("status", "")).contains("Trace:yes"), "material-trace path reports trace evidence")
    _expect(String(trace_view.get("status", "")).contains("Deferred truth:no"), "material-trace path does not fabricate explicit deferral")

    var record_defer := _state()
    record_defer["record_read"] = true
    record_defer["deferred_truth"] = true
    var defer_ready_view: Dictionary = _view(model, record_defer, "GO_TO_HEARING", "Commons Hearing")
    _expect(String(defer_ready_view.get("status", "")).contains("Trace:no"), "explicit-deferral path does not fabricate trace evidence")
    _expect(String(defer_ready_view.get("status", "")).contains("Deferred truth:yes"), "explicit-deferral path reports deferral")

    var hearing := record_trace.duplicate(true)
    hearing["negotiation_open"] = true
    _view(model, hearing, "HEARING_OPEN", "repair pilot")

    var repair_committed := record_trace.duplicate(true)
    repair_committed["commitment"] = "repair_pilot"
    _view(model, repair_committed, "GO_TO_PROJECT_TABLE", "Project Table")

    var records_committed := record_defer.duplicate(true)
    records_committed["commitment"] = "records_first"
    _view(model, records_committed, "GO_TO_PROJECT_TABLE", "Project Table")

    var deferred_commitment := record_defer.duplicate(true)
    deferred_commitment["history"] = ["PUBLIC_COMMITMENT_DEFERRED"]
    var deferred_commitment_view: Dictionary = _view(model, deferred_commitment, "GO_TO_HEARING", "Commons Hearing")
    _expect(not String(deferred_commitment_view.get("objective", "")).contains("Loop complete"), "defer commitment remains non-complete and reopenable")

    var repair_complete := repair_committed.duplicate(true)
    repair_complete["completed"] = true
    repair_complete["outcome"] = "BOUNDED_REPAIR_PILOT_STARTED"
    _view(model, repair_complete, "COMPLETE", "BOUNDED_REPAIR_PILOT_STARTED")

    var records_complete := records_committed.duplicate(true)
    records_complete["completed"] = true
    records_complete["outcome"] = "RECORDS_FIRST_PACKAGE_FILED"
    _view(model, records_complete, "COMPLETE", "RECORDS_FIRST_PACKAGE_FILED")

    var custom_stations := {
        "public_record": {"title": "Records Room"},
        "material_trace": {"title": "Trace Bench"},
        "defer_conclusion": {"title": "Hold Finding"},
        "commons_hearing": {"title": "Public Hearing"},
        "project_table": {"title": "Action Table"},
    }
    var state_before := initial.duplicate(true)
    var stations_before := custom_stations.duplicate(true)
    var custom_view: Dictionary = model.build_view(initial, custom_stations)
    _expect(String(custom_view.get("objective", "")).contains("Records Room"), "optional station metadata can supply presentation title")
    _expect(initial == state_before, "view-model does not mutate state input")
    _expect(custom_stations == stations_before, "view-model does not mutate station metadata")

    var missing_field := _state()
    missing_field.erase("record_read")
    _invalid(model, missing_field, "missing required field fails closed")

    var wrong_type := _state()
    wrong_type["record_read"] = "yes"
    _invalid(model, wrong_type, "wrong field type fails closed")

    var bad_mystery := _state()
    bad_mystery["mystery_state"] = "SOLVED"
    _invalid(model, bad_mystery, "mystery promotion fails closed")

    var bad_commitment := record_trace.duplicate(true)
    bad_commitment["commitment"] = "invented_route"
    _invalid(model, bad_commitment, "unsupported commitment fails closed")

    var bad_completion := repair_committed.duplicate(true)
    bad_completion["completed"] = true
    bad_completion["outcome"] = "FABRICATED_OUTCOME"
    _invalid(model, bad_completion, "unsupported completion outcome fails closed")

    _finish()

func _state() -> Dictionary:
    return {
        "record_read": false,
        "trace_inspected": false,
        "deferred_truth": false,
        "negotiation_open": false,
        "commitment": "",
        "completed": false,
        "outcome": "",
        "mystery_state": "UNKNOWN_BY_DESIGN",
        "history": [],
    }

func _view(model: Variant, state: Dictionary, expected_phase: String, objective_fragment: String) -> Dictionary:
    var view: Dictionary = model.build_view(state)
    _expect(view.get("valid", false) == true, "%s state is valid" % expected_phase)
    _expect(view.get("phase", "") == expected_phase, "%s phase exact" % expected_phase)
    _expect(String(view.get("objective", "")).contains(objective_fragment), "%s objective exposes expected bounded presentation" % expected_phase)
    _expect(String(view.get("status", "")).contains("UNKNOWN_BY_DESIGN"), "%s status preserves UNKNOWN_BY_DESIGN" % expected_phase)
    return view

func _invalid(model: Variant, state: Dictionary, message: String) -> void:
    var state_before := state.duplicate(true)
    var view: Dictionary = model.build_view(state)
    _expect(view.get("valid", true) == false, message)
    _expect(view.get("phase", "") == "INVALID_STATE", "%s uses INVALID_STATE phase" % message)
    _expect(String(view.get("objective", "")).contains("Progress is not inferred"), "%s does not fabricate progress" % message)
    _expect(String(view.get("status", "")).contains("UNKNOWN_BY_DESIGN"), "%s keeps mystery visibly unresolved" % message)
    _expect(state == state_before, "%s leaves input unmodified" % message)

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-HUD-OBJECTIVE-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-HUD-OBJECTIVE-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_HUD_OBJECTIVE_MODEL_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_HUD_OBJECTIVE_MODEL_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
