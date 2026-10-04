extends RefCounted
## Pure movement and nearest-station policy. Callers own their Input and station data.
## All returned values are new dictionaries. This component never changes input.

const INTENT_NAMES := ["left", "right", "up", "down"]


static func key_mapping() -> Dictionary:
    # Data only: the shared live controller remains responsible for Input reads.
    return {
        "left": [KEY_A, KEY_LEFT],
        "right": [KEY_D, KEY_RIGHT],
        "up": [KEY_W, KEY_UP],
        "down": [KEY_S, KEY_DOWN],
    }


static func direction_from_intents(intents: Dictionary) -> Dictionary:
    for intent in intents:
        if not (intent is String) or not INTENT_NAMES.has(intent):
            return _error("UNKNOWN_INTENT")
        if not (intents[intent] is bool):
            return _error("INVALID_INTENT_VALUE")
    var direction := Vector2.ZERO
    if bool(intents.get("left", false)):
        direction.x -= 1.0
    if bool(intents.get("right", false)):
        direction.x += 1.0
    if bool(intents.get("up", false)):
        direction.y -= 1.0
    if bool(intents.get("down", false)):
        direction.y += 1.0
    return {"ok": true, "direction": direction}


static func advance(position: Vector2, direction: Vector2, delta: float, speed: float, bounds: Rect2) -> Dictionary:
    if not position.is_finite():
        return _error("INVALID_POSITION")
    if not direction.is_finite():
        return _error("INVALID_DIRECTION")
    if not _finite(delta) or delta < 0.0:
        return _error("INVALID_DELTA")
    if not _finite(speed) or speed <= 0.0:
        return _error("INVALID_SPEED")
    if not bounds.position.is_finite() or not bounds.size.is_finite() or bounds.size.x <= 0.0 or bounds.size.y <= 0.0:
        return _error("INVALID_BOUNDS")
    # Match main.gd: without input, do not move or clamp. No diagonal speed-up.
    if direction == Vector2.ZERO or delta == 0.0:
        return {"ok": true, "position": position, "moved": false}
    var next_position: Vector2 = position + direction.normalized() * speed * delta
    if not next_position.is_finite():
        return _error("INVALID_MOVEMENT_RESULT")
    next_position.x = clampf(next_position.x, bounds.position.x, bounds.position.x + bounds.size.x)
    next_position.y = clampf(next_position.y, bounds.position.y, bounds.position.y + bounds.size.y)
    if not next_position.is_finite():
        return _error("INVALID_MOVEMENT_RESULT")
    return {"ok": true, "position": next_position, "moved": next_position != position}


static func station_position(station_id: String, stations: Dictionary, insertion_order: Array) -> Dictionary:
    var fault := _validate_stations(stations, insertion_order)
    if not fault.is_empty():
        return _error(fault)
    if not stations.has(station_id):
        return _error("UNKNOWN_STATION")
    return {"ok": true, "position": stations[station_id]["position"]}


static func nearest_station(position: Vector2, stations: Dictionary, insertion_order: Array, radius: float) -> Dictionary:
    if not position.is_finite():
        return _error("INVALID_POSITION")
    if not _finite(radius) or radius < 0.0:
        return _error("INVALID_RADIUS")
    var fault := _validate_stations(stations, insertion_order)
    if not fault.is_empty():
        return _error(fault)

    var best_id := ""
    var best_distance := INF
    # Explicit injection preserves original STATIONS insertion order, including ties.
    for station_id in insertion_order:
        var station_data: Dictionary = stations[station_id]
        var distance: float = position.distance_to(station_data["position"])
        if not _finite(distance):
            return _error("INVALID_DISTANCE")
        if distance < best_distance:
            best_distance = distance
            best_id = station_id
    if best_distance > radius:
        return {"ok": true, "station_id": "", "in_range": false}
    return {"ok": true, "station_id": best_id, "in_range": true, "distance": best_distance}


static func _validate_stations(stations: Dictionary, insertion_order: Array) -> String:
    # No embedded coordinates or station allowlist: caller injects authoritative data
    # and an independently obtained stable station order from station-world.
    if insertion_order.is_empty() or stations.size() != insertion_order.size():
        return "INVALID_STATION_SET"
    var visited := {}
    for station_id in insertion_order:
        if not (station_id is String) or String(station_id).is_empty():
            return "INVALID_STATION_ID"
        if visited.has(station_id) or not stations.has(station_id):
            return "UNKNOWN_OR_DUPLICATE_STATION"
        visited[station_id] = true
        var data: Variant = stations[station_id]
        if not (data is Dictionary) or not data.has("position"):
            return "INVALID_STATION_METADATA"
        var station_position_value: Variant = data["position"]
        if not (station_position_value is Vector2):
            return "INVALID_STATION_POSITION"
        if not station_position_value.is_finite():
            return "INVALID_STATION_POSITION"
    return ""


static func _finite(value: float) -> bool:
    return not is_nan(value) and not is_inf(value)


static func _error(code: String) -> Dictionary:
    return {"ok": false, "error": code}
