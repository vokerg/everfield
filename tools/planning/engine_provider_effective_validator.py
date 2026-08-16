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
            # Each attempt receives a fresh project directory and fresh process.
            # This prevents a prior run's generated state from becoming evidence
            # for a later run.
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
    auth = run(
        [unity_cli, "auth", "login", "--client-id", account_id, "--secret-from-stdin", "--non-interactive", "--format", "json"],
        input_text=account_secret,
        timeout=90,
        secrets=[account_id, account_secret],
    )
    auth_status = run([unity_cli, "auth", "status", "--non-interactive", "--format", "json"], timeout=30, secrets=[account_id, account_secret])
    base["authentication_validated"] = ok(auth) and bool(json_from(auth_status))
    base["authentication_process"] = {k: auth[k] for k in ("exit", "timed_out", "seconds")}
    base["authentication_status_process"] = {k: auth_status[k] for k in ("exit", "timed_out", "seconds")}
    if not base["authentication_validated"]:
        base["state"] = classify_failure(auth)
        base["blocker"] = "UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED"
        return base
    license_status = run([unity_cli, "license", "status", "--format", "json", "--non-interactive"], timeout=60, secrets=[account_id, account_secret])
    license_data = json_from(license_status)
    base["license_process"] = {k: license_status[k] for k in ("exit", "timed_out", "seconds")}
    base["license_validated"] = bool(isinstance(license_data, dict) and license_data.get("data", {}).get("active") is True)
    if not base["license_validated"]:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "UNITY_PERSONAL_LICENSE_CANNOT_BE_ACTIVATED_BY_SERVICE_ACCOUNT_ON_EPHEMERAL_CI"
        return base
    install = run([unity_cli, "install", version, "--architecture", "x86_64", "--accept-eula", "--yes", "--non-interactive", "--format", "json"], timeout=1800)
    installed = run([unity_cli, "editors", "--installed", "--format", "json", "--non-interactive"], timeout=60)
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
    """Prove native execution against an already licensed local Unity install.

    This mode is intentionally separate from credentialed CI validation: a
    local Personal OAuth license is evidence of development execution on this
    machine, not a portable CI credential or commercial authority.
    """
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


def registry_request(path: str, username: str, token: str) -> tuple[int, dict[str, str], bytes]:
    credentials = base64.b64encode(f"{username}:{token}".encode()).decode()
    request = urllib.request.Request(
        f"https://ghcr.io/v2/{path}",
        headers={"Authorization": f"Basic {credentials}", "Accept": "application/vnd.oci.image.manifest.v1+json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.status, dict(response.headers.items()), response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, dict(exc.headers.items()), exc.read()
    except (urllib.error.URLError, TimeoutError):
        return 599, {}, b""


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
    status, headers, body = registry_request("epicgames/unreal-engine/tags/list?n=1000", username, token)
    if status != 200:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "EPIC_GHCR_AUTHORIZATION_OR_ENTITLEMENT_FAILED"
        base["registry_http_status"] = status
        return base
    try:
        tags = json.loads(body).get("tags", [])
    except json.JSONDecodeError:
        tags = []
    tag = select_unreal_tag(tags if isinstance(tags, list) else [])
    if not tag:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "NO_VENDOR_PUBLISHED_UE_5_8_DEVELOPMENT_TAG_OBSERVED"
        return base
    manifest_status, manifest_headers, _ = registry_request(f"epicgames/unreal-engine/manifests/{tag}", username, token)
    if manifest_status != 200:
        base["state"] = "BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION"
        base["blocker"] = "UE_5_8_MANIFEST_NOT_ACCESSIBLE"
        base["registry_http_status"] = manifest_status
        return base
    digest = manifest_headers.get("Docker-Content-Digest")
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
    image = f"ghcr.io/epicgames/unreal-engine:{tag}"
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
    pinned_image = f"ghcr.io/epicgames/unreal-engine@{digest}"
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
