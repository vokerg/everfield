#!/usr/bin/env python3
"""W2-REM-ENG-03 deterministic engine-harness protocol validator v3."""
import copy, hashlib, json, math
D=lambda x: hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
ID={"validator_id":"W2-ENG-PROTOCOL-VALIDATOR-v3","harness_id":"W2-ENG-HARNESS-v3","feature_slice_id":"W2-ENG-FEATURE-SLICE-v2","scenario_manifest_id":"W2-ENG-SCENARIO-INPUTS-v2","source_validator_blob":"e9699ad7d02e1d99fac6d9f41545bf9eeabe5d37","review_work_sha":"9fb365e2ad84c04d2e12305b38b40ddc30153530","semantics":["common-input-bounds","adaptation-equivalence","start-resource-parity","attempt-lineage","candidate-generation-binding","required-injection-uniqueness","closed-result-failure-envelope","aggregate-no-laundering","repair-generation-lineage","failure-class-authority","harness-defect-reopen","fresh-continuation"]}
FEATURE={"feature_slice_id":"W2-ENG-FEATURE-SLICE-v2","logical_state":{"entity_count":32,"world_width":16,"world_height":16,"fields_per_entity":["entity_id","x","y","status","flags"],"seed":424242,"normal_ticks":600},"action_vocabulary":["MOVE_NORTH","MOVE_SOUTH","MOVE_EAST","MOVE_WEST","INTERACT","OPEN_MENU","CONFIRM","CANCEL","SAVE","LOAD"],"player_surface":{"screen_ids":["BOOT_OR_MAIN","PLAY_SURFACE","SETTINGS"],"required_routes":["BOOT_OR_MAIN->PLAY_SURFACE","PLAY_SURFACE->SETTINGS","SETTINGS->PLAY_SURFACE"],"input_classes":["PRIMARY_POINTER_OR_KEYBOARD","CONTROLLER_OR_EQUIVALENT_SEMANTIC_ROUTE"]},"assets":{"logical_asset_ids":[f"ASSET-{i:02d}" for i in range(1,9)],"required_asset_count":8,"broken_reference_asset_id":"ASSET-08"},"save_schema":{"v1_fields":["schema_version","seed","tick","entities","settings"],"v2_added_field":"world_flags","v2_default":{},"malformed_fixture_id":"SAVE-MALFORMED-UNSUPPORTED-v2"},"merge_fixture":{"branch_a_nonoverlap_changes":1,"branch_b_nonoverlap_changes":1,"semantic_overlap_locations":["STATE:entity-07.status","UI:SETTINGS.control-02.label"],"required_overlap_count":2,"generated_collision_required_when_candidate_has_generated_metadata":True},"capture_fixture":{"logical_state_marker":"CAPTURE-STATE-042","viewport_width":1280,"viewport_height":720,"required_frame_count":1},"profiling_fixture":{"normal_logical_updates":19200,"hotspot_extra_updates":3200,"hotspot_id":"HOTSPOT-ENTITY-UPDATE-v2"},"package_fixture":{"target_id":"WINDOWS_X64_DEV_PACKAGE-v1","required_entry_surface":"BOOT_OR_MAIN","required_screen_count":3,"store_signing_required":False,"clean_extract_launch_required":True},"continuation_fixture":{"partial_state_id":"CONT-PARTIAL-v2","remaining_action_ids":["CONT-A1","CONT-A2","CONT-A3"],"required_handoff_fields":["branch","head_sha","attempt_refs","failure_refs","remaining_actions","commands","next_acceptance_step"],"negative_missing_field":"next_acceptance_step"}}
R={"S":"SLICE:logical_state","A":"SLICE:action_vocabulary","U":"SLICE:player_surface","X":"SLICE:assets","V":"SLICE:save_schema","M":"SLICE:merge_fixture","C":"SLICE:capture_fixture","P":"SLICE:profiling_fixture","K":"SLICE:package_fixture","T":"SLICE:continuation_fixture"}
def sc(refs,obs,bounds,inj,**kw):
 d={"fixed_input_refs":[R[x] for x in refs],"obligations":obs,"min_bounds":bounds,"required_injections":[inj]}; d.update(kw); return d
