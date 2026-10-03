extends SceneTree

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var script := load("res://components/old_works_world/old_works_world_presentation.gd")
    _expect(script != null, "Old Works presentation component loads")
    if script == null:
        _finish()
        return

    var presentation: Variant = script.new()
    _expect(presentation.has_method("get_text"), "stable text lookup API exists")
    _expect(presentation.has_method("get_station"), "station contract API exists")
    _expect(presentation.has_method("get_contract"), "invariant contract API exists")

    _expect(presentation.get_text("OW_ARCHIVE_TITLE") == "Archive Ledger", "Archive Ledger title is exact")
    _expect(presentation.get_text("OW_ARCHIVE_BODY_02") == "One recorded account argues for a single dominant cause. Another rejects that reading. Both remain recorded as accounts, not findings.", "Archive Ledger preserves claims-not-findings wording")
    _expect(presentation.get_text("OW_TRACE_TITLE") == "Material Trace", "Material Trace title is exact")
    _expect(presentation.get_text("OW_TRACE_BODY_03") == "The trace supports a history of alteration and repeated maintenance. It does not identify a single cause for the fragmentation.", "Material Trace preserves non-resolution wording")

    var archive: Dictionary = presentation.get_station("public_record")
    _expect(archive.get("evidence_role", "") == "DISC_ROLE:PUBLIC_RECORD", "Archive has public-record role")
    var trace: Dictionary = presentation.get_station("material_trace")
    _expect(trace.get("evidence_role", "") == "DISC_ROLE:MATERIAL_TRACE", "Trace has material-evidence role")

    var contract: Dictionary = presentation.get_contract()
    _expect(contract.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "fragmentation mystery remains UNKNOWN_BY_DESIGN")
    var truth_effects: Dictionary = contract.get("claim_truth_effects", {})
    _expect(truth_effects.get("CLM:FRAGMENTATION-ACCOUNT-A", "") == "NONE", "account A has zero truth effect")
    _expect(truth_effects.get("CLM:FRAGMENTATION-ACCOUNT-B", "") == "NONE", "account B has zero truth effect")
    _expect(contract.get("public_record_exposes_private_information", true) == false, "public record does not expose private provenance gap")
    _expect(contract.get("material_trace_may_select_causal_winner", true) == false, "material trace cannot select a causal winner")
    _expect(contract.get("truth_deferral_is_legal", false) == true, "explicit truth deferral remains legal")
    _expect(contract.get("presentation_mutates_game_state", true) == false, "presentation contract is inert")

    _expect(presentation.get_text("OW_NOT_A_REAL_ID") == "", "unknown presentation ID fails closed")
    _expect(presentation.get_station("unknown_station").is_empty(), "unknown station fails closed")

    _finish()

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-OW-WORLD-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-OW-WORLD-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_OLD_WORKS_WORLD_PRESENTATION_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_OLD_WORKS_WORLD_PRESENTATION_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
