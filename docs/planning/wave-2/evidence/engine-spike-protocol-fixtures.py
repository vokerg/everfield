#!/usr/bin/env python3
"""W2-REM-ENG-02 engine-neutral planning protocol validator v2.1."""

import copy, hashlib, json, math

def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

IDENTITY = {
    "validator_id":"W2-ENG-PROTOCOL-VALIDATOR-v2.1",
    "harness_id":"W2-ENG-HARNESS-v2.1",
    "feature_slice_id":"W2-ENG-FEATURE-SLICE-v2",
    "scenario_manifest_id":"W2-ENG-SCENARIO-INPUTS-v2",
    "semantics":["common-input-bounds","adaptation-equivalence","start-resource-parity",
                 "attempt-lineage","aggregate-no-laundering","repair-generation-lineage",
                 "failure-class-authority","harness-defect-reopen","fresh-continuation"],
}
FEATURE = {
 "feature_slice_id":"W2-ENG-FEATURE-SLICE-v2",
 "logical_state":{"entity_count":32,"world_width":16,"world_height":16,
                  "fields_per_entity":["entity_id","x","y","status","flags"],"seed":424242,"normal_ticks":600},
 "action_vocabulary":["MOVE_NORTH","MOVE_SOUTH","MOVE_EAST","MOVE_WEST","INTERACT",
                      "OPEN_MENU","CONFIRM","CANCEL","SAVE","LOAD"],
 "player_surface":{"screen_ids":["BOOT_OR_MAIN","PLAY_SURFACE","SETTINGS"],
                   "required_routes":["BOOT_OR_MAIN->PLAY_SURFACE","PLAY_SURFACE->SETTINGS","SETTINGS->PLAY_SURFACE"],
                   "input_classes":["PRIMARY_POINTER_OR_KEYBOARD","CONTROLLER_OR_EQUIVALENT_SEMANTIC_ROUTE"]},
 "assets":{"logical_asset_ids":[f"ASSET-{i:02d}" for i in range(1,9)],"required_asset_count":8,
           "broken_reference_asset_id":"ASSET-08"},
 "save_schema":{"v1_fields":["schema_version","seed","tick","entities","settings"],
                "v2_added_field":"world_flags","v2_default":{},"malformed_fixture_id":"SAVE-MALFORMED-UNSUPPORTED-v2"},
 "merge_fixture":{"branch_a_nonoverlap_changes":1,"branch_b_nonoverlap_changes":1,
                  "semantic_overlap_locations":["STATE:entity-07.status","UI:SETTINGS.control-02.label"],
                  "required_overlap_count":2,"generated_collision_required_when_candidate_has_generated_metadata":True},
 "capture_fixture":{"logical_state_marker":"CAPTURE-STATE-042","viewport_width":1280,"viewport_height":720,"required_frame_count":1},
 "profiling_fixture":{"normal_logical_updates":19200,"hotspot_extra_updates":3200,"hotspot_id":"HOTSPOT-ENTITY-UPDATE-v2"},
 "package_fixture":{"target_id":"WINDOWS_X64_DEV_PACKAGE-v1","required_entry_surface":"BOOT_OR_MAIN",
                    "required_screen_count":3,"store_signing_required":False,"clean_extract_launch_required":True},
 "continuation_fixture":{"partial_state_id":"CONT-PARTIAL-v2","remaining_action_ids":["CONT-A1","CONT-A2","CONT-A3"],
                         "required_handoff_fields":["branch","head_sha","attempt_refs","failure_refs","remaining_actions","commands","next_acceptance_step"],
                         "negative_missing_field":"next_acceptance_step"},
}
R={"STATE":"SLICE:logical_state","ACTIONS":"SLICE:action_vocabulary","SURFACE":"SLICE:player_surface",
   "ASSETS":"SLICE:assets","SAVE":"SLICE:save_schema","MERGE":"SLICE:merge_fixture",
   "CAPTURE":"SLICE:capture_fixture","PROFILE":"SLICE:profiling_fixture","PACKAGE":"SLICE:package_fixture","CONT":"SLICE:continuation_fixture"}
