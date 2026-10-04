extends RefCounted

const World = preload("res://components/old_works_world/old_works_world_presentation.gd")
const Hearing = preload("res://components/commons_hearing/commons_hearing_presentation.gd")
const Consequences = preload("res://components/commitment_consequences/commitment_consequence_presentation.gd")
var world: Variant
var hearing: Variant
var consequences: Variant

func _init(w: Variant = null, h: Variant = null, c: Variant = null) -> void:
    world = w if w != null else World.new()
    hearing = h if h != null else Hearing.new()
    consequences = c if c != null else Consequences.new()

func _good(lines: Array) -> Dictionary:
    var visible: Array = []
    for line in lines:
        if not String(line).is_empty():
            visible.append(String(line))
    return {"ok": true, "text": "\n".join(visible), "lines": lines.duplicate(true), "error": ""}

func _bad(reason: String) -> Dictionary:
    return {"ok": false, "text": "[EF-PRESENTATION-INVALID] %s" % reason, "lines": [], "error": reason}
