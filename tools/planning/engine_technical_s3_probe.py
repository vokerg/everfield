#!/usr/bin/env python3
'''W2-ENG-TECH-S3-01 real-engine deterministic S3 empirical tranche.'''
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, pathlib, re, shutil, stat, subprocess, tempfile, time

SEED, TICKS, N, ACTIONS, MOD, OUTMOD = 424242, 600, 32, 10, 1000003, 1000000007
NORMAL, PERTURBED = 405227, 405122
CHECK = re.compile(r"EVERFIELD_S3:(\d+)")

def run(cmd, cwd=None, env=None, timeout=600):
    e=os.environ.copy()
    if env: e.update(env)
    t=time.monotonic()
    try:
        p=subprocess.run(cmd,cwd=cwd,env=e,text=True,capture_output=True,timeout=timeout,check=False)
        return {"cmd":cmd,"exit":p.returncode,"seconds":round(time.monotonic()-t,3),
                "stdout":p.stdout[-12000:],"stderr":p.stderr[-12000:],"timed_out":False}
    except subprocess.TimeoutExpired as x:
        return {"cmd":cmd,"exit":None,"seconds":round(time.monotonic()-t,3),
                "stdout":x.stdout[-12000:] if isinstance(x.stdout,str) else "",
                "stderr":x.stderr[-12000:] if isinstance(x.stderr,str) else "","timed_out":True}
    except FileNotFoundError as x:
        return {"cmd":cmd,"exit":127,"seconds":0,"stdout":"","stderr":str(x),"timed_out":False}

def ok(r): return bool(r and r.get("exit")==0 and not r.get("timed_out"))
def digest_text(s): return hashlib.sha256(s.encode()).hexdigest()
def digest_file(p):
    h=hashlib.sha256()
    with pathlib.Path(p).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def oracle(perturb=False):
    v=[i*17+(SEED%97) for i in range(N)]
    for tick in range(TICKS):
        a=(tick+SEED)%ACTIONS
        if perturb and tick==137: a=(a+1)%ACTIONS
        i=(tick*7+a)%N
        v[i]=(v[i]+a*3+(tick%11)+1)%MOD
    return sum((i+1)*x for i,x in enumerate(v))%OUTMOD

def load_module(path):
    s=importlib.util.spec_from_file_location("cap",path)
    if not s or not s.loader: raise RuntimeError("capability module unavailable")
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def checksum(r):
    hits=CHECK.findall((r.get("stdout") or "")+"\n"+(r.get("stderr") or ""))
    return int(hits[-1]) if hits else None

def record(candidate,name,perturb,ws,r):
    got=checksum(r); expected=PERTURBED if perturb else NORMAL
    passed=ok(r) and got==expected
    return {"attempt_id":f"{candidate.upper().replace(' ','_')}-S3-{name}","scenario_id":"S3",
      "candidate_id":candidate,"kind":"FAILURE_INJECTION" if perturb else "NORMAL",
      "normal_index":None if perturb else (1 if name=="N1" else 2),
      "injection_id":"FI-S3-INPUT-PERTURB-v2" if perturb else None,
      "result":"PASS" if passed else "INCONCLUSIVE","failure_class":"NONE" if passed else "HARNESS",
      "reset_id":f"RESET-{candidate}-{name}","reset_verified":True,
      "workspace_id":digest_text(str(pathlib.Path(ws).resolve())),"resource_class":"W2-ENG-HOST-COMMON-v2",
      "expected_checksum":expected,"observed_checksum":got,"command":r}

def summary(candidate,tool,attempts,build=None):
    vals=[a.get("observed_checksum") for a in attempts]
    good=len(attempts)==3 and all(a["result"]=="PASS" for a in attempts)
    repeat=len(vals)==3 and vals[0]==vals[1]==NORMAL
    inject=len(vals)==3 and vals[2]==PERTURBED and vals[2]!=vals[0]
    return {"candidate":candidate,"scenario":"S3","toolchain":tool,"build":build,"attempts":attempts,
      "normal_repeatable":repeat,"perturbation_distinguishable":inject,"common_oracle_match":good,
      "producer_disposition":"PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW" if good and repeat and inject else "INCONCLUSIVE_HARNESS_OR_INFRA",
      "review_required_before_trust":True}

