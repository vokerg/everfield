# Review — FACTORY-READINESS-LIVENESS-REM-01-REV-01

**Issue:** #1350  
**Producer:** #1344 / `FACTORY-READINESS-LIVENESS-REM-01`  
**Producer terminal:** `5890262283`  
**Producer PR:** #1349  
**Exact producer head:** `83a52c6b6067b90755cb80743f7822ec9dc92595`  
**Review base:** `main@765177165339039dab6f60a6f3dc315cd09b583f`  
**Canonical binding:** Issue #1147 comment `5675066392`  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Disposition:** `CHANGES_NEEDED`

## Exact reviewed packet

- `tools/planning/frontier_maintenance.py` blob `a10bb696f351816f532b510172618934ad0e7bd7`
- `tools/planning/frontier_maintenance_v5.py` blob `dd79a64b28449cfb5dc076d4a327e03d87b4a964`
- `docs/planning/handoffs/issue-1344.md` blob `32b2338b269321a250ce84899ceea11644c3724f`
- draft PR #1349, exact head above

The producer branch is immutable to this review.

## Finding

### MAJOR — a blocked readiness decision becomes invisible after normal provenance integration

The load-bearing detector is:

`readiness_dead_end_terminal_from_comments()`

It parses all trusted operational records, then selects:

`latest = max(records, key=lambda item: item.comment_id)`

and immediately rejects unless that latest record is `STATUS` or `VERIFICATION_STATUS`.

That is not the lifecycle invariant required by the owner routing directive. A normal readiness chain may contain:

1. an ownership `CLAIM`;
2. a terminal blocked/not-ready `STATUS` or `VERIFICATION_STATUS` with no actionable successor;
3. a separate integration `CLAIM`;
4. a later terminal `INTEGRATION_STATUS` publishing the blocked result as noncanonical provenance.

After step 4, the newest operational record is `INTEGRATION_STATUS`. The candidate therefore returns no dead end even though the underlying readiness decision still says blocked/not-ready and has no successor.

This is not hypothetical. Historical #1038 has exactly the relevant shape: verifier terminal `5651326367` represented `BLOCKED`, `implementation_ready: false`, and `required_next_route: NONE`; later integration provenance was published on the same issue.

The producer handoff also encodes the incorrect invariant as “the latest trusted schema-3 operational record is a terminal STATUS or VERIFICATION_STATUS”. Publication provenance must not erase an earlier still-controlling readiness decision.

### Regression gap

The added self-tests cover:
- a direct blocked/no-route readiness terminal;
- a routed terminal;
- an unrelated legitimate NONE terminal;
- temporal scope;
- ready state;
- directive integrity;
- the historical recovery-note suppression.

They do **not** cover the normal sequence:

`blocked/no-route readiness decision -> integration CLAIM -> INTEGRATION_STATUS(DONE)`.

The current implementation would fail that required regression.

## Required bounded remediation

A corrected packet must:

1. select the latest authoritative **implementation-readiness decision terminal** from eligible `STATUS` / `VERIFICATION_STATUS` records rather than selecting the latest operational record of any kind;
2. preserve the decision-routing obligation across later publication/integration provenance;
3. allow a genuinely newer valid readiness decision to supersede the older decision;
4. validate ownership/authority/SHA/lease/directive/temporal predicates against the selected decision terminal exactly as fail-closed as the current candidate;
5. add the missing regression with later integration CLAIM + `INTEGRATION_STATUS(DONE)` and require detection to remain true;
6. keep the existing negative test proving unrelated legitimate `NONE` terminals remain untouched;
7. update the handoff to describe the corrected invariant;
8. retain the active v5 runtime call and no-authority-inflation boundary.

Any byte change invalidates this review subject and requires a fresh required review of the remediation packet.

## Finding counts

- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 0
- informational: 0

## Authority boundary

This review grants no integration eligibility for producer #1344, no implementation readiness, no route authority, no verification PASS, no production/release authority, and no canonical authority.