def sc(refs, obligations, bounds, injection, **extra):
    d={"fixed_input_refs":[R[x] for x in refs],"obligations":obligations,"min_bounds":bounds,"required_injections":[injection]}
    d.update(extra); return d
SCENARIOS={
 "S1":sc(["STATE","ACTIONS","SURFACE","ASSETS"],["clean_reconstruct","build","launch","cold_start","incremental_observation"],
         {"entity_count":32,"asset_count":8,"screen_count":3},"FI-S1-CACHE-MISS-v2"),
 "S2":sc(["STATE","ACTIONS","SURFACE","ASSETS"],["fresh_agent_change","visible_or_state_visible_change","reviewable_diff","automated_verification"],
         {"entity_count":32,"asset_count":8,"screen_count":3,"changed_logical_locations":1},"FI-S2-STALE-META-v2"),
 "S3":sc(["STATE","ACTIONS"],["real_or_shared_rules","exact_seed_input","repeatable_state_events","perturbation_distinguishable"],
         {"entity_count":32,"normal_ticks":600,"action_count":10},"FI-S3-INPUT-PERTURB-v2",required_mechanism_authority="REAL_OR_SHARED_RULES"),
 "S4":sc(["STATE","SAVE"],["round_trip","schema_evolution","explicit_migration","malformed_tuple_diagnostic"],
         {"entity_count":32,"save_v1_field_count":5,"save_v2_added_field_count":1},"FI-S4-INCOMPAT-TUPLE-v2"),
 "S5":sc(["STATE","SURFACE","MERGE"],["parallel_nonoverlap","intentional_overlap","visible_conflict","post_merge_checks"],
         {"overlap_count":2,"branch_a_nonoverlap":1,"branch_b_nonoverlap":1},"FI-S5-OVERLAP-v2"),
 "S6":sc(["STATE","SURFACE","CAPTURE"],["reach_known_state","identity_bound_capture","state_vs_capture_failure_separated"],
         {"screen_count":3,"capture_frame_count":1,"viewport_width":1280,"viewport_height":720},"FI-S6-CAPTURE-DOWN-v2"),
 "S7":sc(["ASSETS","STATE"],["inject_broken_reference","diagnose_from_repo_cli","bounded_repair","rerun"],
         {"asset_count":8,"broken_reference_count":1},"FI-S7-BROKEN-REF-v2"),
 "S8":sc(["STATE","PROFILE"],["representative_workload","parseable_profile","locate_injected_hotspot","resource_observations"],
         {"normal_logical_updates":19200,"hotspot_extra_updates":3200},"FI-S8-HOTSPOT-v2"),
 "S9":sc(["STATE","SURFACE","ASSETS","PACKAGE"],["produce_common_package_target","exact_repro_inputs","clean_extract_launch","typed_failed_package_diagnostic"],
         {"screen_count":3,"asset_count":8},"FI-S9-PACKAGE-CONFIG-v2",required_package_target="WINDOWS_X64_DEV_PACKAGE-v1"),
 "S10":sc(["CONT","STATE","SURFACE"],["repository_only_handoff","fresh_context_reconstruct","complete_remaining_actions","rerun_evidence"],
          {"remaining_action_count":3,"required_handoff_field_count":7},"FI-S10-HANDOFF-GAP-v2",hidden_context_forbidden=True),
}
START={"profile_id":"W2-ENG-START-COLD-v2","cache_mode":"COLD","generated_state_policy":"REGENERATE_FROM_REPO","resource_class":"W2-ENG-HOST-COMMON-v2"}

def adaptation(sid):
    s=SCENARIOS[sid]
    return {"candidate_id":"SYNTHETIC-CANDIDATE","scenario_id":sid,"harness_id":IDENTITY["harness_id"],
            "feature_slice_id":FEATURE["feature_slice_id"],"fixed_input_refs":list(s["fixed_input_refs"]),
            "mappings":{x:"EQUIVALENT" for x in s["obligations"]},"bounds":dict(s["min_bounds"]),
            "failure_injections":list(s["required_injections"]),"start_profile":copy.deepcopy(START),
            "undocumented_manual_intervention":False,"resource_exception":False,
            "mechanism_authority":s.get("required_mechanism_authority","CANDIDATE_NATIVE_EQUIVALENT"),
            "package_target":s.get("required_package_target"),"hidden_context_transfer":False,"extra_evidence":[]}

