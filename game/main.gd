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

const PLAYER_SPEED := 230.0
const INTERACT_RADIUS := 88.0
const WORLD_BOUNDS := Rect2(36.0, 90.0, 888.0, 414.0)
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"

const STATIONS := {
    "public_record": {
        "position": Vector2(176, 188),
        "title": "Archive Ledger",
        "hint": "Public record — required",
        "color": Color("6ca6c8"),
    },
    "material_trace": {
        "position": Vector2(338, 382),
        "title": "Material Trace",
        "hint": "Independent evidence — optional",
        "color": Color("c3a56f"),
    },
    "defer_conclusion": {
        "position": Vector2(498, 184),
        "title": "Defer Conclusion",
        "hint": "Legal investigation alternative",
        "color": Color("8d88ba"),
    },
    "commons_hearing": {
        "position": Vector2(676, 252),
        "title": "Commons Hearing",
        "hint": "Negotiate shared use",
        "color": Color("7dbb8b"),
    },
    "project_table": {
        "position": Vector2(798, 400),
        "title": "Project Table",
        "hint": "Commit the bounded next step",
        "color": Color("d28d7b"),
    },
}

var player: Node2D
var title_label: Label
var objective_label: Label
var status_label: Label
var diagnostic_label: Label
var presentation_panel: ColorRect
var presentation_label: Label
var station_nodes: Dictionary = {}

var old_works_presentation: Variant
var commons_hearing_presentation: Variant
var consequence_presentation: Variant
var session_state: Variant
var diagnostic_catalog: Variant
var hud_objective_model: Variant

func _ready() -> void:
    old_works_presentation = OldWorksPresentation.new()
    commons_hearing_presentation = CommonsHearingPresentation.new()
    consequence_presentation = CommitmentConsequencePresentation.new()
    session_state = SessionState.new()
    diagnostic_catalog = DiagnosticCatalog.new()
    hud_objective_model = HudObjectiveModel.new()
    _build_world()
    reset_slice()
    print("[EVERFIELD][BOOT] Accounts at the Old Works first playable ready")

func _process(delta: float) -> void:
    if player == null:
        return

    var direction := Vector2.ZERO
    if Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
        direction.x -= 1.0
    if Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
        direction.x += 1.0
    if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
        direction.y -= 1.0
    if Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
        direction.y += 1.0

    if direction != Vector2.ZERO:
        player.position += direction.normalized() * PLAYER_SPEED * delta
        player.position.x = clampf(player.position.x, WORLD_BOUNDS.position.x, WORLD_BOUNDS.position.x + WORLD_BOUNDS.size.x)
        player.position.y = clampf(player.position.y, WORLD_BOUNDS.position.y, WORLD_BOUNDS.position.y + WORLD_BOUNDS.size.y)
        _refresh_nearby_hint()

func _unhandled_key_input(event: InputEvent) -> void:
    if not (event is InputEventKey):
        return
    var key_event := event as InputEventKey
    if not key_event.pressed or key_event.echo:
        return

    match key_event.keycode:
        KEY_E:
            interact_nearest()
        KEY_1:
            choose_commitment("repair_pilot")
        KEY_2:
            choose_commitment("records_first")
        KEY_3:
            choose_commitment("defer")
        KEY_R:
            reset_slice()

