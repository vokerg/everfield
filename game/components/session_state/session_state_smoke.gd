extends SceneTree

var failures: Array[String] = []

const EXPECTED_KEYS := [
    "record_read",
    "trace_inspected",
    "deferred_truth",
    "negotiation_open",
    "commitment",
    "completed",
    "outcome",
    "mystery_state",
    "history",
]

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var script := load("res://components/session_state/session_state.gd")
    _expect(script != null, "session-state component loads")
    if script == null:
        _finish()
        return

    var session: Variant = script.new()
    _expect(session.has_method("snapshot"), "deep-copy snapshot API exists")
    _expect(session.has_method("set_field"), "bounded field mutation API exists")
    _expect(session.has_method("append_history"), "ordered history append API exists")
    _expect(session.has_method("reset"), "reset API exists")

    var initial: Dictionary = session.snapshot()
    _expect(initial.size() == EXPECTED_KEYS.size(), "initial state has exact bounded schema size")
    for key in EXPECTED_KEYS:
        _expect(initial.has(key), "initial state contains %s" % key)
    _expect(initial.get("record_read", true) == false, "record_read defaults false")
    _expect(initial.get("trace_inspected", true) == false, "trace_inspected defaults false")
    _expect(initial.get("deferred_truth", true) == false, "deferred_truth defaults false")
    _expect(initial.get("negotiation_open", true) == false, "negotiation_open defaults false")
    _expect(initial.get("commitment", "unexpected") == "", "commitment defaults empty")
    _expect(initial.get("completed", true) == false, "completed defaults false")
    _expect(initial.get("outcome", "unexpected") == "", "outcome defaults empty")
    _expect(initial.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "mystery defaults UNKNOWN_BY_DESIGN")
    _expect((initial.get("history", []) as Array).is_empty(), "history defaults empty")

    _expect(session.set_field("record_read", true), "supported boolean mutation succeeds")
    _expect(session.set_field("commitment", "repair_pilot"), "supported commitment mutation succeeds")
    _expect(session.set_field("outcome", "BOUNDED_REPAIR_PILOT_STARTED"), "supported outcome mutation succeeds")
    _expect(session.append_history("PUBLIC_RECORD_REVIEWED"), "first supported history event appends")
    _expect(session.append_history("COMMITMENT_REPAIR_PILOT"), "second supported history event appends")
    _expect(session.append_history("BOUNDED_REPAIR_PILOT_STARTED"), "third supported history event appends")

    var mutated: Dictionary = session.snapshot()
    var ordered_history: Array = mutated.get("history", [])
    _expect(ordered_history == [
        "PUBLIC_RECORD_REVIEWED",
        "COMMITMENT_REPAIR_PILOT",
        "BOUNDED_REPAIR_PILOT_STARTED",
    ], "history append order is preserved")
    _expect(mutated.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "ordinary mutations preserve mystery invariant")

    mutated["record_read"] = false
    ordered_history.append("MUTATED_SNAPSHOT_ONLY")
    var after_snapshot_mutation: Dictionary = session.snapshot()
    _expect(after_snapshot_mutation.get("record_read", false) == true, "snapshot scalar mutation cannot alter component state")
    _expect(not (after_snapshot_mutation.get("history", []) as Array).has("MUTATED_SNAPSHOT_ONLY"), "snapshot nested-array mutation cannot alter component state")

    _expect(not session.set_field("not_a_real_field", true), "unknown field fails closed")
    _expect(not session.set_field("record_read", "yes"), "wrong field type fails closed")
    _expect(not session.set_field("history", []), "direct history replacement fails closed")
    _expect(not session.set_field("mystery_state", "RESOLVED"), "mystery promotion fails closed")
    _expect(not session.append_history("NOT_A_REAL_EVENT"), "unknown history event fails closed")
    _expect(session.snapshot().get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "failed operations cannot promote mystery")

    session.reset()
    var reset_state: Dictionary = session.snapshot()
    _expect(reset_state.get("record_read", true) == false, "reset restores record_read")
    _expect(reset_state.get("trace_inspected", true) == false, "reset restores trace_inspected")
    _expect(reset_state.get("deferred_truth", true) == false, "reset restores deferred_truth")
    _expect(reset_state.get("negotiation_open", true) == false, "reset restores negotiation_open")
    _expect(reset_state.get("commitment", "unexpected") == "", "reset clears commitment")
    _expect(reset_state.get("completed", true) == false, "reset restores completion")
    _expect(reset_state.get("outcome", "unexpected") == "", "reset clears outcome")
    _expect(reset_state.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "reset preserves UNKNOWN_BY_DESIGN")
    _expect((reset_state.get("history", []) as Array).is_empty(), "reset clears transient history")

    var contract: Dictionary = session.get_contract()
    _expect(contract.get("transient_session_only", false) == true, "contract is transient-session only")
    _expect(contract.get("filesystem_io", true) == false, "contract grants no filesystem I/O")
    _expect(contract.get("save_load", true) == false, "contract grants no save/load")
    _expect(contract.get("durable_persistence", true) == false, "contract grants no durable persistence")
    _expect(contract.get("canon_authority", true) == false, "contract grants no canon authority")

    _finish()

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-SESSION-STATE-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-SESSION-STATE-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_SESSION_STATE_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_SESSION_STATE_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