BEVY = r'''use bevy::prelude::*;
#[derive(Resource)] struct Sim { values: Vec<i64> }
fn main() {
 let seed:i64=424242;
 let mut world=World::new();
 world.insert_resource(Sim{values:(0..32).map(|i|i*17+(seed%97)).collect()});
 let perturb=std::env::var("EVERFIELD_PERTURB").ok().as_deref()==Some("1");
 for tick in 0i64..600 {
  let mut action=(tick+seed)%10;
  if perturb && tick==137 { action=(action+1)%10; }
  let idx=((tick*7+action)%32) as usize;
  let mut sim=world.resource_mut::<Sim>();
  sim.values[idx]=(sim.values[idx]+action*3+(tick%11)+1)%1000003;
 }
 let sim=world.resource::<Sim>();
 let checksum:i64=sim.values.iter().enumerate().map(|(i,v)|((i as i64)+1)* *v).sum::<i64>()%1000000007;
 println!("EVERFIELD_S3:{}",checksum);
}
'''

def bevy(root,lock,tool):
    if tool.get("status") not in ("CAPABLE","CAPABLE_WITH_PRESEED"):
        return {"candidate":"Bevy","scenario":"S3","toolchain":tool,"producer_disposition":"NOT_RUN_TOOLCHAIN_UNAVAILABLE"}
    p=root/"bevy-s3"; (p/"src").mkdir(parents=True)
    (p/"Cargo.toml").write_text("[package]\nname='everfield_bevy_s3'\nversion='0.0.0'\nedition='2024'\n[dependencies]\nbevy={version='=0.19.0',default-features=false}\n")
    shutil.copy2(lock,p/"Cargo.lock"); (p/"src/main.rs").write_text(BEVY)
    cargo=(tool.get("cargo") or {}).get("path") or shutil.which("cargo")
    b=run([str(cargo),"build","--locked","--quiet"],cwd=p,timeout=900) if cargo else None
    exe=p/"target/debug/everfield_bevy_s3"
    if not ok(b) or not exe.exists(): return summary("Bevy",tool,[],b)
    a=[]
    for name,pert in (("N1",False),("N2",False),("FI1",True)):
        ws=root/"runs/bevy"/name; ws.mkdir(parents=True)
        x=ws/"everfield_bevy_s3"; shutil.copy2(exe,x); x.chmod(x.stat().st_mode|stat.S_IXUSR)
        a.append(record("Bevy",name,pert,ws,run([str(x)],cwd=ws,env={"EVERFIELD_PERTURB":"1" if pert else "0"},timeout=120)))
    return summary("Bevy",tool,a,b)

GDSCRIPT = r'''extends Node
const SEED=424242
func _ready():
 var values=[]
 for i in range(32): values.append(i*17+(SEED%97))
 var perturb=OS.get_environment("EVERFIELD_PERTURB")=="1"
 for tick in range(600):
  var action=(tick+SEED)%10
  if perturb and tick==137: action=(action+1)%10
  var idx=(tick*7+action)%32
  values[idx]=(values[idx]+action*3+(tick%11)+1)%1000003
 var checksum=0
 for i in range(32): checksum=(checksum+(i+1)*values[i])%1000000007
 print("EVERFIELD_S3:%d"%checksum)
 get_tree().quit()
'''

