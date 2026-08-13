#!/usr/bin/env python3
"""W2-REM-ENG-05 deterministic engine-harness protocol validator v5."""
import copy,hashlib,json,math
D=lambda o:hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def sd(o):
 try:return D(o)
 except (TypeError,ValueError):return None
def txt(x):return isinstance(x,str) and bool(x.strip())
def tl(x,u=False):return isinstance(x,list) and all(txt(v) for v in x) and (not u or len(x)==len(set(x)))
def td(x):return isinstance(x,dict) and all(txt(k) for k in x)
def num(x):return type(x) in (int,float) and math.isfinite(x)
ID={"validator_id":"W2-ENG-PROTOCOL-VALIDATOR-v5","harness_id":"W2-ENG-HARNESS-v5","feature_slice_id":"W2-ENG-FEATURE-SLICE-v2","scenario_manifest_id":"W2-ENG-SCENARIO-INPUTS-v2","predecessor_validator_blob":"7837695c91365273b2c89f3852b401c2f127af54","review_work_sha":"c535bb9e94cb0da3aeb0d66dcc2606c034d7412f","review_status_comment":5276962394,"semantics":["common-input-bounds","adaptation-equivalence","adaptation-candidate-binding","adaptation-container-shape-closure","start-resource-parity","closed-kind-specific-attempt-schema","attempt-lineage","candidate-generation-binding","required-injection-uniqueness","closed-result-failure-envelope","malformed-result-failure-type-closure","one-to-one-retained-attempt-registry","aggregate-no-laundering","repair-generation-lineage","history-lineage-evidence-validity-split","failure-class-authority","harness-defect-reopen","fresh-continuation"]}
FEATURE={'feature_slice_id': 'W2-ENG-FEATURE-SLICE-v2', 'logical_state': {'entity_count': 32, 'world_width': 16, 'world_height': 16, 'fields_per_entity': ['entity_id', 'x', 'y', 'status', 'flags'], 'seed': 424242, 'normal_ticks': 600}, 'action_vocabulary': ['MOVE_NORTH', 'MOVE_SOUTH', 'MOVE_EAST', 'MOVE_WEST', 'INTERACT', 'OPEN_MENU', 'CONFIRM', 'CANCEL', 'SAVE', 'LOAD'], 'player_surface': {'screen_ids': ['BOOT_OR_MAIN', 'PLAY_SURFACE', 'SETTINGS'], 'required_routes': ['BOOT_OR_MAIN->PLAY_SURFACE', 'PLAY_SURFACE->SETTINGS', 'SETTINGS->PLAY_SURFACE'], 'input_classes': ['PRIMARY_POINTER_OR_KEYBOARD', 'CONTROLLER_OR_EQUIVALENT_SEMANTIC_ROUTE']}, 'assets': {'logical_asset_ids': ['ASSET-01', 'ASSET-02', 'ASSET-03', 'ASSET-04', 'ASSET-05', 'ASSET-06', 'ASSET-07', 'ASSET-08'], 'required_asset_count': 8, 'broken_reference_asset_id': 'ASSET-08'}, 'save_schema': {'v1_fields': ['schema_version', 'seed', 'tick', 'entities', 'settings'], 'v2_added_field': 'world_flags', 'v2_default': {}, 'malformed_fixture_id': 'SAVE-MALFORMED-UNSUPPORTED-v2'}, 'merge_fixture': {'branch_a_nonoverlap_changes': 1, 'branch_b_nonoverlap_changes': 1, 'semantic_overlap_locations': ['STATE:entity-07.status', 'UI:SETTINGS.control-02.label'], 'required_overlap_count': 2, 'generated_collision_required_when_candidate_has_generated_metadata': True}, 'capture_fixture': {'logical_state_marker': 'CAPTURE-STATE-042', 'viewport_width': 1280, 'viewport_height': 720, 'required_frame_count': 1}, 'profiling_fixture': {'normal_logical_updates': 19200, 'hotspot_extra_updates': 3200, 'hotspot_id': 'HOTSPOT-ENTITY-UPDATE-v2'}, 'package_fixture': {'target_id': 'WINDOWS_X64_DEV_PACKAGE-v1', 'required_entry_surface': 'BOOT_OR_MAIN', 'required_screen_count': 3, 'store_signing_required': False, 'clean_extract_launch_required': True}, 'continuation_fixture': {'partial_state_id': 'CONT-PARTIAL-v2', 'remaining_action_ids': ['CONT-A1', 'CONT-A2', 'CONT-A3'], 'required_handoff_fields': ['branch', 'head_sha', 'attempt_refs', 'failure_refs', 'remaining_actions', 'commands', 'next_acceptance_step'], 'negative_missing_field': 'next_acceptance_step'}}
SCENARIOS={'S1': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:action_vocabulary', 'SLICE:player_surface', 'SLICE:assets'], 'obligations': ['clean_reconstruct', 'build', 'launch', 'cold_start', 'incremental_observation'], 'min_bounds': {'entity_count': 32, 'asset_count': 8, 'screen_count': 3}, 'required_injections': ['FI-S1-CACHE-MISS-v2']}, 'S2': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:action_vocabulary', 'SLICE:player_surface', 'SLICE:assets'], 'obligations': ['fresh_agent_change', 'visible_or_state_visible_change', 'reviewable_diff', 'automated_verification'], 'min_bounds': {'entity_count': 32, 'asset_count': 8, 'screen_count': 3, 'changed_logical_locations': 1}, 'required_injections': ['FI-S2-STALE-META-v2']}, 'S3': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:action_vocabulary'], 'obligations': ['real_or_shared_rules', 'exact_seed_input', 'repeatable_state_events', 'perturbation_distinguishable'], 'min_bounds': {'entity_count': 32, 'normal_ticks': 600, 'action_count': 10}, 'required_injections': ['FI-S3-INPUT-PERTURB-v2'], 'required_mechanism_authority': 'REAL_OR_SHARED_RULES'}, 'S4': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:save_schema'], 'obligations': ['round_trip', 'schema_evolution', 'explicit_migration', 'malformed_tuple_diagnostic'], 'min_bounds': {'entity_count': 32, 'save_v1_field_count': 5, 'save_v2_added_field_count': 1}, 'required_injections': ['FI-S4-INCOMPAT-TUPLE-v2']}, 'S5': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:player_surface', 'SLICE:merge_fixture'], 'obligations': ['parallel_nonoverlap', 'intentional_overlap', 'visible_conflict', 'post_merge_checks'], 'min_bounds': {'overlap_count': 2, 'branch_a_nonoverlap': 1, 'branch_b_nonoverlap': 1}, 'required_injections': ['FI-S5-OVERLAP-v2']}, 'S6': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:player_surface', 'SLICE:capture_fixture'], 'obligations': ['reach_known_state', 'identity_bound_capture', 'state_vs_capture_failure_separated'], 'min_bounds': {'screen_count': 3, 'capture_frame_count': 1, 'viewport_width': 1280, 'viewport_height': 720}, 'required_injections': ['FI-S6-CAPTURE-DOWN-v2']}, 'S7': {'fixed_input_refs': ['SLICE:assets', 'SLICE:logical_state'], 'obligations': ['inject_broken_reference', 'diagnose_from_repo_cli', 'bounded_repair', 'rerun'], 'min_bounds': {'asset_count': 8, 'broken_reference_count': 1}, 'required_injections': ['FI-S7-BROKEN-REF-v2']}, 'S8': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:profiling_fixture'], 'obligations': ['representative_workload', 'parseable_profile', 'locate_injected_hotspot', 'resource_observations'], 'min_bounds': {'normal_logical_updates': 19200, 'hotspot_extra_updates': 3200}, 'required_injections': ['FI-S8-HOTSPOT-v2']}, 'S9': {'fixed_input_refs': ['SLICE:logical_state', 'SLICE:player_surface', 'SLICE:assets', 'SLICE:package_fixture'], 'obligations': ['produce_common_package_target', 'exact_repro_inputs', 'clean_extract_launch', 'typed_failed_package_diagnostic'], 'min_bounds': {'screen_count': 3, 'asset_count': 8}, 'required_injections': ['FI-S9-PACKAGE-CONFIG-v2'], 'required_package_target': 'WINDOWS_X64_DEV_PACKAGE-v1'}, 'S10': {'fixed_input_refs': ['SLICE:continuation_fixture', 'SLICE:logical_state', 'SLICE:player_surface'], 'obligations': ['repository_only_handoff', 'fresh_context_reconstruct', 'complete_remaining_actions', 'rerun_evidence'], 'min_bounds': {'remaining_action_count': 3, 'required_handoff_field_count': 7}, 'required_injections': ['FI-S10-HANDOFF-GAP-v2'], 'hidden_context_forbidden': True}}
START={"profile_id":"W2-ENG-START-COLD-v2","cache_mode":"COLD","generated_state_policy":"REGENERATE_FROM_REPO","resource_class":"W2-ENG-HOST-COMMON-v2"}
MATRIX={"PASS":{"NONE"},"FAIL":{"PRODUCT","INFRA","HARNESS","UNKNOWN"},"INCONCLUSIVE":{"PRODUCT","INFRA","HARNESS","UNKNOWN"},"NOT_RUN":{"NONE"}}
def adaptation(sid,cid="SYNTHETIC-CANDIDATE"):
 s=SCENARIOS[sid];return {"candidate_id":cid,"scenario_id":sid,"harness_id":ID["harness_id"],"feature_slice_id":FEATURE["feature_slice_id"],"fixed_input_refs":list(s["fixed_input_refs"]),"mappings":{x:"EQUIVALENT" for x in s["obligations"]},"bounds":dict(s["min_bounds"]),"failure_injections":list(s["required_injections"]),"start_profile":copy.deepcopy(START),"undocumented_manual_intervention":False,"resource_exception":False,"mechanism_authority":s.get("required_mechanism_authority","CANDIDATE_NATIVE_EQUIVALENT"),"package_target":s.get("required_package_target"),"hidden_context_transfer":False,"extra_evidence":[]}
