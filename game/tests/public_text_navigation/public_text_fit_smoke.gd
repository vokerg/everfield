extends SceneTree

# Read-only empirical viewport-fit probe for the *existing published* scene.
# This is not a pagination component or proof until executed on SHA-locked
# reviewed Godot 4.7.1 against the frozen branch HEAD.
const EXPECTED_VIEWPORT := Vector2i(960, 540)
const EXPECTED_LABEL_POSITION := Vector2(500, 98)
const EXPECTED_LABEL_SIZE := Vector2(422, 134)
const EXPECTED_PANEL_POSITION := Vector2(486, 88)
const EXPECTED_PANEL_SIZE := Vector2(450, 154)

var failures: Array[String] = []

func _initialize() -> void:
    call_deferred("_run")

func _run() -> void:
    var scene_resource: Resource = load("res://main.tscn")
    if not scene_resource is PackedScene:
        _fail("published main scene is not a PackedScene")
        _finish(0, 0)
        return

    var scene: Node = (scene_resource as PackedScene).instantiate()
    # SceneTree --headless --script starts with a 64x64 root even when project.godot
    # declares 960x540 (and CLI --resolution may be ignored). Establish the
    # actual published canvas geometry explicitly before measuring any Label.
    root.size = EXPECTED_VIEWPORT
    await process_frame
    root.add_child(scene)
    await process_frame

    var label: Label = scene.get_node_or_null("Presentation") as Label
    var panel: ColorRect = scene.get_node_or_null("PresentationPanel") as ColorRect
    if label == null or panel == null:
        _fail("published exact Presentation/PresentationPanel nodes missing")
        _finish(0, 0)
        return

    _expect(root.size == EXPECTED_VIEWPORT, "must run at exact published 960x540 viewport")
    _expect(Vector2i(root.get_visible_rect().size) == EXPECTED_VIEWPORT,
        "actual visible root rectangle must be 960x540")
    _expect(label.position == EXPECTED_LABEL_POSITION, "published label origin changed")
    _expect(label.size == EXPECTED_LABEL_SIZE, "published 422x134 label changed")
    _expect(panel.position == EXPECTED_PANEL_POSITION, "published panel origin changed")
    _expect(panel.size == EXPECTED_PANEL_SIZE, "published 450x154 panel changed")
    _expect(label.autowrap_mode == TextServer.AUTOWRAP_WORD_SMART, "published word-smart wrapping changed")
    _expect(label.get_theme_font_size("font_size") == 12, "published label font-size changed")

    if not scene.has_method("get_game_state"):
        _fail("published main scene state snapshot unavailable")
        _finish(0, 0)
        return
    var original_state: Dictionary = scene.get_game_state().duplicate(true)
    var presenter: Variant = scene.get("playable_presentation")
    if presenter == null:
        _fail("published reviewed presentation provider unavailable")
        _finish(0, 0)
        return

    # Every value is composed from *exact* reviewed provider bytes.
    # Includes opening, trace, explicit deferral, hearing, both choices and
    # consequence completion; no reworded, invented or private content.
    var scenarios: Array[Dictionary] = [
        {"name": "world_intro", "view": presenter.world_intro()},
        {"name": "world_public_record", "view": presenter.old_works_station("public_record")},
        {"name": "world_material_trace", "view": presenter.old_works_station("material_trace")},
        {"name": "world_truth_deferral", "view": presenter.old_works_station("defer_conclusion")},
        {"name": "commons_hearing_opening", "view": presenter.hearing_opening()},
        {"name": "hearing_repair", "view": presenter.hearing_route("repair_pilot")},
        {"name": "hearing_records_first", "view": presenter.hearing_route("records_first")},
        {"name": "hearing_explicit_deferral", "view": presenter.hearing_route("defer")},
        {"name": "combined_repair", "view": presenter.hearing_and_consequence("repair_pilot", "COMMITMENT_REPAIR_PILOT")},
        {"name": "combined_records_first", "view": presenter.hearing_and_consequence("records_first", "COMMITMENT_RECORDS_FIRST")},
        {"name": "combined_explicit_deferral", "view": presenter.hearing_and_consequence("defer", "PUBLIC_COMMITMENT_DEFERRED")},
        {"name": "consequence_repair_completion", "view": presenter.consequence("BOUNDED_REPAIR_PILOT_STARTED")},
        {"name": "consequence_records_completion", "view": presenter.consequence("RECORDS_FIRST_PACKAGE_FILED")},
    ]

    var measured := 0
    var overflow_count := 0
    for scenario in scenarios:
        var name: String = String(scenario["name"])
        var view: Dictionary = scenario["view"]
        if not view.get("ok", false) or typeof(view.get("text")) != TYPE_STRING:
            _fail("source refused or malformed approved scenario " + name)
            continue
        var exact_text: String = view["text"]
        if exact_text.is_empty():
            _fail("source returned empty approved scenario " + name)
            continue

        # Reset requested bounds explicitly. Godot may grow Label.size.y to its
        # content minimum after layout: that growth is evidence of budget overrun,
        # never additional authorized room inside the published fixed panel.
        label.text = exact_text
        label.size = EXPECTED_LABEL_SIZE
        await process_frame

        var line_count: int = label.get_line_count()
        var summed_line_height := 0.0
        for line_index in range(line_count):
            summed_line_height += float(label.get_line_height(line_index))
        var min_height: float = label.get_combined_minimum_size().y
        var required_height: float = maxf(min_height, summed_line_height)
        var actual_label_height: float = label.size.y
        var available_height: float = EXPECTED_LABEL_SIZE.y
        var overflow: bool = required_height > available_height + 0.5
        var label_grew: bool = actual_label_height > available_height + 0.5
        if overflow:
            overflow_count += 1
        measured += 1

        _expect(line_count > 0, "no shaped lines for " + name)
        _expect(root.size == EXPECTED_VIEWPORT, "viewport changed while measuring " + name)
        _expect(Vector2i(root.get_visible_rect().size) == EXPECTED_VIEWPORT,
            "visible canvas changed while measuring " + name)
        _expect(label.position == EXPECTED_LABEL_POSITION, "label moved for " + name)
        _expect(label.size.x == EXPECTED_LABEL_SIZE.x, "label wrap width changed for " + name)
        _expect(panel.position == EXPECTED_PANEL_POSITION and panel.size == EXPECTED_PANEL_SIZE,
            "published panel changed for " + name)
        _expect(label.text == exact_text, "published text mutated by label layout for " + name)
        # Runtime evidence for font wrapping / occupied label bounds.
        print("EVERFIELD_PUBLIC_TEXT_FIT_EVIDENCE " + JSON.stringify({
            "scenario": name,
            "viewport": [root.size.x, root.size.y],
            "label_size": [EXPECTED_LABEL_SIZE.x, EXPECTED_LABEL_SIZE.y],
            "actual_label_size": [label.size.x, actual_label_height],
            "label_autogrew_beyond_nominal_height": label_grew,
            "visible_rect": [root.get_visible_rect().size.x, root.get_visible_rect().size.y],
            "line_count": line_count,
            "minimum_height": min_height,
            "sum_line_height": summed_line_height,
            "required_height": required_height,
            "available_height": available_height,
            "overflow": overflow,
            "text_characters": exact_text.length(),
            "text_sha256": exact_text.sha256_text(),
        }))

    _expect(scene.get_game_state() == original_state, "read-only text-fit probe changed session state")
    _expect(measured == scenarios.size(), "not all exact reviewed presentation scenarios measured")
    _finish(measured, overflow_count)

func _expect(condition: bool, message: String) -> void:
    if not condition:
        _fail(message)

func _fail(message: String) -> void:
    failures.append(message)
    printerr("[EVERFIELD][PUBLIC-TEXT-FIT][FAIL] " + message)

func _finish(measured: int, overflow_count: int) -> void:
    if not failures.is_empty():
        printerr("EVERFIELD_PUBLIC_TEXT_FIT_FAIL failures=%d measured=%d" % [failures.size(), measured])
        quit(1)
        return
    # This PASS means the MEASUREMENT ran, NOT that every text fits.
    # Overflow reports text exceeding the nominal bounded PANEL budget.
    # It is not itself a pixel-crop/accessibility certification, since the
    # published Label is a non-clipped sibling of the ColorRect panel.
    # Even overflow_count=0 does not certify empirical readability.
    print("EVERFIELD_PUBLIC_TEXT_FIT_MEASURED scenarios=%d overflow_count=%d" % [measured, overflow_count])
    quit(0)
