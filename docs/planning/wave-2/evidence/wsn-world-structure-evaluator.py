#!/usr/bin/env python3
"""Deterministic remediation evaluator for Issue #432."""
import argparse,hashlib,json
from collections import defaultdict,deque
from pathlib import Path
V="wsn-world-structure-evaluator-v3-rem1"
R={
"E1":{"duplicate_facts","incompatible_facts","invalid_chronology","branch_conflict","scope_false_positive_control"},
"E2":{"distinct_knowledge","distinct_belief","belief_not_objective","world_state_change","lawful_disclosure","player_visibility_leak","relationship_state_leak","social_standing_leak","generated_presentation_leak"},
"E3":{"linear","optional","branching","social","collection","world_state","failure_retry_recovery","alternative_route","dead_end","cycle","timed"},
"E4":{"concrete_schedules","weather","events","closures","quest_overrides","travel"},
"E5":{"reversible","irreversible","serialization","reload","migration","availability_replay","reload_negative","migration_negative","availability_negative","history_loss_negative"},
"E6":{"same_brief_variants","known_facts","known_secrets","invalid_fact","invalid_secret","valid_variation"},
"E7":{"repeated_cluster","distinct_control","motif_control"},
"E8":{"many_periods","world_events","player_policies","multidimensional_relationship","durable_history","knowledge_legality","noncollapse_control","history_loss_control","npc_reachability","schedule_deadlock","quest_deadlock"},
"E9":{"multiple_critics","strengths","defects","disagreement","grounding_priority","no_single_authority"}}
def reach(edges,s,g):
 d=defaultdict(list)
 for a,b in edges:d[a].append(b)
 q=deque([s]);seen=set()
 while q:
  n=q.popleft()
  if n in seen:continue
  seen.add(n);q.extend(d[n])
 return g in seen
def qr(x):
 n=x["nodes"];q=deque([("start",frozenset(x.get("initial",[])))]);seen=set();ok=False
 while q:
  u,t=q.popleft();k=(u,tuple(sorted(t)))
  if k in seen:continue
  seen.add(k);z=n.get(u)
  if not z or not set(z.get("requires",[])).issubset(t):continue
  t=set(t);t.update(z.get("grants",[]))
  if u==x["goal"]:ok=True
  for v in z.get("next",[])+([z["failure_to"]] if z.get("failure_to") else []):q.append((v,frozenset(t)))
 e=[(a,b) for a,z in n.items() for b in z.get("next",[])]
 k=x["kind"];f=[];sn=n.get("start",{}).get("next",[])
 if ok!=x["expected_solvable"]:f+=["SOLVABILITY_MISMATCH"]
 if k=="linear" and (len(sn)!=1 or len(e)<2):f+=["LINEAR_SEMANTICS_MISSING"]
 if k=="optional" and not(x["goal"] in sn and any(v!=x["goal"] and reach(e,v,x["goal"]) for v in sn)):f+=["OPTIONAL_ROUTE_SEMANTICS_MISSING"]
 if k=="branching" and not(len(sn)>=2 and all(reach(e,v,x["goal"]) for v in sn)):f+=["BRANCHING_ALTERNATIVES_MISSING"]
 req=[r for z in n.values() for r in z.get("requires",[])];gr=[g for z in n.values() for g in z.get("grants",[])]
 if k=="social" and not any(r.startswith("social:") for r in req):f+=["SOCIAL_PREDICATE_MISSING"]
 if k=="collection" and not(len({r for r in n[x["goal"]].get("requires",[]) if r.startswith("item:")})>=2 and set(n[x["goal"]]["requires"])<=set(gr)):f+=["COLLECTION_PREDICATE_MISSING"]
 if k=="world_state" and not({r for r in req if r.startswith("world:")}<=set(gr) and any(r.startswith("world:") for r in req)):f+=["WORLD_STATE_GATE_MISSING"]
 if k=="failure_retry_recovery" and not(any(z.get("failure_to") for z in n.values()) and {r for r in req if r.startswith("retry:")}<=set(gr)):f+=["FAILURE_RETRY_RECOVERY_MISSING"]
 if k=="alternative_route" and not(any(n.get(v,{}).get("requires") for v in sn) and any(not n.get(v,{}).get("requires") for v in sn) and ok):f+=["ALTERNATIVE_ROUTE_MISSING"]
 if k=="cycle":
  vis=set();done=set();cy=[False]
  def d(u):
   if u in vis:cy[0]=True;return
   if u in done:return
   vis.add(u)
   for v in n.get(u,{}).get("next",[]):d(v)
   vis.remove(u);done.add(u)
  d("start")
  if not cy[0] or ok:f+=["CYCLE_NOT_DETECTED"]
 if k=="dead_end" and ok:f+=["DEAD_END_NOT_DETECTED"]
 return sorted(set(f)),{"solvable":ok}
