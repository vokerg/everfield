#!/usr/bin/env python3
"""Presence-only Unity license configuration diagnostic.

This helper accepts only non-secret mode selectors, boolean presence flags, the
reviewed repository input contract, and non-secret Unity CLI help text. It never
accepts provider credential or license values and cannot establish provider or
license authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import tempfile
from typing import Any

SCHEMA = "W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-DIAG-v1"
SELFTEST_SCHEMA = "W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-DIAG-SELFTEST-v1"
MISSION_ID = "W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-DIAG-01"
ISSUE = 535
BASELINE = "6000.5.6f1"
EXPECTED_CONTRACT_SCHEMA = "W2-ENG-PROVIDER-AUTHORITY-CONTRACT-v1"
EXPECTED_CONTRACT_BLOB = "a4c40fe1f77ec9557dbe0d76af3e947f188c96be"
PRESENCE_ENV = {
    "service_account_id": "UNITY_SERVICE_ACCOUNT_ID_PRESENT",
    "service_account_secret": "UNITY_SERVICE_ACCOUNT_SECRET_PRESENT",
    "license_serial": "UNITY_LICENSE_SERIAL_PRESENT",
    "offline_license_file": "UNITY_OFFLINE_LICENSE_PRESENT",
    "floating_config": "UNITY_FLOATING_CONFIG_PRESENT",
}
SECRET_VALUE_ENV_NAMES = {
    "UNITY_SERVICE_ACCOUNT_ID",
    "UNITY_SERVICE_ACCOUNT_SECRET",
    "UNITY_LICENSE_SERIAL",
    "UNITY_OFFLINE_LICENSE_B64",
    "UNITY_FLOATING_CONFIG_B64",
}


def env_bool(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes"}


def normalized_mode() -> str:
    return os.getenv("UNITY_AUTH_MODE", "").strip().lower()


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def load_contract(path: pathlib.Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    data = json.loads(raw.decode("utf-8"))
    if data.get("schema") != EXPECTED_CONTRACT_SCHEMA:
        raise ValueError("unexpected provider-authority contract schema")
    unity = data.get("unity")
    if not isinstance(unity, dict) or unity.get("baseline") != BASELINE:
        raise ValueError("unexpected Unity contract baseline")
    if unity.get("mode_variable") != "UNITY_AUTH_MODE":
        raise ValueError("unexpected Unity mode variable")
    blob = git_blob_sha(raw)
    if blob != EXPECTED_CONTRACT_BLOB:
        raise ValueError(f"unexpected provider-authority contract blob: {blob}")
    return data, blob


def read_help(path: pathlib.Path | None) -> str:
    if path is None or not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def normalize_help(text: str, exit_code: int) -> dict[str, Any]:
    raw = text.encode("utf-8", errors="replace")
    options = sorted(set(re.findall(r"(?<![A-Za-z0-9_])--[A-Za-z][A-Za-z0-9-]*", text)))[:100]
    subcommands: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^\s{2,}([a-z][a-z0-9-]{1,40})\s{2,}\S", line)
        if match:
            token = match.group(1)
            if token not in {"usage", "options", "commands", "arguments"}:
                subcommands.add(token)
    return {
        "exit": exit_code,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "raw_bytes": len(raw),
        "options": options,
        "subcommands": sorted(subcommands)[:100],
        "raw_text_persisted": False,
    }


def contract_requirements(contract: dict[str, Any]) -> dict[str, list[str]]:
    allowed = contract["unity"].get("allowed_modes")
    if not isinstance(allowed, dict):
        raise ValueError("Unity allowed_modes missing")
    expected = {"service_account_serial", "offline_file", "floating"}
    if set(allowed) != expected:
        raise ValueError("Unity allowed_modes drift")
    result: dict[str, list[str]] = {}
    for mode, spec in allowed.items():
        required = spec.get("secret_presence_required") if isinstance(spec, dict) else None
        if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
            raise ValueError(f"invalid required presence list for {mode}")
        result[mode] = list(required)
    return result


def logical_presence() -> dict[str, bool]:
    return {key: env_bool(env_name) for key, env_name in PRESENCE_ENV.items()}


def secret_name_to_logical(name: str) -> str:
    mapping = {
        "UNITY_SERVICE_ACCOUNT_ID": "service_account_id",
        "UNITY_SERVICE_ACCOUNT_SECRET": "service_account_secret",
        "UNITY_LICENSE_SERIAL": "license_serial",
        "UNITY_OFFLINE_LICENSE_B64": "offline_license_file",
        "UNITY_FLOATING_CONFIG_B64": "floating_config",
    }
    if name not in mapping:
        raise ValueError(f"undeclared Unity secret presence name: {name}")
    return mapping[name]


def classify(contract: dict[str, Any]) -> dict[str, Any]:
    requirements = contract_requirements(contract)
    mode = normalized_mode()
    presence = logical_presence()
    if mode not in requirements:
        missing = ["UNITY_AUTH_MODE must be one of: service_account_serial, offline_file, floating"]
        disposition = "UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT"
        selected = "UNSET_OR_INVALID"
        required_logical: list[str] = []
    else:
        selected = mode
        required_secret_names = requirements[mode]
        required_logical = [secret_name_to_logical(name) for name in required_secret_names]
        missing = [name for name in required_secret_names if not presence[secret_name_to_logical(name)]]
        disposition = (
            "UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT"
            if missing
            else "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING"
        )
    return {
        "mode": selected,
        "presence": presence,
        "required_presence_for_selected_mode": required_logical,
        "missing_predicates": missing,
        "disposition": disposition,
        "presence_is_authorization": False,
        "effective_authorization_validated": False,
        "credential_or_license_values_read": False,
    }


def build_evidence(args: argparse.Namespace) -> dict[str, Any]:
    contract, contract_blob = load_contract(pathlib.Path(args.contract))
    state = classify(contract)
    command_surface = {
        "license": normalize_help(read_help(pathlib.Path(args.license_help)), args.license_help_exit),
        "license_status": normalize_help(read_help(pathlib.Path(args.status_help)), args.status_help_exit),
        "config": normalize_help(read_help(pathlib.Path(args.config_help)), args.config_help_exit),
    }
    return {
        "schema": SCHEMA,
        "mission_id": MISSION_ID,
        "issue": ISSUE,
        "baseline": BASELINE,
        "canonical_program_blob": "e3120ec203c4156328770aa86c12fbb7187966dc",
        "source_blocker": "UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED",
        "source_license_status_exit": 4,
        "reviewed_input_contract": {
            "schema": EXPECTED_CONTRACT_SCHEMA,
            "git_blob": contract_blob,
        },
        "unity": state,
        "cli": {
            "expected_version": "1.0.0-beta.5",
            "observed_version": os.getenv("UNITY_CLI_OBSERVED_VERSION", ""),
            "command_surface": command_surface,
        },
        "runner": {
            "github_sha": os.getenv("GITHUB_SHA"),
            "github_run_id": os.getenv("GITHUB_RUN_ID"),
            "github_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT"),
            "image_os": os.getenv("ImageOS"),
            "image_version": os.getenv("ImageVersion"),
        },
        "secret_values_accepted_by_probe": False,
        "secret_hashes_in_evidence": False,
        "provider_pass": False,
        "unity_license_authority": False,
        "editor_execution_authority": False,
        "integration_authority": False,
        "canonicality": "NOT_CANONICAL",
    }


def set_presence(**kwargs: bool) -> None:
    for logical, env_name in PRESENCE_ENV.items():
        os.environ[env_name] = "true" if kwargs.get(logical, False) else "false"


def self_test() -> dict[str, Any]:
    original = dict(os.environ)
    cases: dict[str, bool] = {}
    contract = {
        "schema": EXPECTED_CONTRACT_SCHEMA,
        "unity": {
            "baseline": BASELINE,
            "mode_variable": "UNITY_AUTH_MODE",
            "allowed_modes": {
                "service_account_serial": {"secret_presence_required": ["UNITY_SERVICE_ACCOUNT_ID", "UNITY_SERVICE_ACCOUNT_SECRET", "UNITY_LICENSE_SERIAL"]},
                "offline_file": {"secret_presence_required": ["UNITY_OFFLINE_LICENSE_B64"]},
                "floating": {"secret_presence_required": ["UNITY_FLOATING_CONFIG_B64"]},
            },
        },
    }
    try:
        for name in PRESENCE_ENV.values():
            os.environ.pop(name, None)
        for name in SECRET_VALUE_ENV_NAMES:
            os.environ.pop(name, None)
        os.environ.pop("UNITY_AUTH_MODE", None)

        set_presence()
        invalid = classify(contract)
        cases["unset_mode_routes_exact_input_required"] = invalid["disposition"] == "UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT"

        os.environ["UNITY_AUTH_MODE"] = "service_account_serial"
        set_presence(service_account_id=True, service_account_secret=True)
        missing_serial = classify(contract)
        cases["service_account_without_serial_is_incomplete"] = missing_serial["missing_predicates"] == ["UNITY_LICENSE_SERIAL"]

        set_presence(service_account_id=True, service_account_secret=True, license_serial=True)
        serial = classify(contract)
        cases["service_account_serial_complete_routes_wiring"] = serial["disposition"] == "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING"

        os.environ["UNITY_AUTH_MODE"] = "offline_file"
        set_presence(offline_license_file=True, license_serial=True)
        offline = classify(contract)
        cases["unrelated_presence_does_not_change_selected_mode"] = offline["disposition"] == "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING" and offline["required_presence_for_selected_mode"] == ["offline_license_file"]

        os.environ["UNITY_AUTH_MODE"] = "floating"
        set_presence(floating_config=True)
        floating = classify(contract)
        cases["floating_complete_routes_wiring"] = floating["disposition"] == "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING"

        sample = "Commands:\n  status  Show status\n  activate  Activate license\nOptions:\n  --format value\n  --no-banner\n"
        normalized = normalize_help(sample, 0)
        cases["help_normalization_is_bounded"] = normalized["subcommands"] == ["activate", "status"] and normalized["options"] == ["--format", "--no-banner"] and normalized["raw_text_persisted"] is False

        serialized = json.dumps({"unity": floating, "help": normalized}, sort_keys=True)
        cases["no_secret_value_fields_emitted"] = all(name not in serialized for name in SECRET_VALUE_ENV_NAMES)
        cases["presence_never_grants_authority"] = floating["effective_authorization_validated"] is False and floating["credential_or_license_values_read"] is False
    finally:
        os.environ.clear()
        os.environ.update(original)
    return {"schema": SELFTEST_SCHEMA, "cases": cases, "pass": all(cases.values())}


def write_json(path: str | None, data: dict[str, Any]) -> None:
    text = json.dumps(data, sort_keys=True, indent=2) + "\n"
    if path:
        out = pathlib.Path(path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    print(text, end="")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", default="docs/planning/wave-2/evidence/provider-authority-input-contract.json")
    parser.add_argument("--license-help")
    parser.add_argument("--status-help")
    parser.add_argument("--config-help")
    parser.add_argument("--license-help-exit", type=int, default=127)
    parser.add_argument("--status-help-exit", type=int, default=127)
    parser.add_argument("--config-help-exit", type=int, default=127)
    parser.add_argument("--out")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        result = self_test()
        write_json(args.out, result)
        return 0 if result["pass"] else 3
    if not args.license_help or not args.status_help or not args.config_help:
        parser.error("--license-help, --status-help, and --config-help are required outside --self-test")
    result = build_evidence(args)
    write_json(args.out, result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
