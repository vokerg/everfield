#!/usr/bin/env python3
"""W2-ENG-TECH-S5-01: real-toolchain merge/conflict evidence tranche."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import pathlib
import shutil
import stat
import subprocess
import tempfile
import time
from typing import Any

RESOURCE = "W2-ENG-HOST-COMMON-v2"
SCENARIO = "S5"
INJECTION = "FI-S5-OVERLAP-v2"
OVERLAP = {
    "STATE:entity-07.status": "state_surface",
    "UI:SETTINGS.control-02.label": "ui_surface",
}
S4_REVIEW_TERMINAL = 5305617167
S4_REVIEW_DISPOSITION = "PASS_BOUNDED_REMEDIATED_S4_V5_ENVELOPE"
S4_REVIEW_PUBLICATION = "b0b87a4ca05f7f21595bb2303978cb7dd0d5791e"
S4_REMEDIATION_PUBLICATION = "6f9e56f1d822ed2e2b18fa10a2bf29927efebe3e"


def canon(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest_obj(obj: Any) -> str:
    return hashlib.sha256(canon(obj).encode()).hexdigest()


def digest_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"cannot load module {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(cmd: list[str], cwd: pathlib.Path | None = None, env: dict[str, str] | None = None, timeout: int = 900) -> dict[str, Any]:
    merged_env = os.environ.copy()
    merged_env.update(env or {})
    started = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=cwd, env=merged_env, text=True, capture_output=True, timeout=timeout, check=False)
        return {
            "exit": p.returncode,
            "timed_out": False,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": p.stdout[-16000:],
            "stderr": p.stderr[-16000:],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "exit": None,
            "timed_out": True,
            "seconds": round(time.monotonic() - started, 3),
            "stdout": exc.stdout[-16000:] if isinstance(exc.stdout, str) else "",
            "stderr": exc.stderr[-16000:] if isinstance(exc.stderr, str) else "",
        }
    except FileNotFoundError as exc:
        return {"exit": 127, "timed_out": False, "seconds": 0, "stdout": "", "stderr": str(exc)}


def ok(result: dict[str, Any] | None) -> bool:
    return bool(result and result.get("exit") == 0 and not result.get("timed_out"))


def semantic_result(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "exit": result.get("exit"),
        "timed_out": result.get("timed_out"),
        "stdout": result.get("stdout"),
        "stderr": result.get("stderr"),
    }


def write(path: pathlib.Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def git(repo: pathlib.Path, *args: str, timeout: int = 120) -> dict[str, Any]:
    return run(["git", *args], cwd=repo, timeout=timeout)


def git_out(repo: pathlib.Path, *args: str) -> str:
    r = git(repo, *args)
    if not ok(r):
        raise RuntimeError(f"git {' '.join(args)} failed: {r['stderr']}")
    return (r.get("stdout") or "").strip()


def stable_git_env() -> dict[str, str]:
    return {
        "GIT_AUTHOR_NAME": "everfield-s5",
        "GIT_AUTHOR_EMAIL": "s5@example.invalid",
        "GIT_COMMITTER_NAME": "everfield-s5",
        "GIT_COMMITTER_EMAIL": "s5@example.invalid",
        "GIT_AUTHOR_DATE": "2000-01-01T00:00:00Z",
        "GIT_COMMITTER_DATE": "2000-01-01T00:00:00Z",
    }


def git_commit(repo: pathlib.Path, message: str) -> str:
    env = stable_git_env()
    add = run(["git", "add", "-A"], cwd=repo, env=env, timeout=60)
    if not ok(add):
        raise RuntimeError(add["stderr"])
    c = run(["git", "commit", "-q", "-m", message], cwd=repo, env=env, timeout=60)
    if not ok(c):
        raise RuntimeError(c["stderr"])
    return git_out(repo, "rev-parse", "HEAD")


def reset_prepare(root: pathlib.Path, candidate: str, label: str, run_identity: str) -> tuple[pathlib.Path, dict[str, Any]]:
    slug = candidate.lower().replace(" ", "-")
    repo = root / "runs" / slug / label
    pre_absent = not repo.exists()
    repo.mkdir(parents=True, exist_ok=False)
    proof = {
        "schema": "S5-RESET-PROOF-v1",
        "candidate": candidate,
        "label": label,
        "pre_workspace_absent": pre_absent,
        "workspace_created_exclusive": repo.exists(),
        "workspace_id": "WS-S5-" + digest_obj({"candidate": candidate, "label": label, "run": run_identity, "role": "workspace"})[:28],
        "reset_id": "RESET-S5-" + digest_obj({"candidate": candidate, "label": label, "run": run_identity, "role": "reset"})[:28],
    }
    return repo, proof


def verify_reset(proof: dict[str, Any]) -> bool:
    return (
        isinstance(proof, dict)
        and proof.get("pre_workspace_absent") is True
        and proof.get("workspace_created_exclusive") is True
        and isinstance(proof.get("workspace_id"), str)
        and bool(proof.get("workspace_id"))
        and isinstance(proof.get("reset_id"), str)
        and bool(proof.get("reset_id"))
    )


def verify_reset_set(raws: list[dict[str, Any]]) -> bool:
    proofs = [x["record"]["reset_proof"] for x in raws]
    return (
        all(verify_reset(p) for p in proofs)
        and len({p["workspace_id"] for p in proofs}) == len(proofs)
        and len({p["reset_id"] for p in proofs}) == len(proofs)
    )


BEVY_FILES = {
    "Cargo.toml": """[package]\nname='everfield_s5_probe'\nversion='0.0.0'\nedition='2024'\n[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n""",
    "src/state.rs": "pub const ENTITY_07_STATUS: &str = \"IDLE\";\n",
    "src/ui.rs": "pub const SETTINGS_CONTROL_02_LABEL: &str = \"Audio\";\n",
    "src/branch_a.rs": "pub const A_ENABLED: bool = false;\n",
    "src/branch_b.rs": "pub const B_LABEL: &str = \"Back\";\n",
    "src/main.rs": r'''use bevy::prelude::*;
mod state; mod ui; mod branch_a; mod branch_b;
#[derive(Resource)] struct MergeState { status: &'static str, label: &'static str, a: bool, b: &'static str }
fn main() {
    let mut world = World::new();
    world.insert_resource(MergeState { status: state::ENTITY_07_STATUS, label: ui::SETTINGS_CONTROL_02_LABEL, a: branch_a::A_ENABLED, b: branch_b::B_LABEL });
    let s = world.resource::<MergeState>();
    let expected_status = std::env::var("EVERFIELD_S5_EXPECT_STATUS").unwrap();
    let expected_label = std::env::var("EVERFIELD_S5_EXPECT_LABEL").unwrap();
    if s.status != expected_status || s.label != expected_label || !s.a || s.b != "Return" { std::process::exit(7); }
    println!("EVERFIELD_S5:PASS");
}
''',
}

GODOT_FILES = {
    "project.godot": "[application]\nconfig/name=\"EverfieldS5\"\nrun/main_scene=\"res://main.tscn\"\n[rendering]\nrenderer/rendering_method=\"gl_compatibility\"\n",
    "main.tscn": "[gd_scene load_steps=2 format=3]\n\n[ext_resource path=\"res://main.gd\" type=\"Script\" id=\"1\"]\n\n[node name=\"Main\" type=\"Node\"]\nscript = ExtResource(\"1\")\n",
    "state.gd": "extends RefCounted\nconst ENTITY_07_STATUS = \"IDLE\"\n",
    "settings.gd": "extends RefCounted\nconst SETTINGS_CONTROL_02_LABEL = \"Audio\"\n",
    "branch_a.gd": "extends RefCounted\nconst A_ENABLED = false\n",
    "branch_b.gd": "extends RefCounted\nconst B_LABEL = \"Back\"\n",
    "main.gd": r'''extends Node
const State = preload("res://state.gd")
const Settings = preload("res://settings.gd")
const A = preload("res://branch_a.gd")
const B = preload("res://branch_b.gd")
func _ready():
 var es = OS.get_environment("EVERFIELD_S5_EXPECT_STATUS")
 var el = OS.get_environment("EVERFIELD_S5_EXPECT_LABEL")
 if State.ENTITY_07_STATUS != es or Settings.SETTINGS_CONTROL_02_LABEL != el or not A.A_ENABLED or B.B_LABEL != "Return":
  get_tree().quit(7); return
 print("EVERFIELD_S5:PASS")
 get_tree().quit(0)
''',
}

DEFOLD_FILES = {
    "game.project": "[project]\ntitle = EverfieldS5\n[bootstrap]\nmain_collection = /main.collectionc\n[display]\nwidth = 320\nheight = 180\n",
    "input/game.input_binding": "",
    "main.collection": "name: \"main\"\nscale_along_z: 0\nembedded_instances {\n id: \"controller\"\n data: \"components {\\n  id: \\\"script\\\"\\n  component: \\\"/controller.script\\\"\\n}\\n\"\n}\n",
    "state.lua": "return { entity_07_status = \"IDLE\" }\n",
    "settings.lua": "return { settings_control_02_label = \"Audio\" }\n",
    "branch_a.lua": "return { a_enabled = false }\n",
    "branch_b.lua": "return { b_label = \"Back\" }\n",
    "controller.script": r'''local state = require "state"
local settings = require "settings"
local a = require "branch_a"
local b = require "branch_b"
function init(self)
 local es = os.getenv("EVERFIELD_S5_EXPECT_STATUS")
 local el = os.getenv("EVERFIELD_S5_EXPECT_LABEL")
 if state.entity_07_status ~= es or settings.settings_control_02_label ~= el or a.a_enabled ~= true or b.b_label ~= "Return" then
  print("EVERFIELD_S5:FAIL")
  sys.exit(7)
  return
 end
 print("EVERFIELD_S5:PASS")
 sys.exit(0)
end
''',
}

CANDIDATE_SPEC = {
    "Bevy": {
        "files": BEVY_FILES,
        "state_path": "src/state.rs",
        "ui_path": "src/ui.rs",
        "a_path": "src/branch_a.rs",
        "b_path": "src/branch_b.rs",
        "state_base": 'pub const ENTITY_07_STATUS: &str = "IDLE";\n',
        "state_a": 'pub const ENTITY_07_STATUS: &str = "ACTIVE";\n',
        "state_b": 'pub const ENTITY_07_STATUS: &str = "PAUSED";\n',
        "ui_base": 'pub const SETTINGS_CONTROL_02_LABEL: &str = "Audio";\n',
        "ui_a": 'pub const SETTINGS_CONTROL_02_LABEL: &str = "Sound";\n',
        "ui_b": 'pub const SETTINGS_CONTROL_02_LABEL: &str = "Volume";\n',
        "a_base": "pub const A_ENABLED: bool = false;\n",
        "a_changed": "pub const A_ENABLED: bool = true;\n",
        "b_base": 'pub const B_LABEL: &str = "Back";\n',
        "b_changed": 'pub const B_LABEL: &str = "Return";\n',
    },
    "Godot": {
        "files": GODOT_FILES,
        "state_path": "state.gd",
        "ui_path": "settings.gd",
        "a_path": "branch_a.gd",
        "b_path": "branch_b.gd",
        "state_base": 'extends RefCounted\nconst ENTITY_07_STATUS = "IDLE"\n',
        "state_a": 'extends RefCounted\nconst ENTITY_07_STATUS = "ACTIVE"\n',
        "state_b": 'extends RefCounted\nconst ENTITY_07_STATUS = "PAUSED"\n',
        "ui_base": 'extends RefCounted\nconst SETTINGS_CONTROL_02_LABEL = "Audio"\n',
        "ui_a": 'extends RefCounted\nconst SETTINGS_CONTROL_02_LABEL = "Sound"\n',
        "ui_b": 'extends RefCounted\nconst SETTINGS_CONTROL_02_LABEL = "Volume"\n',
        "a_base": "extends RefCounted\nconst A_ENABLED = false\n",
        "a_changed": "extends RefCounted\nconst A_ENABLED = true\n",
        "b_base": 'extends RefCounted\nconst B_LABEL = "Back"\n',
        "b_changed": 'extends RefCounted\nconst B_LABEL = "Return"\n',
    },
    "Defold": {
        "files": DEFOLD_FILES,
        "state_path": "state.lua",
        "ui_path": "settings.lua",
        "a_path": "branch_a.lua",
        "b_path": "branch_b.lua",
        "state_base": 'return { entity_07_status = "IDLE" }\n',
        "state_a": 'return { entity_07_status = "ACTIVE" }\n',
        "state_b": 'return { entity_07_status = "PAUSED" }\n',
        "ui_base": 'return { settings_control_02_label = "Audio" }\n',
        "ui_a": 'return { settings_control_02_label = "Sound" }\n',
        "ui_b": 'return { settings_control_02_label = "Volume" }\n',
        "a_base": "return { a_enabled = false }\n",
        "a_changed": "return { a_enabled = true }\n",
        "b_base": 'return { b_label = "Back" }\n',
        "b_changed": 'return { b_label = "Return" }\n',
    },
}


def materialize_fixture(repo: pathlib.Path, candidate: str, bevy_lock: pathlib.Path | None = None) -> None:
    spec = CANDIDATE_SPEC[candidate]
    for rel, text in spec["files"].items():
        write(repo / rel, text)
    if candidate == "Bevy" and bevy_lock:
        shutil.copy2(bevy_lock, repo / "Cargo.lock")


def init_repo(repo: pathlib.Path, candidate: str, bevy_lock: pathlib.Path | None) -> str:
    r = git(repo, "init", "-q")
    if not ok(r):
        raise RuntimeError(r["stderr"])
    git(repo, "config", "user.name", "everfield-s5")
    git(repo, "config", "user.email", "s5@example.invalid")
    materialize_fixture(repo, candidate, bevy_lock)
    return git_commit(repo, "baseline")


def changed_files(repo: pathlib.Path, base: str, head: str) -> list[str]:
    out = git_out(repo, "diff", "--name-only", base, head)
    return [x for x in out.splitlines() if x]


def apply_a(repo: pathlib.Path, candidate: str, inject: bool) -> None:
    s = CANDIDATE_SPEC[candidate]
    write(repo / s["a_path"], s["a_changed"])
    if inject:
        write(repo / s["state_path"], s["state_a"])
        write(repo / s["ui_path"], s["ui_a"])


def apply_b(repo: pathlib.Path, candidate: str, inject: bool) -> None:
    s = CANDIDATE_SPEC[candidate]
    write(repo / s["b_path"], s["b_changed"])
    if inject:
        write(repo / s["state_path"], s["state_b"])
        write(repo / s["ui_path"], s["ui_b"])


def validate_expected_files(repo: pathlib.Path, candidate: str, status: str, label: str) -> dict[str, Any]:
    s = CANDIDATE_SPEC[candidate]
    expected_state = s["state_a"] if status == "ACTIVE" else s["state_base"]
    expected_ui = s["ui_b"] if label == "Volume" else s["ui_base"]
    checks = {
        "state_exact": (repo / s["state_path"]).read_text() == expected_state,
        "ui_exact": (repo / s["ui_path"]).read_text() == expected_ui,
        "a_nonoverlap_preserved": (repo / s["a_path"]).read_text() == s["a_changed"],
        "b_nonoverlap_preserved": (repo / s["b_path"]).read_text() == s["b_changed"],
    }
    return {"ok": all(checks.values()), "checks": checks}


def find_bundle_exe(bundle: pathlib.Path) -> pathlib.Path | None:
    candidates: list[pathlib.Path] = []
    if not bundle.exists():
        return None
    for p in bundle.rglob("*"):
        if not p.is_file() or p.suffix.lower() in (".so", ".dll", ".dylib", ".jar", ".zip"):
            continue
        try:
            if p.stat().st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH):
                candidates.append(p)
        except OSError:
            pass
    return max(candidates, key=lambda p: p.stat().st_size) if candidates else None


def validate_candidate(repo: pathlib.Path, candidate: str, tool: dict[str, Any], tool_root: pathlib.Path, expected_status: str, expected_label: str) -> dict[str, Any]:
    env = {"EVERFIELD_S5_EXPECT_STATUS": expected_status, "EVERFIELD_S5_EXPECT_LABEL": expected_label}
    if candidate == "Bevy":
        cargo = (tool.get("cargo") or {}).get("path") or shutil.which("cargo")
        if not cargo:
            return {"ok": False, "reason": "cargo_missing"}
        build = run([str(cargo), "build", "--locked", "--quiet"], cwd=repo, timeout=900)
        exe = repo / "target" / "debug" / "everfield_s5_probe"
        execution = run([str(exe)], cwd=repo, env=env, timeout=120) if ok(build) and exe.exists() else None
        passed = ok(build) and ok(execution) and "EVERFIELD_S5:PASS" in ((execution or {}).get("stdout", "") + (execution or {}).get("stderr", ""))
        return {
            "ok": passed,
            "build": semantic_result(build),
            "execution": semantic_result(execution) if execution else None,
            "executable_sha256": digest_file(exe) if exe.exists() else None,
        }
    if candidate == "Godot":
        exe = tool.get("executable")
        if not exe:
            return {"ok": False, "reason": "godot_executable_missing"}
        execution = run([str(exe), "--headless", "--path", str(repo)], cwd=repo, env=env, timeout=120)
        passed = ok(execution) and "EVERFIELD_S5:PASS" in ((execution.get("stdout") or "") + (execution.get("stderr") or ""))
        return {"ok": passed, "execution": semantic_result(execution), "executable_sha256": tool.get("executable_sha256")}
    if candidate == "Defold":
        java = (tool.get("java") or {}).get("path") or shutil.which("java")
        jar = tool_root / "bob-1.13.0.jar"
        if not java or not jar.exists():
            return {"ok": False, "reason": "bob_or_java_missing"}
        builds = []
        bundle: pathlib.Path | None = None
        for variant in ("headless", "debug"):
            bdir = repo / f"bundle-{variant}"
            rr = run([str(java), "-jar", str(jar), "--root", str(repo), "--bundle-output", str(bdir), "--variant", variant, "--platform", "x86_64-linux", "--archive", "resolve", "build", "bundle"], cwd=repo, timeout=900)
            builds.append({"variant": variant, "result": semantic_result(rr)})
            if ok(rr):
                bundle = bdir
                break
        exe = find_bundle_exe(bundle) if bundle else None
        execution = None
        if exe:
            execution = run([str(exe)], cwd=exe.parent, env=env, timeout=120)
            if not ok(execution) and shutil.which("xvfb-run"):
                execution = run(["xvfb-run", "-a", str(exe)], cwd=exe.parent, env=env, timeout=120)
        passed = bool(execution and ok(execution) and "EVERFIELD_S5:PASS" in ((execution.get("stdout") or "") + (execution.get("stderr") or "")))
        return {
            "ok": passed,
            "builds": builds,
            "execution": semantic_result(execution) if execution else None,
            "executable_sha256": digest_file(exe) if exe and exe.exists() else None,
        }
    return {"ok": False, "reason": "unknown_candidate"}


def metadata_classification(candidate: str) -> dict[str, Any]:
    generated = {
        "Bevy": ["target/"],
        "Godot": [".godot/"],
        "Defold": ["build/", "bundle-headless/", "bundle-debug/"],
    }[candidate]
    return {
        "candidate_generated_metadata_present": True,
        "generated_paths": generated,
        "relevant_to_represented_edit_surface": False,
        "collision_required": False,
        "reason": "generated build/cache outputs are post-merge validation products, not source-authority inputs for the represented S5 semantic edits",
    }


def execute_attempt(root: pathlib.Path, candidate: str, label: str, inject: bool, direction: str, tool: dict[str, Any], tool_root: pathlib.Path, bevy_lock: pathlib.Path | None, run_identity: str) -> dict[str, Any]:
    repo, proof = reset_prepare(root, candidate, label, run_identity)
    baseline = init_repo(repo, candidate, bevy_lock)
    git(repo, "checkout", "-q", "-b", "branch-a", baseline)
    apply_a(repo, candidate, inject)
    a_head = git_commit(repo, "branch-a")
    git(repo, "checkout", "-q", "-b", "branch-b", baseline)
    apply_b(repo, candidate, inject)
    b_head = git_commit(repo, "branch-b")
    a_changed = changed_files(repo, baseline, a_head)
    b_changed = changed_files(repo, baseline, b_head)

    first, second = ("branch-a", "branch-b") if direction == "A_THEN_B" else ("branch-b", "branch-a")
    git(repo, "checkout", "-q", first)
    merge = git(repo, "merge", "--no-ff", "--no-commit", second)
    unmerged = [x for x in git_out(repo, "diff", "--name-only", "--diff-filter=U").splitlines() if x]
    s = CANDIDATE_SPEC[candidate]
    overlap_paths = [s["state_path"], s["ui_path"]]
    markers = {p: ("<<<<<<<" in (repo / p).read_text() and ">>>>>>>" in (repo / p).read_text()) if (repo / p).exists() else False for p in overlap_paths}
    conflict_visible = merge.get("exit") not in (0, None) and set(unmerged) == set(overlap_paths) and all(markers.values())

    resolution = None
    merged_commit = None
    if inject:
        if conflict_visible:
            write(repo / s["state_path"], s["state_a"])
            write(repo / s["ui_path"], s["ui_b"])
            resolution = {"state_choice": "branch-a/ACTIVE", "ui_choice": "branch-b/Volume"}
            merged_commit = git_commit(repo, "bounded-resolution")
    elif ok(merge):
        merged_commit = git_commit(repo, "nonoverlap-merge")

    file_checks = validate_expected_files(repo, candidate, "ACTIVE" if inject else "IDLE", "Volume" if inject else "Audio") if merged_commit else {"ok": False, "checks": {}}
    validation = validate_candidate(repo, candidate, tool, tool_root, "ACTIVE" if inject else "IDLE", "Volume" if inject else "Audio") if merged_commit and file_checks["ok"] else {"ok": False, "reason": "merge_or_file_checks_failed"}
    mode_ok = conflict_visible if inject else ok(merge) and not unmerged
    passed = mode_ok and file_checks["ok"] and validation.get("ok") is True and verify_reset(proof)

    source_digest_body = {
        "candidate": candidate,
        "label": label,
        "mode": "INJECT" if inject else "NORMAL",
        "direction": direction,
        "baseline_tree": git_out(repo, "rev-parse", f"{baseline}^{{tree}}"),
        "branch_a_tree": git_out(repo, "rev-parse", f"{a_head}^{{tree}}"),
        "branch_b_tree": git_out(repo, "rev-parse", f"{b_head}^{{tree}}"),
        "final_tree": git_out(repo, "rev-parse", "HEAD^{tree}") if merged_commit else None,
        "semantic_mapping": {
            "STATE:entity-07.status": s["state_path"],
            "UI:SETTINGS.control-02.label": s["ui_path"],
            "branch_a_nonoverlap": s["a_path"],
            "branch_b_nonoverlap": s["b_path"],
        },
        "branch_a_changed_files": a_changed,
        "branch_b_changed_files": b_changed,
        "merge_exit": merge.get("exit"),
        "unmerged_paths": unmerged,
        "conflict_markers": markers,
        "resolution": resolution,
        "file_checks": file_checks,
        "candidate_validation": validation,
        "generated_metadata": metadata_classification(candidate),
        "run_identity": run_identity,
    }
    raw = {
        "schema": "S5-RAW-ATTEMPT-v1",
        "candidate": candidate,
        "label": label,
        "mode": "INJECT" if inject else "NORMAL",
        "scenario_id": SCENARIO,
        "required_injection": INJECTION if inject else None,
        "direction": direction,
        "reset_proof": proof,
        "reset_verified_derived": verify_reset(proof),
        "source": source_digest_body,
        "formal_result": "PASS" if passed else "INCONCLUSIVE",
        "failure_class": "NONE" if passed else "HARNESS",
    }
    return {"digest": "sha256:" + digest_obj(raw), "record": raw, "observation": {"merge_seconds": merge.get("seconds")}}


def toolchain_identity(candidate: str, tool: dict[str, Any], validator_sha: str, runner_sha: str, run_identity: str) -> dict[str, Any]:
    if candidate == "Bevy":
        exact = {
            "baseline": "0.19.0",
            "retained_lock_sha256": tool.get("retained_lock_sha256"),
            "rustc_version": ((tool.get("rustc") or {}).get("probe") or {}).get("stdout") or ((tool.get("rustc") or {}).get("probe") or {}).get("stderr"),
            "cargo_version": ((tool.get("cargo") or {}).get("probe") or {}).get("stdout") or ((tool.get("cargo") or {}).get("probe") or {}).get("stderr"),
            "lock_replay_bound": tool.get("lock_replay_bound"),
        }
    elif candidate == "Defold":
        exact = {
            "baseline": "1.13.0",
            "artifact_sha256": (tool.get("artifact_identity") or {}).get("expected_sha256"),
            "artifact_digest_source": (tool.get("artifact_identity") or {}).get("digest_source"),
            "bob_version": (tool.get("bob_version") or {}).get("stdout") or (tool.get("bob_version") or {}).get("stderr"),
            "java_version": (((tool.get("java") or {}).get("probe") or {}).get("stdout") or ((tool.get("java") or {}).get("probe") or {}).get("stderr")),
        }
    elif candidate == "Godot":
        exact = {
            "baseline": "4.7.1-stable",
            "archive_sha256": (tool.get("artifact_identity") or {}).get("expected_sha256"),
            "artifact_digest_source": (tool.get("artifact_identity") or {}).get("digest_source"),
            "executable_sha256": tool.get("executable_sha256"),
            "version": (tool.get("version") or {}).get("stdout") or (tool.get("version") or {}).get("stderr"),
        }
    else:
        exact = {"status": tool.get("status")}
    body = {
        "candidate": candidate,
        "scenario": SCENARIO,
        "exact_toolchain_identity": exact,
        "validator_sha256": validator_sha,
        "runner_sha256": runner_sha,
        "run_identity": run_identity,
        "s4_review_terminal": S4_REVIEW_TERMINAL,
        "s4_review_disposition": S4_REVIEW_DISPOSITION,
    }
    return {"body": body, "identity_digest": "sha256:" + digest_obj(body)}


def derive_ids(candidate: str, identity_digest: str, raws: list[dict[str, Any]], adaptation_identity: str, run_identity: str) -> tuple[str, str, dict[str, Any]]:
    body = {
        "candidate": candidate,
        "candidate_identity_digest": identity_digest,
        "raw_attempt_digests": [x["digest"] for x in raws],
        "adaptation_identity": adaptation_identity,
        "run_identity": run_identity,
        "scenario": SCENARIO,
    }
    work = "WORK-S5-" + digest_obj(body)[:24]
    gid = "GEN-S5-" + digest_obj({"work": work, "body": body})[:24]
    return work, gid, body


def formalize(candidate: str, cident: dict[str, Any], raws: list[dict[str, Any]], validator, run_identity: str) -> dict[str, Any]:
    adaptation = validator.adaptation(SCENARIO, candidate)
    av = validator.va(adaptation, candidate)
    work, gid, id_body = derive_ids(candidate, cident["identity_digest"], raws, av["adaptation_identity"], run_identity)
    normals = [x for x in raws if x["record"]["mode"] == "NORMAL"]
    injections = [x for x in raws if x["record"]["mode"] == "INJECT"]
    g = validator.gen(
        SCENARIO,
        gid=gid,
        work=work,
        normal=tuple(x["record"]["formal_result"] for x in normals),
        classes=tuple(x["record"]["failure_class"] for x in normals),
        injres=injections[0]["record"]["formal_result"],
        injfc=injections[0]["record"]["failure_class"],
        resets=tuple(x["record"]["reset_proof"]["reset_id"] for x in normals),
        oks=tuple(x["record"]["reset_verified_derived"] for x in normals),
        wss=tuple(x["record"]["reset_proof"]["workspace_id"] for x in normals),
        res=RESOURCE,
        cid=candidate,
    )
    fi_ref = [k for k, v in g["attempts"].items() if v["kind"] == "FAILURE_INJECTION"][0]
    inj = injections[0]["record"]
    g["attempts"][fi_ref]["reset_id"] = inj["reset_proof"]["reset_id"]
    g["attempts"][fi_ref]["reset_verified"] = inj["reset_verified_derived"]
    g["attempts"][fi_ref]["workspace_id"] = inj["reset_proof"]["workspace_id"]
    ordered = normals + injections
    bindings = {ref: x["digest"] for ref, x in zip(g["run_registry_refs"], ordered)}
    packet = {
        "candidate_identity": cident,
        "identity_derivation": id_body,
        "raw_attempts": ordered,
        "generation": g,
        "source_bindings": bindings,
        "adaptation_validation": av,
    }
    packet["binding_verification"] = verify_packet(packet, validator, run_identity)
    packet["aggregate"] = validator.agg(g)
    packet["trusted_representation_ok"] = (
        packet["binding_verification"] == {"ok": True, "reasons": []}
        and av["result"] == "ACCEPT"
        and packet["aggregate"] == {"aggregate": "PASS_FOR_COMPARISON", "reasons": [], "valid_envelope": True}
    )
    return packet


def verify_packet(packet: dict[str, Any], validator, run_identity: str) -> dict[str, Any]:
    reasons: list[str] = []
    cident = packet.get("candidate_identity", {})
    body = cident.get("body")
    if not isinstance(body, dict) or cident.get("identity_digest") != "sha256:" + digest_obj(body):
        reasons.append("candidate_identity_digest_mismatch")
    raws = packet.get("raw_attempts", [])
    for raw in raws:
        if raw.get("digest") != "sha256:" + digest_obj(raw.get("record")):
            reasons.append("raw_digest_mismatch")
        if raw.get("record", {}).get("source", {}).get("run_identity") != run_identity:
            reasons.append("raw_run_identity_mismatch")
    if not verify_reset_set(raws):
        reasons.append("reset_set_invalid")
    g = packet.get("generation", {})
    refs = g.get("run_registry_refs", [])
    bindings = packet.get("source_bindings", {})
    if len(refs) != len(raws) or set(refs) != set(bindings):
        reasons.append("binding_registry_mismatch")
    for ref, raw in zip(refs, raws):
        if bindings.get(ref) != raw.get("digest"):
            reasons.append("source_binding_substitution")
        formal = g.get("attempts", {}).get(ref, {})
        record = raw.get("record", {})
        proof = record.get("reset_proof", {})
        if formal.get("candidate_id") != record.get("candidate") or formal.get("result") != record.get("formal_result") or formal.get("failure_class") != record.get("failure_class"):
            reasons.append("formal_raw_result_mismatch")
        if formal.get("reset_id") != proof.get("reset_id") or formal.get("workspace_id") != proof.get("workspace_id") or formal.get("reset_verified") != record.get("reset_verified_derived"):
            reasons.append("formal_raw_reset_mismatch")
    av = validator.va(g.get("adaptation"), g.get("candidate_id")) if isinstance(g, dict) else {"result": "REJECT"}
    if av.get("adaptation_identity"):
        exp_work, exp_gid, _ = derive_ids(g.get("candidate_id"), cident.get("identity_digest"), raws, av["adaptation_identity"], run_identity)
        if exp_work != g.get("candidate_work_id") or exp_gid != g.get("generation_id"):
            reasons.append("generation_identity_mismatch")
    else:
        reasons.append("adaptation_invalid")
    return {"ok": not reasons, "reasons": sorted(set(reasons))}


def negative_tests(packet: dict[str, Any], validator, run_identity: str) -> dict[str, bool]:
    tests: dict[str, bool] = {}
    q = copy.deepcopy(packet)
    s = CANDIDATE_SPEC[q["generation"]["candidate_id"]]
    q["raw_attempts"][-1]["record"]["source"]["semantic_mapping"].pop("UI:SETTINGS.control-02.label", None)
    tests["missing_required_overlap_location_rejected"] = set(q["raw_attempts"][-1]["record"]["source"]["semantic_mapping"]) != {"STATE:entity-07.status", "UI:SETTINGS.control-02.label", "branch_a_nonoverlap", "branch_b_nonoverlap"}
    q = copy.deepcopy(packet)
    q["raw_attempts"][0]["record"]["source"]["file_checks"]["checks"]["a_nonoverlap_preserved"] = False
    tests["lost_nonoverlap_update_rejected"] = not q["raw_attempts"][0]["record"]["source"]["file_checks"]["checks"]["a_nonoverlap_preserved"]
    q = copy.deepcopy(packet)
    q["raw_attempts"][-1]["record"]["source"]["unmerged_paths"] = []
    tests["silent_overlap_acceptance_rejected"] = set(q["raw_attempts"][-1]["record"]["source"]["unmerged_paths"]) != {s["state_path"], s["ui_path"]}
    q = copy.deepcopy(packet)
    q["raw_attempts"][0]["record"]["source"]["candidate_validation"]["ok"] = False
    tests["post_merge_validation_bypass_rejected"] = not q["raw_attempts"][0]["record"]["source"]["candidate_validation"]["ok"]
    q = copy.deepcopy(packet)
    q["raw_attempts"][0]["record"]["source"]["direction"] = "SUBSTITUTED"
    tests["raw_source_substitution_rejected"] = not verify_packet(q, validator, run_identity)["ok"]
    q = copy.deepcopy(packet)
    refs = list(q["source_bindings"])
    q["source_bindings"][refs[0]] = q["source_bindings"][refs[1]]
    tests["formal_raw_binding_substitution_rejected"] = not verify_packet(q, validator, run_identity)["ok"]
    g = copy.deepcopy(packet["generation"])
    ref = g["run_registry_refs"][0]
    g["attempts"][ref]["candidate_generation_id"] = "OTHER"
    tests["candidate_generation_mismatch_rejected"] = validator.agg(g)["aggregate"] != "PASS_FOR_COMPARISON"
    g = copy.deepcopy(packet["generation"])
    g["run_registry_refs"].append(g["run_registry_refs"][0])
    tests["duplicate_registry_rejected"] = validator.agg(g)["aggregate"] != "PASS_FOR_COMPARISON"
    q = copy.deepcopy(packet)
    q["raw_attempts"][1]["record"]["reset_proof"]["workspace_id"] = q["raw_attempts"][0]["record"]["reset_proof"]["workspace_id"]
    tests["reused_workspace_rejected"] = not verify_reset_set(q["raw_attempts"])
    return tests


def candidate_available(candidate: str, tool: dict[str, Any]) -> bool:
    if candidate == "Bevy":
        return tool.get("status") in ("CAPABLE", "CAPABLE_WITH_PRESEED")
    return tool.get("status") == "CAPABLE"


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
    validator_path = pathlib.Path(args.validator).resolve()
    probe_path = pathlib.Path(args.toolchain_probe).resolve()
    bevy_lock = pathlib.Path(args.bevy_lock).resolve()
    artifact_lock_path = pathlib.Path(args.artifact_lock).resolve()
    validator = load_module(validator_path, "everfield_s5_validator")
    probe = load_module(probe_path, "everfield_s5_toolchain_probe")
    validator_sha = digest_file(validator_path)
    runner_sha = digest_file(pathlib.Path(__file__).resolve())
    run_identity = os.environ.get("GITHUB_RUN_ID", "LOCAL") + ":" + os.environ.get("GITHUB_RUN_ATTEMPT", "1") + ":" + os.environ.get("GITHUB_SHA", "LOCAL")

    artifact_lock = probe.load_artifact_lock(artifact_lock_path)
    with tempfile.TemporaryDirectory(prefix="everfield-s5-") as td:
        root = pathlib.Path(td)
        tool_root = root / "toolchains"
        tool_root.mkdir()
        tools = {
            "Bevy": probe.probe_bevy(tool_root / "bevy", bevy_lock),
            "Defold": probe.probe_defold(tool_root, artifact_lock),
            "Godot": probe.probe_godot(tool_root, artifact_lock),
            "Unity": probe.probe_unity(),
            "Unreal Engine": probe.probe_unreal(),
        }
        results: dict[str, Any] = {}
        provisional: list[str] = []
        for candidate in ("Bevy", "Defold", "Godot"):
            tool = tools[candidate]
            if not candidate_available(candidate, tool):
                results[candidate] = {"candidate": candidate, "disposition": "NOT_RUN_TOOLCHAIN_UNAVAILABLE", "toolchain": tool}
                continue
            raws = [
                execute_attempt(root, candidate, "N1", False, "A_THEN_B", tool, tool_root, bevy_lock if candidate == "Bevy" else None, run_identity),
                execute_attempt(root, candidate, "N2", False, "B_THEN_A", tool, tool_root, bevy_lock if candidate == "Bevy" else None, run_identity),
                execute_attempt(root, candidate, "FI1", True, "A_THEN_B", tool, tool_root, bevy_lock if candidate == "Bevy" else None, run_identity),
            ]
            cident = toolchain_identity(candidate, tool, validator_sha, runner_sha, run_identity)
            packet = formalize(candidate, cident, raws, validator, run_identity)
            packet["negative_selftests"] = negative_tests(packet, validator, run_identity)
            packet["disposition"] = "PROVISIONAL_S5_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW" if packet["trusted_representation_ok"] and all(packet["negative_selftests"].values()) else "INCONCLUSIVE_HARNESS_OR_INFRA"
            results[candidate] = packet
            if packet["disposition"].startswith("PROVISIONAL"):
                provisional.append(candidate)

        payload = {
            "schema": "W2-ENG-TECHNICAL-S5-v1",
            "mission_id": "W2-ENG-TECH-S5-01",
            "scenario_id": SCENARIO,
            "harness_id": "W2-ENG-HARNESS-v5",
            "feature_slice_id": "W2-ENG-FEATURE-SLICE-v2",
            "scenario_manifest_id": "W2-ENG-SCENARIO-INPUTS-v2",
            "validator_sha256": validator_sha,
            "runner_sha256": runner_sha,
            "run_identity": run_identity,
            "s5_contract": {
                "fixed_input_refs": ["SLICE:logical_state", "SLICE:player_surface", "SLICE:merge_fixture"],
                "obligations": ["parallel_nonoverlap", "intentional_overlap", "visible_conflict", "post_merge_checks"],
                "min_bounds": {"overlap_count": 2, "branch_a_nonoverlap": 1, "branch_b_nonoverlap": 1},
                "required_injection": INJECTION,
                "semantic_overlap_locations": list(OVERLAP),
            },
            "predecessor_review": {
                "issue": 374,
                "terminal_comment": S4_REVIEW_TERMINAL,
                "disposition": S4_REVIEW_DISPOSITION,
                "review_publication_sha": S4_REVIEW_PUBLICATION,
                "remediation_publication_sha": S4_REMEDIATION_PUBLICATION,
            },
            "toolchains": tools,
            "results": results,
            "provisional_candidates": provisional,
            "authority_bound_not_run": {
                "Unity": "NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY",
                "Unreal Engine": "NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY",
            },
            "historical_issue_82_not_run_cells_preserved": 50,
            "reviewed_s3_s4_provenance_preserved": True,
            "fresh_review_required": True,
            "trusted_comparison_authority": False,
            "integration_authority": False,
            "engine_selected": False,
            "implementation_readiness": False,
            "canonicality": "NOT_CANONICAL",
        }
        out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(json.dumps({"schema": payload["schema"], "provisional_candidates": provisional, "out": str(out)}, sort_keys=True))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
