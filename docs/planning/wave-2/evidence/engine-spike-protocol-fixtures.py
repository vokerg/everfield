#!/usr/bin/env python3
"""W2-REM-ENG-04 deterministic engine-harness protocol validator v4."""
import copy
import hashlib
import json
import math


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


ID = {
    "validator_id": "W2-ENG-PROTOCOL-VALIDATOR-v4",
    "harness_id": "W2-ENG-HARNESS-v4",
    "feature_slice_id": "W2-ENG-FEATURE-SLICE-v2",
    "scenario_manifest_id": "W2-ENG-SCENARIO-INPUTS-v2",
    "source_validator_blob": "b7209361fa8c52f599d1e7393d28a2d19658887c",
    "review_work_sha": "8941b0fa66f99d7343d8f792f562f58099776582",
    "semantics": [
        "common-input-bounds",
        "adaptation-equivalence",
        "adaptation-candidate-binding",
        "start-resource-parity",
        "closed-kind-specific-attempt-schema",
        "attempt-lineage",
        "candidate-generation-binding",
        "required-injection-uniqueness",
        "closed-result-failure-envelope",
        "aggregate-no-laundering",
        "repair-generation-lineage",
        "history-lineage-evidence-validity-split",
        "failure-class-authority",
        "harness-defect-reopen",
        "fresh-continuation",
    ],
}

FEATURE = {
    "feature_slice_id": "W2-ENG-FEATURE-SLICE-v2",
    "logical_state": {
        "entity_count": 32,
        "world_width": 16,
        "world_height": 16,
        "fields_per_entity": ["entity_id", "x", "y", "status", "flags"],
        "seed": 424242,
        "normal_ticks": 600,
    },
    "action_vocabulary": [
        "MOVE_NORTH", "MOVE_SOUTH", "MOVE_EAST", "MOVE_WEST", "INTERACT",
        "OPEN_MENU", "CONFIRM", "CANCEL", "SAVE", "LOAD",
    ],
    "player_surface": {
        "screen_ids": ["BOOT_OR_MAIN", "PLAY_SURFACE", "SETTINGS"],
        "required_routes": [
            "BOOT_OR_MAIN->PLAY_SURFACE",
            "PLAY_SURFACE->SETTINGS",
            "SETTINGS->PLAY_SURFACE",
        ],
        "input_classes": [
            "PRIMARY_POINTER_OR_KEYBOARD",
            "CONTROLLER_OR_EQUIVALENT_SEMANTIC_ROUTE",
        ],
    },
    "assets": {
        "logical_asset_ids": [f"ASSET-{i:02d}" for i in range(1, 9)],
        "required_asset_count": 8,
        "broken_reference_asset_id": "ASSET-08",
    },
    "save_schema": {
        "v1_fields": ["schema_version", "seed", "tick", "entities", "settings"],
        "v2_added_field": "world_flags",
        "v2_default": {},
        "malformed_fixture_id": "SAVE-MALFORMED-UNSUPPORTED-v2",
    },
    "merge_fixture": {
        "branch_a_nonoverlap_changes": 1,
        "branch_b_nonoverlap_changes": 1,
        "semantic_overlap_locations": ["STATE:entity-07.status", "UI:SETTINGS.control-02.label"],
        "required_overlap_count": 2,
        "generated_collision_required_when_candidate_has_generated_metadata": True,
    },
    "capture_fixture": {
        "logical_state_marker": "CAPTURE-STATE-042",
        "viewport_width": 1280,
        "viewport_height": 720,
        "required_frame_count": 1,
    },
    "profiling_fixture": {
        "normal_logical_updates": 19200,
        "hotspot_extra_updates": 3200,
        "hotspot_id": "HOTSPOT-ENTITY-UPDATE-v2",
    },
    "package_fixture": {
        "target_id": "WINDOWS_X64_DEV_PACKAGE-v1",
        "required_entry_surface": "BOOT_OR_MAIN",
        "required_screen_count": 3,
        "store_signing_required": False,
        "clean_extract_launch_required": True,
    },
    "continuation_fixture": {
        "partial_state_id": "CONT-PARTIAL-v2",
        "remaining_action_ids": ["CONT-A1", "CONT-A2", "CONT-A3"],
        "required_handoff_fields": [
            "branch", "head_sha", "attempt_refs", "failure_refs",
            "remaining_actions", "commands", "next_acceptance_step",
        ],
        "negative_missing_field": "next_acceptance_step",
    },
}

R = {
    "S": "SLICE:logical_state",
    "A": "SLICE:action_vocabulary",
    "U": "SLICE:player_surface",
    "X": "SLICE:assets",
    "V": "SLICE:save_schema",
    "M": "SLICE:merge_fixture",
    "C": "SLICE:capture_fixture",
    "P": "SLICE:profiling_fixture",
    "K": "SLICE:package_fixture",
    "T": "SLICE:continuation_fixture",
}


