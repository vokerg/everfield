# W2-ORDER-01 — Causal ordering, replay, and contention experiment

**Mission:** `W2-ORDER-01`  
**Issue:** #75  
**Branch:** `planning/issue-75`  
**Claim:** Issue #75 comment `5262599148`  
**Base main:** `21181eb20302a20d81aaec7b81a84acd4fcbbab8`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Decision state:** `EVIDENCE_REQUIRED`  
**Producer result:** `BOUNDED_PASS` for the experiment-local ordering claim in §11; `W2-REV-01` remains the required independent review.

## Review index

1. Scope, constraints, assumptions, evidence/inference — §§1–2.
2. Ordering alternatives, causal graph, synchronization, tie-break contract — §§3–4.
3. Retained runnable harness and deterministic replay evidence — §§5–7.
4. Contention/performance measurements and correctness/performance separation — §§8–9.
5. Recommendation, risks, unresolved questions, reopen conditions, review route — §§10–14.

## 1. Scope and non-goals

This planning experiment asks one bounded question:

> Can Everfield use deterministic domain-local/causal ordering as the default planning candidate for simulation work, while introducing stable synchronization/tie-break ordering only where commands actually contend, without requiring a global total order for all events?

In scope:

- explicit causal dependency graphs;
- deterministic per-domain order;
- cross-domain synchronization points;
- simultaneous noncommuting effects;
- stable conflict tie-breakers;
- replay from an exact recorded linearization;
- multiple legal interleavings of independent causal components;
- stronger global-total-order and weaker arrival-tied alternatives;
- synthetic coordination-throughput stress as synchronization density rises.

Non-goals:

- no production scheduler, engine/runtime, networking protocol, distributed consensus, lock implementation, or thread model;
- no final tick rate, gameplay system partition, domain granularity, or performance budget;
- no canonical semantic encoding/hash authority;
- no claim that the Python microbenchmark predicts production throughput;
- no engine selection or implementation-readiness transition.

The retained executable is a disposable `PLANNING_EXPERIMENT`, not a production dependency.

## 2. Canonical constraints, assumptions, observations, and inference

### 2.1 Observed canonical constraints

The authoritative Wave 1 foundation requires domains to declare deterministic local ordering, causal edges, synchronization points, and stable tie-breakers. It explicitly says global total order is **not** a default architecture mandate. It also keeps cross-runtime state-hash authority `EVIDENCE_REQUIRED`, requires replay-sensitive semantics to bind versioned logical rules rather than ambient wall time, and gives planning experiments no production authority.

### 2.2 Experiment assumptions

The fixture deliberately makes these assumptions explicit rather than treating them as product decisions:

- A command declares every logical domain it can mutate.
- Commands touching disjoint domains commute in this fixture.
- Commands touching a shared domain are a contention component and require a stable conflict order.
- Causal dependencies are explicit and acyclic.
- Logical `tick` is fixture metadata only; wall-clock arrival never defines canonical semantic order.
- State arithmetic is bounded modulo `1_000_003` solely to keep the stress state compact.
- The process benchmark models coordination topology, not game logic cost.

Reopen if a later runtime cannot soundly declare mutation domains, if nominally disjoint operations have hidden shared state, or if cross-domain effects cannot expose synchronization edges.

### 2.3 Observed experiment results

On Python `3.13.5`, Linux `6.18.35`, x86_64, 5 visible CPUs:

- Fixture: **1,154 events**, **12 domains**, **80 logical ticks**, **110 explicit cross-domain synchronization events**, **28 simultaneous noncommuting conflict pairs**.
- Across 200 seeded `causal_local` schedules: **1 final-state digest**, **200 distinct legal linear trace digests**, **1 conflict-order digest**.
- Across 200 seeded `arrival_tied` schedules: **200 final-state digests**, **200 trace digests**, **200 conflict-order digests**.
- Across 200 `global_total` schedules: **1 final-state digest**, **1 trace digest**, **1 conflict-order digest**.
- `causal_local` and `global_total` converged to the same final logical state when their stable conflict tie-break was the same.
- Replaying the exact recorded `causal_local` seed-37 trace reproduced the exact final state and trace digest.
- In the 4-process synthetic coordination benchmark, local/causal coordination was about `10.63x` the global-ticket baseline at 1% synchronization, `8.24x` at 10%, `1.66x` at 30%, and `0.99x` at 100%.

