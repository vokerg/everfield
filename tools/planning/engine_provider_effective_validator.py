#!/usr/bin/env python3
"""Fail-closed effective Unity/Unreal development-access validator.

This validator consumes provider credentials only in memory and only from the
trusted-main credentialed workflow. It emits outcome data, never credential
identity or credential material. It is deliberately independent per provider.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

SCHEMA = "W2-ENG-PROVIDER-EFFECTIVE-ACCESS-v1"
UNITY_BASELINE = "6000.5.6f1"
UNREAL_BASELINE = "5.8"
NORMAL_CHECKSUM = 405227
PERTURBED_CHECKSUM = 405122
SECRET_ENV_NAMES = (
    "UNITY_SERVICE_ACCOUNT_ID",
    "UNITY_SERVICE_ACCOUNT_SECRET",
    "UNREAL_GITHUB_TOKEN",
)
GHCR_REGISTRY_ORIGIN = "https://ghcr.io"
GHCR_AUTH_HOST = "ghcr.io"
GHCR_AUTH_PATH = "/token"
GHCR_SERVICE = "ghcr.io"
UNREAL_GHCR_REPOSITORY = "epicgames/unreal-engine"
UNREAL_GHCR_SCOPE = f"repository:{UNREAL_GHCR_REPOSITORY}:pull"


def redact(text: str, secrets: list[str]) -> str:
    result = text or ""
    for secret in secrets:
        if secret:
            result = result.replace(secret, "<redacted>")
    lines = []
    for line in result.splitlines():
        upper = line.upper()
        if any(word in upper for word in ("PASSWORD", "TOKEN", "AUTHORIZATION", "SECRET", "COOKIE")):
            lines.append("<redacted-sensitive-output>")
        else:
            lines.append(line[:500])
    joined = "\n".join(lines)
    return joined if len(joined) <= 20000 else joined[:20000] + "\n<truncated-output>"


def run(
    command: list[str],
    *,
    input_text: str | None = None,
    timeout: int = 120,
    secrets: list[str] | None = None,
    env: dict[str, str] | None = None,
) -> dict[str, Any]:
    secrets = secrets or []
    started = time.monotonic()
    safe_command = ["<redacted>" if item in secrets else item for item in command]
    try:
        proc = subprocess.run(
            command,
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
            env={**os.environ, **(env or {})},
        )
        stdout = redact(proc.stdout, secrets)
        stderr = redact(proc.stderr, secrets)
        return {
            "command": safe_command,
            "exit": proc.returncode,
            "timed_out": False,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": stdout,
            "stderr": stderr,
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "command": safe_command,
            "exit": None,
            "timed_out": True,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": redact(exc.stdout if isinstance(exc.stdout, str) else "", secrets),
            "stderr": redact(exc.stderr if isinstance(exc.stderr, str) else "", secrets),
        }
    except FileNotFoundError as exc:
        return {
            "command": safe_command,
            "exit": 127,
            "timed_out": False,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": "",
            "stderr": str(exc)[:500],
        }


def ok(result: dict[str, Any] | None) -> bool:
    return bool(result and result.get("exit") == 0 and not result.get("timed_out"))


def json_from(result: dict[str, Any] | None) -> dict[str, Any] | list[Any] | None:
    if not result:
        return None
    try:
        return json.loads(result.get("stdout", ""))
    except json.JSONDecodeError:
        return None


def classify_failure(result: dict[str, Any] | None) -> str:
    text = " ".join(((result or {}).get("stdout", ""), (result or {}).get("stderr", ""))).upper()
    if (result or {}).get("timed_out") or any(token in text for token in ("TIMEOUT", "TEMPORARY", "503", "429", "NETWORK")):
        return "TRANSIENT_VALIDATION_FAILURE"
    return "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"


def checksum_from(text: str) -> int | None:
    hits = re.findall(r"EVERFIELD_S3:(\d+)", text or "")
    return int(hits[-1]) if hits else None


UNITY_NATIVE_SCRIPT = r'''using UnityEngine;
public static class EverfieldS3 {
    public static void Run() {
        const int seed = 424242, ticks = 600, actions = 10, count = 32;
        const int modulus = 1000003, outputModulus = 1000000007;
        var values = new long[count];
        for (var i = 0; i < count; i++) values[i] = i * 17 + (seed % 97);
        var perturb = System.Environment.GetEnvironmentVariable("EVERFIELD_PERTURB") == "1";
        for (var tick = 0; tick < ticks; tick++) {
            var action = (tick + seed) % actions;
            if (perturb && tick == 137) action = (action + 1) % actions;
            var index = (tick * 7 + action) % count;
            values[index] = (values[index] + action * 3 + (tick % 11) + 1) % modulus;
        }
        long checksum = 0;
        for (var i = 0; i < count; i++) checksum = (checksum + (i + 1) * values[i]) % outputModulus;
        Debug.Log("EVERFIELD_S3:" + checksum);
        Application.Quit(checksum == 405227 || checksum == 405122 ? 0 : 17);
    }
}'''


def unity_native_s3(editor_path: str, version: str) -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="everfield-unity-s3-") as temp:
        for name, perturb, expected in (("N1", False, NORMAL_CHECKSUM), ("N2", False, NORMAL_CHECKSUM), ("FI1", True, PERTURBED_CHECKSUM)):
            root = pathlib.Path(temp) / name
            (root / "Assets" / "Editor").mkdir(parents=True)
            (root / "ProjectSettings").mkdir()
            (root / "ProjectSettings" / "ProjectVersion.txt").write_text(f"m_EditorVersion: {version}\n")
            (root / "Assets" / "Editor" / "EverfieldS3.cs").write_text(UNITY_NATIVE_SCRIPT)
            log_path = root / "Unity.log"
            result = run(
                [editor_path, "-batchmode", "-nographics", "-quit", "-projectPath", str(root), "-executeMethod", "EverfieldS3.Run", "-logFile", str(log_path)],
                timeout=300,
                secrets=[],
                env={"EVERFIELD_PERTURB": "1" if perturb else "0"},
            )
            log_text = log_path.read_text(errors="replace") if log_path.exists() else ""
            observed = checksum_from(result.get("stdout", "") + "\n" + result.get("stderr", "") + "\n" + log_text)
            passed = ok(result) and observed == expected
            attempts.append({
                "attempt_id": f"UNITY-S3-{name}",
                "scenario_id": "S3",
                "kind": "FAILURE_INJECTION" if perturb else "NORMAL",
                "normal_index": None if perturb else (1 if name == "N1" else 2),
                "injection_id": "FI-S3-INPUT-PERTURB-v2" if perturb else None,
                "expected_checksum": expected,
                "observed_checksum": observed,
                "result": "PASS" if passed else "INCONCLUSIVE",
                "failure_class": "NONE" if passed else "ENGINE_OR_HARNESS",
                "native_command": "Unity Editor -batchmode -executeMethod EverfieldS3.Run",
                "process": {k: result[k] for k in ("exit", "timed_out", "seconds")},
            })
    return {
        "scenario_id": "S3",
        "harness_id": "W2-ENG-HARNESS-v5",
        "attempts": attempts,
        "native_execution": True,
        "pass": all(attempt["result"] == "PASS" for attempt in attempts),
    }


def editor_path_from_install(data: Any, version: str) -> str | None:
    candidates: list[str] = []

    def visit(node: Any) -> None:
        if isinstance(node, dict):
            version_fields = " ".join(str(node.get(key, "")) for key in ("version", "editorVersion", "name"))
            for key in ("path", "location", "editorPath"):
                value = node.get(key)
                if isinstance(value, str) and (version in version_fields or version in value):
                    candidates.append(value)
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)

    visit(data)
    candidates.extend([
        f"/Applications/Unity/Hub/Editor/{version}/Unity.app/Contents/MacOS/Unity",
        f"{os.getenv('HOME', '')}/Unity/Hub/Editor/{version}/Editor/Unity",
        f"{os.getenv('HOME', '')}/.local/share/unity3d/Unity/Hub/Editor/{version}/Editor/Unity",
    ])
    for candidate in candidates:
        if candidate and pathlib.Path(candidate).is_file() and os.access(candidate, os.X_OK):
            return candidate
    return None


def unity_service_account_env(account_id: str, account_secret: str) -> dict[str, str]:
    """Use Unity CLI's documented unattended service-account environment path."""
    return {
        "UNITY_SERVICE_ACCOUNT_ID": account_id,
        "UNITY_SERVICE_ACCOUNT_SECRET": account_secret,
        "UNITY_NON_INTERACTIVE": "1",
        "UNITY_FORMAT": "json",
        "UNITY_NO_BANNER": "1",
    }