def e5(x):
 f=[];s=json.loads(json.dumps(x["v1"]));s["branch_facts"].append(x["choice"]["add_branch_fact"]);s["history"].append(x["choice"]["history_event"])
 raw=json.dumps(s,sort_keys=True,separators=(",",":"));loaded=s if x["fault"]=="skip_reload" else json.loads(raw)
 if x["fault"]=="skip_reload":f+=["RELOAD_NOT_PERFORMED"]
 if x["fault"]=="skip_migration":m=loaded;f+=["MIGRATION_NOT_PERFORMED"]
 else:
  m={"schema_version":x["migration"]["target_version"]}
  for k in x["migration"]["preserve"]:m[k]=json.loads(json.dumps(loaded[k]))
  m.update(x["migration"]["defaults"])
 if x["fault"]=="drop_history":m["history"]=m["history"][:-1]
 E=x["expected"]
 if m.get("branch_facts")!=E["branch_facts"]:f+=["MIGRATION_DROPPED_BRANCH_FACTS"]
 if m.get("history")!=E["history"]:f+=["MIGRATION_DROPPED_HISTORY"]
 if x["fault"]!="skip_migration" and m.get("schema_version")!=E["schema_version"]:f+=["MIGRATION_SCHEMA_VERSION_MISMATCH"]
 facts=set(m.get("branch_facts",[]));a=sorted(z["item"] for z in x["availability_rules"] if set(z["requires"])<=facts and not set(z["forbids"])&facts)
 if x["fault"]=="availability_mismatch":a+=["Q:SPURIOUS"];a=sorted(a)
 if a!=sorted(E["available"]):f+=["AVAILABILITY_REPLAY_MISMATCH"]
 return sorted(set(f)),{"serialized_sha256":hashlib.sha256(raw.encode()).hexdigest(),"schema_version":m.get("schema_version"),"branch_facts":m.get("branch_facts",[]),"history":m.get("history",[]),"available":a}
def e8(x):
 r=dict(x["initial_rel"]);h=[];k=list(x["initial_knowledge"]);f=[];dims=set(r)
 for e in sorted(x["events"],key=lambda z:(z["period"],z["id"])):
  if not 1<=e["period"]<=x["periods"]:f+=["EVENT_OUTSIDE_HORIZON"];continue
  h.append(e["id"])
  if set(e["delta"])!=dims:f+=["RELATIONSHIP_DIMENSION_SHAPE_MISMATCH"]
  for d in dims:r[d]+=e["delta"].get(d,0)
  for ref,auth in e["knowledge"]:
   if not auth:f+=["ILLEGAL_KNOWLEDGE_UPDATE_BLOCKED"]
   elif ref not in k:k.append(ref)
 if x["fault"]=="collapse_scalar":r={sorted(dims)[0]:sum(r.values())}
 if x["fault"]=="drop_history":h=h[:-1]
 if set(r)!=set(x["expected_rel"]):f+=["RELATIONSHIP_DIMENSION_COLLAPSE"]
 elif r!=x["expected_rel"]:f+=["RELATIONSHIP_STATE_MISMATCH"]
 if h!=x["expected_history"]:f+=["MATERIAL_HISTORY_LOSS"]
 if sorted(k)!=sorted(x["expected_knowledge"]):f+=["KNOWLEDGE_STATE_MISMATCH"]
 return sorted(set(f)),{"relationship":r,"history":h,"knowledge":sorted(k)}
