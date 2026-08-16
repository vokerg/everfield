# W2 Narrative Root Required Review

**Mission:** `W2-CONTENT-NARR-REV-01`  
**Issue:** #394  
**Task class:** `REQUIRED_REVIEW`  
**Trust mode:** `DEGRADED_SINGLE_AGENT`  
**Judged producer:** Issue #369 / `W2-CONTENT-NARR-01`  
**Disposition:** `CHANGES_NEEDED`  
**Canonicality:** `NOT_CANONICAL`

## 1. Review authority and recovery provenance

This review is the required root review of the immutable Issue #369 narrative/quest/consequence producer packet. It was recovered from a stale ownership generation rather than restarted or reassigned in place.

- original review claim: Issue #394 comment `5306040131`;
- stale-source expiry: `2026-08-16T10:05:53Z`;
- recovery intent: `5307229796`;
- winning recovery generation: `5307230701`;
- recovered branch head before review work: `1f94804059ea8ea3b4c4cfd40c1f8da54627ed7a`;
- recovered substantive review work: none;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner parallel-frontier directive: Issue #84 comment `5305563203`.

Stronger reviewer isolation is unavailable, so this report does **not** claim full independence. `DEGRADED_SINGLE_AGENT` is preserved explicitly.

## 2. Frozen judged identity

The reviewed producer identity is immutable:

- producer Issue #369 / `W2-CONTENT-NARR-01`;
- producer claim `5305987782`;
- producer terminal `5306009345`;
- claimed base `32637bf66d8e76a4f029c9ca74f983cbe5535ffb`;
- substantive work `bee0fdca2b54e52626be3fcd142303037538e860`;
- terminal/head `8531deaccee19bf0ebad36315d1227d8873f9a39`;
- draft PR #393, exact head `8531deaccee19bf0ebad36315d1227d8873f9a39`;
- changed paths exactly:
  - `docs/planning/wave-2/content/narrative-quest-architecture.md`;
  - `docs/planning/wave-2/content/narrative-quest-architecture.yaml`;
  - `docs/planning/handoffs/issue-369.md`.

PR #393 remains draft, open, mergeable at review time, and is judged only as immutable producer provenance. Draft state or mergeability grants no integration authority.

Frozen shared game-design authority used by this review includes W1-SYN-GAME exact work `e74e0b0c95e85f69718868eedae324a298f02f3e`. In that exact candidate, `ProgressionGateContract` is defined as an object with its own `version: 1` field.

## 3. Review result

| Severity | Count |
|---|---:|
| BLOCKER | 0 |
| MAJOR | 0 |
| correction-requiring MINOR | 2 |

Exact correction-requiring findings:

- `W2-CONTENT-NARR-REV-MIN01`
- `W2-CONTENT-NARR-REV-MIN02`

No other material finding was established in the bounded root-review scope.

## 4. Findings

### W2-CONTENT-NARR-REV-MIN01 — ProgressionGateContract version is not explicit per gate

**Severity:** correction-requiring MINOR.

The frozen W1-SYN-GAME shared contract defines `ProgressionGateContract.version` on each contract object. The producer machine packet instead places one `version: 1` field on the collection:

```yaml
progression_gates:
  version: 1
  foundational_gate_count: 0
  gates:
    - gate_id: GATE:NARR:DEEP_HISTORY_INQUIRY
      gate_class: OPTIONAL
```

All five gate records omit their own version and the producer does not define an explicit inheritance rule saying that `progression_gates.version` is mechanically inherited by every member of `gates[]`.

The five records otherwise carry the shared gate fields and retain appropriate non-foundational classifications. The defect is therefore bounded schema ambiguity rather than a gate-classification or progression-design failure.

**Why correction is required:** fan-in/validation must not infer shared-contract version identity. Each gate contract needs mechanically unambiguous version semantics.

**Required correction:** preserve all existing gate IDs, classes, routes, recovery, branch scope, evidence obligations, and `foundational_gate_count: 0`; either add `version: 1` to every gate record (preferred) or define an equally explicit mechanically testable inheritance rule.

### W2-CONTENT-NARR-REV-MIN02 — ConsequenceContract machine required-fields contradict prose conditionality

**Severity:** correction-requiring MINOR.

The producer prose states that `ConsequenceContract` includes:

- a branch-impact ref **when high-impact**;
- compensation/alternative-goal refs **where restoration is impossible**.

The machine packet instead lists both fields unconditionally in `consequence_contract.required_fields`:

```yaml
required_fields:
  - branch_impact_ref
  - compensation_or_alternative_goal_refs
```

No explicit nullability or conditional-required rule reconciles the two surfaces.

**Why correction is required:** downstream authors/validators would otherwise have to fabricate irrelevant values for ordinary reversible consequences or invent undocumented nullability/conditionality. That would shift semantic authority into fan-in implementation rather than preserve the reviewed root contract.

**Required correction:** express the same conditional rules mechanically, for example with explicit conditional-required metadata/invariants or equivalent typed semantics. Preserve `irreversible_requires_branch_impact`, branch-family obligations, and all unrelated consequence semantics.

## 5. Required attack results / non-findings

The remaining mandatory attacks were exercised against the exact producer packet and did not establish a blocker, major, or additional correction-requiring minor:

1. **Frozen identity/provenance:** PASS structurally. Producer claim/terminal/work/head/PR and three-path scope are consistent.
2. **Quest lifecycle/state-machine integrity:** no material contradiction established. The root distinguishes availability, acceptance, activation, terminal outcomes, failure/retry/recovery, and prohibits hidden gameplay-authoritative prose state. Exact quest solvability remains later empirical work.
3. **Objective graph / soft-lock obligations:** structurally present: required-edge acyclicity or bounded monotonic loops, optional-vs-required separation, branch exclusivity, supported routes, role fallback/legal failure, and explicit retry/recovery obligations. No empirical solvability PASS is claimed.
4. **Sibling independence:** clean. Mutable sibling roots are not consumed; world/faction/character references remain provisional typed roles for later fan-in.
5. **Progression gate classification/composition:** no `FOUNDATIONAL` narrative gate is authored; all five gates remain `OPTIONAL`, `SPECIALIZATION`, or `BRANCH_EXCLUSIVE`. MIN01 is only version identity ambiguity.
6. **Truth/claim/knowledge/exposure separation:** clean structurally. Exposure and knowledge cannot promote claims to objective truth; branch facts require compatible predicates.
7. **Chronology/branch-fact leakage:** explicit-order and compatible-branch obligations are present; no list-order authority or discovery-creates-fact rule was found.
8. **Choice/consequence structure:** high-impact branches carry affected-goal, unavailable-content, alternative-goal, signaling, compensation/recovery, and long-horizon evidence obligations. Long-horizon sufficiency itself remains unrun evidence.
9. **GameTimePolicy:** representative windows use `SIMULATION` or `CALENDAR`, exact durations are deferred, pause/scale semantics delegate to the bound policy, and implicit ambient wall time is forbidden.
10. **GameSemanticGraph:** routes/branches/trajectories and semantic-value evidence are required; raw edge count is explicitly not quality evidence.
11. **Generated-content authority/originality:** generated prose remains candidate presentation; authoritative effects require validated command/effect paths and accepted-outcome persistence; outage/grounding failure cannot invent emergency canon.
12. **Scope and authority:** no engine choice, gameplay/high-throughput implementation, readiness, release, verification-PASS, decision, integration, or canonical-content authority is created by the producer packet.

These non-findings are structural review results only. They are not empirical WSN evidence.

## 6. Evidence status

`WSN-E1..WSN-E9` remain exactly `UNRUN_REQUIRED_EVIDENCE`.

In particular, this review does not convert structural obligations into PASS for contradiction/chronology, knowledge leakage, quest solvability, branch persistence, generated-content grounding, semantic sameness, long-horizon composition, or critic calibration.

## 7. Disposition and routing

**Disposition: `CHANGES_NEEDED`.**

The exact producer root does **not** yet satisfy its required-review prerequisite for `W2-CONTENT-SYN-01` fan-in because two correction-requiring MINOR schema-consistency defects remain.

Route exactly one bounded remediation successor: Issue #396 / `W2-CONTENT-NARR-REM-01`, limited to:

1. making each of the five `ProgressionGateContract` records' version semantics mechanically unambiguous; and
2. aligning machine `ConsequenceContract` required/conditional semantics with the prose.

The remediation must preserve all non-finding surfaces above and must receive a **fresh required review of the exact remediated packet** before any narrative-root fan-in disposition.

## 8. Authority boundary

This review is noncanonical provenance. It grants no content fan-in, integration, verification-PASS, engine selection, gameplay/high-throughput implementation, implementation readiness, release, decision, WSN empirical PASS, or canonical authority. Any publication/integration of this review is a separate squash-only authority episode.