def binding(a):
 if not isinstance(a,dict) or not txt(a.get("scenario_id")) or a.get("scenario_id") not in SCENARIOS or sd(a) is None:return None
 s=a["scenario_id"];return {"candidate_id":a.get("candidate_id"),"scenario_id":s,"harness_id":a.get("harness_id"),"feature_slice_id":a.get("feature_slice_id"),"scenario_contract_identity":D(SCENARIOS[s]),"adaptation_identity":sd(a)}
def va(a,cid=None):
 def R(r):return {"result":"REJECT","reasons":[r],"adaptation_identity":sd(a),"binding_id":None}
 if not isinstance(a,dict):return R("adaptation_not_object")
 if sd(a) is None:return R("adaptation_not_canonical_json")
 sid=a.get("scenario_id")
 if not txt(sid):return R("scenario_id_missing_or_invalid")
 if sid not in SCENARIOS:return R("unknown_scenario")
 s=SCENARIOS[sid];w=[];ac=a.get("candidate_id")
 if not txt(ac):w+=['candidate_id_missing_or_invalid']
 if cid is not None and (not txt(cid) or ac!=cid):w+=['candidate_id_mismatch']
 if a.get('harness_id')!=ID['harness_id']:w+=['harness_mismatch']
 if a.get('feature_slice_id')!=FEATURE['feature_slice_id']:w+=['feature_slice_mismatch']
 f=a.get('fixed_input_refs')
 if not tl(f,True):w+=['fixed_input_refs_invalid']
 elif not set(s['fixed_input_refs'])<=set(f):w+=['missing_common_input_ref']
 m=a.get('mappings')
 if not td(m):w+=['mappings_invalid']
 else:w += [f"missing_or_weaker_obligation:{x}" for x in s['obligations'] if m.get(x) not in ('EQUIVALENT','STRICTLY_STRONGER')]
 b=a.get('bounds')
 if not td(b):w+=['bounds_invalid']
 else:
  for k,v in s['min_bounds'].items():
   z=b.get(k)
   if not num(z):w += [f"bound_missing_or_invalid:{k}"]
   elif z<v:w += [f"shrunk_bound:{k}"]
 fi=a.get('failure_injections')
 if not tl(fi,True):w+=['failure_injections_invalid']
 elif not set(s['required_injections'])<=set(fi):w+=['required_failure_injection_missing']
 st=a.get('start_profile')
 if not isinstance(st,dict):w+=['start_profile_invalid']
 else:
  if st.get('cache_mode')!='COLD' or st.get('generated_state_policy')!='REGENERATE_FROM_REPO':w+=['hidden_or_noncommon_start_state']
  if st.get('resource_class')!=START['resource_class']:w+=['noncommon_resource_class']
 if a.get('resource_exception'):w+=['unresolved_resource_exception']
 if a.get('undocumented_manual_intervention'):w+=['hidden_manual_intervention']
 if s.get('required_mechanism_authority') and a.get('mechanism_authority')!=s['required_mechanism_authority']:w+=['lower_authority_mechanism']
 if s.get('required_package_target') and a.get('package_target')!=s['required_package_target']:w+=['common_package_target_missing']
 if s.get('hidden_context_forbidden') and a.get('hidden_context_transfer'):w+=['hidden_context_transfer']
 q=binding(a)
 if q is None:w+=['adaptation_binding_not_derivable']
 return {"result":"REJECT" if w else "ACCEPT","reasons":w,"adaptation_identity":sd(a),"binding_id":D(q) if q else None}