### 2.4 Inference

The correctness evidence supports **partial-order determinism** for the exercised model: independent causal components need not share one semantic sequence number if all shared-domain conflicts have deterministic order and replay preserves the dependency/tie-break contract.

The performance evidence supports only a narrower statement: a mandatory shared sequencer can impose avoidable coordination cost when most work is domain-local, while that advantage collapses as synchronization approaches all events.

### 2.5 Noncanonical recommendation

Admit domain-local/causal ordering as the default **planning candidate** for later shared-kernel work, with:

1. explicit touched-domain declarations;
2. explicit causal dependency IDs;
3. versioned stable local sequence/tie-break semantics;
4. explicit synchronization components for commands touching shared domains;
5. deterministic replay inputs sufficient to reconstruct the accepted conflict order;
6. stronger total ordering only for a bounded scope whose correctness/audit requirement or measured contention justifies it.

This is not a production architecture decision until the declared review/evidence/readiness route passes.

## 3. Alternatives under test

### A. `causal_local`

- Respect all declared causal predecessor edges.
- Maintain deterministic domain-local sequencing.
- At each ready frontier, partition events by overlapping touched domains.
- Events in one contention component use stable `(logical_tick, event_id)` order.
- Independent components may interleave arbitrarily.
- Replay may use an exact accepted linearization, but semantic authority does not require unrelated components to share a total-order ticket.

### B. `global_total`

- Respect all causal predecessor edges.
- Sort every ready frontier globally by `(logical_tick, event_id)`.
- This creates one stronger linearization even for disjoint domains.

This is a valid comparison alternative, not a rejected architecture. It can be appropriate for scopes where a single audit sequence is itself a requirement or where nearly all work contends.

### C. `arrival_tied`

- Respect causal predecessor edges.
- Break simultaneous-ready conflicts by randomized/arrival order.

This is the negative control. It represents the tempting but unsafe assumption that causal readiness alone is sufficient even when two noncommuting effects mutate the same domain.

## 4. Causal graph, synchronization, and tie-break semantics

A minimal conflict fragment is:

```text
                    +--> add(+3) --+
prior(domain D) ----|              +--> barrier(D) --> later(D)
                    +--> mul(*2) --+
```

Both effects are causally ready after the same predecessor and both touch `D`. They do not commute:

```text
x = 10
stable add-before-mul: (10 + 3) * 2 = 26
mul-before-add:        (10 * 2) + 3 = 23
```

Therefore the causal graph alone is insufficient at this synchronization point. The fixture contract adds a stable conflict tie-break: `(logical_tick, event_id)`.

A cross-domain transfer touches both source and destination:

```yaml
event:
  kind: transfer
  touches: [domain_A, domain_B]
  causal_predecessors:
    - latest(domain_A)
    - latest(domain_B)
```

It is therefore a synchronization point in the fixture. Two simultaneously-ready components with disjoint `touches` may be interleaved without changing fixture state.

Experiment-local ordering record:

```yaml
OrderingContract:
  version: order.fixture.v1
  simulation_rules_version: sim.fixture.v1
  event_id: <stable>
  logical_tick: <integer>
  touches: [<declared logical domain ids>]
  causal_predecessors: [<event ids>]
  local_order_key: [logical_tick, event_id]
  conflict_tie_break_key: [logical_tick, event_id]
  accepted_recorded_outcome_ref: <optional retained replay input>
```

This is not a canonical production schema. A later contract must define validation/failure behavior for undeclared touches and hidden shared state.

## 5. Retained runnable reference harness

The following standard-library Python program is the exact logical experiment. It intentionally sorts sets/frontiers before seeded shuffling so seed-dependent traces do not depend on Python hash iteration order.

