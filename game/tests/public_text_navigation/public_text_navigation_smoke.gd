extends SceneTree

# Isolated executable tests for the pure, read-only navigation model. These
# tests are not executed by the existing shared first-playable CI by default.
const Navigation = preload("res://components/public_text_navigation/public_text_navigation.gd")
const Playable = preload("res://components/playable_presentation/playable_presentation.gd")
const SessionState = preload("res://components/session_state/session_state.gd")

var failures: Array[String] = []
var checks := 0

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var model: Variant = Navigation.new()
    var presenter: Variant = Playable.new()
    var session: Variant = SessionState.new()
    var frozen: Dictionary = session.snapshot()
    var provider_contract: Dictionary = presenter.get_contract().duplicate(true)
    var multipage_count := 0
    var multiline_count := 0

    for scenario in Navigation.SCENARIOS:
        var name: String = scenario
        var published: Dictionary = _published(presenter, name)
        _expect(published.get("ok", false) and typeof(published.get("text")) == TYPE_STRING,
            "authentic reviewed provider supplies " + name)
        if not published.get("ok", false) or typeof(published.get("text")) != TYPE_STRING:
            continue
        var original: String = published["text"]
        if original.contains("\n"):
            multiline_count += 1

        var first: Dictionary = model.page_view(name)
        _expect(first.get("ok", false), "source-backed first page exists " + name)
        if not first.get("ok", false):
            continue
        var total: int = first["page_count"]
        _expect(total > 0 and total <= Navigation.MAX_PAGES, "positive bounded page count " + name)
        _expect(first["source_length"] == original.length()
            and first["source_sha256"] == original.sha256_text(),
            "exact approved text identity preserved " + name)
        _expect(first["mystery_state"] == "UNKNOWN_BY_DESIGN",
            "narrative historical cause remains unresolved " + name)
        _expect(first["page_index"] == 0 and not first["has_previous"],
            "correct initial navigation boundary " + name)
        if total > 1:
            multipage_count += 1
            _expect(first["has_next"], "multipage source exposes forward navigation " + name)

        var reconstructed := ""
        for index in range(total):
            var view: Dictionary = model.page_view(name, index)
            _expect(view.get("ok", false), "all published pages reachable %s/%d" % [name, index])
            if not view.get("ok", false):
                continue
            var piece: String = view["text"]
            reconstructed += piece
            _expect(not piece.is_empty() and piece.length() <= Navigation.DEFAULT_PAGE_CHARACTERS,
                "no page exceeds bounded text characters %s/%d" % [name, index])
            _expect(view["page_index"] == index and view["page_count"] == total,
                "deterministic page numbering " + name)
            _expect(view["has_previous"] == (index > 0)
                and view["has_next"] == (index + 1 < total),
                "exact no-wrap navigation indicators " + name)
            if index > 0:
                var back: Dictionary = model.navigate(name, index, -1)
                _expect(back.get("ok", false) and back.get("text") == model.page_view(name, index - 1).get("text"),
                    "back step preserves exact previous page " + name)
            if index + 1 < total:
                var forward: Dictionary = model.navigate(name, index, 1)
                _expect(forward.get("ok", false) and forward.get("text") == model.page_view(name, index + 1).get("text"),
                    "forward step preserves exact next page " + name)
        _expect(reconstructed == original, "no dropped/reordered/inserted characters or paragraph breaks " + name)
        _expect(reconstructed.sha256_text() == original.sha256_text(), "SHA256 byte identity " + name)
        _expect(not model.navigate(name, 0, -1).get("ok", true), "no wrap before first page " + name)
        _expect(not model.navigate(name, total - 1, 1).get("ok", true), "no wrap after final page " + name)
        _expect(not model.page_view(name, total).get("ok", true), "reject bogus out-of-range index " + name)
        var poison: Dictionary = model.page_view(name)
        poison["text"] = "FORGED_PRIVATE_OR_CHANGED_TEXT"
        _expect(model.page_view(name).get("text") == first["text"],
            "returned dictionary mutation cannot poison published provider or next projection " + name)

    _expect(Navigation.SCENARIOS.size() == 13, "exact thirteen reviewed source surfaces")
    _expect(multipage_count >= 7, "measured over-budget public scenarios receive real bounded paging")
    _expect(multiline_count >= 7, "approved multiline text and paragraph breaks exercise pagination")
    _expect(session.snapshot() == frozen, "pagination never mutates the session state")
    _expect(presenter.get_contract() == provider_contract, "pagination does not mutate reviewed presentation contract")

    for invalid in [null, false, 42, [], {}, "", "unknown", "ANWEN_PRIVATE_PROVENANCE"]:
        var denied: Dictionary = model.page_view(invalid)
        _expect(not denied.get("ok", true) and not String(denied.get("text", "")).contains("ANWEN"),
            "unknown, private, empty and malformed scenario input fails closed")
    for bad_index in [null, false, "1", -1, 1.5, 9999]:
        _expect(not model.page_view("world_intro", bad_index).get("ok", true),
            "bogus page index fails closed")
    for bad_budget in [null, false, "128", 0, 1.5, 79, 241, 16384]:
        _expect(not model.page_view("world_intro", 0, bad_budget).get("ok", true),
            "unsafe page budget fails closed")
    for bad_direction in [null, 0, "1", 2, -2, 1.5]:
        _expect(not model.navigate("world_intro", 0, bad_direction).get("ok", true),
            "unknown navigation action fails closed")

    for budget in [Navigation.MIN_PAGE_CHARACTERS, Navigation.MAX_PAGE_CHARACTERS]:
        var original: String = _published(presenter, "combined_records_first")["text"]
        var header: Dictionary = model.page_view("combined_records_first", 0, budget)
        _expect(header.get("ok", false), "allowed page budget works at either boundary")
        if header.get("ok", false):
            var joined := ""
            for index in range(int(header["page_count"])):
                joined += String(model.page_view("combined_records_first", index, budget).get("text", ""))
            _expect(joined == original, "exact reconstruction at page budget boundary")

    _finish()

