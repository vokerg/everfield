#!/usr/bin/env python3
'''Independent retained-packet verifier for W2-ENG-TECH-S6-01.'''
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, pathlib
from typing import Any
MARKER="CAPTURE-STATE-042";WIDTH=1280;HEIGHT=720
SCREENS=["BOOT_OR_MAIN","PLAY_SURFACE","SETTINGS"];ROUTES=["BOOT_OR_MAIN->PLAY_SURFACE","PLAY_SURFACE->SETTINGS","SETTINGS->PLAY_SURFACE"]
def canon(o:Any)->str:return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def dig(o:Any)->str:return "sha256:"+hashlib.sha256(canon(o).encode()).hexdigest()
def load(p:pathlib.Path):
 s=importlib.util.spec_from_file_location("s6v",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def reset_ok(p):return isinstance(p,dict) and p.get("pre_workspace_absent") is True and p.get("workspace_created_exclusive") is True and bool(p.get("workspace_id")) and bool(p.get("reset_id"))
def state_ok(s,c,g):return s.get("marker")==MARKER and s.get("screens")==SCREENS and s.get("routes")==ROUTES and s.get("viewport")=="1280x720" and s.get("candidate")==c and s.get("generation_id")==g
def capture_ok(x,inj):
 if inj:return x.get("mechanism")=="CANDIDATE_BOUND_X11_FRAMEBUFFER" and x.get("expected_unavailable") is True and x.get("exit")==97 and x.get("frame_count")==0 and x.get("path_exists") is False
 sm=x.get("samples");return x.get("mechanism")=="CANDIDATE_BOUND_X11_FRAMEBUFFER" and x.get("expected_unavailable") is False and x.get("exit")==0 and x.get("frame_count")==1 and x.get("path_exists") is True and x.get("dimensions")==[WIDTH,HEIGHT] and isinstance(sm,list) and len(sm)==3 and len(set(sm))>=3 and all(sm)
def check_raw(w,c,g,run):
 r=w["record"];s=r["source"];st=s["state_observation"];cap=s["capture"];inj=r["mode"]=="INJECT";why=[]
 if w.get("digest")!=dig(r):why.append("raw_digest")
 if r.get("candidate")!=c or r.get("candidate_generation_id")!=g:why.append("candidate_generation")
 if s.get("run_identity")!=run:why.append("run_identity")
 if not reset_ok(r.get("reset_proof",{})):why.append("reset")
 if s.get("candidate_process_alive_at_capture") is not True:why.append("process_not_alive")
 if not state_ok(st,c,g):why.append("state")
 if not capture_ok(cap,inj):why.append("capture")
 sep=s.get("failure_separation",{}).get("classification");exp="STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE" if inj else "STATE_AND_CAPTURE_OK"
 if sep!=exp:why.append("separation")
 b=s.get("capture_binding",{});body=b.get("body")
 if not isinstance(body,dict) or b.get("digest")!=dig(body):why.append("capture_binding_digest")
 else:
  expected={"candidate":c,"generation_id":g,"attempt":r["label"],"run_identity":run,"project_digest":s["project_identity"]["digest"],"executable_sha256":s["preparation"].get("executable_sha256"),
            "state_digest":dig(st),"capture_sha256":cap.get("sha256"),"viewport":cap.get("dimensions"),"frame_count":cap.get("frame_count"),"mechanism":cap.get("mechanism"),"classification":sep}
  if body!=expected:why.append("capture_binding_body")
 if r.get("formal_result")!="PASS" or r.get("failure_class")!="NONE":why.append("formal")
 return {"ok":not why,"reasons":sorted(set(why))}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--evidence",required=True);ap.add_argument("--validator",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 d=json.load(open(a.evidence));v=load(pathlib.Path(a.validator));run=d["run_identity"];cv={};attacks={}
 for c in d["provisional_candidates"]:
  p=d["results"][c];g=p["generation"];gid=g["generation_id"];reasons=[];raws=p["raw_attempts"];checks=[check_raw(x,c,gid,run) for x in raws]
  if not all(x["ok"] for x in checks):reasons.append("raw_semantics")
  ps=[x["record"]["reset_proof"] for x in raws]
  if len({x["workspace_id"] for x in ps})!=3 or len({x["reset_id"] for x in ps})!=3:reasons.append("reset_reuse")
  refs=g["run_registry_refs"]
  if len(refs)!=3 or len(set(refs))!=3 or set(refs)!=set(p["source_bindings"]):reasons.append("registry")
  for ref,w in zip(refs,raws):
   if p["source_bindings"].get(ref)!=w["digest"]:reasons.append("source_binding")
   a0=g["attempts"][ref];r=w["record"];rp=r["reset_proof"]
   if a0.get("candidate_id")!=c or a0.get("candidate_generation_id")!=gid or a0.get("result")!=r["formal_result"] or a0.get("failure_class")!=r["failure_class"]:reasons.append("formal_binding")
   if a0.get("reset_id")!=rp["reset_id"] or a0.get("workspace_id")!=rp["workspace_id"] or a0.get("reset_verified")!=r["reset_verified_derived"]:reasons.append("reset_binding")
  agg=v.agg(g)
  if agg!={"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":True}:reasons.append("aggregate")
  if v.va(g["adaptation"],c).get("result")!="ACCEPT":reasons.append("adaptation")
  cv[c]={"ok":not reasons,"reasons":sorted(set(reasons)),"raw_checks":checks,"recomputed_aggregate":agg}
  q=copy.deepcopy(raws[0]);q["record"]["source"]["state_observation"]["marker"]="BAD";att1=not check_raw(q,c,gid,run)["ok"]
  q=copy.deepcopy(raws[0]);q["record"]["source"]["capture"]["dimensions"]=[640,360];att2=not check_raw(q,c,gid,run)["ok"]
  q=copy.deepcopy(raws[2]);q["record"]["source"]["failure_separation"]["classification"]="STATE_REACHABILITY";att3=not check_raw(q,c,gid,run)["ok"]
  gg=copy.deepcopy(g);gg["run_registry_refs"].append(gg["run_registry_refs"][0]);att4=v.agg(gg)["aggregate"]!="PASS_FOR_COMPARISON"
  attacks[c]={"wrong_marker":att1,"wrong_viewport":att2,"fi_misclassification":att3,"duplicate_registry":att4}
 out={"schema":"W2-ENG-TECHNICAL-S6-INDEPENDENT-VERIFY-v1","evidence_run_identity":run,"provisional_candidates":d["provisional_candidates"],"candidate_verification":cv,"negative_attacks":attacks,
      "all_provisional_verified":all(x["ok"] for x in cv.values()) and all(all(y.values()) for y in attacks.values())}
 pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print(json.dumps(out,sort_keys=True));return 0 if out["all_provisional_verified"] else 1
if __name__=="__main__":raise SystemExit(main())