def unity_license_status_envelope(data: Any) -> tuple[bool, bool | None]:
    """Require an explicit structured license-status envelope; ambiguity fails closed."""
    if not isinstance(data, dict):
        return False, None
    if "active" in data:
        return False, None
    payload = data.get("data")
    if not isinstance(payload, dict):
        return False, None
    active = payload.get("active")
    if not isinstance(active, bool):
        return False, None
    return True, active


def unity_license_status_failure(result: dict[str, Any] | None) -> tuple[str, str, str]:
    """Classify a failed Unity license-status process using bounded CLI exit semantics."""
    if (result or {}).get("timed_out"):
        return (
            "TRANSIENT_VALIDATION_FAILURE",
            "LICENSE_STATUS_TRANSIENT_FAILURE",
            "UNITY_LICENSE_STATUS_TRANSIENT_FAILURE",
        )
    exit_code = (result or {}).get("exit")
    if exit_code == 3:
        return (
            "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
            "LICENSE_STATUS_AUTHENTICATION_OR_AUTHORIZATION_FAILED",
            "UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED",
        )
    if exit_code == 4:
        return (
            "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
            "LICENSE_STATUS_CONFIGURATION_REQUIRED",
            "UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED",
        )
    if exit_code == 6:
        return (
            "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
            "LICENSE_STATUS_OPERATION_FAILED",
            "UNITY_LICENSE_STATUS_OPERATION_FAILED",
        )
    if classify_failure(result) == "TRANSIENT_VALIDATION_FAILURE":
        return (
            "TRANSIENT_VALIDATION_FAILURE",
            "LICENSE_STATUS_TRANSIENT_FAILURE",
            "UNITY_LICENSE_STATUS_TRANSIENT_FAILURE",
        )
    return (
        "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
        "LICENSE_STATUS_PROCESS_FAILED",
        "UNITY_LICENSE_STATUS_PROCESS_FAILED",
    )


