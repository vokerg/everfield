# W2-ENG-TECH-S7-REV-01 — required review

## Disposition

`PASS_BOUNDED_S7_BROKEN_REFERENCE_EVIDENCE`

Findings: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR**.

Trust mode: `DEGRADED_SINGLE_AGENT` under canonical resource constraint comment `5244416013`. The judged producer branch was frozen and never mutated by this review. Reopen condition: `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE`.

## Frozen judged candidate

- Producer Issue #507 terminal status: comment `5312727468`, `REVIEW_READY`.
- Producer PR #515: open, draft, mergeable at review; base `main@538b8a3b46b8b095bc43206d4a0ad4fdc151616a`; exact head `95d292115776a66740d7df6a06461ec4c1280a24`.
- Current-main compare at review: 10 ahead / 0 behind, merge base exactly current main; only the 11 S7-owned workflow/runner/evidence/report/handoff paths are present.
- Final execution trigger: `0bb0596b1440759d73a7282d2daee28ef13fb560`.
- Final Actions run: `31992873649`, attempt 1, conclusion `success`; all validate/execute/enforce/persist/upload steps succeeded.
- Evidence-recording commit: `5ceddbf696432cb069db5461c48c2b4e66d67121`; compare from trigger to this commit changes only the generated S7 evidence bundle.
- Compare from evidence-recording commit to terminal head changes only the producer tranche report and Issue #507 handoff; machine evidence is unchanged after workflow persistence.
- Immutable artifact: `9275925526`, `w2-eng-tech-s7-01-r2-31992873649-1`, live at review.
- Artifact ZIP SHA-256 independently recomputed from downloaded bytes: `9356f81d96c9f7804b68f9fed65f82e9b621c5076f020e64f5df570144c244da`, exactly matching GitHub's artifact digest.
- Artifact `evidence.json` SHA-256 independently recomputed: `4900306a228e2ede28c8699b21dee15fabfc1d52a7b354938536d15fd1e25123`, exactly matching committed producer identity.
- Validator: `W2-ENG-PROTOCOL-VALIDATOR-v5`, blob `2c646988dc16e212f43df6a4ee5ce646622ac2a6`.

## Mechanical review

### Candidate-native diagnosis and repair

The exact final packet contains two cold normal attempts plus one `FI-S7-BROKEN-REF-v2` attempt for each represented candidate. Every candidate has three distinct workspace/reset identities.

- **Bevy 0.19.0** — generation `GEN-S7-544c85823f09e1a866b79c58`. The retained locked Cargo/Bevy project runs `cargo check --locked --quiet`; the FI attempt exits 101 and specifically reports the missing `assets/MISSING-ASSET-08.txt` include. Restoring the one driver reference produces the original driver SHA and the same Cargo path reruns exit 0.
- **Defold 1.13.0** — generation `GEN-S7-ec551632e42e05e85eb872e7`. Pinned Bob `resolve build` exits 1 on FI and specifically reports `/assets/MISSING-ASSET-08.lua` missing; restoring the one driver reference restores the exact driver SHA and the same Bob path reruns exit 0.
- **Godot 4.7.1-stable** — generation `GEN-S7-6a86e8eb88e02c6d7c76dc18`. The digest-verified Godot executable runs headless against the generated project. FI exits 1 with `Preload file "res://assets/MISSING-ASSET-08.tres" does not exist`; the restored script reruns through the same Godot command, exits 0, and prints the expected eight-asset marker.

For all three candidates the defect is exactly one reference to exact logical asset `ASSET-08`; all eight asset-file digests remain identical before, during, and after the driver-reference defect; the driver SHA changes only for the injected reference and returns exactly to baseline after repair. `diagnostic_attributed`, `repair_changed_only_broken_reference`, and `rerun_clean` are all true.

### Independent artifact integrity attack

The final artifact was downloaded independently during review. For all nine retained raw attempts, the review recomputed `sha256(canonical_json(raw_record))` and every value exactly matched its stored raw digest. For every candidate, the set of recomputed raw digests exactly equals the `source_bindings` values. This closes source/raw-substitution or post-run evidence-edit ambiguity beyond the producer's own self-test claims.

All three packets have:
- adaptation validation `ACCEPT`;
- exact aggregate `{PASS_FOR_COMPARISON, reasons: [], valid_envelope: true}`;
- source-binding set equality;
- three unique workspace IDs and reset IDs;
- all producer negative self-tests true.

### Formal v5 fail-closed layer

The unchanged v5 S7 contract requires `SLICE:assets` + `SLICE:logical_state`, obligations `inject_broken_reference`, `diagnose_from_repo_cli`, `bounded_repair`, `rerun`, bounds `{asset_count: 8, broken_reference_count: 1}`, injection `FI-S7-BROKEN-REF-v2`, common cold/regenerate start state, and candidate-native-equivalent mechanism authority.

The v5 aggregate rejects malformed/mismatched adaptation binding, cross-candidate or cross-generation attempts, duplicate or mismatched retained registries, malformed result/failure envelopes, missing/unverified/reused reset/workspace identities, missing/duplicate required injections, non-common resource class, and non-product uncertainty before it can return `PASS_FOR_COMPARISON`. The producer's candidate-specific negative controls additionally reject wrong/multiple broken references, host-only/unattributed diagnosis, overbroad repair, rerun bypass, source/raw substitution, generation mismatch, duplicate registries, reused workspace, and candidate-native validation bypass.

### Correction lineage

Run `31991497890` remains explicitly incomplete provenance. Run `31992586423` remains partial provenance with clean Bevy/Defold results and two bounded Godot harness defects. Final R2 preserves the base runner SHA and overrides only typed Godot Resource fixtures and `SceneTree.quit()`. The final run freshly re-executes all three candidates; no prior partial result is promoted by reference alone.

## Authority result

This review trusts only the exact three executed S7 generations above as bounded broken-reference comparison evidence. It does **not** trust or complete Unity or Unreal, which remain `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`; it does not rewrite Issue #82's historical 50 `NOT_RUN` cells or reviewed S3/S4/S5/S6 evidence.

This PASS grants no integration-by-review, engine selection/ranking, implementation/readiness, provider/commercial/legal/platform/release, verification-PASS, decision, canonicalization, or canonical authority. Any publication/integration is a separate current-main/exact-head-authorized episode and must be squash-only.

## Reopen conditions

Reopen if any frozen producer head/run/artifact/evidence identity changes, if the exact artifact becomes inconsistent with the committed evidence identity, if candidate-native diagnosis/repair mechanics are invalidated, or when `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE` permits stronger independence.