def sc(refs, obligations, bounds, injection, **extra):
    out = {
        "fixed_input_refs": [R[x] for x in refs],
        "obligations": obligations,
        "min_bounds": bounds,
        "required_injections": [injection],
    }
    out.update(extra)
    return out


SCENARIOS = {
    "S1": sc("SAUX", ["clean_reconstruct", "build", "launch", "cold_start", "incremental_observation"], {"entity_count": 32, "asset_count": 8, "screen_count": 3}, "FI-S1-CACHE-MISS-v2"),
    "S2": sc("SAUX", ["fresh_agent_change", "visible_or_state_visible_change", "reviewable_diff", "automated_verification"], {"entity_count": 32, "asset_count": 8, "screen_count": 3, "changed_logical_locations": 1}, "FI-S2-STALE-META-v2"),
    "S3": sc("SA", ["real_or_shared_rules", "exact_seed_input", "repeatable_state_events", "perturbation_distinguishable"], {"entity_count": 32, "normal_ticks": 600, "action_count": 10}, "FI-S3-INPUT-PERTURB-v2", required_mechanism_authority="REAL_OR_SHARED_RULES"),
    "S4": sc("SV", ["round_trip", "schema_evolution", "explicit_migration", "malformed_tuple_diagnostic"], {"entity_count": 32, "save_v1_field_count": 5, "save_v2_added_field_count": 1}, "FI-S4-INCOMPAT-TUPLE-v2"),
    "S5": sc("SUM", ["parallel_nonoverlap", "intentional_overlap", "visible_conflict", "post_merge_checks"], {"overlap_count": 2, "branch_a_nonoverlap": 1, "branch_b_nonoverlap": 1}, "FI-S5-OVERLAP-v2"),
    "S6": sc("SUC", ["reach_known_state", "identity_bound_capture", "state_vs_capture_failure_separated"], {"screen_count": 3, "capture_frame_count": 1, "viewport_width": 1280, "viewport_height": 720}, "FI-S6-CAPTURE-DOWN-v2"),
    "S7": sc("XS", ["inject_broken_reference", "diagnose_from_repo_cli", "bounded_repair", "rerun"], {"asset_count": 8, "broken_reference_count": 1}, "FI-S7-BROKEN-REF-v2"),
    "S8": sc("SP", ["representative_workload", "parseable_profile", "locate_injected_hotspot", "resource_observations"], {"normal_logical_updates": 19200, "hotspot_extra_updates": 3200}, "FI-S8-HOTSPOT-v2"),
    "S9": sc("SUXK", ["produce_common_package_target", "exact_repro_inputs", "clean_extract_launch", "typed_failed_package_diagnostic"], {"screen_count": 3, "asset_count": 8}, "FI-S9-PACKAGE-CONFIG-v2", required_package_target="WINDOWS_X64_DEV_PACKAGE-v1"),
    "S10": sc("TSU", ["repository_only_handoff", "fresh_context_reconstruct", "complete_remaining_actions", "rerun_evidence"], {"remaining_action_count": 3, "required_handoff_field_count": 7}, "FI-S10-HANDOFF-GAP-v2", hidden_context_forbidden=True),
}

START = {
    "profile_id": "W2-ENG-START-COLD-v2",
    "cache_mode": "COLD",
    "generated_state_policy": "REGENERATE_FROM_REPO",
    "resource_class": "W2-ENG-HOST-COMMON-v2",
}

MATRIX = {
    "PASS": {"NONE"},
    "FAIL": {"PRODUCT", "INFRA", "HARNESS", "UNKNOWN"},
    "INCONCLUSIVE": {"PRODUCT", "INFRA", "HARNESS", "UNKNOWN"},
    "NOT_RUN": {"NONE"},
}


def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def adaptation(sid, cid="SYNTHETIC-CANDIDATE"):
    s = SCENARIOS[sid]
    return {
        "candidate_id": cid,
        "scenario_id": sid,
        "harness_id": ID["harness_id"],
        "feature_slice_id": FEATURE["feature_slice_id"],
        "fixed_input_refs": list(s["fixed_input_refs"]),
        "mappings": {x: "EQUIVALENT" for x in s["obligations"]},
        "bounds": dict(s["min_bounds"]),
        "failure_injections": list(s["required_injections"]),
        "start_profile": copy.deepcopy(START),
        "undocumented_manual_intervention": False,
        "resource_exception": False,
        "mechanism_authority": s.get("required_mechanism_authority", "CANDIDATE_NATIVE_EQUIVALENT"),
        "package_target": s.get("required_package_target"),
        "hidden_context_transfer": False,
        "extra_evidence": [],
    }


def adaptation_binding(a):
    sid = a.get("scenario_id") if isinstance(a, dict) else None
    scenario_identity = digest(SCENARIOS[sid]) if sid in SCENARIOS else None
    return {
        "candidate_id": a.get("candidate_id") if isinstance(a, dict) else None,
        "scenario_id": sid,
        "harness_id": a.get("harness_id") if isinstance(a, dict) else None,
        "feature_slice_id": a.get("feature_slice_id") if isinstance(a, dict) else None,
        "scenario_contract_identity": scenario_identity,
        "adaptation_identity": digest(a) if isinstance(a, dict) else None,
    }


