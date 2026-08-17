#!/usr/bin/env python3
"""Presence-only Unity license configuration diagnostic.

The trusted-main mode accepts only a non-secret mode selector, boolean presence
flags, the reviewed repository input contract, and non-secret Unity CLI help
text. It never accepts provider credential or license values and cannot grant
provider or license authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
from typing import Any

SCHEMA = "W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-DIAG-v1"
SELFTEST_SCHEMA = "W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-DIAG-SELFTEST-v1"
MISSION_ID = "W2-ENG-PROVIDER-UNITY-LICENSE-CONFIG-MAIN-DIAG-01"
ISSUE = 539
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
SECRET_TO_LOGICAL = {
    "UNITY_SERVICE_ACCOUNT_ID": "service_account_id",
    "UNITY_SERVICE_ACCOUNT_SECRET": "service_account_secret",
    "UNITY_LICENSE_SERIAL": "license_serial",
    "UNITY_OFFLINE_LICENSE_B64": "offline_license_file",
    "UNITY_FLOATING_CONFIG_B64": "floating_config",
}


def env_bool(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes"}


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def load_contract(path: pathlib.Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    data = json.loads(raw.decode("utf-8"))
    blob = git_blob_sha(raw)
    if blob != EXPECTED_CONTRACT_BLOB:
        raise ValueError(f"unexpected provider-authority contract blob: {blob}")
    if data.get("schema") != EXPECTED_CONTRACT_SCHEMA:
        raise ValueError("unexpected provider-authority contract schema")
    unity = data.get("unity")
    if not isinstance(unity, dict) or unity.get("baseline") != BASELINE:
        raise ValueError("unexpected Unity contract baseline")
    if unity.get("mode_variable") != "UNITY_AUTH_MODE":
        raise ValueError("unexpected Unity mode variable")
    return data, blob


def requirements(contract: dict[str, Any]) -> dict[str, list[str]]:
    allowed = contract["unity"].get("allowed_modes")
    expected = {"service_account_serial", "offline_file", "floating"}
    if not isinstance(allowed, dict) or set(allowed) != expected:
        raise ValueError("Unity allowed_modes drift")
    result: dict[str, list[str]] = {}
    for mode, spec in allowed.items():
        required = spec.get("secret_presence_required") if isinstance(spec, dict) else None
        if not isinstance(required, list) or not all(isinstance(item, str) and item in SECRET_TO_LOGICAL for item in required):
            raise ValueError(f"invalid Unity presence contract for {mode}")
        result[mode] = list(required)
    return result


def classify(contract: dict[str, Any]) -> dict[str, Any]:
    req = requirements(contract)
    mode = os.getenv("UNITY_AUTH_MODE", "").strip().lower()
    presence = {logical: env_bool(env_name) for logical, env_name in PRESENCE_ENV.items()}
    if mode not in req:
        selected = "UNSET_OR_INVALID"
        required_logical: list[str] = []
        missing = ["UNITY_AUTH_MODE must be one of: service_account_serial, offline_file, floating"]
        disposition = "UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT"
    else:
        selected = mode
        required_names = req[mode]
        required_logical = [SECRET_TO_LOGICAL[name] for name in required_names]
        missing = [name for name in required_names if not presence[SECRET_TO_LOGICAL[name]]]
        disposition = (
            "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING"
            if not missing
            else "UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT"
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


def read_help(path: str) -> str:
    return pathlib.Path(path).read_text(encoding="utf-8", errors="replace")


def normalize_help(text: str, exit_code: int) -> dict[str, Any]:
    raw = text.encode("utf-8", errors="replace")
    options = sorted(set(re.findall(r"(?<![A-Za-z0-9_])--[A-Za-z][A-Za-z0-9-]*", text)))[:100]
    subcommands: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^\s{2,}([a-z][a-z0-9-]{1,40})\s{2,}\S", line)
        if match and match.group(1) not in {"usage", "options", "commands", "arguments"}:
            subcommands.add(match.group(1))
    return {
        "exit": exit_code,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "raw_bytes": len(raw),
        "options": options,
        "subcommands": sorted(subcommands)[:100],
        "raw_text_persisted": False,
    }


def evidence(args: argparse.Namespace) -> dict[str, Any]:
    contract, blob = load_contract(pathlib.Path(args.contract))
    return {
        "schema": SCHEMA,
        "mission_id": MISSION_ID,
        "issue": ISSUE,
        "baseline": BASELINE,
        "source_blocker": "UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED",
        "source_license_status_exit": 4,
        "reviewed_input_contract": {"schema": EXPECTED_CONTRACT_SCHEMA, "git_blob": blob},
        "unity": classify(contract),
        "cli": {
            "expected_version": "1.0.0-beta.5",
            "observed_version": os.getenv("UNITY_CLI_OBSERVED_VERSION", ""),
            "command_surface": {
                "license": normalize_help(read_help(args.license_help), args.license_help_exit),
                "license_status": normalize_help(read_help(args.status_help), args.status_help_exit),
                "config": normalize_help(read_help(args.config_help), args.config_help_exit),
            },
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
        "unity": {
            "allowed_modes": {
                "service_account_serial": {"secret_presence_required": ["UNITY_SERVICE_ACCOUNT_ID", "UNITY_SERVICE_ACCOUNT_SECRET", "UNITY_LICENSE_SERIAL"]},
                "offline_file": {"secret_presence_required": ["UNITY_OFFLINE_LICENSE_B64"]},
                "floating": {"secret_presence_required": ["UNITY_FLOATING_CONFIG_B64"]},
            }
        }
    }
    try:
        os.environ.pop("UNITY_AUTH_MODE", None)
        set_presence()
        cases["unset_mode_is_exact_input_required"] = classify(contract)["disposition"] == "UNITY_LICENSE_CONFIGURATION_INPUT_REQUIRED_EXACT"

        os.environ["UNITY_AUTH_MODE"] = "service_account_serial"
        set_presence(service_account_id=True, service_account_secret=True)
        cases["serial_missing_is_exact"] = classify(contract)["missing_predicates"] == ["UNITY_LICENSE_SERIAL"]
        set_presence(service_account_id=True, service_account_secret=True, license_serial=True)
        cases["serial_complete_routes_wiring"] = classify(contract)["disposition"] == "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING"

        os.environ["UNITY_AUTH_MODE"] = "offline_file"
        set_presence(offline_license_file=True, license_serial=True)
        offline = classify(contract)
        cases["offline_complete_ignores_unrelated_presence"] = offline["disposition"] == "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING" and offline["required_presence_for_selected_mode"] == ["offline_license_file"]

        os.environ["UNITY_AUTH_MODE"] = "floating"
        set_presence(floating_config=True)
        floating = classify(contract)
        cases["floating_complete_routes_wiring"] = floating["disposition"] == "UNITY_LICENSE_MODE_PRESENT_NEEDS_EFFECTIVE_WIRING"
        cases["presence_never_grants_authority"] = floating["effective_authorization_validated"] is False and floating["credential_or_license_values_read"] is False

        sample = "Commands:\n  status  Show status\n  activate  Activate license\nOptions:\n  --format value\n  --no-banner\n"
        surface = normalize_help(sample, 0)
        cases["help_is_bounded"] = surface["subcommands"] == ["activate", "status"] and surface["options"] == ["--format", "--no-banner"] and surface["raw_text_persisted"] is False
    finally:
        os.environ.clear()
        os.environ.update(original)
    return {"schema": SELFTEST_SCHEMA, "cases": cases, "pass": all(cases.values())}


def emit(path: str | None, result: dict[str, Any]) -> None:
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if path:
        target = pathlib.Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
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
        emit(args.out, result)
        return 0 if result["pass"] else 3
    for value, flag in ((args.license_help, "--license-help"), (args.status_help, "--status-help"), (args.config_help, "--config-help")):
        if not value:
            parser.error(f"{flag} is required outside --self-test")
    result = evidence(args)
    emit(args.out, result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
