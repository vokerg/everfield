extends RefCounted

const MYSTERY_REF := "MYS:FRAGMENTATION-CAUSE"
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"
const PRIVATE_INFORMATION_REF := "INFO:anwen_contested_record_provenance_gap"

const PARTICIPANTS := {
    "OW_HEARING_PARTICIPANT_MAELIN_01": {
        "character_ref": "CHAR:maelin_sor",
        "display_name": "Maelin Sor",
        "hearing_role": "AFFECTED_BURDEN_VOICE",
        "purpose": "KEEP_MATERIAL_AND_CARE_BURDEN_VISIBLE_BEFORE_PUBLIC_COMMITMENT",
        "office_asserted": false,
        "faction_membership_asserted": false,
        "representation_asserted": false,
        "exclusive_standing_asserted": false,
        "private_information_required": false,
        "stance": [
            "BOUNDED_ACTION_REQUIRES_VISIBLE_BURDEN",
            "MAY_REMAIN_NONALIGNED_IF_BURDEN_IS_HIDDEN",
            "PROCEDURAL_VALIDITY_DOES_NOT_CLOSE_CONSEQUENCE_DISPUTE",
        ],
    },
    "OW_HEARING_PARTICIPANT_SELKA_01": {
        "character_ref": "CHAR:selka_vey",
        "display_name": "Selka Vey",
        "hearing_role": "BOUNDED_PROCEDURE_VOICE",
        "purpose": "KEEP_PUBLIC_COMMITMENT_EXPLICIT_SCOPED_AND_NONCOERCIVE",
        "office_asserted": false,
        "faction_membership_asserted": false,
        "representation_asserted": false,
        "exclusive_standing_asserted": false,
        "private_information_required": false,
        "stance": [
            "CHOICE_AND_LIMITS_MUST_BE_STATED_NOT_IMPLIED",
            "DEFERRAL_AND_NONALIGNMENT_ARE_LEGAL_OUTCOMES",
            "PROCEDURAL_COMPLETION_DOES_NOT_PROVE_BURDEN_RESOLVED",
        ],
    },
}

const DIALOGUE_BEATS := {
    "OW_HEARING_OPEN_MAELIN_01": {
        "speaker_ref": "CHAR:maelin_sor",
        "phase": "OPENING",
        "route_scope": "ANY",
        "text": "Before we choose a route, name who carries the work if the Old Works fail again.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_OPEN_SELKA_01": {
        "speaker_ref": "CHAR:selka_vey",
        "phase": "OPENING",
        "route_scope": "ANY",
        "text": "Then keep the choice bounded: record the scope, the burden, and how we can stop or revise it.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_REPAIR_SELKA_01": {
        "speaker_ref": "CHAR:selka_vey",
        "phase": "ROUTE_POSITION",
        "route_scope": "repair_pilot",
        "text": "A repair pilot is a trial, not a title to the Works. State the limit before anyone calls it settled.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_REPAIR_MAELIN_01": {
        "speaker_ref": "CHAR:maelin_sor",
        "phase": "ROUTE_POSITION",
        "route_scope": "repair_pilot",
        "text": "And state who is carrying the repair. If that burden is hidden, I do not support the pilot.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_RECORDS_MAELIN_01": {
        "speaker_ref": "CHAR:maelin_sor",
        "phase": "ROUTE_POSITION",
        "route_scope": "records_first",
        "text": "Records first keeps the burden visible instead of burying it under urgency.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_RECORDS_SELKA_01": {
        "speaker_ref": "CHAR:selka_vey",
        "phase": "ROUTE_POSITION",
        "route_scope": "records_first",
        "text": "Then record the limit: document, use narrowly, and reopen repair only by another public choice.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_DEFER_SELKA_01": {
        "speaker_ref": "CHAR:selka_vey",
        "phase": "DEFER_NONALIGNMENT",
        "route_scope": "defer",
        "text": "No assent is recorded. Reopen the hearing only when someone chooses to.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_DEFER_MAELIN_01": {
        "speaker_ref": "CHAR:maelin_sor",
        "phase": "DEFER_NONALIGNMENT",
        "route_scope": "defer",
        "text": "Then leave the burden on the table too. Deferral is not agreement with either account.",
        "required_for_progression": false,
        "authority_effect": "NONE",
    },
    "OW_HEARING_REFUSE_MAELIN_01": {
        "speaker_ref": "CHAR:maelin_sor",
        "phase": "REFUSAL",
        "route_scope": "ANY",
        "text": "I won’t endorse a route that hides who carries it. Put that burden in view or leave me unaligned.",
        "required_for_progression": false,
        "hidden_gate": false,
        "consent_effect": "NONE",
        "authority_effect": "NONE",
    },
    "OW_HEARING_REFUSE_SELKA_01": {
        "speaker_ref": "CHAR:selka_vey",
        "phase": "REFUSAL",
        "route_scope": "ANY",
        "text": "I won’t call this settled without a bounded scope and a way to revise it. Record nonalignment instead.",
        "required_for_progression": false,
        "hidden_gate": false,
        "consent_effect": "NONE",
        "authority_effect": "NONE",
    },
}

func get_participant(presentation_id: String) -> Dictionary:
    if not PARTICIPANTS.has(presentation_id):
        push_error("[EF-COMMONS-HEARING-UNKNOWN-PARTICIPANT] Unknown participant presentation ID: %s" % presentation_id)
        return {}
    return (PARTICIPANTS[presentation_id] as Dictionary).duplicate(true)

func get_line(beat_id: String) -> Dictionary:
    if not DIALOGUE_BEATS.has(beat_id):
        push_error("[EF-COMMONS-HEARING-UNKNOWN-LINE] Unknown dialogue beat ID: %s" % beat_id)
        return {}
    return (DIALOGUE_BEATS[beat_id] as Dictionary).duplicate(true)

func get_lines_for_route(route_scope: String) -> Array:
    if not ["repair_pilot", "records_first", "defer"].has(route_scope):
        push_error("[EF-COMMONS-HEARING-UNKNOWN-ROUTE] Unsupported hearing route: %s" % route_scope)
        return []

    var result: Array = []
    for beat_id in DIALOGUE_BEATS:
        var beat: Dictionary = DIALOGUE_BEATS[beat_id]
        if beat.get("route_scope", "") == "ANY" or beat.get("route_scope", "") == route_scope:
            var copy := beat.duplicate(true)
            copy["beat_id"] = beat_id
            result.append(copy)
    return result

func get_contract() -> Dictionary:
    return {
        "mystery_ref": MYSTERY_REF,
        "mystery_state": MYSTERY_STATE,
        "private_information_ref": PRIVATE_INFORMATION_REF,
        "participant_count": PARTICIPANTS.size(),
        "dialogue_beat_count": DIALOGUE_BEATS.size(),
        "exactly_two_reviewed_slice_actors_used": true,
        "refusal_available": true,
        "deferral_available": true,
        "nonalignment_legal": true,
        "deferral_is_consent_in_waiting": false,
        "direct_relationship_mutation": false,
        "universal_popularity_or_relationship_scalar": false,
        "private_information_required": false,
        "relationship_state_grants_information_access": false,
        "presentation_mutates_game_state": false,
        "presentation_grants_legitimacy": false,
        "presentation_grants_representation": false,
        "presentation_grants_canonical_authority": false,
    }
