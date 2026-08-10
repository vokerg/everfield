# Planning Program v1 — Cold-Start Verification

## Status

**Bootstrap issue:** #5  
**Role:** Independent cold-start verifier (human-directed preflight episode; independence gate not satisfied)  
**Result:** **FAIL**  
**Canonicalization eligibility:** BLOCKED  
**Candidate work SHA:** `1d7b9a980e74d6999789c86694f3c7fb99e13b99`  
**Issue #4 final branch head:** `a47c88151b92c45235d92b6b6bdf5d74ef4f49b6`  
**Candidate blob:** `1170d97490c2a4ccbf1b9f51191ce97123536439`  
**Canonicalization manifest blob:** `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`  
**Issue #3 disposition blob:** `921977edb4bddc7126daeb05b86df7677a161858`  
**Verification base main SHA:** `c59ad1ef4b9eb1cd42b2349d0f5c7ee7860bddc9`

This verification episode was started under an explicit human directive in the same execution context that previously synthesized Issue #4. It therefore does **not** satisfy the candidate's distinct cold-start independence requirement and cannot establish a valid PASS. It can safely establish FAIL when defects are reproducible from repository + GitHub state alone. Two BLOCKER defects were found.

The three substantive Issue #4 verification artifacts are byte-identical between Issue #4 `work_sha` and current `main` by Git blob identity, so the findings below apply to the exact candidate payload now preserved on `main` as non-canonical provenance.

## Cold-start procedure followed

For this episode, project evidence was re-derived from repository + GitHub state:

1. read `/AGENTS.md` from current `main`;
2. read `docs/planning/START-HERE.md` from current `main`;
3. read Bootstrap Issue #5;
4. inspected Issue #4 final `VERIFICATION_READY` status and squash-provenance integration status;
5. bound the exact Issue #4 candidate, disposition artifact, canonicalization manifest, and current `main` SHA;
6. inspected the candidate's cold-start, capsule/state, recovery, review-transition, context, Wave 1 activation, canonicalization, and implementation-readiness rules;
7. simulated the required adversarial scenarios below.

No prior chat content is used as evidence for the findings.

## Entry-workflow questions

| Question | Repository/GitHub-derived answer | Preflight result |
|---|---|---|
| Current phase | `PLAN-THE-PLAN` until Issue #6 canonicalizes; candidate describes post-bootstrap PLANNING phase | Determinable |
| Currently eligible work | Bootstrap #5 is current verification work; #6 requires a valid #5 PASS | Determinable |
| Priority with multiple tasks | Candidate queue class, then lower `priority_rank`, then issue number | Determinable in intended post-bootstrap model |
| New/claimed/resumable/blocked/review-ready/complete | Derived from branch + prerequisites + operational capsules | **Not fully deterministic; see V5-B02** |
| Branch/base | Deterministic `planning/issue-N`; new work from current main unless issue says otherwise | Determinable |
| Context to load | Entry docs + canonical program + issue-declared bounded packet | Determinable, subject to provisional packet-budget assumptions |
| Output/schema | Issue contract + manifest | Determinable for Wave 1 missions |
| Acceptance/evidence | Issue contract + schema classes | Determinable |
| Independent review path | Explicit mission review/synthesis/verification graph | Determinable |
| Stopping/handoff | Commit useful state, handoff file, final status with exact head | Determinable |
| Downstream unblocked | Exact review-disposition predicates / manifest graph | Mostly determinable; status validator defect remains |
| No normal eligible work | recover handoff/stale/orphan first; otherwise conditional recovery mission | Determinable in prose, but capsule validity gap affects execution |

## Adversarial scenario results

| Scenario | Result | Evidence/conclusion |
|---|---|---|
| Two agents claim same new work | PASS in design | deterministic branch creation serializes first creation; loser must not create alternate branch |
| Agent disappears after branch creation before claim | PASS in design | orphan probe + server-age grace provides eventual recovery |
| Agent disappears after claim / no useful handoff | PASS in design | lease expiry + recovery path exists; mutation fence is intended to revoke stale-generation authority |
| Intentional handoff race | **BLOCKED by V5-B02** | earliest `RESUME_INTENT` rule exists, but exact intent/status capsule schema and complete validity predicates are not defined |
| Review rejects proposal | PASS in design | `CHANGES_REQUIRED` routes to declared synthesis; `INVALIDATED` routes only to recovery/replanning |
| Dependency invalidated | PASS in design | invalidation/recovery route exists |
| No READY tasks | PASS in design | candidate Section 16 defines liveness classification and single-use recovery task |
| Stale planned work after architecture changes | PASS in design | garbage-collection/supersession rules exist |
| Agent starts implementation too early | PASS in design | candidate and entry rules explicitly block gameplay/high-throughput implementation until later readiness gate |
| Author/evaluator self-canonicalizes | PASS in design | candidate prohibits producer self-canonicalization and requires independent verification/integration roles |
| Canonical promotion after #6 | **FAIL — V5-B01** | verified manifest's byte-preserving transform leaves stale bootstrap-next-step sections active in the canonical program |
| Malformed/edited/ambiguous operational comment | **FAIL — V5-B02** | validator depends on per-kind required fields/transitions that are not fully enumerated |

