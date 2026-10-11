extends SceneTree

# Isolated no-scene read-only route-history adversarial smoke.
const HistoryView = preload("res://components/route_history_view/route_history_view.gd")
const SessionState = preload("res://components/session_state/session_state.gd")
const OldWorksWorld = preload("res://components/old_works_world/old_works_world_presentation.gd")
const Consequences = preload("res://components/commitment_consequences/commitment_consequence_presentation.gd")

class FakeWorld:
    extends RefCounted
    func get_contract() -> Dictionary:
        return {
            "mystery_state": "UNKNOWN_BY_DESIGN",
            "public_record_exposes_private_information": false,
            "presentation_mutates_game_state": false,
        }
    func has_text(_id: String) -> bool:
        return true
    func get_text(_id: String) -> String:
        return "FORGED PUBLIC FACT"

class FakeConsequence:
    extends RefCounted
    func get_contract() -> Dictionary:
        return {
            "mystery_state": "UNKNOWN_BY_DESIGN",
            "deferral_is_consent_in_waiting": false,
            "direct_history_mutation": false,
        }
    func get_text(_id: String) -> String:
        return "FORGED CONSENT"

var failures: Array[String] = []
var checks := 0

func _init() -> void:
    call_deferred("_run")

func _append_published(session: Variant, event_id: String) -> void:
    # Exact state actions preceding append_history in published main.gd. Do not
    # silently manufacture source history without matching game state.
    match event_id:
        "PUBLIC_RECORD_REVIEWED":
            _expect(session.set_field("record_read", true), "record flag")
        "MATERIAL_TRACE_INSPECTED":
            _expect(session.set_field("trace_inspected", true), "trace flag")
        "TRUTH_CONCLUSION_DEFERRED":
            _expect(session.set_field("deferred_truth", true), "deferral flag")
        "COMMONS_HEARING_OPENED":
            _expect(session.set_field("negotiation_open", true), "hearing flag")
        "PUBLIC_COMMITMENT_DEFERRED":
            _expect(session.set_field("commitment", ""), "nonconsent commitment")
            _expect(session.set_field("negotiation_open", false), "nonconsent closes hearing")
        "COMMITMENT_REPAIR_PILOT":
            _expect(session.set_field("commitment", "repair_pilot"), "repair selection")
            _expect(session.set_field("negotiation_open", false), "repair closes hearing")
        "COMMITMENT_RECORDS_FIRST":
            _expect(session.set_field("commitment", "records_first"), "records selection")
            _expect(session.set_field("negotiation_open", false), "records closes hearing")
        "BOUNDED_REPAIR_PILOT_STARTED", "RECORDS_FIRST_PACKAGE_FILED":
            _expect(session.set_field("outcome", event_id), "completion outcome")
            _expect(session.set_field("completed", true), "completion flag")
        _:
            _expect(false, "test attempted unknown route event")
            return
    _expect(session.append_history(event_id), "allowed published event appended: %s" % event_id)