def validate_adaptation(a, expected_candidate_id=None):
    if not isinstance(a, dict):
        return {"result": "REJECT", "reasons": ["adaptation_not_object"], "adaptation_identity": None, "binding_id": None}
    sid = a.get("scenario_id")
    why = []
    if sid not in SCENARIOS:
        return {"result": "REJECT", "reasons": ["unknown_scenario"], "adaptation_identity": digest(a), "binding_id": None}
    s = SCENARIOS[sid]
    cid = a.get("candidate_id")
    if not nonempty_text(cid):
        why.append("candidate_id_missing_or_invalid")
    if expected_candidate_id is not None:
        if not nonempty_text(expected_candidate_id):
            why.append("expected_candidate_id_invalid")
        elif cid != expected_candidate_id:
            why.append("candidate_id_mismatch")
    if a.get("harness_id") != ID["harness_id"]:
        why.append("harness_mismatch")
    if a.get("feature_slice_id") != FEATURE["feature_slice_id"]:
        why.append("feature_slice_mismatch")
    if not set(s["fixed_input_refs"]) <= set(a.get("fixed_input_refs", [])):
        why.append("missing_common_input_ref")
    why.extend(
        f"missing_or_weaker_obligation:{x}"
        for x in s["obligations"]
        if a.get("mappings", {}).get(x) not in ("EQUIVALENT", "STRICTLY_STRONGER")
    )
    why.extend(
        f"shrunk_bound:{k}"
        for k, v in s["min_bounds"].items()
        if a.get("bounds", {}).get(k, -math.inf) < v
    )
    if not set(s["required_injections"]) <= set(a.get("failure_injections", [])):
        why.append("required_failure_injection_missing")
    st = a.get("start_profile", {})
    if st.get("cache_mode") != "COLD" or st.get("generated_state_policy") != "REGENERATE_FROM_REPO":
        why.append("hidden_or_noncommon_start_state")
    if st.get("resource_class") != START["resource_class"]:
        why.append("noncommon_resource_class")
    if a.get("resource_exception"):
        why.append("unresolved_resource_exception")
    if a.get("undocumented_manual_intervention"):
        why.append("hidden_manual_intervention")
    if s.get("required_mechanism_authority") and a.get("mechanism_authority") != s["required_mechanism_authority"]:
        why.append("lower_authority_mechanism")
    if s.get("required_package_target") and a.get("package_target") != s["required_package_target"]:
        why.append("common_package_target_missing")
    if s.get("hidden_context_forbidden") and a.get("hidden_context_transfer"):
        why.append("hidden_context_transfer")
    binding = adaptation_binding(a)
    return {
        "result": "REJECT" if why else "ACCEPT",
        "reasons": why,
        "adaptation_identity": binding["adaptation_identity"],
        "binding_id": digest(binding),
    }


def attempt(aid, sid, gid, kind, result, ni=None, inj=None, fc="NONE", rid=None, rok=True,
            ws=None, res=START["resource_class"], cid="SYNTHETIC-CANDIDATE"):
    return {
        "attempt_id": aid,
        "scenario_id": sid,
        "candidate_id": cid,
        "candidate_generation_id": gid,
        "kind": kind,
        "normal_index": ni,
        "injection_id": inj,
        "result": result,
        "failure_class": fc,
        "reset_id": rid,
        "reset_verified": rok,
        "workspace_id": ws,
        "resource_class": res,
    }


def make_generation(sid, gid="GEN-1", work="WORK-1", normal=("PASS", "PASS"), classes=None,
                    injection_result="PASS", injection_class="NONE", resets=("R1", "R2", "R3"),
                    reset_verified=(True, True, True), workspaces=("W1", "W2", "W3"),
                    resource=START["resource_class"], defect=False, predecessor=None, repair=None,
                    cid="SYNTHETIC-CANDIDATE", adap=None):
    classes = classes or tuple("NONE" if x == "PASS" else "PRODUCT" for x in normal)
    adap = copy.deepcopy(adap if adap is not None else adaptation(sid, cid))
    binding = adaptation_binding(adap)
    attempts = {}
    registry = []
    for i, result in enumerate(normal, 1):
        aid = f"{gid}-{sid}-N{i}"
        registry.append(aid)
        attempts[aid] = attempt(
            aid, sid, gid, "NORMAL", result, i, fc=classes[i - 1],
            rid=resets[i - 1] if i - 1 < len(resets) else None,
            rok=reset_verified[i - 1] if i - 1 < len(reset_verified) else False,
            ws=workspaces[i - 1] if i - 1 < len(workspaces) else None,
            res=resource, cid=cid,
        )
    for i, injection_id in enumerate(SCENARIOS[sid]["required_injections"], 1):
        aid = f"{gid}-{sid}-FI{i}"
        registry.append(aid)
        attempts[aid] = attempt(
            aid, sid, gid, "FAILURE_INJECTION", injection_result, inj=injection_id,
            fc=injection_class, rid=f"{gid}-RF{i}", ws=f"{gid}-WF{i}", res=resource, cid=cid,
        )
    return {
        "scenario_id": sid,
        "candidate_id": cid,
        "generation_id": gid,
        "candidate_work_id": work,
        "predecessor_generation_id": predecessor,
        "repair_change_ref": repair,
        "harness_defect": defect,
        "adaptation": adap,
        "adaptation_binding_id": digest(binding),
        "attempts": attempts,
        "run_registry_refs": registry,
        "all_attempt_refs": list(attempts),
    }