SCENARIOS={
"S1":sc("SAUX",["clean_reconstruct","build","launch","cold_start","incremental_observation"],{"entity_count":32,"asset_count":8,"screen_count":3},"FI-S1-CACHE-MISS-v2"),
"S2":sc("SAUX",["fresh_agent_change","visible_or_state_visible_change","reviewable_diff","automated_verification"],{"entity_count":32,"asset_count":8,"screen_count":3,"changed_logical_locations":1},"FI-S2-STALE-META-v2"),
"S3":sc("SA",["real_or_shared_rules","exact_seed_input","repeatable_state_events","perturbation_distinguishable"],{"entity_count":32,"normal_ticks":600,"action_count":10},"FI-S3-INPUT-PERTURB-v2",required_mechanism_authority="REAL_OR_SHARED_RULES"),
"S4":sc("SV",["round_trip","schema_evolution","explicit_migration","malformed_tuple_diagnostic"],{"entity_count":32,"save_v1_field_count":5,"save_v2_added_field_count":1},"FI-S4-INCOMPAT-TUPLE-v2"),
"S5":sc("SUM",["parallel_nonoverlap","intentional_overlap","visible_conflict","post_merge_checks"],{"overlap_count":2,"branch_a_nonoverlap":1,"branch_b_nonoverlap":1},"FI-S5-OVERLAP-v2"),
"S6":sc("SUC",["reach_known_state","identity_bound_capture","state_vs_capture_failure_separated"],{"screen_count":3,"capture_frame_count":1,"viewport_width":1280,"viewport_height":720},"FI-S6-CAPTURE-DOWN-v2"),
"S7":sc("XS",["inject_broken_reference","diagnose_from_repo_cli","bounded_repair","rerun"],{"asset_count":8,"broken_reference_count":1},"FI-S7-BROKEN-REF-v2"),
"S8":sc("SP",["representative_workload","parseable_profile","locate_injected_hotspot","resource_observations"],{"normal_logical_updates":19200,"hotspot_extra_updates":3200},"FI-S8-HOTSPOT-v2"),
"S9":sc("SUXK",["produce_common_package_target","exact_repro_inputs","clean_extract_launch","typed_failed_package_diagnostic"],{"screen_count":3,"asset_count":8},"FI-S9-PACKAGE-CONFIG-v2",required_package_target="WINDOWS_X64_DEV_PACKAGE-v1"),
"S10":sc("TSU",["repository_only_handoff","fresh_context_reconstruct","complete_remaining_actions","rerun_evidence"],{"remaining_action_count":3,"required_handoff_field_count":7},"FI-S10-HANDOFF-GAP-v2",hidden_context_forbidden=True)}
START={"profile_id":"W2-ENG-START-COLD-v2","cache_mode":"COLD","generated_state_policy":"REGENERATE_FROM_REPO","resource_class":"W2-ENG-HOST-COMMON-v2"}
MATRIX={"PASS":{"NONE"},"FAIL":{"PRODUCT","INFRA","HARNESS","UNKNOWN"},"INCONCLUSIVE":{"PRODUCT","INFRA","HARNESS","UNKNOWN"},"NOT_RUN":{"NONE"}}
def adapt(sid):
 s=SCENARIOS[sid]; return {"candidate_id":"SYNTHETIC-CANDIDATE","scenario_id":sid,"harness_id":ID["harness_id"],"feature_slice_id":FEATURE["feature_slice_id"],"fixed_input_refs":list(s["fixed_input_refs"]),"mappings":{x:"EQUIVALENT" for x in s["obligations"]},"bounds":dict(s["min_bounds"]),"failure_injections":list(s["required_injections"]),"start_profile":copy.deepcopy(START),"undocumented_manual_intervention":False,"resource_exception":False,"mechanism_authority":s.get("required_mechanism_authority","CANDIDATE_NATIVE_EQUIVALENT"),"package_target":s.get("required_package_target"),"hidden_context_transfer":False,"extra_evidence":[]}