def attempt(aid,sid,gid,kind,result,ni=None,inj=None,fc='NONE',rid='R',rok=True,ws='W',res=START['resource_class'],cid='SYNTHETIC-CANDIDATE'):
 return {"attempt_id":aid,"scenario_id":sid,"candidate_id":cid,"candidate_generation_id":gid,"kind":kind,"normal_index":ni,"injection_id":inj,"result":result,"failure_class":fc,"reset_id":rid,"reset_verified":rok,"workspace_id":ws,"resource_class":res}
def gen(sid,gid='GEN-1',work='WORK-1',normal=('PASS','PASS'),classes=None,injres='PASS',injfc='NONE',resets=('R1','R2','R3'),oks=(True,True,True),wss=('W1','W2','W3'),res=START['resource_class'],defect=False,pred=None,repair=None,cid='SYNTHETIC-CANDIDATE'):
 classes=classes or tuple('NONE' if x=='PASS' else 'PRODUCT' for x in normal);a=adaptation(sid,cid);ats={};reg=[]
 for i,r in enumerate(normal,1):
  k=f'{gid}-{sid}-N{i}';reg.append(k);ats[k]=attempt(k,sid,gid,'NORMAL',r,i,fc=classes[i-1],rid=resets[i-1] if i-1<len(resets) else None,rok=oks[i-1] if i-1<len(oks) else False,ws=wss[i-1] if i-1<len(wss) else None,res=res,cid=cid)
 for i,x in enumerate(SCENARIOS[sid]['required_injections'],1):
  k=f'{gid}-{sid}-FI{i}';reg.append(k);ats[k]=attempt(k,sid,gid,'FAILURE_INJECTION',injres,inj=x,fc=injfc,rid=f'{gid}-RF{i}',ws=f'{gid}-WF{i}',res=res,cid=cid)
 return {"scenario_id":sid,"candidate_id":cid,"generation_id":gid,"candidate_work_id":work,"predecessor_generation_id":pred,"repair_change_ref":repair,"harness_defect":defect,"adaptation":a,"adaptation_binding_id":D(binding(a)),"attempts":ats,"run_registry_refs":reg,"all_attempt_refs":list(ats)}
