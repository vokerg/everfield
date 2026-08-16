#!/usr/bin/env python3
"""Bind retained W2-ENG-TECH-S3-01 observations through unchanged v5 authority semantics."""
from __future__ import annotations
import argparse, contextlib, copy, hashlib, importlib.util, io, json, pathlib

SOURCE_SHA = "411641a6fbd6a27bd81adf5747c1bb961e5490fdae72d1eea15ac700dd8c85ca"
SOURCE_COMMIT = "899e0011f49ce8a73f8b543a1c4b054ce517e715"
SOURCE_RUN = 31895624493
SOURCE_ARTIFACT = 9249732138
SOURCE_ARTIFACT_DIGEST = "sha256:068e5ee0df2802d4f52486d0ea42932bb99eaa7a04098298bca8586e65a68c72"
SOURCE_PRODUCER_HEAD = "609d463077725acc2c23c894154cca169d6a75fc"
VALIDATOR_SHA = "9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea"
EXECUTED = ("Bevy", "Defold", "Godot")
NORMAL = 405227
PERTURBED = 405122
RESOURCE = "W2-ENG-HOST-COMMON-v2"
INJECTION = "FI-S3-INPUT-PERTURB-v2"


def hbytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def digest(o) -> str:
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_validator(path: pathlib.Path):
    raw = path.read_bytes()
    if hbytes(raw) != VALIDATOR_SHA:
        raise RuntimeError(f"reviewed_validator_sha_mismatch:{hbytes(raw)}")
    spec = importlib.util.spec_from_file_location("everfield_v5", path)
    if not spec or not spec.loader:
        raise RuntimeError("reviewed_validator_import_unavailable")
    mod = importlib.util.module_from_spec(spec)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        spec.loader.exec_module(mod)
    if mod.ID.get("validator_id") != "W2-ENG-PROTOCOL-VALIDATOR-v5":
        raise RuntimeError("reviewed_validator_id_mismatch")
    return mod, captured.getvalue()


def source_hash_ok(raw: bytes, expected: str = SOURCE_SHA) -> bool:
    return hbytes(raw) == expected


def label(a: dict) -> str:
    return f"N{a['normal_index']}" if a.get("kind") == "NORMAL" else "FI1"


def source_candidate_errors(cid: str, r: dict) -> list[str]:
    e: list[str] = []
    ats = r.get("attempts")
    if not isinstance(ats, list) or len(ats) != 3:
        return ["attempt_count_not_three"]
    if r.get("scenario") != "S3": e.append("scenario_mismatch")
    if r.get("candidate") != cid: e.append("candidate_mismatch")
    if r.get("producer_disposition") != "PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW": e.append("producer_disposition_mismatch")
    normal = [a for a in ats if a.get("kind") == "NORMAL"]
    fi = [a for a in ats if a.get("kind") == "FAILURE_INJECTION"]
    if sorted(a.get("normal_index") for a in normal) != [1, 2]: e.append("normal_index_set_invalid")
    if len(fi) != 1 or fi[0].get("injection_id") != INJECTION: e.append("required_injection_invalid")
    if len({a.get("reset_id") for a in ats}) != 3 or any(not a.get("reset_id") for a in ats): e.append("reset_identity_not_unique")
    if len({a.get("workspace_id") for a in ats}) != 3 or any(not a.get("workspace_id") for a in ats): e.append("workspace_identity_not_unique")
    for a in ats:
        expected = NORMAL if a.get("kind") == "NORMAL" else PERTURBED
        if a.get("scenario_id") != "S3" or a.get("candidate_id") != cid: e.append(f"{a.get('attempt_id')}:identity_mismatch")
        if a.get("result") != "PASS" or a.get("failure_class") != "NONE": e.append(f"{a.get('attempt_id')}:source_not_pass")
        if a.get("expected_checksum") != expected or a.get("observed_checksum") != expected: e.append(f"{a.get('attempt_id')}:checksum_mismatch")
        if a.get("resource_class") != RESOURCE: e.append(f"{a.get('attempt_id')}:resource_mismatch")
        cmd = a.get("command") or {}
        if cmd.get("exit") != 0 or cmd.get("timed_out") is not False: e.append(f"{a.get('attempt_id')}:process_not_successful")
        joined = " ".join(str(x) for x in (cmd.get("cmd") or []))
        marker = f"/runs/{cid.lower()}/{label(a)}"
        if marker not in joined: e.append(f"{a.get('attempt_id')}:attempt_workspace_not_in_native_command")
    return e


def reset_derivation(cid: str, ats: list[dict]) -> dict:
    # Ignore producer reset_verified. Derive only from retained process/workspace evidence.
    unique_reset = len({a["reset_id"] for a in ats}) == len(ats)
    unique_workspace = len({a["workspace_id"] for a in ats}) == len(ats)
    command_workspace_bound = all(f"/runs/{cid.lower()}/{label(a)}" in " ".join(a["command"]["cmd"]) for a in ats)
    fresh_process = all(a["command"]["exit"] == 0 and a["command"]["timed_out"] is False for a in ats)
    return {"unique_reset_identity": unique_reset, "unique_workspace_identity": unique_workspace,
            "candidate_native_command_bound_to_attempt_workspace": command_workspace_bound,
            "fresh_successful_process_per_attempt": fresh_process,
            "derived_reset_verified": all((unique_reset, unique_workspace, command_workspace_bound, fresh_process)),
            "producer_reset_verified_field_consumed": False}