def validate(a):
 sid=a.get("scenario_id"); why=[]
 if sid not in SCENARIOS:return {"result":"REJECT","reasons":["unknown_scenario"]}
 s=SCENARIOS[sid]
 if a.get("harness_id")!=ID["harness_id"]:why+=['harness_mismatch']
 if a.get("feature_slice_id")!=FEATURE["feature_slice_id"]:why+=['feature_slice_mismatch']
 if not set(s["fixed_input_refs"])<=set(a.get("fixed_input_refs",[])):why+=['missing_common_input_ref']
 why += [f"missing_or_weaker_obligation:{x}" for x in s["obligations"] if a.get("mappings",{}).get(x) not in ("EQUIVALENT","STRICTLY_STRONGER")]
 why += [f"shrunk_bound:{k}" for k,v in s["min_bounds"].items() if a.get("bounds",{}).get(k,-math.inf)<v]
 if not set(s["required_injections"])<=set(a.get("failure_injections",[])):why+=['required_failure_injection_missing']
 st=a.get("start_profile",{})
 if st.get("cache_mode")!="COLD" or st.get("generated_state_policy")!="REGENERATE_FROM_REPO":why+=['hidden_or_noncommon_start_state']
 if st.get("resource_class")!=START["resource_class"]:why+=['noncommon_resource_class']
 if a.get("resource_exception"):why+=['unresolved_resource_exception']
 if a.get("undocumented_manual_intervention"):why+=['hidden_manual_intervention']
 if s.get("required_mechanism_authority") and a.get("mechanism_authority")!=s["required_mechanism_authority"]:why+=['lower_authority_mechanism']
 if s.get("required_package_target") and a.get("package_target")!=s["required_package_target"]:why+=['common_package_target_missing']
 if s.get("hidden_context_forbidden") and a.get("hidden_context_transfer"):why+=['hidden_context_transfer']
 return {"result":"REJECT" if why else "ACCEPT","reasons":why}
def attempt(aid,sid,gid,kind,result,ni=None,inj=None,fc="NONE",rid=None,rok=True,ws=None,res=START["resource_class"],cid="SYNTHETIC-CANDIDATE"):
 return {"attempt_id":aid,"scenario_id":sid,"candidate_id":cid,"candidate_generation_id":gid,"kind":kind,"normal_index":ni,"injection_id":inj,"result":result,"failure_class":fc,"reset_id":rid,"reset_verified":rok,"workspace_id":ws,"resource_class":res}
def aset(sid,gid="GEN-1",work="WORK-1",normal=("PASS","PASS"),classes=None,ir="PASS",ic="NONE",resets=("R1","R2","R3"),resetok=(True,True,True),wss=("W1","W2","W3"),resource=START["resource_class"],defect=False,pred=None,repair=None,cid="SYNTHETIC-CANDIDATE"):
 classes=classes or tuple("NONE" if x=="PASS" else "PRODUCT" for x in normal); A={}; reg=[]
 for i,r in enumerate(normal,1):
  aid=f"{gid}-{sid}-N{i}";reg.append(aid);A[aid]=attempt(aid,sid,gid,"NORMAL",r,i,fc=classes[i-1],rid=resets[i-1] if i-1<len(resets) else None,rok=resetok[i-1] if i-1<len(resetok) else False,ws=wss[i-1] if i-1<len(wss) else None,res=resource,cid=cid)
 for i,inj in enumerate(SCENARIOS[sid]["required_injections"],1):
  aid=f"{gid}-{sid}-FI{i}";reg.append(aid);A[aid]=attempt(aid,sid,gid,"FAILURE_INJECTION",ir,inj=inj,fc=ic,rid=f"{gid}-RF{i}",ws=f"{gid}-WF{i}",res=resource,cid=cid)
 return {"scenario_id":sid,"candidate_id":cid,"generation_id":gid,"candidate_work_id":work,"predecessor_generation_id":pred,"repair_change_ref":repair,"harness_defect":defect,"attempts":A,"run_registry_refs":reg,"all_attempt_refs":list(A)}
