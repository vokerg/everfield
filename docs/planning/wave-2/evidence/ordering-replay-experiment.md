# W2-ORDER-01 — Causal ordering, replay, and contention experiment

**Mission:** `W2-ORDER-01`  
**Issue:** #75  
**Branch:** `planning/issue-75`  
**Claim:** Issue #75 comment `5262599148`  
**Base main:** `21181eb20302a20d81aaec7b81a84acd4fcbbab8`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Decision state:** `EVIDENCE_REQUIRED`  
**Producer result:** `BOUNDED_PASS` for §9 only; required independent review remains `W2-REV-01`.

## Review index

1. Scope, constraints, assumptions — §§1–2.
2. Alternatives, causal graph, tie-break contract — §§3–4.
3. Runnable fixture, replay, retained race — §§5–6.
4. Contention measurements and claim separation — §§7–8.
5. Bounded result, risks, reopen/review route — §§9–12.

## 1. Question and boundaries

Question: **Can deterministic domain-local/causal ordering remain the default planning candidate when stable ordering is introduced only at actual synchronization/contention points, rather than imposing one total semantic order on all events?**

In scope: explicit causal dependencies, domain-local order, cross-domain synchronization, simultaneous noncommuting effects, stable tie-breaks, legal independent interleavings, exact recorded replay, a global-total alternative, an arrival-tied negative control, and synthetic contention stress.

Out of scope: production scheduler/engine/thread/network/persistence choices; final domain granularity/tick rate; production performance budgets; canonical cross-runtime serialization/hash; engine selection; implementation readiness. The executable below is disposable planning evidence and may not become a production dependency by implication.

## 2. Evidence discipline

### Canonical constraints observed

Wave 1 requires deterministic local ordering, causal edges, synchronization points, and stable tie-breakers, while stating that global total order is not a default mandate. Cross-runtime state-hash authority remains separately `EVIDENCE_REQUIRED`. Replay-sensitive semantics bind logical rules rather than ambient wall time.

### Experiment assumptions

- Commands declare every logical domain they mutate.
- Disjoint-domain operations commute **in this fixture**.
- Shared-domain simultaneous noncommuting effects require deterministic arbitration.
- Causal dependencies are explicit and acyclic.
- `tick` is logical metadata; arrival/wall time has no semantic authority.
- Synthetic coordination cost is not production game-logic cost.

Hidden shared state, undeclared touches, or inability to expose synchronization edges invalidate the fixture model.

### Observed results

Environment: Python `3.13.5`, Linux `6.18.35`, x86_64, 5 visible CPUs.

Fixture: **1,154 events**, **12 domains**, **80 logical ticks**, **110 cross-domain synchronization events**, **28 simultaneous noncommuting conflict pairs**.

Across 200 seeds:

| Policy | Unique final states | Unique linear traces | Unique conflict orders |
|---|---:|---:|---:|
| `causal_local` | 1 | 200 | 1 |
| `global_total` | 1 | 1 | 1 |
| `arrival_tied` | 200 | 200 | 200 |

`causal_local` and `global_total` reached the same final logical state when conflict arbitration matched. Exact replay of causal/local seed 37 reproduced state, trace, and conflict digests.

### Inference

The exercised model demonstrates **partial-order determinism**: unrelated components can have different legal linear interleavings without changing final state, provided all shared-domain conflicts have stable order. It does not prove that a production domain partition has those properties.

## 3. Alternatives

### `causal_local`

Respect predecessor edges. Partition a ready frontier into connected components by overlapping touched domains. Sort each conflict component by stable `(logical_tick,event_id)`. Independent components may interleave.

### `global_total`

Respect predecessor edges and globally sort every ready frontier by `(logical_tick,event_id)`, producing one stronger linearization for both related and unrelated events.

### `arrival_tied` negative control

Respect predecessor edges but shuffle simultaneously-ready events, including shared-domain conflicts. This intentionally tests the incorrect assumption that causal readiness alone is sufficient.