```python
from collections import defaultdict
import hashlib, json, multiprocessing as mp, os, platform, random, statistics
import sys, time

MOD = 1_000_003
DOMAINS = 12
TICKS = 80
CONFLICT_TICKS = {0, 1} | {t for t in range(TICKS) if t % 3 == 2}

def build_fixture():
    events = {}
    deps = defaultdict(set)
    last = {d: None for d in range(DOMAINS)}
    eidn = 0
    conflict_pairs = []
    sync_count = 0

    def new_event(tick, kind, touches, args, preds=None, update_last=True):
        nonlocal eidn
        eid = f"e{eidn:04d}"
        eidn += 1
        touches = tuple(sorted(touches))
        events[eid] = {
            "eid": eid, "tick": tick, "kind": kind,
            "touches": touches, "args": dict(args),
        }
        if preds is None:
            for d in touches:
                if last[d] is not None:
                    deps[eid].add(last[d])
        else:
            deps[eid].update(preds)
        if update_last:
            for d in touches:
                last[d] = eid
        return eid

    for tick in range(TICKS):
        for d in range(DOMAINS):
            new_event(
                tick, "add", (d,),
                {"amount": ((tick + 1) * (d + 3)) % 17 + 1},
            )

        # 108 + 2 = 110 explicit cross-domain synchronization events.
        if tick % 3 == 0:
            for src in (0, 3, 6, 9):
                new_event(
                    tick, "transfer", (src, src + 1),
                    {"amount": (tick + src) % 11 + 1},
                )
                sync_count += 1
        elif tick == 1:
            for src in (2, 8):
                new_event(
                    tick, "transfer", (src, src + 1),
                    {"amount": (tick + src) % 11 + 1},
                )
                sync_count += 1

        # 28 noncommuting simultaneous conflicts; both share one predecessor.
        if tick in CONFLICT_TICKS:
            d = (tick * 5 + 1) % DOMAINS
            prior = last[d]
            preds = [] if prior is None else [prior]
            a = new_event(
                tick, "add", (d,), {"amount": 3},
                preds=preds, update_last=False,
            )
            m = new_event(
                tick, "mul", (d,), {"factor": 2},
                preds=preds, update_last=False,
            )
            b = new_event(
                tick, "barrier", (d,), {},
                preds=[a, m], update_last=True,
            )
            conflict_pairs.append((a, m, b, d))

    for eid in events:
        deps.setdefault(eid, set())
    return events, deps, conflict_pairs, sync_count

EVENTS, DEPS, CONFLICT_PAIRS, SYNC_COUNT = build_fixture()

def topo_index():
    children = defaultdict(list)
    indeg = {}
    for eid in EVENTS:
        indeg[eid] = len(DEPS[eid])
        for parent in DEPS[eid]:
            children[parent].append(eid)
    return indeg, children

def conflict_components(wave):
    wave = sorted(wave)
    adj = {eid: set() for eid in wave}
    by_domain = defaultdict(list)
    for eid in wave:
        for d in EVENTS[eid]["touches"]:
            by_domain[d].append(eid)
    for members in by_domain.values():
        for i, eid in enumerate(members):
            for other in members[i + 1:]:
                adj[eid].add(other)
                adj[other].add(eid)

    components = []
    seen = set()
    for eid in wave:
        if eid in seen:
            continue
        stack = [eid]
        seen.add(eid)
        component = []
        while stack:
            cur = stack.pop()
            component.append(cur)
            for nxt in sorted(adj[cur], reverse=True):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        components.append(tuple(sorted(
            component, key=lambda x: (EVENTS[x]["tick"], x)
        )))
    components.sort(key=lambda c: c[0])
    return components

def apply_event(state, event):
    kind = event["kind"]
    touched = event["touches"]
    args = event["args"]
    if kind == "add":
        d = touched[0]
        state[d] = (state[d] + args["amount"]) % MOD
    elif kind == "mul":
        d = touched[0]
        state[d] = (state[d] * args["factor"]) % MOD
    elif kind == "transfer":
        src, dst = touched
        amount = args["amount"] % MOD
        state[src] = (state[src] - amount) % MOD
        state[dst] = (state[dst] + amount) % MOD
    elif kind == "barrier":
        pass
    else:
        raise ValueError(kind)

def digest_state(state):
    raw = json.dumps(
        state, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(raw).hexdigest()

def run_schedule(policy, seed=0, recorded_trace=None):
    state = {d: (101 + 17 * d) % MOD for d in range(DOMAINS)}
    trace = []

    if recorded_trace is not None:
        done = set()
        for eid in recorded_trace:
            assert eid in EVENTS
            assert DEPS[eid] <= done
            apply_event(state, EVENTS[eid])
            trace.append(eid)
            done.add(eid)
        assert len(done) == len(EVENTS)
    else:
        indeg, children = topo_index()
        ready = {eid for eid, count in indeg.items() if count == 0}
        rng = random.Random(seed)
        done = set()

        while ready:
            wave = sorted(ready)
            ready.clear()

            if policy == "global_total":
                ordered = sorted(
                    wave, key=lambda e: (EVENTS[e]["tick"], e)
                )
            elif policy == "arrival_tied":
                ordered = list(wave)
                rng.shuffle(ordered)
            elif policy == "causal_local":
                components = conflict_components(wave)
                # Components are disjoint by touched domains; only their
                # interleaving changes. Internal conflict order is stable.
                rng.shuffle(components)
                ordered = [
                    eid for component in components for eid in component
                ]
            else:
                raise ValueError(policy)

            for eid in ordered:
                assert DEPS[eid] <= done
                apply_event(state, EVENTS[eid])
                trace.append(eid)
                done.add(eid)

            # Release the next causal wave only after this ready wave commits.
            for eid in ordered:
                for child in children[eid]:
                    indeg[child] -= 1
                    if indeg[child] == 0:
                        ready.add(child)

        assert len(done) == len(EVENTS)

    state_digest = digest_state(state)
    trace_digest = hashlib.sha256(
        "\n".join(trace).encode()
    ).hexdigest()
    pos = {eid: i for i, eid in enumerate(trace)}
    conflict_vector = [
        (a, m, "A<M" if pos[a] < pos[m] else "M<A")
        for a, m, _, _ in CONFLICT_PAIRS
    ]
    conflict_digest = hashlib.sha256(
        json.dumps(conflict_vector, separators=(",", ":")).encode()
    ).hexdigest()
    return state, trace, state_digest, trace_digest, conflict_digest

def correctness():
    summary = {}
    for policy in ("causal_local", "arrival_tied", "global_total"):
        states, traces, conflicts = set(), set(), set()
        for seed in range(200):
            _, _, sd, td, cd = run_schedule(policy, seed)
            states.add(sd)
            traces.add(td)
            conflicts.add(cd)
        summary[policy] = {
            "unique_states": len(states),
            "unique_linear_traces": len(traces),
            "unique_conflict_orders": len(conflicts),
        }

    _, trace, sd, td, cd = run_schedule("causal_local", 37)
    _, replay_trace, rsd, rtd, rcd = run_schedule(
        "causal_local", recorded_trace=trace
    )
    assert (sd, td, cd) == (rsd, rtd, rcd)
    assert trace == replay_trace
    return summary, {
        "seed": 37, "events": len(trace),
        "state_digest": sd, "trace_digest": td,
        "conflict_digest": cd,
    }

def bench_worker(
    policy, n, sync_every, shared_lock, shared_seq, start_evt, q, wid
):
    start_evt.wait()
    local_seq = [0] * DOMAINS
    x = (wid + 1) * 17
    t0 = time.perf_counter()

    if policy == "global_total":
        for i in range(n):
            d = i % DOMAINS
            # Equal synthetic event work outside the coordination section.
            x = (x * 1664525 + 1013904223 + d + i) & 0xffffffff
            with shared_lock:
                shared_seq.value += 1
                ticket = shared_seq.value
            x ^= ticket & 0xffff
    else:
        for i in range(n):
            d = i % DOMAINS
            local_seq[d] += 1
            x = (x * 1664525 + 1013904223 + d + i) & 0xffffffff
            if sync_every and i % sync_every == 0:
                with shared_lock:
                    shared_seq.value += 1
                    ticket = shared_seq.value
                x ^= ticket & 0xffff
            else:
                x ^= local_seq[d] & 0xffff

    q.put((time.perf_counter() - t0, x))

def bench_once(policy, workers, n=200_000, sync_rate=0.0):
    ctx = mp.get_context("fork")
    lock = ctx.Lock()
    shared_seq = ctx.Value("Q", 0, lock=False)
    start_evt = ctx.Event()
    q = ctx.Queue()
    sync_every = (
        0 if sync_rate <= 0 else max(1, round(1 / sync_rate))
    )
    processes = [
        ctx.Process(
            target=bench_worker,
            args=(
                policy, n, sync_every, lock, shared_seq,
                start_evt, q, wid,
            ),
        )
        for wid in range(workers)
    ]
    for p in processes:
        p.start()

    t0 = time.perf_counter()
    start_evt.set()
    results = [q.get() for _ in processes]
    for p in processes:
        p.join()
    wall = time.perf_counter() - t0
    assert all(p.exitcode == 0 for p in processes)
    return wall, workers * n / wall

def benchmark():
    rows = []
    for workers in (1, 2, 4):
        configs = [
            ("global_total", 1.00),
            ("causal_local", 0.00),
            ("causal_local", 0.01),
            ("causal_local", 0.10),
            ("causal_local", 0.30),
            ("causal_local", 1.00),
        ]
        for policy, sync_rate in configs:
            attempts = [
                bench_once(policy, workers, sync_rate=sync_rate)
                for _ in range(7)
            ]
            walls = [a[0] for a in attempts]
            throughput = [a[1] for a in attempts]
            rows.append({
                "workers": workers,
                "policy": policy,
                "sync_rate": sync_rate,
                "median_seconds": statistics.median(walls),
                "median_ops_per_second": statistics.median(throughput),
                "min_seconds": min(walls),
                "max_seconds": max(walls),
            })
    return rows

if __name__ == "__main__":
    summary, replay = correctness()
    print(json.dumps({
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "machine": platform.machine(),
            "cpu_count": os.cpu_count(),
        },
        "fixture": {
            "events": len(EVENTS),
            "domains": DOMAINS,
            "ticks": TICKS,
            "sync_events": SYNC_COUNT,
            "conflict_pairs": len(CONFLICT_PAIRS),
        },
        "correctness": summary,
        "replay": replay,
        "benchmark": benchmark(),
    }, indent=2, sort_keys=True))
```