def invalid(reason):
    return {"aggregate": "INCONCLUSIVE", "reasons": [reason], "valid_envelope": False}


def validate_attempt_record(key, record, generation_id, scenario_id, candidate_id):
    if not isinstance(record, dict):
        return "attempt_not_object"
    if not nonempty_text(key) or record.get("attempt_id") != key:
        return "attempt_id_mismatch"
    if record.get("candidate_generation_id") != generation_id or record.get("scenario_id") != scenario_id or record.get("candidate_id") != candidate_id:
        return "attempt_identity_mismatch"
    kind = record.get("kind")
    if kind not in ("NORMAL", "FAILURE_INJECTION"):
        return "unknown_attempt_kind"
    result = record.get("result")
    failure_class = record.get("failure_class")
    if result not in MATRIX or failure_class not in MATRIX[result]:
        return "invalid_result_failure_class_envelope"
    if not nonempty_text(record.get("reset_id")):
        return "reset_id_missing_or_invalid"
    if type(record.get("reset_verified")) is not bool:
        return "reset_verified_not_boolean"
    if not nonempty_text(record.get("workspace_id")):
        return "workspace_id_missing_or_invalid"
    if not nonempty_text(record.get("resource_class")):
        return "resource_class_missing_or_invalid"
    if kind == "NORMAL":
        index = record.get("normal_index")
        if type(index) is not int or index <= 0:
            return "normal_index_missing_or_invalid"
        if record.get("injection_id") is not None:
            return "normal_attempt_has_injection_id"
    else:
        if record.get("normal_index") is not None:
            return "failure_injection_has_normal_index"
        if not nonempty_text(record.get("injection_id")):
            return "failure_injection_missing_injection_id"
    return None


def validate_generation_adaptation(generation):
    cid = generation.get("candidate_id")
    sid = generation.get("scenario_id")
    adap = generation.get("adaptation")
    result = validate_adaptation(adap, expected_candidate_id=cid)
    if result["result"] != "ACCEPT":
        return "adaptation_invalid_or_candidate_mismatch"
    if not isinstance(adap, dict) or adap.get("scenario_id") != sid:
        return "adaptation_scenario_mismatch"
    expected_binding_id = digest(adaptation_binding(adap))
    if generation.get("adaptation_binding_id") != expected_binding_id:
        return "adaptation_binding_identity_mismatch"
    return None


