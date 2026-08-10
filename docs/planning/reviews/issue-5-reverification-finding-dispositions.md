# Issue #5 Re-verification Finding Dispositions

**State:** REVIEWED-CANDIDATE SUPPORT  
**Remediation issue:** #14  
**Candidate:** `docs/planning/10-planning-program-v1-final-bootstrap-candidate.md`  
**Manifest:** `docs/planning/10-planning-program-v1-canonicalization-manifest.yaml`

## Summary

All five BLOCKER findings from the second Bootstrap Issue #5 verification pass are **ACCEPTED_AND_CORRECTED**. None is rejected, silently deferred, or waived. The corrected artifacts remain NON-CANONICAL and must be re-verified by Issue #5 before Issue #6 may start.

| Finding | Disposition | Correction |
|---|---|---|
| V5-B03 | ACCEPTED_AND_CORRECTED | Replaces current-HEAD equality with durable canonical binding: program header locates canonicalization issue, matching terminal integration status binds current program blob, and activation SHA need only be ancestor/equal current main. A prior binding for a different current blob becomes `CANONICAL_BINDING_MISMATCH`, not a fake activation window. |
| V5-B04 | ACCEPTED_AND_CORRECTED | Verified Issue #6 transform now changes the `AGENTS.md` title, Status section, Current Phase section, cold-start section, and fully replaces `START-HERE.md`; all authoritative entry surfaces report PLANNING while retaining the implementation barrier. |
| V5-B05 | ACCEPTED_AND_CORRECTED | Adds exact bootstrap overlays. Existing Issue #5 uses a typed legacy HANDOFF predecessor → competing schema-3 `BOOTSTRAP_RESUME` → fenced ownership → `BOOTSTRAP_VERIFICATION_STATUS`. Unclaimed Issue #6 gets mission ID `BOOTSTRAP-CANON-06` and enters schema 3 through normal CLAIM. |
| V5-B06 | ACCEPTED_AND_CORRECTED | Schema 3 declares field types/nullability, closed allowed-field sets, owner/external authority modes, exact current-owner/head/work fences for specialized statuses, typed independence profiles, typed compatibility evidence, and external retirement for never-claimed work. |
| V5-B07 | ACCEPTED_AND_CORRECTED | Adds explicit `DEGRADED_SINGLE_AGENT` independence mode anchored to repository-visible Issue #5 comment `5244416013`, with role-episode separation, immutable candidate, cold-start input manifest, prior-rationale gate, evidence requirements, trust degradation label, separate remediation routing, and mandatory reopen when stronger isolation becomes available. |

## V5-B03 — durable activation lineage

The prior design made activation expire as soon as `main` advanced. The final candidate instead treats Issue #6's squash SHA as an **activation ancestor**, not perpetual HEAD. The canonical file itself identifies the canonicalization issue; its terminal `INTEGRATION_STATUS` identifies the exact canonical program blob and activation commit.

A later unrelated squash merge therefore preserves the binding. A later verified program revision changes the header and publishes a new binding. An unauthorized/current-blob mismatch with an older binding fails closed as recovery/reverification rather than replaying Issue #6.

## V5-B04 — one root phase

Issue #6 no longer patches only the dispatcher paragraph. The manifest mechanically replaces all root phase metadata that would otherwise remain bootstrap-specific. After terminal activation:

- `AGENTS.md` says PLANNING;
- `START-HERE.md` says PLANNING;
- canonical Planning Program says PLANNING;
- all three preserve the high-throughput implementation barrier.

## V5-B05 — bootstrap bridge

Issue #5 cannot be retroactively given a normal schema-3 CLAIM because its deterministic branch and legacy ownership history already exist. The bridge is therefore explicit and one-time:

1. Issue #14 completion causes a legacy-shaped Issue #5 `STATUS(HANDOFF_READY)` matching the manifest bridge contract.
2. Verifier contenders post `BOOTSTRAP_RESUME`; lowest valid comment ID for the exact predecessor/head wins.
3. That comment becomes a schema-3 ownership generation.
4. Verification writes are fenced like normal work.
5. Final bridge result is `BOOTSTRAP_VERIFICATION_STATUS` bound to report/simulation work state and exact candidate tuple.

Issue #6 has no existing branch, so no migration is needed. The verified manifest overlays its mission ID and it starts directly with schema-3 CLAIM after a valid bridge PASS.

## V5-B06 — closed authority schema

The new registry makes nullability fail closed and defines types for every authority field. Specialized review/verification/integration results must reference the **current unexpired ownership generation**, bind exact current branch head and immutable work state, and carry typed evidence/provenance.

`STATUS(EXTERNAL)` is the only no-owner result path. It is limited to `SUPERSEDED|INVALIDATED`, requires typed external authorization, and permits a null branch head only when no branch exists. This covers obsolete never-claimed tasks without fabricating ownership.

Base drift is no longer a prose exception: `compatibility_evidence` is either exact-base match or a typed re-verification artifact.

## V5-B07 — truthful degraded independence

The project currently has one available agent. The correction does not call that fully independent. Instead it creates a visible degraded mode with stronger procedural/evidence separation and a mandatory reopen condition.

A degraded reviewer/verifier must use a new role episode, never edit the candidate it judges, fix exact inputs in a cold-start manifest, gather fresh adversarial/mechanical evidence before prior rationale, disclose degraded trust, and route any correction into a separate remediation task. The current resource constraint is anchored by comment ID, so downstream validators can tell whether the mode is permitted.

When multiple agents or isolated execution contexts become available, degraded mode is reopened/disabled by governance rather than silently persisting.

## Remaining assumptions / reopen triggers

These are explicit risks, not blockers for this bootstrap candidate:

- procedural expected-parent fencing should later be strengthened by machine-enforced control-plane primitives;
- degraded single-agent independence is weaker than true isolation and must be measured for escaped defects;
- context and wave-size numeric governors remain provisional;
- canonical binding relies on Git ancestry and exact blob identity, both available from repository state.

Reopen if the Issue #5 simulation cannot deterministically execute the bridge, parse schema 3, resolve binding after a later-main simulation, or produce one unambiguous post-canonical phase.

## Verification readiness

The candidate is ready for Bootstrap Issue #5 re-verification of the exact Issue #14 work state. Issue #6 remains blocked until that re-verification records PASS.