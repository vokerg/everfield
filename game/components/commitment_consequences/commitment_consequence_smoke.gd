extends SceneTree

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var script := load("res://components/commitment_consequences/commitment_consequence_presentation.gd")
    _expect(script != null, "consequence presentation component loads")
    if script == null:
        _finish()
        return

    var p: Variant = script.new()
    _expect(p.get_text("OW_CONSEQ_REPAIR_TITLE") == "Repair Pilot — Bounded Start", "repair title exact")
    _expect(p.get_text("OW_CONSEQ_RECORDS_TITLE") == "Records First — Package Filed", "records-first title exact")
    _expect(p.get_text("OW_CONSEQ_DEFER_BODY") == "Nothing is committed. Deferral records nonalignment for now; it is not approval waiting to happen.", "deferral nonconsent exact")

    _event(p, "COMMITMENT_REPAIR_PILOT", "repair_pilot", "selection")
    _event(p, "BOUNDED_REPAIR_PILOT_STARTED", "repair_pilot", "completion")
    _event(p, "COMMITMENT_RECORDS_FIRST", "records_first", "selection")
    _event(p, "RECORDS_FIRST_PACKAGE_FILED", "records_first", "completion")
    _event(p, "PUBLIC_COMMITMENT_DEFERRED", "defer", "selection")

    var repair_hook: Dictionary = p.get_hook("HOOK:OW:REPAIR-PILOT-REASSESS")
    _expect(repair_hook.get("text_id", "") == "OW_CONSEQ_REPAIR_FOLLOWUP", "repair follow-up hook exact")
    _expect(repair_hook.get("auto_trigger", true) == false, "repair hook is inert")
    var records_hook: Dictionary = p.get_hook("HOOK:OW:RECORDS-FIRST-REASSESS")
    _expect(records_hook.get("text_id", "") == "OW_CONSEQ_RECORDS_FOLLOWUP", "records follow-up hook exact")
    _expect(records_hook.get("active_objective", true) == false, "records hook creates no active objective")

    var contract: Dictionary = p.get_contract()
    _expect(contract.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "mystery remains UNKNOWN_BY_DESIGN")
    _expect(contract.get("deferral_is_consent_in_waiting", true) == false, "deferral is not consent in waiting")
    _expect(contract.get("direct_state_mutation", true) == false, "presentation cannot mutate game state")
    _expect(contract.get("direct_history_mutation", true) == false, "presentation cannot mutate history")

    _expect(p.get_event("NOT_A_REAL_EVENT").is_empty(), "unknown event fails closed")
    _expect(p.get_text("NOT_A_REAL_ID") == "", "unknown presentation ID fails closed")
    _expect(p.get_hook("HOOK:OW:UNKNOWN").is_empty(), "unknown hook fails closed")
    _finish()

func _event(p: Variant, event_id: String, route: String, phase: String) -> void:
    var event: Dictionary = p.get_event(event_id)
    _expect(not event.is_empty(), "%s maps to presentation" % event_id)
    _expect(event.get("route", "") == route, "%s route exact" % event_id)
    _expect(event.get("phase", "") == phase, "%s phase exact" % event_id)
    var ids: Array = event.get("ids", [])
    _expect(not ids.is_empty(), "%s exposes reviewed presentation IDs" % event_id)
    for id in ids:
        _expect(p.get_text(String(id)) != "", "%s references known text %s" % [event_id, id])

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-CONSEQ-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-CONSEQ-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_COMMITMENT_CONSEQUENCE_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_COMMITMENT_CONSEQUENCE_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
