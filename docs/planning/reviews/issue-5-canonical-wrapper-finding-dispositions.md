# Issue #5 Canonical-Wrapper Finding Dispositions — Issue #18

## Status

**Remediation issue:** #18  
**Candidate:** `docs/planning/12-planning-program-v1-bootstrap-safe-candidate.md`  
**Manifest:** `docs/planning/12-planning-program-v1-canonicalization-manifest.yaml`  
**Candidate state:** NON-CANONICAL / VERIFICATION CANDIDATE

## V5-B09 — ACCEPTED_AND_CORRECTED

**Finding:** Issue #16's wrapper retained active-looking Bootstrap Issue #5/#6/#16 instructions after header-only canonical promotion, so a post-terminal reader could see both the canonical `[PLAN-v1]` dispatcher and apparent instructions to replay completed bootstrap work.

**Correction:** Issue #18 adds one normative applicability guard shared by prose and manifest with four deterministic classifications:

1. `PRE_CANONICAL_BOOTSTRAP` — bootstrap verification/canonicalization remains active; Wave 1 normal selection is inactive.
2. `CANONICAL_UNBOUND_ACTIVATION` — only the named canonicalizer's verified post-merge activation sequence remains operational; all other bootstrap-numbered clauses are provenance-only.
3. `CANONICAL_ACTIVE` — exactly one normal queue exists: open `[PLAN-v1]`; every fixed bootstrap-numbered clause is `PROVENANCE_ONLY` and cannot create eligibility, demand replay, alter priority, block selection, or reactivate completed bootstrap work.
4. `CANONICAL_BINDING_MISMATCH` — fail closed to canonical recovery/reverification; never replay bootstrap by inference.

The guard explicitly survives mechanical promotion byte-identically. Present-tense wording in historical bootstrap provenance has no authority effect in `CANONICAL_ACTIVE`.

## Generic protocol preservation

The correction is intentionally an applicability overlay, not a protocol rewrite. Exact Issue #16/base blobs remain the source for V5-B03 through V5-B08 corrections. In particular:

- durable canonical binding remains based on program-blob identity plus activation-SHA ancestry;
- root phase converges on PLANNING;
- schema-3 field typing, ownership/status fencing, legacy bootstrap bridge, context/liveness rules, Wave 1 graph, and squash-only integration remain unchanged;
- `VERIFICATION_RESTART` and `VERIFICATION_REFRESH` remain active generic mechanisms after canonical activation when a current canonical task/revision contract invokes them;
- historical Bootstrap Issue #5 examples cannot create new future verification work by themselves;
- DEGRADED_SINGLE_AGENT remains an explicitly weaker evidence mode with reopen condition when stronger isolation/multi-agent capability exists;
- gameplay/high-throughput implementation remains blocked until later verified implementation readiness.

## Verification requirements

Issue #5 must verify the exact Issue #18 candidate/manifest/current-base tuple and rerun the full inherited scenario suite. The decisive V5-B09 regression is:

1. mechanically promote the wrapper;
2. resolve terminal Issue #6 canonical binding;
3. classify `CANONICAL_ACTIVE`;
4. verify every bootstrap-numbered next-action/eligibility clause is provenance-only;
5. verify the only normal work queue is open `[PLAN-v1]`;
6. verify generic schema-3 restart/refresh remain operational for future declared verification tasks.

## Disposition

**READY_FOR_REVERIFICATION.** No claim of PASS or canonicality is made by this remediation task. Issue #6 remains blocked until Issue #5 records a valid current-base PASS with zero BLOCKER/MAJOR.