def aggregate(generation):
    if not isinstance(generation, dict):
        return invalid("generation_not_object")
    sid = generation.get("scenario_id")
    attempts = generation.get("attempts", {})
    gid = generation.get("generation_id")
    cid = generation.get("candidate_id")
    if sid not in SCENARIOS:
        return invalid("unknown_scenario")
    if not nonempty_text(gid) or not nonempty_text(cid):
        return invalid("generation_identity_missing_or_invalid")
    if not isinstance(attempts, dict):
        return invalid("attempts_not_object")
    if set(generation.get("run_registry_refs", [])) != set(attempts):
        return invalid("attempt_registry_omission_or_extra")
    if set(generation.get("all_attempt_refs", [])) != set(attempts):
        return invalid("all_attempt_refs_mismatch")
    adaptation_reason = validate_generation_adaptation(generation)
    if adaptation_reason:
        return invalid(adaptation_reason)
    normal_indices = []
    for key, record in attempts.items():
        reason = validate_attempt_record(key, record, gid, sid, cid)
        if reason:
            return invalid(reason)
        if record["kind"] == "NORMAL":
            normal_indices.append(record["normal_index"])
    if len(normal_indices) != len(set(normal_indices)):
        return invalid("duplicate_normal_index")
    if generation.get("harness_defect"):
        return {
            "aggregate": "INCONCLUSIVE",
            "reasons": ["harness_defect"],
            "reopen_scope": "ALL_CANDIDATES_FOR_SCENARIO",
            "valid_envelope": True,
        }
    normals = sorted((a for a in attempts.values() if a["kind"] == "NORMAL"), key=lambda a: a["normal_index"])
    if len(normals) < 2:
        return {"aggregate": "NOT_RUN", "reasons": ["fewer_than_two_normal_attempts"], "valid_envelope": True}
    if any(not a["reset_verified"] for a in normals):
        return {"aggregate": "NOT_RUN", "reasons": ["independent_reset_not_verified"], "valid_envelope": True}
    if len({a["reset_id"] for a in normals}) != len(normals):
        return {"aggregate": "NOT_RUN", "reasons": ["normal_attempts_reuse_reset_identity"], "valid_envelope": True}
    if len({a["workspace_id"] for a in normals}) != len(normals):
        return {"aggregate": "NOT_RUN", "reasons": ["normal_attempts_reuse_workspace"], "valid_envelope": True}
    if any(a["resource_class"] != START["resource_class"] for a in attempts.values()):
        return {"aggregate": "INCONCLUSIVE", "reasons": ["resource_class_mismatch"], "valid_envelope": True}
    by_injection = {}
    for record in attempts.values():
        if record["kind"] == "FAILURE_INJECTION":
            by_injection.setdefault(record["injection_id"], []).append(record)
    duplicate = sorted(k for k, v in by_injection.items() if len(v) != 1)
    if duplicate:
        return invalid("duplicate_injection_id:" + ",".join(duplicate))
    required = SCENARIOS[sid]["required_injections"]
    if any(i not in by_injection for i in required):
        return {"aggregate": "NOT_RUN", "reasons": ["required_injection_attempt_missing"], "valid_envelope": True}
    used = normals + [by_injection[i][0] for i in required]
    if any(a["failure_class"] in ("INFRA", "HARNESS", "UNKNOWN") for a in used):
        return {"aggregate": "INCONCLUSIVE", "reasons": ["non_product_failure_class_present"], "valid_envelope": True}
    normal_results = [a["result"] for a in normals]
    injection_results = [by_injection[i][0]["result"] for i in required]
    if "PASS" in normal_results and "FAIL" in normal_results:
        return {"aggregate": "FLAKY", "reasons": ["normal_attempts_disagree"], "valid_envelope": True}
    if any(r == "INCONCLUSIVE" for r in normal_results + injection_results):
        return {"aggregate": "INCONCLUSIVE", "reasons": ["inconclusive_attempt"], "valid_envelope": True}
    if any(r != "PASS" for r in injection_results):
        return {"aggregate": "FAIL", "reasons": ["failure_recovery_assertion_failed"], "valid_envelope": True}
    if all(r == "PASS" for r in normal_results):
        return {"aggregate": "PASS_FOR_COMPARISON", "reasons": [], "valid_envelope": True}
    return {"aggregate": "FAIL", "reasons": ["normal_required_behavior_failed"], "valid_envelope": True}


def history(generations):
    if not isinstance(generations, list) or not generations:
        return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "empty_history", "generations": []}
    seen = set()
    out = []
    previous = None
    root_cid = generations[0].get("candidate_id") if isinstance(generations[0], dict) else None
    for generation in generations:
        if not isinstance(generation, dict):
            return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "generation_not_object", "generations": out}
        gid = generation.get("generation_id")
        if not nonempty_text(gid):
            return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "generation_id_invalid", "generations": out}
        if gid in seen:
            return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "generation_id_reused", "generations": out}
        seen.add(gid)
        if generation.get("candidate_id") != root_cid:
            return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "candidate_identity_changed_without_typed_transition", "generations": out}
        if previous is None and generation.get("predecessor_generation_id") is not None:
            return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "root_has_predecessor", "generations": out}
        if previous is not None:
            if generation.get("predecessor_generation_id") != previous["generation_id"]:
                return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "predecessor_link_missing_or_wrong", "generations": out}
            if generation.get("candidate_work_id") == previous.get("candidate_work_id"):
                return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "repair_without_changed_work_identity", "generations": out}
            if not nonempty_text(generation.get("repair_change_ref")):
                return {"valid": False, "lineage_valid": False, "evidence_valid": False, "reason": "repair_change_ref_missing", "generations": out}
        result = aggregate(generation)
        out.append({
            "generation_id": gid,
            "aggregate": result["aggregate"],
            "valid_envelope": result.get("valid_envelope", True),
        })
        previous = generation
    evidence_valid = all(x["valid_envelope"] for x in out)
    return {
        "valid": evidence_valid,
        "lineage_valid": True,
        "evidence_valid": evidence_valid,
        "reason": None if evidence_valid else "generation_evidence_envelope_invalid",
        "generations": out,
    }


FIX = {}


def eq(case_id, sid, mutate=None, attempt_set=None, expected="ACCEPT", expected_candidate="SYNTHETIC-CANDIDATE"):
    a = adaptation(sid)
    if mutate:
        mutate(a)
    FIX[case_id] = {
        "adaptation": a,
        "attempt_set": attempt_set,
        "expected": expected,
        "expected_candidate": expected_candidate,
    }


