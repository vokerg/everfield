# Issue 585 handoff — W2-ENG-TECH-S6-REM-01

## Terminal candidate

- issue: #585
- mission: `W2-ENG-TECH-S6-REM-01`
- task class: `BLOCKING_REMEDIATION`
- branch: `planning/issue-585`
- winning claim: `5315719466`
- base: `330c9f5b02d05b830eab7647fa552a3812e3f9c9`
- draft PR: #587
- terminal head: the commit containing this handoff and the synchronized S6 remediation report; bind its exact SHA from the terminal schema-3 status on Issue #585 / PR #587 head.
- canonical binding comment: `5245368879`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- canonicality: `NOT_CANONICAL`

## Frozen provenance

Producer #456 / PR #457 remains immutable at `0719199237d3ac46505f52a06df0a0fc93429c9f`, terminal comment `5309296967`. Required review #458 / PR #459 remains immutable at `d2e7c34e583eedd2b2d5c4b02c8969e581b80563`, terminal comment `5309336848`, disposition `CHANGES_NEEDED`, findings `W2-ENG-TECH-S6-REV-M01` and `W2-ENG-TECH-S6-REV-M02`.

## Final evidence to review

- trigger: `3835b5ebae6340aa4137c0c0453b39a7e31bf059`
- Actions run: `32029396638`, attempt 1, success
- generated evidence commit: `20d64d023c46e18b72d876d10edd10e44594de37`
- artifact: `9288296812`
- artifact digest: `sha256:7868a7d499a070bd65b56478384a8eb739d0ccc9a61f5ec9c7a73dd4c650ec1e`
- remediation JSON SHA-256: `9f115927f95102c37c60ff7125de843b7cdde1b680276a111ece854c274339e4`
- independent verifier JSON SHA-256: `10abd799a04c198de845ba2e47eac06e1473cce4bb8705e6eae255d83f50b02c`
- generation: `GEN-S6-REM-47e2192acf40054ae5a3`

### M01 packet

N1 retained PNG: `frames/godot-N1.png`, SHA-256 `ec2083126dba2bdb96929bfd4306485ad52116d4dc1c7be8b00fb90d0955056b`, Git blob `d3630234dc52e14a8d96cd3085ef1e23c4634bc2`, marker RGB `[255,255,0]`.

N2 retained PNG: `frames/godot-N2.png`, SHA-256 `54119fd58b7f625b3b739113bd20fa50c503aed486b84f51885b97a61dfd1b7b`, Git blob `4782c5b407c4cdb426dcb5f7d8f9ae427a7e8bdd`, marker RGB `[255,0,255]`.

Both are 1280×720 PNGs, 4380 bytes, retained in the immutable artifact and repository evidence. The independent verifier confirms actual-byte N1→N2 substitution rejection, missing-frame rejection, tampered-frame rejection, byte distinctness and capture-binding recomputation.

### M02 packet

FI1 independently reaches `CAPTURE-STATE-042` with the Godot candidate alive, then actually executes `/usr/bin/scrot -z /proc/everfield-s6-capture-down.png`. Observed exit is 1, zero retained frames, no output path, with real scrot write-failure stderr. Exact retained classification is `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`; the verifier enforces that classification and rejects relabelling as a reachability failure.

### Unchanged-v5 and preservation

Independent verification is `ok=true`, reasons empty. Unchanged-v5 adaptation recomputes `ACCEPT`; aggregate is exactly `PASS_FOR_COMPARISON`, `valid_envelope=true`. Bevy/Defold remain `INCONCLUSIVE_HARNESS_OR_INFRA`; Unity/Unreal Engine remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`; the 50 Issue #82 historical `NOT_RUN` cells remain unchanged.

## Retained non-authoritative run provenance

- `32028633928` / artifact `9288014144`: construction failure before trusted evidence.
- `32028886604` / artifact `9288113231`: construction failure before trusted evidence.
- `32029026514` / artifact `9288167999`: green but superseded before final exact FI-classification enforcement.
- `32029326533`: green intermediate run, superseded by final `32029396638`.
- producer predecessor `31967222552` / artifact `9268882622` remains non-authoritative provenance.

## Required next route

Exactly one fresh required independent/degraded-independent S6 remediation review must inspect the exact terminal PR #587 head. The reviewer must independently recompute retained PNG byte identities/dimensions/markers, attack actual-byte cross-attempt reuse, check missing/tampered objects fail closed, verify the attempt marker is candidate-rendered, prove the real scrot failure executed while state remained reachable and candidate alive, enforce exact FI classification, recheck unchanged-v5 adaptation/aggregate, preserve blocked/inconclusive cells, and reject authority inflation.

No optional review may substitute for that required review.

## Authority boundary

This handoff is `REVIEW_READY` evidence only. It grants no integration authority, engine selection, gameplay/high-throughput implementation, implementation/readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision or canonical authority. If a later reviewed terminal route explicitly grants integration authority, integration into `main` must be squash-only.