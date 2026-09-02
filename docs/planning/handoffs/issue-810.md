# Issue #810 handoff — Unity S3 v5 artifact-liveness remediation review

## Mission
`W2-ENG-TECH-UNITY-S3-V5-ARTIFACT-LIVENESS-REV-01`

## Review disposition
`PASS_FOR_INTEGRATION`

Findings: `0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR / 1 INFO`.

Trust mode: `DEGRADED_SINGLE_AGENT`. Reviewer actor is distinct from the #808 producer actor; producer branch was frozen and not edited. Reopen for stronger independent attack if `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE` becomes available and then-current repository authority requires it.

## Frozen judged candidate
- producer Issue #808 claim `5513102094`
- producer terminal `5513156000`
- producer PR #809, draft at review freeze
- exact base/main `eb81d354931c67ef2193f5242e49ee181a270b8c`
- exact producer head `d82961e46caf0f0130626ca85ebd082f67e05f1a`
- compare ahead 2 / behind 0 / merge base exact frozen main
- workflow base blob `188e84cf897ca0c09f862ffc03040fed1ce7cd87`
- workflow candidate blob `f9b15228744b6814094d4e64faec4b78f9f952f4`
- substantive workflow diff: fail closed unless `caffeinate` resolves and run only the long native producer under `caffeinate -i`
- producer/recorder Python, validation, evidence schema, upload action, runner identity, permissions, triggers, current-main fence, timeout, and Unity pin unchanged

## Recurrence attacked
- run `33642634779` attempt 1 / job `100289313431`: server job completion `15:04:02Z`; native runner step continues to `15:10:21Z`; native S3 + sanitization PASS; upload then `403 Forbidden: job is completed`.
- run `33595213169` attempt 2 / job `100160452746`: server completion `08:06:14Z`; native step continues to `08:12:30Z`; same PASS-then-upload-403 shape.
- run `33595213169` attempt 1 / job `100137172409`: native step about 23 seconds; upload succeeds.

The review treats idle sleep as a plausible bounded repository-controlled liveness cause, not as proven root cause. Empirical effectiveness is deferred to a fresh exact-current-main run after reviewed publication.

## `caffeinate` semantics
Darwin `caffeinate(8)` documents `-i` as preventing system idle sleep and states that when a utility is supplied the assertion persists for the utility's execution lifetime. The judged producer is passed directly as that utility, so there is no background inhibitor. Reference: https://keith.github.io/xcode-man-pages/caffeinate.8.html

`set -euo pipefail` plus `command -v caffeinate >/dev/null` fails closed if the guard is unavailable. The environment-prefix form preserves `PYTHONPYCACHEPREFIX` for the invoked utility/child process. No secret/permission/trust expansion was found.

## Authority
The review grants only `PASS_FOR_INTEGRATION` for exact PR #809 head `d82961e46caf0f0130626ca85ebd082f67e05f1a` as noncanonical remediation provenance under then-current authority. It grants no artifact-liveness proof, S3 comparison PASS, provider PASS, verification PASS, engine selection/readiness, release, decision, integration-by-review, or canonical authority.

Owner convergence directive Issue #84 comment `5277825639` permits exact-head squash publication of a clean-reviewed bounded remediation packet as noncanonical provenance after current merge-compatibility and ownership checks; it does not waive downstream verification.

## Required next route
Materialize/consume exactly one separately authorized integration task for exact producer PR #809. Integration must re-derive current main/canonical binding/review terminal/PR head-base-files/ownership, use squash only, and record the resulting main SHA without upgrading evidence status.

After publication, route a fresh exact-current-main Unity S3 lineage execution/verification episode. If artifact publication still fails, reopen from that newly observed failure.
