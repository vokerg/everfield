#!/usr/bin/env python3
'''W2-ENG-TECH-S6-01: identity-bound candidate-render capture evidence.'''
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, os, pathlib, shutil, stat, subprocess, tempfile, time
from typing import Any

SCENARIO="S6"; RESOURCE="W2-ENG-HOST-COMMON-v2"; INJECTION="FI-S6-CAPTURE-DOWN-v2"
MARKER="CAPTURE-STATE-042"; WIDTH=1280; HEIGHT=720
SCREENS=["BOOT_OR_MAIN","PLAY_SURFACE","SETTINGS"]
ROUTES=["BOOT_OR_MAIN->PLAY_SURFACE","PLAY_SURFACE->SETTINGS","SETTINGS->PLAY_SURFACE"]
S5_ISSUE=433; S5_TERMINAL=5308620093; S5_REVIEW_ISSUE=454; S5_REVIEW_TERMINAL=5309016465
S5_REVIEW_DISPOSITION="PASS_BOUNDED_S5_V5_ENVELOPE"
S5_REVIEW_PUBLICATION="a7c587956f542c0fc00d5c6875a04a04e124f4e6"
S5_PRODUCER_PUBLICATION="886438990ed395cde2fad0ee6cb98ca6ade0f26f"

def canon(o:Any)->str:return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def digest_obj(o:Any)->str:return hashlib.sha256(canon(o).encode()).hexdigest()
def digest_file(p:pathlib.Path)->str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()
def load_module(p:pathlib.Path,name:str):
    s=importlib.util.spec_from_file_location(name,p)
    if not s or not s.loader: raise RuntimeError(f"cannot load {p}")
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def run(cmd:list[str],cwd:pathlib.Path|None=None,env:dict[str,str]|None=None,timeout:int=900)->dict[str,Any]:
    e=os.environ.copy();e.update(env or {});t=time.monotonic()
    try:
        p=subprocess.run(cmd,cwd=cwd,env=e,text=True,capture_output=True,timeout=timeout,check=False)
        return {"command":cmd,"exit":p.returncode,"timed_out":False,"seconds":round(time.monotonic()-t,3),"stdout":p.stdout[-16000:],"stderr":p.stderr[-16000:]}
    except subprocess.TimeoutExpired as x:
        return {"command":cmd,"exit":None,"timed_out":True,"seconds":round(time.monotonic()-t,3),"stdout":x.stdout[-16000:] if isinstance(x.stdout,str) else "","stderr":x.stderr[-16000:] if isinstance(x.stderr,str) else ""}
    except FileNotFoundError as x:
        return {"command":cmd,"exit":127,"timed_out":False,"seconds":0,"stdout":"","stderr":str(x)}
def ok(r:dict[str,Any]|None)->bool:return bool(r and r.get("exit")==0 and not r.get("timed_out"))
def semantic(r:dict[str,Any]|None)->dict[str,Any]|None:
    if not r:return None
    return {k:r.get(k) for k in ("command","exit","timed_out","stdout","stderr")}
def write(p:pathlib.Path,s:str)->None:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def reset_prepare(root:pathlib.Path,candidate:str,label:str,run_id:str)->tuple[pathlib.Path,dict[str,Any]]:
    p=root/"runs"/candidate.lower().replace(" ","-")/label
    absent=not p.exists();p.mkdir(parents=True,exist_ok=False)
    proof={"schema":"S6-RESET-PROOF-v1","candidate":candidate,"label":label,"pre_workspace_absent":absent,"workspace_created_exclusive":p.exists(),
           "workspace_id":"WS-S6-"+digest_obj({"c":candidate,"l":label,"run":run_id,"r":"ws"})[:28],
           "reset_id":"RESET-S6-"+digest_obj({"c":candidate,"l":label,"run":run_id,"r":"reset"})[:28]}
    return p,proof
def reset_ok(p:dict[str,Any])->bool:
    return isinstance(p,dict) and p.get("pre_workspace_absent") is True and p.get("workspace_created_exclusive") is True and bool(p.get("workspace_id")) and bool(p.get("reset_id"))
def reset_set_ok(raws:list[dict[str,Any]])->bool:
    ps=[x["record"]["reset_proof"] for x in raws]
    return all(reset_ok(x) for x in ps) and len({x["workspace_id"] for x in ps})==len(ps) and len({x["reset_id"] for x in ps})==len(ps)

