extends Node2D

const OldWorksPresentation = preload("res://components/old_works_world/old_works_world_presentation.gd")
const CommonsHearingPresentation = preload("res://components/commons_hearing/commons_hearing_presentation.gd")
const CommitmentConsequencePresentation = preload("res://components/commitment_consequences/commitment_consequence_presentation.gd")
const SessionState = preload("res://components/session_state/session_state.gd")
const DiagnosticCatalog = preload("res://components/diagnostics/diagnostic_catalog.gd")
const HudObjectiveModel = preload("res://components/hud_objectives/hud_objective_model.gd")
const StationWorld = preload("res://components/station_world/station_world.gd")
const TraversalPolicy = preload("res://components/traversal_policy/traversal_policy.gd")
const PlayablePresentation = preload("res://components/playable_presentation/playable_presentation.gd")
const InteractionFeedbackPolicy = preload("res://components/interaction_feedback/interaction_feedback_policy.gd")
const ActionCommandPolicy = preload("res://components/action_commands/action_command_policy.gd")
const PublicTextNavigation = preload("res://components/public_text_navigation/public_text_navigation.gd")
const RouteHistoryView = preload("res://components/route_history_view/route_history_view.gd")

const PLAYER_SPEED := 230.0
const INTERACT_RADIUS := 88.0
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"

var player: Node2D
var title_label: Label
var objective_label: Label
var status_label: Label
var diagnostic_label: Label
var presentation_panel: ColorRect
var presentation_label: Label
var presentation_nav_label: Label
var history_label: RichTextLabel
var history_header_label: Label
var station_nodes: Dictionary = {}

var public_text_navigation: Variant
var route_history_view: Variant
var presentation_scenario := ""
var presentation_source_text := ""
var presentation_page := 0
var presentation_page_count := 0
var history_page := 0

var station_world: Variant
var playable_presentation: Variant
var old_works_presentation: Variant
var commons_hearing_presentation: Variant
var consequence_presentation: Variant
var session_state: Variant
var diagnostic_catalog: Variant
var hud_objective_model: Variant

func _ready() -> void:
    station_world = StationWorld.new()
    old_works_presentation = OldWorksPresentation.new()
    commons_hearing_presentation = CommonsHearingPresentation.new()
    consequence_presentation = CommitmentConsequencePresentation.new()
    playable_presentation = PlayablePresentation.new(old_works_presentation, commons_hearing_presentation, consequence_presentation)
    session_state = SessionState.new()
    diagnostic_catalog = DiagnosticCatalog.new()
    hud_objective_model = HudObjectiveModel.new()
    public_text_navigation = PublicTextNavigation.new()
    route_history_view = RouteHistoryView.new()
    _build_world()
    reset_slice()
    print("[EVERFIELD][BOOT] Accounts at the Old Works first playable ready")

func _process(delta: float) -> void:
    if player == null:
        return
    # Controller owns physical Input; the reviewed policy owns mapping,
    # direction cancellation, normalization, bounds and movement validation.
    var mapping: Dictionary = TraversalPolicy.key_mapping()
    var intents: Dictionary = {}
    for intent in ["left", "right", "up", "down"]:
        var keys: Array = mapping.get(intent, [])
        if keys.size() != 2:
            push_error("[EF-TRAVERSAL-INVALID] Invalid key mapping.")
            return
        intents[intent] = Input.is_key_pressed(keys[0]) or Input.is_key_pressed(keys[1])
    var sampled: Dictionary = TraversalPolicy.direction_from_intents(intents)
    if not sampled.get("ok", false):
        push_error("[EF-TRAVERSAL-INVALID] Invalid sampled key intents.")
        return
    var direction: Vector2 = sampled.get("direction", Vector2.ZERO)
    if direction != Vector2.ZERO:
        var layout: Dictionary = station_world.get_layout()
        var movement: Dictionary = TraversalPolicy.advance(
            player.position, direction, delta, PLAYER_SPEED, layout["world_bounds"]
        )
        if not movement.get("ok", false):
            push_error("[EF-TRAVERSAL-INVALID] Invalid movement step.")
            return
        player.position = movement["position"]
        _refresh_nearby_hint()