func _published(presenter: Variant, scenario: String) -> Dictionary:
    # Independently call the preexisting reviewed API to compare with model.
    match scenario:
        "world_intro":
            return presenter.world_intro()
        "world_public_record":
            return presenter.old_works_station("public_record")
        "world_material_trace":
            return presenter.old_works_station("material_trace")
        "world_truth_deferral":
            return presenter.old_works_station("defer_conclusion")
        "commons_hearing_opening":
            return presenter.hearing_opening()
        "hearing_repair":
            return presenter.hearing_route("repair_pilot")
        "hearing_records_first":
            return presenter.hearing_route("records_first")
        "hearing_explicit_deferral":
            return presenter.hearing_route("defer")
        "combined_repair":
            return presenter.hearing_and_consequence("repair_pilot", "COMMITMENT_REPAIR_PILOT")
        "combined_records_first":
            return presenter.hearing_and_consequence("records_first", "COMMITMENT_RECORDS_FIRST")
        "combined_explicit_deferral":
            return presenter.hearing_and_consequence("defer", "PUBLIC_COMMITMENT_DEFERRED")
        "consequence_repair_completion":
            return presenter.consequence("BOUNDED_REPAIR_PILOT_STARTED")
        "consequence_records_completion":
            return presenter.consequence("RECORDS_FIRST_PACKAGE_FILED")
    return {"ok": false}

func _expect(ok: bool, reason: String) -> void:
    checks += 1
    if not ok:
        failures.append(reason)
        printerr("[EVERFIELD][PUBLIC-TEXT-NAV][FAIL] " + reason)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_PUBLIC_TEXT_NAV_PASS checks=%d" % checks)
        quit(0)
        return
    printerr("EVERFIELD_PUBLIC_TEXT_NAV_FAIL failures=%d checks=%d" % [failures.size(), checks])
    quit(1)
