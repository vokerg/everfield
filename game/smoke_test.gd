extends SceneTree

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var packed := load("res://main.tscn") as PackedScene
    _expect(packed != null, "main scene loads")
    if packed == null:
        _finish()
        return

    var game: Variant = packed.instantiate()
    get_root().add_child(game)
    await process_frame

    _expect(game.has_method("interact_with"), "interaction API exists")
    _expect(game.has_method("choose_commitment"), "commitment API exists")
    _expect(game.has_method("get_game_state"), "state diagnostics API exists")
    _expect(game.has_method("get_presentation_text"), "integrated presentation diagnostics API exists")
    _expect(game.get_node_or_null("Player") != null, "controllable player node exists")
    _expect(game.get_node_or_null("Presentation") != null, "reviewed presentation surface exists")
    _expect(game.get_node_or_null("PresentationNavigation") != null, "visible public paging controls wired")
    _expect(game.get_node_or_null("History") is RichTextLabel and game.get_node_or_null("HistoryHeader") != null,
        "read-only scrollable public history and page header wired")
    _expect(game.public_text_navigation is RefCounted and game.route_history_view is RefCounted,
        "both published independently reviewed component models wired")

    _expect(game.session_state != null, "published bounded session-state component wired")
    _expect(game.diagnostic_catalog != null, "published diagnostic catalog component wired")
    _expect(game.hud_objective_model != null, "published HUD objective/status component wired")
    _expect(game.has_method("_refresh_nearby_hint") and game.has_method("_unhandled_key_input"), "new source-frozen feedback and command dispatch seam is callable")
    # Only the nearest actionable station receives a reversible visual focus.
    # Its rendering is independent of bounded narrative/session state.
    _expect(game._focused_station_id == "", "no focused station at initial spawn")
    var focus_state_before: Dictionary = game.get_game_state()
    var public_node: Node2D = game.station_nodes.get("public_record") as Node2D
    _expect(public_node != null and public_node.get_child(0) is Polygon2D,
        "published record marker exists for visual focus")
    if public_node != null:
        var public_marker: Polygon2D = public_node.get_child(0) as Polygon2D
        _expect(public_marker.scale == Vector2.ONE, "record marker begins at reviewed base scale")
        game.player.position = Vector2(176, 188)
        game._refresh_nearby_hint()
        _expect(game._focused_station_id == "public_record", "focus names exactly nearest in-range station")
        _expect(public_marker.scale == Vector2(1.15, 1.15),
            "in-range marker is visibly enlarged without changing its base polygon or color")
        _expect(game.get_game_state() == focus_state_before,
            "visual focus repaint cannot mutate session state")
        game.player.position = Vector2(92, 286)
        game._refresh_nearby_hint()
        _expect(game._focused_station_id == "" and public_marker.scale == Vector2.ONE,
            "out-of-range marker returns to original scale and no station stays focused")
        _expect(game.get_game_state() == focus_state_before,
            "clearing visual focus cannot mutate session state")

    # Discoverable non-modal help UI exists and responds to H without mutating state
    _expect(game.get_node_or_null("HelpHint") != null and (game.get_node_or_null("HelpHint") as Label).text == "Press H for controls", "H help hint is present and legible at boot")
    _expect(game.get_node_or_null("HelpPanel") != null and not (game.get_node_or_null("HelpPanel") as ColorRect).visible, "Help panel exists and is hidden at boot")
    var state_before_help: Dictionary = game.get_game_state()
    var ev := InputEventKey.new()
    ev.pressed = true
    ev.echo = false
    ev.keycode = KEY_H
    game._unhandled_key_input(ev)
    await process_frame
    _expect((game.get_node("HelpPanel") as ColorRect).visible, "H toggles help panel visible without mutating game state")
    _expect(game.get_game_state() == state_before_help, "Toggling help cannot mutate session state")
    # Toggle off
    game._unhandled_key_input(ev)
    await process_frame
    _expect(not (game.get_node("HelpPanel") as ColorRect).visible, "H toggles help panel hidden again")
    _expect(game.get_game_state() == state_before_help, "Repeated help toggles do not mutate session state")
    var help_hint: Label = game.get_node("HelpHint") as Label
    _expect(help_hint.position.x >= 0 and help_hint.position.y >= 0
        and help_hint.position.x + help_hint.size.x <= 960
        and help_hint.position.y + help_hint.size.y <= 540,
        "H help hint is contained within 960x540 viewport")

    # Key release, echo, and physical-only H must not activate the overlay.
    ev.pressed = false
    game._unhandled_key_input(ev)
    _expect(not (game.get_node("HelpPanel") as ColorRect).visible, "released H does not toggle help")
    ev.pressed = true
    ev.echo = true
    game._unhandled_key_input(ev)
    _expect(not (game.get_node("HelpPanel") as ColorRect).visible, "echo H does not toggle help")
    ev.echo = false
    ev.keycode = 0
    ev.physical_keycode = KEY_H
    game._unhandled_key_input(ev)
    _expect(not (game.get_node("HelpPanel") as ColorRect).visible, "physical-only H does not toggle help")
    ev.keycode = KEY_H
    ev.physical_keycode = 0
    game._unhandled_key_input(ev)
    _expect((game.get_node("HelpPanel") as ColorRect).visible, "H may reopen the help panel")
    game.reset_slice()
    _expect(not (game.get_node("HelpPanel") as ColorRect).visible, "reset hides transient help overlay")
    _expect(game.get_game_state() == state_before_help, "reset after help leaves initial game state intact")

    # Map-view TAB hint and toggle tests: ensure default panels visible, TAB hides them,
    # TAB restores them, release/echo/physical-only events do nothing, reset restores.
    _expect(game.get_node_or_null("PresentationPanel") != null and (game.get_node_or_null("PresentationPanel") as ColorRect).visible, "Presentation panel visible at boot")
    _expect(game.get_node_or_null("HistoryPanel") != null and (game.get_node_or_null("HistoryPanel") as ColorRect).visible, "History panel visible at boot")
    _expect(game.get_node_or_null("MapViewHint") != null and (game.get_node_or_null("MapViewHint") as Label).text == "TAB: view all stations", "map view TAB hint present at boot")

    var snap_before_tab: Dictionary = game.get_game_state()
    var pres_scenario_before: String = game.presentation_scenario
    var pres_page_before: int = game.presentation_page
    var hist_page_before: int = game.history_page
    var pres_text_before: String = game.get_presentation_text()

    var ev_tab := InputEventKey.new()
    ev_tab.pressed = true
    ev_tab.echo = false
    ev_tab.keycode = KEY_TAB
    game._unhandled_key_input(ev_tab)
    await process_frame

    _expect(not (game.get_node("PresentationPanel") as ColorRect).visible
        and not (game.get_node("Presentation") as Label).visible
        and not (game.get_node("PresentationNavigation") as Label).visible
        and not (game.get_node("History") as RichTextLabel).visible
        and not (game.get_node("HistoryHeader") as Label).visible
        and not (game.get_node("HistoryPanel") as ColorRect).visible,
        "TAB hides presentation and history panels and labels")

    _expect(game.get_game_state() == snap_before_tab, "TAB does not mutate session state")
    _expect(game.presentation_scenario == pres_scenario_before and game.presentation_page == pres_page_before and game.history_page == hist_page_before and game.get_presentation_text() == pres_text_before,
        "TAB does not change presentation or history page or text")

    ev_tab.pressed = false
    game._unhandled_key_input(ev_tab)
    _expect(not (game.get_node("PresentationPanel") as ColorRect).visible, "released TAB does not toggle panels")
    ev_tab.pressed = true
    ev_tab.echo = true
    game._unhandled_key_input(ev_tab)
    _expect(not (game.get_node("PresentationPanel") as ColorRect).visible, "echo TAB does not toggle panels")
    ev_tab.echo = false
    ev_tab.keycode = 0
    ev_tab.physical_keycode = KEY_TAB
    game._unhandled_key_input(ev_tab)
    _expect(not (game.get_node("PresentationPanel") as ColorRect).visible, "physical-only TAB does not toggle panels")
    ev_tab.keycode = KEY_TAB
    ev_tab.physical_keycode = 0
    game._unhandled_key_input(ev_tab)
    await process_frame
    _expect((game.get_node("PresentationPanel") as ColorRect).visible, "TAB may reopen the panels")

    # Repeated real TAB keypresses alternate cleanly and restore all panels.
    game._unhandled_key_input(ev_tab)
    await process_frame
    _expect(not (game.get_node("PresentationPanel") as ColorRect).visible
        and not (game.get_node("HistoryPanel") as ColorRect).visible,
        "subsequent TAB hides the public panels again")
    game._unhandled_key_input(ev_tab)
    await process_frame
    _expect((game.get_node("PresentationPanel") as ColorRect).visible
        and (game.get_node("HistoryPanel") as ColorRect).visible
        and (game.get_node("Presentation") as Label).visible
        and (game.get_node("History") as RichTextLabel).visible,
        "TAB restores both full panels, labels and public text")
    _expect(game.get_game_state() == snap_before_tab
        and game.get_presentation_text() == pres_text_before,
        "repeated map toggles preserve session and exact public source text")

    # Reset restores default visibility
    game.reset_slice()
    _expect((game.get_node("PresentationPanel") as ColorRect).visible and (game.get_node("HistoryPanel") as ColorRect).visible, "reset restores presentation/history visibility")
    _expect(game.get_game_state() == snap_before_tab, "reset restores panels without mutating session state")

    _expect(game.station_world is RefCounted, "reviewed station-world metadata provider is wired")
    _expect(game.playable_presentation is RefCounted, "reviewed public narrative assembler is wired")
    var ids: Array[String] = game.station_world.get_station_ids()
    _expect(ids == ["public_record", "material_trace", "defer_conclusion", "commons_hearing", "project_table"], "exact station order is injected into live scene")
    var world_data: Dictionary = game.station_world.get_stations()
    var geometry: Dictionary = game.station_world.get_layout()
    _expect(world_data.size() == 5 and game.station_nodes.size() == 5, "live scene has five source-owned station markers")
    var floor_node := game.get_node_or_null("OldWorksFloor") as Polygon2D
    var walk_node := game.get_node_or_null("WalkPath") as Line2D
    _expect(floor_node != null and walk_node != null, "reviewed floor/path geometry is rendered")
    if floor_node != null and walk_node != null:
        _expect(floor_node.polygon == geometry["floor_polygon"] and floor_node.color == geometry["floor_color"], "scene floor exactly matches station-world snapshot")
        _expect(walk_node.points == geometry["walk_path"] and walk_node.width == geometry["walk_path_width"] and walk_node.default_color == geometry["walk_path_color"], "scene WalkPath exactly matches station-world snapshot")
    for station_id in ids:
        var station_node := game.station_nodes.get(station_id) as Node2D
        _expect(station_node != null, "%s exists as live marker" % station_id)
        if station_node == null:
            continue
        var station_data: Dictionary = world_data[station_id]
        _expect(station_node.position == station_data["position"], "%s uses exact reviewed coordinates" % station_id)
        var marker_node := station_node.get_child(0) as Polygon2D
        var label_node := station_node.get_child(1) as Label
        _expect(marker_node != null and label_node != null, "%s has source-owned marker/label" % station_id)
        if marker_node != null and label_node != null:
            _expect(marker_node.polygon == geometry["marker_polygon"] and marker_node.color == station_data["color"], "%s has exact reviewed polygon and RGB" % station_id)
            _expect(label_node.position == geometry["station_label_position"], "%s retains reviewed label anchor" % station_id)
            # The published main sets size to (148,44) before text layout, but Godot
            # may expand the runtime Control rect for long translated/hinted labels.
            var requested_size: Vector2 = geometry["station_label_size"]
            _expect(label_node.size.x >= requested_size.x and label_node.size.y >= requested_size.y, "%s retains reviewed label minimum dimensions" % station_id)
    var raw_station_copy: Dictionary = game.station_world.get_stations()
    var changed_record: Dictionary = raw_station_copy["public_record"]
    changed_record["position"] = Vector2(-999, -999)
    _expect(game.station_world.get_station("public_record")["position"] == Vector2(176, 188), "controller cannot mutate shared station metadata via snapshots")
    _expect(game.station_nodes["public_record"].position == Vector2(176, 188), "copy tampering cannot move the live marker")
    var public_contract: Dictionary = game.playable_presentation.get_contract()
    _expect(public_contract.get("mystery_state") == "UNKNOWN_BY_DESIGN" and not public_contract.get("private_information_visible", true) and not public_contract.get("deferral_is_consent", true), "new public assembler has no private, truth or implied-consent authority")
    var world_intro_view: Dictionary = game.playable_presentation.world_intro()
    _expect(world_intro_view.get("ok", false) and game.get_presentation_text() == world_intro_view["text"], "scene intro renders exactly reviewed assembler output")
    var intro_original: String = game.get_presentation_text()
    var intro_snapshot: Dictionary = game.get_game_state()
    var intro_pages: int = game.presentation_page_count
    _expect(intro_pages > 0 and intro_pages <= 128, "intro has bounded public page count")
    _expect(game.get_visible_presentation_text() == game.get_node("Presentation").text,
        "live presentation accessor names the actual first visible page")
    _expect(intro_original.begins_with(game.get_visible_presentation_text()),
        "visible first page is an exact approved source prefix")
    var intro_reconstructed: String = game.get_visible_presentation_text()
    for i in range(1, intro_pages):
        _expect(game.navigate_public_text(1), "next approved intro page reachable %d" % i)
        intro_reconstructed += game.get_visible_presentation_text()
    _expect(intro_reconstructed == intro_original, "intro paging reconstructs all reviewed source bytes")
    _expect(not game.navigate_public_text(1), "last public page does not wrap forward")
    for i in range(intro_pages - 1):
        _expect(game.navigate_public_text(-1), "earlier approved intro page reachable %d" % i)
    _expect(not game.navigate_public_text(-1) and game.presentation_page == 0,
        "first public page does not wrap backward")
    _expect(game.get_game_state() == intro_snapshot,
        "public page navigation cannot mutate or infer session state")
    _expect((game.get_node("PresentationNavigation") as Label).text.is_empty() == (intro_pages == 1),
        "page navigation hint only appears when more than one page exists")
    _expect((game.get_node("History") as RichTextLabel).scroll_active,
        "history scroll is available when approved titles exceed vertical viewport")
    _expect(game.get_visible_history_text().is_empty() and game.history_page == 0,
        "initial authentic session has no fabricated prior events")

    game.player.position = Vector2(88, 188)
    _expect(game._nearest_station_id() == "public_record", "live nearest station includes exact radius equality via traversal policy")
    game.player.position = Vector2(87, 188)
    _expect(game._nearest_station_id().is_empty(), "live nearest station rejects out-of-range position")
    game.player.position = geometry["player_spawn"]
    _expect(game.player.position == Vector2(92, 286), "reset spawn is exact source-world metadata")
    _expect(game.diagnostic_catalog.list_codes().size() == 16, "all sixteen reviewed diagnostics available")
    var initial_view: Dictionary = game.get_hud_view()
    _expect(initial_view.get("valid", false), "initial HUD model view is valid")
    _expect(initial_view.get("phase", "") == "INVESTIGATE_RECORD", "initial HUD phase derives from published model")
    _expect(String(initial_view.get("status", "")).contains("UNKNOWN_BY_DESIGN"), "HUD mystery permanently unresolved")

    var mutable_snapshot: Dictionary = game.get_game_state()
    mutable_snapshot["record_read"] = true
    (mutable_snapshot["history"] as Array).append("FORGED_HISTORY")
    _expect(game.get_game_state().get("record_read", true) == false, "gameplay snapshots cannot change bounded session state")
    _expect(not (game.get_game_state().get("history", []) as Array).has("FORGED_HISTORY"), "history snapshot is deeply isolated")
    var invalid_model_view: Dictionary = game.hud_objective_model.build_view({"record_read": true})
    _expect(invalid_model_view.get("phase", "") == "INVALID_STATE", "malformed HUD input fails closed")
    _expect(String(invalid_model_view.get("objective", "")).contains("Progress is not inferred"), "malformed HUD input cannot fabricate progress")
    _expect(not game.session_state.set_field("mystery_state", "SOLVED"), "invalid mystery write is rejected")
    _expect(not game.session_state.append_history("FORGED_HISTORY"), "unsupported session history fails closed")
    _expect(game.get_game_state().get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "failed state writes do not mutate mystery")
    var malformed_diagnostic: Dictionary = game.diagnostic_catalog.get_diagnostic("EF-INTERACT-UNKNOWN")
    _expect(not malformed_diagnostic.get("ok", true) and malformed_diagnostic.get("is_error", false), "missing diagnostic context fails closed")

    _expect(not game.interact_with("commons_hearing"), "negotiation fails closed before investigation")
    _expect((game.get_node("Diagnostic") as Label).text == game.diagnostic_catalog.format_line("EF-GATE-INVESTIGATION"), "gate diagnostic derives exact reviewed catalog text")
    _expect(not game.interact_nearest(), "out-of-range interaction fails closed")
    _expect((game.get_node("Diagnostic") as Label).text == game.diagnostic_catalog.format_line("EF-INTERACT-RANGE"), "range diagnostic derives exact reviewed catalog text")
    _expect(game.interact_with("public_record"), "public record route works")
    _expect(game.get_hud_view().get("phase", "") == "INVESTIGATE_CORROBORATE_OR_DEFER", "record-only HUD remains investigation-incomplete")
    _expect((game.get_node("Diagnostic") as Label).text == game.diagnostic_catalog.format_line("EF-INVESTIGATE-RECORD"), "record diagnostic consumes corrected current-main catalog text")
    var archive_text: String = game.get_presentation_text()
    _expect(game.presentation_scenario == "world_public_record"
        and game.get_visible_presentation_text() == game.public_text_navigation.page_view("world_public_record")["text"],
        "real Archive interaction selects exact published source-backed first page")
    _expect(game.get_visible_history_text().contains("Archive Ledger"),
        "history visibly consumes exact reviewed Archive event title")

    _expect(archive_text == game.playable_presentation.old_works_station("public_record")["text"], "Archive Ledger renders exactly composed public station text")
    _expect(archive_text.contains("One recorded account argues for a single dominant cause. Another rejects that reading. Both remain recorded as accounts, not findings."), "Archive Ledger visibly consumes reviewed Old Works presentation")
    _expect(not archive_text.contains("anwen_contested_record_provenance_gap"), "public record presentation does not expose private provenance gap")

    _expect(game.interact_with("material_trace"), "material trace route works")
    _expect(game.get_hud_view().get("phase", "") == "GO_TO_HEARING", "record and material-trace HUD opens hearing route")
    _expect((game.get_node("Diagnostic") as Label).text == game.diagnostic_catalog.format_line("EF-INVESTIGATE-TRACE"), "trace diagnostic consumes corrected current-main catalog text")
    var trace_text: String = game.get_presentation_text()
    _expect(trace_text == game.playable_presentation.old_works_station("material_trace")["text"], "Material Trace renders exactly composed independent public evidence")
    _expect(trace_text.contains("The trace supports a history of alteration and repeated maintenance. It does not identify a single cause for the fragmentation."), "Material Trace visibly consumes reviewed non-resolving evidence presentation")

    _expect(game.interact_with("commons_hearing"), "negotiation opens after evidence")
    _expect(game.get_hud_view().get("phase", "") == "HEARING_OPEN", "open hearing phase comes from reviewed HUD model")
    var hearing_text: String = game.get_presentation_text()
    _expect(hearing_text == game.playable_presentation.hearing_opening()["text"], "hearing renders exactly composer-validated opening beats")
    _expect(hearing_text.contains("Maelin Sor — Before we choose a route, name who carries the work if the Old Works fail again."), "Commons Hearing visibly presents reviewed Maelin opening beat")
    _expect(hearing_text.contains("Selka Vey — Then keep the choice bounded: record the scope, the burden, and how we can stop or revise it."), "Commons Hearing visibly presents reviewed Selka opening beat")

    _expect(game.choose_commitment("repair_pilot"), "repair-pilot commitment works")
    var repair_selection_text: String = game.get_presentation_text()
    _expect(repair_selection_text == game.playable_presentation.hearing_and_consequence("repair_pilot", "COMMITMENT_REPAIR_PILOT")["text"], "repair selection exactly composes hearing and consequence")
    _expect(repair_selection_text.contains("A repair pilot is a trial, not a title to the Works."), "repair route visibly presents reviewed Commons Hearing stance")
    _expect(repair_selection_text.contains("Repair Pilot — Bounded Start"), "repair route visibly presents reviewed consequence title")
    _expect(repair_selection_text.contains("Starting repair does not decide why the Old Works fragmented, or which account was right."), "repair consequence preserves unresolved mystery")

    _expect(game.interact_with("project_table"), "repair-pilot loop closes")
    _expect(game.get_hud_view().get("phase", "") == "COMPLETE", "repair pilot reaches HUD completion phase")

    var repair_state: Dictionary = game.get_game_state()
    _expect(repair_state.get("completed", false) == true, "repair route marks loop complete")
    _expect(repair_state.get("outcome", "") == "BOUNDED_REPAIR_PILOT_STARTED", "repair route has exact bounded outcome")
    _expect(repair_state.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "repair route does not settle world mystery")
    var repair_history: Array = repair_state.get("history", [])
    var repair_public_history: Dictionary = game.route_history_view.build_view(
        repair_state, game.old_works_presentation, game.consequence_presentation, game.history_page
    )
    _expect(repair_public_history.get("ok", false) and int(repair_public_history["count"]) == repair_history.size(),
        "visible repair history has exact authentic event count")
    _expect(game.get_visible_history_text() == repair_public_history["text"],
        "visible repair history is byte-identical to reviewed source projection")

    _expect(repair_history.size() >= 5, "repair route leaves observable state history")
    _expect(game.get_presentation_text().contains("Work beyond the pilot remains uncommitted."), "repair completion retains reviewed bounded consequence presentation")

    # Verify post-completion interactions do not mutate session, history, or presentation
    var completed_snapshot: Dictionary = game.get_game_state()
    var completed_presentation: String = game.get_presentation_text()
    var completed_history_len: int = (completed_snapshot.get("history", []) as Array).size()
    _expect(not game.interact_with("public_record"), "post-completion interact_with is rejected")
    _expect(not game.choose_commitment("defer"), "post-completion choose_commitment is rejected")
    _expect(not game.interact_nearest(), "post-completion interact_nearest is rejected")
    await process_frame
    _expect(game.get_game_state() == completed_snapshot, "post-completion attempts do not change deep-copy session state")
    _expect(game.get_presentation_text() == completed_presentation, "post-completion attempts do not change visible presentation")
    _expect((game.get_game_state().get("history", []) as Array).size() == completed_history_len, "post-completion attempts do not append history events")

    game.reset_slice()
    _expect(game.interact_with("public_record"), "record can be replayed after reset")
    _expect(game.interact_with("defer_conclusion"), "explicit truth defer is a legal investigation alternative")
    _expect(game.get_presentation_text().contains("You can act on the present condition without pretending the old dispute is settled."), "truth deferral visibly consumes reviewed Old Works presentation")
    _expect(game.interact_with("commons_hearing"), "defer-investigation route still reaches negotiation")
    _expect(game.get_game_state().get("trace_inspected", true) == false, "deferred investigation does not imply a trace")
    _expect(String(game.get_hud_view().get("status", "")).contains("Deferred truth:yes"), "HUD status names explicit truth deferral")

    _expect(game.choose_commitment("defer"), "public commitment can be explicitly deferred")
    _expect(game.get_hud_view().get("phase", "") == "GO_TO_HEARING", "commitment deferral remains noncomplete and reopenable")
    var defer_commitment_text: String = game.get_presentation_text()
    _expect(defer_commitment_text == game.playable_presentation.hearing_and_consequence("defer", "PUBLIC_COMMITMENT_DEFERRED")["text"], "public nonconsent route exactly matches reviewed composer")
    _expect(defer_commitment_text.contains("No assent is recorded. Reopen the hearing only when someone chooses to."), "hearing deferral visibly preserves reviewed nonalignment")
    _expect(defer_commitment_text.contains("Nothing is committed. Deferral records nonalignment for now; it is not approval waiting to happen."), "consequence deferral visibly preserves reviewed nonconsent")
    var deferred_state: Dictionary = game.get_game_state()
    _expect(deferred_state.get("commitment", "unexpected") == "", "deferred public commitment remains no commitment")
    _expect(deferred_state.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "commitment deferral does not settle world mystery")

    _expect(game.interact_with("commons_hearing"), "hearing can be explicitly reopened after deferral")
    _expect(game.choose_commitment("records_first"), "records-first commitment works after explicit deferral")
    var records_selection_text: String = game.get_presentation_text()
    _expect(records_selection_text == game.playable_presentation.hearing_and_consequence("records_first", "COMMITMENT_RECORDS_FIRST")["text"], "records-first route exactly composes reviewed scope")
    _expect(records_selection_text.contains("Records first keeps the burden visible instead of burying it under urgency."), "records-first route visibly presents reviewed Commons Hearing stance")
    _expect(records_selection_text.contains("Records First — Package Filed"), "records-first route visibly presents reviewed consequence title")
    _expect(game.interact_with("project_table"), "records-first loop closes")

    var records_state: Dictionary = game.get_game_state()
    _expect(records_state.get("completed", false) == true, "records-first route marks loop complete")
    _expect(records_state.get("outcome", "") == "RECORDS_FIRST_PACKAGE_FILED", "records-first route has exact bounded outcome")
    _expect(records_state.get("trace_inspected", true) == false, "records-first defer route does not fabricate material-trace evidence")
    _expect(records_state.get("deferred_truth", false) == true, "records-first defer route preserves explicit truth deferral")
    _expect(records_state.get("mystery_state", "") == "UNKNOWN_BY_DESIGN", "records-first route does not settle world mystery")
    var records_history: Array = records_state.get("history", [])
    _expect(game.presentation_scenario == "consequence_records_completion",
        "live records-first completion selects only reviewed consequence scenario")
    var records_history_view: Dictionary = game.route_history_view.build_view(
        records_state, game.old_works_presentation, game.consequence_presentation, game.history_page
    )
    _expect(records_history_view.get("ok", false)
        and game.get_visible_history_text() == records_history_view["text"],
        "defer-reopen-records history retains exactly published events and order")

    _expect(records_history.has("PUBLIC_COMMITMENT_DEFERRED"), "reopened records-first route preserves prior public deferral history")
    _expect(game.get_presentation_text().contains("documentation does not convert either account into a finding."), "records-first completion preserves reviewed truth boundary")

    game.reset_slice()
    _expect(not game.choose_commitment("repair_pilot"), "commitment fails closed before negotiation")
    _expect(not game.interact_with("unknown_station"), "unknown interaction surface fails visibly")
    var unchanged_before_bad_public_view: Dictionary = game.get_game_state()
    _expect(not game.playable_presentation.old_works_station("").get("ok", true), "empty public station cannot display world intro")
    _expect(not game.playable_presentation.hearing_and_consequence("defer", "COMMITMENT_REPAIR_PILOT").get("ok", true), "mismatched consent/consequence cannot be assembled")
    _expect(game.get_game_state() == unchanged_before_bad_public_view, "malformed public queries cannot mutate session state")
    _expect((game.get_node("Diagnostic") as Label).text == game.diagnostic_catalog.format_line("EF-INTERACT-UNKNOWN", {"station_id": "unknown_station"}), "unknown interaction derives error-classified contextual catalog diagnostic")
    _expect(not game.choose_commitment("unsupported"), "unsupported choice before negotiation cannot bypass hearing gate")
    _expect((game.get_node("Diagnostic") as Label).text == game.diagnostic_catalog.format_line("EF-GATE-NEGOTIATION"), "early unsupported choice remains negotiation-gated")

    # Assert real Label/HUD arbitration against the reviewed provider, rather
    # than accepting only the isolated RefCounted unit smoke assertions.
    var live_objective := game.get_node_or_null("Objective") as Label
    _expect(live_objective != null, "actual scene objective Label available for near/far arbitration")
    if live_objective != null:
        game.reset_slice()
        var record_display: Dictionary = game._station_display(
            "public_record", game.station_world.get_station("public_record")
        )
        var exact_hint: String = "[E] %s — %s" % [
            record_display["title"], record_display["hint"]
        ]
        game.player.position = Vector2(88, 188)
        game._refresh_nearby_hint()
        _expect(live_objective.text == exact_hint, "radius 88 boundary displays exactly approved source title and hint")
        game.player.position = Vector2(87, 188)
        game._refresh_nearby_hint()
        _expect(live_objective.text == String(game.get_hud_view()["objective"]),
            "outside radius 88 restores current reviewed phase objective without stale E")
        game.player.position = Vector2(176, 188)
        game._refresh_nearby_hint()
        _expect(live_objective.text == exact_hint, "returning inside radius restores identical approved E prompt")
        _expect(game.interact_with("public_record"), "nearby policy does not replace public interaction")
        _expect(game.interact_with("defer_conclusion"), "nearby policy preserves explicit truth deferral")
        _expect(game.interact_with("commons_hearing"), "nearby policy leaves hearing gate intact")
        _expect(game.choose_commitment("records_first"), "nearby policy leaves approved records-first consent gate intact")
        _expect(game.interact_with("project_table"), "nearby policy leaves bounded completion intact")
        game._refresh_nearby_hint()
        _expect(live_objective.text == String(game.get_hud_view()["objective"]) + " Press R to reset.",
            "COMPLETE wins over nearby E with exact pre-existing reset instruction")
        _expect(not live_objective.text.contains("[E]"), "completed visible label never implies another station action")
        _expect(game.get_game_state().get("mystery_state") == "UNKNOWN_BY_DESIGN",
            "new live HUD hint path cannot resolve private mystery")
        game.reset_slice()
        _expect(live_objective.text == String(game.get_hud_view()["objective"]),
            "scene reset restores reviewed phase with no E or stale R suffix")

    # Force 10 real session events to exercise history's exact 8-entry page
    # window and visibility, without mutating either independently published
    # model or writing synthetic events into a forged snapshot.
    game.reset_slice()
    _expect(game.interact_with("public_record"), "history page fixture reads real public record")
    _expect(game.interact_with("material_trace"), "history page fixture reads real material trace")
    for _i in range(4):
        _expect(game.interact_with("commons_hearing"), "history fixture opens a real hearing")
        _expect(game.choose_commitment("defer"), "history fixture explicitly defers nonconsenting hearing")
    var ten_history: Dictionary = game.get_game_state()
    _expect((ten_history.get("history", []) as Array).size() == 10,
        "genuine repeated hearing/deferral generates 10 legal ordered events")
    _expect(game.history_page == 1, "actual scene follows final history page after ninth event")
    _expect(game.get_visible_history_text() == game.route_history_view.build_view(
        ten_history, game.old_works_presentation, game.consequence_presentation, 1)["text"],
        "visible second history page is exact reviewed window")
    _expect(not game.navigate_public_history(1), "last history page never wraps forward")
    _expect(game.navigate_public_history(-1) and game.history_page == 0,
        "older approved public events remain directly reachable")
    _expect(game.get_visible_history_text() == game.route_history_view.build_view(
        ten_history, game.old_works_presentation, game.consequence_presentation, 0)["text"],
        "first history page preserves all eight exact ordered entries")
    _expect(not game.navigate_public_history(-1), "first history page never wraps backward")
    _expect(game.navigate_public_history(1) and game.history_page == 1,
        "newest approved history page is reachable again")
    _expect(game.get_game_state() == ten_history,
        "history paging never changes session history, commitment, consent or mystery")
    var header: Label = game.get_node("HistoryHeader") as Label
    _expect(header != null and header.text.contains("2/2")
        and header.text.contains("[C]") and header.text.contains("[V]"),
        "actual scene shows previous/next keys and page number only for multi-page history")
    game.reset_slice()
    _expect(game.history_page == 0 and game.get_visible_history_text().is_empty(),
        "R/reset clears all visible history without leaving stale page content")
    _expect(game.presentation_scenario == "world_intro" and game.presentation_page == 0,
        "reset returns to first approved world-intro page")
    _expect(game.get_game_state().get("mystery_state") == "UNKNOWN_BY_DESIGN",
        "new public pagination/historical recap never resolves mystery")


    _finish()

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_SMOKE_PASS")
        quit(0)
        return

    push_error("EVERFIELD_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