## Findings

### V5-B01 — BLOCKER — Verified canonical promotion creates a self-contradictory dispatcher

**Affected surfaces:** candidate Sections 9, 20, 22, 29, 30; `docs/planning/08-planning-program-v1-canonicalization-manifest.yaml` `bootstrap_canonicalization.program_promotion`.

**Failure scenario:**

1. Issue #5 passes the current candidate.
2. Issue #6 follows the verified manifest exactly.
3. The manifest changes only three header literals and requires `all_other_bytes_identical: true`.
4. `docs/planning/PLANNING-PROGRAM-v1.md` therefore still contains candidate Section 29 saying Bootstrap Issue #5 is the required next role and Section 30 saying only #5 is newly eligible and #6 is still pending.
5. At the same time, the manifest replaces `AGENTS.md` / `START-HERE.md` so they say Bootstrap #2–#6 are provenance and fresh agents must query `[PLAN-v1]` work after #6.
6. A cold-start agent now has two active instructions about what happens next: enter Wave 1, or execute the already-completed bootstrap verifier/canonicalizer chain.

**Why this blocks PASS:** The exact artifact that becomes canonical is not internally consistent in its post-bootstrap operational state. The verifier cannot authorize Issue #6 to perform an unverified discretionary rewrite because F-04 specifically required canonicalization to be mechanically constrained.

**Required correction:** Produce a new reviewed remediation candidate/manifest whose verified promotion either (a) promotes a dedicated post-bootstrap canonical-form artifact, or (b) explicitly and mechanically removes/replaces all bootstrap-only operational sections. Re-run independent cold-start verification against the exact remediated work state.

### V5-B02 — BLOCKER — Operational capsule validity still requires an invented per-kind schema/transition interpreter

**Affected surfaces:** candidate Sections 10–14.

**Failure scenario:**

1. Candidate Section 10.2 says an operational capsule is valid only when the required fields for its `kind` are present/type-valid and the predecessor/state transition is allowed.
2. Section 10.3 gives an exact YAML field set only for ownership-granting `CLAIM | RESUME | RECOVER`.
3. The program also relies on `ORPHAN_PROBE`, `RESUME_INTENT`, `PROGRESS`, handoff/status capsules, review completion/disposition, verification status, integration status, and terminal/supersession/invalidation records.
4. Their complete required fields, predecessor references, uniqueness/tie predicates, and allowed transition table are not enumerated as a versioned schema.
5. Two compliant cold-start agents can therefore disagree whether a partially populated `RESUME_INTENT`, `PROGRESS`, `STATUS`, or terminal comment is valid, which changes lease ownership, recovery eligibility, downstream prerequisites, or terminal state.

**Why this blocks PASS:** Eligibility and ownership are defined as functions of the "latest valid" operational state. If validity itself requires policy invention, repository + GitHub state is not a deterministic dispatcher.

**Required correction:** Define a complete versioned capsule-kind registry covering every operational kind used by Planning Program v1. For each kind specify exact required/optional fields, reference/SHA invariants, allowed predecessor kinds/states, ordering/tie rules, authority effect, terminal/supersession behavior, and fail-closed treatment. The issue compiler/verification manifest must make this schema part of the exact verified payload.

## Other observations

- The temporary mutation fence is implementable in principle with current GitHub tooling using an old-head parent commit followed by a non-force branch ref update: if the branch advanced, the ref update is non-fast-forward and fails. This should still be exercised by a genuinely independent verifier after remediation.
- Numeric context and Wave-frontier caps remain explicitly provisional assumptions with reopen conditions; no additional BLOCKER is asserted here solely from those provisional values.
- This episode's own independence gate is not satisfied. That prevents PASS but is not the reason for the two findings above; each is directly reproducible from the committed candidate and manifest.

## Result

**FAIL.** Bootstrap Issue #6 remains blocked. The Issue #4 candidate remains `REVIEWED_CANDIDATE_NON_CANONICAL` and must not be promoted.

Bounded remediation is tracked in **Issue #11 — `[PLAN-BOOTSTRAP] Remediate Issue #5 cold-start verification blockers`**.

After Issue #11 produces an exact remediated candidate/manifest, a **fresh independent execution context** must resume/re-run Issue #5 and verify that exact work SHA against the then-current verified base. This report may be used as prior failure evidence only after the fresh verifier first performs its own cold-start inspection, per the independence rule.