def bad(reason):return {"aggregate":"INCONCLUSIVE","reasons":[reason],"valid_envelope":False}
def aggregate(x):
 sid=x.get("scenario_id");A=x.get("attempts",{});gid=x.get("generation_id");cid=x.get("candidate_id")
 if sid not in SCENARIOS:return bad("unknown_scenario")
 if set(x.get("run_registry_refs",[]))!=set(A):return bad("attempt_registry_omission_or_extra")
 if set(x.get("all_attempt_refs",[]))!=set(A):return bad("all_attempt_refs_mismatch")
 for k,a in A.items():
  if a.get("attempt_id")!=k or a.get("candidate_generation_id")!=gid or a.get("scenario_id")!=sid or a.get("candidate_id")!=cid:return bad("attempt_identity_mismatch")
  if a.get("kind") not in ("NORMAL","FAILURE_INJECTION"):return bad("unknown_attempt_kind")
  r,fc=a.get("result"),a.get("failure_class")
  if r not in MATRIX or fc not in MATRIX[r]:return bad("invalid_result_failure_class_envelope")
  if a["kind"]=="NORMAL" and a.get("injection_id") is not None:return bad("normal_attempt_has_injection_id")
  if a["kind"]=="FAILURE_INJECTION" and not a.get("injection_id"):return bad("failure_injection_missing_injection_id")
 if x.get("harness_defect"):return {"aggregate":"INCONCLUSIVE","reasons":["harness_defect"],"reopen_scope":"ALL_CANDIDATES_FOR_SCENARIO","valid_envelope":True}
 n=sorted((a for a in A.values() if a["kind"]=="NORMAL"),key=lambda a:a.get("normal_index",0))
 if len(n)<2:return {"aggregate":"NOT_RUN","reasons":["fewer_than_two_normal_attempts"],"valid_envelope":True}
 if any(not a.get("reset_verified") for a in n[:2]):return {"aggregate":"NOT_RUN","reasons":["independent_reset_not_verified"],"valid_envelope":True}
 if len({a.get("reset_id") for a in n[:2]})<2:return {"aggregate":"NOT_RUN","reasons":["normal_attempts_reuse_reset_identity"],"valid_envelope":True}
 if len({a.get("workspace_id") for a in n[:2]})<2:return {"aggregate":"NOT_RUN","reasons":["normal_attempts_reuse_workspace"],"valid_envelope":True}
 if any(a.get("resource_class")!=START["resource_class"] for a in A.values()):return {"aggregate":"INCONCLUSIVE","reasons":["resource_class_mismatch"],"valid_envelope":True}
 by={}
 for a in A.values():
  if a["kind"]=="FAILURE_INJECTION":by.setdefault(a["injection_id"],[]).append(a)
 dup=sorted(k for k,v in by.items() if len(v)!=1)
 if dup:return bad("duplicate_injection_id:"+",".join(dup))
 req=SCENARIOS[sid]["required_injections"]
 if any(i not in by for i in req):return {"aggregate":"NOT_RUN","reasons":["required_injection_attempt_missing"],"valid_envelope":True}
 used=n+[by[i][0] for i in req]
 if any(a["failure_class"] in ("INFRA","HARNESS","UNKNOWN") for a in used):return {"aggregate":"INCONCLUSIVE","reasons":["non_product_failure_class_present"],"valid_envelope":True}
 nr=[a["result"] for a in n];ir=[by[i][0]["result"] for i in req]
 if "PASS" in nr and "FAIL" in nr:return {"aggregate":"FLAKY","reasons":["normal_attempts_disagree"],"valid_envelope":True}
 if any(r=="INCONCLUSIVE" for r in nr+ir):return {"aggregate":"INCONCLUSIVE","reasons":["inconclusive_attempt"],"valid_envelope":True}
 if any(r!="PASS" for r in ir):return {"aggregate":"FAIL","reasons":["failure_recovery_assertion_failed"],"valid_envelope":True}
 if all(r=="PASS" for r in nr):return {"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":True}
 return {"aggregate":"FAIL","reasons":["normal_required_behavior_failed"],"valid_envelope":True}
def history(gs):
 if not gs:return {"valid":False,"reason":"empty_history","generations":[]}
 seen=set();out=[];prev=None;cid=gs[0].get("candidate_id")
 for g in gs:
  gid=g["generation_id"]
  if gid in seen:return {"valid":False,"reason":"generation_id_reused","generations":out}
  seen.add(gid)
  if g.get("candidate_id")!=cid:return {"valid":False,"reason":"candidate_identity_changed_without_typed_transition","generations":out}
  if prev is None and g.get("predecessor_generation_id") is not None:return {"valid":False,"reason":"root_has_predecessor","generations":out}
  if prev is not None:
   if g.get("predecessor_generation_id")!=prev["generation_id"]:return {"valid":False,"reason":"predecessor_link_missing_or_wrong","generations":out}
   if g.get("candidate_work_id")==prev.get("candidate_work_id"):return {"valid":False,"reason":"repair_without_changed_work_identity","generations":out}
   if not g.get("repair_change_ref"):return {"valid":False,"reason":"repair_change_ref_missing","generations":out}
  a=aggregate(g);out.append({"generation_id":gid,"aggregate":a["aggregate"],"valid_envelope":a.get("valid_envelope",True)});prev=g
 return {"valid":True,"reason":None,"generations":out}
