# Everfield Selected Engine — Godot 4.7.1-stable

## Record identity

- record class: `FORMAL_ENGINE_SELECTION`
- selected engine: **Godot `4.7.1-stable`**
- selection status: `SELECTED`
- canonical publication rule: `CANONICAL_ONLY_WHEN_AUTHORIZED_RECORD_IS_SQUASH_PUBLISHED_TO_MAIN`
- implementation ready: **false**
- gameplay/high-throughput implementation authorized: **false**

This record is the bounded formal engine-selection outcome authorized by the repository owner. On a task branch or draft PR it is noncanonical publication material. Its selected-engine authority becomes canonical only when this exact record is squash-published to `main` through the authorized Issue #1028 continuation.

## Authority chain

The selection is not inferred from recommendation strength or PR state. It is bound to this exact reviewed and authorized chain:

1. Issue #804 terminal comment `5521287905` — disposition `ENGINE_SELECTION_READY_FOR_CANONICAL_DECISION`, recommendation Godot `4.7.1-stable`, exact producer head `456043100eddc3de20b18f2a29e889c8c64fb90f`.
2. Required Review #832 terminal comment `5536194396` — disposition `CLEAN_FOR_FORMAL_ENGINE_DECISION_GATE`, with zero BLOCKER, zero MAJOR, and zero correction-requiring MINOR findings.
3. Review provenance publication #846 terminal comment `5536290922` — preserves the clean review without granting selection by itself.
4. Formal gate #895 terminal comment `5580950990` — identified the sole missing predicate as `EXPLICIT_CURRENT_REPOSITORY_AUTHORITY_PERMITS_RECORDING_GODOT_4_7_1_STABLE_AS_SELECTED_ENGINE`.
5. Issue #919 owner authority comment `5651198366` — explicitly selects Godot `4.7.1-stable`, authorizes publication of this selected-engine record to `main`, and declares the record canonical upon that authorized publication under the active canonical planning binding.
6. Issue #1028 — the fresh formal decision continuation that performs only that bounded publication.

Canonical Planning Program v1 remains bound by Issue #6 comment `5245368879`, program blob `e3120ec203c4156328770aa86c12fbb7187966dc`, activation SHA `413e729e8d2d5ac2eb138903f3f2ace07283b23e`.

## Decision

Everfield's selected engine is **Godot `4.7.1-stable`**.

The selection closes the engine-choice authority predicate. It does not retroactively convert incomplete or blocked Unity, Unreal, Bevy, Defold, provider, or comparison evidence into PASS, and it does not require reopening generic five-engine comparison work.

## Readiness separation

Engine selection and implementation readiness are separate authority predicates.

This record therefore preserves:

- `implementation_ready: false`;
- no gameplay/high-throughput implementation authorization;
- no provider or hosted-CI PASS created by selection;
- no `PASS_FOR_COMPARISON` created for any candidate;
- no aggregate verification PASS created by selection;
- no production, release, commercial, legal, or platform authority created by selection.

The next planning transition must independently establish implementation readiness under the canonical program before gameplay/high-throughput implementation can begin.

## Change control

A later change to the selected engine requires a new explicit repository authority basis plus the review/verification/canonical publication route then required by the active canonical planning program. Evidence debt or implementation findings may reopen the decision only through such an explicit route; they do not silently mutate this record.

## Publication invariant

Only the squash-published `main` copy is the canonical selected-engine record. Branch commits, draft PRs, comments other than the exact authority chain above, mergeability, or approvals do not independently create or expand canonical authority.
