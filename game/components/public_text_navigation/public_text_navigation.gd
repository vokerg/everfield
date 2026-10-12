extends RefCounted

# Pure, read-only presentation slices from the already integrated public
# PlayablePresentation provider. Never takes arbitrary caller-supplied prose.
const PlayablePresentation = preload("res://components/playable_presentation/playable_presentation.gd")

const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"
const DEFAULT_PAGE_CHARACTERS := 144
const MIN_PAGE_CHARACTERS := 80
const MAX_PAGE_CHARACTERS := 240
const MAX_SOURCE_CHARACTERS := 16384
const MAX_PAGES := 128
const MAX_EXPLICIT_NEWLINES_PER_PAGE := 4

# These are the exact published composition surfaces exercised by the
# independent #1642 13-case 960x540/422x134 evidence. Unknown IDs are denied.
const SCENARIOS := [
    "world_intro",
    "world_public_record",
    "world_material_trace",
    "world_truth_deferral",
    "commons_hearing_opening",
    "hearing_repair",
    "hearing_records_first",
    "hearing_explicit_deferral",
    "combined_repair",
    "combined_records_first",
    "combined_explicit_deferral",
    "consequence_repair_completion",
    "consequence_records_completion",
]

func page_view(scenario: Variant, page_index: Variant = 0, page_characters: Variant = DEFAULT_PAGE_CHARACTERS) -> Dictionary:
    if typeof(scenario) != TYPE_STRING or typeof(page_index) != TYPE_INT or typeof(page_characters) != TYPE_INT:
        return _invalid()
    if not SCENARIOS.has(scenario):
        return _invalid()
    var budget: int = page_characters
    if budget < MIN_PAGE_CHARACTERS or budget > MAX_PAGE_CHARACTERS:
        return _invalid()

    var approved: Dictionary = _approved_pages(scenario, budget)
    if not approved.get("ok", false):
        return _invalid()
    var pages: Array = approved["pages"]
    var index: int = page_index
    if index < 0 or index >= pages.size():
        return _invalid()
    return {
        "ok": true,
        "scenario": scenario,
        "page_index": index,
        "page_count": pages.size(),
        "text": String(pages[index]),
        "has_previous": index > 0,
        "has_next": index + 1 < pages.size(),
        "source_length": approved["source_length"],
        "source_sha256": approved["source_sha256"],
        "mystery_state": MYSTERY_STATE,
        "error": "",
    }

func navigate(scenario: Variant, page_index: Variant, direction: Variant, page_characters: Variant = DEFAULT_PAGE_CHARACTERS) -> Dictionary:
    if typeof(page_index) != TYPE_INT or typeof(direction) != TYPE_INT:
        return _invalid()
    if direction != -1 and direction != 1:
        return _invalid()
    var current: Dictionary = page_view(scenario, page_index, page_characters)
    if not current.get("ok", false):
        return _invalid()
    # Do not wrap or infer implicit consent/progression at either boundary.
    return page_view(scenario, int(page_index) + int(direction), page_characters)

func _approved_pages(scenario: String, budget: int) -> Dictionary:
    var presenter: Variant = PlayablePresentation.new()
    var contract: Variant = presenter.get_contract()
    if typeof(contract) != TYPE_DICTIONARY:
        return {"ok": false}
    if contract.get("mystery_state") != MYSTERY_STATE or contract.get("private_information_visible", true) != false:
        return {"ok": false}
    if contract.get("deferral_is_consent", true) != false or contract.get("mutates_session", true) != false:
        return {"ok": false}
    var view: Dictionary = _approved_view(presenter, scenario)
    if view.get("ok", false) != true or typeof(view.get("text")) != TYPE_STRING:
        return {"ok": false}
    var text: String = view["text"]
    if text.is_empty() or text.strip_edges().is_empty() or text.length() > MAX_SOURCE_CHARACTERS:
        return {"ok": false}
    var pages: Array[String] = _split_exact(text, budget)
    if pages.is_empty() or pages.size() > MAX_PAGES:
        return {"ok": false}
    # No trimming, inserted separators, dropped whitespace or rewording.
    if "".join(PackedStringArray(pages)) != text:
        return {"ok": false}
    return {"ok": true, "pages": pages.duplicate(), "source_length": text.length(), "source_sha256": text.sha256_text()}

func _approved_view(presenter: Variant, scenario: String) -> Dictionary:
    match scenario:
        "world_intro":
            return presenter.world_intro()
        "world_public_record":
            return presenter.old_works_station("public_record")
        "world_material_trace":
            return presenter.old_works_station("material_trace")
        "world_truth_deferral":
            return presenter.old_works_station("defer_conclusion")
        "commons_hearing_opening":
            return presenter.hearing_opening()
        "hearing_repair":
            return presenter.hearing_route("repair_pilot")
        "hearing_records_first":
            return presenter.hearing_route("records_first")
        "hearing_explicit_deferral":
            return presenter.hearing_route("defer")
        "combined_repair":
            return presenter.hearing_and_consequence("repair_pilot", "COMMITMENT_REPAIR_PILOT")
        "combined_records_first":
            return presenter.hearing_and_consequence("records_first", "COMMITMENT_RECORDS_FIRST")
        "combined_explicit_deferral":
            return presenter.hearing_and_consequence("defer", "PUBLIC_COMMITMENT_DEFERRED")
        "consequence_repair_completion":
            return presenter.consequence("BOUNDED_REPAIR_PILOT_STARTED")
        "consequence_records_completion":
            return presenter.consequence("RECORDS_FIRST_PACKAGE_FILED")
    return {"ok": false}

func _split_exact(text: String, budget: int) -> Array[String]:
    var result: Array[String] = []
    var start := 0
    while start < text.length():
        if result.size() >= MAX_PAGES:
            return []
        var hard_end: int = mini(start + budget, text.length())
        var newlines := 0
        for i in range(start, hard_end):
            if text.substr(i, 1) == "\n":
                newlines += 1
                if newlines >= MAX_EXPLICIT_NEWLINES_PER_PAGE:
                    hard_end = i + 1
                    break
        var chosen_end := hard_end
        if hard_end < text.length() and hard_end - start >= MIN_PAGE_CHARACTERS:
            # Prefer an existing newline or whitespace boundary near the
            # budget edge but never remove the delimiter from the source.
            for i in range(hard_end, start + int(budget / 2), -1):
                var c: String = text.substr(i - 1, 1)
                if c == "\n" or c == " " or c == "\t":
                    chosen_end = i
                    break
        if chosen_end <= start:
            return []
        result.append(text.substr(start, chosen_end - start))
        start = chosen_end
    return result

func _invalid() -> Dictionary:
    return {
        "ok": false,
        "scenario": "",
        "page_index": -1,
        "page_count": 0,
        "text": "[EF-PUBLIC-TEXT-NAV-INVALID] Approved text unavailable.",
        "has_previous": false,
        "has_next": false,
        "source_length": 0,
        "source_sha256": "",
        "mystery_state": MYSTERY_STATE,
        "error": "invalid public text navigation request",
    }