Global order remains admissible for a bounded scope that truly requires one audit stream or has near-global contention. This experiment only rejects making it mandatory **by default**.

## 4. Explicit causal/tie-break contract

Minimal noncommuting fragment:

```text
                    +--> add(+3) --+
prior(domain D) ----|              +--> barrier(D) --> later(D)
                    +--> mul(*2) --+
```

For `x=10`, add-before-mul gives `26`; mul-before-add gives `23`. The graph therefore needs stable arbitration at this shared-domain synchronization point.

A transfer touches both domains and depends on the latest event of each:

```yaml
OrderingContract:
  version: order.fixture.v1
  simulation_rules_version: sim.fixture.v1
  event_id: <stable>
  logical_tick: <integer>
  touches: [<logical-domain ids>]
  causal_predecessors: [<event ids>]
  conflict_tie_break_key: [logical_tick, event_id]
  accepted_trace_ref: <optional retained replay input>
```

This is an experiment-local shape, not a production schema.

## 5. Retained runnable harness

The exact correctness fixture and benchmark logic are below. Ready sets are sorted before seeded shuffling so seeded traces do not depend on Python set/hash iteration. Benchmark sync percentages use exact per-100 quotas; the producer self-review corrected an earlier draft that approximated 30% as every third event.

```python
from collections import defaultdict
import hashlib, json, multiprocessing as mp, os, platform, random, statistics
import sys, time

MOD=1_000_003; DOMAINS=12; TICKS=80
CONFLICT_TICKS={0,1}|{t for t in range(TICKS) if t%3==2}

def build_fixture():
    E={}; D=defaultdict(set); last={d:None for d in range(DOMAINS)}
    n=0; pairs=[]; sync=0
    def add(tick,kind,touches,args,preds=None,update=True):
        nonlocal n
        eid=f"e{n:04d}"; n+=1; touches=tuple(sorted(touches))
        E[eid]={"tick":tick,"kind":kind,"touches":touches,"args":dict(args)}
        if preds is None:
            for d in touches:
                if last[d] is not None: D[eid].add(last[d])
        else: D[eid].update(preds)
        if update:
            for d in touches: last[d]=eid
        return eid
    for tick in range(TICKS):
        for d in range(DOMAINS):
            add(tick,"add",(d,),{"amount":((tick+1)*(d+3))%17+1})
        if tick%3==0:
            for src in (0,3,6,9):
                add(tick,"transfer",(src,src+1),{"amount":(tick+src)%11+1}); sync+=1
        elif tick==1:
            for src in (2,8):
                add(tick,"transfer",(src,src+1),{"amount":(tick+src)%11+1}); sync+=1
        if tick in CONFLICT_TICKS:
            d=(tick*5+1)%DOMAINS; p=[] if last[d] is None else [last[d]]
            a=add(tick,"add",(d,),{"amount":3},p,False)
            m=add(tick,"mul",(d,),{"factor":2},p,False)
            b=add(tick,"barrier",(d,),{},[a,m],True)
            pairs.append((a,m,b,d))
    for e in E: D.setdefault(e,set())
    return E,D,pairs,sync
E,D,PAIRS,SYNC=build_fixture()

def index():
    indeg={e:len(D[e]) for e in E}; children=defaultdict(list)
    for e in E:
        for p in D[e]: children[p].append(e)
    return indeg,children

def components(wave):
    wave=sorted(wave); adj={e:set() for e in wave}; by=defaultdict(list)
    for e in wave:
        for d in E[e]["touches"]: by[d].append(e)
    for members in by.values():
        for i,e in enumerate(members):
            for f in members[i+1:]: adj[e].add(f); adj[f].add(e)
    out=[]; seen=set()
    for e in wave:
        if e in seen: continue
        stack=[e]; seen.add(e); comp=[]
        while stack:
            x=stack.pop(); comp.append(x)
            for y in sorted(adj[x],reverse=True):
                if y not in seen: seen.add(y); stack.append(y)
        out.append(tuple(sorted(comp,key=lambda x:(E[x]["tick"],x))))
    return sorted(out,key=lambda c:c[0])

def apply(state,e):
    ev=E[e]; k=ev["kind"]; t=ev["touches"]; a=ev["args"]
    if k=="add": state[t[0]]=(state[t[0]]+a["amount"])%MOD
    elif k=="mul": state[t[0]]=(state[t[0]]*a["factor"])%MOD
    elif k=="transfer":
        s,d=t; q=a["amount"]%MOD; state[s]=(state[s]-q)%MOD; state[d]=(state[d]+q)%MOD
    elif k!="barrier": raise ValueError(k)

def run(policy,seed=0,recorded=None):
    state={d:(101+17*d)%MOD for d in range(DOMAINS)}; trace=[]
    if recorded is not None:
        done=set()
        for e in recorded:
            assert e in E and D[e] <= done
            apply(state,e); trace.append(e); done.add(e)
        assert len(done)==len(E)
    else:
        indeg,children=index(); ready={e for e,n in indeg.items() if n==0}
        rng=random.Random(seed); done=set()
        while ready:
            wave=sorted(ready); ready.clear()
            if policy=="global_total": ordered=sorted(wave,key=lambda e:(E[e]["tick"],e))
            elif policy=="arrival_tied": ordered=list(wave); rng.shuffle(ordered)
            elif policy=="causal_local":
                cs=components(wave); rng.shuffle(cs); ordered=[e for c in cs for e in c]
            else: raise ValueError(policy)
            for e in ordered:
                assert D[e] <= done; apply(state,e); trace.append(e); done.add(e)
            for e in ordered:
                for child in children[e]:
                    indeg[child]-=1
                    if indeg[child]==0: ready.add(child)
        assert len(done)==len(E)
    raw=json.dumps(state,sort_keys=True,separators=(",",":")).encode()
    sd=hashlib.sha256(raw).hexdigest()
    td=hashlib.sha256("\n".join(trace).encode()).hexdigest()
    pos={e:i for i,e in enumerate(trace)}
    cv=[(a,m,"A<M" if pos[a]<pos[m] else "M<A") for a,m,_,_ in PAIRS]
    cd=hashlib.sha256(json.dumps(cv,separators=(",",":")).encode()).hexdigest()
    return state,trace,sd,td,cd

def correctness():
    out={}
    for policy in ("causal_local","global_total","arrival_tied"):
        states=set(); traces=set(); conflicts=set()
        for seed in range(200):
            _,_,sd,td,cd=run(policy,seed); states.add(sd); traces.add(td); conflicts.add(cd)
        out[policy]=(len(states),len(traces),len(conflicts))
    _,trace,sd,td,cd=run("causal_local",37)
    _,trace2,sd2,td2,cd2=run("causal_local",recorded=trace)
    assert trace==trace2 and (sd,td,cd)==(sd2,td2,cd2)
    return out,(sd,td,cd)

def worker(policy,n,pct,lock,shared,start,q,wid):
    start.wait(); local=[0]*DOMAINS; x=(wid+1)*17; t0=time.perf_counter()
    for i in range(n):
        d=i%DOMAINS; local[d]+=1
        x=(x*1664525+1013904223+d+i)&0xffffffff
        need_shared=(policy=="global_total") or (pct and (i%100)<pct)
        if need_shared:
            with lock: shared.value+=1; ticket=shared.value
            x^=ticket&0xffff
        else: x^=local[d]&0xffff
    q.put((time.perf_counter()-t0,x))

def bench_once(policy,workers,n=200_000,pct=0):
    ctx=mp.get_context("fork"); lock=ctx.Lock(); shared=ctx.Value("Q",0,lock=False)
    start=ctx.Event(); q=ctx.Queue()
    ps=[ctx.Process(target=worker,args=(policy,n,pct,lock,shared,start,q,w)) for w in range(workers)]
    for p in ps: p.start()
    t0=time.perf_counter(); start.set(); vals=[q.get() for _ in ps]
    for p in ps: p.join()
    wall=time.perf_counter()-t0; assert all(p.exitcode==0 for p in ps)
    return wall,workers*n/wall

def benchmark():
    rows=[]
    for workers in (1,2,4):
        for policy,pct in [("global_total",100),("causal_local",0),("causal_local",1),
                           ("causal_local",10),("causal_local",30),("causal_local",100)]:
            attempts=[bench_once(policy,workers,pct=pct) for _ in range(7)]
            walls=[x[0] for x in attempts]; ops=[x[1] for x in attempts]
            rows.append((workers,policy,pct,statistics.median(walls),
                         min(walls),max(walls),statistics.median(ops)))
    return rows

if __name__=="__main__":
    print(json.dumps({
      "environment":{"python":sys.version.split()[0],"platform":platform.platform(),
                     "machine":platform.machine(),"cpu_count":os.cpu_count()},
      "fixture":{"events":len(E),"domains":DOMAINS,"ticks":TICKS,
                 "sync_events":SYNC,"conflict_pairs":len(PAIRS)},
      "correctness":correctness(),
      "benchmark":benchmark(),
    },indent=2))
```