def validate(a):
    sid=a.get("scenario_id")
    if sid not in SCENARIOS: return {"result":"REJECT","reasons":["unknown_scenario"]}
    s=SCENARIOS[sid]; why=[]
    if a.get("harness_id")!=IDENTITY["harness_id"]: why+=["harness_mismatch"]
    if a.get("feature_slice_id")!=FEATURE["feature_slice_id"]: why+=["feature_slice_mismatch"]
    if not set(s["fixed_input_refs"])<=set(a.get("fixed_input_refs",[])): why+=["missing_common_input_ref"]
    for x in s["obligations"]:
        if a.get("mappings",{}).get(x) not in ("EQUIVALENT","STRICTLY_STRONGER"): why+=[f"missing_or_weaker_obligation:{x}"]
    for k,v in s["min_bounds"].items():
        if a.get("bounds",{}).get(k,-math.inf)<v: why+=[f"shrunk_bound:{k}"]
    if not set(s["required_injections"])<=set(a.get("failure_injections",[])): why+=["required_failure_injection_missing"]
    st=a.get("start_profile",{})
    if st.get("cache_mode")!="COLD" or st.get("generated_state_policy")!="REGENERATE_FROM_REPO": why+=["hidden_or_noncommon_start_state"]
    if st.get("resource_class")!=START["resource_class"]: why+=["noncommon_resource_class"]
    if a.get("resource_exception"): why+=["unresolved_resource_exception"]
    if a.get("undocumented_manual_intervention"): why+=["hidden_manual_intervention"]
    if s.get("required_mechanism_authority") and a.get("mechanism_authority")!=s["required_mechanism_authority"]: why+=["lower_authority_mechanism"]
    if s.get("required_package_target") and a.get("package_target")!=s["required_package_target"]: why+=["common_package_target_missing"]
    if s.get("hidden_context_forbidden") and a.get("hidden_context_transfer"): why+=["hidden_context_transfer"]
    return {"result":"ACCEPT" if not why else "REJECT","reasons":why}

def attempt(aid,sid,gid,kind,result,normal_index=None,injection_id=None,failure_class="NONE",
            reset_id=None,reset_verified=True,workspace_id=None,resource_class=START["resource_class"]):
    return {"attempt_id":aid,"scenario_id":sid,"candidate_id":"SYNTHETIC-CANDIDATE","candidate_generation_id":gid,
            "kind":kind,"normal_index":normal_index,"injection_id":injection_id,"result":result,
            "failure_class":failure_class,"reset_id":reset_id,"reset_verified":reset_verified,
            "workspace_id":workspace_id,"resource_class":resource_class}

def aset(sid,gid="GEN-1",work="WORK-1",normal=("PASS","PASS"),classes=None,injection_result="PASS",
         injection_class="NONE",reset_ids=("RESET-1","RESET-2","RESET-3"),reset_ok=(True,True,True),
         workspaces=("WS-1","WS-2","WS-3"),resource=START["resource_class"],harness_defect=False,
         predecessor=None,repair=None):
    s=SCENARIOS[sid]; classes=classes or tuple("NONE" if x=="PASS" else "PRODUCT" for x in normal); A={}; reg=[]
    for i,res in enumerate(normal,1):
        aid=f"{gid}-{sid}-N{i}"; reg.append(aid)
        A[aid]=attempt(aid,sid,gid,"NORMAL",res,i,failure_class=classes[i-1],
                       reset_id=reset_ids[i-1] if i-1<len(reset_ids) else None,
                       reset_verified=reset_ok[i-1] if i-1<len(reset_ok) else False,
                       workspace_id=workspaces[i-1] if i-1<len(workspaces) else None,resource_class=resource)
    for i,inj in enumerate(s["required_injections"],1):
        aid=f"{gid}-{sid}-FI{i}"; reg.append(aid)
        A[aid]=attempt(aid,sid,gid,"FAILURE_INJECTION",injection_result,injection_id=inj,
                       failure_class=injection_class,reset_id=f"{gid}-RESET-FI{i}",
                       workspace_id=f"{gid}-WS-FI{i}",resource_class=resource)
    return {"scenario_id":sid,"candidate_id":"SYNTHETIC-CANDIDATE","generation_id":gid,"candidate_work_id":work,
            "predecessor_generation_id":predecessor,"repair_change_ref":repair,"harness_defect":harness_defect,
            "attempts":A,"run_registry_refs":reg,"all_attempt_refs":list(A)}

