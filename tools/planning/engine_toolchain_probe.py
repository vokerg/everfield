#!/usr/bin/env python3
"""Bounded W2-CI-REM-01 capability probe.

This script establishes execution-environment capability only. It does not run,
score, rank, or select an engine and it never upgrades W2-ENG-03 NOT_RUN cells.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import platform
import shutil
import subprocess
import tempfile
import time
from typing import Any

SCHEMA = "W2-CI-ENGINE-TOOLCHAIN-CAPABILITY-v2"
ARTIFACT_LOCK_SCHEMA = "W2-CI-ENGINE-ARTIFACT-LOCK-v1"
CANDIDATES = {
    "Bevy": {"baseline": "0.19.0", "surface": "cargo/rustc + exact retained Cargo.lock replay"},
    "Defold": {"baseline": "1.13.0", "surface": "Java + exact digest-bound bob.jar"},
    "Godot": {"baseline": "4.7.1-stable", "surface": "exact digest-bound Linux archive + headless executable"},
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


def ok(r: dict[str, Any] | None) -> bool:
    return bool(r and r.get("exit") == 0 and not r.get("timed_out"))


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


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


def release_asset_digest(repo: str, tag: str, asset_name: str) -> dict[str, Any]:
    """Best-effort lookup of GitHub's release-asset digest metadata."""
    curl = shutil.which("curl")
    url = f"https://api.github.com/repos/{repo}/releases/tags/{tag}"
    if not curl:
        return {"api_url": url, "asset_name": asset_name, "digest": None, "source": "UNAVAILABLE", "probe": {"exit": 127}}
    probe = run(
        [curl, "-fsSL", "--max-time", "30", "-H", "Accept: application/vnd.github+json", "-H", "X-GitHub-Api-Version: 2022-11-28", url],
        timeout=40,
    )
    digest = None
    if ok(probe):
        try:
            payload = json.loads(probe["stdout"])
            for asset in payload.get("assets", []):
                if asset.get("name") == asset_name:
                    candidate = asset.get("digest")
                    if isinstance(candidate, str) and candidate.startswith("sha256:") and len(candidate) == 71:
                        digest = candidate.split(":", 1)[1].lower()
                    break
        except (json.JSONDecodeError, AttributeError):
            pass
    return {
        "api_url": url,
        "asset_name": asset_name,
        "digest": digest,
        "source": "GITHUB_RELEASE_ASSET_DIGEST" if digest else "NO_AUTHORITATIVE_DIGEST_OBSERVED",
        "probe": probe,
    }


def load_artifact_lock(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema": ARTIFACT_LOCK_SCHEMA, "mission_id": "W2-CI-REM-01", "entries": {}}
    data = json.loads(path.read_text())
    if data.get("schema") != ARTIFACT_LOCK_SCHEMA or not isinstance(data.get("entries"), dict):
        raise ValueError("invalid artifact lock schema")
    return data


def choose_expected_digest(
    lock: dict[str, Any],
    key: str,
    *,
    observed: str,
    url: str,
    version: str,
    vendor: dict[str, Any],
) -> dict[str, Any]:
    entries = lock.setdefault("entries", {})
    existing = entries.get(key)
    if isinstance(existing, dict) and isinstance(existing.get("sha256"), str):
        expected = existing["sha256"].lower()
        source = "RETAINED_REPOSITORY_ARTIFACT_LOCK"
        limitation = existing.get("limitation")
    elif vendor.get("digest"):
        expected = str(vendor["digest"]).lower()
        source = "GITHUB_RELEASE_ASSET_DIGEST"
        limitation = None
        entries[key] = {
            "version": version,
            "url": url,
            "sha256": expected,
            "digest_source": source,
            "limitation": limitation,
        }
    else:
        expected = observed
        source = "OBSERVED_RUN_TOFU_LOCK"
        limitation = (
            "No authoritative vendor digest was observed from the public GitHub release metadata; "
            "this exact run content identity is retained for subsequent replay, not represented as vendor-signed identity."
        )
        entries[key] = {
            "version": version,
            "url": url,
            "sha256": expected,
            "digest_source": source,
            "limitation": limitation,
        }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "verified": expected == observed,
        "digest_source": source,
        "limitation": limitation,
        "vendor_digest_probe": vendor,
    }