## 6. Correctness, replay, and retained race

Common final-state diagnostic for `causal_local` and `global_total`:

`2c384137b5f18771e80bbceb2654bd8a9376d553847a4d8c65b678753e5ebcb0`

This is **experiment-local only**, not W2-HASH-01 cross-runtime authority.

Recorded `causal_local` seed 37:

```yaml
events: 1154
state_digest: 2c384137b5f18771e80bbceb2654bd8a9376d553847a4d8c65b678753e5ebcb0
trace_digest: f74db936f4af78489d3a2e20e97a1d8b992624f19d73fe83d42a2d2a79edcc07
conflict_digest: e2f69c3695d82ca59731a0f3d09db6aee8fa30e7c05b93c2e3559be067e0aba2
```

Replaying that exact trace while verifying every predecessor reproduced all three digests.

The `arrival_tied` negative control is retained as the material race: all 200 seeds produced distinct final-state and conflict-order digests. A later success does not erase that failure mode.

## 7. Exact-percent coordination benchmark

Environment/attempt policy:

```yaml
python: 3.13.5
platform: Linux-6.18.35-x86_64-with-glibc2.41
visible_cpu_count: 5
process_start_method: fork
events_per_worker_per_attempt: 200000
attempts_per_cell: 7
sync_quota: exact N of every 100 synthetic events
reported: median throughput plus observed min/max wall time
```

