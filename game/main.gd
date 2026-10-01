extends Node2D

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
var station_nodes: Dictionary = {}

var state: Dictionary = {}

func _ready() -> void:
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
        label.text = "%s\n%s" % [station_data["title"], station_data["hint"]]
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

    diagnostic_label = Label.new()
    diagnostic_label.name = "Diagnostic"
    diagnostic_label.position = Vector2(26, 506)
    diagnostic_label.size = Vector2(908, 26)
    diagnostic_label.add_theme_font_size_override("font_size", 13)
    add_child(diagnostic_label)

func reset_slice() -> void:
    state = {
        "record_read": false,
        "trace_inspected": false,
        "deferred_truth": false,
        "negotiation_open": false,
        "commitment": "",
        "completed": false,
        "outcome": "",
        "mystery_state": MYSTERY_STATE,
        "history": [],
    }
    if player != null:
        player.position = Vector2(92, 286)
    _set_diagnostic("EF-RESET", "Slice state reset; durable world mystery remains unresolved.")
    _refresh_hud()

func interact_nearest() -> bool:
    var station_id := _nearest_station_id()
    if station_id.is_empty():
        _set_diagnostic("EF-INTERACT-RANGE", "No interaction surface is within range.")
        return false
    return interact_with(station_id)

func interact_with(station_id: String) -> bool:
    if not STATIONS.has(station_id):
        _set_diagnostic("EF-INTERACT-UNKNOWN", "Unknown station: %s" % station_id, true)
        return false

    match station_id:
        "public_record":
            state["record_read"] = true
            _append_history("PUBLIC_RECORD_REVIEWED")
            _set_diagnostic("EF-INVESTIGATE-RECORD", "The archive records incompatible accounts; neither is promoted to truth.")
        "material_trace":
            state["trace_inspected"] = true
            _append_history("MATERIAL_TRACE_INSPECTED")
            _set_diagnostic("EF-INVESTIGATE-TRACE", "The Old Works carries independent material evidence, still insufficient to settle the cause.")
        "defer_conclusion":
            if not state["record_read"]:
                _set_diagnostic("EF-GATE-DEFER", "Review the public record before explicitly deferring a conclusion.")
                return false
            state["deferred_truth"] = true
            _append_history("TRUTH_CONCLUSION_DEFERRED")
            _set_diagnostic("EF-INVESTIGATE-DEFER", "Conclusion deferred by design; uncertainty is a legal route.")
        "commons_hearing":
            if not _investigation_ready():
                _set_diagnostic("EF-GATE-INVESTIGATION", "Read the public record and inspect the material trace or explicitly defer conclusion before negotiating.")
                return false
            state["negotiation_open"] = true
            _append_history("COMMONS_HEARING_OPENED")
            _set_diagnostic("EF-NEGOTIATE", "Choose: [1] repair pilot, [2] records-first, or [3] defer commitment.")
        "project_table":
            if String(state["commitment"]).is_empty():
                _set_diagnostic("EF-GATE-COMMITMENT", "A supported public commitment is required before the project table can close the loop.")
                return false
            state["completed"] = true
            if state["commitment"] == "repair_pilot":
                state["outcome"] = "BOUNDED_REPAIR_PILOT_STARTED"
            else:
                state["outcome"] = "RECORDS_FIRST_PACKAGE_FILED"
            _append_history(String(state["outcome"]))
            _set_diagnostic("EF-SLICE-COMPLETE", "First-playable loop complete; mystery remains UNKNOWN_BY_DESIGN.")

    _refresh_hud()
    return true

func choose_commitment(choice: String) -> bool:
    if not state["negotiation_open"]:
        _set_diagnostic("EF-GATE-NEGOTIATION", "Open the Commons Hearing before choosing a commitment.")
        return false

    match choice:
        "repair_pilot":
            state["commitment"] = "repair_pilot"
            state["negotiation_open"] = false
            _append_history("COMMITMENT_REPAIR_PILOT")
            _set_diagnostic("EF-COMMIT-REPAIR", "Repair pilot selected: bounded and conditionally reversible.")
        "records_first":
            state["commitment"] = "records_first"
            state["negotiation_open"] = false
            _append_history("COMMITMENT_RECORDS_FIRST")
            _set_diagnostic("EF-COMMIT-RECORDS", "Records-first selected: document and limit use before broader repair.")
        "defer":
            state["commitment"] = ""
            state["negotiation_open"] = false
            _append_history("PUBLIC_COMMITMENT_DEFERRED")
            _set_diagnostic("EF-COMMIT-DEFER", "Commitment deferred; the hearing may be reopened without erasing history.")
        _:
            _set_diagnostic("EF-COMMIT-UNKNOWN", "Unsupported commitment choice: %s" % choice, true)
            return false

    _refresh_hud()
    return true

func get_game_state() -> Dictionary:
    return state.duplicate(true)

func _investigation_ready() -> bool:
    return bool(state["record_read"]) and (bool(state["trace_inspected"]) or bool(state["deferred_truth"]))

func _append_history(event_id: String) -> void:
    var history: Array = state["history"]
    history.append(event_id)
    print("[EVERFIELD][STATE] %s" % event_id)

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

func _refresh_nearby_hint() -> void:
    var station_id := _nearest_station_id()
    if station_id.is_empty():
        return
    var station_data: Dictionary = STATIONS[station_id]
    objective_label.text = "[E] %s — %s" % [station_data["title"], station_data["hint"]]

func _refresh_hud() -> void:
    if objective_label == null:
        return

    if bool(state["completed"]):
        objective_label.text = "Loop complete: %s — press R to reset." % state["outcome"]
    elif not bool(state["record_read"]):
        objective_label.text = "Investigate: move with WASD/arrows; reach the Archive Ledger and press E."
    elif not _investigation_ready():
        objective_label.text = "Investigate: inspect the Material Trace OR explicitly Defer Conclusion."
    elif bool(state["negotiation_open"]):
        objective_label.text = "Commons Hearing: [1] repair pilot · [2] records-first · [3] defer commitment."
    elif String(state["commitment"]).is_empty():
        objective_label.text = "Negotiate: reach the Commons Hearing and press E."
    else:
        objective_label.text = "Commit: reach the Project Table and press E to complete the bounded loop."

    status_label.text = "Record:%s  Trace:%s  Deferred truth:%s  Commitment:%s  Mystery:%s" % [
        _flag(state["record_read"]),
        _flag(state["trace_inspected"]),
        _flag(state["deferred_truth"]),
        String(state["commitment"]) if not String(state["commitment"]).is_empty() else "none",
        state["mystery_state"],
    ]

func _set_diagnostic(code: String, message: String, is_error: bool = false) -> void:
    var line := "[%s] %s" % [code, message]
    if diagnostic_label != null:
        diagnostic_label.text = line
    if is_error:
        push_error(line)
    else:
        print("[EVERFIELD][DIAG] %s" % line)

func _flag(value: Variant) -> String:
    return "yes" if bool(value) else "no"