def inv(r):return {"aggregate":"INCONCLUSIVE","reasons":[r],"valid_envelope":False}
def vr(v,ats,n):
 if not tl(v,True):return f'{n}_invalid_or_duplicate'
 if len(v)!=len(ats) or set(v)!=set(ats):return f'{n}_mismatch'
def vat(k,a,g,s,c):
 if not isinstance(a,dict):return 'attempt_not_object'
 if not txt(k) or a.get('attempt_id')!=k:return 'attempt_id_mismatch'
 if a.get('candidate_generation_id')!=g or a.get('scenario_id')!=s or a.get('candidate_id')!=c:return 'attempt_identity_mismatch'
 kind=a.get('kind')
 if kind not in ('NORMAL','FAILURE_INJECTION'):return 'unknown_attempt_kind'
 r,f=a.get('result'),a.get('failure_class')
 if not txt(r) or r not in MATRIX or not txt(f) or f not in MATRIX[r]:return 'invalid_result_failure_class_envelope'
 if not txt(a.get('reset_id')):return 'reset_id_missing_or_invalid'
 if type(a.get('reset_verified')) is not bool:return 'reset_verified_not_boolean'
 if not txt(a.get('workspace_id')):return 'workspace_id_missing_or_invalid'
 if not txt(a.get('resource_class')):return 'resource_class_missing_or_invalid'
 if kind=='NORMAL':
  x=a.get('normal_index')
  if type(x) is not int or x<=0:return 'normal_index_missing_or_invalid'
  if a.get('injection_id') is not None:return 'normal_attempt_has_injection_id'
 else:
  if a.get('normal_index') is not None:return 'failure_injection_has_normal_index'
  if not txt(a.get('injection_id')):return 'failure_injection_missing_injection_id'