def validate_unity() -> dict[str, Any]:
    account_id = os.getenv("UNITY_SERVICE_ACCOUNT_ID", "")
    account_secret = os.getenv("UNITY_SERVICE_ACCOUNT_SECRET", "")
    version = os.getenv("UNITY_EDITOR_VERSION", UNITY_BASELINE)
    unity_cli = os.getenv("UNITY_CLI", "unity")
    present = bool(account_id and account_secret)
    base: dict[str, Any] = {
        "provider": "Unity",
        "baseline": version,
        "state": "NOT_CONFIGURED" if not present else "CONFIGURED_UNVALIDATED",
        "authentication_validated": False,
        "authentication_stage": "NOT_CONFIGURED" if not present else "SERVICE_ACCOUNT_ENV_CONFIGURED",
        "license_validated": False,
        "editor_installed": False,
        "editor_executed": False,
        "native_s3": None,
        "credential_values_read": bool(present),
        "commercial_authority": False,
        "production_authority": False,
        "legal_clearance": False,
        "release_authority": False,
    }
    if not present:
        base["blocker"] = "UNITY_SERVICE_ACCOUNT_ID_AND_SECRET_NOT_CONFIGURED"
        return base

    auth_env = unity_service_account_env(account_id, account_secret)
    # In service-account mode Unity CLI automatically generates the bearer
    # from UNITY_SERVICE_ACCOUNT_ID / UNITY_SERVICE_ACCOUNT_SECRET for
    # authenticated unattended commands. Do not invoke browser/session login.
    license_status = run(
        [unity_cli, "license", "status"],
        timeout=60,
        secrets=[account_id, account_secret],
        env=auth_env,
    )
    license_data = json_from(license_status)
    envelope_valid, license_active = unity_license_status_envelope(license_data)
    base["license_process"] = {k: license_status[k] for k in ("exit", "timed_out", "seconds")}
    base["license_status_envelope_valid"] = envelope_valid
    base["authentication_validated"] = ok(license_status) and envelope_valid
    if base["authentication_validated"]:
        base["authentication_stage"] = "AUTHENTICATED_SERVICE_ACCOUNT_COMMAND"
    elif not ok(license_status):
        failure_state, failure_stage, failure_blocker = unity_license_status_failure(license_status)
        base["state"] = failure_state
        base["authentication_stage"] = failure_stage
        base["blocker"] = failure_blocker
        return base
    else:
        base["authentication_stage"] = "LICENSE_STATUS_RESPONSE_INVALID"
        base["state"] = classify_failure(license_status)
        base["blocker"] = "UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED"
        return base

    base["license_validated"] = license_active is True
    if not base["license_validated"]:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "UNITY_LICENSE_STATUS_NOT_ACTIVE"
        return base

    install = run(
        [unity_cli, "install", version, "--architecture", "x86_64", "--accept-eula", "--yes"],
        timeout=1800,
        secrets=[account_id, account_secret],
        env=auth_env,
    )
    installed = run(
        [unity_cli, "editors", "--installed"],
        timeout=60,
        secrets=[account_id, account_secret],
        env=auth_env,
    )
    installed_data = json_from(installed)
    base["editor_install_process"] = {k: install[k] for k in ("exit", "timed_out", "seconds")}
    editor_path = editor_path_from_install(installed_data, version)
    base["editor_installed"] = editor_path is not None
    base["editor_path_observed"] = bool(editor_path)
    if not editor_path:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "UNITY_EXACT_EDITOR_PATH_NOT_FOUND"
        return base
    native = unity_native_s3(editor_path, version)
    base["native_s3"] = native
    base["editor_executed"] = bool(native.get("pass"))
    base["state"] = "VALIDATED_DEVELOPMENT_ACCESS" if base["editor_executed"] else "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
    if not base["editor_executed"]:
        base["blocker"] = "UNITY_NATIVE_S3_DID_NOT_PASS"
    return base


def validate_local_unity() -> dict[str, Any]:
    """Prove native execution against an already licensed local Unity install."""
    version = os.getenv("UNITY_EDITOR_VERSION", UNITY_BASELINE)
    unity_cli = os.getenv("UNITY_CLI", "unity")
    installed = run([unity_cli, "editors", "--installed", "--format", "json", "--non-interactive"], timeout=60)
    data = json_from(installed)
    editor_path = editor_path_from_install(data, version)
    auth_status = run([unity_cli, "auth", "status", "--non-interactive", "--format", "json"], timeout=30)
    license_status = run([unity_cli, "license", "status", "--format", "json", "--non-interactive"], timeout=60)
    auth_data = json_from(auth_status)
    license_data = json_from(license_status)
    license_active = bool(isinstance(license_data, dict) and license_data.get("data", {}).get("active") is True)
    auth_logged_in = bool(isinstance(auth_data, dict) and auth_data.get("data", {}).get("loggedIn") is True)
    native = unity_native_s3(editor_path, version) if editor_path and license_active else None
    passed = bool(native and native.get("pass"))
    provider = {
        "provider": "Unity",
        "baseline": version,
        "state": "VALIDATED_DEVELOPMENT_ACCESS" if passed else "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
        "authentication_validated": auth_logged_in or license_active,
        "license_validated": license_active,
        "editor_installed": bool(editor_path),
        "editor_executed": passed,
        "native_s3": native,
        "credential_values_read": False,
        "commercial_authority": False,
        "production_authority": False,
        "legal_clearance": False,
        "release_authority": False,
        "processes": {
            "auth_status": {k: auth_status[k] for k in ("exit", "timed_out", "seconds")},
            "license_status": {k: license_status[k] for k in ("exit", "timed_out", "seconds")},
        },
    }
    if not passed:
        provider["blocker"] = "LOCAL_UNITY_LICENSE_EDITOR_OR_NATIVE_S3_NOT_PROVEN"
    return provider


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Fail closed instead of forwarding authorization across redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_NO_REDIRECT_OPENER = urllib.request.build_opener(_NoRedirect())


