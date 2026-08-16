#!/usr/bin/env python3
"""W2-ENG-TECH-S6-REM-01: Godot-only S6 capture remediation."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, pathlib, shutil, subprocess, tempfile, time
from typing import Any

SCENARIO="S6"; CANDIDATE="Godot"; RESOURCE="W2-ENG-HOST-COMMON-v2"
MARKER="CAPTURE-STATE-042"; INJECTION="FI-S6-CAPTURE-DOWN-v2"; WIDTH=1280; HEIGHT=720
SCREENS=["BOOT_OR_MAIN","PLAY_SURFACE","SETTINGS"]
ROUTES=["BOOT_OR_MAIN->PLAY_SURFACE","PLAY_SURFACE->SETTINGS","SETTINGS->PLAY_SURFACE"]
ATTEMPT_HEX={"N1":"E6CC1A","N2":"E61ACC","FI1":"1ACCE6"}
PRODUCER_HEAD="0719199237d3ac46505f52a06df0a0fc93429c9f"
REVIEW_HEAD="d2e7c34e583eedd2b2d5c4b02c8969e581b80563"

def canon(o:Any)->str:return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def dobj(o:Any)->str:return hashlib.sha256(canon(o).encode()).hexdigest()
def dfile(p:pathlib.Path)->str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()
def module(path:pathlib.Path,name:str):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def run(cmd:list[str],cwd:pathlib.Path|None=None,env:dict[str,str]|None=None,timeout:int=120)->dict[str,Any]:
    e=os.environ.copy();e.update(env or {});t=time.monotonic()
    try:
        p=subprocess.run(cmd,cwd=cwd,env=e,text=True,capture_output=True,timeout=timeout,check=False)
        return {"command":cmd,"exit":p.returncode,"timed_out":False,"seconds":round(time.monotonic()-t,3),"stdout":p.stdout[-8000:],"stderr":p.stderr[-8000:]}
    except subprocess.TimeoutExpired as x:
        return {"command":cmd,"exit":None,"timed_out":True,"seconds":round(time.monotonic()-t,3),"stdout":x.stdout[-8000:] if isinstance(x.stdout,str) else "","stderr":x.stderr[-8000:] if isinstance(x.stderr,str) else ""}
def ok(r:dict[str,Any])->bool:return r.get("exit")==0 and not r.get("timed_out")
def write(p:pathlib.Path,s:str):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)

def project_files()->dict[str,str]:
    return {
      "project.godot":'''[application]\nconfig/name="Everfield S6 Remediation"\nrun/main_scene="res://main.tscn"\n[display]\nwindow/size/viewport_width=1280\nwindow/size/viewport_height=720\nwindow/size/window_width_override=1280\nwindow/size/window_height_override=720\nwindow/resizable=false\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n''',
      "main.tscn":'''[gd_scene load_steps=2 format=3]\n\n[ext_resource path="res://main.gd" type="Script" id="1"]\n\n[node name="Main" type="Node2D"]\nscript = ExtResource("1")\n''',
      "main.gd":r'''extends Node2D
func marker_color(a:String)->Color:
    if a == "N1": return Color8(230,204,26,255)
    if a == "N2": return Color8(230,26,204,255)
    return Color8(26,204,230,255)
func marker_hex(a:String)->String:
    if a == "N1": return "E6CC1A"
    if a == "N2": return "E61ACC"
    return "1ACCE6"
func _ready():
    var p=OS.get_environment("EVERFIELD_S6_READY_PATH")
    var g=OS.get_environment("EVERFIELD_S6_GENERATION")
    var a=OS.get_environment("EVERFIELD_S6_ATTEMPT")
    var f=FileAccess.open(p,FileAccess.WRITE)
    f.store_string("CAPTURE-STATE-042|BOOT_OR_MAIN,PLAY_SURFACE,SETTINGS|BOOT_OR_MAIN->PLAY_SURFACE,PLAY_SURFACE->SETTINGS,SETTINGS->PLAY_SURFACE|1280x720|Godot|"+g+"|"+a+"|"+marker_hex(a))
    f.close()
    print("EVERFIELD_S6_STATE:CAPTURE-STATE-042:"+a)
    queue_redraw()
func _draw():
    draw_rect(Rect2(0,0,426,720),Color8(204,31,31,255))
    draw_rect(Rect2(426,0,428,720),Color8(31,184,51,255))
    draw_rect(Rect2(854,0,426,720),Color8(31,64,219,255))
    draw_rect(Rect2(1200,0,80,720),marker_color(OS.get_environment("EVERFIELD_S6_ATTEMPT")))
'''}

def materialize(repo:pathlib.Path):
    for rel,text in project_files().items():write(repo/rel,text)
def project_identity(repo:pathlib.Path)->dict[str,Any]:
    fs={rel:dfile(repo/rel) for rel in sorted(project_files())};return {"files":fs,"digest":"sha256:"+dobj(fs)}
def reset(root:pathlib.Path,label:str,run_id:str)->tuple[pathlib.Path,dict[str,Any]]:
    p=root/label;absent=not p.exists();p.mkdir(parents=True,exist_ok=False)
    proof={"pre_workspace_absent":absent,"workspace_created_exclusive":p.exists(),"workspace_id":"WS-S6R-"+dobj({"run":run_id,"label":label,"kind":"ws"})[:24],"reset_id":"RESET-S6R-"+dobj({"run":run_id,"label":label,"kind":"reset"})[:24]}
    return p,proof
def reset_ok(p:dict[str,Any])->bool:return p.get("pre_workspace_absent") is True and p.get("workspace_created_exclusive") is True and bool(p.get("workspace_id")) and bool(p.get("reset_id"))
def parse_state(path:pathlib.Path)->dict[str,Any]:
    if not path.exists():return {"ok":False,"reason":"missing"}
    parts=path.read_text().strip().split("|")
    if len(parts)!=8:return {"ok":False,"reason":"shape","raw":path.read_text()}
    m,screens,routes,viewport,candidate,gid,attempt,mhex=parts
    r={"marker":m,"screens":screens.split(","),"routes":routes.split(","),"viewport":viewport,"candidate":candidate,"generation_id":gid,"attempt":attempt,"attempt_marker_hex":mhex}
    r["ok"]=m==MARKER and r["screens"]==SCREENS and r["routes"]==ROUTES and viewport=="1280x720" and candidate==CANDIDATE and ATTEMPT_HEX.get(attempt)==mhex
    return r
def wait_state(path:pathlib.Path,p:subprocess.Popen,timeout:float=20)->dict[str,Any]:
    t=time.monotonic()
    while time.monotonic()-t<timeout:
        if path.exists():return parse_state(path)
        if p.poll() is not None:return {"ok":False,"reason":"early_exit","exit":p.returncode}
        time.sleep(.1)
    return {"ok":False,"reason":"timeout"}
def img_facts(path:pathlib.Path)->dict[str,Any]:
    ident=shutil.which("identify");conv=shutil.which("convert")
    if not path.exists() or not ident or not conv:return {"exists":path.exists(),"dimensions":None,"marker_hex":None,"panel_hex":None}
    q=run([ident,"-format","%w %h",str(path)],timeout=20);dims=None
    try:dims=[int(x) for x in q["stdout"].split()] if ok(q) else None
    except ValueError:pass
    q2=run([conv,str(path),"-format","%[hex:p{1240,360}]|%[hex:p{100,360}]|%[hex:p{640,360}]|%[hex:p{1100,360}]","info:"],timeout=20)
    vals=q2["stdout"].strip().upper().split("|") if ok(q2) else []
    vals=[x[:6] for x in vals]
    return {"exists":True,"dimensions":dims,"marker_hex":vals[0] if len(vals)==4 else None,"panel_hex":vals[1:] if len(vals)==4 else None}
def capture(frame:pathlib.Path,inject:bool)->dict[str,Any]:
    scrot=shutil.which("scrot")
    if not scrot:return {"program":"scrot","real_capture_invoked":False,"exit":127,"timed_out":False,"frame_count":0,"path_exists":False}
    display=":199" if inject else os.environ.get("DISPLAY",":99")
    if frame.exists():frame.unlink()
    r=run([scrot,"-z",str(frame)],env={"DISPLAY":display},timeout=30)
    exists=frame.exists() and frame.stat().st_size>0
    facts=img_facts(frame) if exists else {"exists":False,"dimensions":None,"marker_hex":None,"panel_hex":None}
    return {"program":"scrot","real_capture_invoked":True,"capture_environment":{"DISPLAY":display},"command":r["command"],"exit":r["exit"],"timed_out":r["timed_out"],"stdout":r["stdout"],"stderr":r["stderr"],"frame_count":1 if ok(r) and exists else 0,"path_exists":exists,"sha256":dfile(frame) if exists else None,"dimensions":facts["dimensions"],"marker_hex":facts["marker_hex"],"panel_hex":facts["panel_hex"]}
def state_ok(s:dict[str,Any],gid:str,label:str)->bool:return s.get("ok") is True and s.get("generation_id")==gid and s.get("attempt")==label and s.get("attempt_marker_hex")==ATTEMPT_HEX[label]
def capture_ok(c:dict[str,Any],label:str,inject:bool)->bool:
    if inject:return c.get("real_capture_invoked") is True and c.get("program")=="scrot" and c.get("capture_environment",{}).get("DISPLAY")==":199" and c.get("exit") not in (0,None) and c.get("timed_out") is False and c.get("path_exists") is False and c.get("frame_count")==0
    panels=c.get("panel_hex")
    return c.get("real_capture_invoked") is True and c.get("exit")==0 and c.get("path_exists") is True and c.get("frame_count")==1 and c.get("dimensions")==[WIDTH,HEIGHT] and c.get("marker_hex")==ATTEMPT_HEX[label] and isinstance(panels,list) and len(panels)==3 and len(set(panels))==3

def exact_tool_identity(tool:dict[str,Any],validator_sha:str,runner_sha:str,run_id:str)->dict[str,Any]:
    body={"candidate":"Godot","baseline":"4.7.1-stable","archive_sha256":(tool.get("artifact_identity") or {}).get("expected_sha256"),"artifact_digest_source":(tool.get("artifact_identity") or {}).get("digest_source"),"executable_sha256":tool.get("executable_sha256"),"version":(tool.get("version") or {}).get("stdout") or (tool.get("version") or {}).get("stderr"),"validator_sha256":validator_sha,"runner_sha256":runner_sha,"run_identity":run_id,"producer_head":PRODUCER_HEAD,"review_head":REVIEW_HEAD}
    return {"body":body,"identity_digest":"sha256:"+dobj(body)}
def ids(identity_digest:str,adaptation_identity:str,run_id:str)->tuple[str,str]:
    b={"candidate":"Godot","candidate_identity_digest":identity_digest,"adaptation_identity":adaptation_identity,"run_identity":run_id,"scenario":"S6","remediation":"M01+M02"}
    work="WORK-S6R-"+dobj({**b,"role":"work"})[:24];gid="GEN-S6R-"+dobj({**b,"role":"generation","work":work})[:24];return work,gid

def attempt(root:pathlib.Path,out:pathlib.Path,label:str,inject:bool,exe:str,exe_sha:str,gid:str,run_id:str)->dict[str,Any]:
    repo,proof=reset(root,label,run_id);materialize(repo);proj=project_identity(repo);ready=repo/"ready.txt";frame=out/"frames"/"Godot"/(label+".png");frame.parent.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy();env.update({"EVERFIELD_S6_READY_PATH":str(ready),"EVERFIELD_S6_GENERATION":gid,"EVERFIELD_S6_ATTEMPT":label})
    cmd=[exe,"--path",str(repo),"--display-driver","x11","--rendering-method","gl_compatibility"]
    p=subprocess.Popen(cmd,cwd=repo,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE);state=wait_state(ready,p);time.sleep(.8);alive=p.poll() is None
    cap=capture(frame,inject) if state_ok(state,gid,label) and alive else {"program":"scrot","real_capture_invoked":False,"exit":126,"frame_count":0,"path_exists":False,"reason":"state_or_process_not_ready"}
    if p.poll() is None:p.terminate()
    try:stdout,stderr=p.communicate(timeout=5)
    except subprocess.TimeoutExpired:p.kill();stdout,stderr=p.communicate()
    passed=state_ok(state,gid,label) and alive and capture_ok(cap,label,inject) and reset_ok(proof)
    classification="STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE" if inject and passed else "STATE_AND_CAPTURE_OK" if passed else "STATE_REACHABILITY" if not state_ok(state,gid,label) else "CAPTURE_PIPELINE"
    retained=None if inject else {"relative_path":str(frame.relative_to(out)),"sha256":cap.get("sha256"),"dimensions":cap.get("dimensions"),"attempt_marker_hex":cap.get("marker_hex")}
    source={"run_identity":run_id,"project_identity":proj,"candidate_executable_sha256":exe_sha,"launch":{"command":cmd},"candidate_process_alive_at_capture":alive,"candidate_exit":p.returncode,"candidate_stdout":stdout[-6000:],"candidate_stderr":stderr[-6000:],"state_observation":state,"capture":cap,"retained_frame":retained,"failure_separation":{"classification":classification,"state_channel":"candidate-generated-ready-file","capture_channel":"scrot-on-X-display"}}
    bindbody={"candidate":"Godot","generation_id":gid,"attempt":label,"run_identity":run_id,"project_digest":proj["digest"],"executable_sha256":exe_sha,"state_digest":"sha256:"+dobj(state),"retained_frame_sha256":retained["sha256"] if retained else None,"attempt_marker_hex":ATTEMPT_HEX[label],"capture_display":cap.get("capture_environment",{}).get("DISPLAY"),"capture_exit":cap.get("exit"),"classification":classification}
    source["capture_binding"]={"body":bindbody,"digest":"sha256:"+dobj(bindbody)}
    raw={"schema":"S6R-RAW-ATTEMPT-v1","candidate":"Godot","candidate_generation_id":gid,"label":label,"mode":"INJECT" if inject else "NORMAL","scenario_id":"S6","required_injection":INJECTION if inject else None,"reset_proof":proof,"reset_verified_derived":reset_ok(proof),"source":source,"formal_result":"PASS" if passed else "INCONCLUSIVE","failure_class":"NONE" if passed else "INFRA"}
    return {"digest":"sha256:"+dobj(raw),"record":raw}

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);ap.add_argument("--validator",required=True);ap.add_argument("--toolchain-probe",required=True);ap.add_argument("--artifact-lock",required=True);a=ap.parse_args()
    out=pathlib.Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True);vp=pathlib.Path(a.validator).resolve();pp=pathlib.Path(a.toolchain_probe).resolve();al=pathlib.Path(a.artifact_lock).resolve();validator=module(vp,"s6r_validator");probe=module(pp,"s6r_probe")
    run_id=os.environ.get("GITHUB_RUN_ID","LOCAL")+":"+os.environ.get("GITHUB_RUN_ATTEMPT","1")+":"+os.environ.get("GITHUB_SHA","LOCAL");runner_sha=dfile(pathlib.Path(__file__).resolve());validator_sha=dfile(vp)
    with tempfile.TemporaryDirectory(prefix="s6-rem-") as td:
        root=pathlib.Path(td);toolroot=root/"toolchains";toolroot.mkdir();lock=probe.load_artifact_lock(al);tool=probe.probe_godot(toolroot,lock)
        if tool.get("status")!="CAPABLE":raise SystemExit("Godot exact toolchain unavailable: "+json.dumps(tool,sort_keys=True))
        ident=exact_tool_identity(tool,validator_sha,runner_sha,run_id);adapt=validator.adaptation("S6","Godot");av=validator.va(adapt,"Godot");work,gid=ids(ident["identity_digest"],av["adaptation_identity"],run_id)
        exe=tool["executable"];exe_sha=tool.get("executable_sha256")
        raws=[attempt(root,out,"N1",False,exe,exe_sha,gid,run_id),attempt(root,out,"N2",False,exe,exe_sha,gid,run_id),attempt(root,out,"FI1",True,exe,exe_sha,gid,run_id)]
        n1,n2,fi=[x["record"] for x in raws];normal_pass=all(x["formal_result"]=="PASS" for x in (n1,n2));fi_pass=fi["formal_result"]=="PASS";distinct=n1["source"]["capture"].get("sha256")!=n2["source"]["capture"].get("sha256")
        g=validator.gen("S6",gid=gid,work=work,normal=(n1["formal_result"],n2["formal_result"]),classes=(n1["failure_class"],n2["failure_class"]),injres=fi["formal_result"],injfc=fi["failure_class"],resets=(n1["reset_proof"]["reset_id"],n2["reset_proof"]["reset_id"]),oks=(n1["reset_verified_derived"],n2["reset_verified_derived"]),wss=(n1["reset_proof"]["workspace_id"],n2["reset_proof"]["workspace_id"]),res=RESOURCE,cid="Godot")
        firef=[r for r in g["run_registry_refs"] if g["attempts"][r]["kind"]=="FAILURE_INJECTION"][0];g["attempts"][firef]["reset_id"]=fi["reset_proof"]["reset_id"];g["attempts"][firef]["reset_verified"]=fi["reset_verified_derived"];g["attempts"][firef]["workspace_id"]=fi["reset_proof"]["workspace_id"]
        aggregate=validator.agg(g);refs=g["run_registry_refs"];bindings={r:x["digest"] for r,x in zip(refs,raws)}
        local_ok=normal_pass and fi_pass and distinct and av.get("result")=="ACCEPT" and aggregate=={"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":True}
        payload={"schema":"W2-ENG-TECHNICAL-S6-REMEDIATION-v1","mission_id":"W2-ENG-TECH-S6-REM-01","issue":460,"scenario_id":"S6","run_identity":run_id,"validator_sha256":validator_sha,"runner_sha256":runner_sha,"frozen_provenance":{"producer_issue":456,"producer_terminal":5309296967,"producer_head":PRODUCER_HEAD,"producer_run":31967674130,"producer_artifact":9268994399,"review_issue":458,"review_terminal":5309336848,"review_head":REVIEW_HEAD,"review_findings":["W2-ENG-TECH-S6-REV-M01","W2-ENG-TECH-S6-REV-M02"]},"candidate_identity":ident,"adaptation_validation":av,"generation":g,"raw_attempts":raws,"source_bindings":bindings,"aggregate":aggregate,"normal_frame_sha256":{"N1":n1["source"]["capture"].get("sha256"),"N2":n2["source"]["capture"].get("sha256")},"normal_frames_byte_distinct":distinct,"local_semantics_ok":local_ok,"candidate_matrix":{"Godot":"REMEDIATED_EMPIRICAL_S6_EVIDENCE_PENDING_REQUIRED_REVIEW" if local_ok else "CHANGES_STILL_REQUIRED","Bevy":"INCONCLUSIVE_HARNESS_OR_INFRA","Defold":"INCONCLUSIVE_HARNESS_OR_INFRA","Unity":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY","Unreal Engine":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"},"fresh_required_review":True,"trusted_bounded_s6_comparison_authority":False,"integration_authority":False,"engine_selected":False,"implementation_readiness":False,"canonicality":"NOT_CANONICAL"}
        (out/"evidence.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n");print(json.dumps({"generation":gid,"local_ok":local_ok,"frame_sha":payload["normal_frame_sha256"],"fi_exit":fi["source"]["capture"].get("exit")},sort_keys=True));return 0 if local_ok else 1
if __name__=="__main__":raise SystemExit(main())
