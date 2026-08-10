# Planning Program v1 — Cold-Start Re-verification

## Status

**Bootstrap issue:** #5  
**Role:** cold-start verifier episode under recorded single-agent operating constraint  
**Result:** **FAIL**  
**Canonicalization eligibility:** BLOCKED  
**Remediation source issue:** #11  
**Remediation work SHA:** `7ed2d734645adf93910ce60156ec8b45d528fa73`  
**Remediation final branch head:** `2dd05c75915ebefdfb815afffbac7f46f3154912`  
**Candidate blob on current main:** `5e60d827ab99fe04e8a23c4addfc59d6f418d281`  
**Manifest blob on current main:** `9ecad20d9332eb1b649dfcb16beece5cda3fa330`  
**Adopted Wave 1 source blob:** `d7ba9d5e9f6afe6b83837f2da13831873a5b8ddd`  
**Verified base inspected:** `main@fce7218a1e7a4b03bae04aead80f12f5039848fb`

The Issue #11 remediation is durable on `main` as NON-CANONICAL provenance. This episode re-derived the entry workflow and candidate/manifest behavior from current repository + GitHub state before using the previous FAIL as a regression target.

The project owner has recorded that the project currently has one available agent. That prevents claiming full independent-agent separation. This report therefore treats single-agent verification as a visible trust constraint; it does not hide that limitation. The FAIL below is nevertheless authoritative enough to keep Issue #6 blocked because every finding is reproducible from committed text/state without relying on prior private reasoning.

## Cold-start procedure

1. Read current `/AGENTS.md`.
2. Read current `docs/planning/START-HERE.md`.
3. Read Bootstrap Issue #5 and its repository-visible handoff/status.
4. Bind current main and the Issue #11 candidate/manifest blobs.
5. Read the remediated candidate before reconciling prior failure rationale.
6. Inspect the schema-2 registry and proposed root-entry transformations.
7. Simulate claim/recovery/status, canonical promotion, post-merge activation, later-main movement, retirement, and bootstrap-to-canonical authority transitions.
8. Reconcile previous findings only after the remediated payload was independently inspected.

## Entry-workflow questions

| Question | Re-verification result |
|---|---|
| Current project phase | Determinable **during bootstrap** from current entry docs; proposed post-canonical phase is contradictory because `AGENTS.md` remains `PLAN-THE-PLAN` while replacement `START-HERE.md` says `PLANNING` (V5-B04). |
| Currently eligible work | Bootstrap #5 is current; #6 remains blocked on PASS. |
| Priority with multiple tasks | Candidate defines queue class → `priority_rank` → issue number. |
| New/claimed/resumable/blocked/review-ready/complete | Improved substantially by schema 2, but terminal/status validity remains under-specified (V5-B05/V5-B06). |
| Branch/base semantics | Deterministic branches and current-main base are clear. |
| Context to load | Determinable with 100k fallback and no-silent-truncation rule. |
| Output/schema | Wave 1 issue compiler/adopted manifest provides paths/schemas. |
| Acceptance/evidence | Determinable for normal missions; specialized status evidence binding still incomplete (V5-B06). |
| Independent review path | Declared, but current one-agent environment has no liveness-safe truthful mode (V5-B07). |
| Stopping/handoff | Determinable. |
| Downstream unblocked | Review disposition routing is clear; bootstrap bridge remains undefined (V5-B05). |
| No normal eligible work | Liveness path is clear, including post-Issue-6 activation special case, but activation anchoring is not durable across later main movement (V5-B03). |

## Regression status for previous blockers

### V5-B01 — stale bootstrap instructions after canonical promotion

**Core defect corrected.** The remediated candidate body is valid in pre-canonical and post-canonical forms and no longer directs a fully activated agent to repeat #5/#6.

However the new activation test uses equality with the current main SHA, creating V5-B03 below.

### V5-B02 — implicit capsule-kind registry

**Partially corrected, not closed.** The manifest now enumerates kinds, required fields, predecessor conditions, tie rules and transition effects. Remaining authority/type/bridge ambiguities are material enough to keep PASS blocked (V5-B05/V5-B06).

## Findings

### V5-B03 — BLOCKER — canonical activation record expires when `main` advances

**Affected surfaces:** candidate §§9, 20, 22, 29, 30; manifest `agents_entry_patch`, `start_here_replacement`, `bootstrap_canonicalization`.

**Failure scenario:**

1. Issue #6 canonicalizes at squash SHA `A` and posts terminal `INTEGRATION_STATUS(main_sha=A)`.
2. Wave 1 becomes active correctly.
3. Any later accepted planning task squash-merges, moving `main` to `B`.
4. Canonical `AGENTS.md` / `START-HERE.md` require Issue #6 terminal status for the "exact current canonical main SHA".
5. The only valid Issue #6 activation status names `A`, not current HEAD `B`.
6. A fresh agent therefore enters the Issue #6 completion path instead of the open `[PLAN-v1]` queue even though bootstrap finished.

**Required correction:** bind activation to durable canonical lineage, not HEAD equality. The active canonical integration record should remain valid while its activation SHA is an ancestor of current main and the currently referenced canonical-program identity matches that activation lineage, until superseded by a later canonical integration record.

### V5-B04 — BLOCKER — canonical root entry still reports two phases

**Affected surfaces:** current `AGENTS.md` `Status`/`Current Phase`; manifest `agents_entry_patch`; manifest `start_here_replacement`.

