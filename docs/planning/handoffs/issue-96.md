# Issue #96 handoff — W2-REM-ACC-01

**Mission:** `W2-REM-ACC-01`  
**Issue:** #96  
**Branch:** `planning/issue-96`  
**Ownership generation:** Issue #96 comment `5271731759`  
**Actor session:** `w2-rem-acc-01-agent-20260812-2122-01`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Payload commit before handoff:** `3062e43775af51fcfc052d78520e5f6fe99d90bb`  
**Frozen source producer:** W2-ACC-01 / Issue #81 head/work `e009dd2e2deb9006f864e851ea84880ecc64cec2`  
**Source report blob:** `cd97806a06cd2aa3f97689ab7c32b3b631449b09`  
**Source handoff blob:** `a480ece0eb0cc4d3c2f674f3577c1a4f6a07f7aa`  
**Source terminal status:** Issue #81 comment `5270745594`  
**Independent pre-gate review:** Issue #81 comment `5271715858`  
**Corrected platform input:** W2-REM-PLAT-01 / Issue #92 work `9d51099be4d53eff876104f482e3c163d34519e3`  
**Remediation report blob:** `b5f0669a5c9e8fc242b96eabf1a32bc21c0248ee`  
**Requirement-policy blob:** `78690cf658967b2ded35e738df125959a56f0d86`  
**Finding-dispositions blob:** `78576cac9f7cdeaf2552235d19cac01cba7b099b`  
**Current-source observation date:** `2026-08-12`  
**Required formal review:** `W2-REV-01`

## Completed remediation

This bounded revision addresses the exact pre-gate findings without editing the frozen Issue #81 producer branch.

### `PG-ACC-M01` — accepted/corrected

The producer's coarse assertion that every applicable/conditional guideline already had a complete evidence/gap mapping is withdrawn.

A new versioned machine-readable policy now:

- treats source clauses rather than guideline-level summaries as the acceptance unit;
- binds exact source/version/scope, deterministic applicability, exact thresholds/semantics where present, and evidence/gap references;
- keeps empirical checks `NOT_RUN` until actual evidence exists;
- rejects unknown/unmapped/summary-only current-scope clauses as `MAPPING_INCOMPLETE`;
- derives aggregate mapping state rather than accepting a hand-authored completeness boolean;
- atomically expands the XAG 101 and XAG 107 requirements specifically exposed by the independent pre-gate review; and
- marks XAG 102–106 and 108–123 `GUIDELINE_SUMMARY_ONLY`, with atomic expansion required before aggregate mapping completeness can become true.

The resulting authoritative candidate truth is intentionally fail-closed:

```yaml
blocker_id: IR-BLOCKER-ACCESSIBILITY-CURRENT
blocker_authority_state: OPEN
catalog_mapping_complete: false
mapping_state: PARTIAL_ATOMIC_MAPPING_REMEDIATED_PENDING_EXPANSION_AND_INDEPENDENT_REVIEW
required_next_authority: W2-REV-01
```

The retained incompleteness is the correction: an omitted source clause can no longer disappear behind a coarse guideline PASS.

### `PG-ACC-m01` — accepted/corrected

Direct public Valve Deck compatibility checklist requirements remain typed `PLATFORM_COMPATIBILITY_REQUIRED`.

Windows-build-on-Deck/SteamOS-via-Proton execution is now `ACC-PROJECT-DECK-PROTON-01` under `PROJECT_SELECTED_PLATFORM_EVIDENCE`, sourced from corrected `PLAT-PC-FIRST-R1` plus Valve's documented Proton behavior. It is no longer represented as a separate direct Valve `Verified` checklist requirement.

## Exact artifacts

- `docs/planning/wave-2/research/accessibility-current-requirements.md` — remediation report / overlay, blob `b5f0669a5c9e8fc242b96eabf1a32bc21c0248ee`.
- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml` — machine-readable fail-closed policy, blob `78690cf658967b2ded35e738df125959a56f0d86`.
- `docs/planning/wave-2/reviews/w2-acc-01-pre-gate-review-dispositions.md` — accepted finding dispositions, blob `78576cac9f7cdeaf2552235d19cac01cba7b099b`.
- this handoff — exact blob to be bound by the final branch head/terminal status.

## Verification performed

- Policy YAML parsed successfully before repository publication.
- 28 atomic clause records were mechanically checked for resolvable `evidence_requirement_refs` and `gap_refs`; no dangling references were found.
- Branch-stored report/policy/disposition blob identities were re-fetched after the first fast-forward mutation and match the expected blobs above.
- Current first-party Microsoft XAG and Valve Deck sources were rechecked for load-bearing remediation claims; no material drift was found for the exact requirements represented here.
- Source authority remains separated: XAG best practice, direct Valve compatibility checklist, project-selected platform evidence, and unknown legal/partner certification.
- No empirical accessibility PASS, legal compliance result, Valve compatibility result, engine selection, implementation-readiness transition, or canonicalization authority is claimed.

## Self-review

Bounded remediation self-review:

- unresolved BLOCKER: **0**;
- unresolved MAJOR: **0**;
- correction-requiring MINOR: **0**;
- both pre-gate findings explicitly dispositioned: **PASS**;
- source producer/review provenance immutable and exact: **PASS**;
- XAG 101/107 attacked clauses represented atomically: **PASS**;
- remaining XAG summary-only pages fail aggregate mapping closed: **PASS**;
- `NOT_RUN` versus `NOT_APPLICABLE` preserved: **PASS**;
- direct Valve vs project-selected Proton authority separated: **PASS**;
- formal independent review still required: **PASS**.

## Remaining work / risk

The largest retained gap is deliberate and machine-visible: XAG 102–106 and 108–123 still require atomic source-clause expansion (or exact scope-based deferral) before `catalog_mapping_complete` can become true. This remediation prevents false closure; it does not silently do a broad new accessibility research wave under a bounded fix.

Formal `W2-REV-01` must independently adjudicate this remediation together with the frozen producer provenance. If later work requires the blocker to advance beyond OPEN, it must satisfy the policy's exact completeness predicate and the declared review/readiness route.

## Stopping rule

After committing this handoff, perform a cold diff/self-review from current `main`, confirm only the four declared Issue #96 paths changed, verify ownership/head fencing again, then publish schema-3 `STATUS(REVIEW_READY)` for the exact final branch head. Freeze the branch after terminal status and record durable supersession linkage on Issue #81.

Do not create an integration PR or merge to `main` from this remediation without a later declared review/verification/integration authority. Main integration, if later authorized, remains squash-only.
