# W2-ENG-TECH-S6-01 — identity-bound capture evidence tranche

## Scope

This packet is the bounded S6 continuation of the reviewed W2-ENG v5 evidence line. It tests only S6: reaching `CAPTURE-STATE-042`, producing an identity-bound candidate-render capture at 1280×720, and separating state reachability from capture-pipeline failure under `FI-S6-CAPTURE-DOWN-v2`.

## Method

Bevy 0.19.0, Defold 1.13.0, and Godot 4.7.1-stable reuse the reviewed public-toolchain acquisition path. Each attempt is reconstructed in a distinct workspace. A live candidate process renders three distinguishable player-surface panels, writes an exact candidate-generated state identity, remains alive while the X11 framebuffer is captured, and binds the retained frame digest to candidate generation, attempt, project, executable, state, viewport, and run identity.

The framebuffer capture is recorded as `CANDIDATE_BOUND_X11_FRAMEBUFFER`: environment plumbing around a live candidate-rendered surface, not engine-native screenshot authority. Python does not generate the image.

For the required failure injection, the candidate state channel remains exact while the capture channel is deliberately unavailable. The injection is accepted only as `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`.

## Final empirical packet

- final trigger SHA: `b744552663d8dbaf4b8fa27b250ff6507dffe7d8`
- Actions run: `31967674130`, attempt 1, success
- generated evidence commit: `e791ab071727a0833e08dd939b8a0cd2e589e926`
- immutable artifact: `9268994399`
- artifact name: `w2-eng-tech-s6-01-31967674130-1`
- artifact digest: `sha256:da5db6666e1297ec210bcb9d0db6849925421209dee3497346c08de577650fa5`
- evidence SHA-256: `f14b961ce316e0796b3f17753e15d91fc943f79b721db17e5adb58f324521887`
- independent verification SHA-256: `63db2aa4d01586accb9d8f4497fd289727c97e4e82a0491466ab290bb821067d`
- independent verifier: `W2-ENG-TECHNICAL-S6-INDEPENDENT-VERIFY-v1`, `all_provisional_verified=true`

Final producer disposition is `PARTIAL_EMPIRICAL_S6_EVIDENCE_READY_FOR_REVIEW`:

- Godot 4.7.1-stable: `PROVISIONAL_S6_PASS_FOR_COMPARISON_PENDING_REQUIRED_REVIEW`, generation `GEN-S6-8665917a0eb4a88a0e0f2f16`, work `WORK-S6-c51872e5cd4afb8893878dfd`; N1/N2/FI1 PASS, exact binding verification PASS, aggregate exactly `PASS_FOR_COMPARISON`, all producer negative controls PASS, and the independent verifier recomputed the packet cleanly.
- Bevy 0.19.0: `INCONCLUSIVE_HARNESS_OR_INFRA`; all three attempts remained inconclusive because the Bevy build failed before candidate launch (`wayland-sys` host dependency discovery), so no S6 result is promoted for Bevy.
- Defold 1.13.0: `INCONCLUSIVE_HARNESS_OR_INFRA`; the debug bundle built, but the candidate exited before writing the S6 state marker in each attempt, so no S6 result is promoted for Defold.
- Unity: exact `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`; provider state remains `BLOCKED_BY_SPECIFIC_EXTERNAL_CONDITION:UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED`.
- Unreal Engine: exact `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`; provider state remains `NOT_CONFIGURED:UNREAL_GITHUB_USERNAME_AND_TOKEN_NOT_CONFIGURED`.

## Retained producer defect provenance

Run `31967222552` / artifact `9268882622` is retained incomplete producer provenance. Godot already had a valid bound S6 aggregate, but the producer `capture_reuse_substitution_rejected` negative control reused the N1 pixel digest in N2; because the deterministic frames were byte-identical, the attack made no mutation and the envelope correctly stayed non-terminal. The bounded correction at `b744552663d8dbaf4b8fa27b250ff6507dffe7d8` substitutes the prior attempt's full capture binding instead, which is candidate/attempt identity-sensitive and is rejected fail-closed. The final run is the only producer packet eligible for fresh required review.

Bevy and Defold remain explicit inconclusive producer cells; they are not silently converted into passes, failures of the product, or authority blockers for the lawfully bounded Godot S6 packet.

## Preserved provenance / limits

Reviewed S3/S4/S5 provenance is preserved. The 50 historical Issue #82 `NOT_RUN` cells remain preserved. This tranche does not mutate the v5 validator, harness contract, feature slice, scenario manifest, or provider authority state.

## Authority

The producer packet is untrusted until fresh required independent/degraded-independent review. It grants no engine ranking/selection, gameplay or high-throughput implementation/readiness, Unity/Unreal unlock, provider/commercial/legal/platform/release authority, verification-PASS, integration, decision, or canonical authority. Any later publication to `main` requires separate authority and squash-only integration.
