# Issue #5 Finding Dispositions — Planning Program v1 Remediation

**State:** REVIEWED-CANDIDATE SUPPORT  
**Bootstrap remediation issue:** #11  
**Finding source:** `docs/planning/reviews/planning-program-v1-cold-start-verification.md` at Issue #5 work commit `26a06f9ab78ede2c69107e3df3d2327e2aed18f0`  
**Remediated candidate:** `docs/planning/09-planning-program-v1-remediated-candidate.md`  
**Remediated manifest:** `docs/planning/09-planning-program-v1-canonicalization-manifest.yaml`

## Status

Both Issue #5 BLOCKER findings are **ACCEPTED_AND_CORRECTED**. Neither is rejected or deferred. The remediation remains NON-CANONICAL and requires a fresh independent Issue #5 re-verification before Bootstrap Issue #6 may act.

## Disposition table

| Finding | Severity | Disposition | Correction |
|---|---|---|---|
| V5-B01 | BLOCKER | ACCEPTED_AND_CORRECTED | The new candidate is written so bootstrap sections are provenance/conditional invariants rather than active next-step commands. The new manifest mechanically changes the candidate header plus two exact activation/provenance sentences, patches `AGENTS.md` and `START-HERE.md`, and adds a post-merge/pre-terminal Issue #6 barrier. A canonical reader cannot be told to repeat #5/#6 after terminal activation. |
| V5-B02 | BLOCKER | ACCEPTED_AND_CORRECTED | The new candidate and manifest define schema 2 with a closed registry of ten operational kinds, common envelope/authority metadata, exact required fields, enums/constants, predecessor predicates, tie rules, authority effects, terminal behavior, and a deterministic transition table. Unknown/incomplete/edited kinds fail closed. |

## V5-B01 correction details

The Issue #4 manifest's `all_other_bytes_identical` rule exposed bootstrap-only Sections 29–30 as active text after promotion. The remediation fixes that in three layers:

1. the Issue #11 candidate's Sections 29–30 are valid in both candidate and canonical states and explicitly distinguish pre-canonical gating from post-terminal provenance;
2. the Issue #11 manifest enumerates only exact literal replacements, including the canonical Section 9 activation precondition and Section 29 terminal-status boundary;
3. `AGENTS.md` and `START-HERE.md` replacement text explicitly handles the short window after the Issue #6 squash commit but before Wave 1 issue creation and terminal `INTEGRATION_STATUS`.

The resulting operational phases are deterministic:

```text
pre-merge: candidate NON-CANONICAL; Issue #6 cannot activate Wave 1
post-squash, pre-terminal: canonical files exist; only Issue #6 post-merge activation may proceed
post-terminal: bootstrap chain is provenance; normal queue is open [PLAN-v1] issues
```

No discretionary Issue #6 rewrite is authorized.

## V5-B02 correction details

Schema 2 registers exactly:

- `CLAIM`
- `ORPHAN_PROBE`
- `RESUME_INTENT`
- `RESUME`
- `RECOVER`
- `PROGRESS`
- `STATUS`
- `REVIEW_STATUS`
- `VERIFICATION_STATUS`
- `INTEGRATION_STATUS`

The manifest defines:

- common required fields and fail-closed unknown-field behavior;
- GitHub comment ID/server time as authority metadata;
- exact per-kind required fields;
- constants/enums;
- per-kind predecessor/source conditions;
- deterministic intent and ownership-grant winner rules;
- lease renewal requirements;
- task-class completion routes;
- review disposition routing;
- verification PASS/FAIL binding;
- post-squash integration/canonicality records;
- external supersession/invalidation authorization references;
- a full transition table;
- an expected-parent/non-force mutation fence.

The previous ambiguous rule "required fields for its kind" is replaced by a closed machine-readable registry. Unsupported or malformed comments have no authority effect.

## Additional remediation self-review correction

While checking V5-B01, Issue #11 found a related activation-window race: the entry documents would become canonical in the squash commit before Issue #6 had created the 23 Wave 1 issues and posted terminal status. The manifest now requires fresh agents in that window to inspect/complete only Issue #6 post-merge activation and explicitly forbids treating the absent Wave 1 queue as a liveness defect.

This is treated as part of V5-B01 rather than a new scope expansion because it is the same canonical-promotion/dispatcher-consistency surface.

## Immutable Wave 1 contract preservation

Issue #11 does not redesign the reviewed 23-mission Wave 1 DAG. The new manifest immutably adopts only these sections from Issue #4 manifest blob `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`:

- `issue_compiler`;
- `universal_root_acceptance`;
- `wave_1`;
- `non_root_optional_retrieval`;
- `next_wave_candidate_schema`.

Issue #4's `verification_contract` and `bootstrap_canonicalization` sections are explicitly not adopted.

## Re-verification requirement

A fresh independent Issue #5 verifier must verify the exact Issue #11 candidate/manifest work state, the adopted Wave 1 source blob, and the then-current `main` base. At minimum it must re-run both original BLOCKER scenarios plus the new post-merge/pre-terminal activation-window scenario and schema-2 malformed/competing-capsule simulations.

No PASS from the prior non-independent Issue #5 preflight exists or may be inferred. Bootstrap Issue #6 remains blocked until a fresh valid PASS is recorded.