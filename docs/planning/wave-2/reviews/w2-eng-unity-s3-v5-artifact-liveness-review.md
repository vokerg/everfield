# W2 Unity S3 v5 artifact-liveness remediation review

## Mission
`W2-ENG-TECH-UNITY-S3-V5-ARTIFACT-LIVENESS-REV-01`

## Disposition
`PASS_FOR_INTEGRATION`

Finding counts:
- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- INFO: 1

This review authorizes only the next separately authorized squash-only integration episode for the exact judged remediation packet. It does not establish artifact-liveness recovery empirically and grants no comparison, provider, verification, engine-selection/readiness, release, decision, or canonical authority.

## Trust / independence mode
`DEGRADED_SINGLE_AGENT`.

The reviewer actor is distinct from the Issue #808 producer actor. The exact judged producer head was frozen before substantive review; the producer branch was treated as immutable and was not edited. Reopen for stronger independent attack if `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE` becomes available before integration and repository authority requires it.

## Frozen judged packet
- current/frozen main: `eb81d354931c67ef2193f5242e49ee181a270b8c`
- canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- producer Issue #808 claim: `5513102094`
- producer Issue #808 terminal: `5513156000`
- producer PR: #809, draft at review freeze
- producer base: `eb81d354931c67ef2193f5242e49ee181a270b8c`
- producer exact head: `d82961e46caf0f0130626ca85ebd082f67e05f1a`
- compare: ahead `2`, behind `0`, merge base exactly frozen main
- workflow base blob: `188e84cf897ca0c09f862ffc03040fed1ce7cd87`
- workflow candidate blob: `f9b15228744b6814094d4e64faec4b78f9f952f4`
- changed paths exactly:
  - `.github/workflows/unity-s3-v5-lineage-evaluator.yml` — additions 2 / deletions 1
  - `docs/planning/handoffs/issue-808.md` — added

The substantive workflow patch is exactly:
1. `command -v caffeinate >/dev/null` immediately after `set -euo pipefail` in the native lineage step;
2. replacement of direct `python3 tools/planning/unity_s3_v5_lineage.py ...` with `caffeinate -i python3 tools/planning/unity_s3_v5_lineage.py ...` for the producer invocation only.

## Attack plan frozen before rationale
1. Reproduce the recurrence identity and distinguish native execution success from publication failure.
2. Attack whether `caffeinate -i` actually creates the intended macOS idle-sleep assertion and whether its lifetime is bounded to the producer process.
3. Attack fail-closed and shell/environment semantics.
4. Byte/semantic-diff the evaluator security and authority surface.
5. Verify S3 producer/recorder/evidence semantics and historical status are unchanged.
6. Verify no producer-branch Unity execution was used to self-validate the remediation.
7. Attack any attempted authority inflation or integration-by-review.

## Attack 1 — recurrence and scope
PASS.

Exact-current-main run `33642634779`, attempt 1, job `100289313431` ran on `everfield-unity-mac` / runner id `21` at exact head `eb81d354931c67ef2193f5242e49ee181a270b8c`.

The server job record reports:
- job start `2026-09-02T14:54:01Z`;
- server completion `2026-09-02T15:04:02Z`;
- native step start `14:54:09Z` and runner-reported completion `15:10:21Z`;
- sanitized-shape validation PASS at `15:10:21Z`;
- artifact upload then failed at `15:10:22Z` with `403 Forbidden: job is completed`.

The prior failed exact-main attempt, run `33595213169` attempt 2 / job `100160452746`, has the same shape:
- job start `07:56:13Z`;
- server completion `08:06:14Z`;
- native step continues from `07:56:21Z` to `08:12:30Z`;
- sanitized validation PASS;
- upload then fails with the same `403 Forbidden: job is completed`.

By contrast, run `33595213169` attempt 1 / job `100137172409` completed the native step in approximately 23 seconds and artifact upload succeeded.

The evidence supports the narrow claim that long persistent-runner execution is correlated with server-side job finalization before the runner reaches publication. It does not prove idle sleep is the only possible underlying cause. The remediation is therefore judged as a bounded, plausible repository-controlled liveness mitigation, not as empirical proof of recovery.

## Attack 2 — `caffeinate` semantics and lifetime
PASS.

Darwin `caffeinate(8)` documents that `-i` creates an assertion preventing system idle sleep. When a utility is specified, the assertions are created on the utility's behalf and persist for the duration of that utility's execution. Its example `caffeinate -i make` explicitly describes forking/executing the utility and holding the assertion while that process runs. Reference: https://keith.github.io/xcode-man-pages/caffeinate.8.html

The judged command passes the lineage producer directly as the utility:

