#!/usr/bin/env python3
"""W2-REM-ENG-02 planning-only protocol fixtures.

This validator is an engine-neutral planning experiment. It does not contain game logic,
select an engine, or authorize implementation. It exists only to make W2-ENG-HARNESS-v2
common-input, adaptation-equivalence, reset/resource, and attempt-lineage rules executable.
"""

import copy
import hashlib
import json
import math


def canonical_digest(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


VALIDATOR_IDENTITY = {
    "validator_id": "W2-ENG-PROTOCOL-VALIDATOR-v2",
    "harness_id": "W2-ENG-HARNESS-v2",
    "feature_slice_id": "W2-ENG-FEATURE-SLICE-v2",
    "scenario_manifest_id": "W2-ENG-SCENARIO-INPUTS-v2",
    "semantics": [
        "common-input-bounds",
        "adaptation-equivalence",
        "start-resource-parity",
        "attempt-lineage",
        "aggregate-no-laundering",
        "fresh-continuation",
    ],
}

FEATURE_SLICE = {
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
        "semantic_overlap_locations": [
            "STATE:entity-07.status",
            "UI:SETTINGS.control-02.label",
        ],
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

COMMON_REFS = {
    "STATE": "SLICE:logical_state",
    "ACTIONS": "SLICE:action_vocabulary",
    "SURFACE": "SLICE:player_surface",
    "ASSETS": "SLICE:assets",
    "SAVE": "SLICE:save_schema",
    "MERGE": "SLICE:merge_fixture",
    "CAPTURE": "SLICE:capture_fixture",
    "PROFILE": "SLICE:profiling_fixture",
    "PACKAGE": "SLICE:package_fixture",
    "CONT": "SLICE:continuation_fixture",
}

SCENARIOS = {
    "S1": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "ACTIONS", "SURFACE", "ASSETS"]],
        "obligations": ["clean_reconstruct", "build", "launch", "cold_start", "incremental_observation"],
        "min_bounds": {"entity_count": 32, "asset_count": 8, "screen_count": 3},
        "required_injections": ["FI-S1-CACHE-MISS-v2"],
    },
    "S2": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "ACTIONS", "SURFACE", "ASSETS"]],
        "obligations": ["fresh_agent_change", "visible_or_state_visible_change", "reviewable_diff", "automated_verification"],
        "min_bounds": {"entity_count": 32, "asset_count": 8, "screen_count": 3, "changed_logical_locations": 1},
        "required_injections": ["FI-S2-STALE-META-v2"],
    },
    "S3": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "ACTIONS"]],
        "obligations": ["real_or_shared_rules", "exact_seed_input", "repeatable_state_events", "perturbation_distinguishable"],
        "min_bounds": {"entity_count": 32, "normal_ticks": 600, "action_count": 10},
        "required_injections": ["FI-S3-INPUT-PERTURB-v2"],
        "required_mechanism_authority": "REAL_OR_SHARED_RULES",
    },
    "S4": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "SAVE"]],
        "obligations": ["round_trip", "schema_evolution", "explicit_migration", "malformed_tuple_diagnostic"],
        "min_bounds": {"entity_count": 32, "save_v1_field_count": 5, "save_v2_added_field_count": 1},
        "required_injections": ["FI-S4-INCOMPAT-TUPLE-v2"],
    },
    "S5": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "SURFACE", "MERGE"]],
        "obligations": ["parallel_nonoverlap", "intentional_overlap", "visible_conflict", "post_merge_checks"],
        "min_bounds": {"overlap_count": 2, "branch_a_nonoverlap": 1, "branch_b_nonoverlap": 1},
        "required_injections": ["FI-S5-OVERLAP-v2"],
    },
    "S6": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "SURFACE", "CAPTURE"]],
        "obligations": ["reach_known_state", "identity_bound_capture", "state_vs_capture_failure_separated"],
        "min_bounds": {"screen_count": 3, "capture_frame_count": 1, "viewport_width": 1280, "viewport_height": 720},
        "required_injections": ["FI-S6-CAPTURE-DOWN-v2"],
    },
    "S7": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["ASSETS", "STATE"]],
        "obligations": ["inject_broken_reference", "diagnose_from_repo_cli", "bounded_repair", "rerun"],
        "min_bounds": {"asset_count": 8, "broken_reference_count": 1},
        "required_injections": ["FI-S7-BROKEN-REF-v2"],
    },
    "S8": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "PROFILE"]],
        "obligations": ["representative_workload", "parseable_profile", "locate_injected_hotspot", "resource_observations"],
        "min_bounds": {"normal_logical_updates": 19200, "hotspot_extra_updates": 3200},
        "required_injections": ["FI-S8-HOTSPOT-v2"],
    },
    "S9": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["STATE", "SURFACE", "ASSETS", "PACKAGE"]],
        "obligations": ["produce_common_package_target", "exact_repro_inputs", "clean_extract_launch", "typed_failed_package_diagnostic"],
        "min_bounds": {"screen_count": 3, "asset_count": 8},
        "required_injections": ["FI-S9-PACKAGE-CONFIG-v2"],
        "required_package_target": "WINDOWS_X64_DEV_PACKAGE-v1",
    },
    "S10": {
        "fixed_input_refs": [COMMON_REFS[x] for x in ["CONT", "STATE", "SURFACE"]],
        "obligations": ["repository_only_handoff", "fresh_context_reconstruct", "complete_remaining_actions", "rerun_evidence"],
        "min_bounds": {"remaining_action_count": 3, "required_handoff_field_count": 7},
        "required_injections": ["FI-S10-HANDOFF-GAP-v2"],
        "hidden_context_forbidden": True,
    },
}