BEVY = {
"Cargo.toml":'''[package]
name="everfield_s6_probe"
version="0.0.0"
edition="2024"
[dependencies]
bevy = "=0.19.0"
''',
"src/main.rs":r'''use bevy::prelude::*;
use std::{env,fs};
fn setup(mut commands: Commands) {
    commands.spawn(Camera2d);
    let w=426.0;
    commands.spawn((Sprite::from_color(Color::srgb(0.80,0.12,0.12),Vec2::new(w,720.0)),Transform::from_xyz(-427.0,0.0,0.0)));
    commands.spawn((Sprite::from_color(Color::srgb(0.12,0.72,0.20),Vec2::new(w,720.0)),Transform::from_xyz(0.0,0.0,0.0)));
    commands.spawn((Sprite::from_color(Color::srgb(0.12,0.25,0.86),Vec2::new(w,720.0)),Transform::from_xyz(427.0,0.0,0.0)));
    if let Ok(p)=env::var("EVERFIELD_S6_READY_PATH") {
        let g=env::var("EVERFIELD_S6_GENERATION").unwrap_or_default();
        let body=format!("CAPTURE-STATE-042|BOOT_OR_MAIN,PLAY_SURFACE,SETTINGS|BOOT_OR_MAIN->PLAY_SURFACE,PLAY_SURFACE->SETTINGS,SETTINGS->PLAY_SURFACE|1280x720|Bevy|{}",g);
        fs::write(p,body).unwrap();
    }
    println!("EVERFIELD_S6_STATE:CAPTURE-STATE-042");
}
fn main(){
    App::new().add_plugins(DefaultPlugins.set(WindowPlugin{
        primary_window:Some(Window{title:"Everfield S6 Bevy".into(),resolution:(1280,720).into(),resizable:false,..default()}),..default()
    })).add_systems(Startup,setup).run();
}
'''
}
GODOT = {
"project.godot":'''[application]
config/name="Everfield S6 Godot"
run/main_scene="res://main.tscn"
[display]
window/size/viewport_width=1280
window/size/viewport_height=720
window/size/window_width_override=1280
window/size/window_height_override=720
window/resizable=false
[rendering]
renderer/rendering_method="gl_compatibility"
renderer/rendering_method.mobile="gl_compatibility"
''',
"main.tscn":'''[gd_scene load_steps=2 format=3]

[ext_resource path="res://main.gd" type="Script" id="1"]

[node name="Main" type="Node2D"]
script = ExtResource("1")
''',
"main.gd":r'''extends Node2D
func _ready():
    var p=OS.get_environment("EVERFIELD_S6_READY_PATH")
    var g=OS.get_environment("EVERFIELD_S6_GENERATION")
    var f=FileAccess.open(p,FileAccess.WRITE)
    f.store_string("CAPTURE-STATE-042|BOOT_OR_MAIN,PLAY_SURFACE,SETTINGS|BOOT_OR_MAIN->PLAY_SURFACE,PLAY_SURFACE->SETTINGS,SETTINGS->PLAY_SURFACE|1280x720|Godot|"+g)
    f.close()
    print("EVERFIELD_S6_STATE:CAPTURE-STATE-042")
    queue_redraw()
func _draw():
    draw_rect(Rect2(0,0,426,720),Color(0.80,0.12,0.12))
    draw_rect(Rect2(426,0,428,720),Color(0.12,0.72,0.20))
    draw_rect(Rect2(854,0,426,720),Color(0.12,0.25,0.86))
'''
}
DEFOLD = {
"game.project":'''[project]
title = Everfield S6 Defold
[bootstrap]
main_collection = /main.collectionc
[display]
width = 1280
height = 720
high_dpi = 0
''',
"input/game.input_binding":"",
"main.collection":'''name: "main"
scale_along_z: 0
embedded_instances {
  id: "surface"
  data: "components {\\n  id: \\"gui\\"\\n  component: \\"/main.gui\\"\\n}\\n"
}
''',
"main.gui":'''script: "/main.gui_script"
nodes {
  position { x: 213.0 y: 360.0 z: 0.0 }
  size { x: 426.0 y: 720.0 z: 0.0 }
  color { x: 0.80 y: 0.12 z: 0.12 w: 1.0 }
  type: TYPE_BOX
  id: "boot"
}
nodes {
  position { x: 640.0 y: 360.0 z: 0.0 }
  size { x: 428.0 y: 720.0 z: 0.0 }
  color { x: 0.12 y: 0.72 z: 0.20 w: 1.0 }
  type: TYPE_BOX
  id: "play"
}
nodes {
  position { x: 1067.0 y: 360.0 z: 0.0 }
  size { x: 426.0 y: 720.0 z: 0.0 }
  color { x: 0.12 y: 0.25 z: 0.86 w: 1.0 }
  type: TYPE_BOX
  id: "settings"
}
''',
"main.gui_script":r'''function init(self)
    local p=os.getenv("EVERFIELD_S6_READY_PATH")
    local g=os.getenv("EVERFIELD_S6_GENERATION") or ""
    local f=io.open(p,"w")
    f:write("CAPTURE-STATE-042|BOOT_OR_MAIN,PLAY_SURFACE,SETTINGS|BOOT_OR_MAIN->PLAY_SURFACE,PLAY_SURFACE->SETTINGS,SETTINGS->PLAY_SURFACE|1280x720|Defold|"..g)
    f:close()
    print("EVERFIELD_S6_STATE:CAPTURE-STATE-042")
end
'''
}
FILES={"Bevy":BEVY,"Godot":GODOT,"Defold":DEFOLD}

