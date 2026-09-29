# Review — FACTORY-READINESS-LIVENESS-REM-02-REV-01

**Issue:** #1353  
**Producer:** #1352 / `FACTORY-READINESS-LIVENESS-REM-02`  
**Producer terminal:** `5890438163`  
**Producer PR:** #1354  
**Exact producer head:** `ff30aae75ffe80af627c8b9f68742a55522fcce0`  
**Review base:** `main@4a5f81215d8274f6042dfcda1cf57ca7f60eb80b`  
**Canonical binding:** Issue #1147 comment `5675066392`  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Disposition:** `PASS_FOR_INTEGRATION`

## Exact subject

- `tools/planning/frontier_maintenance.py` blob `62f27fbad0fdfd0bc2237dd5c17e3c3532d02978`
- `tools/planning/frontier_maintenance_v5.py` blob `dd79a64b28449cfb5dc076d4a327e03d87b4a964`
- `docs/planning/handoffs/issue-1352.md` blob `e7be600c6849f0a78e5065c7cf17630634285d27`

PR #1354 is exact-head, draft, mergeable, and changes only the three owned paths. Current main remains identical to the producer execution base at review freeze.

## Source finding reconstruction

Review #1350 terminal `5890320939` correctly rejected #1344 because its detector selected the latest operational record overall. A later `INTEGRATION_STATUS` could therefore hide the earlier blocked/no-route readiness decision.

The remediation changes the decision-reconstruction invariant itself rather than adding a special case around one historical issue.

## Attacks

### 1. Latest valid readiness decision reconstruction — PASS

The detector scans operational records newest-to-oldest but considers only terminal implementation-readiness `STATUS` / `VERIFICATION_STATUS` decision candidates.

Each candidate must independently satisfy issue, mission, authority-mode, ownership-generation, actor, SHA, six-hour lease, directive identity/temporal scope, and terminal validity before it can supersede an older decision.

Therefore a malformed newer readiness-shaped record cannot mask an older valid decision.

### 2. Later integration/provenance masking — PASS

`CLAIM` and `INTEGRATION_STATUS` records are not readiness decision terminals and are skipped when selecting the controlling decision.

The required regression explicitly constructs:

`blocked/no-route VERIFICATION_STATUS -> integration CLAIM -> INTEGRATION_STATUS(DONE)`

and requires the blocked decision to remain detected.

An isolated review harness executing the same corrected decision-selection logic passed this scenario.

### 3. Genuine newer readiness decision — PASS

A second regression creates a newer valid READY verification decision. That newer valid readiness decision is selected and supersedes the historical blocked decision, so no dead-end diagnostic is returned.

This avoids making historical blocked state permanent.

### 4. Legitimate NONE isolation — PASS

The detector still requires an implementation-readiness mission plus a valid blocked/not-ready decision. An unrelated terminal carrying `implementation_ready: false` and `required_next_route: NONE` is rejected by the mission filter.

Routed readiness decisions and ready decisions are also negative cases.

### 5. Authority / lease / temporal fail-closed behavior — PASS

The remediation preserves:
- exact trusted immutable owner directive binding;
- expected OWNER vs VERIFIER authority mode;
- exact ownership-generation actor/mission linkage;
- SHA-40 identities;
- canonical six-hour lease check;
- directive temporal scope with only explicit historical #1038 exception;
- no successor-route reinterpretation outside this narrow contract.

### 6. Historical #1038 recovery suppression — PASS

The historical #1038 blocked decision remains detectable structurally, but immutable owner recovery comment `5889876653` suppresses duplicate diagnostic creation because the explicit #1335–#1343 recovery chain already exists.

No readiness PASS or route authority is inferred from that suppression.

### 7. Active runtime wiring — PASS

The scheduled maintenance workflow executes `frontier_maintenance_v5.py`. The exact v5 packet calls `base.materialize_readiness_dead_end_diagnostics(open_items)` and reports `readiness_dead_ends_created` without changing v2/v3/v4 route/dedupe/dispatch logic.

### 8. Authority inflation — PASS

The guard can only create a diagnostic/recovery issue. It cannot set implementation readiness, create a PASS, authorize implementation, select a route outcome, merge code, or grant production/release/canonical authority.

## Validation boundary

The review independently executed the corrected core decision-selection scenarios in an isolated harness and they passed.

The full repository py_compile + inherited v5 self-test chain was not executed from the ChatGPT container because the container cannot resolve GitHub to materialize the repository branch. This is not represented as a full test PASS.

Accordingly, clean review eligibility is contingent on the exact reviewed bytes only. After squash integration, the repository-native GitHub Actions maintenance workflow must pass py_compile and the v5 inherited self-test, and live reconciliation must report `reconciliation_complete: true` before operational health is declared.

## Findings

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- informational: 1 (full repository runtime validation deferred to repository-native post-integration workflow)

## Result

`PASS_FOR_INTEGRATION`

This grants only separately claimed squash-integration eligibility for the exact producer packet. No implementation-readiness, implementation, production/release, decision, or canonical authority is granted.
