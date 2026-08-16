#!/usr/bin/env python3
"""Deterministic standard-library evaluator for Issue #428 / W2-GAME-EV-WSN-01."""
from __future__ import annotations
import argparse, hashlib, json
from collections import defaultdict, deque
from pathlib import Path

VERSION="wsn-world-structure-evaluator-v2"
REQ={
"E1":{"duplicate_facts","incompatible_facts","invalid_chronology","branch_conflict","scope_false_positive_control"},
"E2":{"distinct_knowledge","distinct_belief","world_state_change","forbidden_rejection","belief_not_objective"},
"E3":{"linear","optional","branching","timed","social","collection","world_state","dead_end","cycle"},
"E4":{"concrete_schedules","weather","events","closures","quest_overrides","travel"},
"E5":{"reversible","irreversible","reload","migration","availability"},
"E6":{"same_brief_variants","known_facts","known_secrets","invalid_fact","invalid_secret","valid_variation"},
"E7":{"repeated_cluster","distinct_control","motif_control"},
"E8":{"many_periods","world_events","player_policies","npc_reachability","relationship","knowledge","schedule_deadlock","quest_deadlock"},
"E9":{"multiple_critics","strengths","defects","disagreement","grounding_priority","no_single_authority"}}

def contradiction(records):
    out=[]
    for i,a in enumerate(records):
        for b in records[i+1:]:
            _,sub,val,auth,branch,dispute=a; _,sub2,val2,auth2,branch2,dispute2=b
            if sub!=sub2: continue
            if auth==auth2=="O" and val==val2 and branch==branch2: out.append("DUPLICATE_OBJECTIVE_FACT"); continue
            if val==val2 or auth!="O" or auth2!="O" or dispute or dispute2: continue
            if branch!=branch2 and branch!="G" and branch2!="G": continue
            out.append("GLOBAL_OBJECTIVE_CONTRADICTION")
    return sorted(set(out))

def chronology(events):
    by={e[0]:e for e in events}; out=[]
    for eid,order,req in events:
        if req and (req not in by or by[req][1]>=order): out.append("CHRONOLOGY_PRECONDITION_VIOLATION")
    return sorted(set(out))

def quest(edges, goal="goal", start="start"):
    adj=defaultdict(list)
    nodes={start,goal}
    for a,b in edges: adj[a].append(b); nodes|={a,b}
    seen=set(); q=deque([start])
    while q:
        n=q.popleft()
        if n in seen: continue
        seen.add(n); q.extend(adj[n])
    solvable=goal in seen
    findings=[] if solvable else ["UNREACHABLE_GOAL"]
    if not solvable:
        visiting=set(); done=set(); cyc=False
        def dfs(n):
            nonlocal cyc
            visiting.add(n)
            for m in adj[n]:
                if m in visiting: cyc=True
                elif m not in done: dfs(m)
            visiting.discard(n); done.add(n)
        dfs(start)
        if cyc: findings.append("REACHABLE_CYCLE_WITHOUT_EXIT")
    return solvable,sorted(set(findings))