COMMON_START_PROFILE = {
    "profile_id": "W2-ENG-START-COLD-v2",
    "cache_mode": "COLD",
    "generated_state_policy": "REGENERATE_FROM_REPO",
    "resource_class": "W2-ENG-HOST-COMMON-v2",
}


def base_adaptation(scenario_id):
    sc = SCENARIOS[scenario_id]
    return {
        "candidate_id": "SYNTHETIC-CANDIDATE",
        "scenario_id": scenario_id,
        "harness_id": "W2-ENG-HARNESS-v2",
        "feature_slice_id": "W2-ENG-FEATURE-SLICE-v2",
        "fixed_input_refs": list(sc["fixed_input_refs"]),
        "mappings": {o: "EQUIVALENT" for o in sc["obligations"]},
        "bounds": dict(sc["min_bounds"]),
        "failure_injections": list(sc["required_injections"]),
        "start_profile": copy.deepcopy(COMMON_START_PROFILE),
        "undocumented_manual_intervention": False,
        "resource_exception": False,
        "mechanism_authority": sc.get("required_mechanism_authority", "CANDIDATE_NATIVE_EQUIVALENT"),
        "package_target": sc.get("required_package_target"),
        "hidden_context_transfer": False,
        "extra_evidence": [],
    }


def validate_adaptation(adaptation):
    reasons = []
    scenario_id = adaptation.get("scenario_id")
    if scenario_id not in SCENARIOS:
        return {"result": "REJECT", "reasons": ["unknown_scenario"]}
    sc = SCENARIOS[scenario_id]
    if adaptation.get("harness_id") != "W2-ENG-HARNESS-v2":
        reasons.append("harness_mismatch")
    if adaptation.get("feature_slice_id") != "W2-ENG-FEATURE-SLICE-v2":
        reasons.append("feature_slice_mismatch")
    if not set(sc["fixed_input_refs"]).issubset(set(adaptation.get("fixed_input_refs", []))):
        reasons.append("missing_common_input_ref")
    for obligation in sc["obligations"]:
        if adaptation.get("mappings", {}).get(obligation) not in ("EQUIVALENT", "STRICTLY_STRONGER"):
            reasons.append(f"missing_or_weaker_obligation:{obligation}")
    for key, minimum in sc["min_bounds"].items():
        if adaptation.get("bounds", {}).get(key, -math.inf) < minimum:
            reasons.append(f"shrunk_bound:{key}")
    if not set(sc["required_injections"]).issubset(set(adaptation.get("failure_injections", []))):
        reasons.append("required_failure_injection_missing")
    start = adaptation.get("start_profile", {})
    if start.get("cache_mode") != "COLD" or start.get("generated_state_policy") != "REGENERATE_FROM_REPO":
        reasons.append("hidden_or_noncommon_start_state")
    if start.get("resource_class") != COMMON_START_PROFILE["resource_class"]:
        reasons.append("noncommon_resource_class")
    if adaptation.get("resource_exception"):
        reasons.append("unresolved_resource_exception")
    if adaptation.get("undocumented_manual_intervention"):
        reasons.append("hidden_manual_intervention")
    if sc.get("required_mechanism_authority") and adaptation.get("mechanism_authority") != sc["required_mechanism_authority"]:
        reasons.append("lower_authority_mechanism")
    if sc.get("required_package_target") and adaptation.get("package_target") != sc["required_package_target"]:
        reasons.append("common_package_target_missing")
    if sc.get("hidden_context_forbidden") and adaptation.get("hidden_context_transfer"):
        reasons.append("hidden_context_transfer")
    return {"result": "ACCEPT" if not reasons else "REJECT", "reasons": reasons}


