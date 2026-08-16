# W2-ENG-TECH-S6-REM-01 — capture-byte / capture-down remediation

## Scope

This successor remediates only required-review findings `W2-ENG-TECH-S6-REV-M01` and `W2-ENG-TECH-S6-REV-M02` from Issue #458. Producer Issue #456 / PR #457 and review Issue #458 / PR #459 remain immutable provenance.

The execution scope is Godot 4.7.1-stable only. Bevy and Defold remain `INCONCLUSIVE_HARNESS_OR_INFRA`; Unity and Unreal remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`.

## M01 correction

N1 and N2 use distinct candidate-visible attempt markers rendered by Godot itself. The resulting actual PNG bytes are retained under the remediation evidence directory and uploaded in the immutable Actions artifact. The independent verifier reopens those bytes, hashes and decodes them, validates 1280×720 and the expected attempt-specific marker pixels, and performs an actual-byte substitution attack by replacing N2 with N1 bytes while recomputing byte-hash/binding metadata. Trust requires the substituted object still to fail because its rendered N2 marker is wrong.

## M02 correction

FI1 keeps the exact candidate-generated `CAPTURE-STATE-042` state and live Godot process on the real X display while invoking the same `scrot` capture program against deliberately nonexistent display `:199`. The evidence retains the actual invoked command/environment, observed nonzero exit/error, timeout flag, and output-path absence. `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE` is accepted only from these observed facts.

## Authority

Fresh remediation evidence remains untrusted until a fresh required review. It grants no engine ranking/selection, implementation/readiness, provider/commercial/legal/platform/release, verification-PASS, integration, decision, or canonical authority.

Final run, generation, artifact and digest identities are recorded after Actions execution.
