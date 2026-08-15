#!/usr/bin/env python3
"""Presence-only, non-secret provider-authority intake probe.

The workflow passes boolean presence flags and non-secret mode selectors only.
This script never accepts credential values and can never authorize W2-ENG.
"""
from __future__ import annotations

import argparse
import json
import os
import platform
from typing import Any

SCHEMA = "W2-ENG-PROVIDER-AUTHORITY-INTAKE-v1"
ALLOWED_UNITY_MODES = {"service_account_serial", "offline_file", "floating"}
ALLOWED_UNREAL_MODES = {"github_token", "preseed"}


def env_bool(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes"}


def normalized(name: str) -> str:
    return os.getenv(name, "").strip().lower()


def unity_state() -> dict[str, Any]:
    mode = normalized("UNITY_AUTH_MODE")
    present = {
        "service_account_id": env_bool("UNITY_SERVICE_ACCOUNT_ID_PRESENT"),
        "service_account_secret": env_bool("UNITY_SERVICE_ACCOUNT_SECRET_PRESENT"),
        "license_serial": env_bool("UNITY_LICENSE_SERIAL_PRESENT"),
        "offline_license_file": env_bool("UNITY_OFFLINE_LICENSE_PRESENT"),
        "floating_config": env_bool("UNITY_FLOATING_CONFIG_PRESENT"),
    }
    missing: list[str] = []
    if mode not in ALLOWED_UNITY_MODES:
        missing.append("UNITY_AUTH_MODE must be one of: service_account_serial, offline_file, floating")
    elif mode == "service_account_serial":
        if not present["service_account_id"]:
            missing.append("UNITY_SERVICE_ACCOUNT_ID")
        if not present["service_account_secret"]:
            missing.append("UNITY_SERVICE_ACCOUNT_SECRET")
        if not present["license_serial"]:
            missing.append("UNITY_LICENSE_SERIAL")
    elif mode == "offline_file":
        if not present["offline_license_file"]:
            missing.append("UNITY_OFFLINE_LICENSE_B64")
    elif mode == "floating":
        if not present["floating_config"]:
            missing.append("UNITY_FLOATING_CONFIG_B64")

    state = "AUTHORITY_REQUIRED" if missing else "INPUT_PRESENT_UNVALIDATED"
    return {
        "provider": "Unity",
        "frozen_editor_baseline": "6000.5.6f1",
        "mode": mode if mode in ALLOWED_UNITY_MODES else "UNSET_OR_INVALID",
        "presence": present,
        "state": state,
        "missing_predicates": missing,
        "account_authentication_equals_editor_license": False,
        "effective_authorization_validated": False,
        "credential_values_read": False,
    }


def unreal_state() -> dict[str, Any]:
    mode = normalized("UNREAL_AUTH_MODE")
    present = {
        "github_token": env_bool("UNREAL_GITHUB_TOKEN_PRESENT"),
        "preseed_url": env_bool("UNREAL_PRESEED_URL_PRESENT"),
        "preseed_sha256": env_bool("UNREAL_PRESEED_SHA256_PRESENT"),
    }
    missing: list[str] = []
    if mode not in ALLOWED_UNREAL_MODES:
        missing.append("UNREAL_AUTH_MODE must be one of: github_token, preseed")
    elif mode == "github_token":
        if not present["github_token"]:
            missing.append("UNREAL_GITHUB_TOKEN with effective EpicGames/UnrealEngine access")
    elif mode == "preseed":
        if not present["preseed_url"]:
            missing.append("UNREAL_5_8_PRESEED_URL")
        if not present["preseed_sha256"]:
            missing.append("UNREAL_5_8_PRESEED_SHA256")

    state = "AUTHORITY_REQUIRED" if missing else "INPUT_PRESENT_UNVALIDATED"
    return {
        "provider": "Unreal Engine",
        "frozen_engine_baseline": "5.8",
        "mode": mode if mode in ALLOWED_UNREAL_MODES else "UNSET_OR_INVALID",
        "presence": present,
        "state": state,
        "missing_predicates": missing,
        "repository_github_token_cross_repo_entitlement_assumed": False,
        "effective_authorization_validated": False,
        "credential_values_read": False,
    }


def classify() -> dict[str, Any]:
    unity = unity_state()
    unreal = unreal_state()
    both_present = unity["state"] == "INPUT_PRESENT_UNVALIDATED" and unreal["state"] == "INPUT_PRESENT_UNVALIDATED"
    return {
        "schema": SCHEMA,
        "mission_id": "W2-ENG-PROVIDER-AUTH-PRESEED-01",
        "source_issue": 347,
        "source_main_sha": "92204cb2e58c792ef4199fe3562ca2192096f5c0",
        "canonical_program_blob": "e3120ec203c4156328770aa86c12fbb7187966dc",
        "engine_source_issue": 82,
        "engine_source_terminal_comment": 5276916603,
        "historical_not_run_cells_preserved": 50,
        "prior_not_run_promoted": False,
        "runner": {
            "platform": platform.platform(),
            "machine": platform.machine(),
            "image_os": os.getenv("ImageOS"),
            "image_version": os.getenv("ImageVersion"),
            "github_sha": os.getenv("GITHUB_SHA"),
            "github_run_id": os.getenv("GITHUB_RUN_ID"),
            "github_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT"),
        },
        "providers": {"Unity": unity, "Unreal Engine": unreal},
        "both_input_sets_present": both_present,
        "overall_state": "BOTH_INPUT_SETS_PRESENT_VALIDATION_REQUIRED" if both_present else "AUTHORITY_REQUIRED_EXACT",
        "effective_provider_authority_validated": False,
        "five_candidate_empirical_successor_unlocked": False,
        "workflow_success_is_not_authority": True,
        "secret_values_accepted_by_probe": False,
    }