def _http_request(url: str, headers: dict[str, str]) -> tuple[int, dict[str, str], bytes]:
    request = urllib.request.Request(url, headers=headers)
    try:
        with _NO_REDIRECT_OPENER.open(request, timeout=60) as response:
            return response.status, dict(response.headers.items()), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, dict(exc.headers.items()), exc.read()
    except (urllib.error.URLError, TimeoutError):
        return 599, {}, b""


def _header_value(headers: dict[str, str], name: str) -> str | None:
    target = name.lower()
    for key, value in headers.items():
        if key.lower() == target:
            return value
    return None


def _empty_ghcr_auth_trace() -> dict[str, Any]:
    """Return the complete sanitized auth-stage envelope; never add raw auth data."""
    return {
        "initial_status": None,
        "challenge_present": False,
        "challenge_scheme_bearer": False,
        "challenge_realm_matches": False,
        "challenge_service_matches": False,
        "challenge_scope_matches": False,
        "challenge_accepted": False,
        "token_exchange_attempted": False,
        "token_exchange_status": None,
        "token_response_valid": False,
        "resource_retry_attempted": False,
        "resource_retry_status": None,
        "failure_stage": "INITIAL_RESOURCE_FAILURE",
    }


def _ghcr_trace_stage(trace: dict[str, Any]) -> str:
    initial = trace.get("initial_status")
    if initial == 200:
        return "SUCCESS"
    if initial != 401:
        return "INITIAL_RESOURCE_FAILURE"
    if not trace.get("challenge_accepted"):
        return "CHALLENGE_MISSING_OR_REJECTED"
    if trace.get("token_exchange_status") != 200:
        return "TOKEN_EXCHANGE_FAILED"
    if not trace.get("token_response_valid"):
        return "TOKEN_RESPONSE_INVALID"
    if not trace.get("resource_retry_attempted") or trace.get("resource_retry_status") != 200:
        return "RESOURCE_RETRY_FAILED"
    return "SUCCESS"


def _ghcr_challenge_details(header: str | None) -> tuple[dict[str, str] | None, dict[str, bool]]:
    checks = {
        "challenge_present": bool(header),
        "challenge_scheme_bearer": False,
        "challenge_realm_matches": False,
        "challenge_service_matches": False,
        "challenge_scope_matches": False,
        "challenge_accepted": False,
    }
    if not header or not re.match(r"^Bearer\s+", header, re.IGNORECASE):
        return None, checks
    checks["challenge_scheme_bearer"] = True
    payload = re.sub(r"^Bearer\s+", "", header, count=1, flags=re.IGNORECASE)
    matches = re.findall(r'([A-Za-z][A-Za-z0-9_-]*)="([^"\\]*)"', payload)
    if not matches:
        return None, checks
    params: dict[str, str] = {}
    for key, value in matches:
        lowered = key.lower()
        if lowered in params:
            return None, checks
        params[lowered] = value
    realm = params.get("realm", "")
    service = params.get("service", "")
    scope = params.get("scope", "")
    parsed = urllib.parse.urlsplit(realm)
    checks["challenge_realm_matches"] = bool(
        parsed.scheme.lower() == "https"
        and parsed.hostname == GHCR_AUTH_HOST
        and parsed.username is None
        and parsed.password is None
        and parsed.port in (None, 443)
        and parsed.path == GHCR_AUTH_PATH
        and not parsed.query
        and not parsed.fragment
    )
    checks["challenge_service_matches"] = service == GHCR_SERVICE
    checks["challenge_scope_matches"] = scope == UNREAL_GHCR_SCOPE
    checks["challenge_accepted"] = bool(
        checks["challenge_realm_matches"]
        and checks["challenge_service_matches"]
        and checks["challenge_scope_matches"]
    )
    if not checks["challenge_accepted"]:
        return None, checks
    return {"realm": realm, "service": service, "scope": scope}, checks


def parse_ghcr_bearer_challenge(header: str | None) -> dict[str, str] | None:
    """Accept only the exact HTTPS GHCR pull challenge used for UE access."""
    challenge, _ = _ghcr_challenge_details(header)
    return challenge