Global total takes one shared ticket on every event. Causal/local performs the same synthetic event arithmetic but takes the shared ticket only for its exact configured quota.

| Workers | Policy | Shared sync | Median sec | Range sec | Median ops/s | vs global |
|---:|---|---:|---:|---:|---:|---:|
| 1 | global total | 100% | 0.231 | 0.222–0.260 | 864,422 | 1.00x |
| 1 | causal/local | 0% | 0.115 | 0.112–0.124 | 1,734,786 | 2.01x |
| 1 | causal/local | 1% | 0.124 | 0.121–0.137 | 1,610,333 | 1.86x |
| 1 | causal/local | 10% | 0.134 | 0.132–0.135 | 1,494,827 | 1.73x |
| 1 | causal/local | 30% | 0.169 | 0.161–0.184 | 1,186,088 | 1.37x |
| 1 | causal/local | 100% | 0.263 | 0.258–0.278 | 760,990 | 0.88x |
| 2 | global total | 100% | 0.351 | 0.334–0.394 | 1,140,044 | 1.00x |
| 2 | causal/local | 0% | 0.120 | 0.115–0.121 | 3,321,371 | 2.91x |
| 2 | causal/local | 1% | 0.125 | 0.123–0.149 | 3,208,707 | 2.81x |
| 2 | causal/local | 10% | 0.141 | 0.138–0.148 | 2,838,481 | 2.49x |
| 2 | causal/local | 30% | 0.192 | 0.177–0.208 | 2,083,699 | 1.83x |
| 2 | causal/local | 100% | 0.343 | 0.320–0.404 | 1,164,507 | 1.02x |
| 4 | global total | 100% | 1.474 | 1.414–1.573 | 542,923 | 1.00x |
| 4 | causal/local | 0% | 0.134 | 0.127–0.169 | 5,987,272 | 11.03x |
| 4 | causal/local | 1% | 0.148 | 0.138–0.200 | 5,402,657 | 9.95x |
| 4 | causal/local | 10% | 0.169 | 0.162–0.223 | 4,745,179 | 8.74x |
| 4 | causal/local | 30% | 0.413 | 0.402–0.423 | 1,936,489 | 3.57x |
| 4 | causal/local | 100% | 1.542 | 1.373–1.722 | 518,886 | 0.96x |

