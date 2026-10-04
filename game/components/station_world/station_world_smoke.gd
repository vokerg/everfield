extends SceneTree

var failures: Array[String] = []

func _init() -> void:
    call_deferred("_run")

func _run() -> void:
    var script := load("res://components/station_world/station_world.gd")
    _expect(script != null, "station-world metadata provider script loads")
    if script == null:
        _finish()
        return

    var world: Variant = script.new()
    _expect(world is RefCounted, "provider has no scene or node ownership")

    # Independent literal fixture transcribed from published game/main.gd.
    var expected_ids := [
        "public_record", "material_trace", "defer_conclusion",
        "commons_hearing", "project_table",
    ]
    var fixture := {
        "public_record": [Vector2(176, 188), "Archive Ledger", "Public record — required", Color("6ca6c8")],
        "material_trace": [Vector2(338, 382), "Material Trace", "Independent evidence — optional", Color("c3a56f")],
        "defer_conclusion": [Vector2(498, 184), "Defer Conclusion", "Legal investigation alternative", Color("8d88ba")],
        "commons_hearing": [Vector2(676, 252), "Commons Hearing", "Negotiate shared use", Color("7dbb8b")],
        "project_table": [Vector2(798, 400), "Project Table", "Commit the bounded next step", Color("d28d7b")],
    }
    var ids: Array[String] = world.get_station_ids()
    _expect(ids == expected_ids, "exact station ID order and cardinality")
    _expect(ids.size() == 5, "exactly five world stations")
    var stations: Dictionary = world.get_stations()
    _expect(stations.size() == 5, "world snapshot contains exactly five stations")

    for station_id in expected_ids:
        var station: Dictionary = world.get_station(station_id)
        var expected: Array = fixture[station_id]
        _expect(world.has_station(station_id), "%s is registered" % station_id)
        _expect(station.size() == 4, "%s contains only bounded metadata" % station_id)
        _expect(station.get("position") == expected[0], "%s exact position" % station_id)
        _expect(station.get("title") == expected[1], "%s exact fallback title" % station_id)
        _expect(station.get("hint") == expected[2], "%s exact fallback hint" % station_id)
        _expect(station.get("color") == expected[3], "%s exact marker RGB" % station_id)
        _expect(stations.get(station_id) == station, "%s copied snapshot matches individual lookup" % station_id)

    var layout: Dictionary = world.get_layout()
    _expect(layout.get("world_bounds") == Rect2(36.0, 90.0, 888.0, 414.0), "exact world movement bounds")
    _expect(layout.get("floor_polygon") == PackedVector2Array([
        Vector2(22, 74), Vector2(938, 74), Vector2(938, 516), Vector2(22, 516),
    ]), "exact four-point floor polygon")
    _expect(layout.get("floor_color") == Color("172129"), "exact floor palette")
    _expect(layout.get("walk_path") == PackedVector2Array([
        Vector2(92, 286), Vector2(176, 188), Vector2(338, 382),
        Vector2(498, 184), Vector2(676, 252), Vector2(798, 400),
    ]), "exact six-point WalkPath")
    _expect(layout.get("walk_path_width") == 9.0, "exact WalkPath width")
    _expect(layout.get("walk_path_color") == Color("34444e"), "exact WalkPath color")
    _expect(layout.get("marker_polygon") == PackedVector2Array([
        Vector2(-20, -20), Vector2(20, -20), Vector2(20, 20), Vector2(-20, 20),
    ]), "exact station marker geometry")
    _expect(layout.get("station_label_position") == Vector2(-74, -52), "exact station label offset")
    _expect(layout.get("station_label_size") == Vector2(148, 44), "exact station label size")
    _expect(layout.get("player_spawn") == Vector2(92, 286), "original player spawn metadata")

    ids[0] = "corrupted"
    ids.append("invented")
    _expect(world.get_station_ids() == expected_ids, "mutated returned ID list never changes source IDs")
    var first: Dictionary = world.get_station("public_record")
    first["position"] = Vector2.ZERO
    first["title"] = "FAKE"
    first["hint"] = "FAKE"
    first["color"] = Color.BLACK
    _expect(world.get_station("public_record")["position"] == Vector2(176, 188), "station position mutation isolated")
    _expect(world.get_station("public_record")["title"] == "Archive Ledger", "station title mutation isolated")
    _expect(world.get_station("public_record")["hint"] == "Public record — required", "station hint mutation isolated")
    _expect(world.get_station("public_record")["color"] == Color("6ca6c8"), "station color mutation isolated")
    var nested: Dictionary = stations["material_trace"]
    nested["position"] = Vector2(-999, -999)
    stations.erase("project_table")
    _expect(world.get_station("material_trace")["position"] == Vector2(338, 382), "nested snapshot mutation isolated")
    _expect(world.get_stations().has("project_table"), "snapshot removal cannot remove original station")

    var changed_layout: Dictionary = world.get_layout()
    var floor_copy: PackedVector2Array = changed_layout["floor_polygon"]
    floor_copy[0] = Vector2(-111, -222)
    changed_layout["floor_polygon"] = floor_copy
    var path_copy: PackedVector2Array = changed_layout["walk_path"]
    path_copy[1] = Vector2(-11, -22)
    changed_layout["walk_path"] = path_copy
    changed_layout["world_bounds"] = Rect2(-1, -1, 0, 0)
    _expect(world.get_layout() == layout, "nested floor/path/bounds mutation cannot change original layout")

    _expect(not world.has_station("unknown"), "unknown station is not registered")
    _expect(world.get_station("unknown").is_empty(), "unknown station fails closed visibly")
    _expect(world.get_station("").is_empty(), "empty station fails closed visibly")
    _expect(world.lookup_station(17).is_empty(), "non-string station ID fails closed visibly")
    _expect(world.lookup_station(null).is_empty(), "null station ID fails closed visibly")
    _expect(world.lookup_station("PUBLIC_RECORD").is_empty(), "wrong-case station ID fails closed visibly")
    _expect(world.get_station_ids() == expected_ids, "invalid calls cannot contaminate station IDs")
    _expect(world.get_layout() == layout, "invalid calls cannot contaminate world layout")
    var contract: Dictionary = world.get_contract()
    _expect(contract.get("station_count") == 5, "contract is bounded to exactly five stations")
    _expect(contract.get("scene_or_node_ownership") == false, "no scene/node mutation authority")
    _expect(contract.get("movement_or_input_ownership") == false, "no input or movement authority")
    _expect(contract.get("gameplay_state_mutation") == false, "no mutable gameplay state")
    _expect(contract.get("narrative_truth_or_canon_authority") == false, "no truth or canon authority")
    _expect(contract.get("filesystem_or_network_or_persistence") == false, "no IO or persistence")
    var claimed_ids: Array = contract.get("ordered_station_ids", [])
    claimed_ids.clear()
    _expect(world.get_contract()["ordered_station_ids"] == expected_ids, "contract IDs are copied")
    _finish()

func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-STATION-WORLD-SMOKE][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-STATION-WORLD-SMOKE][FAIL] %s" % message)

func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_STATION_WORLD_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_STATION_WORLD_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
