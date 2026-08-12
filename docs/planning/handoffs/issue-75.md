# Issue #75 handoff — W2-ORDER-01

**Mission:** `W2-ORDER-01`  
**Branch:** `planning/issue-75`  
**Ownership generation:** Issue #75 comment `5262599148`  
**Base main:** `21181eb20302a20d81aaec7b81a84acd4fcbbab8`  
**Authoritative foundation blob:** `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Evidence report blob:** `acf95289fc79fac2adc4cf2d10d2014ed6b004cc`  
**State intended after terminal capsule:** `REVIEW_READY`  
**Required review:** `W2-REV-01`

## Completed work

Produced `docs/planning/wave-2/evidence/ordering-replay-experiment.md` from the task's bounded authoritative packet.

The retained standard-library experiment exercises:

- a 1,154-event / 12-domain causal graph over 80 logical ticks;
- 110 explicit cross-domain synchronization events;
- 28 simultaneous noncommuting shared-domain conflict pairs;
- domain-local/causal scheduling with stable conflict tie-breaks;
- a stronger globally total-ordered comparison;
- an arrival-tied negative control;
- 200 seeded correctness/replay interleavings per policy;
- exact replay of one retained causal/local trace;
- a 1/2/4-process synthetic contention benchmark from 0% through 100% shared synchronization.

The embedded harness was syntax-checked and its exact deterministic correctness path rerun after a self-review correction that removed Python set/hash-order dependence from seeded trace generation. The timed benchmark uses the same retained coordination functions and seven attempts per cell; the report preserves median and observed min/max wall time.

## Material findings

1. `causal_local` produced one final logical state across 200 legal independent-component interleavings while retaining 200 distinct linear traces and one stable conflict-order digest.
2. `arrival_tied` produced 200 distinct final states: a causal predecessor graph alone is insufficient when simultaneously-ready noncommuting effects share a logical domain.
3. `global_total` and `causal_local` converged to the same final state when stable conflict arbitration matched, so this fixture does not require a global semantic sequence for unrelated components.
4. Exact replay of causal/local seed 37 reproduced state, trace, and conflict digests.
5. Synthetic 4-process throughput relative to the global-ticket baseline was `10.63x` at 1% synchronization, `8.24x` at 10%, `1.66x` at 30%, and `0.99x` at 100%; the local advantage disappeared as contention became global.
6. The bounded recommendation is therefore conditional: prefer local/causal ordering as the planning candidate when touched domains/dependencies are explicit and shared conflicts have stable arbitration; retain stronger total order for bounded scopes whose audit/correctness requirement or measured contention justifies it.

## Scope limits / open work

This producer result is a `BOUNDED_PASS` only for the experiment-local ordering claim. It does **not** select a production scheduler, engine/runtime, tick rate, thread model, network model, domain granularity, canonical semantic encoding/hash, or implementation architecture. The Python process benchmark is a coordination-topology probe, not a production capacity forecast.

The fixture assumes that commands declare all mutated logical domains and that disjoint-domain operations commute. Hidden shared state, undeclared touches, changed rules/content, tie-break collisions, high real-runtime synchronization density, or a single-linear-audit requirement reopen the result.

W2-HASH-01 retains authority over cross-runtime semantic hash conformance. W2-SIM-01 must independently establish model/shared-kernel parity after its other prerequisites. Production implementation remains blocked.

## Checks/evidence

- Current base used for claim: `21181eb20302a20d81aaec7b81a84acd4fcbbab8`.
- Authoritative foundation blob: `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`.
- Evidence report blob: `acf95289fc79fac2adc4cf2d10d2014ed6b004cc`.
- Exact correctness result: causal/local `1 state / 200 traces / 1 conflict order`; global total `1 / 1 / 1`; arrival-tied `200 / 200 / 200`.
- Seed-37 state digest: `2c384137b5f18771e80bbceb2654bd8a9376d553847a4d8c65b678753e5ebcb0`.
- Seed-37 trace digest: `f74db936f4af78489d3a2e20e97a1d8b992624f19d73fe83d42a2d2a79edcc07`.
- No producer artifact has been integrated into `main`.
- No independent review disposition is claimed by this handoff.

## Next action

After the terminal schema-3 `STATUS(REVIEW_READY)` records the exact final branch/work SHA, freeze this producer branch. `W2-REV-01` must independently critique the ordering/replay/contention evidence as part of the complete Wave 2 evidence packet. Do not merge this branch to `main` as a substitute for the declared review/synthesis/verification route.
