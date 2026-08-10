# Planning Program v1 — Bootstrap-Final Verification Attempt

## Status

**Bootstrap issue:** #5  
**Mission ID:** `BOOTSTRAP-VERIFY-05`  
**Ownership generation:** `VERIFICATION_RESTART` comment `5244798747`  
**Independence mode:** `DEGRADED_SINGLE_AGENT`  
**Trust:** DEGRADED  
**Result:** **FAIL**  
**Canonicalization eligibility:** BLOCKED  
**Issue #16 candidate work SHA:** `5b1f4e91904e46e5311b0f9cb3318c32402d53a7`  
**Overlay candidate blob:** `d083e5bfa108360818898f9628e939f50b4f3940`  
**Overlay manifest blob:** `bca34638a054d725239b936dd8232a7d274e814d`  
**Base candidate blob:** `9829975eb3b8ac12b7dd8338a3569ff1a50cf309`  
**Base manifest blob:** `1f062de59afcfe8496b4cff0fdff594c2d5fd50c`  
**Adopted Wave 1 blob:** `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`  
**Verified base:** `main@03140f8875392450198c22d864664810e03d6865`  
**Cold-start input manifest blob:** `af6f2f9972948cc3533cd1dbf81361e3e9470dd9`  
**Simulation artifact blob:** `274c817ff68d80e6db2194b188c1404dc3b991fc`

The Issue #16 candidate remained immutable on `main`. This verifier episode used full `VERIFICATION_RESTART` after the prior terminal FAIL and reran the complete scenario matrix.

## Regression result

V5-B03 through V5-B08 now pass their regression scenarios. In particular:

- canonical binding remains valid after later unrelated `main` movement;
- root entry phase converges on PLANNING;
- legacy bootstrap → schema-3 ownership is executable;
- current-owner/head/work/type/provenance fencing is closed;
- degraded single-agent mode is explicit and evidence-heavy;
- changed payload after FAIL uses `VERIFICATION_RESTART`;
- unchanged payload PASS made stale by base drift uses `VERIFICATION_REFRESH` and full re-verification;
- older-base PASS cannot satisfy Issue #6 current-base selection.

One BLOCKER remains.

## V5-B09 — BLOCKER — promoted wrapper still exposes bootstrap-specific work-selection clauses

**Affected surface:** Issue #16 wrapper Sections 3, 6, and 8 plus header-only program promotion.

### Failure scenario

1. Issue #5 passes and Issue #6 follows the verified manifest.
2. Issue #6 promotes the wrapper by replacing only title/state/remediation/authority header literals; all body bytes remain.
3. Issue #6 completes terminal canonical binding and root entry documents direct fresh agents to open `[PLAN-v1]` work.
4. The now-CANONICAL wrapper still contains present-tense clauses including:
   - "The next Issue #5 episode after Issue #16 uses `VERIFICATION_RESTART`...";
   - the Bootstrap Issue #6 selection override;
   - "Issue #16 completion unblocks only Issue #5...".
5. No explicit applicability rule states that bootstrap-numbered clauses become historical/provenance-only after active canonical binding.
6. A cold-start reader therefore sees the canonical dispatcher plus active-looking instructions to replay completed bootstrap work.

### Why it blocks PASS

This is the same failure class as the earlier stale-bootstrap canonical-promotion defect: the canonical file must have exactly one operational current queue after activation. A reader must not infer from context which present-tense clauses have silently expired.

### Required correction

Add an explicit state/applicability guard, preserved by mechanical promotion, that makes all bootstrap-issue-specific clauses provenance-only after `State: CANONICAL` **and** active canonical binding resolution, while keeping generic schema-3/restart/refresh/canonical-binding rules active for future planning verification work.

Bounded remediation is Issue #18 — `[PLAN-BOOTSTRAP] Make final canonical wrapper bootstrap-safe`.

## Scenario disposition

Detailed evidence is `docs/planning/reviews/issue-5-bootstrap-final-verification-simulation.yaml`.

Every required scenario passes except post-terminal canonical wrapper work selection, which fails as V5-B09.

## Final disposition

**FAIL.** Issue #6 remains blocked. Issue #16 remains NON-CANONICAL and becomes `SUPERSEDED_FOR_VERIFICATION` when Issue #18 produces the guarded wrapper.

Issue #5 must fully verify the Issue #18 payload/current base after that remediation.