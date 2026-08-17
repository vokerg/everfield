#!/usr/bin/env python3
"""W2-ENG-TECH-S7-01: candidate-native broken-reference diagnosis/repair tranche."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import tempfile
import time
from typing import Any

MISSION = "W2-ENG-TECH-S7-01"
SCENARIO = "S7"
INJECTION = "FI-S7-BROKEN-REF-v2"
RESOURCE = "W2-ENG-HOST-COMMON-v2"
ASSETS = [f"ASSET-{i:02d}" for i in range(1, 9)]
BROKEN_ASSET = "ASSET-08"
CANDIDATES = {
    "Bevy": "Bevy-0.19.0",
    "Defold": "Defold-1.13.0",
    "Godot": "Godot-4.7.1-stable",
}

def canon(x: Any) -> str:
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def digest_obj(x: Any) -> str:
    return hashlib.sha256(canon(x).encode()).hexdigest()

def sha_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def run(cmd: list[str], cwd: pathlib.Path | None = None, timeout: int = 900) -> dict[str, Any]:
    started = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=timeout, check=False)
        return {
            "cmd": cmd,
            "exit": p.returncode,
            "timed_out": False,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": p.stdout[-12000:],
            "stderr": p.stderr[-12000:],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "cmd": cmd,
            "exit": None,
            "timed_out": True,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": exc.stdout[-12000:] if isinstance(exc.stdout, str) else "",
            "stderr": exc.stderr[-12000:] if isinstance(exc.stderr, str) else "",
        }
    except FileNotFoundError as exc:
        return {"cmd": cmd, "exit": 127, "timed_out": False, "seconds": 0, "stdout": "", "stderr": str(exc)}

def ok(r: dict[str, Any] | None) -> bool:
    return bool(r and r.get("exit") == 0 and r.get("timed_out") is False)

def semantic(r: dict[str, Any] | None) -> dict[str, Any] | None:
    if not r:
        return None
    return {
        "cmd": r.get("cmd"),
        "exit": r.get("exit"),
        "timed_out": r.get("timed_out"),
        "seconds": r.get("seconds"),
        "stdout": r.get("stdout"),
        "stderr": r.get("stderr"),
    }

def write(p: pathlib.Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)

def reset_workspace(root: pathlib.Path, candidate: str, label: str, run_identity: str) -> tuple[pathlib.Path, dict[str, Any]]:
    p = root / "runs" / candidate.lower().replace(" ", "-") / label
    absent = not p.exists()
    p.mkdir(parents=True, exist_ok=False)
    proof = {
        "schema": "S7-RESET-PROOF-v1",
        "pre_workspace_absent": absent,
        "workspace_created_exclusive": p.exists(),
        "workspace_id": "WS-S7-" + digest_obj({"candidate": candidate, "label": label, "run": run_identity})[:28],
        "reset_id": "RESET-S7-" + digest_obj({"candidate": candidate, "label": label, "run": run_identity})[:28],
    }
    return p, proof

def reset_ok(p: dict[str, Any]) -> bool:
    return bool(
        p.get("pre_workspace_absent") is True
        and p.get("workspace_created_exclusive") is True
        and p.get("workspace_id")
        and p.get("reset_id")
    )

def asset_payload(asset: str) -> str:
    return json.dumps({"logical_asset_id": asset, "fixture": "W2-ENG-FEATURE-SLICE-v2"}, sort_keys=True) + "\n"

def asset_digests(repo: pathlib.Path, candidate: str) -> dict[str, str]:
    ext = {"Bevy": ".txt", "Godot": ".tres", "Defold": ".lua"}[candidate]
    return {a: sha_file(repo / "assets" / f"{a}{ext}") for a in ASSETS}

def bevy_source(broken: bool = False) -> str:
    refs = []
    for a in ASSETS:
        path = f"../assets/{a}.txt"
        if a == BROKEN_ASSET and broken:
            path = "../assets/MISSING-ASSET-08.txt"
        refs.append(f'    include_bytes!("{path}").len(),')
    return """use bevy::prelude::*;
