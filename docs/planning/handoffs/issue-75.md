# Issue #75 handoff — W2-ORDER-01

**Mission:** `W2-ORDER-01`  
**Branch:** `planning/issue-75`  
**Ownership generation:** Issue #75 comment `5262599148`  
**Base main:** `21181eb20302a20d81aaec7b81a84acd4fcbbab8`  
**Authoritative foundation blob:** `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Evidence report blob:** `1e9ceba1eb97b4c85d78464109da34c0c4ae0946`  
**State intended after terminal capsule:** `REVIEW_READY`  
**Required review:** `W2-REV-01`

## Completed work

Produced `docs/planning/wave-2/evidence/ordering-replay-experiment.md` from the bounded authoritative packet.

The retained standard-library experiment covers a 1,154-event / 12-domain causal graph, 110 explicit cross-domain synchronization events, 28 simultaneous noncommuting conflicts, 200 seeded interleavings per policy, exact replay of one retained trace, and a 1/2/4-process contention benchmark from 0% through 100% shared synchronization.

Producer self-review corrected two evidence-quality issues before terminalization:

1. seeded ready-frontier handling was normalized so traces do not depend on Python set/hash iteration;
2. the benchmark now uses exact per-100 synchronization quotas rather than approximating 30% as every third event.

The corrected embedded harness was syntax-checked; its exact 200-seed correctness/replay path was rerun successfully; the corrected timed matrix was rerun with seven attempts per cell.

## Material findings

1. `causal_local`: `1 final state / 200 linear traces / 1 conflict order`.
2. `global_total`: `1 / 1 / 1`, with the same final state as `causal_local`.
3. `arrival_tied`: `200 / 200 / 200`; causal readiness alone is insufficient for simultaneous noncommuting shared-domain effects.
4. Causal/local seed 37 replay reproduced exact state, trace, and conflict digests.
5. Corrected 4-process throughput versus global-ticket baseline: `9.95x` at 1% sync, `8.74x` at 10%, `3.57x` at 30%, `0.96x` at 100%.
6. Bounded recommendation: carry domain-local/causal ordering as the default planning candidate only when touched domains/dependencies are explicit and shared conflicts have stable arbitration; retain stronger total order for bounded scopes whose audit/correctness requirement or measured contention justifies it.

## Scope limits / open work

This is a `BOUNDED_PASS` only for the experiment-local ordering claim. It does not select a production scheduler, engine/runtime, tick rate, thread/network model, domain granularity, canonical semantic encoding/hash, or implementation architecture. The Python benchmark is a coordination-topology probe, not a production capacity forecast.

The fixture assumes complete touched-domain declarations and disjoint-domain commutativity. Hidden shared state, undeclared touches, changed rules/content, tie-break collisions, near-global real contention, or a single-linear-audit requirement reopen the result.

W2-HASH-01 retains cross-runtime semantic-hash authority. W2-SIM-01 must establish model/shared-kernel parity independently after its other prerequisites. Production implementation remains blocked.

## Checks/evidence

- Base/claim SHA: `21181eb20302a20d81aaec7b81a84acd4fcbbab8`.
- Foundation blob: `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`.
- Corrected evidence blob: `1e9ceba1eb97b4c85d78464109da34c0c4ae0946`.
- Seed-37 state digest: `2c384137b5f18771e80bbceb2654bd8a9376d553847a4d8c65b678753e5ebcb0`.
- Seed-37 trace digest: `f74db936f4af78489d3a2e20e97a1d8b992624f19d73fe83d42a2d2a79edcc07`.
- Seed-37 conflict digest: `e2f69c3695d82ca59731a0f3d09db6aee8fa30e7c05b93c2e3559be067e0aba2`.
- No producer artifact has been integrated into `main`.
- No independent review disposition is claimed.

## Next action

After terminal schema-3 `STATUS(REVIEW_READY)` binds the exact final branch/work SHA, freeze this branch. `W2-REV-01` must independently critique the ordering/replay/contention evidence. Do not merge this producer branch to `main` as a substitute for the declared review/synthesis/verification route.
