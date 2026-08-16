#!/usr/bin/env python3
"""Independent byte-bearing verifier for W2-ENG-TECH-S6-REM-01."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, pathlib, shutil, subprocess, tempfile
from typing import Any
MARKER="CAPTURE-STATE-042"; WIDTH=1280; HEIGHT=720
SCREENS=["BOOT_OR_MAIN","PLAY_SURFACE","SETTINGS"]
ROUTES=["BOOT_OR_MAIN->PLAY_SURFACE","PLAY_SURFACE->SETTINGS","SETTINGS->PLAY_SURFACE"]
ATTEMPT_HEX={"N1":"E6CC1A","N2":"E61ACC","FI1":"1ACCE6"}
def canon(o:Any)->str:return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def dobj(o:Any)->str:return hashlib.sha256(canon(o).encode()).hexdigest()
def dfile(p:pathlib.Path)->str:
 h=hashlib.sha256();h.update(p.read_bytes());return h.hexdigest()
def module(p:pathlib.Path):
 s=importlib.util.spec_from_file_location("s6rv",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def cmd(c:list[str])->tuple[int,str,str]:
 p=subprocess.run(c,text=True,capture_output=True,check=False);return p.returncode,p.stdout,p.stderr
def normhex(s:str)->str:
 s=s.strip().upper()
 if len(s)>=12:return s[0:2]+s[4:6]+s[8:10]
 return s[:6]
def image_facts(p:pathlib.Path)->dict[str,Any]:
 if not p.exists():return {"ok":False,"reason":"missing"}
 ident=shutil.which("identify");conv=shutil.which("convert")
 if not ident or not conv:return {"ok":False,"reason":"imagemagick_missing"}
 rc,o,e=cmd([ident,"-format","%w %h",str(p)])
 try:dims=[int(x) for x in o.split()] if rc==0 else None
 except ValueError:dims=None
 rc2,o2,e2=cmd([conv,str(p),"-format","%[hex:p{1240,360}]|%[hex:p{100,360}]|%[hex:p{640,360}]|%[hex:p{1100,360}]","info:"])
 vals=[normhex(x) for x in o2.strip().split("|")] if rc2==0 else []
 return {"ok":rc==0 and rc2==0,"dimensions":dims,"marker_hex":vals[0] if len(vals)==4 else None,"panel_hex":vals[1:] if len(vals)==4 else None,"sha256":dfile(p)}
def state_ok(s:dict[str,Any],gid:str,label:str)->bool:
 return s.get("ok") is True and s.get("marker")==MARKER and s.get("screens")==SCREENS and s.get("routes")==ROUTES and s.get("viewport")=="1280x720" and s.get("candidate")=="Godot" and s.get("generation_id")==gid and s.get("attempt")==label and s.get("attempt_marker_hex")==ATTEMPT_HEX[label]
def reset_ok(p:dict[str,Any])->bool:return p.get("pre_workspace_absent") is True and p.get("workspace_created_exclusive") is True and bool(p.get("workspace_id")) and bool(p.get("reset_id"))
def ids(identity_digest:str,adaptation_identity:str,run_id:str)->tuple[str,str]:
 b={"candidate":"Godot","candidate_identity_digest":identity_digest,"adaptation_identity":adaptation_identity,"run_identity":run_id,"scenario":"S6","remediation":"M01+M02"};work="WORK-S6R-"+dobj({**b,"role":"work"})[:24];gid="GEN-S6R-"+dobj({**b,"role":"generation","work":work})[:24];return work,gid
def verify_binding(r:dict[str,Any],gid:str)->list[str]:
 why=[];s=r["source"];label=r["label"];st=s["state_observation"];cap=s["capture"];ret=s.get("retained_frame")
 body=s.get("capture_binding",{}).get("body");bd=s.get("capture_binding",{}).get("digest")
 if not isinstance(body,dict) or bd!="sha256:"+dobj(body):why.append("capture_binding_digest")
 else:
  exp={"candidate":"Godot","generation_id":gid,"attempt":label,"run_identity":s["run_identity"],"project_digest":s["project_identity"]["digest"],"executable_sha256":s["candidate_executable_sha256"],"state_digest":"sha256:"+dobj(st),"retained_frame_sha256":ret["sha256"] if ret else None,"attempt_marker_hex":ATTEMPT_HEX[label],"capture_display":cap.get("capture_environment",{}).get("DISPLAY"),"capture_exit":cap.get("exit"),"classification":s["failure_separation"]["classification"]}
  if body!=exp:why.append("capture_binding_body")
 return why
def verify_normal(w:dict[str,Any],gid:str,out:pathlib.Path,path_override:pathlib.Path|None=None)->dict[str,Any]:
 r=w["record"];label=r["label"];s=r["source"];ret=s.get("retained_frame") or {};why=[]
 if w.get("digest")!="sha256:"+dobj(r):why.append("raw_digest")
 if r.get("candidate_generation_id")!=gid or r.get("formal_result")!="PASS" or r.get("failure_class")!="NONE":why.append("formal")
 if not reset_ok(r.get("reset_proof",{})):why.append("reset")
 if s.get("candidate_process_alive_at_capture") is not True:why.append("process")
 if not state_ok(s.get("state_observation",{}),gid,label):why.append("state")
 cap=s.get("capture",{});p=path_override or (out/ret.get("relative_path",""));facts=image_facts(p)
 if not facts.get("ok") or facts.get("dimensions")!=[WIDTH,HEIGHT] or facts.get("marker_hex")!=ATTEMPT_HEX[label] or len(set(facts.get("panel_hex") or []))!=3:why.append("retained_frame_pixels")
 if not path_override:
  if facts.get("sha256")!=ret.get("sha256") or facts.get("sha256")!=cap.get("sha256"):why.append("retained_frame_hash")
 if cap.get("real_capture_invoked") is not True or cap.get("program")!="scrot" or cap.get("exit")!=0 or cap.get("frame_count")!=1 or cap.get("path_exists") is not True or cap.get("dimensions")!=[WIDTH,HEIGHT] or cap.get("marker_hex")!=ATTEMPT_HEX[label]:why.append("capture_facts")
 if s.get("failure_separation",{}).get("classification")!="STATE_AND_CAPTURE_OK":why.append("classification")
 why.extend(verify_binding(r,gid));return {"ok":not why,"reasons":sorted(set(why)),"frame":facts}
def verify_fi(w:dict[str,Any],gid:str)->dict[str,Any]:
 r=w["record"];s=r["source"];cap=s["capture"];why=[]
 if w.get("digest")!="sha256:"+dobj(r):why.append("raw_digest")
 if r.get("candidate_generation_id")!=gid or r.get("required_injection")!="FI-S6-CAPTURE-DOWN-v2" or r.get("formal_result")!="PASS" or r.get("failure_class")!="NONE":why.append("formal")
 if not reset_ok(r.get("reset_proof",{})):why.append("reset")
 if not state_ok(s.get("state_observation",{}),gid,"FI1") or s.get("candidate_process_alive_at_capture") is not True:why.append("state_process")
 command=cap.get("command") or []
 if cap.get("real_capture_invoked") is not True or cap.get("program")!="scrot" or not command or pathlib.Path(command[0]).name!="scrot" or cap.get("capture_environment",{}).get("DISPLAY")!=":199" or cap.get("exit") in (0,None) or cap.get("timed_out") is not False or cap.get("path_exists") is not False or cap.get("frame_count")!=0:why.append("real_capture_failure")
 if s.get("failure_separation",{}).get("classification")!="STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE":why.append("classification")
 why.extend(verify_binding(r,gid));return {"ok":not why,"reasons":sorted(set(why)),"observed_exit":cap.get("exit"),"observed_stderr":cap.get("stderr")}
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("--evidence",required=True);ap.add_argument("--validator",required=True);ap.add_argument("--out",required=True);a=ap.parse_args();ep=pathlib.Path(a.evidence).resolve();root=ep.parent;d=json.loads(ep.read_text());v=module(pathlib.Path(a.validator).resolve());why=[]
 ident=d["candidate_identity"];body=ident.get("body");
 if not isinstance(body,dict) or ident.get("identity_digest")!="sha256:"+dobj(body):why.append("candidate_identity")
 av=v.va(d["generation"]["adaptation"],"Godot");ew,eg=ids(ident["identity_digest"],av.get("adaptation_identity"),d["run_identity"])
 if d["generation"].get("candidate_work_id")!=ew or d["generation"].get("generation_id")!=eg:why.append("generation_identity")
 gid=eg;raws=d["raw_attempts"];n1=verify_normal(raws[0],gid,root);n2=verify_normal(raws[1],gid,root);fi=verify_fi(raws[2],gid)
 ps=[x["record"]["reset_proof"] for x in raws]
 if len({x["workspace_id"] for x in ps})!=3 or len({x["reset_id"] for x in ps})!=3:why.append("reset_reuse")
 refs=d["generation"]["run_registry_refs"]
 if len(refs)!=3 or len(set(refs))!=3 or set(refs)!=set(d["source_bindings"]):why.append("registry")
 for ref,w in zip(refs,raws):
  if d["source_bindings"].get(ref)!=w.get("digest"):why.append("source_binding")
 agg=v.agg(d["generation"])
 if av.get("result")!="ACCEPT" or agg!={"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":True}:why.append("v5_envelope")
 if not n1["ok"] or not n2["ok"] or not fi["ok"]:why.append("attempt_semantics")
 if n1["frame"].get("sha256")==n2["frame"].get("sha256"):why.append("normal_frames_not_distinct")
 # Actual-byte substitution attack: copy N1 bytes into a synthetic N2 object, recompute every byte hash/binding/raw digest, and still require rejection from the N2 candidate-rendered marker pixels.
 with tempfile.TemporaryDirectory(prefix="s6r-sub-") as td:
  sub=pathlib.Path(td)/"n2-substituted.png";sub.write_bytes((root/raws[0]["record"]["source"]["retained_frame"]["relative_path"]).read_bytes())
  q=copy.deepcopy(raws[1]);r=q["record"];s=r["source"];sha=dfile(sub);s["retained_frame"]["sha256"]=sha;s["capture"]["sha256"]=sha;s["capture_binding"]["body"]["retained_frame_sha256"]=sha;s["capture_binding"]["digest"]="sha256:"+dobj(s["capture_binding"]["body"]);q["digest"]="sha256:"+dobj(r)
  subcheck=verify_normal(q,gid,root,path_override=sub);actual_byte_substitution_rejected=not subcheck["ok"] and "retained_frame_pixels" in subcheck["reasons"]
 # FI misclassification attack.
 q=copy.deepcopy(raws[2]);q["record"]["source"]["failure_separation"]["classification"]="STATE_REACHABILITY";q["record"]["source"]["capture_binding"]["body"]["classification"]="STATE_REACHABILITY";q["record"]["source"]["capture_binding"]["digest"]="sha256:"+dobj(q["record"]["source"]["capture_binding"]["body"]);q["digest"]="sha256:"+dobj(q["record"]);fi_misclassification_rejected=not verify_fi(q,gid)["ok"]
 if not actual_byte_substitution_rejected:why.append("actual_byte_substitution_not_rejected")
 if not fi_misclassification_rejected:why.append("fi_misclassification_not_rejected")
 out={"schema":"W2-ENG-TECHNICAL-S6-REMEDIATION-INDEPENDENT-VERIFY-v1","generation_id":gid,"candidate_identity_ok":"candidate_identity" not in why,"normal_attempts":{"N1":n1,"N2":n2},"failure_injection":fi,"actual_byte_substitution_rejected":actual_byte_substitution_rejected,"fi_misclassification_rejected":fi_misclassification_rejected,"recomputed_adaptation":av,"recomputed_aggregate":agg,"all_remediation_invariants_verified":not why,"reasons":sorted(set(why))}
 pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print(json.dumps({"all_verified":out["all_remediation_invariants_verified"],"generation":gid,"reasons":out["reasons"]},sort_keys=True));return 0 if out["all_remediation_invariants_verified"] else 1
if __name__=="__main__":raise SystemExit(main())
