# Issue 591 handoff — W2-ENG-TECH-S6-REM-02

## Terminal candidate

- issue: #591
- mission: `W2-ENG-TECH-S6-REM-02`
- task class: `BLOCKING_REMEDIATION`
- branch: `planning/issue-591`
- winning claim: `5317388619`
- base: `85974cc21f1e3c5c3f189fa6da573a11dc381efb`
- draft PR: #594
- terminal head: the commit containing this handoff and the synchronized S6 remediation tranche; bind its exact SHA from the terminal schema-3 status on Issue #591 / PR #594 head.
- canonical binding comment: `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- canonicality: `NOT_CANONICAL`

## Frozen provenance

Remediation #585 / PR #587 remains immutable at `917866be1655223ebfc3166a7e1949db738f1ff7`, final run `32029396638`, artifact `9288296812`. Required review #588 / PR #589 remains immutable at `ec08f8f9a693b1bd67e6715bb28b1582afb37b8b`, terminal comment `5317382782`, disposition `CHANGES_NEEDED`, finding `W2-ENG-TECH-S6-REM-REV-M01`.

The prior findings `W2-ENG-TECH-S6-REV-M01` and `W2-ENG-TECH-S6-REV-M02` stay materially closed. This successor addresses only the formal v5 reconstruction/independent aggregation finding and does not reopen the clean PNG or real capture-down corrections.

## Final evidence to review

- trigger: `020b4b9e05d26ff551c229d0b274751cd7995ff0`
- Actions run: `32043481976`, attempt 1, success
- generated evidence commit: `4d54ba0ba00c09890e03d1fe10d2c08d1657069f`
- artifact: `9292381852`
- artifact digest: `sha256:d7b2785e47b2bf8c86356d33439a22bbc4befe90d5ea8b6130fff3830cedecb4`
- remediation JSON SHA-256: `383e6ebb1031260564d605fa7d746e83ebe86cc66982ae7de8741175c73952cb`
- independent verifier JSON SHA-256: `78b533d8cb9d990ffaadedf596591fb83ad3f88f2a2a7b3db7de72f05f61bee9`
- generation: `GEN-S6-REM2-2a8d597ef60acfb220e2`

N1 retained PNG SHA-256 remains `ec2083126dba2bdb96929bfd4306485ad52116d4dc1c7be8b00fb90d0955056b`; N2 remains `54119fd58b7f625b3b739113bd20fa50c503aed486b84f51885b97a61dfd1b7b`. Both remain 1280×720, byte-distinct, candidate-rendered captures. FI1 still executes the real failing scrot command with state reachable and candidate alive and retains exact class `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`.

For each N1/N2/FI1 attempt, the retained packet now records an absent-before / empty-after-create reset body with filesystem identity, an observed candidate `/proc/<pid>/cwd` workspace body with project-file hashes, and derived reset/workspace IDs. Those exact IDs populate the canonical v5 AttemptRecords retained inside the complete generation object. Each formal AttemptRecord is independently hash-bound to its actual capture binding and reset/workspace evidence.

The independent verifier reports `ok=true`, adaptation `ACCEPT`, and independently recomputes canonical v5 `agg()` to exactly `PASS_FOR_COMPARISON`, reasons empty, `valid_envelope=true`. It also proves fail-closed behavior for reused/unverified normal resets, reused normal workspace, duplicate/mismatched run registry, duplicate/mismatched all-attempt registry, candidate/generation AttemptRecord tampering, and formal-to-actual binding substitution. Existing byte substitution/missing/tampered-frame/capture-down controls remain green.

Bevy and Defold remain `INCONCLUSIVE_HARNESS_OR_INFRA`; Unity and Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`; historical Issue #82 50 `NOT_RUN` cells remain unchanged.

## Required next route

Exactly one fresh required independent/degraded-independent review must inspect the exact terminal PR #594 head. It must independently verify the immutable artifact/run/head identities; recompute the retained reset/workspace/formal-link hashes; prove the full retained canonical generation and registries correspond to actual N1/N2/FI1 evidence; call canonical v5 `agg()` itself; rerun or reconstruct the listed negative controls; confirm the clean PNG and real capture-down behavior remains intact; preserve blocked/inconclusive cells; and reject authority inflation.

No optional review may substitute for this required review.

## Authority boundary

This handoff is `REVIEW_READY` evidence only. It grants no integration authority, engine selection, gameplay/high-throughput implementation, implementation/readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision, or canonical authority. If a later reviewed terminal route explicitly grants integration authority, integration into `main` must be squash-only.
