# W2-ENG-TECH-S6-REM-REV-01 — required review of S6 capture remediation

## Scope and trust mode

This is the fresh required review of exact remediation Issue #460 / PR #461 at judged head `0c6e11721f92794e9977e4b1a377c2e5b9cec8e5`. Review ownership is Issue #462, claim `5309429827`, reviewer session `frontier-drain-s6-rem-review-gpt56sol-20260816-01`.

Trust mode is `DEGRADED_SINGLE_AGENT`: the reviewer episode is distinct from remediation session `frontier-drain-s6-rem-gpt56sol-20260816-01`, but no stronger independent agent isolation is claimed.

Canonical authority remains Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`. This review is `NOT_CANONICAL` and grants no integration authority by itself.

## Frozen judged identity

The review froze and checked:

- remediation Issue #460, claim `5309348003`, terminal `5309373000`;
- judged branch `planning/issue-460`, exact head `0c6e11721f92794e9977e4b1a377c2e5b9cec8e5`;
- draft PR #461, exact head `0c6e11721f92794e9977e4b1a377c2e5b9cec8e5`, base `886438990ed395cde2fad0ee6cb98ca6ade0f26f`, mergeable/clean when reviewed;
- trigger `74ccb754b7453cad36a5b0a9007f1591674bd006`;
- Actions run `31968880106`, attempt 1, `success`, on `planning/issue-460`;
- generated evidence commit `be98ca238539ea4aaf1d8e085ec3a9970ed639be`;
- artifact `9269235928`, `w2-eng-tech-s6-rem-01-31968880106-1`;
- recorded artifact SHA-256 `1e731483c6d73c7a4c1f931bfc29cf1eb9d1c5b6b93b9646a25e9ee329d24362`;
- evidence SHA-256 `ffcd86bef441504dc93f65bc8ce4afaa1154448bb36eb68649d44f3909cc846c`;
- independent-verification SHA-256 `6b07a0aa8620cd02e4f45ed335c7ab67ef70a70e89dbad880dd8fa9b82c7cd06`;
- remediation generation `GEN-S6R-682a8afad97938325c6f9f40`.

The Actions artifact was independently downloaded during this review. Its ZIP SHA-256 independently recomputed to the exact recorded artifact digest. The generated evidence commit is an ancestor of the judged head; the only later judged-head changes are the remediation report and handoff, so the byte-bearing generated evidence remains unchanged at the judged head.

## M01 — retained actual frame bytes and attempt attribution

**PASS.** The immutable artifact contains actual `frames/Godot/N1.png` and `frames/Godot/N2.png` byte objects. Independent review recomputation found:

- N1 SHA-256 `32c2c6cce0898ec194ee00d75e6ec89eb5867df97a5852fb7fce69d549dbe34a`, decoded RGB 1280×720, candidate-visible marker pixel `E6CC1A`;
- N2 SHA-256 `8a3b0ba520f9c8577f5d510c97181f3e8449102b3729615b3a1c397f176dbf7b`, decoded RGB 1280×720, candidate-visible marker pixel `E61ACC`;
- normal frames are byte-distinct;
- all three bounded player-surface panels independently decode to distinct retained colors in both frames.

The marker is rendered by the Godot project itself from the attempt identity, not added by the host capture tool. The candidate-generated ready-state record binds the same attempt marker, exact generation, `CAPTURE-STATE-042`, three screen identities/routes, and 1280×720 viewport.

The independent verifier's actual-byte substitution attack is materially adequate for M01: it copies the actual N1 PNG bytes into an N2 object and recomputes the byte SHA, capture SHA, capture-binding digest, and raw-attempt digest. The forged N2 still fails because the retained candidate-rendered N1 pixels do not satisfy independently derived N2 marker authority. Review inspection confirms `actual_byte_substitution_rejected=true` is not merely a prose assertion.

## M02 — real capture-down failure separated from candidate state

**PASS.** FI1 is not a synthetic boolean fixture. The runner starts the exact Godot project, reaches candidate-generated `CAPTURE-STATE-042`, records the Godot process alive at capture time, and invokes the same real capture program used by N1/N2: `/usr/bin/scrot`.

Normal capture runs on `DISPLAY=:99`; FI1 deliberately invokes `scrot` with `DISPLAY=:199`. The retained raw attempt records:

- `real_capture_invoked=true`;
- program `scrot` and command path `/usr/bin/scrot`;
- `DISPLAY=:199`;
- observed exit `1`;
- `timed_out=false`;
- output path absent;
- frame count `0`;
- stderr `scrot: Can't open X display. It *is* running, yeah? [:199]`;
- exact candidate process alive at capture;
- exact candidate-generated state marker/routes/viewport still valid.

Those facts support only `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`. The verifier also performs a recomputed-metadata misclassification attack by changing the FI classification to `STATE_REACHABILITY`; the exact FI verification rejects it. `fi_misclassification_rejected=true` is therefore mechanically supported.

## Identity, reset, source, and v5 envelope attacks

Independent review recomputation additionally confirmed:

- candidate-identity body digest is exact;
- remediation `WORK-S6R-f4576f798ba60a2e4d47dc78` and `GEN-S6R-682a8afad97938325c6f9f40` reconstruct exactly from candidate identity, adaptation identity and run identity;
- all N1/N2/FI1 raw-attempt canonical digests recompute exactly;
- all capture-binding body digests recompute exactly;
- the formal source-binding registry maps one-to-one to the three raw-attempt digests;
- N1/N2/FI1 workspace IDs and reset IDs are each unique, with exclusive fresh-workspace facts retained;
- exact Godot executable SHA-256 `32f8d7596c4b41185512b1c49d69f2da3be018fd784a53e349fa92a98a97bcde` and Godot `4.7.1-stable` identity are retained in candidate/run bindings;
- the reviewed v5 validator remains blob `2c646988dc16e212f43df6a4ee5ce646622ac2a6`, validator byte SHA-256 `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`;
- independent verifier recomputation returns adaptation `ACCEPT` and aggregate `PASS_FOR_COMPARISON` with `valid_envelope=true`;
- the evidence itself keeps `trusted_bounded_s6_comparison_authority=false`, `integration_authority=false`, `engine_selected=false`, `implementation_readiness=false`, `canonicality=NOT_CANONICAL` pending this review.

The source producer #456 and required review #458 remain immutable provenance; findings `W2-ENG-TECH-S6-REV-M01` and `W2-ENG-TECH-S6-REV-M02` are closed only for this exact remediation generation.

## Candidate/status preservation

No cross-candidate or scenario authority is upgraded:

- Godot: exact remediation generation may now be trusted only as bounded reviewed S6 v5 comparison evidence;
- Bevy: remains `INCONCLUSIVE_HARNESS_OR_INFRA`;
- Defold: remains `INCONCLUSIVE_HARNESS_OR_INFRA`;
- Unity: remains `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`;
- Unreal Engine: remains `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`.

No S1/S2/S7-S10 completion, five-candidate completion, engine ranking/selection, gameplay/high-throughput implementation, implementation/production readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision, canonicality, or integration authority is created here.

## Findings

- BLOCKER: 0
- MAJOR: 0
- MINOR requiring correction: 0

No material defect was found against the exact M01/M02 remediation contract.

## Disposition

`PASS_BOUNDED_REMEDIATED_S6_V5_ENVELOPE`

The exact Godot remediation generation `GEN-S6R-682a8afad97938325c6f9f40` is acceptable as bounded reviewed S6 v5 comparison evidence only. Any publication/integration is a separate convergence action requiring current merge compatibility and repository integration authority, and must be squash-only. This review itself remains noncanonical review provenance.