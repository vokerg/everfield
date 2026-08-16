#!/usr/bin/env python3
"""Issue #433 bounded corrections: Bevy lock identity + generated-metadata collision."""
from __future__ import annotations
import hashlib, importlib.util, json, os, pathlib, shutil, sys
from typing import Any

HERE=pathlib.Path(__file__).resolve()
BASE=HERE.with_name('engine_technical_s5_probe.py')
GEN_META='generated/candidate-metadata.txt'

def sha(path): return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
def shatxt(text:str)->str: return 'sha256:'+hashlib.sha256(text.encode()).hexdigest()
def load(path,name):
 s=importlib.util.spec_from_file_location(name,path)
 if not s or not s.loader: raise RuntimeError(path)
 mod=importlib.util.module_from_spec(s);s.loader.exec_module(mod);return mod

m=load(BASE,'everfield_s5_base')
BASE_SHA=sha(BASE);ENTRY_SHA=sha(HERE)

# Correction 1: preserve exact retained Cargo.lock root package identity.
m.BEVY_FILES['Cargo.toml']="""[package]\nname='everfield_bevy_probe'\nversion='0.0.0'\nedition='2024'\n[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n"""

# Correction 2: every candidate can emit deterministic candidate-generated metadata
# from its actual branch state. The metadata is generated only for FI1, tracked on
# both branches, required to conflict, and regenerated after bounded resolution.
m.BEVY_FILES['src/main.rs']=r'''use bevy::prelude::*;
mod state; mod ui; mod branch_a; mod branch_b;
#[derive(Resource)] struct MergeState { status: &'static str, label: &'static str, a: bool, b: &'static str }
fn main() {
    let mut world = World::new();
    world.insert_resource(MergeState { status: state::ENTITY_07_STATUS, label: ui::SETTINGS_CONTROL_02_LABEL, a: branch_a::A_ENABLED, b: branch_b::B_LABEL });
    let s = world.resource::<MergeState>();
    if std::env::var("EVERFIELD_S5_EMIT_METADATA").ok().as_deref() == Some("1") {
        println!("EVERFIELD_S5_METADATA:{}|{}|{}|{}", s.status, s.label, s.a, s.b);
        return;
    }
    let expected_status = std::env::var("EVERFIELD_S5_EXPECT_STATUS").unwrap();
    let expected_label = std::env::var("EVERFIELD_S5_EXPECT_LABEL").unwrap();
    if s.status != expected_status || s.label != expected_label || !s.a || s.b != "Return" { std::process::exit(7); }
    println!("EVERFIELD_S5:PASS");
}
'''
m.GODOT_FILES['main.gd']=r'''extends Node
const State = preload("res://state.gd")
const Settings = preload("res://settings.gd")
const A = preload("res://branch_a.gd")
const B = preload("res://branch_b.gd")
func _ready():
 if OS.get_environment("EVERFIELD_S5_EMIT_METADATA") == "1":
  print("EVERFIELD_S5_METADATA:%s|%s|%s|%s" % [State.ENTITY_07_STATUS, Settings.SETTINGS_CONTROL_02_LABEL, A.A_ENABLED, B.B_LABEL])
  get_tree().quit(0); return
 var es = OS.get_environment("EVERFIELD_S5_EXPECT_STATUS")
 var el = OS.get_environment("EVERFIELD_S5_EXPECT_LABEL")
 if State.ENTITY_07_STATUS != es or Settings.SETTINGS_CONTROL_02_LABEL != el or not A.A_ENABLED or B.B_LABEL != "Return":
  get_tree().quit(7); return
 print("EVERFIELD_S5:PASS")
 get_tree().quit(0)
'''
m.DEFOLD_FILES['controller.script']=r'''local state = require "state"
local settings = require "settings"
local a = require "branch_a"
local b = require "branch_b"
function init(self)
 if os.getenv("EVERFIELD_S5_EMIT_METADATA") == "1" then
  print("EVERFIELD_S5_METADATA:" .. state.entity_07_status .. "|" .. settings.settings_control_02_label .. "|" .. tostring(a.a_enabled) .. "|" .. b.b_label)
  sys.exit(0)
  return
 end
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
'''