# Preserve EQ-01..15 outcomes.
FIX={}
def eq(i,s,mut=None,att=None,exp="ACCEPT"):
 a=adapt(s);mut and mut(a);FIX[i]={"adaptation":a,"attempt_set":att,"expected":exp}
eq("EQ-01","S2");eq("EQ-02","S7",lambda a:a.__setitem__("failure_injections",[]),exp="REJECT");eq("EQ-03","S3",lambda a:a.__setitem__("mechanism_authority","ABSTRACT_SIMULATOR"),exp="REJECT");eq("EQ-04","S6",lambda a:a["extra_evidence"].append("FRAME_STATE_IDENTITY"));eq("EQ-05","S1",lambda a:a["start_profile"].__setitem__("cache_mode","UNDECLARED_WARM"),exp="REJECT");eq("EQ-06","S8",lambda a:a["extra_evidence"].append("ADAPTER_PROFILE_PARSE"));e7=aset("S9",normal=("FAIL","PASS"));e7["attempts"].pop("GEN-1-S9-N1");eq("EQ-07","S9",att=e7,exp="REJECT");eq("EQ-08","S9",lambda a:a["extra_evidence"].append("EXTRA_PLATFORM_PACKAGE"));eq("EQ-09","S5",lambda a:a["bounds"].__setitem__("overlap_count",0),exp="REJECT");eq("EQ-10","S2",lambda a:a.__setitem__("undocumented_manual_intervention",True),exp="REJECT");eq("EQ-11","S4",lambda a:a["extra_evidence"].append("NATIVE_SERIALIZATION_EQUIVALENT"));eq("EQ-12","S10",lambda a:a.__setitem__("hidden_context_transfer",True),exp="REJECT");eq("EQ-13","S3",lambda a:a["bounds"].__setitem__("entity_count",16),exp="REJECT");eq("EQ-14","S8",lambda a:a["start_profile"].__setitem__("resource_class","BIGGER-HOST-v1"),exp="REJECT");eq("EQ-15","S1",lambda a:a["mappings"].pop("launch"),exp="REJECT")
EQ={}
for k,f in FIX.items():
 v=validate(f["adaptation"]);o=v["result"];ar=None
 if o=="ACCEPT" and f["attempt_set"] is not None:ar=aggregate(f["attempt_set"]);o="ACCEPT" if ar["aggregate"]=="PASS_FOR_COMPARISON" else "REJECT"
 EQ[k]={"overall":o,"adaptation":v,"attempt":ar,"expected":f["expected"],"matches":o==f["expected"]}
AG={"AG-01_clean":aset("S1"),"AG-02_disagree":aset("S1",normal=("PASS","FAIL")),"AG-03_one_normal":aset("S1",normal=("PASS",)),"AG-04_missing_injection":aset("S1"),"AG-05_same_reset":aset("S1",resets=("R1","R1")),"AG-06_hidden_failed_attempt":aset("S9",normal=("FAIL","PASS")),"AG-07_infra_then_pass":aset("S1",normal=("FAIL","PASS"),classes=("INFRA","NONE")),"AG-08_injection_failure":aset("S1",ir="FAIL",ic="PRODUCT"),"AG-09_harness_defect":aset("S1",defect=True),"AG-10_reset_unverified":aset("S1",resetok=(True,False)),"AG-11_workspace_reused":aset("S1",wss=("W1","W1")),"AG-12_stronger_resource":aset("S1",resource="BIGGER-HOST-v1"),"AG-13_three_attempt_flaky":aset("S1",normal=("PASS","FAIL","PASS"))}
for aid in list(AG["AG-04_missing_injection"]["attempts"]):
 if AG["AG-04_missing_injection"]["attempts"][aid]["kind"]=="FAILURE_INJECTION":
  del AG["AG-04_missing_injection"]["attempts"][aid];AG["AG-04_missing_injection"]["run_registry_refs"].remove(aid);AG["AG-04_missing_injection"]["all_attempt_refs"].remove(aid)
