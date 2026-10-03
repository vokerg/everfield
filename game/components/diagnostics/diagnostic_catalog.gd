extends RefCounted

const ORDERED_CODES: Array[String] = [
    "EF-RESET",
    "EF-INTERACT-RANGE",
    "EF-INTERACT-UNKNOWN",
    "EF-INVESTIGATE-RECORD",
    "EF-INVESTIGATE-TRACE",
    "EF-GATE-DEFER",
    "EF-INVESTIGATE-DEFER",
    "EF-GATE-INVESTIGATION",
    "EF-NEGOTIATE",
    "EF-GATE-COMMITMENT",
    "EF-SLICE-COMPLETE",
    "EF-GATE-NEGOTIATION",
    "EF-COMMIT-REPAIR",
    "EF-COMMIT-RECORDS",
    "EF-COMMIT-DEFER",
    "EF-COMMIT-UNKNOWN",
]

const DEFINITIONS: Dictionary = {
    "EF-RESET": {
        "message": "Slice state reset; durable world mystery remains unresolved.",
        "is_error": false,
    },
    "EF-INTERACT-RANGE": {
        "message": "No interaction surface is within range.",
        "is_error": false,
    },
    "EF-INTERACT-UNKNOWN": {
        "message": "Unknown station: %s",
        "is_error": true,
        "context_key": "station_id",
    },
    "EF-INVESTIGATE-RECORD": {
        "message": "The archive records incompatible accounts; neither is promoted to truth.",
        "is_error": false,
    },
    "EF-INVESTIGATE-TRACE": {
        "message": "The Old Works carries independent material evidence, still insufficient to settle the cause.",
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
        "message": "Unsupported commitment choice: %s",
        "is_error": true,
        "context_key": "choice",
    },
}

func list_codes() -> Array[String]:
    return ORDERED_CODES.duplicate()

func has_code(code: String) -> bool:
    return DEFINITIONS.has(code)

func get_diagnostic(code: String, context: Dictionary = {}) -> Dictionary:
    if code.strip_edges().is_empty():
        return _failure_payload(code, "Diagnostic code is empty.")

    if not DEFINITIONS.has(code):
        return _failure_payload(code, "Unknown diagnostic code: %s" % code)

    var definition: Dictionary = DEFINITIONS[code]
    var message := String(definition["message"])
    var context_key := String(definition.get("context_key", ""))
    if not context_key.is_empty():
        if not context.has(context_key):
            return _failure_payload(
                code,
                "Missing required diagnostic context '%s' for %s." % [context_key, code]
            )
        var raw_value: Variant = context[context_key]
        if typeof(raw_value) != TYPE_STRING or String(raw_value).strip_edges().is_empty():
            return _failure_payload(
                code,
                "Invalid required diagnostic context '%s' for %s." % [context_key, code]
            )
        message = message % String(raw_value)

    return {
        "ok": true,
        "known": true,
        "code": code,
        "message": message,
        "is_error": bool(definition["is_error"]),
    }

func format_line(code: String, context: Dictionary = {}) -> String:
    var diagnostic := get_diagnostic(code, context)
    return "[%s] %s" % [diagnostic["code"], diagnostic["message"]]

func _failure_payload(requested_code: String, message: String) -> Dictionary:
    var visible_code := requested_code
    if visible_code.strip_edges().is_empty():
        visible_code = "<empty>"
    return {
        "ok": false,
        "known": false,
        "code": visible_code,
        "message": message,
        "is_error": true,
    }