The qualitative crossover is the evidence: sparse synchronization strongly benefits from avoiding a universal shared ticket in this microbenchmark; at 100% the advantage disappears.

Limits: Python multiprocessing/lock cost is not an engine scheduler; `fork` is Linux-specific; there is no game workload, job stealing, cache model, network/persistence/rendering, or production latency target. A real admitted runtime must remeasure.

## 8. Correctness and performance are separate claims

Correctness:

- `causal_local` passes only because shared-domain conflicts have a stable tie-break.
- `global_total` also passes.
- `arrival_tied` fails deterministic state.

Performance:

- sparse synthetic synchronization favored local coordination;
- full synchronization did not.

Therefore performance cannot weaken conflict arbitration, and correctness alone cannot justify globally sequencing unrelated work.

## 9. Bounded result

`BOUNDED_PASS`:

> For the exercised model, domain-local/causal scheduling with explicit touched domains, causal edges, synchronization components, and a stable conflict tie-break preserves one final logical state across multiple legal independent interleavings and exact recorded replay. This evidence does not require a global total-order sequencer as the **default semantic ordering mechanism**. Stronger total ordering remains admissible for bounded scopes whose audit/correctness requirement or measured contention justifies it.

Noncanonical recommendation: carry the causal/local contract as the default planning candidate into shared-kernel/parity work; require evidence before any production promotion.

This result does not select a scheduler/runtime/engine, prove production performance, prove hidden-state independence, establish canonical hash/serialization, resolve W2-SIM-01 parity, or change implementation readiness.

## 10. Observability and adversarial follow-up

Later evidence should expose exact ordering/rules versions, stable event IDs, touched domains, predecessor IDs, conflict component/tie-break key, retained accepted trace/outcome reference, measured synchronization/queueing, and replay divergence references.

Required adversarial cases: undeclared touches; hidden global state; tie-break collision; cyclic/missing dependency; changed rules/content; cross-domain rollback/failure; near-global contention; accepted nondeterministic external outcomes replayed without re-calling their producer.

## 11. Risks and reopen conditions

Material risks:

1. false domain independence from hidden shared mutation;
2. unstable/colliding event identity or tie-break;
3. missing dependency edges;
4. over-synchronization collapsing concurrency;
5. under-synchronization recreating the retained race;
6. a bounded audit requirement genuinely needing one sequence;
7. transferring Python microbenchmark ratios into production claims;
8. losing trace/rules/content/outcome evidence;
9. overclaiming local diagnostics as canonical semantic hashes.

Reopen on any observed state divergence under the proposed contract; inability to validate touched domains; near-global real workload contention; new single-linear-audit requirement; changed authoritative ordering rules; or stronger reviewed runtime evidence contradicting this result.

## 12. Review/downstream route

Required independent critique is `W2-REV-01`; this producer cannot self-promote the result.

`W2-SIM-01` remains separately gated by `W2-ORDER-01_REVIEW_READY` and its other prerequisites and must establish model/shared-kernel parity independently.

Do not merge this producer branch to `main` as a substitute for Wave 2 review/synthesis/verification. Any eventual `main` integration remains squash-only under the canonical program.