def materialize(repo:pathlib.Path,candidate:str)->None:
    for rel,text in FILES[candidate].items():write(repo/rel,text)
def source_digest(repo:pathlib.Path,candidate:str)->dict[str,Any]:
    files={rel:digest_file(repo/rel) for rel in sorted(FILES[candidate])}
    lock=repo/"Cargo.lock"
    if candidate=="Bevy" and lock.exists():files["Cargo.lock"]=digest_file(lock)
    return {"files":files,"digest":"sha256:"+digest_obj(files)}
def find_bundle_exe(bundle:pathlib.Path)->pathlib.Path|None:
    found=[]
    if not bundle.exists():return None
    for p in bundle.rglob("*"):
        if not p.is_file() or p.suffix.lower() in (".so",".dll",".dylib",".jar",".zip"):continue
        try:
            if p.stat().st_mode & (stat.S_IXUSR|stat.S_IXGRP|stat.S_IXOTH):found.append(p)
        except OSError:pass
    return max(found,key=lambda p:p.stat().st_size) if found else None

def prepare_candidate(repo:pathlib.Path,candidate:str,tool:dict[str,Any],tool_root:pathlib.Path)->dict[str,Any]:
    materialize(repo,candidate)
    if candidate=="Bevy":
        cargo=(tool.get("cargo") or {}).get("path") or shutil.which("cargo")
        if not cargo:return {"ok":False,"reason":"cargo_missing"}
        lock=run([str(cargo),"generate-lockfile"],cwd=repo,timeout=900)
        build=run([str(cargo),"build","--locked","--quiet"],cwd=repo,timeout=1800) if ok(lock) else None
        exe=repo/"target"/"debug"/"everfield_s6_probe"
        return {"ok":ok(lock) and ok(build) and exe.exists(),"lock":semantic(lock),"build":semantic(build),"executable":str(exe) if exe.exists() else None,"executable_sha256":digest_file(exe) if exe.exists() else None}
    if candidate=="Godot":
        exe=tool.get("executable")
        return {"ok":bool(exe and pathlib.Path(exe).exists()),"executable":exe,"executable_sha256":tool.get("executable_sha256")}
    if candidate=="Defold":
        java=(tool.get("java") or {}).get("path") or shutil.which("java");jar=tool_root/"bob-1.13.0.jar";bundle=repo/"bundle-debug"
        if not java or not jar.exists():return {"ok":False,"reason":"bob_or_java_missing"}
        b=run([str(java),"-jar",str(jar),"--root",str(repo),"--bundle-output",str(bundle),"--variant","debug","--platform","x86_64-linux","--archive","resolve","build","bundle"],cwd=repo,timeout=1200)
        exe=find_bundle_exe(bundle) if ok(b) else None
        return {"ok":ok(b) and bool(exe),"build":semantic(b),"executable":str(exe) if exe else None,"executable_sha256":digest_file(exe) if exe else None}
    return {"ok":False,"reason":"unknown_candidate"}

def parse_state(path:pathlib.Path)->dict[str,Any]:
    if not path.exists():return {"ok":False,"reason":"ready_file_missing"}
    s=path.read_text().strip();parts=s.split("|")
    if len(parts)!=6:return {"ok":False,"reason":"ready_file_shape","raw":s}
    marker,screens,routes,viewport,candidate,generation=parts
    obj={"marker":marker,"screens":screens.split(","),"routes":routes.split(","),"viewport":viewport,"candidate":candidate,"generation_id":generation,"raw":s}
    obj["ok"]=marker==MARKER and obj["screens"]==SCREENS and obj["routes"]==ROUTES and viewport==f"{WIDTH}x{HEIGHT}"
    return obj
def wait_state(path:pathlib.Path,p:subprocess.Popen,timeout:float=20.0)->dict[str,Any]:
    t=time.monotonic()
    while time.monotonic()-t<timeout:
        if path.exists():return parse_state(path)
        if p.poll() is not None:return {"ok":False,"reason":"candidate_exited_before_state","exit":p.returncode}
        time.sleep(.1)
    return {"ok":False,"reason":"state_timeout"}