def agg(g):
 if not isinstance(g,dict):return inv('generation_not_object')
 s,A,gid,c=g.get('scenario_id'),g.get('attempts',{}),g.get('generation_id'),g.get('candidate_id')
 if not txt(s) or s not in SCENARIOS:return inv('unknown_scenario')
 if not txt(gid) or not txt(c):return inv('generation_identity_missing_or_invalid')
 if not isinstance(A,dict):return inv('attempts_not_object')
 for n in ('run_registry_refs','all_attempt_refs'):
  z=vr(g.get(n),A,n)
  if z:return inv(z)
 a=g.get('adaptation');v=va(a,c)
 if v['result']!='ACCEPT' or not isinstance(a,dict) or a.get('scenario_id')!=s:return inv('adaptation_invalid_or_candidate_mismatch')
 q=binding(a)
 if not q or g.get('adaptation_binding_id')!=D(q):return inv('adaptation_binding_identity_mismatch')
 ix=[]
 for k,v in A.items():
  z=vat(k,v,gid,s,c)
  if z:return inv(z)
  if v['kind']=='NORMAL':ix.append(v['normal_index'])
 if len(ix)!=len(set(ix)):return inv('duplicate_normal_index')
 if g.get('harness_defect'):return {"aggregate":"INCONCLUSIVE","reasons":["harness_defect"],"reopen_scope":"ALL_CANDIDATES_FOR_SCENARIO","valid_envelope":True}
 N=sorted((x for x in A.values() if x['kind']=='NORMAL'),key=lambda x:x['normal_index'])
 if len(N)<2:return {"aggregate":"NOT_RUN","reasons":["fewer_than_two_normal_attempts"],"valid_envelope":True}
 if any(not x['reset_verified'] for x in N):return {"aggregate":"NOT_RUN","reasons":["independent_reset_not_verified"],"valid_envelope":True}
 if len({x['reset_id'] for x in N})!=len(N):return {"aggregate":"NOT_RUN","reasons":["normal_attempts_reuse_reset_identity"],"valid_envelope":True}
 if len({x['workspace_id'] for x in N})!=len(N):return {"aggregate":"NOT_RUN","reasons":["normal_attempts_reuse_workspace"],"valid_envelope":True}
 if any(x['resource_class']!=START['resource_class'] for x in A.values()):return {"aggregate":"INCONCLUSIVE","reasons":["resource_class_mismatch"],"valid_envelope":True}
 B={}
 for x in A.values():
  if x['kind']=='FAILURE_INJECTION':B.setdefault(x['injection_id'],[]).append(x)
 if any(len(v)!=1 for v in B.values()):return inv('duplicate_injection_id')
 req=SCENARIOS[s]['required_injections']
 if any(x not in B for x in req):return {"aggregate":"NOT_RUN","reasons":["required_injection_attempt_missing"],"valid_envelope":True}
 U=N+[B[x][0] for x in req]
 if any(x['failure_class'] in ('INFRA','HARNESS','UNKNOWN') for x in U):return {"aggregate":"INCONCLUSIVE","reasons":["non_product_failure_class_present"],"valid_envelope":True}
 nr=[x['result'] for x in N];ir=[B[x][0]['result'] for x in req]
 if 'PASS' in nr and 'FAIL' in nr:return {"aggregate":"FLAKY","reasons":["normal_attempts_disagree"],"valid_envelope":True}
 if any(x=='INCONCLUSIVE' for x in nr+ir):return {"aggregate":"INCONCLUSIVE","reasons":["inconclusive_attempt"],"valid_envelope":True}
 if any(x!='PASS' for x in ir):return {"aggregate":"FAIL","reasons":["failure_recovery_assertion_failed"],"valid_envelope":True}
 if all(x=='PASS' for x in nr):return {"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":True}
 return {"aggregate":"FAIL","reasons":["normal_required_behavior_failed"],"valid_envelope":True}
