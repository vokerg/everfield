# Issue #1547 — Exact frozen-head feedback policy verifier

## Ownership and source binding

- Task `IMPLEMENTATION-DEMAND-INTERACTION-FEEDBACK-03-VER-01`; first valid owner CLAIM comment `5988865864`, session `frontier-verify-feedback-1547-gpt56sol-20261005-0749-01`. Claim was immediately reread and was the only valid claim. Deterministic branch `planning/issue-1547` was created from exact `main@781d65ca07c7b410faaecfa1e8cbfd6f5fc8ed48`.
- Canonical binding #1147 comment `5675066392`, program Git blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Canonical planning authority is not modified.
- Producer #1543 source-only terminal `STATUS(REVIEW_READY)` comment `5988862194`, immutable source draft PR **#1546**, exact source head `d6b645d5a31d53003e451637ecce14541dbe40df`. The source is not reviewed, runtime-verified, published, or canonical by that producer status. The isolated verifier checks out this immutable head, *not* the verifier's own PR checkout.
- Exactly three immutable source blobs: `game/components/interaction_feedback/interaction_feedback_policy.gd` `0f3b32c254f00f27338202fa7f0dd53c6f2efcf8`; `game/components/interaction_feedback/interaction_feedback_smoke.gd` `90c3608288426d29fefec8e7248074ab2ca4b969`; `docs/planning/handoffs/issue-1543.md` `f95d2f0ac7975215217b3b8a8c54635a75176593`. Current published immutable controller, scene, HUD, station, traversal and presentation provider Git blobs are positively checked in the workflow.
- Sibling #1544 has separate `game/components/action_commands/**` exclusive scope. Shared fan-in #1545 remains explicitly **BLOCKED** until both components obtain exact-head locked-engine PASS, clean distinct required review and independently authorized squash publication.

## Verifier-specific unmerged evidence surface

Exactly two verifier-only files on this branch:
1. Temporary `.github/workflows/verify-interaction-feedback-1547.yml` — own pull-request-triggered, SHA-pinned GitHub Actions execution of the source component; **must never be merged**.
2. `docs/planning/handoffs/issue-1547.md` — this provenance and continuation record; no game code/provider edits.

The workflow uses reviewed published `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` to acquire the exact `4.7.1-stable` Linux x86_64 ZIP, SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`, byte verifies the download and engine banner `4.7.1.stable.official.a13da4feb`. The test is the new isolated script:

```sh
godot --headless --path game --script res://components/interaction_feedback/interaction_feedback_smoke.gd
```

The script must exit zero, contain the exact full-line `EVERFIELD_INTERACTION_FEEDBACK_SMOKE_PASS`, show the near-to-far stale prompt negative test, and contain zero `[EF-INTERACTION-FEEDBACK][FAIL]` assertions, parser errors or uncontrolled engine errors. Exercises approved real HUD/SessionState fixtures, far/near/far/near, immutable source text and snapshots, COMPLETE/R reset precedence, typed missing/unknown station IDs, malformed HUD, forged mystery/status/phase, negative path and explicit truth/consent boundaries. Logs and immutable source hashes plus run/source/verifier PR SHA identity are archived under `issue-1547-evidence/`.

## Terminal gate and handoff

**Creation of this verifier workflow and this handoff is NOT runtime evidence or PASS.** Open an **exact-head draft** verifier-only PR to `main`, and confirm the GitHub Actions run is triggered *on the final verifier PR head containing both files*. Inspect the real completed run and job, the exact Godot banner and downloaded ZIP lock, raw/retained smoke log and all `source-git-blobs` / `run-identity.txt` data, exit, full-line success and negative checks. Fetch artifact ID, byte size and SHA-256. If workflow/head advances after a success, rerun on the new final HEAD; predecessor success alone is never terminal proof.

If exact frozen-head test and all identity/evidence checks PASS, publish schema-3 `VERIFICATION_STATUS(DONE)` on **Issue #1547** binding owner generation `5988865864`, final verifier PR/head, source PR/head/blobs, reviewed engine, actual run/job/attempt/conclusion and artifact; `extensions.result: PASS`; required next route is **existing required independent Review #1548**, which must remain independent from both producer and verifier. That review may reject/fail the source. If any run or source evidence fails, record negative logs and route precise bounded producer remediation and fresh exact runtime verification; do not fabricate PASS.

Neither this temporary workflow nor handoff has integration authority, should be squash-merged, or can make the source canonical, permit self-review, resolve mystery truth, reveal private Anwen provenance, imply consent, persist data, certify accessibility/production/readiness, or authorize release. Accepted game/component publication, if warranted, needs separately authorized squash-only NONCANONICAL integration after clean required review.