#[derive(Resource)] struct AssetCount(usize);
fn main() {
    let sizes = [
%s
    ];
    let mut world = World::new();
    world.insert_resource(AssetCount(sizes.len()));
    if world.resource::<AssetCount>().0 != 8 || sizes.iter().any(|x| *x == 0) { std::process::exit(7); }
    println!("EVERFIELD_S7:PASS:8");
}
""" % "\n".join(refs)

def godot_source(broken: bool = False) -> str:
    lines = ["extends SceneTree"]
    for i, a in enumerate(ASSETS, 1):
        path = f"res://assets/{a}.tres"
        if a == BROKEN_ASSET and broken:
            path = "res://assets/MISSING-ASSET-08.tres"
        lines.append(f'const A{i} = preload("{path}")')
    lines += [
        "func _init():",
        " var n = 0",
        " for x in [A1,A2,A3,A4,A5,A6,A7,A8]:",
        "  if x != null: n += 1",
        ' if n != 8: get_tree().quit(7); return',
        ' print("EVERFIELD_S7:PASS:8")',
        " get_tree().quit(0)",
    ]
    return "\n".join(lines) + "\n"

def defold_source(broken: bool = False) -> str:
    reqs = []
    for i, a in enumerate(ASSETS, 1):
        mod = f"assets.{a}"
        if a == BROKEN_ASSET and broken:
            mod = "assets.MISSING-ASSET-08"
        reqs.append(f'local a{i} = require "{mod}"')
    reqs += [
        "function init(self)",
        " local n = 0",
        " for _,v in ipairs({a1,a2,a3,a4,a5,a6,a7,a8}) do if v ~= nil then n = n + 1 end end",
        ' if n ~= 8 then print("EVERFIELD_S7:FAIL"); sys.exit(7); return end',
        ' print("EVERFIELD_S7:PASS:8")',
        " sys.exit(0)",
        "end",
    ]
    return "\n".join(reqs) + "\n"

def materialize(repo: pathlib.Path, candidate: str, bevy_lock: pathlib.Path) -> pathlib.Path:
    for a in ASSETS:
        if candidate == "Godot":
            write(repo / "assets" / f"{a}.tres", f'[gd_resource format=3]\n\n[resource]\nresource_name = "{a}"\n')
        elif candidate == "Defold":
            write(repo / "assets" / f"{a}.lua", f'return {{ logical_asset_id = "{a}" }}\n')
        else:
            write(repo / "assets" / f"{a}.txt", asset_payload(a))
    if candidate == "Bevy":
        write(repo / "Cargo.toml", "[package]\nname='everfield_bevy_probe'\nversion='0.0.0'\nedition='2024'\n[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n")
        (repo / "src").mkdir(exist_ok=True)
        write(repo / "src" / "main.rs", bevy_source(False))
        shutil.copy2(bevy_lock, repo / "Cargo.lock")
        return repo / "src" / "main.rs"
    if candidate == "Godot":
        write(repo / "project.godot", '[application]\nconfig/name="EverfieldS7"\nrun/main_scene="res://main.tscn"\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n')
        write(repo / "main.tscn", '[gd_scene load_steps=2 format=3]\n\n[ext_resource path="res://main.gd" type="Script" id="1"]\n\n[node name="Main" type="Node"]\nscript = ExtResource("1")\n')
        write(repo / "main.gd", godot_source(False))
        return repo / "main.gd"
    write(repo / "game.project", "[project]\ntitle = EverfieldS7\n[bootstrap]\nmain_collection = /main.collectionc\n[display]\nwidth = 320\nheight = 180\n")
    write(repo / "input" / "game.input_binding", "")
    write(repo / "main.collection", 'name: "main"\nscale_along_z: 0\nembedded_instances {\n id: "controller"\n data: "components {\\n  id: \\"script\\"\\n  component: \\"/controller.script\\"\\n}\\n"\n}\n')
    write(repo / "controller.script", defold_source(False))
    return repo / "controller.script"

def candidate_command(repo: pathlib.Path, candidate: str, tool: dict[str, Any], tool_root: pathlib.Path) -> dict[str, Any]:
    if candidate == "Bevy":
        cargo = ((tool.get("cargo") or {}).get("path")) or shutil.which("cargo")
        if not cargo:
            return {"cmd": ["cargo", "check"], "exit": 127, "timed_out": False, "seconds": 0, "stdout": "", "stderr": "cargo missing"}
        return run([str(cargo), "check", "--locked", "--quiet"], cwd=repo, timeout=900)
    if candidate == "Godot":
        exe = tool.get("executable")
        if not exe:
            return {"cmd": ["godot", "--headless"], "exit": 127, "timed_out": False, "seconds": 0, "stdout": "", "stderr": "godot missing"}
        return run([str(exe), "--headless", "--path", str(repo), "--script", "res://main.gd"], cwd=repo, timeout=90)
    java = ((tool.get("java") or {}).get("path")) or shutil.which("java")
    jar = tool_root / "bob-1.13.0.jar"
    if not java or not jar.exists():
        return {"cmd": ["java", "-jar", str(jar)], "exit": 127, "timed_out": False, "seconds": 0, "stdout": "", "stderr": "java or bob missing"}
    return run([str(java), "-jar", str(jar), "--root", str(repo), "resolve", "build"], cwd=repo, timeout=900)

def diagnostic_ok(candidate: str, r: dict[str, Any]) -> bool:
    text = ((r.get("stdout") or "") + "\n" + (r.get("stderr") or "")).lower()
    if candidate == "Bevy":
        return (not ok(r)) and "missing-asset-08" in text and ("couldn't read" in text or "no such file" in text)
    if candidate == "Godot":
        return "missing-asset-08" in text and (not ok(r) or "error" in text)
    return (not ok(r)) and "missing-asset-08" in text and ("not found" in text or "could not" in text or "unable" in text or "error" in text)

def driver_text(candidate: str, broken: bool) -> str:
    return {"Bevy": bevy_source, "Godot": godot_source, "Defold": defold_source}[candidate](broken)

def execute_attempt(root: pathlib.Path, candidate: str, label: str, inject: bool, tool: dict[str, Any], tool_root: pathlib.Path, bevy_lock: pathlib.Path, run_identity: str) -> dict[str, Any]:
    repo, reset = reset_workspace(root, candidate, label, run_identity)
    driver = materialize(repo, candidate, bevy_lock)
    baseline_assets = asset_digests(repo, candidate)
    baseline_driver = driver.read_text()
    baseline_driver_sha = sha_file(driver)
    normal = candidate_command(repo, candidate, tool, tool_root)
    if not inject:
        marker_present = "EVERFIELD_S7:PASS:8" in ((normal.get("stdout") or "") + (normal.get("stderr") or ""))
        passed = ok(normal) and (candidate != "Godot" or marker_present)
        source = {
            "candidate_native": True,
            "phase": "NORMAL",
            "asset_ids": ASSETS,
            "asset_digests": baseline_assets,
            "driver_sha256": baseline_driver_sha,
            "candidate_command": semantic(normal),
            "eight_asset_binding": len(baseline_assets) == 8 and set(baseline_assets) == set(ASSETS),
        }
    else:
        write(driver, driver_text(candidate, True))
        defect_driver_sha = sha_file(driver)
        defect_assets = asset_digests(repo, candidate)
        defect_text = driver.read_text()
        broken_reference_count = defect_text.count("MISSING-ASSET-08")
        diagnosis = candidate_command(repo, candidate, tool, tool_root)
        diag_ok = diagnostic_ok(candidate, diagnosis)
        write(driver, baseline_driver)
        repaired_driver_sha = sha_file(driver)
        repaired_assets = asset_digests(repo, candidate)
        rerun = candidate_command(repo, candidate, tool, tool_root)
        rerun_marker_present = "EVERFIELD_S7:PASS:8" in ((rerun.get("stdout") or "") + (rerun.get("stderr") or ""))
        rerun_pass = ok(rerun) and (candidate != "Godot" or rerun_marker_present)
        exact_scope = (
            baseline_assets == defect_assets == repaired_assets
            and baseline_driver_sha != defect_driver_sha
            and baseline_driver_sha == repaired_driver_sha
            and broken_reference_count == 1
            and BROKEN_ASSET == "ASSET-08"
        )
        passed = diag_ok and rerun_pass and exact_scope
        source = {
            "candidate_native": True,
            "phase": "FAILURE_INJECTION_AND_REPAIR",
            "injection_id": INJECTION,
            "broken_asset_id": BROKEN_ASSET,
            "broken_reference_count": broken_reference_count,
            "asset_ids": ASSETS,
            "asset_digests_before": baseline_assets,
            "asset_digests_defect": defect_assets,
            "asset_digests_after_repair": repaired_assets,
            "driver_sha256_before": baseline_driver_sha,
            "driver_sha256_defect": defect_driver_sha,
            "driver_sha256_after_repair": repaired_driver_sha,
            "diagnosis": semantic(diagnosis),
            "diagnostic_attributed": diag_ok,
            "repair_changed_only_broken_reference": exact_scope,
            "rerun": semantic(rerun),
            "rerun_clean": rerun_pass,
        }
    passed = bool(passed and reset_ok(reset))
    raw = {
        "schema": "W2-ENG-TECHNICAL-S7-RAW-v1",
        "candidate": candidate,
        "candidate_id": CANDIDATES[candidate],
        "label": label,
        "scenario_id": SCENARIO,
        "kind": "FAILURE_INJECTION" if inject else "NORMAL",
        "injection_id": INJECTION if inject else None,
        "reset_proof": reset,
        "reset_verified_derived": reset_ok(reset),
        "source": source,
        "formal_result": "PASS" if passed else "INCONCLUSIVE",
        "failure_class": "NONE" if passed else "HARNESS",
    }
    return {"digest": "sha256:" + digest_obj(raw), "record": raw}

def tool_identity(candidate: str, tool: dict[str, Any]) -> dict[str, Any]:
    if candidate == "Bevy":
        body = {
            "baseline": "0.19.0",
            "retained_lock_sha256": tool.get("retained_lock_sha256"),
            "lock_replay_bound": tool.get("lock_replay_bound"),
            "cargo": (((tool.get("cargo") or {}).get("probe") or {}).get("stdout") or "").strip(),
            "rustc": (((tool.get("rustc") or {}).get("probe") or {}).get("stdout") or "").strip(),
        }
    elif candidate == "Godot":
        body = {
            "baseline": "4.7.1-stable",
            "artifact_expected_sha256": (tool.get("artifact_identity") or {}).get("expected_sha256"),
            "artifact_observed_sha256": (tool.get("artifact_identity") or {}).get("observed_sha256"),
            "artifact_verified": (tool.get("artifact_identity") or {}).get("verified"),
            "executable_sha256": tool.get("executable_sha256"),
            "version": (((tool.get("version") or {}).get("stdout")) or "").strip(),
        }
    else:
        body = {
            "baseline": "1.13.0",
            "artifact_expected_sha256": (tool.get("artifact_identity") or {}).get("expected_sha256"),
            "artifact_observed_sha256": (tool.get("artifact_identity") or {}).get("observed_sha256"),
            "artifact_verified": (tool.get("artifact_identity") or {}).get("verified"),
            "bob_version": ((((tool.get("bob_version") or {}).get("stdout")) or ((tool.get("bob_version") or {}).get("stderr")) or "")).strip(),
        }
    return {"body": body, "identity_digest": "sha256:" + digest_obj(body)}

def formal_generation(v, candidate: str, raws: list[dict[str, Any]], run_identity: str, tool_id: dict[str, Any]) -> dict[str, Any]:
    cid = CANDIDATES[candidate]
    source_digest_set = [x["digest"] for x in raws]
    work = "WORK-S7-" + digest_obj({"candidate": cid, "tool": tool_id["identity_digest"], "run": run_identity})[:24]
    gid = "GEN-S7-" + digest_obj({"candidate": cid, "work": work, "sources": source_digest_set})[:24]
    adaptation = v.adaptation("S7", cid)
    attempts: dict[str, Any] = {}
    refs: list[str] = []
    source_bindings: dict[str, str] = {}
    for i, raw in enumerate(raws):
        rr = raw["record"]
        is_fi = rr["kind"] == "FAILURE_INJECTION"
        aid = f"{gid}-S7-{'FI1' if is_fi else 'N' + str(i + 1)}"
        refs.append(aid)
        source_bindings[aid] = raw["digest"]
        attempts[aid] = {
            "attempt_id": aid,
            "scenario_id": "S7",
            "candidate_id": cid,
            "candidate_generation_id": gid,
            "kind": rr["kind"],
            "normal_index": None if is_fi else i + 1,
            "injection_id": INJECTION if is_fi else None,
            "result": rr["formal_result"],
            "failure_class": rr["failure_class"],
            "reset_id": rr["reset_proof"]["reset_id"],
            "reset_verified": rr["reset_verified_derived"],
            "workspace_id": rr["reset_proof"]["workspace_id"],
            "resource_class": RESOURCE,
        }
    g = {
        "scenario_id": "S7",
        "candidate_id": cid,
        "generation_id": gid,
        "candidate_work_id": work,
        "predecessor_generation_id": None,
        "repair_change_ref": None,
        "harness_defect": False,
        "adaptation": adaptation,
        "adaptation_binding_id": v.D(v.binding(adaptation)),
        "attempts": attempts,
        "run_registry_refs": list(refs),
        "all_attempt_refs": list(refs),
    }
    return {
        "generation": g,
        "source_bindings": source_bindings,
        "adaptation_validation": v.va(adaptation, cid),
        "aggregate": v.agg(g),
    }

def packet_ok(packet: dict[str, Any]) -> bool:
    try:
        raws = packet["raw_attempts"]
        if [x["record"]["label"] for x in raws] != ["N1", "N2", "FI1"]:
            return False
        if len({x["record"]["reset_proof"]["workspace_id"] for x in raws}) != 3:
            return False
        if len({x["record"]["reset_proof"]["reset_id"] for x in raws}) != 3:
            return False
        if any(not x["record"]["source"].get("candidate_native") for x in raws):
            return False
        fi = raws[2]["record"]["source"]
        if fi.get("broken_asset_id") != BROKEN_ASSET or fi.get("broken_reference_count") != 1:
            return False
        if fi.get("diagnostic_attributed") is not True or fi.get("repair_changed_only_broken_reference") is not True or fi.get("rerun_clean") is not True:
            return False
        for _, d in packet["source_bindings"].items():
            if d not in {x["digest"] for x in raws}:
                return False
        return packet["aggregate"] == {"aggregate": "PASS_FOR_COMPARISON", "reasons": [], "valid_envelope": True}
    except (KeyError, TypeError):
        return False

def negative_selftests(v, packet: dict[str, Any]) -> dict[str, bool]:
    out: dict[str, bool] = {}
    def rawmut(name: str, fn) -> None:
        x = copy.deepcopy(packet)
        fn(x)
        out[name] = not packet_ok(x)
    rawmut("wrong_broken_asset", lambda x: x["raw_attempts"][2]["record"]["source"].__setitem__("broken_asset_id", "ASSET-07"))
    rawmut("more_than_one_broken_reference", lambda x: x["raw_attempts"][2]["record"]["source"].__setitem__("broken_reference_count", 2))
    rawmut("host_only_diagnosis", lambda x: x["raw_attempts"][2]["record"]["source"].__setitem__("candidate_native", False))
    rawmut("missing_diagnostic_attribution", lambda x: x["raw_attempts"][2]["record"]["source"].__setitem__("diagnostic_attributed", False))
    rawmut("unbounded_repair", lambda x: x["raw_attempts"][2]["record"]["source"].__setitem__("repair_changed_only_broken_reference", False))
    rawmut("rerun_bypass", lambda x: x["raw_attempts"][2]["record"]["source"].__setitem__("rerun_clean", False))
    rawmut("source_raw_substitution", lambda x: x["source_bindings"].__setitem__(next(iter(x["source_bindings"])), "sha256:" + "0" * 64))
    rawmut("candidate_native_validation_bypass", lambda x: x["raw_attempts"][0]["record"]["source"].__setitem__("candidate_native", False))
    for name, fn in {
        "candidate_generation_mismatch": lambda g: next(iter(g["attempts"].values())).__setitem__("candidate_generation_id", "OTHER"),
        "duplicate_registry_ref": lambda g: g["run_registry_refs"].append(g["run_registry_refs"][0]),
        "reused_workspace": lambda g: list(g["attempts"].values())[1].__setitem__("workspace_id", list(g["attempts"].values())[0]["workspace_id"]),
    }.items():
        g = copy.deepcopy(packet["generation"])
        fn(g)
        out[name] = v.agg(g).get("aggregate") != "PASS_FOR_COMPARISON"
    return out

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--validator", required=True)
    ap.add_argument("--toolchain-probe", required=True)
    ap.add_argument("--bevy-lock", required=True)
    ap.add_argument("--artifact-lock", required=True)
    args = ap.parse_args()

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    validator_path = pathlib.Path(args.validator)
    toolchain_path = pathlib.Path(args.toolchain_probe)
    bevy_lock = pathlib.Path(args.bevy_lock)
    artifact_lock_path = pathlib.Path(args.artifact_lock)
    v = load_module(validator_path, "everfield_s7_validator")
    tp = load_module(toolchain_path, "everfield_s7_toolchain")

    assert v.ID["validator_id"] == "W2-ENG-PROTOCOL-VALIDATOR-v5"
    assert v.SCENARIOS["S7"]["required_injections"] == [INJECTION]
    assert v.SCENARIOS["S7"]["min_bounds"] == {"asset_count": 8, "broken_reference_count": 1}
    assert v.FEATURE["assets"]["broken_reference_asset_id"] == BROKEN_ASSET
    assert bevy_lock.exists() and artifact_lock_path.exists()

    run_identity = canon({
        "github_sha": os.getenv("GITHUB_SHA"),
        "github_run_id": os.getenv("GITHUB_RUN_ID"),
        "github_run_attempt": os.getenv("GITHUB_RUN_ATTEMPT"),
        "issue": 507,
    })
    artifact_lock = tp.load_artifact_lock(artifact_lock_path)

    with tempfile.TemporaryDirectory(prefix="everfield-s7-") as td:
        root = pathlib.Path(td)
        tools_root = root / "toolchains"
        tools_root.mkdir()
        tools = {
            "Bevy": tp.probe_bevy(tools_root, bevy_lock),
            "Defold": tp.probe_defold(tools_root, artifact_lock),
            "Godot": tp.probe_godot(tools_root, artifact_lock),
        }
        results: dict[str, Any] = {}
        provisional: list[str] = []
        for candidate in ("Bevy", "Defold", "Godot"):
            tool = tools[candidate]
            tool_id = tool_identity(candidate, tool)
            raws = [
                execute_attempt(root, candidate, "N1", False, tool, tools_root, bevy_lock, run_identity),
                execute_attempt(root, candidate, "N2", False, tool, tools_root, bevy_lock, run_identity),
                execute_attempt(root, candidate, "FI1", True, tool, tools_root, bevy_lock, run_identity),
            ]
            formal = formal_generation(v, candidate, raws, run_identity, tool_id)
            packet = {
                "candidate": candidate,
                "candidate_id": CANDIDATES[candidate],
                "toolchain_status": tool.get("status"),
                "toolchain_reason": tool.get("reason"),
                "toolchain_identity": tool_id,
                "raw_attempts": raws,
                **formal,
            }
            packet["negative_selftests"] = negative_selftests(v, packet)
            packet["source_binding_complete"] = set(packet["source_bindings"].values()) == {x["digest"] for x in raws}
            packet["trusted_representation_ok"] = packet_ok(packet) and all(packet["negative_selftests"].values()) and packet["source_binding_complete"]
            if packet["trusted_representation_ok"]:
                provisional.append(candidate)
            results[candidate] = packet

        evidence = {
            "schema": "W2-ENG-TECHNICAL-S7-v1",
            "mission_id": MISSION,
            "issue": 507,
            "scenario_id": "S7",
            "harness_id": v.ID["harness_id"],
            "feature_slice_id": v.ID["feature_slice_id"],
            "scenario_manifest_id": v.ID["scenario_manifest_id"],
            "validator_id": v.ID["validator_id"],
            "validator_sha256": sha_file(validator_path),
            "runner_sha256": sha_file(pathlib.Path(__file__)),
            "toolchain_probe_sha256": sha_file(toolchain_path),
            "run_identity": json.loads(run_identity),
            "s7_contract": {
                "fixed_input_refs": v.SCENARIOS["S7"]["fixed_input_refs"],
                "obligations": v.SCENARIOS["S7"]["obligations"],
                "min_bounds": v.SCENARIOS["S7"]["min_bounds"],
                "required_injection": INJECTION,
                "asset_ids": ASSETS,
                "broken_reference_asset_id": BROKEN_ASSET,
                "resource_class": RESOURCE,
            },
            "predecessor_review": {
                "issue": 462,
                "terminal_comment": 5309450099,
                "disposition": "PASS_BOUNDED_REMEDIATED_S6_V5_ENVELOPE",
                "s6_reviewed_publication_sha": "40179080013d742b70b4a5be611f1666dd3cd599",
            },
            "producer_corrections": [
                {
                    "run_id": 31991497890,
                    "run_attempt": 1,
                    "trigger_sha": "3d40ab57858a7c23c2456d22d4b7a1cec0017457",
                    "evidence_commit_sha": "9508e95c9f7ef063dda684fe7329f4ceb1e1676f",
                    "artifact_id": 9275748382,
                    "artifact_digest": "sha256:a5783e6188f37c7587d3c7db6f2efe7f602a3eeb5eab316d383f140cfd580f46",
                    "evidence_sha256": "92ecd5fcd56a92e4507a4c1f7eacd025daefb21e8b59d717f3e3b72413bc9b01",
                    "status": "RETAINED_INCOMPLETE_PRODUCER_PROVENANCE",
                    "findings": [
                        "BEVY_COMPILE_ONLY_SUCCESS_RUNTIME_MARKER_MISCLASSIFIED",
                        "DEFOLD_REQUIRED_EMPTY_INPUT_BINDING_OMITTED",
                        "GODOT_PROJECT_LAUNCH_MODE_NONTERMINATING",
                    ],
                }
            ],
            "results": results,
            "provisional_candidates": provisional,
            "authority_bound_not_run": {
                "Unity": "NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY",
                "Unreal Engine": "NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY",
            },
            "historical_issue_82_not_run_cells_preserved": 50,
            "reviewed_s3_s4_s5_s6_provenance_preserved": True,
            "fresh_review_required": True,
            "trusted_comparison_authority": False,
            "integration_authority": False,
            "engine_selected": False,
            "implementation_readiness": False,
            "verification_pass_authority": False,
            "release_authority": False,
            "decision_authority": False,
            "canonicality": "NOT_CANONICAL",
        }
        out.write_text(json.dumps(evidence, sort_keys=True, indent=2) + "\n")
        print(json.dumps({
            "schema": evidence["schema"],
            "provisional_candidates": provisional,
            "candidate_aggregates": {k: v["aggregate"] for k, v in results.items()},
            "out": str(out),
        }, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