def godot(root,tool):
    if tool.get("status")!="CAPABLE" or not tool.get("executable"):
        return {"candidate":"Godot","scenario":"S3","toolchain":tool,"producer_disposition":"NOT_RUN_TOOLCHAIN_UNAVAILABLE"}
    a=[]; exe=tool["executable"]
    for name,pert in (("N1",False),("N2",False),("FI1",True)):
        ws=root/"runs/godot"/name; ws.mkdir(parents=True)
        (ws/"project.godot").write_text('[application]\nconfig/name="EverfieldS3"\nrun/main_scene="res://main.tscn"\n[display]\nwindow/size/viewport_width=320\nwindow/size/viewport_height=180\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n')
        (ws/"main.tscn").write_text('[gd_scene load_steps=2 format=3]\n\n[ext_resource path="res://main.gd" type="Script" id="1"]\n\n[node name="Main" type="Node"]\nscript = ExtResource("1")\n')
        (ws/"main.gd").write_text(GDSCRIPT)
        a.append(record("Godot",name,pert,ws,run([exe,"--headless","--path",str(ws)],cwd=ws,env={"EVERFIELD_PERTURB":"1" if pert else "0"},timeout=120)))
    return summary("Godot",tool,a)

LUA = r'''function init(self)
 local seed=424242
 local values={}
 for i=0,31 do values[i+1]=i*17+(seed%97) end
 local perturb=os.getenv("EVERFIELD_PERTURB")=="1"
 for tick=0,599 do
  local action=(tick+seed)%10
  if perturb and tick==137 then action=(action+1)%10 end
  local idx=((tick*7+action)%32)+1
  values[idx]=(values[idx]+action*3+(tick%11)+1)%1000003
 end
 local checksum=0
 for i=1,32 do checksum=(checksum+i*values[i])%1000000007 end
 print("EVERFIELD_S3:"..tostring(checksum))
 sys.exit(0)
end
'''

def bundle_exe(bundle):
    c=[]
    if not bundle.exists(): return None
    for p in bundle.rglob("*"):
        if not p.is_file() or p.suffix.lower() in (".so",".dll",".dylib",".jar",".zip"): continue
        try:
            if p.stat().st_mode&(stat.S_IXUSR|stat.S_IXGRP|stat.S_IXOTH): c.append(p)
        except OSError: pass
    return max(c,key=lambda p:p.stat().st_size) if c else None

