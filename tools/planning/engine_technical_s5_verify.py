#!/usr/bin/env python3
"""Independent fail-closed verifier for W2-ENG-TECH-S5-01 retained evidence."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, pathlib
from typing import Any

INJECTION='FI-S5-OVERLAP-v2'
SPEC={
 'Bevy': {'state':'src/state.rs','ui':'src/ui.rs','a':'src/branch_a.rs','b':'src/branch_b.rs'},
 'Godot': {'state':'state.gd','ui':'settings.gd','a':'branch_a.gd','b':'branch_b.gd'},
 'Defold': {'state':'state.lua','ui':'settings.lua','a':'branch_a.lua','b':'branch_b.lua'},
}

def J(o:Any)->str:return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=True)
def H(o:Any)->str:return hashlib.sha256(J(o).encode()).hexdigest()
def load(path,name):
 s=importlib.util.spec_from_file_location(name,path)
 if not s or not s.loader: raise RuntimeError(path)
 m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def semantic(record:dict[str,Any])->dict[str,Any]:
 reasons=[]; c=record.get('candidate'); sp=SPEC.get(c)
 if not sp:return {'ok':False,'reasons':['unknown_candidate']}
 src=record.get('source') or {}
 mapping={'STATE:entity-07.status':sp['state'],'UI:SETTINGS.control-02.label':sp['ui'],'branch_a_nonoverlap':sp['a'],'branch_b_nonoverlap':sp['b']}
 if src.get('semantic_mapping')!=mapping:reasons.append('semantic_mapping_mismatch')
 if src.get('candidate_validation',{}).get('ok') is not True:reasons.append('candidate_native_validation_failed')
 fc=src.get('file_checks') or {}; checks=fc.get('checks') or {}
 if fc.get('ok') is not True or not checks or not all(x is True for x in checks.values()):reasons.append('file_checks_failed')
 md=src.get('generated_metadata') or {}
 if md.get('relevant_to_represented_edit_surface') is not False or md.get('collision_required') is not False:reasons.append('metadata_classification_invalid')
 if not src.get('final_tree'):reasons.append('final_tree_missing')
 label=record.get('label'); expected_direction={'N1':'A_THEN_B','N2':'B_THEN_A','FI1':'A_THEN_B'}.get(label)
 if record.get('direction')!=expected_direction or src.get('direction')!=expected_direction:reasons.append('direction_mismatch')
 mode=record.get('mode')
 if mode=='NORMAL':
  if record.get('required_injection') is not None:reasons.append('normal_injection_nonnull')
  if src.get('branch_a_changed_files')!=[sp['a']]:reasons.append('normal_a_scope')
  if src.get('branch_b_changed_files')!=[sp['b']]:reasons.append('normal_b_scope')
  if src.get('merge_exit')!=0 or src.get('unmerged_paths')!=[]:reasons.append('normal_merge_not_clean')
  if src.get('resolution') is not None:reasons.append('normal_resolution_unexpected')
  mk=src.get('conflict_markers') or {}
  if set(mk)!={sp['state'],sp['ui']} or any(mk.values()):reasons.append('normal_markers_invalid')
 elif mode=='INJECT':
  if record.get('required_injection')!=INJECTION:reasons.append('injection_id_mismatch')
  if set(src.get('branch_a_changed_files') or [])!={sp['a'],sp['state'],sp['ui']}:reasons.append('inject_a_scope')
  if set(src.get('branch_b_changed_files') or [])!={sp['b'],sp['state'],sp['ui']}:reasons.append('inject_b_scope')
  if src.get('merge_exit') in (0,None):reasons.append('overlap_not_rejected')
  if set(src.get('unmerged_paths') or [])!={sp['state'],sp['ui']}:reasons.append('unmerged_paths_mismatch')
  mk=src.get('conflict_markers') or {}
  if set(mk)!={sp['state'],sp['ui']} or not all(mk.values()):reasons.append('conflict_markers_missing')
  if src.get('resolution')!={'state_choice':'branch-a/ACTIVE','ui_choice':'branch-b/Volume'}:reasons.append('resolution_mismatch')
 else:reasons.append('mode_invalid')
 reset=record.get('reset_proof') or {}
 if not (record.get('reset_verified_derived') is True and reset.get('pre_workspace_absent') is True and reset.get('workspace_created_exclusive') is True and reset.get('workspace_id') and reset.get('reset_id')):reasons.append('reset_invalid')
 expected_pass=not reasons
 if record.get('formal_result')!=('PASS' if expected_pass else 'INCONCLUSIVE'):reasons.append('formal_result_not_derived')
 if record.get('failure_class')!=('NONE' if expected_pass else 'HARNESS'):reasons.append('failure_class_not_derived')
 return {'ok':not reasons,'reasons':sorted(set(reasons))}

def candidate(packet:dict[str,Any],v)->dict[str,Any]:
 reasons=[]; ci=packet.get('candidate_identity') or {}; body=ci.get('body')
 if not isinstance(body,dict) or ci.get('identity_digest')!='sha256:'+H(body):reasons.append('candidate_identity_digest')
 raws=packet.get('raw_attempts') or []
 for x in raws:
  if x.get('digest')!='sha256:'+H(x.get('record')):reasons.append('raw_digest')
  sem=semantic(x.get('record') or {})
  reasons.extend('semantic:'+r for r in sem['reasons'])
 proofs=[x.get('record',{}).get('reset_proof',{}) for x in raws]
 if len({p.get('workspace_id') for p in proofs})!=len(proofs):reasons.append('workspace_reuse')
 if len({p.get('reset_id') for p in proofs})!=len(proofs):reasons.append('reset_reuse')
 g=packet.get('generation') or {}; refs=g.get('run_registry_refs') or []; binds=packet.get('source_bindings') or {}
 if len(refs)!=len(raws) or set(refs)!=set(binds):reasons.append('registry_binding_shape')
 for ref,x in zip(refs,raws):
  if binds.get(ref)!=x.get('digest'):reasons.append('source_binding')
  f=(g.get('attempts') or {}).get(ref,{}) ; r=x.get('record') or {}; p=r.get('reset_proof') or {}
  if (f.get('candidate_id'),f.get('result'),f.get('failure_class'))!=(r.get('candidate'),r.get('formal_result'),r.get('failure_class')):reasons.append('formal_raw_result')
  if (f.get('reset_id'),f.get('workspace_id'),f.get('reset_verified'))!=(p.get('reset_id'),p.get('workspace_id'),r.get('reset_verified_derived')):reasons.append('formal_raw_reset')
 ident=packet.get('identity_derivation') or {}; run_id=ident.get('run_identity'); adaptation=ident.get('adaptation_identity')
 deriv={'candidate':g.get('candidate_id'),'candidate_identity_digest':ci.get('identity_digest'),'raw_attempt_digests':[x.get('digest') for x in raws],'adaptation_identity':adaptation,'run_identity':run_id,'scenario':'S5'}
 work='WORK-S5-'+H(deriv)[:24]; gid='GEN-S5-'+H({'work':work,'body':deriv})[:24]
 if g.get('candidate_work_id')!=work or g.get('generation_id')!=gid:reasons.append('generation_identity')
 agg=v.agg(g)
 if agg!=packet.get('aggregate'):reasons.append('aggregate_mismatch')
 return {'ok':not reasons,'reasons':sorted(set(reasons)),'recomputed_aggregate':agg}

def mutate_digest(raw):raw['digest']='sha256:'+H(raw['record'])
def attacks(packet:dict[str,Any],v)->dict[str,bool]:
 out={}
 q=copy.deepcopy(packet);q['raw_attempts'][-1]['record']['source']['semantic_mapping'].pop('UI:SETTINGS.control-02.label',None);mutate_digest(q['raw_attempts'][-1]);out['missing_overlap_rejected']=not candidate(q,v)['ok']
 q=copy.deepcopy(packet);q['raw_attempts'][0]['record']['source']['file_checks']['checks']['a_nonoverlap_preserved']=False;q['raw_attempts'][0]['record']['source']['file_checks']['ok']=False;mutate_digest(q['raw_attempts'][0]);out['lost_nonoverlap_rejected']=not candidate(q,v)['ok']
 q=copy.deepcopy(packet);q['raw_attempts'][-1]['record']['source']['unmerged_paths']=[];mutate_digest(q['raw_attempts'][-1]);out['silent_overlap_rejected']=not candidate(q,v)['ok']
 q=copy.deepcopy(packet);q['raw_attempts'][0]['record']['source']['candidate_validation']['ok']=False;mutate_digest(q['raw_attempts'][0]);out['validation_bypass_rejected']=not candidate(q,v)['ok']
 q=copy.deepcopy(packet);keys=list(q['source_bindings']);q['source_bindings'][keys[0]]=q['source_bindings'][keys[1]];out['binding_substitution_rejected']=not candidate(q,v)['ok']
 q=copy.deepcopy(packet);q['raw_attempts'][1]['record']['reset_proof']['workspace_id']=q['raw_attempts'][0]['record']['reset_proof']['workspace_id'];mutate_digest(q['raw_attempts'][1]);out['workspace_reuse_rejected']=not candidate(q,v)['ok']
 q=copy.deepcopy(packet);q['candidate_identity']['body']['exact_toolchain_identity']['baseline']='SUBSTITUTED';out['toolchain_identity_substitution_rejected']=not candidate(q,v)['ok']
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--evidence',required=True);ap.add_argument('--validator',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
 d=json.load(open(a.evidence));v=load(pathlib.Path(a.validator).resolve(),'s5v')
 results={}; neg={}
 for name,p in d.get('results',{}).items():
  if isinstance(p,dict) and p.get('raw_attempts'):
   results[name]=candidate(p,v);neg[name]=attacks(p,v)
 provisional=d.get('provisional_candidates') or []
 all_provisional=all(results.get(n,{}).get('ok') is True and all(neg.get(n,{}).values()) for n in provisional)
 out={'schema':'W2-ENG-TECHNICAL-S5-INDEPENDENT-VERIFY-v1','evidence_run_identity':d.get('run_identity'),'candidate_verification':results,'negative_attacks':neg,'provisional_candidates':provisional,'all_provisional_verified':all_provisional}
 pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'all_provisional_verified':all_provisional,'provisional_candidates':provisional},sort_keys=True))
 return 0 if all_provisional else 3
if __name__=='__main__':raise SystemExit(main())
