# W2-GAME-EV-REM-02 — core-game evidence remediation v3

## Scope and lineage

This packet is bounded fictional-game planning evidence for Issue #217. It consumes immutable Issue #210 head `b387a7f27733b52daa0d36f40d2e066041ae90b0` and Issue #212 review artifact `fc3c32abf038e2a90b44495b43c012eb1196039f`. It does not edit historical Issue #197 or #210 bytes.

Only six IDs are rerun: `GDF-E2`, `GDF-E4`, `EPA-E3`, `EPA-E7`, `AGE-E3`, `AGE-E4`. The unaffected v2 IDs `GDF-E1`, `GDF-E3`, `EPA-E1`, `EPA-E2`, `EPA-E4`, `EPA-E5` retain exact Issue #210 result identity `c57be3ef32cb2b915aa736d4c007e671e42680b6` without rerun or status upgrade.

## Exact v3 evidence

- Policy/search evidence: `core-game-policy-search-v3.json`, blob `fa02ab4c13b247bc2df954db8b0c9ef74a9e84d9`.
- Progression/transition evidence: `core-game-progression-exploit-v3.json`, blob `39d5deab192cf49a41566e5cfc70f5a658296b22`.
- Automation choice evidence: `core-game-automation-decisions-v3.json`, blob `50f64d428a5261e9b319acb51b30ccbce0c34a39`.
- Normalized affected results: `core-game-results-v3.json`, blob `b901850128c0aaad84f3ddb5679108a13dc60088`.
- Producer review-finding dispositions: `w2-rev-03-dispositions.md`, blob `cc81441aa34cdd535ee92a3b16b2ee8dcd62d0af`.

## M01 correction: generated behavior and search

The v3 policy artifact defines one exact fictional action/state model and four distinct deterministic behavior rules. Scripted, bounded-rational/noisy, joint-objective search, and seeded fuzz classes each generate a retained trace from their declared rule; none is merely a label assigned to a fixed Issue #210 lifestyle trace.

For the search-dependent predicates, every feasible sequence is retained conceptually under one closed enumeration rule: breadth by depth, stable action order, nonnegative stock state, depth 4. The complete feasible frontier counts reproduce as `7`, `49`, `339`, `2327`. Five independent/joint objective winners are explicit and materially different; no one generated route wins all objectives, and every winner has a declared gap on another objective. This is the evidence consumed by rerun `GDF-E2` and `EPA-E3`.

`AGE-E3` consumes the four versioned behavior rules and their exact generated traces rather than primary-family labels.

## M02 correction: closed progression and transition enumeration

The v3 progression object replaces prose requirements with a closed `requires_all` symbol grammar. Mutations are exact operations against exact node fields. The validator order is fixed: symbol validation, cycle detection, fixed-point reachability, required-goal report. The missing-symbol, cycle, and path-loss cases are therefore derivable from retained objects without inventing transformation semantics. This is the evidence consumed by rerun `EPA-E7`.

The same artifact defines a bounded fictional transition system with exact state fields, action preconditions/effects, stable action order, and full breadth-first enumeration through depth 3. Complete frontier counts reproduce as `4`, `16`, `63`; retained first findings come from generated sequences rather than supplied classification rows. This is the evidence consumed by rerun `AGE-E4`.

## M03 correction: named choice surfaces

The v3 automation artifact keeps the exact Issue #210 payback sweep immutable and adds the missing semantic layer. Manual exposes `allocation`; partial exposes `allocation`, `configuration`, `logistics`; strong exposes those three plus `expansion` and `quality`. Every surface has two distinct fictional choices with declared state deltas, and each higher tier is a strict superset. This is the evidence consumed by rerun `GDF-E4`.

## Result normalization

The producer result object reports all six affected reruns as PASS against these bounded fictional-game predicates. That is not an independent review disposition. Full-tranche review authority remains `PENDING_FRESH_AGGREGATE_REVIEW`; `IR-BLOCKER-GAME-EVIDENCE` remains OPEN.

Human preference/fun remains out of scope. This packet creates no gameplay or production implementation authority, engine selection, release approval, readiness completion, verification PASS, legal/provider authority, or canonical status.

## Required next gate

Exactly one fresh aggregate review of the exact terminal Issue #217 packet. The Issue #212 reviewer episode may not self-adjudicate this producer remediation. If that review is clean, later synthesis/readiness work may consume the reviewed evidence; producer output alone cannot resolve the blocker.
