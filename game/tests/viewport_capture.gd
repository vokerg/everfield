extends SceneTree

# Capture authentic rendered pixels under a virtual X11 display.
# This is visual diagnostic evidence, NOT an accessibility certificate,
# a physical keyboard test or authority to revise reviewed narrative text.
const EXPECTED_VIEWPORT := Vector2i(960, 540)

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var destination := OS.get_environment("EVERFIELD_CAPTURE_DIR")
    if destination.is_empty():
        _fail("missing required screenshot output directory")
        return
    var scene := load("res://main.tscn") as PackedScene
    if scene == null:
        _fail("main scene could not be loaded")
        return
    var game: Node = scene.instantiate()
    get_root().add_child(game)
    await process_frame
    if get_root().size != EXPECTED_VIEWPORT:
        _fail("unexpected actual root viewport: %s" % get_root().size)
        return
    if not await _capture(destination, "01-intro"):
        return

    var help: ColorRect = game.get_node_or_null("HelpPanel") as ColorRect
    if help == null:
        _fail("existing help panel is unavailable")
        return
    help.visible = true
    if not await _capture(destination, "02-controls-help"):
        return
    game.reset_slice()

    if not game.interact_with("public_record") or not game.interact_with("defer_conclusion"):
        _fail("real session could not complete the reviewed investigation")
        return
    if not game.interact_with("commons_hearing"):
        _fail("real session could not open reviewed hearing")
        return
    if not await _capture(destination, "03-commons-hearing"):
        return

    if not game.choose_commitment("repair_pilot") or not game.interact_with("project_table"):
        _fail("real session could not complete reviewed repair route")
        return
    if not bool(game.get_game_state().get("completed", false)):
        _fail("game did not actually complete")
        return
    if not await _capture(destination, "04-repair-consequence"):
        return
    print("EVERFIELD_RENDERED_VIEWPORT_CAPTURE_PASS screenshots=4 width=960 height=540")
    quit(0)


func _capture(directory: String, label: String) -> bool:
    # Wait for actual drawing, not a mocked model snapshot.
    await process_frame
    await process_frame
    await RenderingServer.frame_post_draw
    var captured: Image = get_root().get_texture().get_image()
    if captured == null or captured.is_empty():
        _fail("empty GPU framebuffer for %s" % label)
        return false
    if Vector2i(captured.get_width(), captured.get_height()) != EXPECTED_VIEWPORT:
        _fail("wrong PNG pixel size for %s: %dx%d" % [
            label, captured.get_width(), captured.get_height()
        ])
        return false
    var unique_colors := {}
    for y in range(0, captured.get_height(), 20):
        for x in range(0, captured.get_width(), 20):
            unique_colors[captured.get_pixel(x, y).to_html()] = true
    if unique_colors.size() < 5:
        _fail("blank/uniform screenshot rejected for %s (%d colors)" % [
            label, unique_colors.size()
        ])
        return false
    var destination := "%s/%s.png" % [directory, label]
    if captured.save_png(destination) != OK:
        _fail("PNG export failed for %s" % label)
        return false
    print("[EVERFIELD][RENDER-EVIDENCE] %s colors=%d" % [
        destination, unique_colors.size()
    ])
    return true


func _fail(message: String) -> void:
    push_error("[EVERFIELD][RENDER-EVIDENCE][FAIL] " + message)
    quit(1)
