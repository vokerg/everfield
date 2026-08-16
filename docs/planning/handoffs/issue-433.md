# Issue #433 handoff — W2-ENG-TECH-S5-01

## State

`REVIEW_READY` pending exact-head draft PR and terminal schema-3 status.

Producer disposition: `PARTIAL_EMPIRICAL_S5_EVIDENCE_READY_FOR_REVIEW`.

Three lawfully executable public candidates have complete bounded producer S5 evidence. Unity and Unreal Engine remain exact `NOT_RUN_BLOCKED_BY_SPECIFIC_AUTHORITY`. No result is trusted reviewed comparison evidence until the mandatory fresh review passes.

## Ownership / branch

- issue: `433`
- mission: `W2-ENG-TECH-S5-01`
- winning claim: `5308441704`
- actor session: `frontier-drain-s5-gpt56sol-20260816-01`
- branch: `planning/issue-433`
- claim base: `3de6f8f276cd1479ceccdea7362420f1e0efa030`
- current main observed during terminal reporting: `cf65031bfa3275b674e8232734176cac67485c8d`
- canonical blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: `5245368879`
- activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`

## Final empirical identity

- final trigger: `f515bbcba6e53f56534bce5f58a3869d006aa3d5`
- final Actions run: `31960259059`, attempt 1, success
- generated evidence commit: `c8e5b102c8f1798e7df7c631f8344ea203d22cb0`
- artifact: `9267094933`
- artifact name: `w2-eng-tech-s5-01-31960259059-1`
- artifact digest: `sha256:1dd12fb8436b0949ccf890dfb2a7233a5e73335cdfbb17d633b0c1b8e4bfd55c`
- evidence SHA-256: `3e7dfdf8323caeb061027e2435fb6a3c20748802c34d10f49c42aa496f5f1107`
- independent verification SHA-256: `1ffa031649b7aafeca8cda3c0a33e577a6ac17a27b74f81ed547a221a8704e04`
- independent verifier: `W2-ENG-TECHNICAL-S5-INDEPENDENT-VERIFY-v2`, `all_provisional_verified=true`

Final exact generations:

- Bevy: `GEN-S5-d973bfa614c120e3099bcab7`, work `WORK-S5-9416eddd5c88619eee82e3b6`
- Defold: `GEN-S5-19071a679f17a453a680a2a5`, work `WORK-S5-c878e41cc82a6d1af29c1119`
- Godot: `GEN-S5-9a4eb68ccb19ba8ca84aa7c9`, work `WORK-S5-cd2b8d29d3f915d1a8e1c1ef`

For all three: N1/N2/FI1 PASS, adaptation `ACCEPT`, aggregate exactly `PASS_FOR_COMPARISON`, `valid_envelope=true`, producer representation trusted only provisionally pending required review.

## Exact S5 semantics demonstrated

- N1: A→B independent non-overlap merge
- N2: B→A independent non-overlap merge
- FI1 required overlap at:
  - `STATE:entity-07.status`
  - `UI:SETTINGS.control-02.label`
- candidate-generated metadata collision at `generated/candidate-metadata.txt`
- exact three-way visible conflict in FI1
- deterministic bounded source resolution: state `ACTIVE` from A, UI `Volume` from B
- metadata regenerated from resolved candidate state: `ACTIVE|Volume|true|Return`
- candidate-native post-merge validation succeeds
- reset/workspace/source/toolchain/generation bindings are fail-closed

## Retained producer defect provenance

Do not promote or erase:

- `31959088675` / artifact `9266757869` — Bevy retained-lock root package identity mismatch.
- `31959336546` / artifact `9266839656` — exact v5 generated-metadata collision requirement not exercised.
- `31959682648` / artifact `9266948644` — partial metadata correction with stale verifier; safe failure/no promoted persistence.
- `31959719316` — cancelled superseded intermediate correction run.
- `31959757285` / artifact `9266994724` — Defold engine outputs correct metadata under `DEBUG:SCRIPT:` but producer marker parser required column zero; retained incomplete producer provenance.

The final v2 parser correction searches for the exact `EVERFIELD_S5_METADATA:` marker within each log line and retains only the marker suffix. Final toolchain identity binds this correction and predecessor-entry identity.

## Files / evidence surfaces

- `.github/workflows/w2-eng-technical-s5.yml`
- `tools/planning/engine_technical_s5_probe.py`
- `tools/planning/engine_technical_s5_entry.py`
- `tools/planning/engine_technical_s5_entry_v2.py`
- `tools/planning/engine_technical_s5_verify.py`
- `docs/planning/wave-2/evidence/engine-technical-s5-tranche.md`
- `docs/planning/wave-2/evidence/ci/engine-technical-s5/`
- `docs/planning/handoffs/issue-433.md`

## Self-review

- unresolved BLOCKER: 0
- unresolved MAJOR: 0
- correction-requiring MINOR: 0

The three material producer defects above were found before terminalization, corrected in bounded follow-up code, and preserved as predecessor provenance. Final run #31960259059 is the only producer packet eligible for fresh required review.

## Required fresh review

Create/use exactly one fresh required review successor for the exact terminal producer packet. Reviewer must not edit `planning/issue-433` and must attack:

1. exact claim/work/head/PR/run/artifact/evidence identities;
2. all failed/incomplete/cancelled predecessor producer runs and no evidence laundering;
3. real candidate-process/toolchain authenticity for Bevy, Defold, Godot;
4. N1/N2 merge-direction independence and non-overlap preservation;
5. both required semantic overlap locations;
6. candidate-generated metadata generation, collision, and resolved regeneration;
7. Defold log-prefix parser correction and exact-marker fail-closed behavior;
8. post-merge candidate-native validity;
9. reset/source/toolchain/generation identity and registry bindings;
10. unchanged v5 adaptation/aggregate semantics;
11. independent-verifier negative attacks;
12. Unity/Unreal exact authority-bound classification and Issue #82/S3/S4 preservation;
13. any engine-selection/readiness/provider/release/verification/integration/canonical authority inflation.

Suggested mission: `W2-ENG-TECH-S5-REV-01`.

## Authority boundary

`NOT_CANONICAL`. Producer evidence only. No trusted review authority, engine selection, gameplay/high-throughput implementation, implementation/readiness, production/commercial/legal/platform/release, verification-PASS, decision, integration, or canonical authority. Any eventual main publication is separately authorized and squash-only.
