#!/usr/bin/env python3
"""Bounded W2-CI-ENABLE-01 capability probe.

This script establishes execution-environment capability only. It does not run,
score, rank, or select an engine and it never upgrades W2-ENG-03 NOT_RUN cells.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import platform
import shutil
import subprocess
import tempfile
import time
from typing import Any

SCHEMA = "W2-CI-ENGINE-TOOLCHAIN-CAPABILITY-v1"
CANDIDATES = {
    "Bevy": {"baseline": "0.19.0", "surface": "cargo/rustc + Bevy dependency materialization"},
    "Defold": {"baseline": "1.13.0", "surface": "Java + exact bob.jar"},
    "Godot": {"baseline": "4.7.1-stable", "surface": "Linux editor/headless executable"},
    "Unity": {"baseline": "6000.5.6f1", "surface": "Linux editor + unattended activation/account state"},
    "Unreal Engine": {"baseline": "5.8", "surface": "Linux editor/source package + Epic entitlement"},
}


def run(cmd: list[str], cwd: pathlib.Path | None = None, timeout: int = 180) -> dict[str, Any]:
    started = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=timeout, check=False)
        return {
            "cmd": cmd,
            "exit": p.returncode,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": p.stdout[-4000:],
            "stderr": p.stderr[-4000:],
            "timed_out": False,
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "cmd": cmd,
            "exit": None,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": (exc.stdout or "")[-4000:] if isinstance(exc.stdout, str) else "",
            "stderr": (exc.stderr or "")[-4000:] if isinstance(exc.stderr, str) else "",
            "timed_out": True,
        }
    except FileNotFoundError as exc:
        return {"cmd": cmd, "exit": 127, "seconds": 0, "stdout": "", "stderr": str(exc), "timed_out": False}


def ok(r: dict[str, Any]) -> bool:
    return r.get("exit") == 0 and not r.get("timed_out")


def command_version(name: str, args: list[str]) -> dict[str, Any]:
    path = shutil.which(name)
    if not path:
        return {"path": None, "probe": None}
    return {"path": path, "probe": run([path, *args], timeout=30)}


def head(url: str) -> dict[str, Any]:
    curl = shutil.which("curl")
    if not curl:
        return {"url": url, "probe": {"exit": 127, "stderr": "curl missing"}}
    return {"url": url, "probe": run([curl, "-fsSIL", "--max-time", "30", url], timeout=40)}


def probe_bevy(root: pathlib.Path) -> dict[str, Any]:
    rustc = command_version("rustc", ["--version"])
    cargo = command_version("cargo", ["--version"])
    if not cargo["path"] or not rustc["path"]:
        return {"status": "FAILED", "reason": "rustc_or_cargo_missing", "rustc": rustc, "cargo": cargo}
    d = root / "bevy-smoke"
    d.mkdir()
    (d / "src").mkdir()
    (d / "src" / "main.rs").write_text("fn main() { println!(\"bevy-ci-bootstrap\"); }\n")
    (d / "Cargo.toml").write_text(
        "[package]\nname='everfield_bevy_probe'\nversion='0.0.0'\nedition='2024'\n"
        "[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n"
    )
    fetch = run([cargo["path"], "fetch", "--locked"], cwd=d, timeout=240)
    # Cargo.lock does not exist on first resolution; retry without --locked, then
    # prove the materialized lock can be replayed exactly.
    if not ok(fetch):
        resolve = run([cargo["path"], "fetch"], cwd=d, timeout=300)
    else:
        resolve = fetch
    locked = run([cargo["path"], "fetch", "--locked"], cwd=d, timeout=240) if ok(resolve) else None
    check = run([cargo["path"], "check", "--locked", "--quiet"], cwd=d, timeout=420) if locked and ok(locked) else None
    capable = bool(check and ok(check))
    return {
        "status": "CAPABLE_WITH_PRESEED" if capable else "FAILED",
        "reason": "pinned_bevy_core_dependency_resolved_and_compiled; full graphics/package harness not executed" if capable else "pinned_bevy_dependency_bootstrap_failed",
        "rustc": rustc,
        "cargo": cargo,
        "initial_locked_fetch": fetch,
        "resolve_fetch": resolve,
        "replay_locked_fetch": locked,
        "cargo_check": check,
        "cargo_lock_present": (d / "Cargo.lock").exists(),
    }


def probe_defold(root: pathlib.Path) -> dict[str, Any]:
    java = command_version("java", ["-version"])
    curl = shutil.which("curl")
    url = "https://github.com/defold/defold/releases/download/1.13.0/bob.jar"
    if not java["path"] or not curl:
        return {"status": "FAILED", "reason": "java_or_curl_missing", "java": java, "url": url}
    jar = root / "bob-1.13.0.jar"
    dl = run([curl, "-fL", "--retry", "2", "--connect-timeout", "20", "-o", str(jar), url], timeout=240)
    version = run([java["path"], "-jar", str(jar), "--version"], timeout=120) if ok(dl) else None
    capable = bool(version and ok(version))
    return {
        "status": "CAPABLE" if capable else "FAILED",
        "reason": "exact_bob_jar_downloaded_and_executed" if capable else "bob_download_or_execution_failed",
        "java": java,
        "url": url,
        "download": dl,
        "bob_version": version,
        "bytes": jar.stat().st_size if jar.exists() else 0,
    }


def probe_godot(root: pathlib.Path) -> dict[str, Any]:
    curl = shutil.which("curl")
    unzip = shutil.which("unzip")
    url = "https://github.com/godotengine/godot/releases/download/4.7.1-stable/Godot_v4.7.1-stable_linux.x86_64.zip"
    if not curl or not unzip:
        return {"status": "FAILED", "reason": "curl_or_unzip_missing", "url": url}
    z = root / "godot-4.7.1.zip"
    out = root / "godot"
    out.mkdir()
    dl = run([curl, "-fL", "--retry", "2", "--connect-timeout", "20", "-o", str(z), url], timeout=300)
    uz = run([unzip, "-q", str(z), "-d", str(out)], timeout=120) if ok(dl) else None
    exe = None
    if uz and ok(uz):
        matches = sorted(p for p in out.iterdir() if p.is_file() and p.name.startswith("Godot_v4.7.1"))
        exe = matches[0] if matches else None
        if exe:
            exe.chmod(exe.stat().st_mode | 0o111)
    version = run([str(exe), "--headless", "--version"], timeout=60) if exe else None
    capable = bool(version and ok(version))
    return {
        "status": "CAPABLE" if capable else "FAILED",
        "reason": "exact_linux_editor_downloaded_and_headless_process_executed" if capable else "godot_download_or_headless_execution_failed",
        "url": url,
        "download": dl,
        "unzip": uz,
        "executable": str(exe) if exe else None,
        "version": version,
        "bytes": z.stat().st_size if z.exists() else 0,
    }


def probe_unity() -> dict[str, Any]:
    archive = head("https://unity.com/releases/editor/archive")
    hub = head("https://hub.unity3d.com/")
    # Deliberately do not consume credentials or activate a license in an
    # infrastructure probe. The downstream empirical episode must bind the
    # exact provider account/license state if one is supplied lawfully.
    return {
        "status": "BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY",
        "reason": "public_vendor_network_is_probeable_but_unattended_editor_activation/account_license_state_is_not_repository_self_grantable",
        "required_external_authority": "valid Unity unattended-use account/license/activation material for the exact editor baseline",
        "archive_network": archive,
        "hub_network": hub,
        "credential_values_read": False,
    }


def probe_unreal() -> dict[str, Any]:
    public = head("https://www.unrealengine.com/")
    source = head("https://github.com/EpicGames/UnrealEngine")
    return {
        "status": "BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY",
        "reason": "public_vendor_network_is_probeable_but_linux_engine_source/prebuilt_acquisition_requires_Epic-linked entitlement_or_preseeded_artifact",
        "required_external_authority": "Epic-authorized Unreal Engine 5.8 source/prebuilt artifact access suitable for unattended CI",
        "public_network": public,
        "source_entitlement_probe": source,
        "credential_values_read": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="everfield-ci-probe-") as td:
        root = pathlib.Path(td)
        result: dict[str, Any] = {
            "schema": SCHEMA,
            "mission_id": "W2-CI-ENABLE-01",
            "source_issue": 339,
            "source_main_sha": "92204cb2e58c792ef4199fe3562ca2192096f5c0",
            "canonical_program_blob": "e3120ec203c4156328770aa86c12fbb7187966dc",
            "engine_source_issue": 82,
            "engine_source_terminal_comment": 5276916603,
            "historical_not_run_cells_preserved": 50,
            "harness_id": "W2-ENG-HARNESS-v5",
            "feature_slice_id": "W2-ENG-FEATURE-SLICE-v2",
            "scenario_manifest_id": "W2-ENG-SCENARIO-INPUTS-v2",
            "engine_selection_authority": "NONE",
            "implementation_authority": "NONE",
            "runner": {
                "platform": platform.platform(),
                "machine": platform.machine(),
                "python": platform.python_version(),
                "image_os": os.getenv("ImageOS"),
                "image_version": os.getenv("ImageVersion"),
                "runner_os": os.getenv("RUNNER_OS"),
                "runner_arch": os.getenv("RUNNER_ARCH"),
                "github_sha": os.getenv("GITHUB_SHA"),
                "github_run_id": os.getenv("GITHUB_RUN_ID"),
                "github_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT"),
            },
            "common_prerequisites": {
                "git": command_version("git", ["--version"]),
                "python3": command_version("python3", ["--version"]),
                "curl": command_version("curl", ["--version"]),
                "unzip": command_version("unzip", ["-v"]),
                "xvfb-run": command_version("xvfb-run", ["--help"]),
                "ffmpeg": command_version("ffmpeg", ["-version"]),
                "disk": run(["df", "-h", "."], timeout=30),
                "memory": run(["bash", "-lc", "grep -E 'MemTotal|MemAvailable' /proc/meminfo"], timeout=30),
                "cpu": run(["bash", "-lc", "nproc && lscpu | sed -n '1,12p'"], timeout=30),
            },
            "candidates": {},
        }
        result["candidates"]["Bevy"] = {**CANDIDATES["Bevy"], **probe_bevy(root)}
        result["candidates"]["Defold"] = {**CANDIDATES["Defold"], **probe_defold(root)}
        result["candidates"]["Godot"] = {**CANDIDATES["Godot"], **probe_godot(root)}
        result["candidates"]["Unity"] = {**CANDIDATES["Unity"], **probe_unity()}
        result["candidates"]["Unreal Engine"] = {**CANDIDATES["Unreal Engine"], **probe_unreal()}
        statuses = {k: v["status"] for k, v in result["candidates"].items()}
        result["status_summary"] = statuses
        result["full_five_candidate_harness_capable"] = all(v in ("CAPABLE", "CAPABLE_WITH_PRESEED") for v in statuses.values())
        result["residual_external_authority_candidates"] = [k for k, v in statuses.items() if v == "BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY"]
        result["prior_not_run_promoted"] = False
        out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
        print(json.dumps({"schema": SCHEMA, "statuses": statuses, "full_five_candidate_harness_capable": result["full_five_candidate_harness_capable"], "out": str(out)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