def hist(gs):
 if not isinstance(gs,list) or not gs:return {"valid":False,"lineage_valid":False,"evidence_valid":False,"reason":"empty_history","generations":[]}
 seen=set();out=[];p=None;c=gs[0].get('candidate_id') if isinstance(gs[0],dict) else None
 for g in gs:
  if not isinstance(g,dict):return {"valid":False,"lineage_valid":False,"evidence_valid":False,"reason":"generation_not_object","generations":out}
  gid=g.get('generation_id')
  if not txt(gid) or gid in seen:return {"valid":False,"lineage_valid":False,"evidence_valid":False,"reason":"generation_id_invalid_or_reused","generations":out}
  seen.add(gid)
  if g.get('candidate_id')!=c:return {"valid":False,"lineage_valid":False,"evidence_valid":False,"reason":"candidate_identity_changed_without_typed_transition","generations":out}
  if p is None and g.get('predecessor_generation_id') is not None:return {"valid":False,"lineage_valid":False,"evidence_valid":False,"reason":"root_has_predecessor","generations":out}
  if p is not None and (g.get('predecessor_generation_id')!=p['generation_id'] or g.get('candidate_work_id')==p.get('candidate_work_id') or not txt(g.get('repair_change_ref'))):return {"valid":False,"lineage_valid":False,"evidence_valid":False,"reason":"repair_lineage_invalid","generations":out}
  r=agg(g);out.append({"generation_id":gid,"aggregate":r['aggregate'],"valid_envelope":r.get('valid_envelope',True)});p=g
 ev=all(x['valid_envelope'] for x in out);return {"valid":ev,"lineage_valid":True,"evidence_valid":ev,"reason":None if ev else "generation_evidence_envelope_invalid","generations":out}
# Equivalence corpus: inherited EQ-01..05 and EQ-07..17.
EQ={}
def E(k,s,fn=None,exp='ACCEPT'):
 a=adaptation(s);fn and fn(a);EQ[k]=(va(a,'SYNTHETIC-CANDIDATE')['result'],exp)
E('EQ-01','S2');E('EQ-02','S7',lambda a:a.__setitem__('failure_injections',[]),'REJECT');E('EQ-03','S3',lambda a:a.__setitem__('mechanism_authority','ABSTRACT_SIMULATOR'),'REJECT');E('EQ-04','S6',lambda a:a['extra_evidence'].append('FRAME_STATE_IDENTITY'));E('EQ-05','S1',lambda a:a['start_profile'].__setitem__('cache_mode','UNDECLARED_WARM'),'REJECT');E('EQ-08','S9',lambda a:a['extra_evidence'].append('EXTRA_PLATFORM_PACKAGE'));E('EQ-09','S5',lambda a:a['bounds'].__setitem__('overlap_count',0),'REJECT');E('EQ-10','S2',lambda a:a.__setitem__('undocumented_manual_intervention',True),'REJECT');E('EQ-11','S4',lambda a:a['extra_evidence'].append('NATIVE_SERIALIZATION_EQUIVALENT'));E('EQ-12','S10',lambda a:a.__setitem__('hidden_context_transfer',True),'REJECT');E('EQ-13','S3',lambda a:a['bounds'].__setitem__('entity_count',16),'REJECT');E('EQ-14','S8',lambda a:a['start_profile'].__setitem__('resource_class','BIGGER-HOST-v1'),'REJECT');E('EQ-15','S1',lambda a:a['mappings'].pop('launch'),'REJECT');E('EQ-16','S1',lambda a:a.__setitem__('candidate_id','OTHER-CANDIDATE'),'REJECT');E('EQ-17','S1',lambda a:a.pop('candidate_id'),'REJECT')
e7=gen('S9',normal=('FAIL','PASS'));e7['attempts'].pop('GEN-1-S9-N1');EQ['EQ-07']=('REJECT' if agg(e7)['aggregate']!='PASS_FOR_COMPARISON' else 'ACCEPT','REJECT')
# Aggregate inherited truth classes AG-01..29.
AG={'AG-01_clean':gen('S1'),'AG-02_disagree':gen('S1',normal=('PASS','FAIL')),'AG-03_one_normal':gen('S1',normal=('PASS',)),'AG-04_missing_injection':gen('S1'),'AG-05_same_reset':gen('S1',resets=('R1','R1')),'AG-06_hidden_failed_attempt':gen('S9',normal=('FAIL','PASS')),'AG-07_infra_then_pass':gen('S1',normal=('FAIL','PASS'),classes=('INFRA','NONE')),'AG-08_injection_failure':gen('S1',injres='FAIL',injfc='PRODUCT'),'AG-09_harness_defect':gen('S1',defect=True),'AG-10_reset_unverified':gen('S1',oks=(True,False)),'AG-11_workspace_reused':gen('S1',wss=('W1','W1')),'AG-12_stronger_resource':gen('S1',res='BIGGER-HOST-v1'),'AG-13_three_attempt_flaky':gen('S1',normal=('PASS','FAIL','PASS'))}
for k in list(AG['AG-04_missing_injection']['attempts']):
 if AG['AG-04_missing_injection']['attempts'][k]['kind']=='FAILURE_INJECTION':del AG['AG-04_missing_injection']['attempts'][k];AG['AG-04_missing_injection']['run_registry_refs'].remove(k);AG['AG-04_missing_injection']['all_attempt_refs'].remove(k)
