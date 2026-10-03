extends RefCounted

const MYSTERY_REF := "MYS:FRAGMENTATION-CAUSE"
const MYSTERY_STATE := "UNKNOWN_BY_DESIGN"

const TEXT := {
    "OW_CONSEQ_REPAIR_TITLE": "Repair Pilot — Bounded Start",
    "OW_CONSEQ_REPAIR_BODY": "The project table records a limited repair pilot as the next shared-use step. Work beyond the pilot remains uncommitted.",
    "OW_CONSEQ_REPAIR_HISTORY": "This commitment stays in the record even if the pilot is later paused, reframed, or replaced by a fresh public choice.",
    "OW_CONSEQ_REPAIR_TRUTH": "Starting repair does not decide why the Old Works fragmented, or which account was right.",
    "OW_CONSEQ_REPAIR_FOLLOWUP": "When observable pilot evidence exists, reassess the bounded pilot: continue it, pause it, or reframe it through a fresh explicit decision.",
    "OW_CONSEQ_RECORDS_TITLE": "Records First — Package Filed",
    "OW_CONSEQ_RECORDS_BODY": "The project table records documentation and limited use before broader repair. Broader physical repair remains deferred, not silently selected.",
    "OW_CONSEQ_RECORDS_HISTORY": "The records-first commitment remains part of the route history if a later reassessment opens a different bounded choice.",
    "OW_CONSEQ_RECORDS_TRUTH": "Filing the package preserves competing accounts; documentation does not convert either account into a finding.",
    "OW_CONSEQ_RECORDS_FOLLOWUP": "After a bounded record and present-condition reassessment, make a fresh choice about whether to open a repair pilot or continue records-first.",
    "OW_CONSEQ_DEFER_TITLE": "No Public Commitment",
    "OW_CONSEQ_DEFER_BODY": "Nothing is committed. Deferral records nonalignment for now; it is not approval waiting to happen.",
    "OW_CONSEQ_DEFER_REOPEN": "The hearing may be reopened only through a new explicit act. The prior deferral remains in the history.",
    "OW_CONSEQ_DEFER_TABLE": "The project table remains open because no supported public commitment was made.",
    "OW_CONSEQ_DEFER_TRUTH": "Deferring action does not settle the historical dispute.",
}

const EVENTS := {
    "COMMITMENT_REPAIR_PILOT": {"route":"repair_pilot","phase":"selection","ids":["OW_CONSEQ_REPAIR_TITLE","OW_CONSEQ_REPAIR_BODY","OW_CONSEQ_REPAIR_HISTORY","OW_CONSEQ_REPAIR_TRUTH"],"hook":"HOOK:OW:REPAIR-PILOT-REASSESS"},
    "BOUNDED_REPAIR_PILOT_STARTED": {"route":"repair_pilot","phase":"completion","ids":["OW_CONSEQ_REPAIR_TITLE","OW_CONSEQ_REPAIR_BODY","OW_CONSEQ_REPAIR_HISTORY","OW_CONSEQ_REPAIR_TRUTH"],"hook":"HOOK:OW:REPAIR-PILOT-REASSESS"},
    "COMMITMENT_RECORDS_FIRST": {"route":"records_first","phase":"selection","ids":["OW_CONSEQ_RECORDS_TITLE","OW_CONSEQ_RECORDS_BODY","OW_CONSEQ_RECORDS_HISTORY","OW_CONSEQ_RECORDS_TRUTH"],"hook":"HOOK:OW:RECORDS-FIRST-REASSESS"},
    "RECORDS_FIRST_PACKAGE_FILED": {"route":"records_first","phase":"completion","ids":["OW_CONSEQ_RECORDS_TITLE","OW_CONSEQ_RECORDS_BODY","OW_CONSEQ_RECORDS_HISTORY","OW_CONSEQ_RECORDS_TRUTH"],"hook":"HOOK:OW:RECORDS-FIRST-REASSESS"},
    "PUBLIC_COMMITMENT_DEFERRED": {"route":"defer","phase":"selection","ids":["OW_CONSEQ_DEFER_TITLE","OW_CONSEQ_DEFER_BODY","OW_CONSEQ_DEFER_REOPEN","OW_CONSEQ_DEFER_TABLE","OW_CONSEQ_DEFER_TRUTH"],"hook":""},
}

const HOOKS := {
    "HOOK:OW:REPAIR-PILOT-REASSESS": {"text_id":"OW_CONSEQ_REPAIR_FOLLOWUP","auto_trigger":false,"active_objective":false,"erases_history":false},
    "HOOK:OW:RECORDS-FIRST-REASSESS": {"text_id":"OW_CONSEQ_RECORDS_FOLLOWUP","auto_trigger":false,"active_objective":false,"erases_history":false},
}

func get_text(id: String) -> String:
    if not TEXT.has(id):
        push_error("[EF-CONSEQ-UNKNOWN-ID] %s" % id)
        return ""
    return String(TEXT[id])

func get_event(event_id: String) -> Dictionary:
    if not EVENTS.has(event_id):
        push_error("[EF-CONSEQ-UNKNOWN-EVENT] %s" % event_id)
        return {}
    return (EVENTS[event_id] as Dictionary).duplicate(true)

func get_hook(hook_id: String) -> Dictionary:
    if not HOOKS.has(hook_id):
        push_error("[EF-CONSEQ-UNKNOWN-HOOK] %s" % hook_id)
        return {}
    return (HOOKS[hook_id] as Dictionary).duplicate(true)

func get_contract() -> Dictionary:
    return {
        "mystery_ref": MYSTERY_REF,
        "mystery_state": MYSTERY_STATE,
        "claim_a_truth_effect": "NONE",
        "claim_b_truth_effect": "NONE",
        "deferral_is_consent_in_waiting": false,
        "direct_state_mutation": false,
        "direct_history_mutation": false,
        "presentation_grants_canonical_authority": false,
        "followup_hooks_auto_trigger": false,
        "followup_hooks_create_active_objective": false,
    }