The verified transform replaces only the `Mandatory Cold-Start Entry Point` section. After Issue #6, root `AGENTS.md` would still say `Current Phase: PLAN-THE-PLAN`, while replacement `START-HERE.md` says `Phase: PLANNING` and canonical Planning Program v1 activates detailed planning.

Issue #5 explicitly requires a fresh agent to determine current project phase and detect contradictions among entry documents. Two active phase declarations fail that test.

**Required correction:** make the deterministic Issue #6 transform update root phase/authority metadata together with the entry section, while preserving the no-gameplay/high-throughput-implementation barrier.

### V5-B05 — BLOCKER — bootstrap #5/#6 cannot deterministically enter schema 2

**Affected surfaces:** Bootstrap Issues #5/#6; candidate §§11–14, 22; manifest `verification_contract`, `operational_capsules`, `INTEGRATION_STATUS`.

Issue #5 and #6 were created under the legacy bootstrap protocol. They have no schema-2 mission IDs and their existing branches/ownership comments are not schema-2 grants. Yet the remediated canonical model expects a schema-2 verification/integration chain with `ownership_generation_comment_id`, `mission_id`, and a valid referenced `VERIFICATION_STATUS`.

For the already-existing `planning/issue-5` branch there is no legal schema-2 transition from the legacy HANDOFF state: a new schema-2 `CLAIM` is invalid because the branch already exists, and schema-2 `RESUME` requires a schema-2 `STATUS(HANDOFF_READY)` backed by a schema-2 owner that never existed. Issue #6 likewise has no manifest-assigned bootstrap schema-2 mission identity.

**Required correction:** define an explicit legacy-bootstrap bridge with exact bootstrap identities and exact authoritative PASS/claim/integration record formats, or an equally deterministic migration transition. Issue #6 must be able to validate the exact Issue #5 PASS without inventing a mission ID or ownership predecessor.

### V5-B06 — BLOCKER — schema-2 authority remains insufficiently typed/fenced

**Affected surface:** manifest `operational_capsules` and `transition_table`.

The registry enumerates required field names but lacks a closed field type/nullability registry. More importantly:

- `REVIEW_STATUS`, `VERIFICATION_STATUS`, and `INTEGRATION_STATUS` require an `ownership_generation_comment_id` but do not state that it must equal the current valid unexpired owner generation at publication time;
- specialized result capsules do not consistently bind their own `work_sha` and branch `head_sha`, so result content can be path-bound rather than immutably work-state-bound;
- `PASS_requires_fresh_independent_context` has no complete required machine-visible provenance fields by which a validator can decide that predicate;
- base-drift compatibility/reverification is permitted but no conditional required field identifies the compatibility/reverification evidence record;
- external `STATUS(SUPERSEDED|INVALIDATED)` for never-claimed work is ambiguous because `ownership_generation_comment_id` is unconditionally required and nullability/external-authority typing is undefined.

A stale reviewer/verifier or two cold-start validators can therefore disagree about whether a terminal result is valid. This reopens the stale-writer and hidden-interpreter failures schema 2 was meant to close.

**Required correction:** closed field/type/nullability registry; current-owner/unexpired-lease predicate or explicit typed external-authority path for every authority-bearing result; own work/head binding; machine-visible independence mode/provenance; explicit base-drift evidence reference; deterministic representation of external retirement for unclaimed work.

### V5-B07 — BLOCKER — mandatory independence has no truthful single-agent liveness mode

**Affected surfaces:** candidate §§7, 19, 28; manifest `verification_contract`, `VERIFICATION_STATUS`.

The current project environment has one available agent. The candidate requires a fresh independent execution context but supplies no bounded degraded mode when no second project agent/runtime context can be spawned. Waiting indefinitely violates the autonomous liveness/no-routine-human-gate principles; setting the existing `PASS_requires_fresh_independent_context` flag to true without a distinct context would be false evidence.

**Required correction:** define an explicit degraded single-agent independence mode activated only by repository-visible owner/resource constraint. It must be labeled degraded, use a separate role episode, prohibit candidate edits during its verification episode, require a repo/GitHub-only cold-start input manifest and fresh adversarial/mechanical evidence before prior rationale, and carry a reopen condition for stronger multi-agent isolation. The mode is a liveness fallback, not full independence.

## Other scenario results

- Deterministic branch creation remains a credible new-claim exclusion primitive.
- Orphan probe + intent competition now has a closed high-level route.
- Handoff and stale recovery tie-breaking are explicit.
- `CHANGES_REQUIRED` vs `INVALIDATED` routing is explicit.
- Domain synthesis `REVIEW_READY` vs final synthesis `VERIFICATION_READY` remains correct.
- Context-budget fallback is deterministic when the execution window is unknown.
- No-READY recovery remains bounded.
- Candidate still prohibits premature gameplay/high-throughput implementation.
- Squash-only integration remains explicit.

These passing scenarios do not offset the bootstrap/canonical authority blockers above.

## Result

**FAIL.** Bootstrap Issue #6 remains blocked. Issue #11 artifacts remain NON-CANONICAL and are superseded for verification once the bounded remediation below exists.

Bounded remediation is tracked in **Issue #14 — `[PLAN-BOOTSTRAP] Remediate Issue #5 re-verification boundary blockers`**.

After Issue #14 produces the corrected candidate/manifest, Issue #5 must re-verify that exact payload and current base. Because the project currently has one available agent, that next verification must use the explicit degraded-independence protocol defined by Issue #14 rather than pretending full independent-agent separation.