extends SceneTree

const HistoryView = preload("res://components/route_history_view/route_history_view.gd")
const SessionState = preload("res://components/session_state/session_state.gd")
const OldWorksWorld = preload("res://components/old_works_world/old_works_world_presentation.gd")
const Consequences = preload("res://components/commitment_consequences/commitment_consequence_presentation.gd")

var failures: Array[String] = []
var checks := 0

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var session: Variant = SessionState.new()
    var world: Variant = OldWorksWorld.new()
    var consequences: Variant = Consequences.new()
    var model: Variant = HistoryView.new()
    var initial: Dictionary = session.snapshot()

    var empty: Dictionary = model.build_view(initial, world, consequences)
    _expect(empty.get("ok", false) and empty.get("count", -1) == 0
        and empty.get("text") == "" and empty.get("entries", [1]).is_empty(),
        "empty reviewed history has no fabricated events or text")
    _expect(session.snapshot() == initial, "empty view does not mutate session")

    var expected_events := [
        "PUBLIC_RECORD_REVIEWED",
        "TRUTH_CONCLUSION_DEFERRED",
        "COMMONS_HEARING_OPENED",
        "PUBLIC_COMMITMENT_DEFERRED",
        "COMMONS_HEARING_OPENED",
        "COMMITMENT_RECORDS_FIRST",
        "RECORDS_FIRST_PACKAGE_FILED",
    ]
    for event_id in expected_events:
        _expect(session.append_history(event_id), "published event accepted: %s" % event_id)

    var frozen: Dictionary = session.snapshot()
    var displayed: Dictionary = model.build_view(frozen, world, consequences)
    _expect(displayed.get("ok", false) and displayed.get("count", 0) == expected_events.size(),
        "deferral, hearing reopen and records-first completion render full event order")
    var entries: Array = displayed.get("entries", [])
    if entries.size() == expected_events.size():
        for i in range(expected_events.size()):
            var entry: Dictionary = entries[i]
            _expect(entry.get("index") == i + 1 and entry.get("event_id") == expected_events[i],
                "public history entry order and machine identity preserved at %d" % i)
        _expect(entries[0].get("title") == world.get_text("OW_ARCHIVE_TITLE"),
            "public record title comes from reviewed Old Works provider")
        _expect(entries[1].get("title") == world.get_text("OW_DEFER_TITLE"),
            "explicit truth deferral uses reviewed non-resolution title")
        _expect(entries[3].get("title") == consequences.get_text("OW_CONSEQ_DEFER_TITLE"),
            "public commitment deferral uses approved nonconsent title")
        _expect(entries[6].get("title") == consequences.get_text("OW_CONSEQ_RECORDS_TITLE"),
            "records-first outcome uses exact approved public title")
        entries[0]["title"] = "FORGED"
        var next_view: Dictionary = model.build_view(session.snapshot(), world, consequences)
        _expect(next_view["entries"][0]["title"] == world.get_text("OW_ARCHIVE_TITLE"),
            "returned entry mutation cannot poison model or providers")
    _expect(session.snapshot() == frozen, "history build and returned-view changes do not mutate SessionState")
    _expect(displayed.get("mystery_state") == "UNKNOWN_BY_DESIGN",
        "public history does not resolve the historical cause")

    var inject: Dictionary = frozen.duplicate(true)
    var private_list: Array = inject["history"]
    private_list.append("ANWEN_PRIVATE_PROVENANCE")
    var denied: Dictionary = model.build_view(inject, world, consequences)
    _expect(not denied.get("ok", true)
        and not String(denied.get("text", "")).contains("ANWEN"),
        "unknown or private event is rejected without echoing value")
    _expect(not model.build_view({"mystery_state": "UNKNOWN_BY_DESIGN", "history": [77]}, world, consequences).get("ok", true),
        "non-string event rejected")
    _expect(not model.build_view({"mystery_state": "KNOWN", "history": []}, world, consequences).get("ok", true),
        "mystery truth promotion rejected")
    _expect(not model.build_view({"mystery_state": "UNKNOWN_BY_DESIGN", "history": "fake"}, world, consequences).get("ok", true),
        "non-array history rejected")
    _expect(not model.build_view({"mystery_state": "UNKNOWN_BY_DESIGN"}, world, consequences).get("ok", true),
        "missing history rejected")
    _expect(not model.build_view(null, world, consequences).get("ok", true),
        "missing snapshot rejected")
    _expect(not model.build_view(frozen, null, consequences).get("ok", true),
        "missing reviewed Old Works source rejected")
    _expect(not model.build_view(frozen, world, null).get("ok", true),
        "missing reviewed consequence source rejected")

    session.reset()
    var cleared: Dictionary = model.build_view(session.snapshot(), world, consequences)
    _expect(cleared.get("ok", false) and cleared.get("count", -1) == 0,
        "session reset clears visible history without durable storage")

    _finish()

func _expect(condition: bool, context: String) -> void:
    checks += 1
    if not condition:
        failures.append(context)
        printerr("[EVERFIELD][ROUTE-HISTORY][FAIL] %s" % context)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_ROUTE_HISTORY_VIEW_PASS checks=%d" % checks)
        quit(0)
        return
    printerr("[EVERFIELD][ROUTE-HISTORY] %d failures across %d checks" % [failures.size(), checks])
    quit(1)