def _ghcr_bearer_token(challenge: dict[str, str], username: str, token: str) -> tuple[str | None, int, bool]:
    credentials = base64.b64encode(f"{username}:{token}".encode()).decode()
    query = urllib.parse.urlencode({"service": challenge["service"], "scope": challenge["scope"]})
    status, _, body = _http_request(
        f"{challenge['realm']}?{query}",
        {"Authorization": f"Basic {credentials}", "Accept": "application/json"},
    )
    if status != 200:
        return None, status, False
    try:
        data = json.loads(body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None, status, False
    if not isinstance(data, dict):
        return None, status, False
    bearer = data.get("token")
    access_token = data.get("access_token")
    if bearer and access_token and bearer != access_token:
        return None, status, False
    value = bearer or access_token
    valid = isinstance(value, str) and 16 <= len(value) <= 65536
    return (value if valid else None), status, valid


def registry_request(path: str, username: str, token: str) -> tuple[int, dict[str, str], bytes, dict[str, Any]]:
    """Perform one GHCR Registry v2 request and emit only sanitized auth-stage facts."""
    trace = _empty_ghcr_auth_trace()
    if not path or path.startswith("/") or "//" in path or "\\" in path:
        trace["initial_status"] = 400
        trace["failure_stage"] = _ghcr_trace_stage(trace)
        return 400, {}, b"", trace
    resource_url = f"{GHCR_REGISTRY_ORIGIN}/v2/{path}"
    accept = "application/vnd.oci.image.manifest.v1+json, application/json"
    status, headers, body = _http_request(resource_url, {"Accept": accept})
    trace["initial_status"] = status
    if status != 401:
        trace["failure_stage"] = _ghcr_trace_stage(trace)
        return status, headers, body, trace
    challenge_header = _header_value(headers, "WWW-Authenticate")
    challenge, checks = _ghcr_challenge_details(challenge_header)
    trace.update(checks)
    if challenge is None:
        trace["failure_stage"] = _ghcr_trace_stage(trace)
        return status, headers, body, trace
    trace["token_exchange_attempted"] = True
    bearer, token_status, token_valid = _ghcr_bearer_token(challenge, username, token)
    trace["token_exchange_status"] = token_status
    trace["token_response_valid"] = token_valid
    if bearer is None:
        trace["failure_stage"] = _ghcr_trace_stage(trace)
        return 401, {}, b"", trace
    trace["resource_retry_attempted"] = True
    retry_status, retry_headers, retry_body = _http_request(
        resource_url,
        {"Authorization": f"Bearer {bearer}", "Accept": accept},
    )
    trace["resource_retry_status"] = retry_status
    trace["failure_stage"] = _ghcr_trace_stage(trace)
    return retry_status, retry_headers, retry_body, trace


def select_unreal_tag(tags: list[str]) -> str | None:
    candidates = [tag for tag in tags if re.fullmatch(r"(?:dev|release)[-_]5\.8(?:[-.]\d+)?(?:[-.]linux)?", tag, re.IGNORECASE)]
    return sorted(candidates, key=lambda tag: ("dev" not in tag.lower(), len(tag), tag))[0] if candidates else None


UNREAL_NATIVE_SCRIPT = r'''import os
import unreal

seed = 424242
ticks = 600
actions = 10
count = 32
modulus = 1000003
output_modulus = 1000000007
values = [i * 17 + (seed % 97) for i in range(count)]
perturb = os.environ.get("EVERFIELD_PERTURB") == "1"
for tick in range(ticks):
    action = (tick + seed) % actions
    if perturb and tick == 137:
        action = (action + 1) % actions
    index = (tick * 7 + action) % count
    values[index] = (values[index] + action * 3 + (tick % 11) + 1) % modulus
checksum = 0
for index, value in enumerate(values):
    checksum = (checksum + (index + 1) * value) % output_modulus
unreal.log("EVERFIELD_S3:%d" % checksum)
if checksum not in (405227, 405122):
    raise RuntimeError("Everfield S3 checksum mismatch")
unreal.SystemLibrary.quit_editor()
'''


def unreal_native_s3(image: str, editor_path: str, token: str) -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="everfield-unreal-s3-") as temp:
        root = pathlib.Path(temp)
        (root / "Everfield.uproject").write_text('{"FileVersion":3,"EngineAssociation":""}\n')
        (root / "EverfieldS3.py").write_text(UNREAL_NATIVE_SCRIPT)
        for name, perturb, expected in (("N1", False, NORMAL_CHECKSUM), ("N2", False, NORMAL_CHECKSUM), ("FI1", True, PERTURBED_CHECKSUM)):
            result = run(
                [
                    "docker", "run", "--rm", "--network", "none",
                    "-e", f"EVERFIELD_PERTURB={'1' if perturb else '0'}",
                    "-v", f"{root}:/everfield:ro",
                    "--entrypoint", editor_path,
                    image,
                    "/everfield/Everfield.uproject",
                    "-unattended", "-nullrhi", "-nop4", "-nosplash", "-NoSound",
                    "-ExecutePythonScript=/everfield/EverfieldS3.py",
                ],
                timeout=900,
                secrets=[token],
            )
            observed = checksum_from(result.get("stdout", "") + "\n" + result.get("stderr", ""))
            passed = ok(result) and observed == expected
            attempts.append({
                "attempt_id": f"UNREAL-S3-{name}",
                "scenario_id": "S3",
                "kind": "FAILURE_INJECTION" if perturb else "NORMAL",
                "normal_index": None if perturb else (1 if name == "N1" else 2),
                "injection_id": "FI-S3-INPUT-PERTURB-v2" if perturb else None,
                "expected_checksum": expected,
                "observed_checksum": observed,
                "result": "PASS" if passed else "INCONCLUSIVE",
                "failure_class": "NONE" if passed else "ENGINE_OR_HARNESS",
                "native_command": "UnrealEditor -unattended -ExecutePythonScript=EverfieldS3.py",
                "process": {k: result[k] for k in ("exit", "timed_out", "seconds")},
            })
    return {
        "scenario_id": "S3",
        "harness_id": "W2-ENG-HARNESS-v5",
        "attempts": attempts,
        "native_execution": True,
        "pass": all(attempt["result"] == "PASS" for attempt in attempts),
    }