func _unhandled_key_input(event: InputEvent) -> void:
    # The published pure decoder preserves logical keycode, pressed, echo and
    # exact E/1/2/3/R meanings. Dispatch and session gates remain here.
    var command: Dictionary = ActionCommandPolicy.decode_event(event)
    if command.get("ok", false):
        match String(command.get("action", "")):
            "interact":
                interact_nearest()
            "choose_commitment":
                choose_commitment(String(command.get("choice", "")))
            "reset":
                reset_slice()
        return
    # These four keys are absent from the frozen ActionCommandPolicy and
    # TraversalPolicy maps; physical-only, released and echo events do nothing.
    if not (event is InputEventKey):
        return
    var key_event: InputEventKey = event as InputEventKey
    if not key_event.pressed or key_event.echo:
        return
    match key_event.keycode:
        KEY_Z:
            navigate_public_text(-1)
        KEY_X:
            navigate_public_text(1)
        KEY_C:
            navigate_public_history(-1)
        KEY_V:
            navigate_public_history(1)

func _build_world() -> void:
    var layout: Dictionary = station_world.get_layout()
    station_nodes.clear()
    var backdrop := Polygon2D.new()
    backdrop.name = "OldWorksFloor"
    backdrop.polygon = layout["floor_polygon"]
    backdrop.color = layout["floor_color"]
    add_child(backdrop)

    var path := Line2D.new()
    path.name = "WalkPath"
    path.width = layout["walk_path_width"]
    path.default_color = layout["walk_path_color"]
    path.points = layout["walk_path"]
    add_child(path)

    for station_id in station_world.get_station_ids():
        var station_data: Dictionary = station_world.get_station(station_id)
        var display := _station_display(String(station_id), station_data)
        var station := Node2D.new()
        station.name = String(station_id)
        station.position = station_data["position"]

        var marker := Polygon2D.new()
        marker.polygon = layout["marker_polygon"]
        marker.color = station_data["color"]
        station.add_child(marker)

        var label := Label.new()
        label.position = layout["station_label_position"]
        label.size = layout["station_label_size"]
        label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
        label.text = "%s\n%s" % [display["title"], display["hint"]]
        label.add_theme_font_size_override("font_size", 12)
        station.add_child(label)

        add_child(station)
        station_nodes[station_id] = station

    player = Node2D.new()
    player.name = "Player"
    var player_shape := Polygon2D.new()
    player_shape.polygon = PackedVector2Array([
        Vector2(0, -18), Vector2(14, 14), Vector2(0, 9), Vector2(-14, 14)
    ])
    player_shape.color = Color("f1e9d2")
    player.add_child(player_shape)
    add_child(player)

    title_label = Label.new()
    title_label.name = "Title"
    title_label.position = Vector2(24, 14)
    title_label.size = Vector2(900, 42)
    title_label.text = "EVERFIELD — Accounts at the Old Works"
    title_label.add_theme_font_size_override("font_size", 24)
    add_child(title_label)

    objective_label = Label.new()
    objective_label.name = "Objective"
    objective_label.position = Vector2(26, 474)
    objective_label.size = Vector2(908, 30)
    objective_label.add_theme_font_size_override("font_size", 16)
    add_child(objective_label)

    status_label = Label.new()
    status_label.name = "Status"
    status_label.position = Vector2(26, 52)
    status_label.size = Vector2(908, 32)
    status_label.add_theme_font_size_override("font_size", 14)
    add_child(status_label)

    presentation_panel = ColorRect.new()
    presentation_panel.name = "PresentationPanel"
    presentation_panel.position = Vector2(486, 88)
    presentation_panel.size = Vector2(450, 154)
    presentation_panel.color = Color(0.035, 0.047, 0.055, 0.94)
    presentation_panel.z_index = 5
    add_child(presentation_panel)

    presentation_label = Label.new()
    presentation_label.name = "Presentation"
    presentation_label.position = Vector2(500, 98)
    presentation_label.size = Vector2(422, 134)
    presentation_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
    presentation_label.vertical_alignment = VERTICAL_ALIGNMENT_TOP
    presentation_label.add_theme_font_size_override("font_size", 12)
    presentation_label.z_index = 6
    add_child(presentation_label)

    presentation_nav_label = Label.new()
    presentation_nav_label.name = "PresentationNavigation"
    presentation_nav_label.position = Vector2(500, 242)
    presentation_nav_label.size = Vector2(422, 22)
    presentation_nav_label.add_theme_font_size_override("font_size", 12)
    presentation_nav_label.z_index = 6
    add_child(presentation_nav_label)

    var history_panel := ColorRect.new()
    history_panel.name = "HistoryPanel"
    history_panel.position = Vector2(486, 276)
    history_panel.size = Vector2(450, 182)
    history_panel.color = Color(0.035, 0.047, 0.055, 0.94)
    history_panel.z_index = 5
    add_child(history_panel)

    history_header_label = Label.new()
    history_header_label.name = "HistoryHeader"
    history_header_label.position = Vector2(500, 282)
    history_header_label.size = Vector2(422, 24)
    history_header_label.add_theme_font_size_override("font_size", 12)
    history_header_label.z_index = 6
    add_child(history_header_label)

    # RichTextLabel has an actual scrollbar for long reviewed public titles;
    # never clip or silently omit any of the eight entries on a model page.
    history_label = RichTextLabel.new()
    history_label.name = "History"
    history_label.position = Vector2(500, 308)
    history_label.size = Vector2(422, 140)
    history_label.fit_content = false
    history_label.scroll_active = true
    history_label.bbcode_enabled = false
    history_label.add_theme_font_size_override("normal_font_size", 12)
    history_label.z_index = 6
    add_child(history_label)

    diagnostic_label = Label.new()
    diagnostic_label.name = "Diagnostic"
    diagnostic_label.position = Vector2(26, 506)
    diagnostic_label.size = Vector2(908, 26)
    diagnostic_label.add_theme_font_size_override("font_size", 13)
    add_child(diagnostic_label)