## 6. Correctness and interleaving results

The 200-seed stress result:

| Policy | Unique final states | Unique linear traces | Unique conflict orders | Interpretation |
|---|---:|---:|---:|---|
| `causal_local` | 1 | 200 | 1 | independent components interleaved differently; shared-domain conflict order remained stable |
| `global_total` | 1 | 1 | 1 | stronger deterministic linearization |
| `arrival_tied` | 200 | 200 | 200 | nondeterministic shared-domain conflict order changed state |

The common final-state digest for `causal_local` and `global_total` was:

`2c384137b5f18771e80bbceb2654bd8a9376d553847a4d8c65b678753e5ebcb0`

This is an experiment-local SHA-256 diagnostic only. It **does not** claim the canonical cross-runtime semantic-hash authority owned by W2-HASH-01.

### Retained mismatch/race

The `arrival_tied` negative control is not discarded as “flaky.” It is the material race finding: causal readiness without deterministic arbitration for noncommuting shared-domain effects is insufficient. All 200 seeds landed on distinct final-state digests in this stress corpus.

## 7. Deterministic replay evidence

Recorded run:

```yaml
policy: causal_local
seed: 37
event_count: 1154
state_digest: 2c384137b5f18771e80bbceb2654bd8a9376d553847a4d8c65b678753e5ebcb0
trace_digest: f74db936f4af78489d3a2e20e97a1d8b992624f19d73fe83d42a2d2a79edcc07
conflict_digest: e2f69c3695d82ca59731a0f3d09db6aee8fa30e7c05b93c2e3559be067e0aba2
```