def self_test() -> dict[str, Any]:
    original = dict(os.environ)
    cases: dict[str, bool] = {}
    keys = [
        "UNITY_AUTH_MODE", "UNITY_SERVICE_ACCOUNT_ID_PRESENT", "UNITY_SERVICE_ACCOUNT_SECRET_PRESENT",
        "UNITY_LICENSE_SERIAL_PRESENT", "UNITY_OFFLINE_LICENSE_PRESENT", "UNITY_FLOATING_CONFIG_PRESENT",
        "UNREAL_AUTH_MODE", "UNREAL_GITHUB_TOKEN_PRESENT", "UNREAL_PRESEED_URL_PRESENT", "UNREAL_PRESEED_SHA256_PRESENT",
    ]
    try:
        for key in keys:
            os.environ.pop(key, None)
        empty = classify()
        cases["empty_is_exact_authority_required"] = empty["overall_state"] == "AUTHORITY_REQUIRED_EXACT"
        cases["empty_never_unlocks"] = empty["five_candidate_empirical_successor_unlocked"] is False

        os.environ["UNITY_AUTH_MODE"] = "service_account_serial"
        os.environ["UNITY_SERVICE_ACCOUNT_ID_PRESENT"] = "true"
        os.environ["UNITY_SERVICE_ACCOUNT_SECRET_PRESENT"] = "true"
        partial = classify()
        cases["partial_unity_rejected"] = partial["providers"]["Unity"]["state"] == "AUTHORITY_REQUIRED"

        os.environ["UNITY_LICENSE_SERIAL_PRESENT"] = "true"
        unity_only = classify()
        cases["one_provider_never_unlocks"] = unity_only["overall_state"] == "AUTHORITY_REQUIRED_EXACT" and not unity_only["five_candidate_empirical_successor_unlocked"]

        os.environ["UNREAL_AUTH_MODE"] = "github_token"
        os.environ["UNREAL_GITHUB_TOKEN_PRESENT"] = "true"
        both = classify()
        cases["both_present_still_unvalidated"] = both["overall_state"] == "BOTH_INPUT_SETS_PRESENT_VALIDATION_REQUIRED"
        cases["presence_never_becomes_authority"] = both["effective_provider_authority_validated"] is False and not both["five_candidate_empirical_successor_unlocked"]
    finally:
        os.environ.clear()
        os.environ.update(original)
    return {"schema": "W2-ENG-PROVIDER-AUTHORITY-SELFTEST-v1", "cases": cases, "pass": all(cases.values())}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    result = self_test() if args.self_test else classify()
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    print(text, end="")
    if args.self_test and not result["pass"]:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
