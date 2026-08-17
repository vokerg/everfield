#!/usr/bin/env python3
"""Bounded Godot-only harness remediation for W2-ENG-TECH-S7-01.

Preserves the executed base S7 producer as provenance and overrides only the two
Godot fixture defects exposed by run 31992586423:
- valid typed .tres Resource fixtures;
- SceneTree.quit() rather than Node-only get_tree().quit().
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve()
BASE_PATH = HERE.with_name("engine_technical_s7_probe.py")


def sha_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_base():
    spec = importlib.util.spec_from_file_location("everfield_s7_base_r2", BASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BASE_PATH}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def corrected_godot_source(base, broken: bool = False) -> str:
    lines = ["extends SceneTree"]
    for i, asset in enumerate(base.ASSETS, 1):
        path = f"res://assets/{asset}.tres"
        if asset == base.BROKEN_ASSET and broken:
            path = "res://assets/MISSING-ASSET-08.tres"
        lines.append(f'const A{i} = preload("{path}")')
    lines += [
        "func _init():",
        " var n = 0",
        " for x in [A1,A2,A3,A4,A5,A6,A7,A8]:",
        "  if x != null: n += 1",
        " if n != 8: quit(7); return",
        ' print("EVERFIELD_S7:PASS:8")',
        " quit(0)",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    base = load_base()
    base_runner_sha = sha_file(BASE_PATH)
    original_materialize = base.materialize

    def materialize(repo: pathlib.Path, candidate: str, bevy_lock: pathlib.Path) -> pathlib.Path:
        driver = original_materialize(repo, candidate, bevy_lock)
        if candidate == "Godot":
            for asset in base.ASSETS:
                base.write(
                    repo / "assets" / f"{asset}.tres",
                    f'[gd_resource type="Resource" format=3]\n\n[resource]\nresource_name = "{asset}"\n',
                )
        return driver

    base.godot_source = lambda broken=False: corrected_godot_source(base, broken)
    base.materialize = materialize
    # Bind evidence runner_sha256 to this remediation runner, not the retained base producer.
    base.__file__ = str(HERE)

    rc = base.main()
    if rc != 0:
        return rc

    # base.main() writes --out; recover that path fail-closed from argv exactly as the base parser does.
    import sys
    try:
        out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1])
    except (ValueError, IndexError) as exc:
        raise RuntimeError("missing --out after base execution") from exc

    evidence = json.loads(out.read_text())
    corrections = evidence.setdefault("producer_corrections", [])
    corrections.append(
        {
            "run_id": 31992586423,
            "run_attempt": 1,
            "trigger_sha": "274c2e62419acb7d55c318540cd4c6e7b596fbe6",
            "evidence_commit_sha": "40a0622373c52ac88b54eff5c9ce1433cad7ce29",
            "artifact_id": 9275837343,
            "artifact_digest": "sha256:4e76f57fd65aabdb3e2397da495817fc6fdd9889c31b84453bba22fe7eed111e",
            "evidence_sha256": "b09d1304845cf555fa04cd28d38f367d6ceb355d6dcf6ba70b95635b4235f547",
            "status": "RETAINED_PARTIAL_PRODUCER_PROVENANCE",
            "trusted_public_candidates": ["Bevy", "Defold"],
            "findings": [
                "GODOT_RESOURCE_TYPE_FIELD_OMITTED",
                "GODOT_SCENETREE_GET_TREE_CALL_INVALID",
            ],
        }
    )
    evidence["remediation_runner"] = {
        "path": str(HERE.relative_to(HERE.parents[2])),
        "sha256": sha_file(HERE),
        "retained_base_runner_path": str(BASE_PATH.relative_to(BASE_PATH.parents[2])),
        "retained_base_runner_sha256": base_runner_sha,
        "scope": "GODOT_FIXTURE_TYPE_AND_SCENETREE_QUIT_ONLY",
    }
    out.write_text(json.dumps(evidence, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "remediation_runner": evidence["remediation_runner"],
        "provisional_candidates": evidence.get("provisional_candidates", []),
        "producer_corrections": len(corrections),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