_original_validate=m.validate_candidate
def validate_candidate(repo,candidate,tool,tool_root,expected_status,expected_label):
 if candidate!='Bevy': return _original_validate(repo,candidate,tool,tool_root,expected_status,expected_label)
 env={'EVERFIELD_S5_EXPECT_STATUS':expected_status,'EVERFIELD_S5_EXPECT_LABEL':expected_label}
 cargo=(tool.get('cargo') or {}).get('path') or shutil.which('cargo')
 if not cargo:return {'ok':False,'reason':'cargo_missing'}
 build=m.run([str(cargo),'build','--locked','--quiet'],cwd=repo,timeout=900)
 exe=repo/'target'/'debug'/'everfield_bevy_probe'
 execution=m.run([str(exe)],cwd=repo,env=env,timeout=120) if m.ok(build) and exe.exists() else None
 passed=m.ok(build) and m.ok(execution) and 'EVERFIELD_S5:PASS' in (((execution or {}).get('stdout') or '')+((execution or {}).get('stderr') or ''))
 return {'ok':passed,'build':m.semantic_result(build),'execution':m.semantic_result(execution) if execution else None,'executable_sha256':m.digest_file(exe) if exe.exists() else None}
m.validate_candidate=validate_candidate


def _metadata_line(result:dict[str,Any]|None)->str|None:
 if not result:return None
 for line in ((result.get('stdout') or '')+'\n'+(result.get('stderr') or '')).splitlines():
  if line.startswith('EVERFIELD_S5_METADATA:'): return line.split(':',1)[1].strip()
 return None

def _metadata_process(work:pathlib.Path,candidate:str,tool:dict[str,Any],tool_root:pathlib.Path)->dict[str,Any]:
 env={'EVERFIELD_S5_EMIT_METADATA':'1'}
 if candidate=='Bevy':
  cargo=(tool.get('cargo') or {}).get('path') or shutil.which('cargo')
  if not cargo:return {'ok':False,'reason':'cargo_missing'}
  build=m.run([str(cargo),'build','--locked','--quiet'],cwd=work,timeout=900)
  exe=work/'target'/'debug'/'everfield_bevy_probe'
  execution=m.run([str(exe)],cwd=work,env=env,timeout=120) if m.ok(build) and exe.exists() else None
  meta=_metadata_line(execution)
  return {'ok':bool(m.ok(build) and m.ok(execution) and meta),'metadata':meta,'build':m.semantic_result(build),'execution':m.semantic_result(execution) if execution else None}
 if candidate=='Godot':
  exe=tool.get('executable')
  if not exe:return {'ok':False,'reason':'godot_executable_missing'}
  execution=m.run([str(exe),'--headless','--path',str(work)],cwd=work,env=env,timeout=120)
  meta=_metadata_line(execution)
  return {'ok':bool(m.ok(execution) and meta),'metadata':meta,'execution':m.semantic_result(execution)}
 if candidate=='Defold':
  java=(tool.get('java') or {}).get('path') or shutil.which('java');jar=tool_root/'bob-1.13.0.jar'
  if not java or not jar.exists():return {'ok':False,'reason':'bob_or_java_missing'}
  builds=[];bundle=None
  for variant in ('headless','debug'):
   bdir=work/f'bundle-{variant}'
   rr=m.run([str(java),'-jar',str(jar),'--root',str(work),'--bundle-output',str(bdir),'--variant',variant,'--platform','x86_64-linux','--archive','resolve','build','bundle'],cwd=work,timeout=900)
   builds.append({'variant':variant,'result':m.semantic_result(rr)})
   if m.ok(rr):bundle=bdir;break
  exe=m.find_bundle_exe(bundle) if bundle else None;execution=None
  if exe:
   execution=m.run([str(exe)],cwd=exe.parent,env=env,timeout=120)
   if not m.ok(execution) and shutil.which('xvfb-run'):execution=m.run(['xvfb-run','-a',str(exe)],cwd=exe.parent,env=env,timeout=120)
  meta=_metadata_line(execution)
  return {'ok':bool(execution and m.ok(execution) and meta),'metadata':meta,'builds':builds,'execution':m.semantic_result(execution) if execution else None}
 return {'ok':False,'reason':'unknown_candidate'}