def aggregate(x):
    sid=x["scenario_id"]; s=SCENARIOS[sid]; A=x["attempts"]; gid=x["generation_id"]
    if set(x.get("run_registry_refs",[]))!=set(A): return {"aggregate":"INCONCLUSIVE","reasons":["attempt_registry_omission_or_extra"]}
    if set(x.get("all_attempt_refs",[]))!=set(A): return {"aggregate":"INCONCLUSIVE","reasons":["all_attempt_refs_mismatch"]}
    for k,a in A.items():
        if a.get("attempt_id")!=k or a.get("candidate_generation_id")!=gid or a.get("scenario_id")!=sid:
            return {"aggregate":"INCONCLUSIVE","reasons":["attempt_identity_mismatch"]}
    if x.get("harness_defect"): return {"aggregate":"INCONCLUSIVE","reasons":["harness_defect"],"reopen_scope":"ALL_CANDIDATES_FOR_SCENARIO"}
    n=sorted([a for a in A.values() if a.get("kind")=="NORMAL"],key=lambda a:a.get("normal_index",0))
    if len(n)<2: return {"aggregate":"NOT_RUN","reasons":["fewer_than_two_normal_attempts"]}
    if any(not a.get("reset_verified") for a in n[:2]): return {"aggregate":"NOT_RUN","reasons":["independent_reset_not_verified"]}
    if len({a.get("reset_id") for a in n[:2]})<2: return {"aggregate":"NOT_RUN","reasons":["normal_attempts_reuse_reset_identity"]}
    if len({a.get("workspace_id") for a in n[:2]})<2: return {"aggregate":"NOT_RUN","reasons":["normal_attempts_reuse_workspace"]}
    if any(a.get("resource_class")!=START["resource_class"] for a in A.values()): return {"aggregate":"INCONCLUSIVE","reasons":["resource_class_mismatch"]}
    inj={a.get("injection_id"):a for a in A.values() if a.get("kind")=="FAILURE_INJECTION"}
    if any(i not in inj for i in s["required_injections"]): return {"aggregate":"NOT_RUN","reasons":["required_injection_attempt_missing"]}
    used=n+[inj[i] for i in s["required_injections"]]
    if any(a.get("failure_class") in ("INFRA","HARNESS","UNKNOWN") for a in used):
        return {"aggregate":"INCONCLUSIVE","reasons":["non_product_failure_class_present"]}
    nr=[a["result"] for a in n]; ir=[inj[i]["result"] for i in s["required_injections"]]
    if "PASS" in nr and "FAIL" in nr: return {"aggregate":"FLAKY","reasons":["normal_attempts_disagree"]}
    if any(r=="INCONCLUSIVE" for r in nr+ir): return {"aggregate":"INCONCLUSIVE","reasons":["inconclusive_attempt"]}
    if any(r!="PASS" for r in ir): return {"aggregate":"FAIL","reasons":["failure_recovery_assertion_failed"]}
    if all(r=="PASS" for r in nr): return {"aggregate":"PASS_FOR_COMPARISON","reasons":[]}
    return {"aggregate":"FAIL","reasons":["normal_required_behavior_failed"]}

