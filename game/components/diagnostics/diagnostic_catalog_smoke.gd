extends SceneTree

var failures: Array[String] = []

const EXPECTED: Dictionary = {
    "EF-RESET": {
        "message": "Slice state reset; durable world mystery remains unresolved.",
        "is_error": false,
    },
    "EF-INTERACT-RANGE": {
        "message": "No interaction surface is within range.",
        "is_error": false,
    },
    "EF-INTERACT-UNKNOWN": {
        "message": "Unknown station: missing_station",
        "is_error": true,
        "context": {"station_id": "missing_station"},
    },
    "EF-INVESTIGATE-RECORD": {
        "message": "Reviewed Archive Ledger presentation; competing accounts remain claims, not findings.",
        "is_error": false,
    },
    "EF-INVESTIGATE-TRACE": {
        "message": "Reviewed Material Trace presentation; alteration evidence does not select a causal winner.",
        "is_error": false,
    },
    "EF-GATE-DEFER": {
        "message": "Review the public record before explicitly deferring a conclusion.",
        "is_error": false,
    },
    "EF-INVESTIGATE-DEFER": {
        "message": "Conclusion deferred by design; uncertainty is a legal route.",
        "is_error": false,
    },
    "EF-GATE-INVESTIGATION": {
        "message": "Read the public record and inspect the material trace or explicitly defer conclusion before negotiating.",
        "is_error": false,
    },
    "EF-NEGOTIATE": {
        "message": "Choose: [1] repair pilot, [2] records-first, or [3] defer commitment.",
        "is_error": false,
    },
    "EF-GATE-COMMITMENT": {
        "message": "A supported public commitment is required before the project table can close the loop.",
        "is_error": false,
    },
    "EF-SLICE-COMPLETE": {
        "message": "First-playable loop complete; mystery remains UNKNOWN_BY_DESIGN.",
        "is_error": false,
    },
    "EF-GATE-NEGOTIATION": {
        "message": "Open the Commons Hearing before choosing a commitment.",
        "is_error": false,
    },
    "EF-COMMIT-REPAIR": {
        "message": "Repair pilot selected: bounded and conditionally reversible.",
        "is_error": false,
    },
    "EF-COMMIT-RECORDS": {
        "message": "Records-first selected: document and limit use before broader repair.",
        "is_error": false,
    },
    "EF-COMMIT-DEFER": {
        "message": "Commitment deferred; the hearing may be reopened without erasing history.",
        "is_error": false,
    },
    "EF-COMMIT-UNKNOWN": {
        "message": "Unsupported commitment choice: unsupported",
        "is_error": true,
        "context": {"choice": "unsupported"},
    },
}

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var script := load("res://components/diagnostics/diagnostic_catalog.gd")
    _expect(script != null, "diagnostic catalog loads")
    if script == null:
        _finish()
        return

    var catalog: Variant = script.new()
    _expect(catalog.has_method("list_codes"), "stable code-list API exists")
    _expect(catalog.has_method("get_diagnostic"), "structured diagnostic API exists")
    _expect(catalog.has_method("format_line"), "formatted-line API exists")

    var codes: Array[String] = catalog.list_codes()
    _expect(codes.size() == EXPECTED.size(), "exact current diagnostic code count is preserved")
    for code in EXPECTED:
        _expect(codes.has(code), "%s is represented" % code)

        var expected: Dictionary = EXPECTED[code]
        var context: Dictionary = expected.get("context", {}).duplicate(true)
        var context_before := context.duplicate(true)
        var payload: Dictionary = catalog.get_diagnostic(code, context)

        _expect(payload.get("ok", false) == true, "%s resolves successfully" % code)
        _expect(payload.get("known", false) == true, "%s remains a known diagnostic" % code)
        _expect(payload.get("code", "") == code, "%s preserves its stable code" % code)
        _expect(payload.get("message", "") == expected["message"], "%s preserves its exact message contract" % code)
        _expect(payload.get("is_error", null) == expected["is_error"], "%s preserves error classification" % code)
        _expect(catalog.format_line(code, context) == "[%s] %s" % [code, expected["message"]], "%s formatted output includes code and message" % code)
        _expect(context == context_before, "%s lookup does not mutate caller context" % code)

    var returned_codes: Array[String] = catalog.list_codes()
    returned_codes.clear()
    _expect(catalog.list_codes().size() == EXPECTED.size(), "returned code list cannot mutate catalog state")

    var unknown_context := {"nested": {"unchanged": true}}
    var unknown_before := unknown_context.duplicate(true)
    var unknown: Dictionary = catalog.get_diagnostic("EF-NOT-REAL", unknown_context)
    _expect(unknown.get("ok", true) == false, "unknown code fails closed")
    _expect(unknown.get("known", true) == false, "unknown code cannot be mistaken for a known diagnostic")
    _expect(unknown.get("is_error", false) == true, "unknown code is visibly error-classified")
    _expect(unknown.get("code", "") == "EF-NOT-REAL", "unknown requested code remains visible")
    _expect(not String(unknown.get("message", "")).is_empty(), "unknown code emits a nonempty failure message")
    _expect(catalog.format_line("EF-NOT-REAL", unknown_context).begins_with("[EF-NOT-REAL] "), "unknown formatted output remains visibly fail-closed")
    _expect(unknown_context == unknown_before, "unknown lookup does not mutate caller dictionaries")

    var empty: Dictionary = catalog.get_diagnostic("   ")
    _expect(empty.get("ok", true) == false, "empty code fails closed")
    _expect(empty.get("known", true) == false, "empty code is never treated as known")
    _expect(empty.get("is_error", false) == true, "empty code is visibly error-classified")
    _expect(empty.get("code", "") == "<empty>", "empty code gets a visible placeholder")
    _expect(catalog.format_line("   ").begins_with("[<empty>] "), "empty formatted output remains visible")

    var missing_context: Dictionary = catalog.get_diagnostic("EF-INTERACT-UNKNOWN")
    _expect(missing_context.get("ok", true) == false, "missing required context fails closed")
    _expect(missing_context.get("is_error", false) == true, "missing context is visibly error-classified")
    _expect(not String(missing_context.get("message", "")).is_empty(), "missing context emits a nonempty failure message")

    var invalid_context: Dictionary = catalog.get_diagnostic("EF-COMMIT-UNKNOWN", {"choice": 42})
    _expect(invalid_context.get("ok", true) == false, "invalid required context type fails closed")
    _expect(invalid_context.get("is_error", false) == true, "invalid context type is visibly error-classified")

    _finish()

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-DIAGNOSTIC-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-DIAGNOSTIC-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_DIAGNOSTIC_CONTRACT_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_DIAGNOSTIC_CONTRACT_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