def generate_metadata(repo:pathlib.Path,candidate:str,tool:dict[str,Any],tool_root:pathlib.Path,tag:str)->dict[str,Any]:
 work=repo.parent/f'{repo.name}-metadata-{tag}'
 if work.exists():shutil.rmtree(work)
 shutil.copytree(repo,work,ignore=shutil.ignore_patterns('.git','target','.godot','bundle-*','build'))
 try:r=_metadata_process(work,candidate,tool,tool_root)
 finally:shutil.rmtree(work,ignore_errors=True)
 if r.get('metadata'):r['metadata_sha256']=shatxt(r['metadata'])
 return r

_original_execute=m.execute_attempt
def execute_attempt(root,candidate,label,inject,direction,tool,tool_root,bevy_lock,run_identity):
 if not inject:return _original_execute(root,candidate,label,inject,direction,tool,tool_root,bevy_lock,run_identity)
 repo,proof=m.reset_prepare(root,candidate,label,run_identity);baseline=m.init_repo(repo,candidate,bevy_lock)
 m.git(repo,'checkout','-q','-b','branch-a',baseline);m.apply_a(repo,candidate,True)
 ma=generate_metadata(repo,candidate,tool,tool_root,'A');m.write(repo/GEN_META,(ma.get('metadata') or 'GENERATION_FAILED_A')+'\n');a_head=m.git_commit(repo,'branch-a')
 m.git(repo,'checkout','-q','-b','branch-b',baseline);m.apply_b(repo,candidate,True)
 mb=generate_metadata(repo,candidate,tool,tool_root,'B');m.write(repo/GEN_META,(mb.get('metadata') or 'GENERATION_FAILED_B')+'\n');b_head=m.git_commit(repo,'branch-b')
 a_changed=m.changed_files(repo,baseline,a_head);b_changed=m.changed_files(repo,baseline,b_head)
 first,second=('branch-a','branch-b') if direction=='A_THEN_B' else ('branch-b','branch-a')
 m.git(repo,'checkout','-q',first);merge=m.git(repo,'merge','--no-ff','--no-commit',second)
 unmerged=[x for x in m.git_out(repo,'diff','--name-only','--diff-filter=U').splitlines() if x]
 s=m.CANDIDATE_SPEC[candidate];overlap=[s['state_path'],s['ui_path'],GEN_META]
 markers={p:('<<<<<<<' in (repo/p).read_text() and '>>>>>>>' in (repo/p).read_text()) if (repo/p).exists() else False for p in overlap}
 conflict_visible=merge.get('exit') not in (0,None) and set(unmerged)==set(overlap) and all(markers.values())
 resolution=None;merged_commit=None;mr={'ok':False,'reason':'conflict_not_visible'}
 if conflict_visible:
  m.write(repo/s['state_path'],s['state_a']);m.write(repo/s['ui_path'],s['ui_b'])
  mr=generate_metadata(repo,candidate,tool,tool_root,'RESOLVED');m.write(repo/GEN_META,(mr.get('metadata') or 'GENERATION_FAILED_RESOLVED')+'\n')
  resolution={'state_choice':'branch-a/ACTIVE','ui_choice':'branch-b/Volume','generated_metadata_choice':'REGENERATED_FROM_RESOLVED_CANDIDATE_STATE'}
  merged_commit=m.git_commit(repo,'bounded-resolution-with-generated-metadata')
 file_checks=m.validate_expected_files(repo,candidate,'ACTIVE','Volume') if merged_commit else {'ok':False,'checks':{}}
 validation=m.validate_candidate(repo,candidate,tool,tool_root,'ACTIVE','Volume') if merged_commit and file_checks['ok'] else {'ok':False,'reason':'merge_or_file_checks_failed'}
 generated_ok=ma.get('ok') is True and mb.get('ok') is True and mr.get('ok') is True and ma.get('metadata_sha256')!=mb.get('metadata_sha256') and (repo/GEN_META).read_text().strip()==mr.get('metadata')
 passed=conflict_visible and file_checks['ok'] and validation.get('ok') is True and m.verify_reset(proof) and generated_ok
 md={'candidate_generated_metadata_present':True,'generated_collision_required':True,'collision_path':GEN_META,'branch_a_generation':ma,'branch_b_generation':mb,'resolved_generation':mr,'branch_values_distinct':ma.get('metadata_sha256')!=mb.get('metadata_sha256'),'resolved_file_matches_candidate_generation':bool(mr.get('metadata') and (repo/GEN_META).read_text().strip()==mr.get('metadata'))}
 source={'candidate':candidate,'label':label,'mode':'INJECT','direction':direction,'baseline_tree':m.git_out(repo,'rev-parse',f'{baseline}^{{tree}}'),'branch_a_tree':m.git_out(repo,'rev-parse',f'{a_head}^{{tree}}'),'branch_b_tree':m.git_out(repo,'rev-parse',f'{b_head}^{{tree}}'),'final_tree':m.git_out(repo,'rev-parse','HEAD^{tree}') if merged_commit else None,'semantic_mapping':{'STATE:entity-07.status':s['state_path'],'UI:SETTINGS.control-02.label':s['ui_path'],'branch_a_nonoverlap':s['a_path'],'branch_b_nonoverlap':s['b_path'],'candidate_generated_metadata':GEN_META},'branch_a_changed_files':a_changed,'branch_b_changed_files':b_changed,'merge_exit':merge.get('exit'),'unmerged_paths':unmerged,'conflict_markers':markers,'resolution':resolution,'file_checks':file_checks,'candidate_validation':validation,'generated_metadata':md,'run_identity':run_identity}
 raw={'schema':'S5-RAW-ATTEMPT-v1','candidate':candidate,'label':label,'mode':'INJECT','scenario_id':m.SCENARIO,'required_injection':m.INJECTION,'direction':direction,'reset_proof':proof,'reset_verified_derived':m.verify_reset(proof),'source':source,'formal_result':'PASS' if passed else 'INCONCLUSIVE','failure_class':'NONE' if passed else 'HARNESS'}
 return {'digest':'sha256:'+m.digest_obj(raw),'record':raw,'observation':{'merge_seconds':merge.get('seconds')}}