def history(gs):
    if not gs:return {"valid":False,"reason":"empty_history","generations":[]}
    seen=set(); rec=[]; prev=None
    for g in gs:
        gid=g["generation_id"]
        if gid in seen:return {"valid":False,"reason":"generation_id_reused","generations":rec}
        seen.add(gid)
        if prev is None and g.get("predecessor_generation_id") is not None:return {"valid":False,"reason":"root_has_predecessor","generations":rec}
        if prev is not None:
            if g.get("predecessor_generation_id")!=prev["generation_id"]:return {"valid":False,"reason":"predecessor_link_missing_or_wrong","generations":rec}
            if g.get("candidate_work_id")==prev.get("candidate_work_id"):return {"valid":False,"reason":"repair_without_changed_work_identity","generations":rec}
            if not g.get("repair_change_ref"):return {"valid":False,"reason":"repair_change_ref_missing","generations":rec}
        rec.append({"generation_id":gid,"aggregate":aggregate(g)["aggregate"]}); prev=g
    return {"valid":True,"reason":None,"generations":rec}

FIX={}
def eq(fid,sid,mut=None,attempt_set=None,expected="ACCEPT"):
    a=adaptation(sid); mut and mut(a); FIX[fid]={"adaptation":a,"attempt_set":attempt_set,"expected":expected}
eq("EQ-01","S2"); eq("EQ-02","S7",lambda a:a.__setitem__("failure_injections",[]),expected="REJECT")
eq("EQ-03","S3",lambda a:a.__setitem__("mechanism_authority","ABSTRACT_SIMULATOR"),expected="REJECT")
eq("EQ-04","S6",lambda a:a["extra_evidence"].append("FRAME_STATE_IDENTITY"))
eq("EQ-05","S1",lambda a:a["start_profile"].__setitem__("cache_mode","UNDECLARED_WARM"),expected="REJECT")
eq("EQ-06","S8",lambda a:a["extra_evidence"].append("ADAPTER_PROFILE_PARSE"))
e7=aset("S9",normal=("FAIL","PASS")); e7["attempts"].pop("GEN-1-S9-N1"); eq("EQ-07","S9",attempt_set=e7,expected="REJECT")
eq("EQ-08","S9",lambda a:a["extra_evidence"].append("EXTRA_PLATFORM_PACKAGE"))
eq("EQ-09","S5",lambda a:a["bounds"].__setitem__("overlap_count",0),expected="REJECT")
eq("EQ-10","S2",lambda a:a.__setitem__("undocumented_manual_intervention",True),expected="REJECT")
eq("EQ-11","S4",lambda a:a["extra_evidence"].append("NATIVE_SERIALIZATION_EQUIVALENT"))
eq("EQ-12","S10",lambda a:a.__setitem__("hidden_context_transfer",True),expected="REJECT")
eq("EQ-13","S3",lambda a:a["bounds"].__setitem__("entity_count",16),expected="REJECT")
eq("EQ-14","S8",lambda a:a["start_profile"].__setitem__("resource_class","BIGGER-HOST-v1"),expected="REJECT")
eq("EQ-15","S1",lambda a:a["mappings"].pop("launch"),expected="REJECT")
EQ={}
for k,f in FIX.items():
    vr=validate(f["adaptation"]); overall=vr["result"]; ar=None
    if overall=="ACCEPT" and f.get("attempt_set") is not None:
        ar=aggregate(f["attempt_set"]); overall="ACCEPT" if ar["aggregate"]=="PASS_FOR_COMPARISON" else "REJECT"
    EQ[k]={"overall":overall,"adaptation":vr,"attempt":ar,"expected":f["expected"],"matches":overall==f["expected"]}

AG={
 "AG-01_clean":aset("S1"),"AG-02_disagree":aset("S1",normal=("PASS","FAIL")),"AG-03_one_normal":aset("S1",normal=("PASS",)),
 "AG-04_missing_injection":aset("S1"),"AG-05_same_reset":aset("S1",reset_ids=("RESET-1","RESET-1")),
 "AG-06_hidden_failed_attempt":aset("S9",normal=("FAIL","PASS")),"AG-07_infra_then_pass":aset("S1",normal=("FAIL","PASS"),classes=("INFRA","NONE")),
 "AG-08_injection_failure":aset("S1",injection_result="FAIL",injection_class="PRODUCT"),"AG-09_harness_defect":aset("S1",harness_defect=True),
 "AG-10_reset_unverified":aset("S1",reset_ok=(True,False)),"AG-11_workspace_reused":aset("S1",workspaces=("WS-1","WS-1")),
 "AG-12_stronger_resource":aset("S1",resource="BIGGER-HOST-v1"),"AG-13_three_attempt_flaky":aset("S1",normal=("PASS","FAIL","PASS")),
}
for aid in list(AG["AG-04_missing_injection"]["attempts"]):
    if AG["AG-04_missing_injection"]["attempts"][aid]["kind"]=="FAILURE_INJECTION":
        del AG["AG-04_missing_injection"]["attempts"][aid]; AG["AG-04_missing_injection"]["run_registry_refs"].remove(aid); AG["AG-04_missing_injection"]["all_attempt_refs"].remove(aid)