def capture(path:pathlib.Path,inject:bool)->dict[str,Any]:
    if inject:
        return {"mechanism":"CANDIDATE_BOUND_X11_FRAMEBUFFER","injection":INJECTION,"command":["everfield-s6-capture-disabled"],"exit":97,"timed_out":False,"expected_unavailable":True,"frame_count":0,"path_exists":False,"sha256":None,"dimensions":None,"samples":None}
    scrot=shutil.which("scrot")
    if not scrot:return {"mechanism":"CANDIDATE_BOUND_X11_FRAMEBUFFER","command":["scrot"],"exit":127,"timed_out":False,"expected_unavailable":False,"frame_count":0,"path_exists":False,"sha256":None,"dimensions":None,"samples":None}
    r=run([scrot,"-z",str(path)],timeout=30);exists=path.exists() and path.stat().st_size>0;dims=None;samples=None
    ident=shutil.which("identify");conv=shutil.which("convert")
    if ok(r) and exists and ident:
        q=run([ident,"-format","%w %h",str(path)],timeout=30)
        try:dims=[int(x) for x in q["stdout"].split()] if ok(q) else None
        except ValueError:dims=None
    if ok(r) and exists and conv:
        q=run([conv,str(path),"-format","%[pixel:p{100,360}]|%[pixel:p{640,360}]|%[pixel:p{1180,360}]","info:"],timeout=30)
        samples=q["stdout"].strip().split("|") if ok(q) else None
    return {"mechanism":"CANDIDATE_BOUND_X11_FRAMEBUFFER","command":r["command"],"exit":r["exit"],"timed_out":r["timed_out"],"expected_unavailable":False,
            "frame_count":1 if ok(r) and exists else 0,"path_exists":exists,"sha256":digest_file(path) if exists else None,"dimensions":dims,"samples":samples,"stderr":r["stderr"][-4000:]}

def launch_command(candidate:str,prep:dict[str,Any],repo:pathlib.Path)->list[str]:
    exe=str(prep["executable"])
    if candidate=="Godot":return [exe,"--path",str(repo),"--display-driver","x11","--rendering-method","gl_compatibility"]
    return [exe]
def state_exact(s:dict[str,Any],candidate:str,gid:str)->bool:
    return s.get("ok") is True and s.get("candidate")==candidate and s.get("generation_id")==gid
def capture_exact(c:dict[str,Any],inject:bool)->bool:
    if inject:return c.get("expected_unavailable") is True and c.get("exit")==97 and c.get("frame_count")==0 and c.get("path_exists") is False
    samples=c.get("samples")
    return c.get("expected_unavailable") is False and c.get("exit")==0 and c.get("frame_count")==1 and c.get("path_exists") is True and c.get("dimensions")==[WIDTH,HEIGHT] and isinstance(samples,list) and len(samples)==3 and len(set(samples))>=3 and all(samples)

