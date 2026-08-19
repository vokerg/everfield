# W2-ENG-TECH-S6-REM-REV-02 — required review of formal-bound S6 remediation

## Review disposition

`PASS_BOUNDED_S6_FORMAL_V5_REMEDIATED_ENVELOPE`

This is the fresh required degraded-independent review routed by Issue #591. The judged producer packet is review-clean for the exact Godot S6 generation and may be treated as bounded S6 `PASS_FOR_COMPARISON` evidence under the canonical v5 aggregation contract. This review does not grant integration, engine ranking/selection, implementation/readiness, provider/commercial/legal/platform/release, verification-PASS, decision, production, or canonical authority.

Findings: **0 BLOCKER, 0 MAJOR, 0 correction-required MINOR**.

## Frozen judged identity

- producer issue / mission: #591 / `W2-ENG-TECH-S6-REM-02`
- producer terminal status: comment `5317449098`
- producer branch/head: `planning/issue-591@d95a208bec7d213d2f8e958d8bb0a628ffbcd112`
- producer draft PR: #594, exact head `d95a208bec7d213d2f8e958d8bb0a628ffbcd112`
- evidence trigger: `020b4b9e05d26ff551c229d0b274751cd7995ff0`
- Actions run: `32043481976`, attempt 1, success
- evidence commit: `4d54ba0ba00c09890e03d1fe10d2c08d1657069f`
- immutable artifact: `9292381852`
- artifact ZIP SHA-256: `d7b2785e47b2bf8c86356d33439a22bbc4befe90d5ea8b6130fff3830cedecb4`
- remediation JSON SHA-256: `383e6ebb1031260564d605fa7d746e83ebe86cc66982ae7de8741175c73952cb`
- independent-verifier JSON SHA-256: `78b533d8cb9d990ffaadedf596591fb83ad3f88f2a2a7b3db7de72f05f61bee9`
- generation: `GEN-S6-REM2-2a8d597ef60acfb220e2`
- exact judged canonical validator blob: `2c646988dc16e212f43df6a4ee5ce646622ac2a6`
- exact judged producer probe blob: `dc82deb95128259a23283931f69144f9b9003ec3`
- exact judged independent verifier blob: `e56e0e263d483c5363b49a7783b01d96d7d597ee`

Git comparison from evidence commit `4d54ba0...` to terminal producer head `d95a208...` is one metadata-only commit adding `docs/planning/handoffs/issue-591.md` and `docs/planning/wave-2/evidence/engine-technical-s6-tranche.md`. No probe, verifier, workflow, validator, JSON, or PNG evidence bytes changed after the successful evidence commit.

## Independent artifact and byte checks

The review downloaded artifact `9292381852` independently and recomputed the ZIP digest exactly as `d7b2785e47b2bf8c86356d33439a22bbc4befe90d5ea8b6130fff3830cedecb4`. The retained JSON digests independently match the producer terminal packet.

N1 independently decodes as a 1280×720 PNG with marker pixel `[255,255,0]` and SHA-256 `ec2083126dba2bdb96929bfd4306485ad52116d4dc1c7be8b00fb90d0955056b`. N2 independently decodes as a 1280×720 PNG with marker pixel `[255,0,255]` and SHA-256 `54119fd58b7f625b3b739113bd20fa50c503aed486b84f51885b97a61dfd1b7b`. The two frame byte streams are distinct. Substituting the actual N1 bytes for N2 fails the retained SHA/marker identity; a missing frame fails inspection; a one-byte mutation fails the retained byte identity.

The judged producer source shows that Godot itself draws the attempt-specific marker in `m.gd`, while the host captures the X11 framebuffer with `scrot`; the host does not synthesize the marker image.

## FI1 state/capture separation

FI1 retained evidence independently re-hashes and shows:

- target state reached: `state_ok=true`
- candidate alive at capture: `true`
- actual command: `/usr/bin/scrot -z /proc/everfield-s6-capture-down.png`
- command executed: `true`
- exit: `1`
- stderr: `scrot: Saving to file /proc/everfield-s6-capture-down.png failed`
- captured frames: `0`
- target artifact exists: `false`
- failure mode: `REAL_SCROT_WRITE_TO_UNWRITABLE_PROC_PATH`
- exact classification: `STATE_REACHABLE_CAPTURE_PIPELINE_UNAVAILABLE`