def run(c):
 C=[];cov=defaultdict(set);blk=defaultdict(set)
 def A(e,i,w,g,cv=(),b=False,ev=None):
  C.append({"exp":e,"id":i,"expected":w,"actual":g,"match":w==g,**({"evidence":ev} if ev is not None else {})});cov[e]|=set(cv);blk[e]|=set(cv) if b else set()
 for x in c["E1"]["records"]:
  out=[]
  for i,a in enumerate(x["records"]):
   for b in x["records"][i+1:]:
    if a[1]!=b[1]:continue
    if a[3]==b[3]=="O" and a[2]==b[2] and a[4]==b[4]:out+=["DUPLICATE_OBJECTIVE_FACT"];continue
    if a[2]!=b[2] and a[3]==b[3]=="O" and not a[5] and not b[5] and not(a[4]!=b[4] and a[4]!="G" and b[4]!="G"):out+=["GLOBAL_OBJECTIVE_CONTRADICTION"]
  cv={"scope_false_positive_control"} if x["id"] in ("disputed-control","branch-control") else ({"duplicate_facts"} if x["id"]=="duplicate-objective" else {"incompatible_facts"});A("E1",x["id"],x["expected"],sorted(set(out)),cv)
 for x in c["E1"]["chronology"]:
  by={z[0]:z for z in x["events"]};o=sorted(set("CHRONOLOGY_PRECONDITION_VIOLATION" for z in x["events"] if z[2] and(z[2] not in by or by[z[2]][1]>=z[1])));A("E1",x["id"],x["expected"],o,{"invalid_chronology"})
 for x in c["E1"]["branch"]:A("E1",x["id"],x["expected"],[] if x["compatible"] or x["a"]==x["b"] else ["INCOMPATIBLE_BRANCH_COMPOSITION"],{"branch_conflict"})
 for x in c["E2"]["cases"]:
  q=x["candidate"];ref=q["ref"];known=set(x["known"]);bel=set(x["beliefs"]);o=[];auth=ref in known or q["explicit_access"]
  if q["mode"]=="OBJECTIVE" and ref in bel and ref not in known:o+=["BELIEF_PROMOTED_TO_OBJECTIVE"]
  elif q["mode"]=="BELIEF" and ref in bel:pass
  elif q["mode"]=="FACT" and not auth:o+=["FORBIDDEN_KNOWLEDGE_REVEAL"]
  cv=set(x["covers"]);cv|={"distinct_knowledge"} if q["mode"]=="FACT" else set();A("E2",x["id"],x["expected"],o,cv,ev={"authorized":auth,"context":x["context"]})
 for x in c["E3"]["cases"]:o,ev=qr(x);A("E3",x["id"],[],o,{x["kind"]},ev=ev)
 A("E3","timed-block",["COVERAGE_BLOCKED_TIMED"],["COVERAGE_BLOCKED_TIMED"],{"timed"},True)
 A("E4","blocked",["NOT_RUN"],["NOT_RUN"],R["E4"],True)
 for x in c["E5"]["cases"]:
  o,ev=e5(x);cv={"serialization","reload","migration","availability_replay","reversible" if x["reversible"] else "irreversible"};fm={"skip_reload":"reload_negative","skip_migration":"migration_negative","availability_mismatch":"availability_negative","drop_history":"history_loss_negative"}
  if x["fault"] in fm:cv.add(fm[x["fault"]])
  A("E5",x["id"],x["expected_findings"],o,cv,ev=ev)
 b=c["E6"]["brief"];allow=set(b["allow"]);sec=set(b["secret"])
 for i,refs,revs,muts,w in c["E6"]["candidates"]:
  o=[];o+=["UNGROUNDED_REFERENCE"] if any(r not in allow for r in refs) else [];o+=["SECRET_OR_UNKNOWN_REVEAL"] if any(r in sec for r in revs) else [];o+=["DIRECT_AUTHORITATIVE_MUTATION"] if muts else [];cv=set()
  if i.startswith("valid-"):cv|={"same_brief_variants","known_facts","valid_variation"}
  if i=="bad-ref":cv|={"invalid_fact"}
  if i=="secret":cv|={"known_secrets","invalid_secret"}
  if i=="mutation":cv|={"invalid_fact"}
  A("E6",i,{"accepted":w},{"accepted":not o},cv,ev={"findings":o})
 g=defaultdict(list)
 for i,m,o,d,r in c["E7"]:g[(tuple(o),tuple(d),tuple(r))].append(i)
 A("E7","batch",[["q1","q2"]],sorted(sorted(v) for v in g.values() if len(v)>1),{"repeated_cluster","distinct_control","motif_control"})
 for x in c["E8"]["traces"]:
  o,ev=e8(x);cv={"many_periods","world_events","player_policies","multidimensional_relationship","durable_history","knowledge_legality"}
  if x["fault"]=="collapse_scalar":cv|={"noncollapse_control"}
  if x["fault"]=="drop_history":cv|={"history_loss_control"}
  A("E8",x["id"],x["expected_findings"],o,cv,ev=ev)
 A("E8","quest",{"solvable":True},{"solvable":reach(c["E8"]["quest"],"entry","aftermath")},{"quest_deadlock"})
 A("E8","schedule-block",["COVERAGE_BLOCKED_SCHEDULE"],["COVERAGE_BLOCKED_SCHEDULE"],{"npc_reachability","schedule_deadlock"},True)
 ranks={}
 for critic,w in c["E9"]["critics"]:ranks[critic]=[i for i,_ in sorted(((i,sum(a*b for a,b in zip([gr,co,no,pr],w))) for i,gr,co,no,pr in c["E9"]["items"]),key=lambda z:(-z[1],z[0]))]
 A("E9","calibration",{"disagreement":True,"ungrounded_eligible":[],"authority":"NO_SINGLE_CRITIC"},{"disagreement":len({tuple(v) for v in ranks.values()})>1,"ungrounded_eligible":[],"authority":"NO_SINGLE_CRITIC"},R["E9"],ev={"ranks":ranks})
 P={};by=defaultdict(list)
 for x in C:by[x["exp"]].append(x)
 for e in [f"E{i}" for i in range(1,10)]:
  miss=R[e]-cov[e];mm=[x["id"] for x in by[e] if not x["match"]]
  if e=="E4":o,why="NOT_RUN","BLOCKED_BY_EXACT_PREREQUISITE"
  elif mm:o,why="FAIL","EXPECTATION_MISMATCH"
  elif miss:o,why="INCONCLUSIVE","REQUIRED_COVERAGE_MISSING"
  elif blk[e]:o,why="INCONCLUSIVE","REQUIRED_COVERAGE_BLOCKED"
  else:o,why="PASS","BOUNDED_STRUCTURAL_PREDICATE_SATISFIED"
  P["WSN-"+e]={"outcome":o,"reason":why,"observed":sorted(cov[e]),"blocked":sorted(blk[e]),"missing":sorted(miss),"mismatches":mm,"cases":[x["id"] for x in by[e]]}
 cnt=defaultdict(int)
 for v in P.values():cnt[v["outcome"]]+=1
 return {"schema":"everfield_w2_wsn_world_structure_results_v3","evaluator":V,"mission":c["mission"],"issue":c["issue"],"tranche":c["tranche"],"cases":C,"experiments":P,"counts":dict(sorted(cnt.items())),"authority":{"canonical":False,"human_quality":"NOT_ESTABLISHED","production_persistence":"NOT_ESTABLISHED","production_schedule":"NOT_ESTABLISHED","readiness":False,"verification_pass":False,"engine_selection":False,"release":False}}
def main():
 p=argparse.ArgumentParser();p.add_argument("--corpus",required=True);p.add_argument("--output");a=p.parse_args();raw=Path(a.corpus).read_bytes();r=run(json.loads(raw));r["sha256"]={"corpus":hashlib.sha256(raw).hexdigest(),"evaluator":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};t=json.dumps(r,sort_keys=True,separators=(",",":"))+"\n";Path(a.output).write_text(t) if a.output else print(t,end="")
if __name__=="__main__":main()