def write_probe_project(path: pathlib.Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    (path / "src").mkdir(exist_ok=True)
    (path / "src" / "main.rs").write_text('fn main() { println!("bevy-ci-bootstrap"); }\n')
    (path / "Cargo.toml").write_text(
        "[package]\nname='everfield_bevy_probe'\nversion='0.0.0'\nedition='2024'\n"
        "[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n"
    )


def probe_bevy(root: pathlib.Path, retained_lock: pathlib.Path) -> dict[str, Any]:
    rustc = command_version("rustc", ["--version"])
    cargo = command_version("cargo", ["--version"])
    if not cargo["path"] or not rustc["path"]:
        return {"status": "FAILED", "reason": "rustc_or_cargo_missing", "rustc": rustc, "cargo": cargo}

    seed = root / "bevy-seed"
    write_probe_project(seed)
    retained_lock.parent.mkdir(parents=True, exist_ok=True)

    if retained_lock.exists():
        shutil.copy2(retained_lock, seed / "Cargo.lock")
        lock_source = "RETAINED_REPOSITORY_LOCK"
        resolution = {"cmd": ["reuse", str(retained_lock)], "exit": 0, "seconds": 0, "stdout": "", "stderr": "", "timed_out": False}
    else:
        resolution = run([cargo["path"], "fetch"], cwd=seed, timeout=300)
        if ok(resolution) and (seed / "Cargo.lock").exists():
            shutil.copy2(seed / "Cargo.lock", retained_lock)
        lock_source = "GENERATED_AND_PERSISTED_THIS_RUN"

    lock_present = retained_lock.exists()
    lock_sha = sha256_file(retained_lock) if lock_present else None

    replay = root / "bevy-replay"
    write_probe_project(replay)
    if lock_present:
        shutil.copy2(retained_lock, replay / "Cargo.lock")
    replay_fetch = run([cargo["path"], "fetch", "--locked"], cwd=replay, timeout=240) if lock_present else None
    check = run([cargo["path"], "check", "--locked", "--quiet"], cwd=replay, timeout=420) if ok(replay_fetch) else None
    capable = bool(lock_sha and check and ok(check))

    return {
        "status": "CAPABLE_WITH_PRESEED" if capable else "FAILED",
        "reason": (
            "exact_retained_cargo_lock_replayed_and_compiled; full graphics/package harness not executed"
            if capable
            else "retained_bevy_resolution_replay_failed"
        ),
        "rustc": rustc,
        "cargo": cargo,
        "resolution": resolution,
        "retained_lock_path": retained_lock.as_posix(),
        "retained_lock_source": lock_source,
        "retained_lock_sha256": lock_sha,
        "lock_replay_bound": capable,
        "replay_locked_fetch": replay_fetch,
        "cargo_check": check,
    }


def probe_defold(root: pathlib.Path, lock: dict[str, Any]) -> dict[str, Any]:
    java = command_version("java", ["-version"])
    curl = shutil.which("curl")
    url = "https://github.com/defold/defold/releases/download/1.13.0/bob.jar"
    if not java["path"] or not curl:
        return {"status": "FAILED", "reason": "java_or_curl_missing", "java": java, "url": url}

    jar = root / "bob-1.13.0.jar"
    dl = run([curl, "-fL", "--retry", "2", "--connect-timeout", "20", "-o", str(jar), url], timeout=240)
    if not ok(dl) or not jar.exists():
        return {"status": "FAILED", "reason": "bob_download_failed", "java": java, "url": url, "download": dl}

    observed = sha256_file(jar)
    vendor = release_asset_digest("defold/defold", "1.13.0", "bob.jar")
    identity = choose_expected_digest(lock, "defold_bob_1.13.0", observed=observed, url=url, version="1.13.0", vendor=vendor)
    version = run([java["path"], "-jar", str(jar), "--version"], timeout=120) if identity["verified"] else None
    capable = bool(identity["verified"] and version and ok(version))
    return {
        "status": "CAPABLE" if capable else "FAILED",
        "reason": "digest_bound_bob_jar_downloaded_and_executed" if capable else "bob_artifact_identity_or_execution_failed",
        "java": java,
        "url": url,
        "download": dl,
        "artifact_identity": identity,
        "bob_version": version,
        "bytes": jar.stat().st_size,
    }


def probe_godot(root: pathlib.Path, lock: dict[str, Any]) -> dict[str, Any]:
    curl = shutil.which("curl")
    unzip = shutil.which("unzip")
    asset_name = "Godot_v4.7.1-stable_linux.x86_64.zip"
    url = f"https://github.com/godotengine/godot/releases/download/4.7.1-stable/{asset_name}"
    if not curl or not unzip:
        return {"status": "FAILED", "reason": "curl_or_unzip_missing", "url": url}

    z = root / "godot-4.7.1.zip"
    out = root / "godot"
    out.mkdir()
    dl = run([curl, "-fL", "--retry", "2", "--connect-timeout", "20", "-o", str(z), url], timeout=300)
    if not ok(dl) or not z.exists():
        return {"status": "FAILED", "reason": "godot_download_failed", "url": url, "download": dl}

    observed = sha256_file(z)
    vendor = release_asset_digest("godotengine/godot", "4.7.1-stable", asset_name)
    identity = choose_expected_digest(lock, "godot_4.7.1_linux_x86_64_zip", observed=observed, url=url, version="4.7.1-stable", vendor=vendor)
    uz = run([unzip, "-q", str(z), "-d", str(out)], timeout=120) if identity["verified"] else None

    exe = None
    if uz and ok(uz):
        matches = sorted(p for p in out.iterdir() if p.is_file() and p.name.startswith("Godot_v4.7.1"))
        exe = matches[0] if matches else None
        if exe:
            exe.chmod(exe.stat().st_mode | 0o111)

    version = run([str(exe), "--headless", "--version"], timeout=60) if exe else None
    capable = bool(identity["verified"] and version and ok(version))
    return {
        "status": "CAPABLE" if capable else "FAILED",
        "reason": "digest_bound_linux_archive_extracted_and_headless_process_executed" if capable else "godot_artifact_identity_or_headless_execution_failed",
        "url": url,
        "download": dl,
        "artifact_identity": identity,
        "unzip": uz,
        "executable": str(exe) if exe else None,
        "executable_sha256": sha256_file(exe) if exe and exe.exists() else None,
        "version": version,
        "bytes": z.stat().st_size,
    }


def probe_unity() -> dict[str, Any]:
    archive = head("https://unity.com/releases/editor/archive")
    hub = head("https://hub.unity3d.com/")
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
        "reason": "public_vendor_network_is_probeable_but_linux_engine_source/prebuilt_acquisition_requires_Epic-linked_entitlement_or_preseeded_artifact",
        "required_external_authority": "Epic-authorized Unreal Engine 5.8 source/prebuilt artifact access suitable for unattended CI",
        "public_network": public,
        "source_entitlement_probe": source,
        "credential_values_read": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--bevy-lock", required=True)
    ap.add_argument("--artifact-lock", required=True)
    args = ap.parse_args()

    out = pathlib.Path(args.out)
    bevy_lock = pathlib.Path(args.bevy_lock)
    artifact_lock_path = pathlib.Path(args.artifact_lock)
    out.parent.mkdir(parents=True, exist_ok=True)
    artifact_lock_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        artifact_lock = load_artifact_lock(artifact_lock_path)
    except (ValueError, json.JSONDecodeError) as exc:
        artifact_lock = {"schema": ARTIFACT_LOCK_SCHEMA, "mission_id": "W2-CI-REM-01", "entries": {}, "load_error": str(exc)}

    with tempfile.TemporaryDirectory(prefix="everfield-ci-rem-probe-") as td:
        root = pathlib.Path(td)
        result: dict[str, Any] = {
            "schema": SCHEMA,
            "mission_id": "W2-CI-REM-01",
            "source_issue": 343,
            "predecessor_issue": 339,
            "required_review_issue": 341,
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

        result["candidates"]["Bevy"] = {**CANDIDATES["Bevy"], **probe_bevy(root, bevy_lock)}
        result["candidates"]["Defold"] = {**CANDIDATES["Defold"], **probe_defold(root, artifact_lock)}
        result["candidates"]["Godot"] = {**CANDIDATES["Godot"], **probe_godot(root, artifact_lock)}
        result["candidates"]["Unity"] = {**CANDIDATES["Unity"], **probe_unity()}
        result["candidates"]["Unreal Engine"] = {**CANDIDATES["Unreal Engine"], **probe_unreal()}

        artifact_lock["bevy_lock"] = {
            "path": bevy_lock.as_posix(),
            "sha256": sha256_file(bevy_lock) if bevy_lock.exists() else None,
        }
        artifact_lock["updated_by_github_run_id"] = os.getenv("GITHUB_RUN_ID")
        artifact_lock_path.write_text(json.dumps(artifact_lock, sort_keys=True, indent=2) + "\n")

        statuses = {k: v["status"] for k, v in result["candidates"].items()}
        result["status_summary"] = statuses
        result["artifact_lock_path"] = artifact_lock_path.as_posix()
        result["artifact_lock_sha256"] = sha256_file(artifact_lock_path)
        result["full_five_candidate_harness_capable"] = all(v in ("CAPABLE", "CAPABLE_WITH_PRESEED") for v in statuses.values())
        result["residual_external_authority_candidates"] = [k for k, v in statuses.items() if v == "BLOCKED_BY_SPECIFIC_EXTERNAL_AUTHORITY"]
        result["prior_not_run_promoted"] = False
        out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
        print(json.dumps({
            "schema": SCHEMA,
            "statuses": statuses,
            "full_five_candidate_harness_capable": result["full_five_candidate_harness_capable"],
            "artifact_lock_sha256": result["artifact_lock_sha256"],
            "out": str(out),
        }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