func _run() -> void:
    var session: Variant = SessionState.new()
    var world: Variant = OldWorksWorld.new()
    var consequences: Variant = Consequences.new()
    var model: Variant = HistoryView.new()
    var initial: Dictionary = session.snapshot()

    var empty: Dictionary = model.build_view(initial, world, consequences)
    _expect(empty.get("ok", false) and empty.get("count", -1) == 0
        and empty.get("text") == "" and empty.get("entries", [1]).is_empty(),
        "empty real session has no invented history")
    _expect(empty.get("page_count") == 1 and not empty.get("has_next", true),
        "empty session has exactly one bounded page")
    _expect(session.snapshot() == initial, "empty projection cannot mutate state")

    # FSR-1643-B01: an allowlisted completion ID in a contradictory,
    # uncompleted snapshot MUST NOT fabricate a completed public route.
    var forged_completion: Dictionary = initial.duplicate(true)
    forged_completion["history"] = ["RECORDS_FIRST_PACKAGE_FILED"]
    var rejected: Dictionary = model.build_view(forged_completion, world, consequences)
    _expect(not rejected.get("ok", true)
        and not String(rejected.get("text", "")).contains("Package Filed"),
        "forged allowed-ID completion cannot fabricate records-first result")
    var forged_selection: Dictionary = initial.duplicate(true)
    forged_selection["history"] = ["COMMITMENT_REPAIR_PILOT"]
    _expect(not model.build_view(forged_selection, world, consequences).get("ok", true),
        "forged allowed commitment cannot invent a prior hearing")
    var forged_hearing: Dictionary = initial.duplicate(true)
    forged_hearing["history"] = ["COMMONS_HEARING_OPENED"]
    _expect(not model.build_view(forged_hearing, world, consequences).get("ok", true),
        "forged allowed hearing cannot invent investigation")
    var forged_full: Dictionary = initial.duplicate(true)
    forged_full["history"] = [
        "PUBLIC_RECORD_REVIEWED", "TRUTH_CONCLUSION_DEFERRED",
        "COMMONS_HEARING_OPENED", "COMMITMENT_RECORDS_FIRST",
        "RECORDS_FIRST_PACKAGE_FILED",
    ]
    _expect(not model.build_view(forged_full, world, consequences).get("ok", true),
        "self-inconsistent forged completed history rejected even if all IDs allowed")

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
        _append_published(session, event_id)

    var frozen: Dictionary = session.snapshot()
    var displayed: Dictionary = model.build_view(frozen, world, consequences)
    _expect(displayed.get("ok", false) and displayed.get("count", -1) == expected_events.size(),
        "genuine deferral, reopened hearing, records-first completion accepted")
    _expect(displayed.get("page_count") == 1 and displayed.get("entries", []).size() == 7,
        "seven real route events fit first bounded page")
    var entries: Array = displayed.get("entries", [])
    if entries.size() == expected_events.size():
        for i in range(expected_events.size()):
            var entry: Dictionary = entries[i]
            _expect(entry.get("index") == i + 1 and entry.get("event_id") == expected_events[i],
                "real ordered public history event at index %d" % i)
        _expect(entries[0].get("title") == world.get_text("OW_ARCHIVE_TITLE"),
            "real reviewed archive title, not copied narrative")
        _expect(entries[1].get("title") == world.get_text("OW_DEFER_TITLE"),
            "real reviewed truth-deferral title")
        _expect(entries[3].get("title") == consequences.get_text("OW_CONSEQ_DEFER_TITLE"),
            "nonconsent title remains exact reviewed provider text")
        _expect(entries[6].get("title") == consequences.get_text("OW_CONSEQ_RECORDS_TITLE"),
            "records completion uses reviewed public title")
        entries[0]["title"] = "FORGED"
        _expect(model.build_view(session.snapshot(), world, consequences)["entries"][0]["title"]
            == world.get_text("OW_ARCHIVE_TITLE"),
            "mutating returned entries cannot mutate real provider or model")
    _expect(session.snapshot() == frozen, "read-only projection preserves input session snapshot")
    _expect(displayed.get("mystery_state") == "UNKNOWN_BY_DESIGN",
        "source may never decide unknown historical cause")

    # Simulated reported flags must exactly agree with the ordered transitions.
    var contradict: Dictionary = frozen.duplicate(true)
    contradict["completed"] = false
    _expect(not model.build_view(contradict, world, consequences).get("ok", true),
        "completed public event cannot be paired with completed=false")
    contradict = frozen.duplicate(true)
    contradict["outcome"] = ""
    _expect(not model.build_view(contradict, world, consequences).get("ok", true),
        "completed public event cannot be paired with blank outcome")
    contradict = frozen.duplicate(true)
    contradict["commitment"] = "repair_pilot"
    _expect(not model.build_view(contradict, world, consequences).get("ok", true),
        "last explicit selection cannot be silently reassigned")
    contradict = frozen.duplicate(true)
    contradict["negotiation_open"] = true
    _expect(not model.build_view(contradict, world, consequences).get("ok", true),
        "final explicit commitment closes the hearing")
    contradict = frozen.duplicate(true)
    contradict["extra_unaudited_field"] = "TRUE"
    _expect(not model.build_view(contradict, world, consequences).get("ok", true),
        "foreign snapshot shape rejected")

    # FSR-1643-M01: two contract-compatible but substituted script providers
    # cannot inject arbitrary allegedly reviewed narrative facts/consent.
    _expect(not model.build_view(frozen, FakeWorld.new(), consequences).get("ok", true),
        "forged World provider must not authorize arbitrary title")
    _expect(not model.build_view(frozen, world, FakeConsequence.new()).get("ok", true),
        "forged consequence provider must not authorize arbitrary assent text")
    _expect(not model.build_view(frozen, null, consequences).get("ok", true),
        "missing World provider rejected")
    _expect(not model.build_view(frozen, world, null).get("ok", true),
        "missing consequence provider rejected")

    var injected: Dictionary = frozen.duplicate(true)
    var private_list: Array = injected["history"]
    private_list.append("ANWEN_PRIVATE_PROVENANCE")
    rejected = model.build_view(injected, world, consequences)
    _expect(not rejected.get("ok", true)
        and not String(rejected.get("text", "")).contains("ANWEN"),
        "unknown private ID rejected without echo")
    _expect(not model.build_view({"mystery_state":"UNKNOWN_BY_DESIGN", "history":[77]}, world, consequences).get("ok", true),
        "malformed non-string history rejected")
    _expect(not model.build_view({"mystery_state":"KNOWN", "history":[]}, world, consequences).get("ok", true),
        "promoted mystery truth rejected")
    _expect(not model.build_view({"mystery_state":"UNKNOWN_BY_DESIGN", "history":"fake"}, world, consequences).get("ok", true),
        "non-array history rejected")
    _expect(not model.build_view(null, world, consequences).get("ok", true),
        "missing snapshot rejected")

    # Genuine repair choice, completion and later explicit reconsideration
    # remain valid; old completion flags may persist after re-opening as in
    # the real controller's currently reviewed state transitions.
    session.reset()
    for event_id in [
        "PUBLIC_RECORD_REVIEWED", "MATERIAL_TRACE_INSPECTED",
        "COMMONS_HEARING_OPENED", "COMMITMENT_REPAIR_PILOT",
        "BOUNDED_REPAIR_PILOT_STARTED",
    ]:
        _append_published(session, event_id)
    _expect(model.build_view(session.snapshot(), world, consequences).get("ok", false),
        "genuine repair pilot completion accepted")
    _append_published(session, "COMMONS_HEARING_OPENED")
    _append_published(session, "COMMITMENT_RECORDS_FIRST")
    _expect(model.build_view(session.snapshot(), world, consequences).get("ok", false),
        "reopened hearing may choose records while previous repair outcome still recorded")
    _append_published(session, "RECORDS_FIRST_PACKAGE_FILED")
    _expect(model.build_view(session.snapshot(), world, consequences).get("ok", false),
        "new completion after reconsideration remains a valid history")

    # FSR-1643-M02: repeated legal hearing/nonconsent creates many *real*
    # events. Each page is finite, deterministic, ordered and explicitly
    # navigable; original SessionState history stays complete/unchanged.
    session.reset()
    _append_published(session, "PUBLIC_RECORD_REVIEWED")
    _append_published(session, "TRUTH_CONCLUSION_DEFERRED")
    _append_published(session, "COMMONS_HEARING_OPENED")
    for _i in range(18):
        _append_published(session, "PUBLIC_COMMITMENT_DEFERRED")
        _append_published(session, "COMMONS_HEARING_OPENED")
    var many: Dictionary = session.snapshot()
    var total_events: int = many["history"].size()
    var expected_pages: int = int(ceil(float(total_events) / float(model.PAGE_SIZE)))
    var recovered_events: Array = []
    for page_index in range(expected_pages):
        var page_view: Dictionary = model.build_view(many, world, consequences, page_index)
        _expect(page_view.get("ok", false) and page_view.get("count") == total_events
            and page_view.get("page") == page_index
            and page_view.get("page_count") == expected_pages,
            "page metadata accurately declares complete underlying history")
        var items: Array = page_view.get("entries", [])
        _expect(items.size() <= model.PAGE_SIZE and String(page_view.get("text", "")).length() < 1000,
            "finite page always bounded to eight real events")
        _expect(page_view.get("has_previous") == (page_index > 0)
            and page_view.get("has_next") == (page_index + 1 < expected_pages),
            "navigation flags expose hidden preceding/following pages")
        for item in items:
            _expect(item["index"] == recovered_events.size() + 1,
                "numbered history index preserved across pages")
            recovered_events.append(item["event_id"])
    _expect(recovered_events == many["history"],
        "all original order and duplicate nonconsent/hearing events recoverable by paging")
    _expect(session.snapshot() == many, "pagination never drops or mutates source history")
    _expect(not model.build_view(many, world, consequences, expected_pages).get("ok", true),
        "nonexistent later page fail closed")
    _expect(not model.build_view(many, world, consequences, -1).get("ok", true),
        "negative page index fail closed")

    var too_many: Dictionary = initial.duplicate(true)
    too_many["record_read"] = true
    var over_limit: Array = []
    for _i in range(model.MAX_HISTORY_EVENTS + 1):
        over_limit.append("PUBLIC_RECORD_REVIEWED")
    too_many["history"] = over_limit
    _expect(not model.build_view(too_many, world, consequences).get("ok", true),
        "explicit oversize input cap fails closed without silent truncated claims")
    _expect(model.build_view(many, world, consequences, 0).get("ok", false),
        "maximum input negative does not poison future valid projections")

    session.reset()
    var cleared: Dictionary = model.build_view(session.snapshot(), world, consequences)
    _expect(cleared.get("ok", false) and cleared.get("count", -1) == 0,
        "reset clears history, including previous choices and nonconsent")
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