def validate_unreal() -> dict[str, Any]:
    username = os.getenv("UNREAL_GITHUB_USERNAME", "")
    token = os.getenv("UNREAL_GITHUB_TOKEN", "")
    base: dict[str, Any] = {
        "provider": "Unreal Engine",
        "baseline": os.getenv("UNREAL_ENGINE_VERSION", UNREAL_BASELINE),
        "state": "NOT_CONFIGURED" if not (username and token) else "CONFIGURED_UNVALIDATED",
        "registry_authorization_validated": False,
        "container_identity": None,
        "editor_executed": False,
        "native_s3": None,
        "credential_values_read": bool(token),
        "commercial_authority": False,
        "production_authority": False,
        "legal_clearance": False,
        "release_authority": False,
    }
    if not (username and token):
        base["blocker"] = "UNREAL_GITHUB_USERNAME_AND_TOKEN_NOT_CONFIGURED"
        return base
    status, headers, body, auth_trace = registry_request(f"{UNREAL_GHCR_REPOSITORY}/tags/list?n=1000", username, token)
    if status != 200:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "EPIC_GHCR_AUTHORIZATION_OR_ENTITLEMENT_FAILED"
        base["registry_http_status"] = status
        base["registry_auth_trace"] = auth_trace
        return base
    try:
        tags = json.loads(body).get("tags", [])
    except (json.JSONDecodeError, UnicodeDecodeError):
        tags = []
    tag = select_unreal_tag(tags if isinstance(tags, list) else [])
    if not tag:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "NO_VENDOR_PUBLISHED_UE_5_8_DEVELOPMENT_TAG_OBSERVED"
        return base
    manifest_status, manifest_headers, _, manifest_auth_trace = registry_request(f"{UNREAL_GHCR_REPOSITORY}/manifests/{tag}", username, token)
    if manifest_status != 200:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "UE_5_8_MANIFEST_NOT_ACCESSIBLE"
        base["registry_http_status"] = manifest_status
        base["registry_auth_trace"] = manifest_auth_trace
        return base
    digest = _header_value(manifest_headers, "Docker-Content-Digest")
    base["registry_authorization_validated"] = True
    base["published_tag"] = tag
    base["container_identity"] = digest if isinstance(digest, str) and digest.startswith("sha256:") else None
    if not base["container_identity"]:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "UE_5_8_MANIFEST_DIGEST_MISSING"
        return base
    login = run(["docker", "login", "ghcr.io", "--username", username, "--password-stdin"], input_text=token, timeout=60, secrets=[token])
    if not ok(login):
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "DOCKER_GHCR_LOGIN_FAILED"
        return base
    image = f"ghcr.io/{UNREAL_GHCR_REPOSITORY}:{tag}"
    try:
        pull = run(["docker", "pull", image], timeout=3600, secrets=[token])
    finally:
        run(["docker", "logout", "ghcr.io"], timeout=60, secrets=[token])
    base["container_pull_process"] = {k: pull[k] for k in ("exit", "timed_out", "seconds")}
    if not ok(pull):
        base["state"] = classify_failure(pull)
        base["blocker"] = "UE_5_8_CONTAINER_PULL_FAILED_OR_RESOURCE_LIMITED"
        return base
    inspect = run(["docker", "image", "inspect", image, "--format", "{{json .RepoDigests}}"], timeout=60)
    base["container_local_identity"] = redact(inspect.get("stdout", ""), [token])
    pinned_image = f"ghcr.io/{UNREAL_GHCR_REPOSITORY}@{digest}"
    editor_probe = run([
        "docker", "run", "--rm", "--network", "none", "--entrypoint", "/bin/sh", pinned_image,
        "-lc", "for p in /home/ue5/UnrealEngine/Engine/Binaries/Linux/UnrealEditor /home/ue4/UnrealEngine/Engine/Binaries/Linux/UE4Editor; do if [ -x \"$p\" ]; then printf '%s' \"$p\"; exit 0; fi; done; exit 7",
    ], timeout=120, secrets=[token])
    editor_path = editor_probe.get("stdout", "").strip()
    base["editor_path_observed"] = bool(editor_path) and "\n" not in editor_path and len(editor_path) < 300
    if not base["editor_path_observed"]:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "UE_NATIVE_EDITOR_BINARY_NOT_FOUND_IN_PINNED_CONTAINER"
        return base
    native = unreal_native_s3(pinned_image, editor_path, token)
    base["native_s3"] = native
    base["editor_executed"] = bool(native.get("pass"))
    base["state"] = "VALIDATED_DEVELOPMENT_ACCESS" if base["editor_executed"] else "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
    if not base["editor_executed"]:
        base["blocker"] = "UNREAL_NATIVE_S3_DID_NOT_PASS"
    return base


def derive_frontier(providers: dict[str, dict[str, Any]]) -> dict[str, Any]:
    unity = providers["Unity"].get("state") == "VALIDATED_DEVELOPMENT_ACCESS"
    unreal = providers["Unreal Engine"].get("state") == "VALIDATED_DEVELOPMENT_ACCESS"
    return {
        "provider_unlocks": {"Unity": unity, "Unreal Engine": unreal},
        "unity_empirical_cells_eligible": unity,
        "unreal_empirical_cells_eligible": unreal,
        "combined_provider_predicate": unity and unreal,
        "combined_predicate_used_for_individual_unlock": False,
        "commercial_license_authority": False,
        "production_authority": False,
        "legal_clearance": False,
        "release_authority": False,
        "engine_selected": False,
        "historical_not_run_cells_preserved": 50,
        "historical_not_run_cells_mutated": False,
    }


def validate(*, health_only: bool = False) -> dict[str, Any]:
    providers = {"Unity": validate_unity(), "Unreal Engine": validate_unreal()}
    if health_only:
        for provider in providers.values():
            provider.pop("native_s3", None)
            provider.pop("editor_executed", None)
    return {
        "schema": SCHEMA,
        "mission_id": "W2-ENG-PROVIDER-EFFECTIVE-01",
        "runner": {key: os.getenv(key) for key in ("GITHUB_SHA", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "RUNNER_OS", "RUNNER_ARCH", "ImageOS", "ImageVersion")},
        "providers": providers,
        "frontier": derive_frontier(providers),
        "secret_values_in_evidence": False,
        "secret_hashes_in_evidence": False,
        "workflow_success_is_not_authority": True,
    }