AG["AG-06_hidden_failed_attempt"]["attempts"].pop("GEN-1-S9-N1")
dup=aset("S1");inj=SCENARIOS["S1"]["required_injections"][0];aid="GEN-1-S1-FI-RETAINED-FAIL";dup["attempts"][aid]=attempt(aid,"S1","GEN-1","FAILURE_INJECTION","FAIL",inj=inj,fc="PRODUCT",rid="RF",ws="WF");dup["run_registry_refs"].append(aid);dup["all_attempt_refs"].append(aid);AG["AG-14_duplicate_required_injection"]=dup
cn=aset("S1");cn["attempts"]["GEN-1-S1-N1"]["candidate_id"]="OTHER";AG["AG-15_cross_candidate_normal"]=cn
ci=aset("S1");ci["attempts"]["GEN-1-S1-FI1"]["candidate_id"]="OTHER";AG["AG-16_cross_candidate_injection"]=ci
mp=aset("S1");mp["attempts"]["GEN-1-S1-N1"]["failure_class"]="PRODUCT";AG["AG-17_pass_product_envelope"]=mp
AGR={k:aggregate(v) for k,v in AG.items()};EXP=["PASS_FOR_COMPARISON","FLAKY","NOT_RUN","NOT_RUN","NOT_RUN","INCONCLUSIVE","INCONCLUSIVE","FAIL","INCONCLUSIVE","NOT_RUN","NOT_RUN","INCONCLUSIVE","FLAKY","INCONCLUSIVE","INCONCLUSIVE","INCONCLUSIVE","INCONCLUSIVE"]
g1=aset("S1",normal=("FAIL","FAIL"));g2=aset("S1",gid="GEN-2",work="WORK-2",pred="GEN-1",repair="REPAIR-DIFF-1");reuse=copy.deepcopy(g2);reuse["generation_id"]="GEN-1";reuse["predecessor_generation_id"]="GEN-1";[a.__setitem__("candidate_generation_id","GEN-1") for a in reuse["attempts"].values()];nolink=copy.deepcopy(g2);nolink["predecessor_generation_id"]=None;same=copy.deepcopy(g2);same["candidate_work_id"]="WORK-1";cross=copy.deepcopy(g2);cross["candidate_id"]="OTHER";[a.__setitem__("candidate_id","OTHER") for a in cross["attempts"].values()]
HIST={"HIST-01_repair_linked":[g1,g2],"HIST-02_generation_reuse":[g1,reuse],"HIST-03_missing_predecessor":[g1,nolink],"HIST-04_same_work_masquerade":[g1,same],"HIST-05_cross_candidate_generation":[g1,cross]};HRES={k:history(v) for k,v in HIST.items()}
INPUTS={"equivalence":FIX,"aggregate":AG,"history":HIST,"result_failure_matrix":{k:sorted(v) for k,v in MATRIX.items()}};RESULT={"equivalence_results":EQ,"aggregate_results":AGR,"history_results":HRES}
def main():
 assert all(x["matches"] for x in EQ.values());assert [x["aggregate"] for x in AGR.values()]==EXP;assert HRES["HIST-01_repair_linked"]["valid"] and [(x["generation_id"],x["aggregate"]) for x in HRES["HIST-01_repair_linked"]["generations"]]==[("GEN-1","FAIL"),("GEN-2","PASS_FOR_COMPARISON")];assert all(not HRES[k]["valid"] for k in list(HRES)[1:]);assert AGR["AG-09_harness_defect"]["reopen_scope"]=="ALL_CANDIDATES_FOR_SCENARIO";assert all(not AGR[k]["valid_envelope"] for k in list(AGR)[13:])
 print(json.dumps({k:v["overall"] for k,v in EQ.items()},sort_keys=True));print(json.dumps({k:v["aggregate"] for k,v in AGR.items()},sort_keys=True));print(json.dumps({k:v["valid"] for k,v in HRES.items()},sort_keys=True))
 for n,o in [("validator_contract",ID),("feature_slice",FEATURE),("scenario_manifest",SCENARIOS),("fixture_inputs",INPUTS),("result_object",RESULT)]:print(n,D(o))
if __name__=="__main__":main()
