class_name EverfieldStationWorld
extends RefCounted

# Exact, ordered, read-only source metadata from published game/main.gd.
# The live scene and movement policy remain owned by later, separate tasks.
const STATION_ORDER := [
    "public_record",
    "material_trace",
    "defer_conclusion",
    "commons_hearing",
    "project_table",
]

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

const WORLD_BOUNDS := Rect2(36.0, 90.0, 888.0, 414.0)

func get_station_ids() -> Array[String]:
    var ids: Array[String] = []
    for station_id in STATION_ORDER:
        ids.append(String(station_id))
    return ids

func has_station(station_id: String) -> bool:
    return STATIONS.has(station_id)

func get_station(station_id: String) -> Dictionary:
    if not STATIONS.has(station_id):
        printerr("[EF-STATION-WORLD-UNKNOWN] Unknown station: %s" % station_id)
        return {}
    # The source dictionary is never handed directly to a caller.
    return (STATIONS[station_id] as Dictionary).duplicate(true)

func lookup_station(station_id: Variant) -> Dictionary:
    # Non-string/invalid metadata from later fan-in cannot become a station.
    if typeof(station_id) != TYPE_STRING:
        printerr("[EF-STATION-WORLD-INVALID] Station ID must be a string.")
        return {}
    return get_station(String(station_id))

func get_stations() -> Dictionary:
    var result: Dictionary = {}
    for station_id in STATION_ORDER:
        result[String(station_id)] = get_station(String(station_id))
    return result

func get_layout() -> Dictionary:
    # Allocate new PackedVector2Array values on every call. Positions,
    # palette and geometry preserve the exact published main.gd literals.
    return {
        "world_bounds": WORLD_BOUNDS,
        "floor_polygon": PackedVector2Array([
            Vector2(22, 74), Vector2(938, 74),
            Vector2(938, 516), Vector2(22, 516),
        ]),
        "floor_color": Color("172129"),
        "walk_path": PackedVector2Array([
            Vector2(92, 286), Vector2(176, 188), Vector2(338, 382),
            Vector2(498, 184), Vector2(676, 252), Vector2(798, 400),
        ]),
        "walk_path_width": 9.0,
        "walk_path_color": Color("34444e"),
        "marker_polygon": PackedVector2Array([
            Vector2(-20, -20), Vector2(20, -20),
            Vector2(20, 20), Vector2(-20, 20),
        ]),
        "station_label_position": Vector2(-74, -52),
        "station_label_size": Vector2(148, 44),
        "player_spawn": Vector2(92, 286),
    }

func get_contract() -> Dictionary:
    return {
        "station_count": 5,
        "ordered_station_ids": get_station_ids(),
        "positions_and_fallbacks_match_published_main": true,
        "old_works_public_presentation_is_separate": true,
        "caller_receives_copies": true,
        "scene_or_node_ownership": false,
        "movement_or_input_ownership": false,
        "gameplay_state_mutation": false,
        "narrative_truth_or_canon_authority": false,
        "filesystem_or_network_or_persistence": false,
    }
