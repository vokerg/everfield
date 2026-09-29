# Issue #1352 handoff — preserve readiness decisions across provenance integration

## Identity

- Mission: `FACTORY-READINESS-LIVENESS-REM-02`
- Issue: #1352
- Winning claim: comment `5890351292`
- Branch: `planning/issue-1352`
- Execution base: `main@4a5f81215d8274f6042dfcda1cf57ca7f60eb80b`
- Canonical binding: Issue #1147 comment `5675066392`
- Source failed producer: #1344 / PR #1349 head `83a52c6b6067b90755cb80743f7822ec9dc92595`
- Source required Review #1350 terminal: `5890320939` / `CHANGES_NEEDED`
- Finding: `READINESS_DECISION_MASKED_BY_LATER_INTEGRATION_PROVENANCE`

## Corrected runtime surface

### Base maintenance

`tools/planning/frontier_maintenance.py` candidate blob before this handoff commit:

`62f27fbad0fdfd0bc2237dd5c17e3c3532d02978`

The readiness-dead-end detector no longer chooses the latest operational record overall. It scans newest-to-oldest for the latest **valid implementation-readiness decision terminal** and validates, for each candidate:

- kind is `STATUS` or `VERIFICATION_STATUS`;
- state/terminal marker is appropriate;
- mission is implementation-readiness scoped;
- authority mode matches producer/verifier role;
- exact issue, owner-generation, actor, mission, SHA identities bind;
- canonical six-hour owner lease is valid at the candidate terminal;
- controlling directive temporal scope is valid, with only explicit historical #1038 exception.

Only after choosing the latest valid readiness decision does the guard ask whether that decision has an actionable route and whether it is blocked/not-ready.

Consequences:

- later integration/provenance records cannot erase the routing obligation;
- malformed later readiness-shaped records cannot mask an older valid decision;
- a genuinely newer valid readiness decision supersedes the older one;
- arbitrary legitimate `NONE` terminals outside the narrow contract remain untouched.

### Active v5

`tools/planning/frontier_maintenance_v5.py` candidate blob:

`dd79a64b28449cfb5dc076d4a327e03d87b4a964`

The scheduled v5 runtime invokes `base.materialize_readiness_dead_end_diagnostics(open_items)` and exposes `readiness_dead_ends_created` in its existing summary. Existing v2/v3/v4 transition, dedupe, dispatch, exact-main, and route-allowlist behavior is not otherwise changed.

## Regression coverage

The inherited base self-test now includes the source-review-required lifecycle:

1. readiness owner;
2. blocked/no-route readiness decision terminal;
3. later integration owner;
4. later `INTEGRATION_STATUS(DONE)`;
5. expected: the earlier blocked decision remains detected.

It also adds a newer valid READY readiness decision and requires that decision to supersede the older blocked decision.

Existing negative/fail-closed cases from #1344 are retained: routed decision, unrelated legitimate NONE, pre-directive scope, ready decision, edited/wrong directive, exact #1038 recovery suppression, malformed authority/ownership/SHA/lease handling.

## Self-review

- source MAJOR corrected in decision reconstruction: PASS by static inspection;
- required integration-provenance regression present: PASS by static inspection;
- genuine newer-decision supersession regression present: PASS by static inspection;
- active v5 call site present: PASS;
- no route/readiness/implementation authority fabricated: PASS;
- unrelated `NONE` terminals remain outside implementation-readiness decision filter: PASS;
- changed paths are limited to base maintenance, active v5 wiring, and this handoff: PASS.

A local clone/self-test could not be executed from the ChatGPT container because that environment cannot resolve GitHub. This is **not** recorded as a test PASS. Fresh required review must independently inspect the exact packet. After any integration, the repository's actual GitHub Actions maintenance workflow must run its py_compile + v5 inherited self-test chain successfully, and live reconciliation must report `reconciliation_complete: true` before the factory is called operationally healthy.

## Required fresh review

Fresh review must attack at minimum:

- integration provenance masking;
- malformed newer readiness decisions;
- genuine newer valid decision supersession;
- false positives on unrelated `NONE`;
- directive temporal/identity binding;
- six-hour ownership lease;
- recovery-note duplicate suppression;
- active v5 wiring;
- no authority inflation;
- exact-current-main compatibility.

No integration authority is created by this remediation producer.