def binding_map_ok(g: dict, bindings: dict) -> bool:
    return isinstance(bindings, dict) and set(bindings) == set(g.get("attempts", {})) and all(
        isinstance(bindings[k], dict) and bindings[k].get("source_attempt_id") for k in g.get("attempts", {})
    )


def build_candidate(v, source: dict, cid: str):
    r = source["results"][cid]
    errs = source_candidate_errors(cid, r)
    if errs:
        raise RuntimeError(f"source_candidate_invalid:{cid}:{','.join(errs)}")
    ats = r["attempts"]
    reset = reset_derivation(cid, ats)
    if not reset["derived_reset_verified"]:
        raise RuntimeError(f"reset_not_derivable:{cid}")

    a = v.adaptation("S3", cid)
    av = v.va(a, cid)
    if av.get("result") != "ACCEPT":
        raise RuntimeError(f"adaptation_rejected:{cid}:{av.get('reasons')}")

    work_basis = {"source_evidence_sha256": SOURCE_SHA, "producer_head": SOURCE_PRODUCER_HEAD,
                  "candidate": cid, "toolchain": r.get("toolchain"), "build": r.get("build"),
                  "bundle_executable_sha256": r.get("bundle_executable_sha256")}
    work = "WORK-S3-" + digest(work_basis)[:24]
    gen_basis = {"source_run": SOURCE_RUN, "source_commit": SOURCE_COMMIT, "candidate": cid,
                 "source_attempt_ids": [x["attempt_id"] for x in ats], "work": work}
    gid = "GEN-S3-" + digest(gen_basis)[:24]

    formal = {}
    bindings = {}
    for x in ats:
        suffix = label(x)
        aid = f"{gid}-S3-{suffix}"
        formal[aid] = v.attempt(aid, "S3", gid, x["kind"], "PASS",
                                ni=x.get("normal_index"), inj=x.get("injection_id"), fc="NONE",
                                rid=x["reset_id"], rok=reset["derived_reset_verified"],
                                ws=x["workspace_id"], res=x["resource_class"], cid=cid)
        bindings[aid] = {"source_attempt_id": x["attempt_id"],
                         "source_json_pointer": f"/results/{cid}/attempts/{ats.index(x)}",
                         "source_expected_checksum": x["expected_checksum"],
                         "source_observed_checksum": x["observed_checksum"],
                         "source_process_command_sha256": digest(x["command"]["cmd"]),
                         "source_process_exit": x["command"]["exit"],
                         "source_process_timed_out": x["command"]["timed_out"]}

    g = {"scenario_id": "S3", "candidate_id": cid, "generation_id": gid,
         "candidate_work_id": work, "predecessor_generation_id": None, "repair_change_ref": None,
         "harness_defect": False, "adaptation": a,
         "adaptation_binding_id": v.D(v.binding(a)), "attempts": formal,
         "run_registry_refs": list(formal), "all_attempt_refs": list(formal)}
    if not binding_map_ok(g, bindings):
        raise RuntimeError(f"source_binding_map_invalid:{cid}")
    aggregate = v.agg(g)
    if aggregate != {"aggregate": "PASS_FOR_COMPARISON", "reasons": [], "valid_envelope": True}:
        raise RuntimeError(f"v5_aggregate_not_pass:{cid}:{aggregate}")
    return g, bindings, reset, av, aggregate