func reset_slice() -> void:
    session_state.reset()
    history_page = 0
    if player != null:
        player.position = station_world.get_layout()["player_spawn"]
    _emit_diagnostic("EF-RESET")
    _show_world_intro()
    _refresh_history_view()
    _refresh_hud()

func interact_nearest() -> bool:
    var station_id := _nearest_station_id()
    if station_id.is_empty():
        _emit_diagnostic("EF-INTERACT-RANGE")
        return false
    return interact_with(station_id)

func interact_with(station_id: String) -> bool:
    if not station_world.has_station(station_id):
        _emit_diagnostic("EF-INTERACT-UNKNOWN", {"station_id": station_id})
        return false

    var current: Dictionary = get_game_state()
    match station_id:
        "public_record":
            if not session_state.set_field("record_read", true):
                return false
            if not _append_history("PUBLIC_RECORD_REVIEWED"):
                return false
            _show_old_works_station("public_record")
            _emit_diagnostic("EF-INVESTIGATE-RECORD")
        "material_trace":
            if not session_state.set_field("trace_inspected", true):
                return false
            if not _append_history("MATERIAL_TRACE_INSPECTED"):
                return false
            _show_old_works_station("material_trace")
            _emit_diagnostic("EF-INVESTIGATE-TRACE")
        "defer_conclusion":
            if not bool(current["record_read"]):
                _emit_diagnostic("EF-GATE-DEFER")
                return false
            if not session_state.set_field("deferred_truth", true):
                return false
            if not _append_history("TRUTH_CONCLUSION_DEFERRED"):
                return false
            _show_old_works_station("defer_conclusion")
            _emit_diagnostic("EF-INVESTIGATE-DEFER")
        "commons_hearing":
            if not _investigation_ready():
                _emit_diagnostic("EF-GATE-INVESTIGATION")
                return false
            if not session_state.set_field("negotiation_open", true):
                return false
            if not _append_history("COMMONS_HEARING_OPENED"):
                return false
            _show_hearing_opening()
            _emit_diagnostic("EF-NEGOTIATE")
        "project_table":
            var commitment := String(current["commitment"])
            if commitment.is_empty():
                _emit_diagnostic("EF-GATE-COMMITMENT")
                return false
            var outcome := "BOUNDED_REPAIR_PILOT_STARTED" if commitment == "repair_pilot" else "RECORDS_FIRST_PACKAGE_FILED"
            if not session_state.set_field("outcome", outcome):
                return false
            if not session_state.set_field("completed", true):
                return false
            if not _append_history(outcome):
                return false
            _show_consequence(outcome)
            _emit_diagnostic("EF-SLICE-COMPLETE")

    _refresh_hud()
    return true