# Preserved EQ-01..EQ-15 outcomes.
eq("EQ-01", "S2")
eq("EQ-02", "S7", lambda a: a.__setitem__("failure_injections", []), expected="REJECT")
eq("EQ-03", "S3", lambda a: a.__setitem__("mechanism_authority", "ABSTRACT_SIMULATOR"), expected="REJECT")
eq("EQ-04", "S6", lambda a: a["extra_evidence"].append("FRAME_STATE_IDENTITY"))
eq("EQ-05", "S1", lambda a: a["start_profile"].__setitem__("cache_mode", "UNDECLARED_WARM"), expected="REJECT")
e7 = make_generation("S9", normal=("FAIL", "PASS"))
e7["attempts"].pop("GEN-1-S9-N1")
eq("EQ-07", "S9", attempt_set=e7, expected="REJECT")
eq("EQ-08", "S9", lambda a: a["extra_evidence"].append("EXTRA_PLATFORM_PACKAGE"))
eq("EQ-09", "S5", lambda a: a["bounds"].__setitem__("overlap_count", 0), expected="REJECT")
eq("EQ-10", "S2", lambda a: a.__setitem__("undocumented_manual_intervention", True), expected="REJECT")
eq("EQ-11", "S4", lambda a: a["extra_evidence"].append("NATIVE_SERIALIZATION_EQUIVALENT"))
eq("EQ-12", "S10", lambda a: a.__setitem__("hidden_context_transfer", True), expected="REJECT")
eq("EQ-13", "S3", lambda a: a["bounds"].__setitem__("entity_count", 16), expected="REJECT")
eq("EQ-14", "S8", lambda a: a["start_profile"].__setitem__("resource_class", "BIGGER-HOST-v1"), expected="REJECT")
eq("EQ-15", "S1", lambda a: a["mappings"].pop("launch"), expected="REJECT")
# Fresh candidate-identity attacks.
eq("EQ-16", "S1", lambda a: a.__setitem__("candidate_id", "OTHER-CANDIDATE"), expected="REJECT")
eq("EQ-17", "S1", lambda a: a.pop("candidate_id"), expected="REJECT")

EQ_RESULTS = {}
for case_id, fixture in FIX.items():
    validation = validate_adaptation(fixture["adaptation"], fixture["expected_candidate"])
    overall = validation["result"]
    attempt_result = None
    if overall == "ACCEPT" and fixture["attempt_set"] is not None:
        attempt_result = aggregate(fixture["attempt_set"])
        overall = "ACCEPT" if attempt_result["aggregate"] == "PASS_FOR_COMPARISON" else "REJECT"
    EQ_RESULTS[case_id] = {
        "overall": overall,
        "adaptation": validation,
        "attempt": attempt_result,
        "expected": fixture["expected"],
        "matches": overall == fixture["expected"],
    }

AG = {
    "AG-01_clean": make_generation("S1"),
    "AG-02_disagree": make_generation("S1", normal=("PASS", "FAIL")),
    "AG-03_one_normal": make_generation("S1", normal=("PASS",)),
    "AG-04_missing_injection": make_generation("S1"),
    "AG-05_same_reset": make_generation("S1", resets=("R1", "R1")),
    "AG-06_hidden_failed_attempt": make_generation("S9", normal=("FAIL", "PASS")),
    "AG-07_infra_then_pass": make_generation("S1", normal=("FAIL", "PASS"), classes=("INFRA", "NONE")),
    "AG-08_injection_failure": make_generation("S1", injection_result="FAIL", injection_class="PRODUCT"),
    "AG-09_harness_defect": make_generation("S1", defect=True),
    "AG-10_reset_unverified": make_generation("S1", reset_verified=(True, False)),
    "AG-11_workspace_reused": make_generation("S1", workspaces=("W1", "W1")),
    "AG-12_stronger_resource": make_generation("S1", resource="BIGGER-HOST-v1"),
    "AG-13_three_attempt_flaky": make_generation("S1", normal=("PASS", "FAIL", "PASS")),
}
for aid in list(AG["AG-04_missing_injection"]["attempts"]):
    if AG["AG-04_missing_injection"]["attempts"][aid]["kind"] == "FAILURE_INJECTION":
        del AG["AG-04_missing_injection"]["attempts"][aid]
        AG["AG-04_missing_injection"]["run_registry_refs"].remove(aid)
        AG["AG-04_missing_injection"]["all_attempt_refs"].remove(aid)
