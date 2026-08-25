# Issue #687 — terminal ownership and dispatch retry remediation

Source review: Issue #685 / PR #686 over immutable Issue #682 / PR #684 at `040ddf86a4c2a71a89693c741a05986ff96be5a1`.

## M03 closed — conservative terminal ownership binding
Automatic issue reconciliation now requires the latest trusted schema-3 operational record itself to be terminal and additionally proves a strict OWNER subset: matching issue, mission and actor, `authority_mode: OWNER`, concrete 40-hex head/work bindings, and an earlier referenced ownership-generating CLAIM/RESUME/RECOVER/BOOTSTRAP_RESUME from the same issue/mission/actor. Ambiguous, malformed, EXTERNAL, or stale-terminal shapes remain open for agent reconciliation instead of being auto-closed.

## M04 closed — retry-safe dispatch lifecycle
Factory transition issues no longer count as non-transition successors. A registered route remains eligible across maintenance runs until either (a) an exact-main matching workflow run is observed or (b) a trusted machine-readable factory dispatch marker exists. A successful dispatch records `factory_frontier_dispatch: 1`; a transient API failure leaves no marker, so the next maintenance run retries. Once marked, the transition issue owns downstream handling and maintenance stops automatic redispatch.

## Regression controls
The no-network `--self-test` now covers: valid bound terminal, later live claim suppression, missing ownership reference, actor mismatch, untrusted terminal, predecessor rejection prose, explicit rejected PR forms, normal successor consumption, factory-transition non-consumption, and trusted dispatch-marker route matching. The maintenance workflow still runs compile plus self-test before mutation.

Route allowlist, exact-main dispatch fencing, entry directives, workflow permissions, and all authority boundaries are otherwise unchanged. Fresh review is mandatory before squash-only integration.
