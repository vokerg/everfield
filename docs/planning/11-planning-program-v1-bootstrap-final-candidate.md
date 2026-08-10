# Planning Program v1 — Bootstrap Final Candidate

**State:** REVIEWED-CANDIDATE-BOOTSTRAP-FINAL  
**Bootstrap remediation issue:** #16  
**Authority:** NON-CANONICAL until Bootstrap Issue #5 records PASS for this exact effective candidate/manifest state and Bootstrap Issue #6 performs verified squash-only promotion and terminal activation.  
**Scope:** Pre-implementation planning only; no gameplay implementation, final engine choice, or mass implementation backlog is authorized.

## 1. Exact composition

The effective candidate is a deterministic composition:

- base candidate: `docs/planning/10-planning-program-v1-final-bootstrap-candidate.md` at blob `9829975eb3b8ac12b7dd8338a3569ff1a50cf309`;
- adopt base Sections **2–23 inclusive**;
- exclude base header/Section 1, Section 24 bootstrap provenance, and Section 25 downstream gate;
- extend/override base Section 13 only for terminal-verification re-entry using Sections 3–5 below;
- replace base Section 19 verification-binding/Issue-6 selection clauses with Sections 2, 5, and 6 below; retain its squash/canonicalization safety clauses;
- apply this file as the overlay;
- machine composition is defined by `docs/planning/11-planning-program-v1-canonicalization-manifest.yaml` over exact base manifest blob `1f062de59afcfe8496b4cff0fdff594c2d5fd50c`.

Any missing/mismatched base blob or unresolved composition target is a verification failure. Issue #14 artifacts are `SUPERSEDED_FOR_VERIFICATION`, not CANONICAL.

All other Issue #14 corrections remain byte-for-byte normative: durable canonical binding, one PLANNING phase across entry docs, schema-3 typed status/ownership rules, mutation fencing, bootstrap bridge, FULL/DEGRADED independence modes, context budgets, no-READY recovery, reviewed 23-mission Wave 1 graph, squash-only integration, wave governors, and the implementation barrier.

## 2. Current-base verification authority

Verification authority is keyed by:

`(candidate_work_sha, manifest_identity, adopted_wave_1_contract_blob_sha, verified_base_main_sha)`.

Issue #6 may use only the highest-comment-ID valid verification result for the exact effective candidate/adopted-Wave1 tuple **and current main base**. It must be PASS with zero BLOCKER/MAJOR. Older-base PASS records are provenance only.

## 3. `VERIFICATION_RESTART`

`VERIFICATION_RESTART` creates a new schema-3 ownership generation for a verification issue after a terminal PASS or FAIL when declared remediation/revision changed candidate or manifest.

Validity requires: valid terminal source result; closed/completed remediation/revision issue; new candidate or manifest identity differs from source; new payload exists on current `main`; new verified base equals current `main`; observed head equals verification branch head; contenders bind the same source/new tuple/base/head; lowest valid GitHub comment ID wins; only the winner owns.

Restart always triggers **full normal verification** with a new FULL or DEGRADED independence episode. It carries forward no PASS authority.

The next Issue #5 episode after Issue #16 uses `VERIFICATION_RESTART` from formal FAIL comment `5244679631`.

## 4. `VERIFICATION_REFRESH`

`VERIFICATION_REFRESH` creates a new schema-3 ownership generation only when a valid PASS became stale solely because `main` advanced.

Validity requires: source is valid PASS; candidate/manifest/adopted-Wave1 identities exactly unchanged; old verified base is a strict ancestor of new base; new base equals current `main`; observed head equals verification branch head; contenders bind same source/new base/head; lowest valid GitHub comment ID wins; only winner owns.

After refresh, the verifier reruns the **full** required cold-start/adversarial suite with a new independence episode and new immutable evidence. Refresh is a liveness transition, not a compatibility waiver. Candidate/manifest change makes refresh invalid and requires restart/full verification.

## 5. Result lifecycle

After restart or refresh, ordinary mutation fencing applies. Final `VERIFICATION_STATUS` or `BOOTSTRAP_VERIFICATION_STATUS` binds current owner, head/work SHA, exact candidate tuple, current base, report/simulation evidence, and independence profile.

For one exact tuple/base, highest valid result comment ID is authoritative. FAIL routes remediation. PASS can unlock canonicalization only while its verified base remains current.

State machine:

```text
PASS(C,A) + main=A -> Issue #6 may be READY
PASS(C,A) + main advances to B -> VERIFICATION_REFRESH -> full verify -> PASS(C,B) or FAIL(C,B)
terminal result(C) + remediation produces D != C -> VERIFICATION_RESTART -> full verify(D,current-main)
```

Repeated drift repeats refresh. Candidate change never uses refresh.

## 6. Issue #6 override

Select highest valid `BOOTSTRAP_VERIFICATION_STATUS` matching the current effective candidate/adopted-Wave1 tuple and `verified_base_main_sha == current main`; require PASS/zero BLOCKER/MAJOR; only then Issue #6 is READY.

If no current-base PASS exists: unchanged candidate + older ancestor-base PASS → refresh; changed candidate/manifest → restart/full verification; current-base FAIL → declared remediation. No invented compatibility policy or human gate is required.

## 7. Canonicalization

Issue #6 promotes this wrapper to `docs/planning/PLANNING-PROGRAM-v1.md` using exact manifest header replacements. The canonical wrapper continues to compose the immutable Issue #14 base candidate blob plus this overlay.

AGENTS/START-HERE transforms, durable canonical binding, post-merge 23-issue Wave 1 instantiation, terminal `INTEGRATION_STATUS`, and squash-only rules are inherited from exact base manifest blob `1f062de59afcfe8496b4cff0fdff594c2d5fd50c` except at explicitly replaced overlay paths.

## 8. Verification and reopen conditions

Issue #5 must verify exact Issue #16 work SHA, overlay manifest identity, base candidate blob `9829975eb3b8ac12b7dd8338a3569ff1a50cf309`, base manifest blob `1f062de59afcfe8496b4cff0fdff594c2d5fd50c`, adopted Wave 1 blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`, current main, composition operations, restart/refresh races, evidence parity, and all V5-B03–B07 regressions.

Reopen if stale-base PASS can strand the graph; candidate change can use refresh; multiple restart/refresh owners can win; older results override current-base results; refresh evidence is weaker than normal verification; composition requires invented policy; base churn warrants integration locking; or stronger multi-agent/isolation capability becomes available.

PASS remains forbidden with unresolved BLOCKER/MAJOR. Issue #16 completion unblocks only Issue #5. Valid current-base PASS may unblock Issue #6; Issue #6 terminal binding activates Wave 1. Nothing here authorizes gameplay implementation.