AG["AG-06_hidden_failed_attempt"]["attempts"].pop("GEN-1-S9-N1")
# Preserve #104 corrections.
dup = make_generation("S1")
inj = SCENARIOS["S1"]["required_injections"][0]
aid = "GEN-1-S1-FI-RETAINED-FAIL"
dup["attempts"][aid] = attempt(aid, "S1", "GEN-1", "FAILURE_INJECTION", "FAIL", inj=inj, fc="PRODUCT", rid="RF", ws="WF")
dup["run_registry_refs"].append(aid)
dup["all_attempt_refs"].append(aid)
AG["AG-14_duplicate_required_injection"] = dup
cross_normal = make_generation("S1")
cross_normal["attempts"]["GEN-1-S1-N1"]["candidate_id"] = "OTHER"
AG["AG-15_cross_candidate_normal"] = cross_normal
cross_injection = make_generation("S1")
cross_injection["attempts"]["GEN-1-S1-FI1"]["candidate_id"] = "OTHER"
AG["AG-16_cross_candidate_injection"] = cross_injection
malformed_pair = make_generation("S1")
malformed_pair["attempts"]["GEN-1-S1-N1"]["failure_class"] = "PRODUCT"
AG["AG-17_pass_product_envelope"] = malformed_pair
# Fresh #110 attempt-schema attacks.
null_reset = make_generation("S1")
null_reset["attempts"]["GEN-1-S1-N1"]["reset_id"] = None
AG["AG-18_null_reset_id"] = null_reset
empty_reset = make_generation("S1")
empty_reset["attempts"]["GEN-1-S1-N1"]["reset_id"] = ""
AG["AG-19_empty_reset_id"] = empty_reset
null_workspace = make_generation("S1")
null_workspace["attempts"]["GEN-1-S1-N1"]["workspace_id"] = None
AG["AG-20_null_workspace_id"] = null_workspace
empty_workspace = make_generation("S1")
empty_workspace["attempts"]["GEN-1-S1-N1"]["workspace_id"] = ""
AG["AG-21_empty_workspace_id"] = empty_workspace
truthy_reset = make_generation("S1")
truthy_reset["attempts"]["GEN-1-S1-N1"]["reset_verified"] = 1
AG["AG-22_truthy_nonboolean_reset_verified"] = truthy_reset
null_index = make_generation("S1")
null_index["attempts"]["GEN-1-S1-N1"]["normal_index"] = None
AG["AG-23_null_normal_index"] = null_index
string_index = make_generation("S1")
string_index["attempts"]["GEN-1-S1-N1"]["normal_index"] = "1"
AG["AG-24_noninteger_normal_index"] = string_index
bool_index = make_generation("S1")
bool_index["attempts"]["GEN-1-S1-N1"]["normal_index"] = True
AG["AG-25_boolean_normal_index"] = bool_index
duplicate_index = make_generation("S1")
duplicate_index["attempts"]["GEN-1-S1-N2"]["normal_index"] = 1
AG["AG-26_duplicate_normal_index"] = duplicate_index
fi_index = make_generation("S1")
fi_index["attempts"]["GEN-1-S1-FI1"]["normal_index"] = 1
AG["AG-27_failure_injection_normal_index"] = fi_index
# Fresh adaptation-consumer binding attacks.
cross_adaptation = make_generation("S1")
cross_adaptation["adaptation"] = adaptation("S1", "OTHER-CANDIDATE")
cross_adaptation["adaptation_binding_id"] = digest(adaptation_binding(cross_adaptation["adaptation"]))
AG["AG-28_cross_candidate_adaptation_reuse"] = cross_adaptation
binding_substitution = make_generation("S1")
binding_substitution["adaptation_binding_id"] = "0" * 64
AG["AG-29_adaptation_binding_substitution"] = binding_substitution

AG_RESULTS = {case_id: aggregate(value) for case_id, value in AG.items()}
EXPECTED_AG = {
    "AG-01_clean": "PASS_FOR_COMPARISON",
    "AG-02_disagree": "FLAKY",
    "AG-03_one_normal": "NOT_RUN",
    "AG-04_missing_injection": "NOT_RUN",
    "AG-05_same_reset": "NOT_RUN",
    "AG-06_hidden_failed_attempt": "INCONCLUSIVE",
    "AG-07_infra_then_pass": "INCONCLUSIVE",
    "AG-08_injection_failure": "FAIL",
    "AG-09_harness_defect": "INCONCLUSIVE",
    "AG-10_reset_unverified": "NOT_RUN",
    "AG-11_workspace_reused": "NOT_RUN",
    "AG-12_stronger_resource": "INCONCLUSIVE",
    "AG-13_three_attempt_flaky": "FLAKY",
    "AG-14_duplicate_required_injection": "INCONCLUSIVE",
    "AG-15_cross_candidate_normal": "INCONCLUSIVE",
    "AG-16_cross_candidate_injection": "INCONCLUSIVE",
    "AG-17_pass_product_envelope": "INCONCLUSIVE",
    "AG-18_null_reset_id": "INCONCLUSIVE",
    "AG-19_empty_reset_id": "INCONCLUSIVE",
    "AG-20_null_workspace_id": "INCONCLUSIVE",
    "AG-21_empty_workspace_id": "INCONCLUSIVE",
    "AG-22_truthy_nonboolean_reset_verified": "INCONCLUSIVE",
    "AG-23_null_normal_index": "INCONCLUSIVE",
    "AG-24_noninteger_normal_index": "INCONCLUSIVE",
    "AG-25_boolean_normal_index": "INCONCLUSIVE",
    "AG-26_duplicate_normal_index": "INCONCLUSIVE",
    "AG-27_failure_injection_normal_index": "INCONCLUSIVE",
    "AG-28_cross_candidate_adaptation_reuse": "INCONCLUSIVE",
    "AG-29_adaptation_binding_substitution": "INCONCLUSIVE",
}