func _build_world() -> void:
    var backdrop := Polygon2D.new()
    backdrop.name = "OldWorksFloor"
    backdrop.polygon = PackedVector2Array([
        Vector2(22, 74), Vector2(938, 74), Vector2(938, 516), Vector2(22, 516)
    ])
    backdrop.color = Color("172129")
    add_child(backdrop)

    var path := Line2D.new()
    path.name = "WalkPath"
    path.width = 9.0
    path.default_color = Color("34444e")
    path.points = PackedVector2Array([
        Vector2(92, 286), Vector2(176, 188), Vector2(338, 382),
        Vector2(498, 184), Vector2(676, 252), Vector2(798, 400)
    ])
    add_child(path)

    for station_id in STATIONS:
        var station_data: Dictionary = STATIONS[station_id]
        var display := _station_display(String(station_id), station_data)
        var station := Node2D.new()
        station.name = String(station_id)
        station.position = station_data["position"]

        var marker := Polygon2D.new()
        marker.polygon = PackedVector2Array([
            Vector2(-20, -20), Vector2(20, -20), Vector2(20, 20), Vector2(-20, 20)
        ])
        marker.color = station_data["color"]
        station.add_child(marker)

        var label := Label.new()
        label.position = Vector2(-74, -52)
        label.size = Vector2(148, 44)
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

    diagnostic_label = Label.new()
    diagnostic_label.name = "Diagnostic"
    diagnostic_label.position = Vector2(26, 506)
    diagnostic_label.size = Vector2(908, 26)
    diagnostic_label.add_theme_font_size_override("font_size", 13)
    add_child(diagnostic_label)

func reset_slice() -> void:
    session_state.reset()
    if player != null:
        player.position = Vector2(92, 286)
    _emit_diagnostic("EF-RESET")
    _show_world_intro()
    _refresh_hud()

func interact_nearest() -> bool:
    var station_id := _nearest_station_id()
    if station_id.is_empty():
        _emit_diagnostic("EF-INTERACT-RANGE")
        return false
    return interact_with(station_id)

func interact_with(station_id: String) -> bool:
    if not STATIONS.has(station_id):
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
    return presentation_label.text if presentation_label != null else ""

func get_hud_view() -> Dictionary:
    return hud_objective_model.build_view(get_game_state(), _hud_station_metadata())

func _hud_station_metadata() -> Dictionary:
    var metadata := {}
    for station_id in STATIONS:
        var station_data: Dictionary = STATIONS[station_id]
        metadata[station_id] = {"title": String(_station_display(String(station_id), station_data)["title"])}
    return metadata

func _investigation_ready() -> bool:
    var current: Dictionary = get_game_state()
    return bool(current["record_read"]) and (bool(current["trace_inspected"]) or bool(current["deferred_truth"]))

func _append_history(event_id: String) -> bool:
    if not session_state.append_history(event_id):
        return false
    print("[EVERFIELD][STATE] %s" % event_id)
    return true

func _nearest_station_id() -> String:
    if player == null:
        return ""
    var best_id := ""
    var best_distance := INF
    for station_id in STATIONS:
        var station_position: Vector2 = STATIONS[station_id]["position"]
        var distance := player.position.distance_to(station_position)
        if distance < best_distance:
            best_distance = distance
            best_id = String(station_id)
    return best_id if best_distance <= INTERACT_RADIUS else ""

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
    var lines: Array = [
        old_works_presentation.get_text("OW_WORLD_TITLE"),
        old_works_presentation.get_text("OW_WORLD_SUBTITLE"),
        old_works_presentation.get_text("OW_WORLD_ENTRY"),
    ]
    _set_presentation(_join_lines(lines))

func _show_old_works_station(station_id: String) -> void:
    var station: Dictionary = old_works_presentation.get_station(station_id)
    if station.is_empty():
        _set_presentation("Presentation unavailable for %s." % station_id)
        return

    var lines: Array = []
    for key in ["title_id", "prompt_id"]:
        var text_id := String(station.get(key, ""))
        if not text_id.is_empty():
            lines.append(old_works_presentation.get_text(text_id))
    for body_id in station.get("body_ids", []):
        lines.append(old_works_presentation.get_text(String(body_id)))
    for key in ["exit_id", "result_id"]:
        var text_id := String(station.get(key, ""))
        if not text_id.is_empty():
            lines.append(old_works_presentation.get_text(text_id))
    _set_presentation(_join_lines(lines))