func choose_commitment(choice: String) -> bool:
    if not bool(get_game_state()["negotiation_open"]):
        _emit_diagnostic("EF-GATE-NEGOTIATION")
        return false

    match choice:
        "repair_pilot":
            if not session_state.set_field("commitment", "repair_pilot"):
                return false
            if not session_state.set_field("negotiation_open", false):
                return false
            if not _append_history("COMMITMENT_REPAIR_PILOT"):
                return false
            _show_hearing_and_consequence("repair_pilot", "COMMITMENT_REPAIR_PILOT")
            _emit_diagnostic("EF-COMMIT-REPAIR")
        "records_first":
            if not session_state.set_field("commitment", "records_first"):
                return false
            if not session_state.set_field("negotiation_open", false):
                return false
            if not _append_history("COMMITMENT_RECORDS_FIRST"):
                return false
            _show_hearing_and_consequence("records_first", "COMMITMENT_RECORDS_FIRST")
            _emit_diagnostic("EF-COMMIT-RECORDS")
        "defer":
            if not session_state.set_field("commitment", ""):
                return false
            if not session_state.set_field("negotiation_open", false):
                return false
            if not _append_history("PUBLIC_COMMITMENT_DEFERRED"):
                return false
            _show_hearing_and_consequence("defer", "PUBLIC_COMMITMENT_DEFERRED")
            _emit_diagnostic("EF-COMMIT-DEFER")
        _:
            _emit_diagnostic("EF-COMMIT-UNKNOWN", {"choice": choice})
            return false

    _refresh_hud()
    return true

func get_game_state() -> Dictionary:
    # A deep-copy snapshot is the only public state view; gameplay state lives
    # exclusively inside the reviewed bounded session-state component.
    return session_state.snapshot()

func get_presentation_text() -> String:
    # Compatibility audit accessor: the COMPLETE reviewed source, never a
    # silently cropped first page. Use get_visible_presentation_text for UI.
    return presentation_source_text

func get_visible_presentation_text() -> String:
    return presentation_label.text if presentation_label != null else ""

func get_visible_history_text() -> String:
    return history_label.text if history_label != null else ""

func get_hud_view() -> Dictionary:
    return hud_objective_model.build_view(get_game_state(), _hud_station_metadata())

func _hud_station_metadata() -> Dictionary:
    var metadata := {}
    for station_id in station_world.get_station_ids():
        var station_data: Dictionary = station_world.get_station(station_id)
        metadata[station_id] = {"title": String(_station_display(station_id, station_data)["title"])}
    return metadata

func _investigation_ready() -> bool:
    var current: Dictionary = get_game_state()
    return bool(current["record_read"]) and (bool(current["trace_inspected"]) or bool(current["deferred_truth"]))

func _append_history(event_id: String) -> bool:
    if not session_state.append_history(event_id):
        return false
    print("[EVERFIELD][STATE] %s" % event_id)
    # Auto-follow the latest completed bounded history page, but never alter
    # session state to change public projection/presentation position.
    var history_size: int = (session_state.snapshot().get("history", []) as Array).size()
    history_page = int((history_size - 1) / RouteHistoryView.PAGE_SIZE) if history_size > 0 else 0
    _refresh_history_view()
    return true