Re-applying that exact trace while checking every predecessor before execution reproduced all three digests exactly.

The evidence proves deterministic replay only for this fixture and accepted trace. A production replay envelope still needs exact rules/content identity, accepted generated outcomes where relevant, domain/tie-break contract version, and whatever later ArtifactIdentity/retention contract is reviewed.

## 8. Coordination-throughput benchmark

Environment:

```yaml
python: 3.13.5
platform: Linux-6.18.35-x86_64-with-glibc2.41
machine: x86_64
visible_cpu_count: 5
process_start_method: fork
events_per_worker_per_attempt: 200000
attempts_per_cell: 7
reported_statistic: median wall-clock throughput
```

The global baseline performs the same synthetic event arithmetic as the local candidate but acquires one shared sequence lock/ticket for **every** event. The causal/local candidate increments process-local domain sequence and acquires that same shared coordination primitive only at the configured synchronization rate.

| Workers | Policy | Shared-sync rate | Median sec | Observed sec range | Median ops/s | vs same-worker global |
|---:|---|---:|---:|---:|---:|---:|
| 1 | global total | 100% | 0.228 | 0.225–0.241 | 876,783 | 1.00x |
| 1 | causal/local | 0% | 0.112 | 0.108–0.121 | 1,784,419 | 2.04x |
| 1 | causal/local | 1% | 0.120 | 0.115–0.130 | 1,670,026 | 1.90x |
| 1 | causal/local | 10% | 0.135 | 0.130–0.145 | 1,485,846 | 1.69x |
| 1 | causal/local | 30% | 0.178 | 0.174–0.194 | 1,123,509 | 1.28x |
| 1 | causal/local | 100% | 0.260 | 0.256–0.273 | 770,297 | 0.88x |
| 2 | global total | 100% | 0.327 | 0.316–0.344 | 1,221,416 | 1.00x |
| 2 | causal/local | 0% | 0.115 | 0.112–0.119 | 3,483,348 | 2.85x |
| 2 | causal/local | 1% | 0.125 | 0.122–0.136 | 3,207,443 | 2.63x |
| 2 | causal/local | 10% | 0.151 | 0.147–0.167 | 2,649,040 | 2.17x |
| 2 | causal/local | 30% | 0.202 | 0.182–0.259 | 1,984,024 | 1.62x |
| 2 | causal/local | 100% | 0.318 | 0.294–0.335 | 1,256,181 | 1.03x |
| 4 | global total | 100% | 1.499 | 1.464–1.531 | 533,746 | 1.00x |
| 4 | causal/local | 0% | 0.142 | 0.129–0.170 | 5,631,925 | 10.55x |
| 4 | causal/local | 1% | 0.141 | 0.135–0.144 | 5,674,214 | 10.63x |
| 4 | causal/local | 10% | 0.182 | 0.160–0.272 | 4,398,142 | 8.24x |
| 4 | causal/local | 30% | 0.901 | 0.887–0.986 | 888,388 | 1.66x |
| 4 | causal/local | 100% | 1.517 | 1.466–1.648 | 527,274 | 0.99x |