def make_attempt_set(scenario_id, normal=("PASS", "PASS"), injection_result="PASS", omit_first=False,
                     reset_ids=("RESET-1", "RESET-2"), resource_class="W2-ENG-HOST-COMMON-v2"):
    sc = SCENARIOS[scenario_id]
    attempts = {}
    registry = []
    for index, result in enumerate(normal, start=1):
        attempt_id = f"{scenario_id}-N{index}"
        registry.append(attempt_id)
        attempts[attempt_id] = {
            "kind": "NORMAL",
            "index": index,
            "result": result,
            "reset_id": reset_ids[index - 1] if index - 1 < len(reset_ids) else None,
            "resource_class": resource_class,
        }
    for index, injection_id in enumerate(sc["required_injections"], start=1):
        attempt_id = f"{scenario_id}-FI{index}"
        registry.append(attempt_id)
        attempts[attempt_id] = {
            "kind": "FAILURE_INJECTION",
            "injection_id": injection_id,
            "result": injection_result,
            "reset_id": f"RESET-FI{index}",
            "resource_class": resource_class,
        }
    if omit_first:
        attempts.pop(f"{scenario_id}-N1", None)
    return {
        "scenario_id": scenario_id,
        "attempts": attempts,
        "run_registry_refs": registry,
        "all_attempt_refs": list(attempts.keys()),
    }


def aggregate_attempts(attempt_set):
    scenario_id = attempt_set["scenario_id"]
    sc = SCENARIOS[scenario_id]
    attempts = attempt_set["attempts"]
    reasons = []
    if set(attempt_set.get("run_registry_refs", [])) != set(attempts.keys()):
        reasons.append("attempt_registry_omission_or_extra")
    if set(attempt_set.get("all_attempt_refs", [])) != set(attempts.keys()):
        reasons.append("all_attempt_refs_mismatch")
    if reasons:
        return {"aggregate": "INCONCLUSIVE", "reasons": reasons}
    normal = sorted(
        [a for a in attempts.values() if a.get("kind") == "NORMAL"],
        key=lambda x: x.get("index", 0),
    )
    if len(normal) < 2:
        return {"aggregate": "NOT_RUN", "reasons": ["fewer_than_two_normal_attempts"]}
    if len({a.get("reset_id") for a in normal[:2]}) < 2:
        return {"aggregate": "INCONCLUSIVE", "reasons": ["normal_attempts_not_independently_reset"]}
    if any(a.get("resource_class") != COMMON_START_PROFILE["resource_class"] for a in attempts.values()):
        return {"aggregate": "INCONCLUSIVE", "reasons": ["resource_class_mismatch"]}
    injections = {
        a.get("injection_id"): a
        for a in attempts.values()
        if a.get("kind") == "FAILURE_INJECTION"
    }
    if any(injection_id not in injections for injection_id in sc["required_injections"]):
        return {"aggregate": "NOT_RUN", "reasons": ["required_injection_attempt_missing"]}
    normal_results = [a["result"] for a in normal[:2]]
    injection_results = [injections[injection_id]["result"] for injection_id in sc["required_injections"]]
    if len(set(normal_results)) > 1:
        return {"aggregate": "FLAKY", "reasons": ["normal_attempts_disagree"]}
    if any(result == "INCONCLUSIVE" for result in normal_results + injection_results):
        return {"aggregate": "INCONCLUSIVE", "reasons": ["inconclusive_attempt"]}
    if any(result != "PASS" for result in injection_results):
        return {"aggregate": "FAIL", "reasons": ["failure_recovery_assertion_failed"]}
    if all(result == "PASS" for result in normal_results):
        return {"aggregate": "PASS_FOR_COMPARISON", "reasons": []}
    return {"aggregate": "FAIL", "reasons": ["normal_required_behavior_failed"]}


FIXTURES = {}


def add_fixture(fixture_id, scenario_id, mutate=None, attempt_set=None, expected="ACCEPT"):
    adaptation = base_adaptation(scenario_id)
    if mutate:
        mutate(adaptation)
    FIXTURES[fixture_id] = {
        "adaptation": adaptation,
        "attempt_set": attempt_set,
        "expected": expected,
    }