func _nearest_station_id() -> String:
    if player == null:
        return ""
    var nearest: Dictionary = TraversalPolicy.nearest_station(
        player.position, station_world.get_stations(), station_world.get_station_ids(), INTERACT_RADIUS
    )
    if not nearest.get("ok", false):
        push_error("[EF-TRAVERSAL-INVALID] Invalid station proximity metadata.")
        return ""
    return String(nearest.get("station_id", ""))

func _station_display(station_id: String, fallback: Dictionary) -> Dictionary:
    var display := {
        "title": String(fallback.get("title", "")),
        "hint": String(fallback.get("hint", "")),
    }
    if not ["public_record", "material_trace", "defer_conclusion"].has(station_id):
        return display

    var station: Dictionary = old_works_presentation.get_station(station_id)
    if station.is_empty():
        return display
    var title_id := String(station.get("title_id", ""))
    var prompt_id := String(station.get("prompt_id", ""))
    if old_works_presentation.has_text(title_id):
        display["title"] = old_works_presentation.get_text(title_id)
    if old_works_presentation.has_text(prompt_id):
        display["hint"] = old_works_presentation.get_text(prompt_id)
    return display

func _show_world_intro() -> void:
    _show_public_view(playable_presentation.world_intro(), "world_intro")

func _show_old_works_station(station_id: String) -> void:
    var scenes := {
        "public_record": "world_public_record",
        "material_trace": "world_material_trace",
        "defer_conclusion": "world_truth_deferral",
    }
    _show_public_view(playable_presentation.old_works_station(station_id), String(scenes.get(station_id, "")))

func _show_hearing_opening() -> void:
    _show_public_view(playable_presentation.hearing_opening(), "commons_hearing_opening")

func _show_hearing_and_consequence(route_scope: String, event_id: String) -> void:
    var scenes := {
        "repair_pilot": "combined_repair",
        "records_first": "combined_records_first",
        "defer": "combined_explicit_deferral",
    }
    _show_public_view(playable_presentation.hearing_and_consequence(route_scope, event_id), String(scenes.get(route_scope, "")))

func _show_consequence(event_id: String) -> void:
    var scenes := {
        "BOUNDED_REPAIR_PILOT_STARTED": "consequence_repair_completion",
        "RECORDS_FIRST_PACKAGE_FILED": "consequence_records_completion",
    }
    _show_public_view(playable_presentation.consequence(event_id), String(scenes.get(event_id, "")))

func _show_public_view(view: Dictionary, scenario: String) -> void:
    # Source approval is independently checked against the published pure
    # navigation model; an arbitrary caller view cannot inject visible prose.
    var first: Dictionary = public_text_navigation.page_view(scenario)
    if not view.get("ok", false) or typeof(view.get("text")) != TYPE_STRING or not first.get("ok", false):
        _invalid_public_view()
        return
    var expected: String = String(view["text"])
    if expected.is_empty() or first.get("source_sha256") != expected.sha256_text():
        _invalid_public_view()
        return
    var complete := ""
    for index in range(int(first["page_count"])):
        var piece: Dictionary = public_text_navigation.page_view(scenario, index)
        if not piece.get("ok", false):
            _invalid_public_view()
            return
        complete += String(piece["text"])
    if complete != expected:
        _invalid_public_view()
        return
    presentation_scenario = scenario
    presentation_source_text = complete
    presentation_page = 0
    presentation_page_count = int(first["page_count"])
    _render_public_page(first)

func _invalid_public_view() -> void:
    presentation_scenario = ""
    presentation_source_text = ""
    presentation_page = 0
    presentation_page_count = 0
    _set_presentation("[EF-PRESENTATION-INVALID] Reviewed public text unavailable.")
    if presentation_nav_label != null:
        presentation_nav_label.text = ""