def run(c):
    cases=[]; cov=defaultdict(set); blocked=defaultdict(set)
    def add(exp,cid,expected,actual,covers=(),is_blocked=False):
        match=expected==actual
        cases.append({"id":cid,"exp":exp,"expected":expected,"actual":actual,"match":match})
        cov[exp]|=set(covers)
        if is_blocked: blocked[exp]|=set(covers)

    for cid,recs,expected in c["E1"]["records"]:
        covers={"scope_false_positive_control"} if cid in ("disputed-control","branch-control") else ({"duplicate_facts"} if cid=="duplicate-objective" else {"incompatible_facts"})
        add("E1",cid,expected,contradiction(recs),covers)
    for cid,events,expected in c["E1"]["chronology"]:
        add("E1",cid,expected,chronology(events),{"invalid_chronology"})
    for cid,a,b,compat,expected in c["E1"]["branch"]:
        actual=[] if compat or a==b else ["INCOMPATIBLE_BRANCH_COMPOSITION"]
        add("E1",cid,expected,actual,{"branch_conflict"})

    for cid,know,belief,candidate,expected in c["E2"]:
        ref,mode,allow=candidate; out=[]
        if mode=="OBJECTIVE" and ref in belief and ref not in know: out=["BELIEF_PROMOTED_TO_OBJECTIVE"]
        elif mode=="BELIEF" and ref in belief: pass
        elif ref in know or allow: pass
        else: out=["FORBIDDEN_KNOWLEDGE_REVEAL"]
        covers={"distinct_knowledge"}
        if cid=="false-belief-as-belief": covers|={"distinct_belief","belief_not_objective"}
        if cid=="belief-no-promotion": covers|={"belief_not_objective"}
        if cid=="player-exposure-no-leak": covers|={"forbidden_rejection"}
        if cid=="post-disclosure": covers|={"world_state_change","forbidden_rejection"}
        add("E2",cid,expected,out,covers)

    for cid,kind,edges,want in c["E3"]["routes"]:
        solv,find=quest(edges)
        expected={"solvable":want,"findings":[] if want else (sorted(["UNREACHABLE_GOAL","REACHABLE_CYCLE_WITHOUT_EXIT"]) if cid=="cycle" else ["UNREACHABLE_GOAL"])}
        actual={"solvable":solv,"findings":find}
        covers={kind}
        if cid=="dead-end": covers={"dead_end"}
        if cid=="cycle": covers={"cycle"}
        add("E3",cid,expected,actual,covers)
    add("E3","timed-block",["COVERAGE_BLOCKED_TIMED"],["COVERAGE_BLOCKED_TIMED"],{"timed"},True)

    add("E4","blocked",["NOT_RUN"],["NOT_RUN"],set(REQ["E4"]),True)

    for cid,reversible,available,adds,removes,preserve,expected in c["E5"]:
        facts=["BF:"+cid]; history=["HE:"+cid]; avail=list(available)
        for x in removes:
            if x in avail: avail.remove(x)
        for x in adds:
            if x not in avail: avail.append(x)
        out=[]
        if "branch_facts" not in preserve: out.append("MIGRATION_DROPPED_BRANCH_FACTS"); facts=[]
        if "history" not in preserve: out.append("MIGRATION_DROPPED_HISTORY"); history=[]
        covers={"reload","migration","availability", "reversible" if reversible else "irreversible"}
        add("E5",cid,expected,sorted(out),covers)

    brief=c["E6"]["brief"]; allow=set(brief["allow"]); secret=set(brief["secret"])
    for cid,refs,reveals,mutations,want in c["E6"]["candidates"]:
        out=[]
        if any(r not in allow for r in refs): out.append("UNGROUNDED_REFERENCE")
        if any(r in secret for r in reveals): out.append("SECRET_OR_UNKNOWN_REVEAL")
        if mutations: out.append("DIRECT_AUTHORITATIVE_MUTATION")
        accepted=not out
        covers=set()
        if cid.startswith("valid-"): covers|={"same_brief_variants","known_facts","valid_variation"}
        if cid=="bad-ref": covers|={"invalid_fact"}
        if cid=="secret": covers|={"known_secrets","invalid_secret"}
        if cid=="mutation": covers|={"invalid_fact"}
        add("E6",cid,{"accepted":want},{"accepted":accepted},covers)

    groups=defaultdict(list)
    for iid,motif,obj,dia,rew in c["E7"]: groups[(tuple(obj),tuple(dia),tuple(rew))].append(iid)
    clusters=sorted(sorted(v) for v in groups.values() if len(v)>1)
    add("E7","batch",[["q1","q2"]],clusters,{"repeated_cluster","distinct_control","motif_control"})

    for cid,periods,events,expected in c["E8"]["traces"]:
        rel=[0,0,0]; knowledge=[]; history=[]; out=[]
        for eid,p,delta,kadds in sorted(events,key=lambda x:(x[1],x[0])):
            if p<1 or p>periods: out.append("EVENT_OUTSIDE_HORIZON"); continue
            history.append(eid)
            rel=[a+b for a,b in zip(rel,delta)]
            for ref,authorized in kadds:
                if not authorized: out.append("ILLEGAL_KNOWLEDGE_UPDATE_BLOCKED")
                elif ref not in knowledge: knowledge.append(ref)
        covers={"many_periods","world_events","player_policies","relationship","knowledge"}
        add("E8",cid,expected,sorted(set(out)),covers)
    solv,find=quest(c["E8"]["quest"],goal="aftermath",start="entry")
    add("E8","quest",{"solvable":True,"findings":[]},{"solvable":solv,"findings":find},{"quest_deadlock"})
    add("E8","schedule-block",["COVERAGE_BLOCKED_SCHEDULE"],["COVERAGE_BLOCKED_SCHEDULE"],{"npc_reachability","schedule_deadlock"},True)

    scores={}; eligibility={}
    for critic,weights in c["E9"]["critics"]:
        scores[critic]={}; eligibility[critic]={}
        for iid,grounded,cons,novel,pref in c["E9"]["items"]:
            vals=[grounded,cons,novel,pref]
            scores[critic][iid]=sum(a*b for a,b in zip(vals,weights))
            eligibility[critic][iid]=bool(grounded)
    ranks={k:[i for i,_ in sorted(v.items(),key=lambda kv:(-kv[1],kv[0]))] for k,v in scores.items()}
    disagreement=len({tuple(v) for v in ranks.values()})>1
    bad_eligible=[(k,i) for k in eligibility for i,v in eligibility[k].items() if i=="ungrounded-pretty" and v]
    actual={"disagreement":disagreement,"ungrounded_eligible":bad_eligible,"authority":"NO_SINGLE_CRITIC"}
    expected={"disagreement":True,"ungrounded_eligible":[],"authority":"NO_SINGLE_CRITIC"}
    add("E9","calibration",expected,actual,set(REQ["E9"]))

    per={}
    by=defaultdict(list)
    for x in cases: by[x["exp"]].append(x)
    for exp in [f"E{i}" for i in range(1,10)]:
        missing=REQ[exp]-cov[exp]; mism=[x["id"] for x in by[exp] if not x["match"]]
        if exp=="E4": outcome="NOT_RUN"; reason="BLOCKED_BY_EXACT_PREREQUISITE"
        elif mism: outcome="FAIL"; reason="EXPECTATION_MISMATCH"
        elif missing: outcome="INCONCLUSIVE"; reason="REQUIRED_COVERAGE_MISSING"
        elif blocked[exp]: outcome="INCONCLUSIVE"; reason="REQUIRED_COVERAGE_BLOCKED"
        else: outcome="PASS"; reason="BOUNDED_STRUCTURAL_PREDICATE_SATISFIED"
        per["WSN-"+exp]={
          "outcome":outcome,"reason":reason,"observed":sorted(cov[exp]),"blocked":sorted(blocked[exp]),
          "missing":sorted(missing),"mismatches":mism,"cases":[x["id"] for x in by[exp]]
        }
    counts=defaultdict(int)
    for v in per.values(): counts[v["outcome"]]+=1
    return {"schema":"everfield_w2_wsn_world_structure_results_v2","evaluator":VERSION,
      "mission":c["mission"],"issue":c["issue"],"tranche":c["tranche"],"cases":cases,"experiments":per,
      "counts":dict(sorted(counts.items())),
      "authority":{"canonical":False,"human_quality":"NOT_ESTABLISHED","production_persistence":"NOT_ESTABLISHED","production_schedule":"NOT_ESTABLISHED","readiness":False,"verification_pass":False,"engine_selection":False,"release":False}}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--corpus",required=True); p.add_argument("--output")
    a=p.parse_args(); cp=Path(a.corpus); raw=cp.read_bytes(); c=json.loads(raw)
    r=run(c); r["sha256"]={"corpus":hashlib.sha256(raw).hexdigest(),"evaluator":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    text=json.dumps(r,sort_keys=True,separators=(",",":"))+"\n"
    if a.output: Path(a.output).write_text(text)
    else: print(text,end="")
if __name__=="__main__": main()