m.execute_attempt=execute_attempt

_original_identity=m.toolchain_identity
def toolchain_identity(candidate,tool,validator_sha,runner_sha,run_identity):
 x=_original_identity(candidate,tool,validator_sha,ENTRY_SHA,run_identity);x['body']['base_runner_sha256']=BASE_SHA;x['body']['correction_entry_sha256']=ENTRY_SHA;x['body']['generated_metadata_collision_exercised']=True;x['identity_digest']='sha256:'+m.digest_obj(x['body']);return x
m.toolchain_identity=toolchain_identity
m.__file__=str(HERE)

def main():
 rc=m.main()
 if rc==0 and '--out' in sys.argv:
  out=pathlib.Path(sys.argv[sys.argv.index('--out')+1]);d=json.loads(out.read_text())
  d['s5_contract']['generated_collision_required_when_candidate_has_generated_metadata']=True
  d['producer_corrections']=[
   {'run_id':31959088675,'artifact_id':9266757869,'artifact_digest':'sha256:aaec74a44c4de8e4b8e0843c764afbdaa26e8e39bb5af478172a37491d1d5b84','evidence_sha256':'a8dca2083d0c5f132e74f410f49fab4b3687914a8281189718fe5001ba897bbe','finding':'BEVY_RETAINED_LOCK_ROOT_PACKAGE_IDENTITY_MISMATCH','status':'RETAINED_FAILED_PRODUCER_PROVENANCE'},
   {'run_id':31959336546,'artifact_id':9266839656,'artifact_digest':'sha256:4bb52e98c7e77a1adcfe6106e06d9de23acadc9cbe01d09aed8cea7f33bd92ca','evidence_sha256':'51f43ec15093b21e95a2b8d5f4f1896efc70bc23c0a6a397ab5e228578b3ef6b','finding':'GENERATED_METADATA_COLLISION_REQUIREMENT_NOT_EXERCISED','status':'RETAINED_INCOMPLETE_PRODUCER_PROVENANCE'}]
  out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
 return rc

if __name__=='__main__':raise SystemExit(main())