AG['AG-06_hidden_failed_attempt']['attempts'].pop('GEN-1-S9-N1')
d=gen('S1');x=SCENARIOS['S1']['required_injections'][0];k='GEN-1-S1-FI-RETAINED-FAIL';d['attempts'][k]=attempt(k,'S1','GEN-1','FAILURE_INJECTION','FAIL',inj=x,fc='PRODUCT',rid='RF',ws='WF');d['run_registry_refs'].append(k);d['all_attempt_refs'].append(k);AG['AG-14_duplicate_required_injection']=d
def mut(k,fn):g=gen('S1');fn(g);AG[k]=g
mut('AG-15_cross_candidate_normal',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('candidate_id','OTHER'));mut('AG-16_cross_candidate_injection',lambda g:g['attempts']['GEN-1-S1-FI1'].__setitem__('candidate_id','OTHER'));mut('AG-17_pass_product_envelope',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('failure_class','PRODUCT'));mut('AG-18_null_reset_id',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('reset_id',None));mut('AG-19_empty_reset_id',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('reset_id',''));mut('AG-20_null_workspace_id',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('workspace_id',None));mut('AG-21_empty_workspace_id',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('workspace_id',''));mut('AG-22_truthy_nonboolean_reset_verified',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('reset_verified',1));mut('AG-23_null_normal_index',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('normal_index',None));mut('AG-24_noninteger_normal_index',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('normal_index','1'));mut('AG-25_boolean_normal_index',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('normal_index',True));mut('AG-26_duplicate_normal_index',lambda g:g['attempts']['GEN-1-S1-N2'].__setitem__('normal_index',1));mut('AG-27_failure_injection_normal_index',lambda g:g['attempts']['GEN-1-S1-FI1'].__setitem__('normal_index',1));mut('AG-28_cross_candidate_adaptation_reuse',lambda g:(g.__setitem__('adaptation',adaptation('S1','OTHER-CANDIDATE')),g.__setitem__('adaptation_binding_id',D(binding(g['adaptation'])))));mut('AG-29_adaptation_binding_substitution',lambda g:g.__setitem__('adaptation_binding_id','0'*64))
# Review regressions AG-30..49.
mut('AG-30_unhashable_result',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('result',[]));mut('AG-31_unhashable_failure_class',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('failure_class',[]));mut('AG-32_duplicate_run_registry_ref',lambda g:g['run_registry_refs'].append(g['run_registry_refs'][0]));mut('AG-33_duplicate_all_attempt_ref',lambda g:g['all_attempt_refs'].append(g['all_attempt_refs'][0]));mut('AG-34_null_run_registry_refs',lambda g:g.__setitem__('run_registry_refs',None));mut('AG-35_null_all_attempt_refs',lambda g:g.__setitem__('all_attempt_refs',None))
def ma(k,f,v):
 def z(g):g['adaptation'][f]=v;g['adaptation_binding_id']=D(binding(g['adaptation'])) if binding(g['adaptation']) else None
 mut(k,z)
ma('AG-36_malformed_fixed_input_refs','fixed_input_refs',None);ma('AG-37_malformed_mappings','mappings',None);ma('AG-38_malformed_bounds','bounds',None);ma('AG-39_malformed_failure_injections','failure_injections',None);ma('AG-40_malformed_start_profile','start_profile',None);ma('AG-41_unhashable_adaptation_scenario_id','scenario_id',[]);mut('AG-42_dict_result',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('result',{}));mut('AG-43_dict_failure_class',lambda g:g['attempts']['GEN-1-S1-N1'].__setitem__('failure_class',{}));mut('AG-44_string_run_registry_refs',lambda g:g.__setitem__('run_registry_refs','GEN-1-S1-N1'));mut('AG-45_dict_all_attempt_refs',lambda g:g.__setitem__('all_attempt_refs',{}));ma('AG-46_list_mappings','mappings',[]);ma('AG-47_list_bounds','bounds',[]);ma('AG-48_dict_failure_injections','failure_injections',{});ma('AG-49_list_start_profile','start_profile',[])
EXPECTED={'AG-01_clean':'PASS_FOR_COMPARISON','AG-02_disagree':'FLAKY','AG-03_one_normal':'NOT_RUN','AG-04_missing_injection':'NOT_RUN','AG-05_same_reset':'NOT_RUN','AG-06_hidden_failed_attempt':'INCONCLUSIVE','AG-07_infra_then_pass':'INCONCLUSIVE','AG-08_injection_failure':'FAIL','AG-09_harness_defect':'INCONCLUSIVE','AG-10_reset_unverified':'NOT_RUN','AG-11_workspace_reused':'NOT_RUN','AG-12_stronger_resource':'INCONCLUSIVE','AG-13_three_attempt_flaky':'FLAKY'}
for k in AG:
 if k not in EXPECTED:EXPECTED[k]='INCONCLUSIVE'
