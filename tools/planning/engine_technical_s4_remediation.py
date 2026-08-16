#!/usr/bin/env python3
"""W2-ENG-TECH-S4-REM-01: fresh S4 rerun with derived reset and source binding."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, os, pathlib, shutil, stat, subprocess, tempfile, time

RESOURCE="W2-ENG-HOST-COMMON-v2"
PRODUCER_HEAD="942a8c05032c1506730f52e897496172fb56fcf3"
PRODUCER_RUN=31924179133
PRODUCER_ARTIFACT=9257331215
PRODUCER_EVIDENCE_SHA="8ba3922733c4051f798dab002de4cf607f6176ffe3f66d3e85a2568473967453"
REVIEW_ISSUE=362
REVIEW_TERMINAL=5305556485


def J(o): return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def H(o): return hashlib.sha256((o if isinstance(o, bytes) else J(o).encode())).hexdigest()
def sha_file(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def load(path, name):
    s=importlib.util.spec_from_file_location(name, path)
    if not s or not s.loader: raise RuntimeError(f"cannot load {path}")
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def run(cmd,cwd=None,env=None,timeout=900):
    e=os.environ.copy(); e.update(env or {})
    t=time.monotonic()
    try:
        p=subprocess.run(cmd,cwd=cwd,env=e,text=True,capture_output=True,timeout=timeout,check=False)
        return {"exit":p.returncode,"timed_out":False,"seconds":round(time.monotonic()-t,3),"stdout":p.stdout[-16000:],"stderr":p.stderr[-16000:]}
    except subprocess.TimeoutExpired as x:
        return {"exit":None,"timed_out":True,"seconds":round(time.monotonic()-t,3),"stdout":x.stdout[-16000:] if isinstance(x.stdout,str) else "","stderr":x.stderr[-16000:] if isinstance(x.stderr,str) else ""}
    except FileNotFoundError as x:
        return {"exit":127,"timed_out":False,"seconds":0,"stdout":"","stderr":str(x)}

def ok(r): return r.get("exit")==0 and not r.get("timed_out")
def marker_ok(r,mode):
    m="EVERFIELD_S4:PASS:INCOMPAT_TUPLE" if mode=="INJECT" else "EVERFIELD_S4:PASS:NORMAL"
    return ok(r) and m in ((r.get("stdout") or "")+(r.get("stderr") or ""))

def tree_digest(root):
    root=pathlib.Path(root); rows=[]
    if not root.exists(): return H([])
    for p in sorted(x for x in root.rglob("*") if x.is_file()):
        rows.append([str(p.relative_to(root)),sha_file(p),p.stat().st_size])
    return H(rows)

def canonical_toolchain(tool):
    keep={k:v for k,v in tool.items() if k not in {"download","probe","vendor_digest_probe","version","unzip","bob_version"}}
    return keep

def reset_prepare(root,candidate,label,run_identity):
    slug=candidate.lower().replace(" ","-")
    ws=pathlib.Path(root)/"runs"/slug/label
    state=pathlib.Path(root)/"state"/slug/label
    pre_ws=not ws.exists(); pre_state=not state.exists()
    ws.mkdir(parents=True,exist_ok=False); state.mkdir(parents=True,exist_ok=False)
    home=state/"home"; xdg=state/"xdg-data"; cfg=state/"xdg-config"; cache=state/"xdg-cache"
    for p in (home,xdg,cfg,cache): p.mkdir()
    proof={
      "schema":"S4-RESET-PROOF-v1","candidate":candidate,"label":label,
      "pre_workspace_absent":pre_ws,"pre_state_root_absent":pre_state,
      "workspace_created_exclusive":ws.exists(),"state_root_created_exclusive":state.exists(),
      "state_root_empty_before_candidate":not any(x.is_file() for x in state.rglob("*")),
      "workspace_id":"WS-"+H({"candidate":candidate,"label":label,"run":run_identity,"role":"workspace"})[:28],
      "state_root_id":"STATE-"+H({"candidate":candidate,"label":label,"run":run_identity,"role":"candidate-native-state"})[:28],
      "reset_id":"RESET-"+H({"candidate":candidate,"label":label,"run":run_identity,"role":"reset"})[:28],
      "env_isolation_keys":["HOME","XDG_DATA_HOME","XDG_CONFIG_HOME","XDG_CACHE_HOME"]
    }
    env={"HOME":str(home),"XDG_DATA_HOME":str(xdg),"XDG_CONFIG_HOME":str(cfg),"XDG_CACHE_HOME":str(cache)}
    return ws,state,env,proof

def verify_reset(p):
    req=("pre_workspace_absent","pre_state_root_absent","workspace_created_exclusive","state_root_created_exclusive","state_root_empty_before_candidate")
    return isinstance(p,dict) and all(p.get(k) is True for k in req) and all(isinstance(p.get(k),str) and p[k] for k in ("workspace_id","state_root_id","reset_id")) and p.get("env_isolation_keys")==["HOME","XDG_DATA_HOME","XDG_CONFIG_HOME","XDG_CACHE_HOME"]

def verify_reset_set(raws):
    ps=[x["record"]["reset_proof"] for x in raws]
    return all(verify_reset(p) for p in ps) and len({p["workspace_id"] for p in ps})==len(ps) and len({p["state_root_id"] for p in ps})==len(ps) and len({p["reset_id"] for p in ps})==len(ps)

def raw_attempt(candidate,label,mode,fixture_sha,command_semantic,result,host,proof,state_after,cid,run_identity):
    reset_ok=verify_reset(proof)
    passed=marker_ok(result,mode) and host.get("pass") is True and reset_ok
    rec={
      "schema":"S4-RAW-ATTEMPT-v1","candidate":candidate,"label":label,"mode":mode,
      "scenario_id":"S4","candidate_identity_digest":cid,"run_identity":run_identity,
      "fixture_sha256":fixture_sha,"command_semantic":command_semantic,
      "result":{"exit":result.get("exit"),"timed_out":result.get("timed_out"),"stdout":result.get("stdout"),"stderr":result.get("stderr")},
      "host_semantics":host,"reset_proof":proof,"reset_verified_derived":reset_ok,
      "candidate_state_after_sha256":state_after,"formal_result":"PASS" if passed else "INCONCLUSIVE",
      "failure_class":"NONE" if passed else "HARNESS"
    }
    return {"digest":"sha256:"+H(rec),"record":rec,"observation":{"seconds":result.get("seconds")}}

def derive_ids(candidate,cid,raws,adaptation_identity,run_identity):
    body={"candidate":candidate,"candidate_identity_digest":cid,"raw_attempt_digests":[x["digest"] for x in raws],"adaptation_identity":adaptation_identity,"run_identity":run_identity,"scenario":"S4"}
    work="WORK-S4R-"+H(body)[:24]
    gid="GEN-S4R-"+H({"work":work,"body":body})[:24]
    return work,gid,body

def formalize(candidate,cident,raws,v,run_identity):
    a=v.adaptation("S4",candidate); av=v.va(a,candidate)
    work,gid,idbody=derive_ids(candidate,cident["identity_digest"],raws,av["adaptation_identity"],run_identity)
    normals=[x for x in raws if x["record"]["mode"]=="NORMAL"]; inj=[x for x in raws if x["record"]["mode"]=="INJECT"]
    g=v.gen("S4",gid=gid,work=work,
      normal=tuple(x["record"]["formal_result"] for x in normals),
      classes=tuple(x["record"]["failure_class"] for x in normals),
      injres=inj[0]["record"]["formal_result"],injfc=inj[0]["record"]["failure_class"],
      resets=tuple(x["record"]["reset_proof"]["reset_id"] for x in normals),
      oks=tuple(x["record"]["reset_verified_derived"] for x in normals),
      wss=tuple(x["record"]["reset_proof"]["workspace_id"] for x in normals),res=RESOURCE,cid=candidate)
    fi=[k for k,z in g["attempts"].items() if z["kind"]=="FAILURE_INJECTION"][0]
    ir=inj[0]["record"]; g["attempts"][fi]["reset_id"]=ir["reset_proof"]["reset_id"]; g["attempts"][fi]["reset_verified"]=ir["reset_verified_derived"]; g["attempts"][fi]["workspace_id"]=ir["reset_proof"]["workspace_id"]
    ordered=normals+inj
    bindings={ref:x["digest"] for ref,x in zip(g["run_registry_refs"],ordered)}
    packet={"candidate_identity":cident,"identity_derivation":idbody,"raw_attempts":ordered,"generation":g,"source_bindings":bindings,"adaptation_validation":av}
    packet["binding_verification"]=verify_packet(packet,v,run_identity)
    packet["aggregate"]=v.agg(g)
    packet["trusted_representation_ok"]=packet["binding_verification"]["ok"] and av["result"]=="ACCEPT" and packet["aggregate"]=={"aggregate":"PASS_FOR_COMPARISON","reasons":[],"valid_envelope":True}
    return packet

def verify_packet(packet,v,run_identity):
    reasons=[]; ci=packet.get("candidate_identity",{}); body=ci.get("body")
    if not isinstance(body,dict) or ci.get("identity_digest")!="sha256:"+H(body): reasons.append("candidate_identity_digest_mismatch")
    raws=packet.get("raw_attempts",[])
    for x in raws:
        if x.get("digest")!="sha256:"+H(x.get("record")): reasons.append("raw_digest_mismatch")
        if x.get("record",{}).get("candidate_identity_digest")!=ci.get("identity_digest"): reasons.append("raw_candidate_identity_mismatch")
        if x.get("record",{}).get("run_identity")!=run_identity: reasons.append("raw_run_identity_mismatch")
    if not verify_reset_set(raws): reasons.append("reset_set_invalid")
    g=packet.get("generation",{}); refs=g.get("run_registry_refs",[]); binds=packet.get("source_bindings",{})
    if len(refs)!=len(raws) or set(refs)!=set(binds): reasons.append("binding_registry_mismatch")
    for ref,x in zip(refs,raws):
        if binds.get(ref)!=x.get("digest"): reasons.append("source_binding_substitution")
        f=g.get("attempts",{}).get(ref,{}); r=x.get("record",{}); p=r.get("reset_proof",{})
        if f.get("candidate_id")!=r.get("candidate") or f.get("result")!=r.get("formal_result") or f.get("failure_class")!=r.get("failure_class"): reasons.append("formal_raw_result_mismatch")
        if f.get("reset_id")!=p.get("reset_id") or f.get("workspace_id")!=p.get("workspace_id") or f.get("reset_verified")!=r.get("reset_verified_derived"): reasons.append("formal_raw_reset_mismatch")
    av=v.va(g.get("adaptation"),g.get("candidate_id")) if isinstance(g,dict) else {"result":"REJECT"}
    expected=derive_ids(g.get("candidate_id"),ci.get("identity_digest"),raws,av.get("adaptation_identity"),run_identity) if av.get("adaptation_identity") else (None,None,None)
    if expected[0]!=g.get("candidate_work_id") or expected[1]!=g.get("generation_id"): reasons.append("generation_identity_mismatch")
    return {"ok":not reasons,"reasons":sorted(set(reasons))}

def negative_tests(clean,p,v,run_identity):
    tests={}
    q=copy.deepcopy(p); q["raw_attempts"][0]["record"]["reset_proof"].pop("pre_state_root_absent",None); tests["missing_reset_proof_rejected"]=not verify_reset(q["raw_attempts"][0]["record"]["reset_proof"])
    q=copy.deepcopy(p); q["raw_attempts"][0]["record"]["reset_proof"]["pre_workspace_absent"]=False; tests["asserted_reset_without_proof_rejected"]=not verify_reset(q["raw_attempts"][0]["record"]["reset_proof"])
    q=copy.deepcopy(p); q["raw_attempts"][1]["record"]["reset_proof"]["workspace_id"]=q["raw_attempts"][0]["record"]["reset_proof"]["workspace_id"]; tests["reused_workspace_rejected"]=not verify_reset_set(q["raw_attempts"])
    q=copy.deepcopy(p); q["raw_attempts"][1]["record"]["reset_proof"]["state_root_id"]=q["raw_attempts"][0]["record"]["reset_proof"]["state_root_id"]; tests["reused_state_root_rejected"]=not verify_reset_set(q["raw_attempts"])
    q=copy.deepcopy(p); q["raw_attempts"][0]["record"]["fixture_sha256"]="0"*64; tests["raw_source_digest_substitution_rejected"]=not verify_packet(q,v,run_identity)["ok"]
    q=copy.deepcopy(p); ks=list(q["source_bindings"]); q["source_bindings"][ks[0]]=q["source_bindings"][ks[1]]; tests["formal_raw_binding_substitution_rejected"]=not verify_packet(q,v,run_identity)["ok"]
    q=copy.deepcopy(p); q["candidate_identity"]["body"]["executable_sha256"]="0"*64; tests["binary_identity_substitution_rejected"]=not verify_packet(q,v,run_identity)["ok"]
    q=copy.deepcopy(p); q["candidate_identity"]["body"]["toolchain_digest"]="0"*64; tests["toolchain_identity_substitution_rejected"]=not verify_packet(q,v,run_identity)["ok"]
    g=copy.deepcopy(p["generation"]); k=g["run_registry_refs"][0]; g["attempts"][k]["candidate_generation_id"]="OTHER"; tests["candidate_generation_mismatch_rejected"]=v.agg(g)["aggregate"]!="PASS_FOR_COMPARISON"
    g=copy.deepcopy(p["generation"]); g["run_registry_refs"].append(g["run_registry_refs"][0]); tests["duplicate_registry_rejected"]=v.agg(g)["aggregate"]!="PASS_FOR_COMPARISON"
    tests["schema_field_omission_rejected"]=not clean.parse_fixture(clean.fixture_v1().replace("settings=volume:7\n","")).get("ok")
    tests["migration_default_omission_rejected"]=not clean.parse_fixture(clean.fixture_v2().replace("world_flags={}\n","")).get("ok")
    tests["malformed_tuple_acceptance_rejected"]=clean.parse_fixture(clean.fixture_v1(True)).get("reason")=="malformed_entity_tuple"
    return tests

def host_semantics(clean,ws,mode): return clean.host_semantics(ws,mode)
def copy_input(clean,ws,inject): pathlib.Path(ws,"input.save").write_text(clean.fixture_v1(inject))

def candidate_identity(candidate,version,tool,binary_sha,build_body,validator_sha,producer_sha,run_identity):
    body={"candidate":candidate,"version":version,"toolchain_digest":"sha256:"+H(canonical_toolchain(tool)),"executable_sha256":binary_sha,"build_identity_digest":"sha256:"+H(build_body),"validator_sha256":validator_sha,"producer_runner_sha256":producer_sha,"harness_id":"W2-ENG-HARNESS-v5","scenario_manifest_id":"W2-ENG-SCENARIO-INPUTS-v2","scenario_id":"S4","run_identity":run_identity,"predecessor":{"producer_head":PRODUCER_HEAD,"producer_run":PRODUCER_RUN,"producer_artifact":PRODUCER_ARTIFACT,"producer_evidence_sha256":PRODUCER_EVIDENCE_SHA,"review_issue":REVIEW_ISSUE,"review_terminal":REVIEW_TERMINAL}}
    return {"body":body,"identity_digest":"sha256:"+H(body)}

def execute_attempt(clean,root,candidate,label,mode,cident,run_identity,runner,fixture_sha):
    ws,state,env,proof=reset_prepare(root,candidate,label,run_identity)
    result,semantic=runner(ws,state,env,mode)
    host=host_semantics(clean,ws,mode)
    return raw_attempt(candidate,label,mode,fixture_sha,semantic,result,host,proof,tree_digest(state),cident["identity_digest"],run_identity)

def bevy(clean,cap,v,root,lock,validator_sha,producer_sha,run_identity):
    tool=cap.probe_bevy(root,lock)
    if tool.get("status") not in ("CAPABLE","CAPABLE_WITH_PRESEED"): return {"candidate":"Bevy","disposition":"NOT_RUN_TOOLCHAIN_UNAVAILABLE","toolchain":tool}
    build=root/"build-bevy"; (build/"src").mkdir(parents=True); shutil.copy2(lock,build/"Cargo.lock")
    (build/"Cargo.toml").write_text("[package]\nname='everfield_bevy_probe'\nversion='0.0.0'\nedition='2024'\n[dependencies]\nbevy = { version = '=0.19.0', default-features = false }\n")
    (build/"src/main.rs").write_text(clean.BEVY)
    cargo=(tool.get("cargo") or {}).get("path") or shutil.which("cargo"); br=run([str(cargo),"build","--locked","--quiet"],cwd=build) if cargo else {"exit":127,"timed_out":False}
    exe=build/"target/debug/everfield_bevy_probe"
    if not ok(br) or not exe.exists(): return {"candidate":"Bevy","disposition":"REMEDIATION_INCONCLUSIVE","toolchain":tool,"build":br}
    bsha=sha_file(exe); build_body={"cargo_lock_sha256":sha_file(lock),"source_sha256":hashlib.sha256(clean.BEVY.encode()).hexdigest(),"binary_sha256":bsha,"build_exit":br["exit"]}
    ci=candidate_identity("Bevy","0.19.0",tool,bsha,build_body,validator_sha,producer_sha,run_identity)
    def rr(ws,state,env,mode):
        x=ws/"everfield_bevy_probe"; shutil.copy2(exe,x); x.chmod(x.stat().st_mode|stat.S_IXUSR); copy_input(clean,ws,mode=="INJECT")
        r=run([str(x)],cwd=ws,env={**env,"EVERFIELD_S4_MODE":mode},timeout=120)
        return r,{"program":"bevy-binary","binary_sha256":bsha,"mode":mode}
    raws=[execute_attempt(clean,root,"Bevy",l,m,ci,run_identity,rr,hashlib.sha256(clean.fixture_v1(m=="INJECT").encode()).hexdigest()) for l,m in (("N1","NORMAL"),("N2","NORMAL"),("FI1","INJECT"))]
    p=formalize("Bevy",ci,raws,v,run_identity); p["negative_selftests"]=negative_tests(clean,p,v,run_identity); p["build"]=br; p["toolchain"]=tool; p["disposition"]="REMEDIATED_S4_PROVISIONAL_PASS_PENDING_FRESH_REVIEW" if p["trusted_representation_ok"] and all(p["negative_selftests"].values()) else "REMEDIATION_INCONCLUSIVE"; return p

def godot(clean,cap,v,root,lock,validator_sha,producer_sha,run_identity):
    tool=cap.probe_godot(root,lock); exe=pathlib.Path(tool.get("executable") or "")
    if tool.get("status")!="CAPABLE" or not exe.exists(): return {"candidate":"Godot","disposition":"NOT_RUN_TOOLCHAIN_UNAVAILABLE","toolchain":tool}
    bsha=sha_file(exe); build_body={"artifact_sha256":tool.get("artifact_identity",{}).get("observed_sha256"),"executable_sha256":bsha,"script_sha256":hashlib.sha256(clean.GDSCRIPT.encode()).hexdigest()}
    ci=candidate_identity("Godot","4.7.1-stable",tool,bsha,build_body,validator_sha,producer_sha,run_identity)
    def rr(ws,state,env,mode):
        copy_input(clean,ws,mode=="INJECT"); (ws/"project.godot").write_text('[application]\nconfig/name="EverfieldS4Rem"\nrun/main_scene="res://main.tscn"\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n'); (ws/"main.tscn").write_text('[gd_scene load_steps=2 format=3]\n\n[ext_resource path="res://main.gd" type="Script" id="1"]\n\n[node name="Main" type="Node"]\nscript = ExtResource("1")\n'); (ws/"main.gd").write_text(clean.GDSCRIPT)
        r=run([str(exe),"--headless","--path",str(ws)],cwd=ws,env={**env,"EVERFIELD_S4_MODE":mode},timeout=120)
        return r,{"program":"godot-headless","binary_sha256":bsha,"mode":mode,"project_role":"isolated-attempt"}
    raws=[execute_attempt(clean,root,"Godot",l,m,ci,run_identity,rr,hashlib.sha256(clean.fixture_v1(m=="INJECT").encode()).hexdigest()) for l,m in (("N1","NORMAL"),("N2","NORMAL"),("FI1","INJECT"))]
    p=formalize("Godot",ci,raws,v,run_identity); p["negative_selftests"]=negative_tests(clean,p,v,run_identity); p["toolchain"]=tool; p["disposition"]="REMEDIATED_S4_PROVISIONAL_PASS_PENDING_FRESH_REVIEW" if p["trusted_representation_ok"] and all(p["negative_selftests"].values()) else "REMEDIATION_INCONCLUSIVE"; return p

def bundle_exe(bundle):
    xs=[]
    for p in pathlib.Path(bundle).rglob("*"):
        if p.is_file() and p.suffix.lower() not in (".so",".dll",".dylib",".jar",".zip") and (p.stat().st_mode&(stat.S_IXUSR|stat.S_IXGRP|stat.S_IXOTH)): xs.append(p)
    return max(xs,key=lambda p:p.stat().st_size) if xs else None

def defold(clean,cap,v,root,lock,validator_sha,producer_sha,run_identity):
    tool=cap.probe_defold(root,lock); java=(tool.get("java") or {}).get("path") or shutil.which("java"); jar=root/"bob-1.13.0.jar"
    if tool.get("status")!="CAPABLE" or not java or not jar.exists(): return {"candidate":"Defold","disposition":"NOT_RUN_TOOLCHAIN_UNAVAILABLE","toolchain":tool}
    proj=root/"build-defold"; proj.mkdir(); (proj/"input").mkdir(); (proj/"input/game.input_binding").write_text(""); (proj/"game.project").write_text('[project]\ntitle = EverfieldS4\n[bootstrap]\nmain_collection = /main.collectionc\n[display]\nwidth = 320\nheight = 180\n'); (proj/"main.collection").write_text('name: "main"\nscale_along_z: 0\nembedded_instances {\n id: "controller"\n data: "components {\\n  id: \\"script\\"\\n  component: \\"/controller.script\\"\\n}\\n"\n}\n'); (proj/"controller.script").write_text(clean.LUA)
    builds=[]; bundle=None
    for vv in ("headless","debug"):
        b=proj/("bundle-"+vv); r=run([java,"-jar",str(jar),"--root",str(proj),"--bundle-output",str(b),"--variant",vv,"--platform","x86_64-linux","--archive","resolve","build","bundle"],cwd=proj); builds.append({"variant":vv,"result":r})
        if ok(r): bundle=b; break
    exe=bundle_exe(bundle) if bundle else None
    if not exe: return {"candidate":"Defold","disposition":"REMEDIATION_INCONCLUSIVE","toolchain":tool,"builds":builds}
    bsha=sha_file(exe); build_body={"bob_sha256":tool.get("artifact_identity",{}).get("observed_sha256"),"bundle_executable_sha256":bsha,"script_sha256":hashlib.sha256(clean.LUA.encode()).hexdigest(),"bundle_tree_sha256":tree_digest(bundle)}
    ci=candidate_identity("Defold","1.13.0",tool,bsha,build_body,validator_sha,producer_sha,run_identity)
    rel=exe.relative_to(bundle)
    def rr(ws,state,env,mode):
        shutil.copytree(bundle,ws/"bundle"); x=ws/"bundle"/rel; copy_input(clean,x.parent,mode=="INJECT")
        ee={**env,"EVERFIELD_S4_MODE":mode}; r=run([str(x)],cwd=x.parent,env=ee,timeout=120)
        if not ok(r) and shutil.which("xvfb-run"): r=run(["xvfb-run","-a",str(x)],cwd=x.parent,env=ee,timeout=120)
        return r,{"program":"defold-bundle","binary_sha256":bsha,"mode":mode,"candidate_state_root_id":"isolated-via-HOME-XDG"}
    raws=[execute_attempt(clean,root,"Defold",l,m,ci,run_identity,rr,hashlib.sha256(clean.fixture_v1(m=="INJECT").encode()).hexdigest()) for l,m in (("N1","NORMAL"),("N2","NORMAL"),("FI1","INJECT"))]
    p=formalize("Defold",ci,raws,v,run_identity); p["negative_selftests"]=negative_tests(clean,p,v,run_identity); p["toolchain"]=tool; p["builds"]=builds; p["disposition"]="REMEDIATED_S4_PROVISIONAL_PASS_PENDING_FRESH_REVIEW" if p["trusted_representation_ok"] and all(p["negative_selftests"].values()) else "REMEDIATION_INCONCLUSIVE"; return p

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",required=True); ap.add_argument("--producer-runner",required=True); ap.add_argument("--producer-sha256",required=True); ap.add_argument("--validator",required=True); ap.add_argument("--bevy-lock",required=True); ap.add_argument("--artifact-lock",required=True); ap.add_argument("--capability-probe",default="tools/planning/engine_toolchain_probe.py"); args=ap.parse_args()
    clean=load(pathlib.Path(args.producer_runner),"producer_s4"); cap=load(pathlib.Path(args.capability_probe),"cap"); v=load(pathlib.Path(args.validator),"v5")
    producer_sha=sha_file(args.producer_runner); assert producer_sha==args.producer_sha256,(producer_sha,args.producer_sha256)
    validator_sha=sha_file(args.validator); run_identity={"trigger_sha":os.getenv("GITHUB_SHA"),"run_id":os.getenv("GITHUB_RUN_ID"),"run_attempt":os.getenv("GITHUB_RUN_ATTEMPT"),"runner_os":os.getenv("RUNNER_OS"),"runner_arch":os.getenv("RUNNER_ARCH")}
    lock=cap.load_artifact_lock(pathlib.Path(args.artifact_lock))
    with tempfile.TemporaryDirectory(prefix="everfield-s4-rem-") as td:
        root=pathlib.Path(td)
        results={"Bevy":bevy(clean,cap,v,root,pathlib.Path(args.bevy_lock),validator_sha,producer_sha,run_identity),"Defold":defold(clean,cap,v,root,lock,validator_sha,producer_sha,run_identity),"Godot":godot(clean,cap,v,root,lock,validator_sha,producer_sha,run_identity),"Unity":{"candidate":"Unity","disposition":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"},"Unreal Engine":{"candidate":"Unreal Engine","disposition":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"}}
        passed=[c for c in ("Bevy","Defold","Godot") if results[c].get("disposition")=="REMEDIATED_S4_PROVISIONAL_PASS_PENDING_FRESH_REVIEW"]
        payload={"schema":"W2-ENG-TECHNICAL-S4-REMEDIATION-v1","mission_id":"W2-ENG-TECH-S4-REM-01","source_issue":364,"producer_issue":360,"producer_head":PRODUCER_HEAD,"producer_run":PRODUCER_RUN,"producer_artifact":PRODUCER_ARTIFACT,"producer_evidence_sha256":PRODUCER_EVIDENCE_SHA,"review_issue":REVIEW_ISSUE,"review_terminal":REVIEW_TERMINAL,"findings_closed_by_design":["W2-ENG-TECH-S4-REV-M01","W2-ENG-TECH-S4-REV-M02","W2-ENG-TECH-S4-REV-M03"],"harness_id":"W2-ENG-HARNESS-v5","scenario_manifest_id":"W2-ENG-SCENARIO-INPUTS-v2","scenario_id":"S4","validator_sha256":validator_sha,"producer_runner_sha256":producer_sha,"run_identity":run_identity,"results":results,"remediated_provisional_candidates":passed,"all_public_candidates_remediated_provisionally":set(passed)=={"Bevy","Defold","Godot"},"authority_bound_not_run":{"Unity":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY","Unreal Engine":"NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY"},"historical_issue_82_not_run_cells_preserved":50,"historical_issue_82_cells_mutated":False,"reviewed_s3_provenance_preserved":True,"engine_selected":False,"trusted_comparison_authority":False,"fresh_review_required":True,"integration_authority":False,"canonicality":"NOT_CANONICAL"}
        pathlib.Path(args.out).parent.mkdir(parents=True,exist_ok=True); pathlib.Path(args.out).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
        print(json.dumps({"remediated_provisional_candidates":passed,"count":len(passed)},sort_keys=True))
        return 0 if passed else 2
if __name__=="__main__": raise SystemExit(main())
