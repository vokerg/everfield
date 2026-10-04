extends SceneTree
## Isolated pure-policy smoke, locked runtime target: Godot 4.7.1-stable.
## Run: godot --headless --path game --script res://components/traversal_policy/traversal_policy_smoke.gd

const Policy = preload("res://components/traversal_policy/traversal_policy.gd")
const SOURCE_SPEED := 230.0
const SOURCE_RADIUS := 88.0
const SOURCE_BOUNDS := Rect2(36.0, 90.0, 888.0, 414.0)

var failures: Array[String] = []


func _init() -> void:
    call_deferred("_run")


func _run() -> void:
    _test_keys_and_directions()
    _test_movement()
    _test_nearest_and_injected_schema()
    _finish()


func _test_keys_and_directions() -> void:
    var bindings: Dictionary = Policy.key_mapping()
    _expect(bindings == {
        "left": [KEY_A, KEY_LEFT],
        "right": [KEY_D, KEY_RIGHT],
        "up": [KEY_W, KEY_UP],
        "down": [KEY_S, KEY_DOWN],
    }, "WASD/arrow intent mapping exactly matches main.gd")
    bindings["left"].append(KEY_SPACE)
    bindings["up"] = []
    _expect(Policy.key_mapping()["left"] == [KEY_A, KEY_LEFT], "binding arrays returned without shared mutability")
    _expect(Policy.key_mapping()["up"] == [KEY_W, KEY_UP], "binding dictionaries returned without shared mutability")

    var rest: Dictionary = Policy.direction_from_intents({})
    _expect(rest.get("ok", false) and rest.get("direction") == Vector2.ZERO, "zero input stays still")
    var west: Dictionary = Policy.direction_from_intents({"left": true})
    var east: Dictionary = Policy.direction_from_intents({"right": true})
    var north: Dictionary = Policy.direction_from_intents({"up": true})
    var south: Dictionary = Policy.direction_from_intents({"down": true})
    _expect(west.get("direction") == Vector2.LEFT, "left intent")
    _expect(east.get("direction") == Vector2.RIGHT, "right intent")
    _expect(north.get("direction") == Vector2.UP, "up intent")
    _expect(south.get("direction") == Vector2.DOWN, "down intent")
    _expect(Policy.direction_from_intents({"left": true, "right": true}).get("direction") == Vector2.ZERO, "opposing horizontal intentions cancel")
    _expect(Policy.direction_from_intents({"up": true, "down": true}).get("direction") == Vector2.ZERO, "opposing vertical intentions cancel")
    _expect(Policy.direction_from_intents({"right": true, "up": true}).get("direction") == Vector2(1, -1), "diagonal direction matches controller before normalization")
    _reject(Policy.direction_from_intents({"fly": true}), "unknown input flag rejected")
    _reject(Policy.direction_from_intents({"left": 1}), "malformed input flag rejected")


func _test_movement() -> void:
    var start := Vector2(92, 286)
    var still: Dictionary = Policy.advance(start, Vector2.ZERO, 1.0, SOURCE_SPEED, SOURCE_BOUNDS)
    _expect(still.get("ok", false) and still.get("position") == start and not still.get("moved", true), "no input preserves position")
    var stationary: Dictionary = Policy.advance(start, Vector2.RIGHT, 0.0, SOURCE_SPEED, SOURCE_BOUNDS)
    _expect(stationary.get("position") == start, "zero delta preserves position")
    var right: Dictionary = Policy.advance(start, Vector2.RIGHT, 0.4, SOURCE_SPEED, SOURCE_BOUNDS)
    var right_pos: Vector2 = right.get("position", Vector2.ZERO)
    _expect(right.get("ok", false) and right_pos.is_equal_approx(Vector2(184, 286)), "positive cardinal speed 230 units/s")
    var left: Dictionary = Policy.advance(start, Vector2.LEFT, 0.1, SOURCE_SPEED, SOURCE_BOUNDS)
    var left_pos: Vector2 = left.get("position", Vector2.ZERO)
    _expect(left_pos.is_equal_approx(Vector2(69, 286)), "negative cardinal speed 230 units/s")
    var diag: Dictionary = Policy.advance(start, Vector2(1, -1), 0.4, SOURCE_SPEED, SOURCE_BOUNDS)
    var diag_pos: Vector2 = diag.get("position", Vector2.ZERO)
    _expect(diag.get("ok", false) and is_equal_approx(diag_pos.distance_to(start), 92.0), "diagonal normalized, no speed amplification")
    _expect(diag_pos.distance_to(Vector2(176, 188)) <= SOURCE_RADIUS, "published D+W movement reaches Archive Ledger radius")
    var bottom_right: Dictionary = Policy.advance(start, Vector2(1, 1), 10.0, SOURCE_SPEED, SOURCE_BOUNDS)
    _expect(bottom_right.get("position") == Vector2(924, 504), "positive x/y clamp matches movement smoke")
    var top_left: Dictionary = Policy.advance(start, Vector2(-1, -1), 10.0, SOURCE_SPEED, SOURCE_BOUNDS)
    _expect(top_left.get("position") == Vector2(36, 90), "negative x/y clamp matches movement smoke")
    _reject(Policy.advance(start, Vector2.RIGHT, -1.0, SOURCE_SPEED, SOURCE_BOUNDS), "negative delta rejected")
    _reject(Policy.advance(start, Vector2.RIGHT, INF, SOURCE_SPEED, SOURCE_BOUNDS), "infinite delta rejected")
    _reject(Policy.advance(start, Vector2.RIGHT, NAN, SOURCE_SPEED, SOURCE_BOUNDS), "NaN delta rejected")
    _reject(Policy.advance(start, Vector2.RIGHT, 0.1, 0.0, SOURCE_BOUNDS), "nonpositive speed rejected")
    _reject(Policy.advance(start, Vector2.RIGHT, 0.1, -1.0, SOURCE_BOUNDS), "negative speed rejected")
    _reject(Policy.advance(Vector2(INF, 0), Vector2.RIGHT, 0.1, SOURCE_SPEED, SOURCE_BOUNDS), "nonfinite origin rejected")
    _reject(Policy.advance(start, Vector2(NAN, 1), 0.1, SOURCE_SPEED, SOURCE_BOUNDS), "nonfinite direction rejected")
    _reject(Policy.advance(start, Vector2.RIGHT, 0.1, SOURCE_SPEED, Rect2(36, 90, -1, 414)), "invalid bounds rejected")