Thus the injected failure is a real capture-pipeline failure after state reachability, not a state-reachability failure. Relabelling it as `STATE_REACHABILITY_FAILURE` is rejected by the exact review contract.

## Reset/workspace evidence reconstruction

For N1, N2, and FI1, the review independently canonical-JSON-hashed every retained reset body, workspace body, and actual binding body. All hashes reproduce exactly. Every derived ID is the required prefix of the corresponding full digest.

Each reset body proves `absent_before=true`, `empty_after_create=true`, and retains filesystem device/inode identity. Each workspace body retains the same device/inode identity, exact project-file hashes, and an observed `/proc/<pid>/cwd` equal to its retained workspace path. All three reset records are `verified=true`; normal reset identities are distinct; normal workspace identities are distinct.

The exact producer source constructs those records from the runtime-created per-attempt directories before passing the derived N1/N2 reset/workspace identities into canonical v5 `gen()`, then replaces the single FI AttemptRecord reset/workspace fields with the actual FI evidence identities. No literal `R1/R2/W1/W2` placeholders remain in the retained generation.

## Formal generation and actual-evidence binding

The retained generation contains exactly three AttemptRecords and both `run_registry_refs` and `all_attempt_refs` are unique, complete, cardinality-equal sets of those exact keys. All AttemptRecords bind candidate `Godot`, scenario `S6`, generation `GEN-S6-REM2-2a8d597ef60acfb220e2`, common resource class `W2-ENG-HOST-COMMON-v2`, matching result/failure envelopes, and matching reset/workspace identities.

For each N1/N2/FI1 formal AttemptRecord, the review independently recomputed:

- the canonical formal AttemptRecord SHA-256;
- the actual attempt binding SHA-256;
- the reset evidence SHA-256;
- the workspace evidence SHA-256; and
- the enclosing `formal_attempt_bindings` link SHA-256.

All links reproduce exactly and map one formal attempt to the same actual N1/N2/FI1 execution. Deliberately swapping actual-binding digests between formal links causes the formal/actual binding check to fail.

## Independent canonical v5 aggregation

The review inspected and cold-executed the exact S6 aggregation semantics from canonical validator blob `2c646988dc16e212f43df6a4ee5ce646622ac2a6` against the retained generation rather than copying the producer aggregate. Independent results are:

- adaptation validation: `ACCEPT`
- adaptation identity: `25d0ead1111ff8ef214a622286f71baa86ba127a13a65ca7c674cdcc2128f713`
- adaptation binding: `da9e08a47340186dcab7d9fc62380b64ee580c0d7f39d2005aa3f83c30276476`
- aggregate: `PASS_FOR_COMPARISON`
- reasons: `[]`
- `valid_envelope=true`

The judged independent verifier is materially independent of the producer aggregate at the aggregation step: it loads the validator, calls `v.va(...)`, calls `v.agg(copy.deepcopy(g))`, re-hashes the formal/actual links, and compares its recomputation to the producer result.

The review independently reconstructed the routed negative attacks. Reused normal reset becomes `NOT_RUN / normal_attempts_reuse_reset_identity`; unverified normal reset becomes `NOT_RUN / independent_reset_not_verified`; reused normal workspace becomes `NOT_RUN / normal_attempts_reuse_workspace`; duplicate or incomplete run/all-attempt registries become structural `INCONCLUSIVE` with `valid_envelope=false`; AttemptRecord candidate or generation tampering becomes structural `INCONCLUSIVE` with `valid_envelope=false`; and formal-to-actual link substitution is rejected. All routed fail-closed controls therefore hold.

## Preservation and authority boundary

The producer packet preserves Bevy and Defold as `INCONCLUSIVE_HARNESS_OR_INFRA`, Unity and Unreal Engine as `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`, and the historical Issue #82 count of 50 `NOT_RUN` cells. This review makes no changes to those cells and does not infer ranking or selection from the bounded Godot S6 result.

The exact Godot generation above is now review-clean bounded S6 comparison evidence. The packet remains `NOT_CANONICAL`. No integration into `main` is authorized by Issue #596; any later integration or canonicalization requires a separately eligible task with explicit repository authority and, for integration, squash-only execution.