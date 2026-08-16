# W2-ENG-TECH-S6-01 — identity-bound capture evidence tranche

## Scope

This packet is the bounded S6 continuation of the reviewed W2-ENG v5 evidence line. It tests only S6: reaching `CAPTURE-STATE-042`, producing an identity-bound candidate-render capture at 1280×720, and separating state reachability from capture-pipeline failure under `FI-S6-CAPTURE-DOWN-v2`.

## Method

Bevy 0.19.0, Defold 1.13.0, and Godot 4.7.1-stable reuse the reviewed public-toolchain acquisition path. Each attempt is reconstructed in a distinct workspace. A live candidate process renders three distinguishable player-surface panels, writes an exact candidate-generated state identity, remains alive while the X11 framebuffer is captured, and binds the retained frame digest to candidate generation, attempt, project, executable, state, viewport, and run identity.

The framebuffer capture is recorded as `CANDIDATE_BOUND_X11_FRAMEBUFFER`: environment plumbing around a live candidate-rendered surface, not engine-native screenshot authority. Python does not generate the image.

For the required failure injection, the candidate state channel remains exact while the capture channel is deliberately unavailable. The injection is accepted only as `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`.

## Authority

The producer packet is untrusted until fresh required independent/degraded-independent review. It grants no engine ranking/selection, gameplay or high-throughput implementation/readiness, Unity/Unreal unlock, provider/commercial/legal/platform/release authority, verification-PASS, integration, decision, or canonical authority.

Final empirical identities and dispositions are recorded after the Actions execution.