The 4-worker crossover is the important qualitative result: the advantage is large when shared synchronization is sparse, shrinks materially at 30%, and disappears at 100%. That is evidence **against both extremes**: neither “always globally order” nor “local ordering is always faster” is supported.

### Benchmark limitations

- Python `multiprocessing`/lock cost is not an engine scheduler.
- The benchmark does no meaningful game simulation, cache-sensitive entity traversal, job stealing, network replication, persistence, or rendering.
- `fork` is Linux-specific.
- The shared lock is a deliberately simple coordination proxy.
- The benchmark compares coordination topology under equal synthetic event work; it does not establish a production latency/throughput budget.

A later engine/shared-kernel spike must remeasure the admitted scheduling choices in its actual runtime.

## 9. Correctness and performance are separate claims

Correctness result:

- `causal_local` **passes this fixture** only because its conflict components receive a stable tie-break.
- `arrival_tied` fails deterministic-state replay despite satisfying the same predecessor graph.
- `global_total` also passes this fixture.

Performance result:

- Sparse synchronization strongly favored local coordination in this microbenchmark.
- Near-total synchronization erased that advantage.

Therefore performance does not justify weakening deterministic conflict arbitration, and correctness does not by itself justify imposing global sequencing on unrelated work.

## 10. Alternatives and tradeoffs

| Alternative | Strength | Cost/risk | Appropriate bounded use |
|---|---|---|---|
| Domain-local + causal + stable conflict tie-break | allows independent work without semantic total order | requires complete touch/dependency declarations and synchronization validation | default planning candidate from this experiment |
| Global total order | simplest single linear audit/replay stream | unnecessary global coordination can serialize independent work | bounded high-contention/audit scope when evidence justifies |
| Arrival/wall-time tie-break | operationally easy | nondeterministic state for simultaneous noncommuting effects | not admissible for canonical effects in the exercised model |
| Recorded accepted linearization | exact replay of accepted run | storage/provenance/retention burden; does not remove need to validate original arbitration | replay/evidence envelope, especially for accepted nondeterministic external outcomes |

