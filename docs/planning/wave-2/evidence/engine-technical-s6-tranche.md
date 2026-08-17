# W2-ENG-TECH-S6-REM-01 — S6 byte-binding and capture-down remediation

## Scope and frozen provenance

Issue #585 is the exact bounded blocking-remediation successor required by terminal review Issue #458. It preserves producer Issue #456 / PR #457 at terminal head `0719199237d3ac46505f52a06df0a0fc93429c9f` and review Issue #458 / PR #459 at review head `d2e7c34e583eedd2b2d5c4b02c8969e581b80563` as immutable provenance. The only routed findings are `W2-ENG-TECH-S6-REV-M01` and `W2-ENG-TECH-S6-REV-M02`.

The fixed S6 contract remains unchanged: state marker `CAPTURE-STATE-042`, injection `FI-S6-CAPTURE-DOWN-v2`, viewport 1280×720, three distinguishable screen regions, one retained capture frame per normal attempt, and common resource `W2-ENG-HOST-COMMON-v2`.

## Final fresh evidence packet

- final trigger: `3835b5ebae6340aa4137c0c0453b39a7e31bf059`
- Actions run: `32029396638`, attempt 1, success
- generated evidence commit: `20d64d023c46e18b72d876d10edd10e44594de37`
- immutable artifact: `9288296812`, `w2-eng-tech-s6-rem-01-32029396638-1`
- artifact digest: `sha256:7868a7d499a070bd65b56478384a8eb739d0ccc9a61f5ec9c7a73dd4c650ec1e`
- remediation evidence SHA-256: `9f115927f95102c37c60ff7125de843b7cdde1b680276a111ece854c274339e4`
- independent-verification SHA-256: `10abd799a04c198de845ba2e47eac06e1473cce4bb8705e6eae255d83f50b02c`
- Godot generation: `GEN-S6-REM-47e2192acf40054ae5a3`
- Godot executable SHA-256: `32f8d7596c4b41185512b1c49d69f2da3be018fd784a53e349fa92a98a97bcde`
- candidate project SHA-256: `325092562ce35b7499de0f4e718551323e182c9a92f1aae34cac6bb6d428fdf4`

The run identity binds the exact probe SHA-256 `6ca7560c7931ac3808acd866e20d4596d6ffda8a95dc1709c89530b5e611f903`, verifier SHA-256 `21c070ac6e2cc457b916696765265e0156e83aba03a87b9f2ea556ac03dd0d8a`, unchanged-v5 fixture SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`, and toolchain artifact-lock SHA-256 `23f71143c3771df2f438b899a7a948e58da93bc15a3defe9cf3fb5e2b9147daf`.

## M01 — byte-bearing capture identity

Both trusted normal attempts retain the actual candidate-bound X11 framebuffer PNG bytes in the immutable artifact and repository evidence packet:

- N1: `frames/godot-N1.png`, 1280×720 PNG, 4380 bytes, rendered marker RGB `[255,255,0]`, byte SHA-256 `ec2083126dba2bdb96929bfd4306485ad52116d4dc1c7be8b00fb90d0955056b`, Git blob `d3630234dc52e14a8d96cd3085ef1e23c4634bc2`, binding SHA-256 `a14de7a515fc2c4064ca4e28ec152d901f98721ba6807e017369a743892bcee7`.
- N2: `frames/godot-N2.png`, 1280×720 PNG, 4380 bytes, rendered marker RGB `[255,0,255]`, byte SHA-256 `54119fd58b7f625b3b739113bd20fa50c503aed486b84f51885b97a61dfd1b7b`, Git blob `4782c5b407c4cdb426dcb5f7d8f9ae427a7e8bdd`, binding SHA-256 `9cc3d45f7c0354bc08c3b01b9a60e01adec3d4a8a0134e86d8b4ede8b0c42b54`.

The per-attempt marker is candidate-rendered and mechanically sampled from the retained pixels. N1 and N2 frame bytes differ. The independent verifier physically substitutes retained N1 bytes into the N2 validation context and rejects them; it also rejects a missing frame and a byte-tampered frame. The capture binding is fail-closed over candidate, generation, attempt, run, state, project identity, executable identity, capture metadata and byte SHA-256.

## M02 — observed capture-pipeline failure

FI1 reaches exact state `CAPTURE-STATE-042|Godot|GEN-S6-REM-47e2192acf40054ae5a3|FI1|00FFFF|1280x720` while the candidate process is independently observed alive. The same real capture mechanism used by normal attempts executes `/usr/bin/scrot -z /proc/everfield-s6-capture-down.png` under `FI-S6-CAPTURE-DOWN-v2`.

The observed result is exit 1, zero frames, no output path, and stderr `scrot: Saving to file /proc/everfield-s6-capture-down.png failed`. The retained and independently checked classification is exactly `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`; relabelling as a state/reachability failure is rejected. FI1 binding SHA-256 is `0195ad3af236df09e2e68701757e216ad192884d158c34dca9b04c21b6535842`.

## Unchanged-v5 and preserved cells

The independent verifier recomputes unchanged-v5 adaptation `ACCEPT`, adaptation identity `25d0ead1111ff8ef214a622286f71baa86ba127a13a65ca7c674cdcc2128f713`, binding ID `da9e08a47340186dcab7d9fc62380b64ee580c0d7f39d2005aa3f83c30276476`, and aggregate exactly `PASS_FOR_COMPARISON` with `valid_envelope=true` and no reasons.

Bevy and Defold remain exactly `INCONCLUSIVE_HARNESS_OR_INFRA`. Unity and Unreal Engine remain exactly `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. The 50 historical Issue #82 `NOT_RUN` cells remain preserved. Reviewed S3/S4/S5 evidence and the unchanged-v5 authority model are not mutated.

## Failed and superseded run provenance

- `32028633928` / artifact `9288014144`: non-authoritative construction failure before trusted evidence; Godot tool workspace parent absent.
- `32028886604` / artifact `9288113231`: non-authoritative construction failure before trusted evidence; attempt-workspace parent absent.
- `32029026514` / artifact `9288167999`, digest `sha256:ccf1eb1dab132761db5f7eeb3e90f5cbcfaa2e4049ede7ce2a4be0f719206a0c`: green but superseded by explicit fail-closed FI-classification tightening.
- `32029326533`: green intermediate classification run, superseded by the final workflow assertion packet `32029396638`.

The original producer predecessor `31967222552` / artifact `9268882622` and reviewed producer run `31967674130` / artifact `9268994399` remain immutable non-final provenance for this remediation episode.

## Disposition and authority

Producer disposition is `PROVISIONAL_S6_REMEDIATED_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW`. The remediation packet is `NOT_CANONICAL` and is not trusted comparison authority until exactly one fresh required independent/degraded-independent review of the exact terminal remediation packet completes.

Draft PR #587 is the review surface. This task grants no integration, engine ranking/selection, gameplay/high-throughput implementation, implementation or production readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision, or canonical authority. Any later integration requires separate repository authority and, if authorized, squash-only integration into `main`.