func _render_public_page(view: Dictionary) -> void:
    if not view.get("ok", false) or view.get("source_sha256") != presentation_source_text.sha256_text():
        _invalid_public_view()
        return
    presentation_page = int(view["page_index"])
    _set_presentation(String(view["text"]))
    if presentation_nav_label != null:
        presentation_nav_label.text = (
            "Page %d/%d    [Z] Previous    [X] Next" %
            [presentation_page + 1, presentation_page_count]
        ) if presentation_page_count > 1 else ""

func navigate_public_text(direction: int) -> bool:
    if direction != -1 and direction != 1:
        return false
    if presentation_scenario.is_empty():
        return false
    var view: Dictionary = public_text_navigation.navigate(presentation_scenario, presentation_page, direction)
    if not view.get("ok", false):
        return false
    if view.get("source_sha256") != presentation_source_text.sha256_text():
        return false
    _render_public_page(view)
    return true

func _refresh_history_view() -> void:
    if history_label == null or history_header_label == null:
        return
    # Genuine state source: the only accepted provenance is SessionState's
    # own deep-copy snapshot and the exact reviewed World/Consequence scripts.
    var view: Dictionary = route_history_view.build_view(
        session_state.snapshot(), old_works_presentation, consequence_presentation, history_page
    )
    if not view.get("ok", false):
        history_label.text = "[EF-ROUTE-HISTORY-INVALID] Public route history unavailable."
        history_header_label.text = "Public history unavailable"
        return
    history_label.text = String(view["text"])
    history_header_label.text = "Public history: %d events" % int(view["count"])
    if int(view["page_count"]) > 1:
        history_header_label.text += "  %d/%d [C] Prev [V] Next" % [
            history_page + 1, int(view["page_count"])
        ]

func navigate_public_history(direction: int) -> bool:
    if direction != -1 and direction != 1:
        return false
    var candidate_page: int = history_page + direction
    var view: Dictionary = route_history_view.build_view(
        session_state.snapshot(), old_works_presentation, consequence_presentation, candidate_page
    )
    if not view.get("ok", false):
        return false
    history_page = candidate_page
    _refresh_history_view()
    return true

func _set_presentation(text: String) -> void:
    if presentation_label != null:
        presentation_label.text = text
    print("[EVERFIELD][PRESENTATION-PAGE] %s" % text.replace("\n", " | "))

func _refresh_nearby_hint() -> void:
    # Movement must arbitrate again even after walking out of range. The old
    # early return left the most recent [E] prompt visibly stale.
    _refresh_hud()

func _refresh_hud() -> void:
    if objective_label == null or status_label == null:
        return
    var view: Dictionary = get_hud_view()
    var station_id := _nearest_station_id()
    var display: Dictionary = {}
    if not station_id.is_empty():
        # Both IDs and public text come from existing reviewed providers;
        # malformed/unknown nearest data never authorizes a new action.
        var station_data: Dictionary = station_world.get_station(station_id)
        display = _station_display(station_id, station_data)
    var objective: Dictionary = InteractionFeedbackPolicy.objective_view(
        view, station_id, display, station_world.get_station_ids()
    )
    objective_label.text = String(objective.get(
        "objective", "[EF-HUD-STATE] Invalid bounded session state. Progress is not inferred."
    ))
    status_label.text = String(view.get("status", "Mystery:UNKNOWN_BY_DESIGN"))

func _emit_diagnostic(code: String, context: Dictionary = {}) -> void:
    # The published catalog owns all messages, dynamic context and error flags.
    # Missing/unknown codes are returned as visibly fail-closed errors.
    var payload: Dictionary = diagnostic_catalog.get_diagnostic(code, context)
    var line := "[%s] %s" % [payload["code"], payload["message"]]
    if diagnostic_label != null:
        diagnostic_label.text = line
    if not bool(payload.get("ok", false)) or bool(payload.get("is_error", true)):
        push_error(line)
    else:
        print("[EVERFIELD][DIAG] %s" % line)