## 11. Bounded decision/result

`BOUNDED_PASS` for this planning claim:

> For the exercised deterministic simulation model, domain-local/causal scheduling with explicit touched domains, causal edges, synchronization components, and a stable conflict tie-break preserves one final logical state across multiple legal independent interleavings and exact recorded replay. A global total-order sequencer is therefore **not required by this evidence as the default semantic ordering mechanism**. Stronger total ordering remains admissible for a bounded scope when later correctness/audit requirements or measured contention justify it.

This result does **not**:

- prove production performance;
- select a scheduler/runtime/engine;
- prove hidden state cannot violate domain independence;
- establish canonical state serialization/hash;
- resolve W2-SIM-01 parity;
- resolve implementation readiness.

## 12. Observability and downstream evaluation

A later shared-kernel/simulation implementation should expose at minimum:

```yaml
OrderingEvidence:
  ordering_contract_version: <exact>
  simulation_rules_version: <exact>
  event_id: <stable>
  touched_domains: []
  causal_predecessor_ids: []
  conflict_component_id: <when applicable>
  conflict_tie_break_key: <when applicable>
  accepted_order_or_trace_ref: <retained evidence>
  synchronization_rate: <measured>
  contention_wait_or_queue_metric: <measured>
  replay_result: PASS | FAIL | INCONCLUSIVE
  divergence_ref: <required on mismatch>
```

Required adversarial cases should include:

- undeclared/incorrect touched-domain metadata;
- hidden shared singleton/global state;
- simultaneous noncommuting effects;
- cyclic or missing dependencies;
- tie-break key collision;
- replay with changed rules/content/tie-break version;
- high-contention domains where local coordination no longer wins;
- cross-domain rollback/failure semantics;
- accepted external/generated outcome replay without re-calling the nondeterministic producer.

## 13. Failure modes and risks

1. **False independence:** two “disjoint” domains mutate shared hidden state. This invalidates component reordering.
2. **Tie-break collision or unstable identity:** deterministic conflict order disappears.
3. **Dependency omission:** replay may be deterministic but semantically wrong because the graph is incomplete.
4. **Over-synchronization:** a domain model that declares everything shared degenerates toward global ordering and loses concurrency.
5. **Under-synchronization:** missing a shared-domain edge reproduces the `arrival_tied` class of race.
6. **Audit requirement mismatch:** some bounded systems may require one linear external sequence independent of state equivalence.
7. **Benchmark transference:** Python lock ratios cannot be promoted into production capacity claims.
8. **Hash overclaim:** local diagnostic digests are not cross-runtime semantic identity.
9. **Replay retention loss:** exact replay cannot be asserted if required trace/rules/content/outcome evidence becomes unavailable.

## 14. Unresolved questions and reopen conditions

Unresolved:

- What production logical domains and command touch declarations are appropriate?
- Which cross-domain operations require synchronization barriers versus commutative/CRDT-like semantics?
- Does any target runtime/platform materially change the contention crossover?
- Which bounded scopes, if any, require a single globally auditable sequence?
- What exact trace/ArtifactIdentity/retention shape will W2-SIM-01 and later implementation evidence use?
- How should a production validator fail when a command touches undeclared state?

Reopen this result if:

- W2-SIM-01 or engine spikes observe divergent state under the proposed local/causal contract;
- hidden/shared mutation makes disjoint-component commutativity false;
- stable event identity/tie-break cannot be guaranteed;
- target workload synchronization density is near-global or a single-order audit requirement appears;
- a reviewed runtime model proves a different scheduling contract materially simpler or safer;
- canonical semantic-hash evidence changes what replay equivalence may assert;
- the authoritative foundation/ordering requirement changes.

## 15. Independent review and downstream route

Required independent critique remains `W2-REV-01`. The producer must not self-promote this evidence.

`W2-SIM-01` is also gated on `W2-ORDER-01_REVIEW_READY` plus its other prerequisites and must compare abstract/model behavior with the representative shared kernel; it may not treat this fixture as production parity proof.

No producer artifact from this branch should be merged into `main` as a substitute for the declared Wave 2 review/synthesis/verification route. Any eventual `main` integration remains squash-only under the canonical program.
