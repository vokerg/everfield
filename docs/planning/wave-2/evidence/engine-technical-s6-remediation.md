# W2-ENG-TECH-S6-REM-01 — capture-byte / capture-down remediation

## Scope

This successor remediates only required-review findings `W2-ENG-TECH-S6-REV-M01` and `W2-ENG-TECH-S6-REV-M02` from Issue #458. Producer Issue #456 / PR #457 and review Issue #458 / PR #459 remain immutable provenance.

Execution scope is Godot 4.7.1-stable only. Bevy and Defold remain `INCONCLUSIVE_HARNESS_OR_INFRA`; Unity and Unreal remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`.

## Final empirical identity

- Trigger: `74ccb754b7453cad36a5b0a9007f1591674bd006`
- Actions run: `31968880106`, attempt 1, success
- Generated evidence commit: `be98ca238539ea4aaf1d8e085ec3a9970ed639be`
- Immutable artifact: `9269235928`, `w2-eng-tech-s6-rem-01-31968880106-1`
- Artifact digest: `sha256:1e731483c6d73c7a4c1f931bfc29cf1eb9d1c5b6b93b9646a25e9ee329d24362`
- Evidence SHA-256: `ffcd86bef441504dc93f65bc8ce4afaa1154448bb36eb68649d44f3909cc846c`
- Independent verification SHA-256: `6b07a0aa8620cd02e4f45ed335c7ab67ef70a70e89dbad880dd8fa9b82c7cd06`
- Fresh remediation generation: `GEN-S6R-682a8afad97938325c6f9f40`
- Unchanged-v5 aggregate: `PASS_FOR_COMPARISON`, `valid_envelope=true`

## M01 correction — retained capture bytes and actual-byte reuse rejection

Godot itself renders an attempt-specific marker into the player surface: N1 `E6CC1A`, N2 `E61ACC`. The actual 1280×720 PNGs are retained in the repository evidence packet and immutable Actions artifact:

- `frames/Godot/N1.png`: `32c2c6cce0898ec194ee00d75e6ec89eb5867df97a5852fb7fce69d549dbe34a`
- `frames/Godot/N2.png`: `8a3b0ba520f9c8577f5d510c97181f3e8449102b3729615b3a1c397f176dbf7b`

The independent verifier reopens the retained bytes, recomputes SHA-256, decodes dimensions/pixels, validates the expected marker plus three distinct player-surface panels, and confirms the two normal frame byte objects differ.

Its substitution attack copies the actual N1 PNG bytes into a synthetic N2 frame, then recomputes the substituted frame SHA, capture SHA, capture-binding body/digest and raw-attempt digest. The forged N2 object still fails because its candidate-rendered marker pixels are N1 (`E6CC1A`) rather than the independently derived N2 marker (`E61ACC`). `actual_byte_substitution_rejected=true`.

## M02 correction — mechanically observed capture-down failure

FI1 reaches exact candidate-generated `CAPTURE-STATE-042` with the exact three screen identities/routes while the Godot process remains alive on the real display. The same capture program used by normal attempts is then actually invoked against deliberately unavailable display `:199`:

- program: `/usr/bin/scrot`
- observed exit: `1`
- timed out: `false`
- output path exists: `false`
- frame count: `0`
- observed error: `scrot: Can't open X display. It *is* running, yeah? [:199]`

Only those observed failure facts plus the independent state/process facts produce `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`. The independent verifier also confirms a recomputed-metadata relabel to `STATE_REACHABILITY` fails closed: `fi_misclassification_rejected=true`.

## Independent verification

`W2-ENG-TECHNICAL-S6-REMEDIATION-INDEPENDENT-VERIFY-v1` reports:

- `all_remediation_invariants_verified=true`;
- candidate identity and fresh generation derivation valid;
- N1/N2 retained byte objects valid and byte-distinct;
- actual-byte substitution rejected;
- real capture-down failure valid;
- FI misclassification rejected;
- unchanged-v5 adaptation `ACCEPT`;
- recomputed aggregate `PASS_FOR_COMPARISON`, `valid_envelope=true`.

## Disposition and authority

Producer remediation disposition: `REMEDIATED_EMPIRICAL_S6_EVIDENCE_READY_FOR_REVIEW`.

This packet remains untrusted pending one fresh required independent/degraded-independent review of this exact remediation head/run/artifact/generation. It grants no engine ranking/selection, implementation/readiness, provider/commercial/legal/platform/release, verification-PASS, integration, decision, or canonical authority.