func _test_nearest_and_injected_schema() -> void:
    # Fixture copied from main.gd@9b406cc0 (not duplicated into production policy).
    var stations := {
        "public_record": {"position": Vector2(176, 188)},
        "material_trace": {"position": Vector2(338, 382)},
        "defer_conclusion": {"position": Vector2(498, 184)},
        "commons_hearing": {"position": Vector2(676, 252)},
        "project_table": {"position": Vector2(798, 400)},
    }
    var order := ["public_record", "material_trace", "defer_conclusion", "commons_hearing", "project_table"]
    var untouched := stations.duplicate(true)
    var actual: Dictionary = Policy.nearest_station(Vector2(176, 188), stations, order, SOURCE_RADIUS)
    _expect(actual.get("ok", false) and actual.get("station_id") == "public_record", "five published stations preserve IDs and lookup")
    var edge: Dictionary = Policy.nearest_station(Vector2(88, 188), stations, order, SOURCE_RADIUS)
    _expect(edge.get("in_range", false) and edge.get("station_id") == "public_record", "radius equality is in-range")
    var far: Dictionary = Policy.nearest_station(Vector2.ZERO, stations, order, SOURCE_RADIUS)
    _expect(far.get("ok", false) and far.get("station_id") == "" and not far.get("in_range", true), "out-of-range never invents interaction")
    _expect(Policy.station_position("material_trace", stations, order).get("position") == Vector2(338, 382), "explicit known station resolved")
    _reject(Policy.station_position("unknown_station", stations, order), "unknown station ID rejected visibly")
    _reject(Policy.nearest_station(Vector2.ZERO, stations, order, -0.1), "negative radius rejected")
    _reject(Policy.nearest_station(Vector2.ZERO, stations, order, NAN), "NaN radius rejected")
    _reject(Policy.nearest_station(Vector2(INF, 0), stations, order, SOURCE_RADIUS), "nonfinite query position rejected")

    var tie := {"first": {"position": Vector2(-1, 0)}, "second": {"position": Vector2(1, 0)}}
    var first: Dictionary = Policy.nearest_station(Vector2.ZERO, tie, ["first", "second"], 1.0)
    var second: Dictionary = Policy.nearest_station(Vector2.ZERO, tie, ["second", "first"], 1.0)
    _expect(first.get("station_id") == "first" and second.get("station_id") == "second", "distance ties keep supplied insertion order")
    _reject(Policy.nearest_station(Vector2.ZERO, stations, ["public_record"], SOURCE_RADIUS), "missing station order rejected")
    _reject(Policy.nearest_station(Vector2.ZERO, stations, ["public_record", "material_trace", "defer_conclusion", "commons_hearing", "rogue"], SOURCE_RADIUS), "unknown injected station rejected")
    _reject(Policy.nearest_station(Vector2.ZERO, stations, ["public_record", "public_record", "defer_conclusion", "commons_hearing", "project_table"], SOURCE_RADIUS), "duplicate station ID rejected")
    var malformed := stations.duplicate(true)
    malformed["material_trace"] = {"position": "338,382"}
    _reject(Policy.nearest_station(Vector2.ZERO, malformed, order, SOURCE_RADIUS), "malformed injected station rejected")
    _expect(stations == untouched, "policy never mutates station dictionary or nested values")
    _expect(order == ["public_record", "material_trace", "defer_conclusion", "commons_hearing", "project_table"], "policy never mutates station order")


func _reject(result: Dictionary, description: String) -> void:
    _expect(result.get("ok", true) == false and not String(result.get("error", "")).is_empty(), description)


func _expect(condition: bool, message: String) -> void:
    if condition:
        print("[EF-TRAVERSAL-POLICY][PASS] %s" % message)
        return
    failures.append(message)
    push_error("[EF-TRAVERSAL-POLICY][FAIL] %s" % message)


func _finish() -> void:
    if failures.is_empty():
        print("EVERFIELD_TRAVERSAL_POLICY_SMOKE_PASS")
        quit(0)
        return
    push_error("EVERFIELD_TRAVERSAL_POLICY_SMOKE_FAIL count=%d failures=%s" % [failures.size(), failures])
    quit(1)
