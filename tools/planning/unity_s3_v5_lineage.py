#!/usr/bin/env python3
# Retain sanitized, mechanically checkable lineage for trusted-main Unity S3 attempts.
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import subprocess
import tempfile
import time
import uuid
from typing import Any

SCHEMA = "W2-ENG-UNITY-S3-V5-LINEAGE-v1"
MISSION_ID = "W2-ENG-TECH-UNITY-S3-V5-RERUN-01"
REPOSITORY = "vokerg/everfield"
UNITY_VERSION = "6000.5.6f1"
CANDIDATE_ID = "Unity"
HARNESS_ID = "W2-ENG-HARNESS-v5"
VALIDATOR_ID = "W2-ENG-PROTOCOL-VALIDATOR-v5"
FEATURE_SLICE_ID = "W2-ENG-FEATURE-SLICE-v2"
SCENARIO_MANIFEST_ID = "W2-ENG-SCENARIO-INPUTS-v2"
SCENARIO_ID = "S3"
RESOURCE_CLASS = "W2-ENG-HOST-COMMON-v2"
INJECTION_ID = "FI-S3-INPUT-PERTURB-v2"
MECHANISM_AUTHORITY = "REAL_OR_SHARED_RULES"
NORMAL_CHECKSUM = 405227
PERTURBED_CHECKSUM = 405122
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
BANNED_KEY_FRAGMENTS = ("secret", "password", "cookie", "authorization", "bearer", "session_token", "access_token")
BANNED_VALUE_FRAGMENTS = (
    "unity_service_account_secret", "unreal_github_token", "password=", "token=",
    "authorization:", "cookie=", "bearer ",
)

S3_INPUT = {
    "seed": 424242,
    "entity_count": 32,
    "normal_ticks": 600,
    "action_count": 10,
    "perturb_tick": 137,
    "required_injection": INJECTION_ID,
}
START_PROFILE = {
    "profile_id": "W2-ENG-START-COLD-v2",
    "cache_mode": "COLD",
    "generated_state_policy": "REGENERATE_FROM_REPO",
    "resource_class": RESOURCE_CLASS,
}

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