AG["AG-06_hidden_failed_attempt"]["attempts"].pop("GEN-1-S9-N1")
AGR={k:aggregate(v) for k,v in AG.items()}
EXP={"AG-01_clean":"PASS_FOR_COMPARISON","AG-02_disagree":"FLAKY","AG-03_one_normal":"NOT_RUN","AG-04_missing_injection":"NOT_RUN",
     "AG-05_same_reset":"NOT_RUN","AG-06_hidden_failed_attempt":"INCONCLUSIVE","AG-07_infra_then_pass":"INCONCLUSIVE","AG-08_injection_failure":"FAIL",
     "AG-09_harness_defect":"INCONCLUSIVE","AG-10_reset_unverified":"NOT_RUN","AG-11_workspace_reused":"NOT_RUN",
     "AG-12_stronger_resource":"INCONCLUSIVE","AG-13_three_attempt_flaky":"FLAKY"}
g1=aset("S1",gid="GEN-1",work="WORK-1",normal=("FAIL","FAIL"))
g2=aset("S1",gid="GEN-2",work="WORK-2",predecessor="GEN-1",repair="REPAIR-DIFF-1")
reuse=copy.deepcopy(g2); reuse["generation_id"]="GEN-1"; reuse["predecessor_generation_id"]="GEN-1"
for a in reuse["attempts"].values():a["candidate_generation_id"]="GEN-1"
nolink=copy.deepcopy(g2); nolink["predecessor_generation_id"]=None
same=copy.deepcopy(g2); same["candidate_work_id"]="WORK-1"
HIST={"HIST-01_repair_linked":[g1,g2],"HIST-02_generation_reuse":[g1,reuse],"HIST-03_missing_predecessor":[g1,nolink],"HIST-04_same_work_masquerade":[g1,same]}
HRES={k:history(v) for k,v in HIST.items()}
INPUTS={"equivalence":FIX,"aggregate":AG,"history":HIST}
RESULT={"equivalence_results":EQ,"aggregate_results":AGR,"history_results":HRES}

def main():
    assert all(x["matches"] for x in EQ.values())
    assert all(AGR[k]["aggregate"]==v for k,v in EXP.items())
    assert HRES["HIST-01_repair_linked"]["valid"] and [(x["generation_id"],x["aggregate"]) for x in HRES["HIST-01_repair_linked"]["generations"]]==[("GEN-1","FAIL"),("GEN-2","PASS_FOR_COMPARISON")]
    assert not HRES["HIST-02_generation_reuse"]["valid"] and not HRES["HIST-03_missing_predecessor"]["valid"] and not HRES["HIST-04_same_work_masquerade"]["valid"]
    assert AGR["AG-09_harness_defect"]["reopen_scope"]=="ALL_CANDIDATES_FOR_SCENARIO"
    print(json.dumps({k:v["overall"] for k,v in EQ.items()},sort_keys=True))
    print(json.dumps({k:v["aggregate"] for k,v in AGR.items()},sort_keys=True))
    print(json.dumps({k:v["valid"] for k,v in HRES.items()},sort_keys=True))
    for name,obj in [("validator_contract",IDENTITY),("feature_slice",FEATURE),("scenario_manifest",SCENARIOS),("fixture_inputs",INPUTS),("result_object",RESULT)]:
        print(name,digest(obj))
if __name__=="__main__":main()