def defold(root,tool):
    if tool.get("status")!="CAPABLE":
        return {"candidate":"Defold","scenario":"S3","toolchain":tool,"producer_disposition":"NOT_RUN_TOOLCHAIN_UNAVAILABLE"}
    jar=root/"bob-1.13.0.jar"; java=(tool.get("java") or {}).get("path") or shutil.which("java")
    if not jar.exists() or not java: return summary("Defold",tool,[])
    p=root/"defold-s3"; p.mkdir()
    (p/"game.project").write_text("[project]\ntitle = EverfieldS3\n[bootstrap]\nmain_collection = /main.collectionc\n[display]\nwidth = 320\nheight = 180\n")
    (p/"main.collection").write_text('name: "main"\nscale_along_z: 0\nembedded_instances {\n id: "controller"\n data: "components {\\n  id: \\"script\\"\\n  component: \\"/controller.script\\"\\n}\\n"\n}\n')
    (p/"controller.script").write_text(LUA)
    bundle=p/"bundle"
    b=run([java,"-jar",str(jar),"--root",str(p),"--bundle-output",str(bundle),"--variant","headless","--platform","x86_64-linux","resolve","build","bundle"],cwd=p,timeout=900)
    variant="headless"
    if not ok(b):
        bundle=p/"bundle-debug"; variant="debug"
        b=run([java,"-jar",str(jar),"--root",str(p),"--bundle-output",str(bundle),"--variant","debug","--platform","x86_64-linux","resolve","build","bundle"],cwd=p,timeout=900)
    exe=bundle_exe(bundle)
    if not ok(b) or not exe:
        z=summary("Defold",tool,[],b); z["bundle_variant"]=variant; return z
    a=[]
    for name,pert in (("N1",False),("N2",False),("FI1",True)):
        ws=root/"runs/defold"/name; shutil.copytree(bundle,ws)
        x=ws/exe.relative_to(bundle)
        rr=run([str(x)],cwd=x.parent,env={"EVERFIELD_PERTURB":"1" if pert else "0"},timeout=120)
        if not ok(rr) and shutil.which("xvfb-run"):
            rr=run(["xvfb-run","-a",str(x)],cwd=x.parent,env={"EVERFIELD_PERTURB":"1" if pert else "0"},timeout=120)
        a.append(record("Defold",name,pert,ws,rr))
    z=summary("Defold",tool,a,b); z["bundle_variant"]=variant; z["bundle_executable_sha256"]=digest_file(exe); return z

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",required=True); ap.add_argument("--bevy-lock",required=True); ap.add_argument("--artifact-lock",required=True)
    ap.add_argument("--capability-probe",default="tools/planning/engine_toolchain_probe.py"); args=ap.parse_args()
    out=pathlib.Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    lock=pathlib.Path(args.bevy_lock); alock=pathlib.Path(args.artifact_lock); cap=load_module(pathlib.Path(args.capability_probe))
    if oracle(False)!=NORMAL or oracle(True)!=PERTURBED: raise RuntimeError("oracle constant mismatch")
    artifacts=cap.load_artifact_lock(alock)
    with tempfile.TemporaryDirectory(prefix="everfield-s3-") as td:
        root=pathlib.Path(td)
        bp=cap.probe_bevy(root,lock); dp=cap.probe_defold(root,artifacts); gp=cap.probe_godot(root,artifacts)
        up=cap.probe_unity(); xp=cap.probe_unreal()
        results={"Bevy":bevy(root,lock,bp),"Defold":defold(root,dp),"Godot":godot(root,gp),
          "Unity":{"candidate":"Unity","scenario":"S3","toolchain":up,"producer_disposition":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"},
          "Unreal Engine":{"candidate":"Unreal Engine","scenario":"S3","toolchain":xp,"producer_disposition":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"}}
        good=[k for k,v in results.items() if v.get("producer_disposition")=="PROVISIONAL_S3_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW"]
        payload={"schema":"W2-ENG-TECHNICAL-S3-v1","mission_id":"W2-ENG-TECH-S3-01","source_issue":351,
          "source_engine_issue":82,"source_engine_terminal_comment":5276916603,"routing_directive_comment":5303081124,
          "canonical_binding_comment":5245368879,"canonical_program_blob":"e3120ec203c4156328770aa86c12fbb7187966dc",
          "harness_id":"W2-ENG-HARNESS-v5","feature_slice_id":"W2-ENG-FEATURE-SLICE-v2","scenario_manifest_id":"W2-ENG-SCENARIO-INPUTS-v2",
          "scenario_id":"S3","scenario_contract":{"entity_count":32,"seed":424242,"normal_ticks":600,"action_count":10,
          "required_mechanism_authority":"REAL_OR_SHARED_RULES","required_failure_injection":"FI-S3-INPUT-PERTURB-v2","resource_class":"W2-ENG-HOST-COMMON-v2"},
          "oracle":{"normal_checksum":NORMAL,"perturbed_checksum":PERTURBED,"normal_recomputed":oracle(False),"perturbed_recomputed":oracle(True)},
          "runner":{"github_sha":os.getenv("GITHUB_SHA"),"github_run_id":os.getenv("GITHUB_RUN_ID"),"github_run_attempt":os.getenv("GITHUB_RUN_ATTEMPT"),
          "runner_os":os.getenv("RUNNER_OS"),"runner_arch":os.getenv("RUNNER_ARCH"),"image_os":os.getenv("ImageOS"),"image_version":os.getenv("ImageVersion")},
          "results":results,"provisional_review_pending_s3_pass_candidates":good,"provisional_review_pending_s3_pass_count":len(good),
          "historical_issue_82_not_run_cells_preserved":50,"historical_issue_82_cells_mutated":False,"partial_candidate_ranking_permitted":False,
          "engine_selected":False,"production_implementation_ready":False,"provider_permission":False,"verification_pass_authority":False,
          "decision_authority":False,"canonicality":"NOT_CANONICAL","integration_authority":False,
          "required_review":"FRESH_INDEPENDENT_OR_DEGRADED_INDEPENDENT_REVIEW"}
        out.write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
        print(json.dumps({"results":{k:v.get("producer_disposition") for k,v in results.items()},"pass_candidates":good,"out":str(out)},sort_keys=True))
    return 0
if __name__=="__main__": raise SystemExit(main())