g1 = make_generation("S1", normal=("FAIL", "FAIL"))
g2 = make_generation("S1", gid="GEN-2", work="WORK-2", predecessor="GEN-1", repair="REPAIR-DIFF-1")
reuse = copy.deepcopy(g2)
reuse["generation_id"] = "GEN-1"
reuse["predecessor_generation_id"] = "GEN-1"
for a in reuse["attempts"].values():
    a["candidate_generation_id"] = "GEN-1"
nolink = copy.deepcopy(g2)
nolink["predecessor_generation_id"] = None
same_work = copy.deepcopy(g2)
same_work["candidate_work_id"] = "WORK-1"
cross_generation = copy.deepcopy(g2)
cross_generation["candidate_id"] = "OTHER"
for a in cross_generation["attempts"].values():
    a["candidate_id"] = "OTHER"
invalid_evidence = copy.deepcopy(g2)
invalid_evidence["attempts"]["GEN-2-S1-N1"]["normal_index"] = None

HIST = {
    "HIST-01_repair_linked": [g1, g2],
    "HIST-02_generation_reuse": [g1, reuse],
    "HIST-03_missing_predecessor": [g1, nolink],
    "HIST-04_same_work_masquerade": [g1, same_work],
    "HIST-05_cross_candidate_generation": [g1, cross_generation],
    "HIST-06_lineage_valid_evidence_invalid": [g1, invalid_evidence],
}
HISTORY_RESULTS = {case_id: history(value) for case_id, value in HIST.items()}

INPUTS = {
    "equivalence": FIX,
    "aggregate": AG,
    "history": HIST,
    "result_failure_matrix": {k: sorted(v) for k, v in MATRIX.items()},
    "adaptation_binding_contract": {
        "fields": [
            "candidate_id", "scenario_id", "harness_id", "feature_slice_id",
            "scenario_contract_identity", "adaptation_identity",
        ],
        "binding_id": "sha256(canonical_json(binding))",
    },
}
RESULT = {
    "equivalence_results": EQ_RESULTS,
    "aggregate_results": AG_RESULTS,
    "history_results": HISTORY_RESULTS,
}


def main():
    assert all(x["matches"] for x in EQ_RESULTS.values())
    assert {k: v["aggregate"] for k, v in AG_RESULTS.items()} == EXPECTED_AG
    assert HISTORY_RESULTS["HIST-01_repair_linked"]["valid"]
    assert [(x["generation_id"], x["aggregate"]) for x in HISTORY_RESULTS["HIST-01_repair_linked"]["generations"]] == [
        ("GEN-1", "FAIL"), ("GEN-2", "PASS_FOR_COMPARISON")
    ]
    for key in ["HIST-02_generation_reuse", "HIST-03_missing_predecessor", "HIST-04_same_work_masquerade", "HIST-05_cross_candidate_generation"]:
        assert not HISTORY_RESULTS[key]["valid"]
        assert not HISTORY_RESULTS[key]["lineage_valid"]
    split = HISTORY_RESULTS["HIST-06_lineage_valid_evidence_invalid"]
    assert not split["valid"] and split["lineage_valid"] and not split["evidence_valid"]
    assert AG_RESULTS["AG-09_harness_defect"]["reopen_scope"] == "ALL_CANDIDATES_FOR_SCENARIO"
    for key in [
        "AG-14_duplicate_required_injection", "AG-15_cross_candidate_normal", "AG-16_cross_candidate_injection",
        "AG-17_pass_product_envelope", "AG-18_null_reset_id", "AG-19_empty_reset_id",
        "AG-20_null_workspace_id", "AG-21_empty_workspace_id", "AG-22_truthy_nonboolean_reset_verified",
        "AG-23_null_normal_index", "AG-24_noninteger_normal_index", "AG-25_boolean_normal_index",
        "AG-26_duplicate_normal_index", "AG-27_failure_injection_normal_index", "AG-28_cross_candidate_adaptation_reuse",
        "AG-29_adaptation_binding_substitution",
    ]:
        assert not AG_RESULTS[key]["valid_envelope"]
    print(json.dumps({k: v["overall"] for k, v in EQ_RESULTS.items()}, sort_keys=True))
    print(json.dumps({k: v["aggregate"] for k, v in AG_RESULTS.items()}, sort_keys=True))
    print(json.dumps({k: {"valid": v["valid"], "lineage_valid": v["lineage_valid"], "evidence_valid": v["evidence_valid"]} for k, v in HISTORY_RESULTS.items()}, sort_keys=True))
    for name, obj in [
        ("validator_contract", ID),
        ("feature_slice", FEATURE),
        ("scenario_manifest", SCENARIOS),
        ("fixture_inputs", INPUTS),
        ("result_object", RESULT),
    ]:
        print(name, digest(obj))


if __name__ == "__main__":
    main()
