# Issue #1091 handoff

## Mission
`W2-CONTENT-NARR-CONT-02-REM-01` — bounded remediation of Review #1088 finding `W2-CONTENT-NARR-CONT-02-REV-MIN01`.

## Ownership and basis
- claim comment: `5659129051`
- actor session: `frontier-remediate-narr-cont02-1091-gpt56sol-20260914-01`
- branch: `planning/issue-1091`
- branch base: `main@13272159e2d4c9921aeb410a0a85cb470eaa23d7`
- source producer: Issue #1052 / PR #1090
- source producer terminal: `5659029610`
- source exact head: `1dde50f577087ccf4aa5edfac9b3fa1ca11815ff`
- source Markdown blob: `3ef5829ad1fcf7d554a55b6fb1a9ca94fa65721f`
- source YAML blob: `5093e4a1d1d149d21afc0690a352a051e4319aa3`
- source review: Issue #1088 terminal `5659090077`, `CHANGES_NEEDED`

## Exact correction
Only the reviewed predecessor world-interface bounds were restored.

The corrected Markdown now states the exact inherited bounds for:
- `WORLD_ROLE:CONT_CONTESTED_SITE`: exactly three reviewed target interfaces;
- `WORLD_ROLE:CONT_HISTORY_OR_EVIDENCE_SOURCE`: exactly `WORLD_IFACE:HISTORY-TRACE`;
- `WORLD_ROLE:CONT_AFTERMATH_SURFACE`: exactly six reviewed target interfaces.

The corrected YAML now carries the same exact bindings under `provisional_interfaces.reviewed_world_bindings`, marks each as non-widening, and qualifies `OPEN:NARR-CONT02:WORLD_SURFACE_SELECTION` so any downstream selection must remain within the reviewed target sets.

No target was selected, added, or removed.

## Corrected blobs before handoff commit
- Markdown: `9cdeb595f9690eb65f3df974e182218364612ea6`
- YAML: `a8d51364fabf553db37f1b30f3545e673a8babc0`

## Frozen non-finding semantics
Unchanged from source producer:
- one bounded structural arc / three quest-family stages;
- route-cardinality minima, pre-activation underflow, and recovery recomputation;
- deny-by-default optional private context;
- refusal/rejection and legal-recovery semantics;
- consequence, persistence/history, and `BranchImpactEvidence` obligations;
- zero foundational gates and baseline-play legality;
- exact WSN E3/E4/E5/E8 states;
- no exact time/schedule/travel/weather/reachability assertions;
- no sibling CONT-02 mutable consumption;
- engine neutrality and all higher-authority denials.

## Review and downstream
This remediation does not grant `W2-CONTENT-NARR-CONT-02_REVIEWED`. A fresh required remediation review must judge the exact corrected packet before any narrative CONT-02 token exists.

No integration, verification-PASS, implementation/readiness, engine-selection, release, decision, final-canon, or canonical authority is granted.