`caffeinate -i python3 tools/planning/unity_s3_v5_lineage.py --editor-path "$UNITY_EDITOR_PATH" --out "$output_path"`

Therefore the idle-sleep assertion spans the producer process lifetime, including the period while that Python producer waits on its Unity subprocess, and ends when the producer exits. The patch does not create a background inhibitor and does not wrap the later validator, sanitized-shape check, or upload action.

## Attack 3 — fail-closed and shell/environment behavior
PASS.

The step retains `set -euo pipefail`. `command -v caffeinate >/dev/null` therefore terminates the step if the expected executable cannot be resolved; the native episode is not silently executed without the guard.

`PYTHONPYCACHEPREFIX=... caffeinate -i python3 ...` supplies the variable to the invoked `caffeinate` process and its executed child environment. Producer arguments, editor path, output path, and the later `--validate` invocation are otherwise unchanged.

No secret, token, privilege, workflow permission, runner label, or workflow trigger was added.

## Attack 4 — evaluator security / authority surface
PASS.

The exact PR patch modifies only the two workflow lines described above and adds the producer handoff. The following remain unchanged in the evaluator:
- event gate: `workflow_dispatch`;
- repository/ref/SHA/current-main fail-closed fence;
- trusted runner identity and labels `self-hosted, macOS, ARM64, everfield-unity`;
- `permissions: contents: read`;
- concurrency policy;
- `timeout-minutes: 30`;
- pinned checkout SHA `11d5960a326750d5838078e36cf38b85af677262`;
- pinned upload-artifact SHA `ea165f8d65b6e75b540449e92b4886f43607fa02`;
- pinned Unity editor `6000.5.6f1` and CLI/editor identity checks;
- deterministic producer/recorder self-tests;
- sanitized lineage shape assertions;
- upload path, retention, and fail-on-missing behavior.

The remediation neither weakens a trusted identity fence nor expands repository/token authority.

## Attack 5 — evidence semantics and historical state
PASS.

No producer or recorder Python file is changed. The S3 N1/N2/FI1 attempt identities, reset/workspace separation, lineage schema, sanitization rules, candidate-work semantics, and recorder trust boundary are untouched.

The evaluator continues to assert:
- `pass_for_comparison` is false;
- `integration_authority` is false;
- all 50 historical `NOT_RUN` cells are preserved;
- historical `NOT_RUN` cells are not mutated.

A future successful artifact upload would make a recorder-consumable exact-main lineage packet available; it would not by itself convert that packet into comparison PASS, verification PASS, or canonical evidence.

## Attack 6 — producer self-validation / execution boundary
PASS.

Issue #808 records no Unity dispatch from the producer branch, and review performed no producer-branch Unity dispatch. Review evidence is static/semantic plus already-existing exact-main recurrence evidence. Empirical effectiveness remains a post-integration exact-current-main test.

## Attack 7 — authority inflation
PASS.

Issue #808 terminal status, PR #809 description, and its handoff all preserve `NOT_CANONICAL` authority and explicitly deny comparison, verification, integration-by-producer, decision, readiness, and canonical grants.

Owner convergence directive Issue #84 comment `5277825639` permits squash-integration of an exact bounded remediation packet after its required clean review and current merge-compatibility checks, but only as noncanonical provenance/evidence. It does not bypass verification or canonicalization.

## Informational finding
`INFO-1 / EMPIRICAL_EFFECTIVENESS_DEFERRED`: `caffeinate -i` addresses macOS idle system sleep, not every possible host/network/runner-service liveness failure. That is not a correction-requiring defect in this bounded remediation. The exact empirical question must be tested only after reviewed squash publication by a fresh exact-current-main lineage run; if artifact publication still fails, reopen the liveness chain from that new observed failure rather than upgrading this review result.

## Final judgment
`PASS_FOR_INTEGRATION` with 0 BLOCKER, 0 MAJOR, and 0 correction-requiring MINOR findings.

The exact producer packet at PR #809 head `d82961e46caf0f0130626ca85ebd082f67e05f1a` is a bounded, fail-closed macOS idle-sleep liveness remediation with no observed expansion of evaluator trust, permissions, evidence semantics, or authority.

## Required next route
A separate integration task must re-derive current main/canonical binding, exact #808/#810 terminal identities, owner directive `5277825639`, PR #809 exact head/base/files/draft/merge compatibility, and duplicate ownership immediately before claim and immediately before merge. Only exact-head squash integration is permitted.

After reviewed publication, route a fresh exact-current-main execution/verification episode to determine whether native S3 plus sanitized artifact publication/recorder liveness succeeds. No stronger evidence status follows from this review or integration alone.
