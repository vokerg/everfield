#!/usr/bin/env python3
"""Classify quarantined Unity user-login behavior without persisting auth material."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from typing import Any

SCHEMA = "W2-ENG-PROVIDER-UNITY-PERSONAL-HEADLESS-DIAG-v1"
SELFTEST_SCHEMA = "W2-ENG-PROVIDER-UNITY-PERSONAL-HEADLESS-DIAG-SELFTEST-v1"
MISSION_ID = "W2-ENG-PROVIDER-UNITY-PERSONAL-HEADLESS-DIAG-01"
ISSUE = 561

SENSITIVE_PATTERNS = (
    r"https?://",
    r"\buser[_ -]?code\b\s*[:=]",
    r"\bdevice[_ -]?code\b\s*[:=]",
    r"\baccess[_ -]?token\b\s*[:=]",
    r"\brefresh[_ -]?token\b\s*[:=]",
    r"\bstate\b\s*[:=]",
    r"\bcookie\b\s*[:=]",
)


def text(path: str) -> str:
    return pathlib.Path(path).read_text(encoding="utf-8", errors="replace")


def is_json(raw: str) -> bool:
    try:
        json.loads(raw)
        return True
    except Exception:
        return False


def classify_login(raw: str, exit_code: int, timed_out: bool) -> dict[str, Any]:
    low = raw.lower()
    browser = any(x in low for x in ("browser", "sign-in page", "sign in page", "open the following"))
    device = any(x in low for x in ("device code", "device_code", "user code", "user_code", "verification_uri"))
    noninteractive = "non-interactive" in low or "noninteractive" in low
    unsupported = any(x in low for x in ("not supported", "unsupported", "requires interaction", "interactive login"))
    service_account = "service account" in low or "client-id" in low or "client id" in low
    if device and not timed_out:
        disposition = "SUPPORTED_DEVICE_OR_NONINTERACTIVE_USER_FLOW_DISCOVERED_REQUIRES_REVIEW"
    elif timed_out or browser or (noninteractive and unsupported):
        disposition = "HEADLESS_USER_LOGIN_REQUIRES_INTERACTIVE_BROWSER_OR_PERSISTENT_SESSION"
    else:
        disposition = "HEADLESS_USER_LOGIN_DIAGNOSTIC_INCONCLUSIVE"
    return {
        "process_exit": exit_code,
        "timed_out": timed_out,
        "output_is_valid_json": is_json(raw),
        "mentions_browser_interaction": browser,
        "mentions_device_code_flow": device,
        "mentions_non_interactive": noninteractive,
        "mentions_non_interactive_not_supported": noninteractive and unsupported,
        "mentions_service_account": service_account,
        "disposition": disposition,
        "raw_output_persisted": False,
        "raw_output_hashed": False,
    }


def status_signed_in(raw: str) -> bool:
    low = raw.lower()
    # Deliberately narrow. Never emit identity text.
    negative = any(x in low for x in ("not signed in", "not authenticated", '"authenticated":false', '"signedin":false', '"signed_in":false'))
    positive = any(x in low for x in ('"authenticated":true', '"signedin":true', '"signed_in":true', '"user":{'))
    return positive and not negative


def build(args: argparse.Namespace) -> dict[str, Any]:
    login_raw = text(args.login_output)
    status_raw = text(args.status_output)
    login = classify_login(login_raw, args.login_exit, args.login_timed_out)
    signed_in = status_signed_in(status_raw)
    if signed_in:
        # Unexpected authentication is a fail-closed diagnostic outcome; do not treat as PASS.
        login["disposition"] = "HEADLESS_USER_LOGIN_DIAGNOSTIC_INCONCLUSIVE"
    return {
        "schema": SCHEMA,
        "mission_id": MISSION_ID,
        "issue": ISSUE,
        "unity_cli_expected_version": "1.0.0-beta.5",
        "unity_cli_observed_version": args.observed_version,
        "invocation": {
            "command": "unity auth login --no-store --non-interactive --format json",
            "credentials_supplied": False,
            "user_input_supplied": False,
            "hard_timeout_seconds": args.timeout_seconds,
        },
        "login": login,
        "post_login_status_signed_in": signed_in,
        "status_raw_output_persisted": False,
        "status_raw_output_hashed": False,
        "oauth_url_or_code_persisted": False,
        "credential_or_session_value_consumed": False,
        "provider_authentication_validated": False,
        "unity_license_validated": False,
        "integration_authority": False,
        "canonicality": "NOT_CANONICAL",
    }


def self_test() -> dict[str, Any]:
    cases: dict[str, bool] = {}
    browser = "Open your browser to https://example.invalid/login?state=SECRET"
    b = classify_login(browser, 124, True)
    cases["browser_timeout_classifies_external_session"] = b["disposition"] == "HEADLESS_USER_LOGIN_REQUIRES_INTERACTIVE_BROWSER_OR_PERSISTENT_SESSION"
    device = '{"verification_uri":"https://example.invalid","user_code":"ABCD"}'
    d = classify_login(device, 0, False)
    cases["device_flow_is_review_required"] = d["disposition"] == "SUPPORTED_DEVICE_OR_NONINTERACTIVE_USER_FLOW_DISCOVERED_REQUIRES_REVIEW"
    emitted = json.dumps({"login": b}, sort_keys=True)
    cases["sensitive_browser_url_not_emitted"] = "example.invalid" not in emitted and "SECRET" not in emitted
    cases["no_raw_or_hash_authority"] = b["raw_output_persisted"] is False and b["raw_output_hashed"] is False
    cases["status_negative_not_signed_in"] = status_signed_in('{"authenticated":false,"user":null}') is False
    # Validate evidence schema fields cannot accidentally contain raw auth-shaped data.
    safe = {"disposition": b["disposition"], "timed_out": b["timed_out"]}
    safe_text = json.dumps(safe)
    cases["safe_projection_has_no_sensitive_patterns"] = not any(re.search(p, safe_text, re.I) for p in SENSITIVE_PATTERNS)
    return {"schema": SELFTEST_SCHEMA, "cases": cases, "pass": all(cases.values())}


def emit(path: str | None, obj: dict[str, Any]) -> None:
    s = json.dumps(obj, sort_keys=True, indent=2) + "\n"
    if path:
        p = pathlib.Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(s, encoding="utf-8")
    print(s, end="")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--out")
    p.add_argument("--observed-version", default="")
    p.add_argument("--login-output")
    p.add_argument("--status-output")
    p.add_argument("--login-exit", type=int, default=127)
    p.add_argument("--login-timed-out", action="store_true")
    p.add_argument("--timeout-seconds", type=int, default=20)
    args = p.parse_args()
    if args.self_test:
        result = self_test()
        emit(args.out, result)
        return 0 if result["pass"] else 3
    if not args.login_output or not args.status_output:
        p.error("--login-output and --status-output required")
    result = build(args)
    emit(args.out, result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