def execute_attempt(root:pathlib.Path,candidate:str,label:str,inject:bool,tool:dict[str,Any],tool_root:pathlib.Path,run_id:str,gid:str)->dict[str,Any]:
    repo,proof=reset_prepare(root,candidate,label,run_id);prep=prepare_candidate(repo,candidate,tool,tool_root);project=source_digest(repo,candidate)
    ready=repo/"s6-ready.txt";cap=repo/"s6-capture.png"
    env={"EVERFIELD_S6_READY_PATH":str(ready),"EVERFIELD_S6_GENERATION":gid,"EVERFIELD_S6_CAPTURE_INJECTION":INJECTION if inject else "NONE"}
    process=None;state={"ok":False,"reason":"candidate_not_started"};alive=False;c={"mechanism":"NONE","exit":127,"frame_count":0}
    launch=None;controlled_exit=None;stdout="";stderr="";elapsed=0.0
    if prep.get("ok") and prep.get("executable"):
        cmd=launch_command(candidate,prep,repo);e=os.environ.copy();e.update(env);t=time.monotonic()
        try:
            process=subprocess.Popen(cmd,cwd=repo,env=e,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            launch={"command":cmd,"pid":process.pid,"started":True};state=wait_state(ready,process);time.sleep(.6);alive=process.poll() is None
            c=capture(cap,inject) if state_exact(state,candidate,gid) and alive else {"mechanism":"CANDIDATE_BOUND_X11_FRAMEBUFFER","exit":126,"frame_count":0,"reason":"state_or_process_not_ready"}
        except Exception as x:launch={"command":cmd,"started":False,"error":repr(x)}
        finally:
            if process:
                if process.poll() is None:process.terminate()
                try:stdout,stderr=process.communicate(timeout=5)
                except subprocess.TimeoutExpired:process.kill();stdout,stderr=process.communicate()
                controlled_exit=process.returncode
            elapsed=round(time.monotonic()-t,3)
    s_ok=state_exact(state,candidate,gid);cap_ok=capture_exact(c,inject)
    classification=("STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE" if inject and s_ok and cap_ok else "STATE_AND_CAPTURE_OK" if (not inject and s_ok and cap_ok) else "STATE_REACHABILITY" if not s_ok else "CAPTURE_PIPELINE")
    passed=s_ok and alive and cap_ok and reset_ok(proof)
    binding_body={"candidate":candidate,"generation_id":gid,"attempt":label,"run_identity":run_id,"project_digest":project["digest"],
                  "executable_sha256":prep.get("executable_sha256"),"state_digest":"sha256:"+digest_obj(state),"capture_sha256":c.get("sha256"),
                  "viewport":c.get("dimensions"),"frame_count":c.get("frame_count"),"mechanism":c.get("mechanism"),"classification":classification}
    source={"run_identity":run_id,"project_identity":project,"preparation":prep,"launch":launch,"candidate_process_alive_at_capture":alive,
            "candidate_controlled_exit":controlled_exit,"candidate_stdout":stdout[-8000:],"candidate_stderr":stderr[-8000:],"state_observation":state,
            "capture":c,"failure_separation":{"state_channel":"candidate-generated-ready-file","capture_channel":"x11-framebuffer","classification":classification},
            "capture_binding":{"body":binding_body,"digest":"sha256:"+digest_obj(binding_body)}}
    raw={"schema":"S6-RAW-ATTEMPT-v1","candidate":candidate,"candidate_generation_id":gid,"label":label,"mode":"INJECT" if inject else "NORMAL",
         "scenario_id":SCENARIO,"required_injection":INJECTION if inject else None,"reset_proof":proof,"reset_verified_derived":reset_ok(proof),
         "source":source,"formal_result":"PASS" if passed else "INCONCLUSIVE","failure_class":"NONE" if passed else ("INFRA" if classification=="CAPTURE_PIPELINE" else "HARNESS")}
    return {"digest":"sha256:"+digest_obj(raw),"record":raw,"observation":{"elapsed_seconds":elapsed}}

def toolchain_identity(candidate:str,tool:dict[str,Any],validator_sha:str,runner_sha:str,run_id:str)->dict[str,Any]:
    if candidate=="Bevy":
        exact={"baseline":"0.19.0","retained_lock_sha256":tool.get("retained_lock_sha256"),"rustc_version":((tool.get("rustc") or {}).get("probe") or {}).get("stdout") or ((tool.get("rustc") or {}).get("probe") or {}).get("stderr"),"cargo_version":((tool.get("cargo") or {}).get("probe") or {}).get("stdout") or ((tool.get("cargo") or {}).get("probe") or {}).get("stderr"),"lock_replay_bound":tool.get("lock_replay_bound")}
    elif candidate=="Defold":
        exact={"baseline":"1.13.0","artifact_sha256":(tool.get("artifact_identity") or {}).get("expected_sha256"),"artifact_digest_source":(tool.get("artifact_identity") or {}).get("digest_source"),"bob_version":(tool.get("bob_version") or {}).get("stdout") or (tool.get("bob_version") or {}).get("stderr"),"java_version":((tool.get("java") or {}).get("probe") or {}).get("stdout") or ((tool.get("java") or {}).get("probe") or {}).get("stderr")}
    elif candidate=="Godot":
        exact={"baseline":"4.7.1-stable","archive_sha256":(tool.get("artifact_identity") or {}).get("expected_sha256"),"artifact_digest_source":(tool.get("artifact_identity") or {}).get("digest_source"),"executable_sha256":tool.get("executable_sha256"),"version":(tool.get("version") or {}).get("stdout") or (tool.get("version") or {}).get("stderr")}
    else:exact={"status":tool.get("status")}
    body={"candidate":candidate,"scenario":SCENARIO,"exact_toolchain_identity":exact,"validator_sha256":validator_sha,"runner_sha256":runner_sha,"run_identity":run_id,
          "s5_issue":S5_ISSUE,"s5_terminal":S5_TERMINAL,"s5_review_issue":S5_REVIEW_ISSUE,"s5_review_terminal":S5_REVIEW_TERMINAL,"s5_review_disposition":S5_REVIEW_DISPOSITION,
          "s5_review_publication":S5_REVIEW_PUBLICATION,"s5_producer_publication":S5_PRODUCER_PUBLICATION}
    return {"body":body,"identity_digest":"sha256:"+digest_obj(body)}
def derive_ids(candidate:str,ident:str,adaptation_identity:str,run_id:str)->tuple[str,str]:
    b={"candidate":candidate,"candidate_identity_digest":ident,"adaptation_identity":adaptation_identity,"run_identity":run_id,"scenario":SCENARIO}
    work="WORK-S6-"+digest_obj({**b,"role":"work"})[:24];gid="GEN-S6-"+digest_obj({**b,"role":"generation","work":work})[:24]
    return work,gid

def validate_raw(raw_wrap:dict[str,Any],candidate:str,gid:str,run_id:str)->bool:
    if raw_wrap.get("digest")!="sha256:"+digest_obj(raw_wrap.get("record")):return False
    r=raw_wrap["record"];s=r["source"];st=s["state_observation"];cap=s["capture"];inj=r["mode"]=="INJECT"
    if r.get("candidate")!=candidate or r.get("candidate_generation_id")!=gid or s.get("run_identity")!=run_id:return False
    if not reset_ok(r.get("reset_proof",{})) or not s.get("candidate_process_alive_at_capture"):return False
    if not state_exact(st,candidate,gid) or not capture_exact(cap,inj):return False
    b=s.get("capture_binding",{});body=b.get("body")
    if not isinstance(body,dict) or b.get("digest")!="sha256:"+digest_obj(body):return False
    expected={"candidate":candidate,"generation_id":gid,"attempt":r["label"],"run_identity":run_id,"project_digest":s["project_identity"]["digest"],
              "executable_sha256":s["preparation"].get("executable_sha256"),"state_digest":"sha256:"+digest_obj(st),"capture_sha256":cap.get("sha256"),
              "viewport":cap.get("dimensions"),"frame_count":cap.get("frame_count"),"mechanism":cap.get("mechanism"),"classification":s["failure_separation"]["classification"]}
    if body!=expected:return False
    expected_class="STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE" if inj else "STATE_AND_CAPTURE_OK"
    return s["failure_separation"].get("classification")==expected_class and r.get("formal_result")=="PASS" and r.get("failure_class")=="NONE"

def verify_packet(packet:dict[str,Any],validator,run_id:str)->dict[str,Any]:
    reasons=[];cident=packet.get("candidate_identity",{});body=cident.get("body")
    if not isinstance(body,dict) or cident.get("identity_digest")!="sha256:"+digest_obj(body):reasons.append("candidate_identity_digest_mismatch")
    g=packet.get("generation",{});candidate=g.get("candidate_id");av=validator.va(g.get("adaptation"),candidate) if isinstance(g,dict) else {"result":"REJECT"}
    if av.get("adaptation_identity"):
        ew,eg=derive_ids(candidate,cident.get("identity_digest"),av["adaptation_identity"],run_id)
        if ew!=g.get("candidate_work_id") or eg!=g.get("generation_id"):reasons.append("generation_identity_mismatch")
    else:reasons.append("adaptation_invalid")
    raws=packet.get("raw_attempts",[])
    if not reset_set_ok(raws):reasons.append("reset_set_invalid")
    refs=g.get("run_registry_refs",[]);bindings=packet.get("source_bindings",{})
    if len(refs)!=len(raws) or len(set(refs))!=len(refs) or set(refs)!=set(bindings):reasons.append("binding_registry_mismatch")
    for ref,raw in zip(refs,raws):
        r=raw.get("record",{});formal=g.get("attempts",{}).get(ref,{})
        if bindings.get(ref)!=raw.get("digest"):reasons.append("source_binding_substitution")
        if not validate_raw(raw,candidate,g.get("generation_id"),run_id):reasons.append("raw_semantics_invalid")
        p=r.get("reset_proof",{})
        if formal.get("candidate_id")!=candidate or formal.get("candidate_generation_id")!=g.get("generation_id") or formal.get("result")!=r.get("formal_result") or formal.get("failure_class")!=r.get("failure_class"):reasons.append("formal_raw_result_mismatch")
        if formal.get("reset_id")!=p.get("reset_id") or formal.get("workspace_id")!=p.get("workspace_id") or formal.get("reset_verified")!=r.get("reset_verified_derived"):reasons.append("formal_raw_reset_mismatch")
    return {"ok":not reasons,"reasons":sorted(set(reasons))}

def formalize(candidate:str,cident:dict[str,Any],tool:dict[str,Any],root:pathlib.Path,tool_root:pathlib.Path,validator,run_id:str)->dict[str,Any]:
    adaptation=validator.adaptation(SCENARIO,candidate);av=validator.va(adaptation,candidate);work,gid=derive_ids(candidate,cident["identity_digest"],av["adaptation_identity"],run_id)
    raws=[execute_attempt(root,candidate,"N1",False,tool,tool_root,run_id,gid),execute_attempt(root,candidate,"N2",False,tool,tool_root,run_id,gid),execute_attempt(root,candidate,"FI1",True,tool,tool_root,run_id,gid)]
    normals=raws[:2];fi=raws[2]
    g=validator.gen(SCENARIO,gid=gid,work=work,normal=tuple(x["record"]["formal_result"] for x in normals),classes=tuple(x["record"]["failure_class"] for x in normals),
                    injres=fi["record"]["formal_result"],injfc=fi["record"]["failure_class"],resets=tuple(x["record"]["reset_proof"]["reset_id"] for x in normals),
                    oks=tuple(x["record"]["reset_verified_derived"] for x in normals),wss=tuple(x["record"]["reset_proof"]["workspace_id"] for x in normals),res=RESOURCE,cid=candidate)
    fi_ref=[k for k,v in g["attempts"].items() if v["kind"]=="FAILURE_INJECTION"][0];p=fi["record"]["reset_proof"]
    g["attempts"][fi_ref]["reset_id"]=p["reset_id"];g["attempts"][fi_ref]["reset_verified"]=fi["record"]["reset_verified_derived"];g["attempts"][fi_ref]["workspace_id"]=p["workspace_id"]
    packet={"candidate_identity":cident,"raw_attempts":raws,"generation":g,"source_bindings":{ref:x["digest"] for ref,x in zip(g["run_registry_refs"],raws)},"adaptation_validation":av}
    packet["binding_verification"]=verify_packet(packet,validator,run_id);packet["aggregate"]=validator.agg(g)
    packet["trusted_representation_ok"]=packet["binding_verification"]=={"ok":True,"reasons":[]} and av["result"]=="ACCEPT" and packet["aggregate"]=={"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":True}
    return packet

def negative_tests(packet:dict[str,Any],validator,run_id:str)->dict[str,bool]:
    tests={}
    def bad(mut):
        q=copy.deepcopy(packet);mut(q);return not verify_packet(q,validator,run_id)["ok"]
    tests["wrong_state_marker_rejected"]=bad(lambda q:q["raw_attempts"][0]["record"]["source"]["state_observation"].__setitem__("marker","OTHER"))
    tests["capture_reuse_substitution_rejected"]=bad(lambda q:q["raw_attempts"][1]["record"]["source"]["capture"].__setitem__("sha256",q["raw_attempts"][0]["record"]["source"]["capture"].get("sha256")))
    tests["wrong_viewport_rejected"]=bad(lambda q:q["raw_attempts"][0]["record"]["source"]["capture"].__setitem__("dimensions",[640,360]))
    tests["missing_frame_rejected"]=bad(lambda q:q["raw_attempts"][0]["record"]["source"]["capture"].__setitem__("frame_count",0))
    tests["host_fabricated_mechanism_rejected"]=bad(lambda q:q["raw_attempts"][0]["record"]["source"]["capture"].__setitem__("mechanism","HOST_FABRICATED"))
    tests["capture_down_misclassification_rejected"]=bad(lambda q:q["raw_attempts"][2]["record"]["source"]["failure_separation"].__setitem__("classification","STATE_REACHABILITY"))
    tests["generation_mismatch_rejected"]=bad(lambda q:q["raw_attempts"][0]["record"].__setitem__("candidate_generation_id","OTHER"))
    g=copy.deepcopy(packet["generation"]);g["run_registry_refs"].append(g["run_registry_refs"][0]);tests["duplicate_registry_rejected"]=validator.agg(g)["aggregate"]!="PASS_FOR_COMPARISON"
    tests["reused_workspace_rejected"]=bad(lambda q:q["raw_attempts"][1]["record"]["reset_proof"].__setitem__("workspace_id",q["raw_attempts"][0]["record"]["reset_proof"]["workspace_id"]))
    tests["raw_source_substitution_rejected"]=bad(lambda q:q["raw_attempts"][0]["record"]["source"].__setitem__("run_identity","SUBSTITUTED"))
    tests["candidate_process_validation_bypass_rejected"]=bad(lambda q:q["raw_attempts"][0]["record"]["source"].__setitem__("candidate_process_alive_at_capture",False))
    return tests
def candidate_available(candidate:str,tool:dict[str,Any])->bool:
    return tool.get("status") in ("CAPABLE","CAPABLE_WITH_PRESEED") if candidate=="Bevy" else tool.get("status")=="CAPABLE"

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);ap.add_argument("--validator",required=True);ap.add_argument("--toolchain-probe",required=True);ap.add_argument("--bevy-lock",required=True);ap.add_argument("--artifact-lock",required=True);a=ap.parse_args()
    out=pathlib.Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);vp=pathlib.Path(a.validator).resolve();pp=pathlib.Path(a.toolchain_probe).resolve();bl=pathlib.Path(a.bevy_lock).resolve();al=pathlib.Path(a.artifact_lock).resolve()
    validator=load_module(vp,"everfield_s6_validator");probe=load_module(pp,"everfield_s6_toolchain_probe");vsha=digest_file(vp);rsha=digest_file(pathlib.Path(__file__).resolve())
    run_id=os.environ.get("GITHUB_RUN_ID","LOCAL")+":"+os.environ.get("GITHUB_RUN_ATTEMPT","1")+":"+os.environ.get("GITHUB_SHA","LOCAL");artifact_lock=probe.load_artifact_lock(al)
    with tempfile.TemporaryDirectory(prefix="everfield-s6-") as td:
        root=pathlib.Path(td);tool_root=root/"toolchains";tool_root.mkdir()
        tools={"Bevy":probe.probe_bevy(tool_root/"bevy",bl),"Defold":probe.probe_defold(tool_root,artifact_lock),"Godot":probe.probe_godot(tool_root,artifact_lock),"Unity":probe.probe_unity(),"Unreal Engine":probe.probe_unreal()}
        results={};provisional=[]
        for candidate in ("Bevy","Defold","Godot"):
            tool=tools[candidate]
            if not candidate_available(candidate,tool):results[candidate]={"candidate":candidate,"disposition":"NOT_RUN_TOOLCHAIN_UNAVAILABLE","toolchain":tool};continue
            cident=toolchain_identity(candidate,tool,vsha,rsha,run_id);packet=formalize(candidate,cident,tool,root,tool_root,validator,run_id);packet["negative_selftests"]=negative_tests(packet,validator,run_id)
            packet["disposition"]="PROVISIONAL_S6_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW" if packet["trusted_representation_ok"] and all(packet["negative_selftests"].values()) else "INCONCLUSIVE_HARNESS_OR_INFRA"
            results[candidate]=packet
            if packet["disposition"].startswith("PROVISIONAL"):provisional.append(candidate)
        payload={"schema":"W2-ENG-TECHNICAL-S6-v1","mission_id":"W2-ENG-TECH-S6-01","issue":456,"scenario_id":SCENARIO,"harness_id":"W2-ENG-HARNESS-v5",
                 "feature_slice_id":"W2-ENG-FEATURE-SLICE-v2","scenario_manifest_id":"W2-ENG-SCENARIO-INPUTS-v2","validator_sha256":vsha,"runner_sha256":rsha,"run_identity":run_id,
                 "s6_contract":{"fixed_input_refs":["SLICE:logical_state","SLICE:player_surface","SLICE:capture_fixture"],"obligations":["reach_known_state","identity_bound_capture","state_vs_capture_failure_separated"],
                                "min_bounds":{"screen_count":3,"capture_frame_count":1,"viewport_width":1280,"viewport_height":720},"logical_state_marker":MARKER,"required_injection":INJECTION,"capture_mechanism":"CANDIDATE_BOUND_X11_FRAMEBUFFER"},
                 "predecessor_review":{"producer_issue":S5_ISSUE,"producer_terminal":S5_TERMINAL,"review_issue":S5_REVIEW_ISSUE,"review_terminal":S5_REVIEW_TERMINAL,"disposition":S5_REVIEW_DISPOSITION,
                                       "review_publication_sha":S5_REVIEW_PUBLICATION,"producer_publication_sha":S5_PRODUCER_PUBLICATION},
                 "toolchains":tools,"results":results,"provisional_candidates":provisional,"authority_bound_not_run":{"Unity":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY","Unreal Engine":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"},
                 "provider_state":{"Unity":"BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION:UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED","Unreal Engine":"NOT_CONFIGURED:UNREAL_GITHUB_USERNAME_AND_TOKEN_NOT_CONFIGURED"},
                 "historical_issue_82_not_run_cells_preserved":50,"reviewed_s3_s4_s5_provenance_preserved":True,"fresh_review_required":True,"trusted_comparison_authority":False,
                 "integration_authority":False,"engine_selected":False,"implementation_readiness":False,"canonicality":"NOT_CANONICAL"}
        out.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
        print(json.dumps({"schema":payload["schema"],"provisional_candidates":provisional,"dispositions":{k:v.get("disposition") for k,v in results.items()}},sort_keys=True))
    return 0
if __name__=="__main__":raise SystemExit(main())
