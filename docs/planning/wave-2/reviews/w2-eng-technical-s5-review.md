# W2-ENG-TECH-S5-REV-01 — required review of public-toolchain S5 packet

## Disposition

`PASS_BOUNDED_S5_V5_ENVELOPE`

Findings: **0 BLOCKER / 0 MAJOR / 0 MINOR**.

Trust mode: `DEGRADED_SINGLE_AGENT`. This is a fresh ownership/review episode distinct from producer session `frontier-drain-s5-gpt56sol-20260816-01`, but no stronger reviewer isolation is available in this execution context. The judged producer branch is immutable and was not edited.

This review grants trusted bounded S5 comparison evidence only to the exact final Bevy, Defold, and Godot generations named below. It grants no integration authority, engine ranking/selection, implementation/readiness, provider/commercial/legal/platform/release authority, verification-PASS, decision, or canonical authority.

## Frozen judged identity

- producer Issue: `#433` / `W2-ENG-TECH-S5-01`
- winning producer claim: `5308441704`
- terminal producer status: `5308620093`
- producer branch: `planning/issue-433`
- exact judged head / PR #453 head: `89089a841e4c199592fc45bc3562d0d32df6300d`
- producer claim base: `3de6f8f276cd1479ceccdea7362420f1e0efa030`
- PR #453 routed base: `cf65031bfa3275b674e8232734176cac67485c8d`
- final trigger: `f515bbcba6e53f56534bce5f58a3869d006aa3d5`
- final run: `31960259059`, attempt `1`, conclusion `success`
- generated evidence commit: `c8e5b102c8f1798e7df7c631f8344ea203d22cb0`
- artifact: `9267094933`, `w2-eng-tech-s5-01-31960259059-1`
- artifact ZIP SHA-256: `1dd12fb8436b0949ccf890dfb2a7233a5e73335cdfbb17d633b0c1b8e4bfd55c`
- `evidence.json` SHA-256: `3e7dfdf8323caeb061027e2435fb6a3c20748802c34d10f49c42aa496f5f1107`
- `independent-verification.json` SHA-256: `1ffa031649b7aafeca8cda3c0a33e577a6ac17a27b74f81ed547a221a8704e04`
- validator final-run byte SHA-256: `9a50e3e21279a7a94836d6162fee218a0e187bafe292847fd5f0b108df45deea`
- validator repository blob: `2c646988dc16e212f43df6a4ee5ce646622ac2a6`
- unchanged authority identities: `W2-ENG-HARNESS-v5`, `W2-ENG-FEATURE-SLICE-v2`, `W2-ENG-SCENARIO-INPUTS-v2`

At review time current `main` had advanced to `94186664d570239319e6689ddaac1e97ccaf721d`, making PR #453 non-mergeable. That base drift does not alter the frozen judged head and is not treated as review or integration authority. Any later producer publication must be separately recovered/authorized and squash-only.

## Independent artifact inspection

The final artifact was independently downloaded through the GitHub Actions artifact endpoint. The downloaded ZIP itself hashes exactly to `1dd12fb8436b0949ccf890dfb2a7233a5e73335cdfbb17d633b0c1b8e4bfd55c`. Its eight retained files are `evidence.json`, `evidence.sha256`, `harness-validator.json`, `independent-verification.json`, `independent-verification.log`, `independent-verification.sha256`, `run-identity.txt`, and `summary.log`.

Re-hashing the extracted machine files independently reproduced the routed hashes exactly:

- `evidence.json`: `3e7dfdf8323caeb061027e2435fb6a3c20748802c34d10f49c42aa496f5f1107`
- `independent-verification.json`: `1ffa031649b7aafeca8cda3c0a33e577a6ac17a27b74f81ed547a221a8704e04`

The final Actions job `95197043479` shows successful exact-trigger checkout, authority-input validation, fresh S5 execution, independent verifier execution, envelope enforcement, generated-evidence commit, and artifact upload. The upload log independently records 25,921 bytes and the same ZIP SHA-256.