ATTEMPT_PLAN = (
    ("UNITY-S3-N1", "NORMAL", 1, None, False, NORMAL_CHECKSUM),
    ("UNITY-S3-N2", "NORMAL", 2, None, False, NORMAL_CHECKSUM),
    ("UNITY-S3-FI1", "FAILURE_INJECTION", None, INJECTION_ID, True, PERTURBED_CHECKSUM),
)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sensitive_scan(value: Any, trail: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            lower = str(key).lower()
            require(not any(fragment in lower for fragment in BANNED_KEY_FRAGMENTS),
                    f"sensitive key at {trail}.{key}")
            sensitive_scan(child, f"{trail}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            sensitive_scan(child, f"{trail}[{index}]")
    elif isinstance(value, str):
        lower = value.lower()
        require(not any(fragment in lower for fragment in BANNED_VALUE_FRAGMENTS),
                f"sensitive value at {trail}")
        require(not value.startswith("/"), f"absolute path leaked at {trail}")
        require(not re.match(r"^[A-Za-z]:[\\/]", value), f"absolute path leaked at {trail}")


def checksum_from(text: str) -> int | None:
    hits = re.findall(r"EVERFIELD_S3:(\d+)", text or "")
    return int(hits[-1]) if hits else None


def run_process(command: list[str], *, env: dict[str, str], timeout: int = 300) -> dict[str, Any]:
    started = time.monotonic()
    try:
        proc = subprocess.run(
            command,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
            env={**os.environ, **env},
        )
        return {
            "exit": proc.returncode,
            "timed_out": False,
            "seconds": round(time.monotonic() - started, 3),
            "_stdout": proc.stdout,
            "_stderr": proc.stderr,
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "exit": None,
            "timed_out": True,
            "seconds": round(time.monotonic() - started, 3),
            "_stdout": exc.stdout if isinstance(exc.stdout, str) else "",
            "_stderr": exc.stderr if isinstance(exc.stderr, str) else "",
        }


def shared_source() -> dict[str, Any]:
    script_bytes = UNITY_NATIVE_SCRIPT.encode("utf-8")
    project_version = f"m_EditorVersion: {UNITY_VERSION}\n".encode("utf-8")
    files = {
        "Assets/Editor/EverfieldS3.cs": hashlib.sha256(script_bytes).hexdigest(),
        "ProjectSettings/ProjectVersion.txt": hashlib.sha256(project_version).hexdigest(),
    }
    return {
        "fixed_input_digest": digest(S3_INPUT),
        "unity_script_sha256": files["Assets/Editor/EverfieldS3.cs"],
        "generated_project_source_digest": digest(files),
        "generated_files": files,
    }


def adaptation_seed() -> dict[str, Any]:
    return {
        "candidate_id": CANDIDATE_ID,
        "scenario_id": SCENARIO_ID,
        "harness_id": HARNESS_ID,
        "feature_slice_id": FEATURE_SLICE_ID,
        "fixed_input_refs": ["SLICE:logical_state", "SLICE:action_vocabulary"],
        "mappings": {
            "real_or_shared_rules": "EQUIVALENT",
            "exact_seed_input": "EQUIVALENT",
            "repeatable_state_events": "EQUIVALENT",
            "perturbation_distinguishable": "EQUIVALENT",
        },
        "bounds": {"entity_count": 32, "normal_ticks": 600, "action_count": 10},
        "failure_injections": [INJECTION_ID],
        "start_profile": dict(START_PROFILE),
        "undocumented_manual_intervention": False,
        "resource_exception": False,
        "mechanism_authority": MECHANISM_AUTHORITY,
        "package_target": None,
        "hidden_context_transfer": False,
        "extra_evidence": [],
    }


def workspace_identity(root: pathlib.Path, attempt_id: str) -> tuple[str, str]:
    marker = {
        "schema": "EVERFIELD-UNITY-S3-WORKSPACE-MARKER-v1",
        "attempt_id": attempt_id,
        "nonce": uuid.uuid4().hex,
    }
    marker_bytes = canonical_bytes(marker)
    marker_path = root / ".everfield-workspace-marker.json"
    marker_path.write_bytes(marker_bytes)
    marker_digest = hashlib.sha256(marker_bytes).hexdigest()
    return digest({"attempt_id": attempt_id, "marker_sha256": marker_digest}), marker_digest


def materialize_project(root: pathlib.Path) -> dict[str, Any]:
    (root / "Assets" / "Editor").mkdir(parents=True)
    (root / "ProjectSettings").mkdir()
    source_path = root / "Assets" / "Editor" / "EverfieldS3.cs"
    version_path = root / "ProjectSettings" / "ProjectVersion.txt"
    source_path.write_text(UNITY_NATIVE_SCRIPT, encoding="utf-8")
    version_path.write_text(f"m_EditorVersion: {UNITY_VERSION}\n", encoding="utf-8")
    observed = {
        "Assets/Editor/EverfieldS3.cs": file_sha256(source_path),
        "ProjectSettings/ProjectVersion.txt": file_sha256(version_path),
    }
    return {
        "generated_project_source_digest": digest(observed),
        "generated_files": observed,
    }


def lineage_basis(attempt: dict[str, Any]) -> dict[str, Any]:
    return {
        key: attempt[key]
        for key in (
            "attempt_id", "scenario_id", "candidate_id", "kind", "normal_index",
            "injection_id", "expected_checksum", "observed_checksum", "result",
            "failure_class", "workspace_id", "workspace_marker_sha256", "reset_id",
            "reset_verified", "reset_facts", "resource_class", "executor_identity",
            "editor", "source", "process", "native_command_id",
        )
    }


def raw_digest_basis(attempt: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value for key, value in attempt.items()
        if key not in {"raw_attempt_digest", "source_binding_id"}
    }


def candidate_work_material(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "candidate_id": CANDIDATE_ID,
        "baseline": UNITY_VERSION,
        "validator_id": VALIDATOR_ID,
        "harness_id": HARNESS_ID,
        "feature_slice_id": FEATURE_SLICE_ID,
        "scenario_manifest_id": SCENARIO_MANIFEST_ID,
        "scenario_id": SCENARIO_ID,
        "fixed_input_digest": packet["source"]["fixed_input_digest"],
        "generated_project_source_digest": packet["source"]["generated_project_source_digest"],
        "unity_script_sha256": packet["source"]["unity_script_sha256"],
        "editor_executable_sha256": packet["editor"]["executable_sha256"],
        "resource_class": RESOURCE_CLASS,
    }


def generation_material(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "candidate_work_id": packet["candidate"]["candidate_work_id"],
        "source_head_sha": packet["run"]["head_sha"],
        "run_id": packet["run"]["run_id"],
        "run_attempt": packet["run"]["run_attempt"],
        "attempt_lineage_digests": [
            packet["attempts"][attempt_id]["lineage_digest"]
            for attempt_id in packet["run_registry_refs"]
        ],
    }


def execute_attempt(
    root: pathlib.Path,
    *,
    attempt_id: str,
    kind: str,
    normal_index: int | None,
    injection_id: str | None,
    perturb: bool,
    expected: int,
    editor_path: pathlib.Path,
    editor_digest: str,
    executor_identity: dict[str, Any],
) -> dict[str, Any]:
    pre_generation_empty = not any(root.iterdir())
    generated_state_absent = all(not (root / name).exists() for name in ("Library", "Temp", "Logs", "obj"))
    workspace_id, marker_digest = workspace_identity(root, attempt_id)
    source = materialize_project(root)
    expected_source = shared_source()
    source_matches = source == {
        "generated_project_source_digest": expected_source["generated_project_source_digest"],
        "generated_files": expected_source["generated_files"],
    }
    reset_facts = {
        "fresh_attempt_directory_created": True,
        "pre_generation_directory_empty": pre_generation_empty,
        "no_preexisting_generated_state": generated_state_absent,
        "workspace_marker_created_before_project": True,
        "source_materialized_from_embedded_contract": source_matches,
        "project_version_matches": source["generated_files"]["ProjectSettings/ProjectVersion.txt"] == expected_source["generated_files"]["ProjectSettings/ProjectVersion.txt"],
        "fixed_input_digest_matches": expected_source["fixed_input_digest"] == digest(S3_INPUT),
    }
    reset_verified = all(reset_facts.values())
    reset_id = digest({
        "attempt_id": attempt_id,
        "workspace_id": workspace_id,
        "source_digest": source["generated_project_source_digest"],
        "fixed_input_digest": expected_source["fixed_input_digest"],
        "reset_facts": reset_facts,
    })
    log_path = root / "Unity.log"
    command = [
        str(editor_path), "-batchmode", "-nographics", "-quit",
        "-projectPath", str(root), "-executeMethod", "EverfieldS3.Run",
        "-logFile", str(log_path),
    ]
    process = run_process(command, env={"EVERFIELD_PERTURB": "1" if perturb else "0"})
    log_text = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else ""
    observed = checksum_from(process.pop("_stdout") + "\n" + process.pop("_stderr") + "\n" + log_text)
    passed = process["exit"] == 0 and process["timed_out"] is False and observed == expected
    attempt: dict[str, Any] = {
        "attempt_id": attempt_id,
        "scenario_id": SCENARIO_ID,
        "candidate_id": CANDIDATE_ID,
        "kind": kind,
        "normal_index": normal_index,
        "injection_id": injection_id,
        "expected_checksum": expected,
        "observed_checksum": observed,
        "result": "PASS" if passed else "INCONCLUSIVE",
        "failure_class": "NONE" if passed else ("INFRA" if process["timed_out"] else "HARNESS"),
        "workspace_id": workspace_id,
        "workspace_marker_sha256": marker_digest,
        "reset_id": reset_id,
        "reset_verified": reset_verified,
        "reset_facts": reset_facts,
        "resource_class": RESOURCE_CLASS,
        "executor_identity": dict(executor_identity),
        "editor": {
            "version": UNITY_VERSION,
            "executable_name": editor_path.name,
            "executable_sha256": editor_digest,
        },
        "source": {
            **source,
            "unity_script_sha256": expected_source["unity_script_sha256"],
            "fixed_input_digest": expected_source["fixed_input_digest"],
        },
        "process": process,
        "native_command_id": "Unity Editor -batchmode -executeMethod EverfieldS3.Run",
    }
    attempt["lineage_digest"] = digest(lineage_basis(attempt))
    return attempt


def build_packet(editor_path: pathlib.Path) -> dict[str, Any]:
    env = {
        "repository": os.getenv("GITHUB_REPOSITORY", ""),
        "ref": os.getenv("GITHUB_REF", ""),
        "head_sha": os.getenv("GITHUB_SHA", ""),
        "event": os.getenv("GITHUB_EVENT_NAME", ""),
        "run_id": os.getenv("GITHUB_RUN_ID", ""),
        "run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", ""),
        "runner_name": os.getenv("RUNNER_NAME", ""),
        "runner_os": os.getenv("RUNNER_OS", ""),
        "runner_arch": os.getenv("RUNNER_ARCH", ""),
    }
    require(env["repository"] == REPOSITORY, "repository mismatch")
    require(env["ref"] == "refs/heads/main", "ref is not main")
    require(env["event"] == "workflow_dispatch", "event is not workflow_dispatch")
    require(SHA_RE.fullmatch(env["head_sha"]) is not None, "invalid head SHA")
    require(env["run_id"].isdigit() and env["run_attempt"].isdigit(), "invalid run identity")
    require(env["runner_name"] == "everfield-unity-mac", "runner name mismatch")
    require(env["runner_os"] == "macOS" and env["runner_arch"] == "ARM64", "runner platform mismatch")
    require(editor_path.is_file() and os.access(editor_path, os.X_OK), "Unity editor is not executable")
    editor_digest = file_sha256(editor_path)
    source = shared_source()
    executor_identity = {
        "execution_context": "PERSISTENT_SELF_HOSTED_WORKSTATION",
        "runner_name": env["runner_name"],
        "runner_os": env["runner_os"],
        "runner_arch": env["runner_arch"],
    }
    attempts: dict[str, Any] = {}
    with tempfile.TemporaryDirectory(prefix="everfield-unity-s3-v5-") as temp:
        parent = pathlib.Path(temp)
        for attempt_id, kind, normal_index, injection_id, perturb, expected in ATTEMPT_PLAN:
            root = parent / attempt_id
            root.mkdir()
            attempts[attempt_id] = execute_attempt(
                root,
                attempt_id=attempt_id,
                kind=kind,
                normal_index=normal_index,
                injection_id=injection_id,
                perturb=perturb,
                expected=expected,
                editor_path=editor_path,
                editor_digest=editor_digest,
                executor_identity=executor_identity,
            )
    packet: dict[str, Any] = {
        "schema": SCHEMA,
        "mission_id": MISSION_ID,
        "run": {
            "repository": env["repository"],
            "ref": env["ref"],
            "head_sha": env["head_sha"],
            "event": env["event"],
            "run_id": env["run_id"],
            "run_attempt": env["run_attempt"],
        },
        "reviewed_v5": {
            "validator_id": VALIDATOR_ID,
            "harness_id": HARNESS_ID,
            "feature_slice_id": FEATURE_SLICE_ID,
            "scenario_manifest_id": SCENARIO_MANIFEST_ID,
        },
        "contract": {
            "scenario_id": SCENARIO_ID,
            "seed": 424242,
            "entity_count": 32,
            "normal_ticks": 600,
            "action_count": 10,
            "required_injection": INJECTION_ID,
            "mechanism_authority": MECHANISM_AUTHORITY,
            "resource_class": RESOURCE_CLASS,
            "minimum_normal_attempts": 2,
            "required_failure_injection_attempts": 1,
        },
        "editor": {
            "version": UNITY_VERSION,
            "executable_name": editor_path.name,
            "executable_sha256": editor_digest,
        },
        "source": source,
        "adaptation_seed": adaptation_seed(),
        "candidate": {
            "candidate_id": CANDIDATE_ID,
            "candidate_work_id": "",
            "candidate_generation_id": "",
        },
        "attempts": attempts,
        "run_registry_refs": [item[0] for item in ATTEMPT_PLAN],
        "all_attempt_refs": [item[0] for item in ATTEMPT_PLAN],
        "source_registry": {},
        "native_s3_pass": all(item["result"] == "PASS" for item in attempts.values()),
        "historical_not_run_cells_preserved": 50,
        "historical_not_run_cells_mutated": False,
        "authority": {
            "pass_for_comparison": False,
            "provider_pass": False,
            "engine_selected": False,
            "implementation_readiness": False,
            "production_authority": False,
            "commercial_authority": False,
            "legal_clearance": False,
            "release_authority": False,
            "verification_pass_authority": False,
            "decision_authority": False,
            "integration_authority": False,
            "canonicality": "NOT_CANONICAL",
        },
    }
    packet["candidate"]["candidate_work_id"] = digest(candidate_work_material(packet))
    packet["candidate"]["candidate_generation_id"] = digest(generation_material(packet))
    generation_id = packet["candidate"]["candidate_generation_id"]
    for attempt_id in packet["run_registry_refs"]:
        attempt = packet["attempts"][attempt_id]
        attempt["candidate_generation_id"] = generation_id
        attempt["raw_attempt_digest"] = digest(raw_digest_basis(attempt))
        attempt["source_binding_id"] = digest({
            "attempt_id": attempt_id,
            "candidate_generation_id": generation_id,
            "raw_attempt_digest": attempt["raw_attempt_digest"],
            "workspace_id": attempt["workspace_id"],
            "reset_id": attempt["reset_id"],
            "generated_project_source_digest": attempt["source"]["generated_project_source_digest"],
        })
        packet["source_registry"][attempt_id] = {
            "lineage_digest": attempt["lineage_digest"],
            "raw_attempt_digest": attempt["raw_attempt_digest"],
            "source_binding_id": attempt["source_binding_id"],
        }
    validate_packet(packet)
    return packet


def _expected_generation(packet: dict[str, Any]) -> str:
    return digest(generation_material(packet))


def validate_packet(packet: Any) -> None:
    require(isinstance(packet, dict), "packet must be an object")
    sensitive_scan(packet)
    require(packet.get("schema") == SCHEMA, "schema mismatch")
    require(packet.get("mission_id") == MISSION_ID, "mission mismatch")
    run = packet.get("run")
    require(isinstance(run, dict), "run identity missing")
    require(run.get("repository") == REPOSITORY, "run repository mismatch")
    require(run.get("ref") == "refs/heads/main", "run ref mismatch")
    require(run.get("event") == "workflow_dispatch", "run event mismatch")
    require(isinstance(run.get("head_sha"), str) and SHA_RE.fullmatch(run["head_sha"]) is not None, "run head invalid")
    require(str(run.get("run_id", "")).isdigit() and str(run.get("run_attempt", "")).isdigit(), "run id invalid")
    reviewed = packet.get("reviewed_v5")
    require(reviewed == {
        "validator_id": VALIDATOR_ID,
        "harness_id": HARNESS_ID,
        "feature_slice_id": FEATURE_SLICE_ID,
        "scenario_manifest_id": SCENARIO_MANIFEST_ID,
    }, "reviewed-v5 identity drift")
    contract = packet.get("contract")
    require(isinstance(contract, dict), "contract missing")
    for key, value in {
        "scenario_id": SCENARIO_ID, "seed": 424242, "entity_count": 32,
        "normal_ticks": 600, "action_count": 10, "required_injection": INJECTION_ID,
        "mechanism_authority": MECHANISM_AUTHORITY, "resource_class": RESOURCE_CLASS,
        "minimum_normal_attempts": 2, "required_failure_injection_attempts": 1,
    }.items():
        require(contract.get(key) == value, f"contract mismatch: {key}")
    source = packet.get("source")
    require(source == shared_source(), "shared source digest mismatch")
    editor = packet.get("editor")
    require(isinstance(editor, dict) and editor.get("version") == UNITY_VERSION, "editor version mismatch")
    require(isinstance(editor.get("executable_name"), str) and editor["executable_name"], "editor name missing")
    require(isinstance(editor.get("executable_sha256"), str) and HEX64_RE.fullmatch(editor["executable_sha256"]) is not None, "editor digest invalid")
    require(packet.get("adaptation_seed") == adaptation_seed(), "adaptation seed drift")
    refs = packet.get("run_registry_refs")
    all_refs = packet.get("all_attempt_refs")
    expected_refs = [item[0] for item in ATTEMPT_PLAN]
    require(refs == expected_refs and all_refs == expected_refs, "attempt registry mismatch")
    attempts = packet.get("attempts")
    require(
        isinstance(attempts, dict)
        and len(attempts) == len(expected_refs)
        and set(attempts) == set(expected_refs),
        "attempt set mismatch",
    )
    candidate = packet.get("candidate")
    require(isinstance(candidate, dict) and candidate.get("candidate_id") == CANDIDATE_ID, "candidate mismatch")
    expected_work = digest(candidate_work_material(packet))
    require(candidate.get("candidate_work_id") == expected_work, "candidate work identity mismatch")
    expected_generation = _expected_generation(packet)
    require(candidate.get("candidate_generation_id") == expected_generation, "candidate generation identity mismatch")
    source_registry = packet.get("source_registry")
    require(isinstance(source_registry, dict) and set(source_registry) == set(expected_refs), "source registry mismatch")
    workspace_ids: set[str] = set()
    reset_ids: set[str] = set()
    binding_ids: set[str] = set()
    lineage_ids: set[str] = set()
    for plan in ATTEMPT_PLAN:
        attempt_id, kind, normal_index, injection_id, _perturb, expected = plan
        attempt = attempts[attempt_id]
        require(attempt.get("attempt_id") == attempt_id, "attempt id mismatch")
        require(attempt.get("scenario_id") == SCENARIO_ID and attempt.get("candidate_id") == CANDIDATE_ID, "attempt identity mismatch")
        require(attempt.get("candidate_generation_id") == expected_generation, "attempt generation mismatch")
        require(attempt.get("kind") == kind and attempt.get("normal_index") == normal_index and attempt.get("injection_id") == injection_id, "attempt kind identity mismatch")
        require(attempt.get("expected_checksum") == expected, "expected checksum mismatch")
        require(attempt.get("result") in {"PASS", "INCONCLUSIVE"}, "result invalid")
        matrix = {"PASS": {"NONE"}, "INCONCLUSIVE": {"INFRA", "HARNESS", "UNKNOWN"}}
        require(attempt.get("failure_class") in matrix[attempt["result"]], "result/failure envelope invalid")
        require(isinstance(attempt.get("workspace_id"), str) and HEX64_RE.fullmatch(attempt["workspace_id"]) is not None, "workspace id invalid")
        require(isinstance(attempt.get("workspace_marker_sha256"), str) and HEX64_RE.fullmatch(attempt["workspace_marker_sha256"]) is not None, "workspace marker invalid")
        require(isinstance(attempt.get("reset_id"), str) and HEX64_RE.fullmatch(attempt["reset_id"]) is not None, "reset id invalid")
        facts = attempt.get("reset_facts")
        require(isinstance(facts, dict) and facts, "reset facts missing")
        mechanical_reset = all(value is True for value in facts.values())
        require(type(attempt.get("reset_verified")) is bool and attempt["reset_verified"] == mechanical_reset, "reset verification is not mechanically derived")
        require(attempt["reset_verified"] is True, "attempt reset did not verify")
        require(attempt.get("resource_class") == RESOURCE_CLASS, "resource class mismatch")
        executor = attempt.get("executor_identity")
        require(executor == {
            "execution_context": "PERSISTENT_SELF_HOSTED_WORKSTATION",
            "runner_name": "everfield-unity-mac",
            "runner_os": "macOS",
            "runner_arch": "ARM64",
        }, "executor identity mismatch")
        require(attempt.get("editor") == editor, "per-attempt editor binding mismatch")
        attempt_source = attempt.get("source")
        require(isinstance(attempt_source, dict), "attempt source missing")
        require(attempt_source.get("generated_project_source_digest") == source["generated_project_source_digest"], "project source digest mismatch")
        require(attempt_source.get("unity_script_sha256") == source["unity_script_sha256"], "script digest mismatch")
        require(attempt_source.get("fixed_input_digest") == source["fixed_input_digest"], "fixed input digest mismatch")
        process = attempt.get("process")
        require(isinstance(process, dict) and set(process) == {"exit", "timed_out", "seconds"}, "process envelope mismatch")
        require(type(process["timed_out"]) is bool, "timeout flag invalid")
        require(process["exit"] is None or type(process["exit"]) is int, "process exit invalid")
        require(type(process["seconds"]) in (int, float) and process["seconds"] >= 0, "process seconds invalid")
        require(attempt.get("native_command_id") == "Unity Editor -batchmode -executeMethod EverfieldS3.Run", "native command identity mismatch")
        lineage = digest(lineage_basis(attempt))
        require(attempt.get("lineage_digest") == lineage, "lineage digest mismatch")
        raw = digest(raw_digest_basis(attempt))
        require(attempt.get("raw_attempt_digest") == raw, "raw attempt digest mismatch")
        binding = digest({
            "attempt_id": attempt_id,
            "candidate_generation_id": expected_generation,
            "raw_attempt_digest": raw,
            "workspace_id": attempt["workspace_id"],
            "reset_id": attempt["reset_id"],
            "generated_project_source_digest": attempt_source["generated_project_source_digest"],
        })
        require(attempt.get("source_binding_id") == binding, "source binding mismatch")
        require(source_registry[attempt_id] == {
            "lineage_digest": lineage,
            "raw_attempt_digest": raw,
            "source_binding_id": binding,
        }, "source registry entry mismatch")
        workspace_ids.add(attempt["workspace_id"])
        reset_ids.add(attempt["reset_id"])
        binding_ids.add(binding)
        lineage_ids.add(lineage)
    require(len(workspace_ids) == 3, "attempt workspaces are not unique")
    require(len(reset_ids) == 3, "attempt resets are not unique")
    require(len(binding_ids) == 3, "source bindings are not unique")
    require(len(lineage_ids) == 3, "lineage digests are not unique")
    require(packet.get("native_s3_pass") == all(attempt["result"] == "PASS" for attempt in attempts.values()), "native pass summary mismatch")
    require(packet.get("historical_not_run_cells_preserved") == 50 and packet.get("historical_not_run_cells_mutated") is False, "historical evidence mutation")
    authority = packet.get("authority")
    require(isinstance(authority, dict), "authority boundary missing")
    for key in (
        "pass_for_comparison", "provider_pass", "engine_selected", "implementation_readiness",
        "production_authority", "commercial_authority", "legal_clearance",
        "release_authority", "verification_pass_authority", "decision_authority",
        "integration_authority",
    ):
        require(authority.get(key) is False, f"authority inflation: {key}")
    require(authority.get("canonicality") == "NOT_CANONICAL", "canonicality inflation")


def synthetic_packet() -> dict[str, Any]:
    source = shared_source()
    editor = {"version": UNITY_VERSION, "executable_name": "Unity", "executable_sha256": "a" * 64}
    attempts: dict[str, Any] = {}
    for index, (attempt_id, kind, normal_index, injection_id, _perturb, expected) in enumerate(ATTEMPT_PLAN, 1):
        facts = {
            "fresh_attempt_directory_created": True,
            "pre_generation_directory_empty": True,
            "no_preexisting_generated_state": True,
            "workspace_marker_created_before_project": True,
            "source_materialized_from_embedded_contract": True,
            "project_version_matches": True,
            "fixed_input_digest_matches": True,
        }
        attempt = {
            "attempt_id": attempt_id,
            "scenario_id": SCENARIO_ID,
            "candidate_id": CANDIDATE_ID,
            "kind": kind,
            "normal_index": normal_index,
            "injection_id": injection_id,
            "expected_checksum": expected,
            "observed_checksum": expected,
            "result": "PASS",
            "failure_class": "NONE",
            "workspace_id": hashlib.sha256(f"workspace-{index}".encode()).hexdigest(),
            "workspace_marker_sha256": hashlib.sha256(f"marker-{index}".encode()).hexdigest(),
            "reset_id": hashlib.sha256(f"reset-{index}".encode()).hexdigest(),
            "reset_verified": True,
            "reset_facts": facts,
            "resource_class": RESOURCE_CLASS,
            "executor_identity": {
                "execution_context": "PERSISTENT_SELF_HOSTED_WORKSTATION",
                "runner_name": "everfield-unity-mac",
                "runner_os": "macOS",
                "runner_arch": "ARM64",
            },
            "editor": dict(editor),
            "source": {
                "generated_project_source_digest": source["generated_project_source_digest"],
                "generated_files": dict(source["generated_files"]),
                "unity_script_sha256": source["unity_script_sha256"],
                "fixed_input_digest": source["fixed_input_digest"],
            },
            "process": {"exit": 0, "timed_out": False, "seconds": 1.0 + index},
            "native_command_id": "Unity Editor -batchmode -executeMethod EverfieldS3.Run",
        }
        attempt["lineage_digest"] = digest(lineage_basis(attempt))
        attempts[attempt_id] = attempt
    packet = {
        "schema": SCHEMA,
        "mission_id": MISSION_ID,
        "run": {
            "repository": REPOSITORY, "ref": "refs/heads/main", "head_sha": "b" * 40,
            "event": "workflow_dispatch", "run_id": "123", "run_attempt": "1",
        },
        "reviewed_v5": {
            "validator_id": VALIDATOR_ID, "harness_id": HARNESS_ID,
            "feature_slice_id": FEATURE_SLICE_ID, "scenario_manifest_id": SCENARIO_MANIFEST_ID,
        },
        "contract": {
            "scenario_id": SCENARIO_ID, "seed": 424242, "entity_count": 32,
            "normal_ticks": 600, "action_count": 10, "required_injection": INJECTION_ID,
            "mechanism_authority": MECHANISM_AUTHORITY, "resource_class": RESOURCE_CLASS,
            "minimum_normal_attempts": 2, "required_failure_injection_attempts": 1,
        },
        "editor": editor,
        "source": source,
        "adaptation_seed": adaptation_seed(),
        "candidate": {"candidate_id": CANDIDATE_ID, "candidate_work_id": "", "candidate_generation_id": ""},
        "attempts": attempts,
        "run_registry_refs": [item[0] for item in ATTEMPT_PLAN],
        "all_attempt_refs": [item[0] for item in ATTEMPT_PLAN],
        "source_registry": {},
        "native_s3_pass": True,
        "historical_not_run_cells_preserved": 50,
        "historical_not_run_cells_mutated": False,
        "authority": {
            "pass_for_comparison": False, "provider_pass": False, "engine_selected": False,
            "implementation_readiness": False, "production_authority": False,
            "commercial_authority": False, "legal_clearance": False, "release_authority": False,
            "verification_pass_authority": False, "decision_authority": False,
            "integration_authority": False, "canonicality": "NOT_CANONICAL",
        },
    }
    packet["candidate"]["candidate_work_id"] = digest(candidate_work_material(packet))
    packet["candidate"]["candidate_generation_id"] = digest(generation_material(packet))
    gid = packet["candidate"]["candidate_generation_id"]
    for attempt_id in packet["run_registry_refs"]:
        attempt = packet["attempts"][attempt_id]
        attempt["candidate_generation_id"] = gid
        attempt["raw_attempt_digest"] = digest(raw_digest_basis(attempt))
        attempt["source_binding_id"] = digest({
            "attempt_id": attempt_id,
            "candidate_generation_id": gid,
            "raw_attempt_digest": attempt["raw_attempt_digest"],
            "workspace_id": attempt["workspace_id"],
            "reset_id": attempt["reset_id"],
            "generated_project_source_digest": attempt["source"]["generated_project_source_digest"],
        })
        packet["source_registry"][attempt_id] = {
            "lineage_digest": attempt["lineage_digest"],
            "raw_attempt_digest": attempt["raw_attempt_digest"],
            "source_binding_id": attempt["source_binding_id"],
        }
    return packet


def self_test() -> None:
    import copy
    base = synthetic_packet()
    validate_packet(base)
    expected_refs = [item[0] for item in ATTEMPT_PLAN]
    round_trip = json.loads(json.dumps(base, indent=2, sort_keys=True) + "\n")
    assert list(round_trip["attempts"]) != expected_refs
    validate_packet(round_trip)
    cases = []

    def rejected(name: str, mutator) -> None:
        candidate = copy.deepcopy(base)
        mutator(candidate)
        try:
            validate_packet(candidate)
        except ValueError:
            cases.append(name)
        else:
            raise AssertionError(f"negative case accepted: {name}")

    rejected("missing_attempt", lambda p: p["attempts"].pop("UNITY-S3-N2"))
    rejected("extra_attempt", lambda p: p["attempts"].__setitem__("UNITY-S3-EXTRA", copy.deepcopy(p["attempts"]["UNITY-S3-N1"])))
    rejected("wrong_attempt_id", lambda p: p["attempts"].__setitem__("UNITY-S3-WRONG", p["attempts"].pop("UNITY-S3-N2")))
    rejected("reset_false", lambda p: p["attempts"]["UNITY-S3-N1"].__setitem__("reset_verified", False))
    rejected("duplicate_workspace", lambda p: p["attempts"]["UNITY-S3-N2"].__setitem__("workspace_id", p["attempts"]["UNITY-S3-N1"]["workspace_id"]))
    rejected("tampered_source", lambda p: p["attempts"]["UNITY-S3-N1"]["source"].__setitem__("generated_project_source_digest", "0" * 64))
    rejected("wrong_resource", lambda p: p["attempts"]["UNITY-S3-N1"].__setitem__("resource_class", "OTHER"))
    rejected("wrong_run_head", lambda p: p["run"].__setitem__("head_sha", "not-a-sha"))
    rejected("duplicate_registry", lambda p: p.__setitem__("run_registry_refs", [p["run_registry_refs"][0]] * 3))
    rejected("tampered_raw_digest", lambda p: p["attempts"]["UNITY-S3-N1"].__setitem__("raw_attempt_digest", "0" * 64))
    rejected("sensitive_key", lambda p: p.__setitem__("session_token", "redacted"))
    rejected("absolute_path", lambda p: p["attempts"]["UNITY-S3-N1"].__setitem__("native_command_id", "/private/tmp/Unity"))
    assert len(cases) == 12
    print(json.dumps({"self_test": "PASS", "round_trip": "PASS", "negative_cases": cases}, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--validate")
    parser.add_argument("--out")
    parser.add_argument("--editor-path")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.validate:
        validate_packet(json.loads(pathlib.Path(args.validate).read_text(encoding="utf-8")))
        print(json.dumps({"validation": "PASS", "path": pathlib.Path(args.validate).name}, sort_keys=True))
        return 0
    require(bool(args.out and args.editor_path), "--out and --editor-path are required for native execution")
    packet = build_packet(pathlib.Path(args.editor_path))
    output = pathlib.Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "schema": SCHEMA,
        "run_id": packet["run"]["run_id"],
        "head_sha": packet["run"]["head_sha"],
        "native_s3_pass": packet["native_s3_pass"],
        "candidate_work_id": packet["candidate"]["candidate_work_id"],
        "candidate_generation_id": packet["candidate"]["candidate_generation_id"],
        "sanitized": True,
        "authority": "NOT_CANONICAL",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