add_fixture("EQ-01", "S2", expected="ACCEPT")
add_fixture("EQ-02", "S7", lambda a: a.__setitem__("failure_injections", []), expected="REJECT")
add_fixture("EQ-03", "S3", lambda a: a.__setitem__("mechanism_authority", "ABSTRACT_SIMULATOR"), expected="REJECT")
add_fixture("EQ-04", "S6", lambda a: a["extra_evidence"].append("FRAME_STATE_IDENTITY"), expected="ACCEPT")
add_fixture("EQ-05", "S1", lambda a: a["start_profile"].__setitem__("cache_mode", "UNDECLARED_WARM"), expected="REJECT")
add_fixture("EQ-06", "S8", lambda a: a["extra_evidence"].append("ADAPTER_PROFILE_PARSE"), expected="ACCEPT")
add_fixture("EQ-07", "S9", attempt_set=make_attempt_set("S9", normal=("FAIL", "PASS"), omit_first=True), expected="REJECT")
add_fixture("EQ-08", "S9", lambda a: a["extra_evidence"].append("EXTRA_PLATFORM_PACKAGE"), expected="ACCEPT")
add_fixture("EQ-09", "S5", lambda a: a["bounds"].__setitem__("overlap_count", 0), expected="REJECT")
add_fixture("EQ-10", "S2", lambda a: a.__setitem__("undocumented_manual_intervention", True), expected="REJECT")
add_fixture("EQ-11", "S4", lambda a: a["extra_evidence"].append("NATIVE_SERIALIZATION_EQUIVALENT"), expected="ACCEPT")
add_fixture("EQ-12", "S10", lambda a: a.__setitem__("hidden_context_transfer", True), expected="REJECT")
add_fixture("EQ-13", "S3", lambda a: a["bounds"].__setitem__("entity_count", 16), expected="REJECT")
add_fixture("EQ-14", "S8", lambda a: a["start_profile"].__setitem__("resource_class", "BIGGER-HOST-v1"), expected="REJECT")
add_fixture("EQ-15", "S1", lambda a: a["mappings"].pop("launch"), expected="REJECT")

RESULTS = {}
for fixture_id, fixture in FIXTURES.items():
    adaptation_result = validate_adaptation(fixture["adaptation"])
    overall = adaptation_result["result"]
    attempt_result = None
    if overall == "ACCEPT" and fixture.get("attempt_set") is not None:
        attempt_result = aggregate_attempts(fixture["attempt_set"])
        overall = "ACCEPT" if attempt_result["aggregate"] == "PASS_FOR_COMPARISON" else "REJECT"
    RESULTS[fixture_id] = {
        "overall": overall,
        "adaptation": adaptation_result,
        "attempt": attempt_result,
        "expected": fixture["expected"],
        "matches": overall == fixture["expected"],
    }

AGGREGATE_FIXTURES = {
    "AG-01_clean": make_attempt_set("S1"),
    "AG-02_disagree": make_attempt_set("S1", normal=("PASS", "FAIL")),
    "AG-03_one_normal": make_attempt_set("S1", normal=("PASS",)),
    "AG-04_missing_injection": make_attempt_set("S1"),
    "AG-05_same_reset": make_attempt_set("S1", reset_ids=("RESET-1", "RESET-1")),
    "AG-06_hidden_failed_attempt": make_attempt_set("S9", normal=("FAIL", "PASS"), omit_first=True),
}
for attempt_id in list(AGGREGATE_FIXTURES["AG-04_missing_injection"]["attempts"]):
    if AGGREGATE_FIXTURES["AG-04_missing_injection"]["attempts"][attempt_id]["kind"] == "FAILURE_INJECTION":
        AGGREGATE_FIXTURES["AG-04_missing_injection"]["attempts"].pop(attempt_id)
        AGGREGATE_FIXTURES["AG-04_missing_injection"]["run_registry_refs"].remove(attempt_id)
        AGGREGATE_FIXTURES["AG-04_missing_injection"]["all_attempt_refs"].remove(attempt_id)

AGGREGATE_RESULTS = {
    fixture_id: aggregate_attempts(fixture)
    for fixture_id, fixture in AGGREGATE_FIXTURES.items()
}
EXPECTED_AGGREGATES = {
    "AG-01_clean": "PASS_FOR_COMPARISON",
    "AG-02_disagree": "FLAKY",
    "AG-03_one_normal": "NOT_RUN",
    "AG-04_missing_injection": "NOT_RUN",
    "AG-05_same_reset": "INCONCLUSIVE",
    "AG-06_hidden_failed_attempt": "INCONCLUSIVE",
}

FIXTURE_INPUTS = {
    "fixtures": FIXTURES,
    "aggregate_fixtures": AGGREGATE_FIXTURES,
}
RESULT_OBJECT = {
    "equivalence_results": RESULTS,
    "aggregate_results": AGGREGATE_RESULTS,
}


def main():
    assert all(result["matches"] for result in RESULTS.values())
    assert all(
        AGGREGATE_RESULTS[key]["aggregate"] == expected
        for key, expected in EXPECTED_AGGREGATES.items()
    )
    print(json.dumps({key: value["overall"] for key, value in RESULTS.items()}, sort_keys=True))
    print(json.dumps({key: value["aggregate"] for key, value in AGGREGATE_RESULTS.items()}, sort_keys=True))
    print("validator_contract", canonical_digest(VALIDATOR_IDENTITY))
    print("feature_slice", canonical_digest(FEATURE_SLICE))
    print("scenario_manifest", canonical_digest(SCENARIOS))
    print("fixture_inputs", canonical_digest(FIXTURE_INPUTS))
    print("result_object", canonical_digest(RESULT_OBJECT))


if __name__ == "__main__":
    main()
