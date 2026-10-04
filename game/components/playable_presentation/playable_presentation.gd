extends RefCounted

# Read-only public narrative assembly. Never owns nodes, input, state, or truth.
const World = preload("res://components/old_works_world/old_works_world_presentation.gd")
const Hearing = preload("res://components/commons_hearing/commons_hearing_presentation.gd")
const Consequences = preload("res://components/commitment_consequences/commitment_consequence_presentation.gd")
const WorldReader = preload("res://components/playable_presentation/world_reader.gd")
const HearingReader = preload("res://components/playable_presentation/hearing_reader.gd")
const ConsequenceReader = preload("res://components/playable_presentation/consequence_reader.gd")

const CHOICES := {
    "repair_pilot": "COMMITMENT_REPAIR_PILOT",
    "records_first": "COMMITMENT_RECORDS_FIRST",
    "defer": "PUBLIC_COMMITMENT_DEFERRED",
}
var world: Variant
var hearing: Variant
var consequences: Variant

func _init(w: Variant = null, h: Variant = null, c: Variant = null) -> void:
    world = w if w != null else World.new()
    hearing = h if h != null else Hearing.new()
    consequences = c if c != null else Consequences.new()

func world_intro() -> Dictionary:
    return WorldReader.new().compose(world)

func old_works_station(station_id: String) -> Dictionary:
    if station_id.is_empty():
        return _bad("invalid public station")
    return WorldReader.new().compose(world, station_id)

func hearing_opening() -> Dictionary:
    return HearingReader.new().compose(hearing)

func hearing_route(route: String) -> Dictionary:
    if not CHOICES.has(route):
        return _bad("unknown hearing route")
    return HearingReader.new().compose(hearing, route)

func consequence(event_id: String) -> Dictionary:
    return ConsequenceReader.new().compose(consequences, event_id)

func hearing_and_consequence(route: String, event_id: String) -> Dictionary:
    # An outcome may not be paired with a different public choice.
    if not CHOICES.has(route) or CHOICES[route] != event_id:
        return _bad("route and selected consequence disagree")
    var first: Dictionary = hearing_route(route)
    if not first.get("ok", false):
        return first
    var second: Dictionary = consequence(event_id)
    if not second.get("ok", false):
        return second
    var lines: Array = first["lines"].duplicate(true)
    lines.append("")
    lines.append_array(second["lines"])
    return {"ok": true, "text": "%s\n\n%s" % [first["text"], second["text"]], "lines": lines.duplicate(true), "error": ""}

func get_contract() -> Dictionary:
    return {"mystery_ref": "MYS:FRAGMENTATION-CAUSE", "mystery_state": "UNKNOWN_BY_DESIGN", "private_information_visible": false, "deferral_is_consent": false, "mutates_session": false, "owns_scene": false, "canonical_authority": false}

func _bad(reason: String) -> Dictionary:
    return {"ok": false, "text": "[EF-PRESENTATION-INVALID] %s" % reason, "lines": [], "error": reason}