def selftests(v, source: dict, baseline: dict, bindings: dict) -> dict:
    c = "Bevy"; g = baseline[c]
    tests = {}
    x = copy.deepcopy(g); first = next(iter(x["attempts"])); x["attempts"][first].pop("candidate_generation_id")
    tests["missing_candidate_generation_id"] = v.agg(x)["aggregate"] != "PASS_FOR_COMPARISON"
    x = copy.deepcopy(g); x["adaptation"]["mechanism_authority"] = "ABSTRACT_SIMULATOR"
    tests["mechanism_authority_downgrade"] = v.va(x["adaptation"], c)["result"] == "REJECT"
    x = copy.deepcopy(g); x["run_registry_refs"].append(x["run_registry_refs"][0])
    tests["duplicate_registry_ref"] = v.agg(x)["aggregate"] != "PASS_FOR_COMPARISON"
    x = copy.deepcopy(g); normals = [a for a in x["attempts"].values() if a["kind"] == "NORMAL"]
    normals[1]["reset_id"] = normals[0]["reset_id"]; normals[1]["workspace_id"] = normals[0]["workspace_id"]
    tests["reused_reset_workspace"] = v.agg(x)["aggregate"] == "NOT_RUN"
    x = copy.deepcopy(source["results"][c]); x["attempts"][0]["observed_checksum"] += 1
    tests["checksum_substitution"] = bool(source_candidate_errors(c, x))
    tests["source_evidence_hash_substitution"] = not source_hash_ok(json.dumps(source, sort_keys=True).encode(), "0" * 64)
    b = copy.deepcopy(bindings[c]); b.pop(next(iter(b)))
    tests["formal_attempt_without_source_binding"] = not binding_map_ok(g, b)
    if not all(tests.values()):
        raise RuntimeError(f"negative_selftest_failed:{[k for k,vv in tests.items() if not vv]}")
    return tests


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--validator", default="docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    source_path = pathlib.Path(args.source); raw = source_path.read_bytes()
    if not source_hash_ok(raw):
        raise RuntimeError(f"source_evidence_sha_mismatch:{hbytes(raw)}")
    source = json.loads(raw)
    if source.get("mission_id") != "W2-ENG-TECH-S3-01" or source.get("source_issue") != 351 or source.get("scenario_id") != "S3":
        raise RuntimeError("source_identity_mismatch")
    if source.get("historical_issue_82_not_run_cells_preserved") != 50 or source.get("historical_issue_82_cells_mutated") is not False:
        raise RuntimeError("historical_issue_82_provenance_mismatch")
    if source.get("oracle") != {"normal_checksum": NORMAL, "normal_recomputed": NORMAL, "perturbed_checksum": PERTURBED, "perturbed_recomputed": PERTURBED}:
        raise RuntimeError("source_oracle_mismatch")
    for cid in ("Unity", "Unreal Engine"):
        if source["results"][cid]["producer_disposition"] != "NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY":
            raise RuntimeError(f"authority_bound_candidate_changed:{cid}")

    v, fixture_output = load_validator(pathlib.Path(args.validator))
    generations = {}; bindings = {}; resets = {}; avs = {}; aggs = {}
    for cid in EXECUTED:
        generations[cid], bindings[cid], resets[cid], avs[cid], aggs[cid] = build_candidate(v, source, cid)
    tests = selftests(v, source, generations, bindings)

    packet = {"schema": "W2-ENG-TECH-S3-V5-REMEDIATION-v1", "mission_id": "W2-ENG-TECH-S3-REM-01",
      "source": {"producer_issue": 351, "producer_terminal_comment": 5303181547, "producer_head": SOURCE_PRODUCER_HEAD,
        "evidence_commit": SOURCE_COMMIT, "run_id": SOURCE_RUN, "artifact_id": SOURCE_ARTIFACT,
        "artifact_digest": SOURCE_ARTIFACT_DIGEST, "evidence_sha256": SOURCE_SHA,
        "failed_history_refs": [
          {"run_id":31895282641,"evidence_commit":"5d6b940ee3c57ac78f0d40a890cdc6d48891fd4c","artifact_id":9249633980,"artifact_digest":"sha256:dee70cb19ad8ae254e69914d5cdc0b15902aaf8410971d14217b0162868d5135"},
          {"run_id":31895462621,"evidence_commit":"67848934b336aa7cde5e391d5cb7fef1766cf462","artifact_id":9249687249,"artifact_digest":"sha256:f2258a90ccd47faa6f78bc864fc3578821ca047d6abfd5f08ac7c33d6a578d2a"}]},
      "review_route": {"source_review_issue":353,"source_review_terminal_comment":5303205496,"finding_closed_by_this_packet":"W2-ENG-TECH-S3-REV-M01","fresh_review_required":True},
      "reviewed_validator": {"validator_id":v.ID["validator_id"],"validator_sha256":VALIDATOR_SHA,"harness_id":v.ID["harness_id"],"feature_slice_id":v.ID["feature_slice_id"],"scenario_manifest_id":v.ID["scenario_manifest_id"],"fixture_validator_executed":True,"fixture_output_sha256":hashlib.sha256(fixture_output.encode()).hexdigest()},
      "formal_generations": generations, "source_attempt_bindings": bindings, "reset_derivation": resets,
      "adaptation_validation": avs, "v5_aggregates": aggs, "negative_selftests": tests,
      "authority_bound_not_run": {"Unity":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY","Unreal Engine":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"},
      "historical_issue_82_not_run_cells_preserved":50,"historical_issue_82_cells_mutated":False,
      "all_executed_candidates_v5_pass_for_comparison": all(x.get("aggregate")=="PASS_FOR_COMPARISON" and x.get("valid_envelope") is True for x in aggs.values()),
      "engine_selected":False,"s1_s2_s4_s10_complete":False,"production_implementation_ready":False,"provider_permission":False,
      "verification_pass_authority":False,"decision_authority":False,"canonicality":"NOT_CANONICAL","integration_authority":False}
    pathlib.Path(args.out).write_text(json.dumps(packet, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"v5_aggregates":aggs,"negative_selftests":tests,"out":args.out}, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