func _show_hearing_opening() -> void:
    var maelin: Dictionary = commons_hearing_presentation.get_participant("OW_HEARING_PARTICIPANT_MAELIN_01")
    var selka: Dictionary = commons_hearing_presentation.get_participant("OW_HEARING_PARTICIPANT_SELKA_01")
    var maelin_line: Dictionary = commons_hearing_presentation.get_line("OW_HEARING_OPEN_MAELIN_01")
    var selka_line: Dictionary = commons_hearing_presentation.get_line("OW_HEARING_OPEN_SELKA_01")
    var lines: Array = [
        "Commons Hearing",
        "%s — %s" % [maelin.get("display_name", "Maelin Sor"), maelin_line.get("text", "")],
        "%s — %s" % [selka.get("display_name", "Selka Vey"), selka_line.get("text", "")],
        "Refusal, deferral, and nonalignment remain legal outcomes.",
    ]
    _set_presentation(_join_lines(lines))

func _hearing_route_text(route_scope: String) -> String:
    var beat_ids: Array = []
    match route_scope:
        "repair_pilot":
            beat_ids = ["OW_HEARING_REPAIR_MAELIN_01", "OW_HEARING_REPAIR_SELKA_01"]
        "records_first":
            beat_ids = ["OW_HEARING_RECORDS_MAELIN_01", "OW_HEARING_RECORDS_SELKA_01"]
        "defer":
            beat_ids = ["OW_HEARING_DEFER_MAELIN_01", "OW_HEARING_DEFER_SELKA_01"]
        _:
            return ""

    var lines: Array = ["Commons Hearing — %s" % route_scope.replace("_", " ")]
    for beat_id in beat_ids:
        var beat: Dictionary = commons_hearing_presentation.get_line(String(beat_id))
        var speaker := _speaker_name(String(beat.get("speaker_ref", "")))
        lines.append("%s — %s" % [speaker, beat.get("text", "")])
    return _join_lines(lines)

func _speaker_name(character_ref: String) -> String:
    if character_ref == "CHAR:maelin_sor":
        return String(commons_hearing_presentation.get_participant("OW_HEARING_PARTICIPANT_MAELIN_01").get("display_name", "Maelin Sor"))
    if character_ref == "CHAR:selka_vey":
        return String(commons_hearing_presentation.get_participant("OW_HEARING_PARTICIPANT_SELKA_01").get("display_name", "Selka Vey"))
    return "Unknown participant"

func _consequence_text(event_id: String) -> String:
    var event: Dictionary = consequence_presentation.get_event(event_id)
    if event.is_empty():
        return "Consequence presentation unavailable for %s." % event_id
    var lines: Array = []
    for text_id in event.get("ids", []):
        lines.append(consequence_presentation.get_text(String(text_id)))
    return _join_lines(lines)

func _show_hearing_and_consequence(route_scope: String, event_id: String) -> void:
    _set_presentation("%s\n\n%s" % [_hearing_route_text(route_scope), _consequence_text(event_id)])

func _show_consequence(event_id: String) -> void:
    _set_presentation(_consequence_text(event_id))

func _set_presentation(text: String) -> void:
    if presentation_label != null:
        presentation_label.text = text
    print("[EVERFIELD][PRESENTATION] %s" % text.replace("\n", " | "))

func _join_lines(lines: Array) -> String:
    var result := ""
    for line in lines:
        var text := String(line)
        if text.is_empty():
            continue
        if not result.is_empty():
            result += "\n"
        result += text
    return result

func _refresh_nearby_hint() -> void:
    var station_id := _nearest_station_id()
    if station_id.is_empty():
        return
    var station_data: Dictionary = STATIONS[station_id]
    var display := _station_display(station_id, station_data)
    objective_label.text = "[E] %s — %s" % [display["title"], display["hint"]]

func _refresh_hud() -> void:
    if objective_label == null or status_label == null:
        return
    var view: Dictionary = get_hud_view()
    objective_label.text = String(view.get("objective", "[EF-HUD-STATE] Invalid bounded session state."))
    if view.get("phase", "") == "COMPLETE":
        objective_label.text += " Press R to reset."
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