## Adversarial review results

### 1. Identity and artifact binding — PASS

Claim, terminal status, branch/head, PR head, trigger/run, generated commit, artifact id/name/digest, machine-file hashes, validator identity, report/handoff, and final generation IDs agree. No judged producer identity drift was found.

### 2. Producer-defect provenance — PASS

All five failed/incomplete/superseded runs remain visibly non-authoritative in the producer report/handoff and terminal status:

1. `31959088675` / `9266757869`: Bevy retained-lock root package mismatch.
2. `31959336546` / `9266839656`: generated-metadata collision not exercised.
3. `31959682648` / `9266948644`: partial correction with stale verifier; no promoted persistence.
4. `31959719316`: cancelled superseded intermediate run.
5. `31959757285` / `9266994724`: Defold log-prefix parser mismatch.

The final machine packet carries the three predecessor corrections that produced retained evidence; the report/handoff/status separately preserve the non-persisted partial and cancelled runs. None is reused as final authority.

### 3. Candidate-native authenticity — PASS

Source and retained machine evidence bind real candidate execution rather than a Python-only result oracle:

- **Bevy**: `cargo build --locked --quiet` against retained Bevy `0.19.0` lock SHA `fd7e1276ff5c8cde22d98c0932f70eb39383d9b60ac2d15f11d921dfa71218b0`, followed by execution of the built `everfield_bevy_probe` binary.
- **Defold**: exact Bob `1.13.0` (`f735c12...`) bundle build through Java 25 followed by execution of the bundled Defold engine process; retained logs identify `Defold Engine 1.13.0 (f735c12)`.
- **Godot**: exact retained `4.7.1-stable` executable, digest-bound and invoked `--headless --path` against the actual project.

All three candidates independently emit `EVERFIELD_S5:PASS` on the resolved candidate-native validation path.

### 4. N1/N2 directional independence — PASS

For each candidate, N1 and N2 share one exact baseline tree, use directions `A_THEN_B` and `B_THEN_A`, and each branch changes exactly one non-overlap file. Both merges are clean, preserve both updates, and converge to the same final tree per candidate.

### 5. Exact semantic overlaps — PASS

FI1 maps exactly `STATE:entity-07.status` and `UI:SETTINGS.control-02.label` to the candidate-native state/UI files. Both branches change both surfaces incompatibly. Git reports a nonzero merge exit, exactly the expected unmerged paths, and visible conflict markers. Silent last-writer-wins is not accepted.

### 6. Mandatory generated-metadata collision — PASS

All represented fixtures generate candidate-native metadata. In FI1, both branches invoke the real candidate process and materialize distinct `generated/candidate-metadata.txt` values:

- branch A: `ACTIVE|Sound|true|Back`
- branch B: `PAUSED|Volume|false|Return`

The tracked metadata path is a third visible unmerged conflict for Bevy, Defold, and Godot. Candidate-generated digests are distinct and omission/noncollision is rejected by the retained independent verifier.

### 7. Resolved metadata regeneration — PASS

After choosing branch-A state (`ACTIVE`) and branch-B UI (`Volume`), the producer reruns the candidate-native process from resolved source and rewrites the tracked metadata from that output. All three final values are exactly `ACTIVE|Volume|true|Return`, and the retained file equals the generated value rather than either branch value.

### 8. Defold parser correction — PASS

Exact `engine_technical_s5_entry_v2.py` searches each combined stdout/stderr line for only the literal marker `EVERFIELD_S5_METADATA:` and returns only the suffix after that marker. Missing marker yields `None`; no fallback or fabricated metadata exists. This narrowly fixes Defold's normal `DEBUG:SCRIPT:` prefix while preserving fail-closed behavior. The predecessor packet records correct exit-0 `DEBUG:SCRIPT:` metadata that the old column-zero parser rejected; the final packet cleanly extracts all three Defold metadata generations.

### 9. Post-merge candidate-native validity — PASS

