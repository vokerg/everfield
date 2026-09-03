#!/usr/bin/env python3
"""Project bounded, non-secret Unity CLI help into Personal-path evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
from typing import Any

SCHEMA = "W2-ENG-PROVIDER-UNITY-PERSONAL-PATH-DIAG-v1"
SELFTEST_SCHEMA = "W2-ENG-PROVIDER-UNITY-PERSONAL-PATH-DIAG-SELFTEST-v1"
MISSION_ID = "W2-ENG-PROVIDER-UNITY-PERSONAL-PATH-DIAG-01"
ISSUE = 557

TOKENS = {
    "personal_flag": "--personal",
    "accept_eula_flag": "--accept-eula",
    "client_id_flag": "--client-id",
    "secret_stdin_flag": "--secret-from-stdin",
    "serial_flag": "--serial",
    "license_file_flag": "--license-file",
    "floating_flag": "--floating",
    "non_interactive_flag": "--non-interactive",
    "browser_concept": "browser",
    "device_concept": "device",
    "session_concept": "session",
    "token_concept": "token",
    "export_concept": "export",
    "import_concept": "import",
    "user_concept": "user",
}


def normalize(text: str, exit_code: int) -> dict[str, Any]:
    lowered = text.lower()
    raw = text.encode("utf-8", errors="replace")
    options = sorted(set(re.findall(r"(?<![A-Za-z0-9_])--[A-Za-z][A-Za-z0-9-]*", text)))[:120]
    subcommands: set[str] = set()
    for line in text.splitlines():
        m = re.match(r"^\s{2,}([a-z][a-z0-9-]{1,40})\s{2,}\S", line.lower())
        if m and m.group(1) not in {"usage", "options", "commands", "arguments"}:
            subcommands.add(m.group(1))
    return {
        "exit": exit_code,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "raw_bytes": len(raw),
        "options": options,
        "subcommands": sorted(subcommands)[:120],
        "tokens": {name: token.lower() in lowered for name, token in TOKENS.items()},
        "raw_text_persisted": False,
    }


def read(path: str) -> str:
    return pathlib.Path(path).read_text(encoding="utf-8", errors="replace")


def conclude(commands: dict[str, Any]) -> str:
    activate = commands["license_activate"]
    auth_login = commands["auth_login"]
    if activate["exit"] != 0 or not activate["tokens"]["personal_flag"]:
        return "PINNED_CLI_PERSONAL_PATH_SURFACE_INCONSISTENT"
    unattended_user_signal = any(
        auth_login["tokens"][name]
        for name in ("browser_concept", "device_concept", "session_concept", "token_concept", "user_concept")
    )
    service_account_signal = auth_login["tokens"]["client_id_flag"] and auth_login["tokens"]["secret_stdin_flag"]
    if unattended_user_signal and not service_account_signal:
        return "PERSONAL_PATH_SUPPORTED_CONTRACT_REMEDIATION_REQUIRED"
    return "PERSONAL_PATH_REQUIRES_EXACT_EXTERNAL_USER_SESSION_PREDICATE"


def build(args: argparse.Namespace) -> dict[str, Any]:
    command_specs = {
        "auth": (args.auth_help, args.auth_exit),
        "auth_login": (args.auth_login_help, args.auth_login_exit),
        "auth_status": (args.auth_status_help, args.auth_status_exit),
        "license": (args.license_help, args.license_exit),
        "license_activate": (args.activate_help, args.activate_exit),
        "license_status": (args.status_help, args.status_exit),
    }
    commands = {name: normalize(read(path), code) for name, (path, code) in command_specs.items()}
    return {
        "schema": SCHEMA,
        "mission_id": MISSION_ID,
        "issue": ISSUE,
        "unity_cli_expected_version": "1.0.0-beta.5",
        "unity_cli_observed_version": args.observed_version,
        "commands": commands,
        "historical_facts": {
            "personal_user_oauth_activation_succeeded": True,
            "service_account_personal_result": "SERVICE_ACCOUNT_UNSUPPORTED",
            "source_issue": 373,
        },
        "current_protected_config": {
            "source_run": 32007010902,
            "auth_mode": "UNSET_OR_INVALID",
            "service_account_id_present": True,
            "service_account_secret_present": True,
            "license_serial_present": False,
            "offline_license_present": False,
            "floating_config_present": False,
        },
        "disposition": conclude(commands),
        "provider_authentication_validated": False,
        "unity_license_validated": False,
        "credential_or_session_value_consumed": False,
        "activation_command_executed": False,
        "integration_authority": False,
        "canonicality": "NOT_CANONICAL",
    }


def self_test() -> dict[str, Any]:
    cases: dict[str, bool] = {}
    sample_activate = "Options:\n  --personal  Activate Personal\n  --accept-eula\n  --non-interactive\n"
    a = normalize(sample_activate, 0)
    cases["personal_detected"] = a["tokens"]["personal_flag"] and a["tokens"]["accept_eula_flag"]
    cases["raw_not_persisted"] = a["raw_text_persisted"] is False and "Activate Personal" not in json.dumps(a)
    sample_service = "Options:\n  --client-id value\n  --secret-from-stdin\n"
    s = normalize(sample_service, 0)
    cases["service_account_flags_detected"] = s["tokens"]["client_id_flag"] and s["tokens"]["secret_stdin_flag"]
    cases["no_false_session"] = not s["tokens"]["session_concept"] and not s["tokens"]["token_concept"]
    sample_device = "Use browser device login for user authentication"
    d = normalize(sample_device, 0)
    cases["user_transport_concepts_detected"] = d["tokens"]["browser_concept"] and d["tokens"]["device_concept"] and d["tokens"]["user_concept"]
    return {"schema": SELFTEST_SCHEMA, "cases": cases, "pass": all(cases.values())}


def emit(path: str | None, obj: dict[str, Any]) -> None:
    text = json.dumps(obj, sort_keys=True, indent=2) + "\n"
    if path:
        p = pathlib.Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    print(text, end="")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--out")
    p.add_argument("--observed-version", default="")
    for prefix in ("auth", "auth-login", "auth-status", "license", "activate", "status"):
        p.add_argument(f"--{prefix}-help")
        p.add_argument(f"--{prefix}-exit", type=int, default=127)
    args = p.parse_args()
    if args.self_test:
        result = self_test()
        emit(args.out, result)
        return 0 if result["pass"] else 3
    required = [args.auth_help, args.auth_login_help, args.auth_status_help, args.license_help, args.activate_help, args.status_help]
    if not all(required):
        p.error("all help-file arguments are required outside --self-test")
    result = build(args)
    emit(args.out, result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