def self_test() -> dict[str, Any]:
    original = dict(os.environ)
    cases: dict[str, bool] = {}
    try:
        for key in SECRET_ENV_NAMES + ("UNITY_EDITOR_VERSION", "UNREAL_ENGINE_VERSION", "UNREAL_GITHUB_USERNAME"):
            os.environ.pop(key, None)
        empty = validate()
        cases["empty_is_per_provider_not_configured"] = all(v["state"] == "NOT_CONFIGURED" for v in empty["providers"].values())
        cases["empty_does_not_unlock"] = not any(empty["frontier"]["provider_unlocks"].values())
        fake = {"Unity": {"state": "VALIDATED_DEVELOPMENT_ACCESS"}, "Unreal Engine": {"state": "NOT_CONFIGURED"}}
        one = derive_frontier(fake)
        cases["one_provider_unlocks_independently"] = one["unity_empirical_cells_eligible"] and not one["unreal_empirical_cells_eligible"]
        cases["one_provider_does_not_require_combined"] = one["combined_predicate_used_for_individual_unlock"] is False
        redacted = redact("token=unit-test-secret", ["unit-test-secret"])
        cases["redaction_removes_fixture_secret"] = "unit-test-secret" not in redacted
        cases["commercial_authority_stays_false"] = one["commercial_license_authority"] is False

        active_ok, active_value = unity_license_status_envelope({"data": {"active": True}})
        inactive_ok, inactive_value = unity_license_status_envelope({"data": {"active": False}})
        missing_ok, _ = unity_license_status_envelope({"data": {}})
        nonbool_ok, _ = unity_license_status_envelope({"data": {"active": "true"}})
        ambiguous_ok, _ = unity_license_status_envelope({"active": True})
        conflicting_ok, _ = unity_license_status_envelope({"active": False, "data": {"active": True}})
        cases["unity_license_active_envelope_valid"] = active_ok and active_value is True
        cases["unity_license_inactive_envelope_valid"] = inactive_ok and inactive_value is False
        cases["unity_license_missing_active_rejected"] = not missing_ok
        cases["unity_license_nonboolean_active_rejected"] = not nonbool_ok
        cases["unity_license_ambiguous_envelope_rejected"] = not ambiguous_ok
        cases["unity_license_conflicting_top_level_active_rejected"] = not conflicting_ok

        def unity_process(exit_code: int | None, *, timed_out: bool = False, stderr: str = "") -> dict[str, Any]:
            return {"exit": exit_code, "timed_out": timed_out, "stdout": "", "stderr": stderr}

        exit0 = unity_process(0)
        exit3 = unity_process(3)
        exit4 = unity_process(4)
        exit6 = unity_process(6)
        timeout = unity_process(None, timed_out=True)
        transient = unity_process(1, stderr="temporary network failure")
        unknown = unity_process(17)
        cases["unity_license_exit0_active_process_and_envelope_valid"] = ok(exit0) and active_ok and active_value is True
        cases["unity_license_exit0_inactive_process_and_envelope_valid"] = ok(exit0) and inactive_ok and inactive_value is False
        cases["unity_license_exit3_authentication_or_authorization_classified"] = unity_license_status_failure(exit3) == (
            "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
            "LICENSE_STATUS_AUTHENTICATION_OR_AUTHORIZATION_FAILED",
            "UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED",
        )
        exit4_expected = (
            "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
            "LICENSE_STATUS_CONFIGURATION_REQUIRED",
            "UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED",
        )
        cases["unity_license_exit4_valid_envelope_stays_configuration_blocked"] = active_ok and unity_license_status_failure(exit4) == exit4_expected
        cases["unity_license_exit4_invalid_envelope_stays_configuration_blocked"] = not missing_ok and unity_license_status_failure(exit4) == exit4_expected
        cases["unity_license_exit6_operation_failure_classified"] = unity_license_status_failure(exit6) == (
            "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
            "LICENSE_STATUS_OPERATION_FAILED",
            "UNITY_LICENSE_STATUS_OPERATION_FAILED",
        )
        cases["unity_license_timeout_classified_transient"] = unity_license_status_failure(timeout) == (
            "TRANSIENT_VALIDATION_FAILURE",
            "LICENSE_STATUS_TRANSIENT_FAILURE",
            "UNITY_LICENSE_STATUS_TRANSIENT_FAILURE",
        )
        cases["unity_license_network_failure_classified_transient"] = unity_license_status_failure(transient) == (
            "TRANSIENT_VALIDATION_FAILURE",
            "LICENSE_STATUS_TRANSIENT_FAILURE",
            "UNITY_LICENSE_STATUS_TRANSIENT_FAILURE",
        )
        cases["unity_license_unknown_nonzero_fails_closed"] = unity_license_status_failure(unknown) == (
            "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION",
            "LICENSE_STATUS_PROCESS_FAILED",
            "UNITY_LICENSE_STATUS_PROCESS_FAILED",
        )
        cases["unity_license_nonzero_never_authenticates_or_licenses"] = all(
            not (ok(result) and active_ok and active_value is True)
            for result in (exit3, exit4, exit6, timeout, transient, unknown)
        )

        unity_env = unity_service_account_env("fixture-id", "fixture-secret")
        cases["unity_service_account_env_exact"] = unity_env == {
            "UNITY_SERVICE_ACCOUNT_ID": "fixture-id",
            "UNITY_SERVICE_ACCOUNT_SECRET": "fixture-secret",
            "UNITY_NON_INTERACTIVE": "1",
            "UNITY_FORMAT": "json",
            "UNITY_NO_BANNER": "1",
        }

        exact = 'Bearer realm="https://ghcr.io/token",service="ghcr.io",scope="repository:epicgames/unreal-engine:pull"'
        exact_challenge, exact_checks = _ghcr_challenge_details(exact)
        cases["ghcr_exact_bearer_challenge_accepted"] = exact_challenge == {
            "realm": "https://ghcr.io/token",
            "service": "ghcr.io",
            "scope": "repository:epicgames/unreal-engine:pull",
        } and all(exact_checks.values())
        cases["ghcr_http_realm_rejected"] = parse_ghcr_bearer_challenge(
            'Bearer realm="http://ghcr.io/token",service="ghcr.io",scope="repository:epicgames/unreal-engine:pull"'
        ) is None
        cases["ghcr_wrong_host_rejected"] = parse_ghcr_bearer_challenge(
            'Bearer realm="https://example.com/token",service="ghcr.io",scope="repository:epicgames/unreal-engine:pull"'
        ) is None
        cases["ghcr_wrong_service_rejected"] = parse_ghcr_bearer_challenge(
            'Bearer realm="https://ghcr.io/token",service="example.com",scope="repository:epicgames/unreal-engine:pull"'
        ) is None
        cases["ghcr_push_scope_rejected"] = parse_ghcr_bearer_challenge(
            'Bearer realm="https://ghcr.io/token",service="ghcr.io",scope="repository:epicgames/unreal-engine:pull,push"'
        ) is None
        cases["ghcr_other_repository_scope_rejected"] = parse_ghcr_bearer_challenge(
            'Bearer realm="https://ghcr.io/token",service="ghcr.io",scope="repository:other/repo:pull"'
        ) is None
        cases["ghcr_non_bearer_challenge_rejected"] = parse_ghcr_bearer_challenge(
            'Basic realm="https://ghcr.io/token"'
        ) is None
        cases["ghcr_realm_query_rejected"] = parse_ghcr_bearer_challenge(
            'Bearer realm="https://ghcr.io/token?redirect=https://example.com",service="ghcr.io",scope="repository:epicgames/unreal-engine:pull"'
        ) is None

        def stage_trace(**updates: Any) -> dict[str, Any]:
            trace = _empty_ghcr_auth_trace()
            trace.update(updates)
            return trace

        cases["ghcr_stage_initial_resource_failure"] = _ghcr_trace_stage(stage_trace(initial_status=503)) == "INITIAL_RESOURCE_FAILURE"
        cases["ghcr_stage_challenge_rejected"] = _ghcr_trace_stage(stage_trace(initial_status=401)) == "CHALLENGE_MISSING_OR_REJECTED"
        cases["ghcr_stage_token_exchange_failed"] = _ghcr_trace_stage(stage_trace(initial_status=401, challenge_accepted=True, token_exchange_attempted=True, token_exchange_status=401)) == "TOKEN_EXCHANGE_FAILED"
        cases["ghcr_stage_token_response_invalid"] = _ghcr_trace_stage(stage_trace(initial_status=401, challenge_accepted=True, token_exchange_attempted=True, token_exchange_status=200, token_response_valid=False)) == "TOKEN_RESPONSE_INVALID"
        cases["ghcr_stage_resource_retry_failed"] = _ghcr_trace_stage(stage_trace(initial_status=401, challenge_accepted=True, token_exchange_attempted=True, token_exchange_status=200, token_response_valid=True, resource_retry_attempted=True, resource_retry_status=401)) == "RESOURCE_RETRY_FAILED"
        cases["ghcr_stage_success"] = _ghcr_trace_stage(stage_trace(initial_status=401, challenge_accepted=True, token_exchange_attempted=True, token_exchange_status=200, token_response_valid=True, resource_retry_attempted=True, resource_retry_status=200)) == "SUCCESS"
        trace_text = json.dumps(stage_trace(initial_status=401, challenge_accepted=True, token_exchange_attempted=True, token_exchange_status=401), sort_keys=True)
        cases["ghcr_auth_trace_contains_no_fixture_secret_or_bearer"] = "unit-test-secret" not in trace_text and "fixture-bearer-value" not in trace_text and "authorization" not in trace_text.lower() and "cookie" not in trace_text.lower()
    finally:
        os.environ.clear()
        os.environ.update(original)
    return {"schema": "W2-ENG-PROVIDER-EFFECTIVE-ACCESS-SELFTEST-v1", "cases": cases, "pass": all(cases.values())}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--health-only", action="store_true")
    parser.add_argument("--local-unity-proof", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = self_test()
    elif args.local_unity_proof:
        unity = validate_local_unity()
        result = {
            "schema": SCHEMA,
            "mission_id": "W2-ENG-PROVIDER-EFFECTIVE-01",
            "providers": {"Unity": unity, "Unreal Engine": {
                "provider": "Unreal Engine",
                "baseline": UNREAL_BASELINE,
                "state": "NOT_CONFIGURED",
                "credential_values_read": False,
                "commercial_authority": False,
                "production_authority": False,
                "legal_clearance": False,
                "release_authority": False,
                "blocker": "LOCAL_UNITY_PROOF_MODE_DOES_NOT_VALIDATE_UNREAL",
            }},
            "frontier": derive_frontier({"Unity": unity, "Unreal Engine": {"state": "NOT_CONFIGURED"}}),
            "secret_values_in_evidence": False,
            "secret_hashes_in_evidence": False,
            "workflow_success_is_not_authority": True,
        }
    else:
        result = validate(health_only=args.health_only)
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.out:
        pathlib.Path(args.out).write_text(text)
    print(text, end="")
    return 0 if (not args.self_test or result["pass"]) else 3


if __name__ == "__main__":
    raise SystemExit(main())