Each resolved packet actually executes its native validation path successfully. Source inspection independently confirms that Bevy, Godot, and Defold compare the candidate state/UI against `EVERFIELD_S5_EXPECT_STATUS` and `EVERFIELD_S5_EXPECT_LABEL` and exit nonzero on mismatch; they also require branch-A enabled and branch-B label `Return`. Thus a mismatched expected state/UI cannot take the observed PASS path.

### 10. Reset/workspace derivation — PASS

Each candidate has three distinct reconstructed workspace IDs and reset IDs for N1/N2/FI1. `pre_workspace_absent=true`, exclusive workspace creation, and `reset_verified_derived=true` are retained in raw evidence. Independent recomputation found no reuse.

### 11. Raw/source/toolchain binding — PASS

Independent canonical-JSON recomputation reproduced every candidate-identity digest and every raw-attempt digest. Source bindings are one-to-one with the three raw attempt digests per candidate. Exact run identity, validator, runner/correction entry, retained Bevy lock, Defold artifact, Godot artifact/executable, and tool versions are bound into candidate identity. Substitution attacks fail closed.

### 12. Generation identity — PASS

Independent recomputation using exact candidate identity digest, ordered raw-attempt digests, adaptation identity, run identity, and scenario reproduced all work/generation IDs:

- Bevy: `WORK-S5-9416eddd5c88619eee82e3b6` / `GEN-S5-d973bfa614c120e3099bcab7`
- Defold: `WORK-S5-c878e41cc82a6d1af29c1119` / `GEN-S5-19071a679f17a453a680a2a5`
- Godot: `WORK-S5-cd2b8d29d3f915d1a8e1c1ef` / `GEN-S5-9a4eb68ccb19ba8ca84aa7c9`

Temporary workspace paths are not identity authority.

### 13. Unchanged v5 validation/aggregation — PASS

The judged validator is the unchanged reviewed v5 authority. Exact adaptations are `ACCEPT`. Retained and independently recomputed aggregates are exactly `PASS_FOR_COMPARISON` with `valid_envelope=true` for Bevy, Defold, and Godot. The v5 validator rejects duplicate retained registries, generation mismatch, invalid adaptation/binding, bad reset/resource envelopes, malformed attempts, and laundering failure classes.

### 14. Negative attacks — PASS

The producer self-tests and separate retained verifier collectively reject the required attacks: missing overlap; lost non-overlap; silent overlap; generated-metadata collision omission; resolved-metadata bypass; candidate-native validation bypass; formal/raw binding substitution; raw-source substitution; workspace reuse; toolchain identity substitution; candidate-generation mismatch; and duplicate registry. All retained negative booleans are true for all three provisional candidates.

### 15. Blocked candidates and prior provenance — PASS

Unity `6000.5.6f1` and Unreal Engine `5.8` remain exact `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. Issue #82's historical 50 `NOT_RUN` cells and reviewed S3/S4 provenance remain explicitly preserved. No five-candidate-completion claim is made.

### 16. Authority inflation — PASS

The packet explicitly keeps `fresh_review_required=true`, `trusted_comparison_authority=false` at producer time, `integration_authority=false`, `engine_selected=false`, `implementation_readiness=false`, and `canonicality=NOT_CANONICAL`. This review changes only the trust status of the exact three reviewed S5 generations within the bounded v5 comparison envelope. S1/S2/S6-S10, engine selection/ranking, production/readiness, provider/legal/platform/release, verification-PASS, decision, canonicalization, and integration remain outside authority.

## Reviewed bounded result

The exact final producer packet supports trusted bounded S5 v5 comparison evidence for only:

- Bevy `GEN-S5-d973bfa614c120e3099bcab7`
- Defold `GEN-S5-19071a679f17a453a680a2a5`
- Godot `GEN-S5-9a4eb68ccb19ba8ca84aa7c9`

No other S5 generation or candidate is upgraded. No publication to `main` is authorized by this review alone; later integration is a separate authority decision and must remain squash-only.