# History inherited truth classes HIST-01..06.
g1=gen('S1',normal=('FAIL','FAIL'));g2=gen('S1',gid='GEN-2',work='WORK-2',pred='GEN-1',repair='REPAIR-DIFF-1');reuse=copy.deepcopy(g2);reuse['generation_id']='GEN-1';reuse['predecessor_generation_id']='GEN-1';[a.__setitem__('candidate_generation_id','GEN-1') for a in reuse['attempts'].values()];nolink=copy.deepcopy(g2);nolink['predecessor_generation_id']=None;same=copy.deepcopy(g2);same['candidate_work_id']='WORK-1';cross=copy.deepcopy(g2);cross['candidate_id']='OTHER';[a.__setitem__('candidate_id','OTHER') for a in cross['attempts'].values()];bad=copy.deepcopy(g2);bad['attempts']['GEN-2-S1-N1']['normal_index']=None
H={'HIST-01_repair_linked':[g1,g2],'HIST-02_generation_reuse':[g1,reuse],'HIST-03_missing_predecessor':[g1,nolink],'HIST-04_same_work_masquerade':[g1,same],'HIST-05_cross_candidate_generation':[g1,cross],'HIST-06_lineage_valid_evidence_invalid':[g1,bad]}
AR={k:agg(v) for k,v in AG.items()};HR={k:hist(v) for k,v in H.items()}
INPUTS={"equivalence":EQ,"aggregate":AG,"history":H,"result_failure_matrix":{k:sorted(v) for k,v in MATRIX.items()},"adaptation_binding_contract":{"fields":["candidate_id","scenario_id","harness_id","feature_slice_id","scenario_contract_identity","adaptation_identity"],"binding_id":"sha256(canonical_json(binding))"},"registry_contract":{"fields":["run_registry_refs","all_attempt_refs"],"shape":"list[nonempty_unique_attempt_id]","authority_rule":"cardinality_and_set_equality_to_exact_retained_attempt_keys"},"malformed_container_policy":"typed_structural_inconclusive_valid_envelope_false"}
RESULT={"equivalence_results":EQ,"aggregate_results":AR,"history_results":HR}
def main():
 assert all(a==b for a,b in EQ.values());assert {k:v['aggregate'] for k,v in AR.items()}==EXPECTED
 assert HR['HIST-01_repair_linked']['valid'] and not HR['HIST-06_lineage_valid_evidence_invalid']['valid'] and HR['HIST-06_lineage_valid_evidence_invalid']['lineage_valid'] and not HR['HIST-06_lineage_valid_evidence_invalid']['evidence_valid']
 for k in ('HIST-02_generation_reuse','HIST-03_missing_predecessor','HIST-04_same_work_masquerade','HIST-05_cross_candidate_generation'):assert not HR[k]['valid'] and not HR[k]['lineage_valid']
 for k in list(AG)[13:]:assert AR[k]['aggregate']=='INCONCLUSIVE' and not AR[k]['valid_envelope']
 assert AR['AG-09_harness_defect']['reopen_scope']=='ALL_CANDIDATES_FOR_SCENARIO'
 print(json.dumps({k:v[0] for k,v in EQ.items()},sort_keys=True));print(json.dumps({k:v['aggregate'] for k,v in AR.items()},sort_keys=True));print(json.dumps({k:{'valid':v['valid'],'lineage_valid':v['lineage_valid'],'evidence_valid':v['evidence_valid']} for k,v in HR.items()},sort_keys=True))
 for n,o in [('validator_contract',ID),('feature_slice',FEATURE),('scenario_manifest',SCENARIOS),('fixture_inputs',INPUTS),('result_object',RESULT)]:print(n,D(o))
if __name__=='__main__':main()
