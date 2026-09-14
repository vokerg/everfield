# W2-CONTENT-NARR-CONT-02 — bounded narrative / quest / consequence continuation

**Issue:** #1052  
**Mission:** `W2-CONTENT-NARR-CONT-02`  
**State:** PRODUCER CANDIDATE / NONCANONICAL  
**Conflict domain:** CONTENT  
**Producer base:** `main@e82f12b52087f3820294048451fadc8e29418999`  
**Authority:** engine-neutral bounded planning provenance only; no integration, verification-PASS, implementation-readiness, engine-selection, release, decision, final-canon, or canonical authority.

## 1. Frozen reviewed basis

This packet consumes only immutable reviewed predecessor provenance:

- canonical Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding Issue #6 comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- CONT-02 activation Review #1063 terminal `5654948592`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_02_ACTIVATION`;
- reviewed continuation fan-in #986 terminal `5644862732`, Markdown blob `b39f535dc71639f3ebc67e33a2d692a2b3a77588`, YAML blob `78148f50649ada789feb3cca61182e18465bb628`;
- required fan-in Review #1009 terminal `5645006619`, disposition `CLEAN_FOR_BOUNDED_CONTENT_CONTINUATION_CONSUMPTION`;
- reviewed narrative CONT-01 remediation source represented on main by Markdown blob `a5ccc99a937cfdbca0ed293f4a70f8191d7b800a` and YAML blob `14c748fdc870d24d804fea84416c25b2956f0288`.

No mutable CONT-02 world, social, character, or evaluation output is read or consumed.

## 2. Purpose

CONT-02 deepens the reviewed narrative grammar without authoring a quest catalog or fixing final plot canon. It introduces a second bounded structural arc for tracing consequences, choosing a response portfolio, and validating continued play after a response.

The packet preserves all reviewed fan-in invariants:

1. private context remains optional and deny-by-default;
2. mutually exclusive branches are never jointly required;
3. relationship, legitimacy, player exposure, testimony, or proximity never grants private knowledge;
4. route cardinality is checked before objective activation and recomputed after substitution/recovery;
5. exact schedules, timed windows, travel times, weather windows, and NPC reachability are not asserted;
6. high-impact consequences require signaling, affected-goal accounting, persistence/reversibility, and recovery/mitigation/compensation or meaningful alternatives;
7. irreversible concrete world change is not authorized without separately reviewed `BranchImpactEvidence`;
8. ordinary foundational play remains legal.

## 3. Provisional interfaces only

CONT-02 may use only fan-in-governed provisional refs:

### World
- `WORLD_ROLE:CONT_CONTESTED_SITE`
- `WORLD_ROLE:CONT_HISTORY_OR_EVIDENCE_SOURCE`
- `WORLD_ROLE:CONT_AFTERMATH_SURFACE`

The contested site remains a bounded set whose concrete selection is downstream-owned. No member is selected here.

### Social
- `SOCIAL_ROLE:CONT_AFFECTED_GROUP`
- `SOCIAL_ROLE:CONT_STEWARDSHIP_OR_SERVICE`
- `SOCIAL_ROLE:CONT_COUNTERPRESSURE`

These refer to typed pressure/obligation surfaces, not one mandatory faction.

### Character
- `CHAR_ROLE:CONT_PERSPECTIVE_HOLDER`
- `CHAR_ROLE:CONT_AFFECTED_TIE`
- `CHAR_ROLE:CONT_PRIVATE_CONTEXT_HOLDER`

Concrete holder identity remains unresolved. Private context is optional, default-deny, and never counts toward a required route minimum.

## 4. Arc: `ARC_CONT02:TRACE_RESPOND_VALIDATE`

This is one structural arc with three quest-family stages. The stages are grammar fixtures, not authored quests.

### 4.1 `QFAM_CONT02:TRACE_CAUSAL_ACCOUNTS`

Purpose: establish what is observably different after a prior consequence while preserving uncertainty about ultimate cause.

Required objectives:

- `OBJ_CONT02:OBSERVE_DELTA` — identify at least one observable consequence/effect surface without inferring unsupported exact timing;
- `OBJ_CONT02:COMPARE_CAUSAL_ACCOUNTS` — compare at least **two materially distinct non-private** evidence/perspective routes;
- `OBJ_CONT02:REGISTER_WORKING_ACCOUNT_OR_UNCERTAINTY` — record a working interpretation or explicit uncertainty without promoting claim/testimony to objective fact.

Optional:
- `OBJ_CONT02:PRIVATE_CONTEXT` may enrich interpretation only after lawful disclosure. It never counts toward the two-route minimum.

Cardinality:
- before `OBJ_CONT02:COMPARE_CAUSAL_ACCOUNTS` activates, at least two simultaneously legal materially distinct non-private routes must exist;
- if fewer than two remain, transition to `STATE_CONT02:PRE_TRACE_DEFERRED`;
- substitution or route loss requires recomputation before the comparison can resume.

No unresolved world cause is forced closed.

### 4.2 `QFAM_CONT02:SELECT_RESPONSE_PORTFOLIO`

Purpose: choose a bounded response while making tradeoffs and alternatives explicit.

Required objective:
- `OBJ_CONT02:SELECT_RESPONSE_PORTFOLIO`.

A portfolio is a structural combination drawn from materially differentiated response families:
- `RESPONSE_CONT02:MAINTAIN_OR_STEWARD`;
- `RESPONSE_CONT02:REPAIR_OR_COMPENSATE`;
- `RESPONSE_CONT02:REDIRECT`;
- `RESPONSE_CONT02:LEARN_OR_RECONTEXTUALIZE`;
- `RESPONSE_CONT02:DEFER_OR_NONALIGN`.

At least **two simultaneously legal materially differentiated response families** must exist before selection activates. If not, transition to `STATE_CONT02:PRE_RESPONSE_DEFERRED`.

Every selectable response states:
- affected goal/content classes;
- observability and precommitment signaling;
- persistence/reversibility class;
- recovery, mitigation, compensation, or meaningful alternative;
- evidence needed for any high-impact or irreversible variant;
- branch scope;
- whether continued baseline play remains legal.

Refusal or rejection by an affected actor/group cannot be converted into consent by retry, standing, gifts, prior quest success, or relationship state. Rejection triggers recomputation, substitution, defer/nonalignment, or legal failure.

### 4.3 `QFAM_CONT02:VALIDATE_AFTERMATH_CONTINUITY`

Purpose: ensure a chosen response leaves meaningful continued play rather than a cosmetic or hidden-terminal branch.

Required objectives:
- `OBJ_CONT02:OBSERVE_RESPONSE_EFFECT`;
- `OBJ_CONT02:CHOOSE_CONTINUED_GOAL`.

At least **two simultaneously legal materially distinct continued-goal families** must exist before `OBJ_CONT02:CHOOSE_CONTINUED_GOAL` activates. Candidate structural families are:
- `GOAL_CONT02:STEWARDSHIP_OR_MAINTENANCE`;
- `GOAL_CONT02:REPAIR_OR_COMPENSATION`;
- `GOAL_CONT02:INVESTIGATION_OR_RECONTEXTUALIZATION`;
- `GOAL_CONT02:REDIRECTION`;
- `GOAL_CONT02:NONALIGNED_BASELINE_CONTINUATION`.

If the set drops below two after a state change, transition to `STATE_CONT02:PRE_CONTINUED_GOAL_DEFERRED` before selection. Recovery must recompute cardinality.

## 5. Information authority

Records distinguish:
- objective fact authority;
- claim/testimony/interpretation;
- character knowledge and acquisition provenance;
- player exposure;
- confidentiality/access policy;
- branch applicability.

The rules are fail-closed:

- a claim, belief, testimony, interpretation, generated summary, relationship state, public standing, or legitimacy cannot promote itself to objective fact;
- player exposure does not grant character knowledge;
- private information defaults to `DENY`;
- allowed private acquisition is explicit holder disclosure or a later validated authority effect;
- retry never rewrites a prior refusal or disclosure history;
- contradiction may remain unresolved.

## 6. Consequence deepening

CONT-02 preserves `REVERSIBLE`, `CONDITIONALLY_REVERSIBLE`, and `IRREVERSIBLE`.

Every response consequence must declare:
- trigger and branch scope;
- affected state and goal/content refs;
- typed effect operations;
- observability;
- persistence/history behavior;
- reversibility and reversal/mitigation semantics;
- compensation or alternative goals when restoration is impossible;
- downstream dependencies;
- evidence refs.

For a high-impact, branch-exclusive, or irreversible concrete instance, `BranchImpactEvidence` is mandatory before the instance can be treated as sufficient. This producer creates no such evidence and authorizes no concrete irreversible world change.

A retry, repair, reconciliation, or compensation may change current state but cannot erase material consequence, disclosure, refusal, or relationship history.

## 7. Progression discipline

This packet creates **zero FOUNDATIONAL gates**.

Structural gates:

### `GATE:NARR-CONT02:CAUSAL_TRACE` — OPTIONAL
Unlocks deeper reassessment. Comparison activates only with at least two non-private routes. Underflow uses `STATE_CONT02:PRE_TRACE_DEFERRED`.

### `GATE:NARR-CONT02:RESPONSE_SELECTION` — BRANCH_EXCLUSIVE
Unlocks response-specific consequence content. Selection activates only with at least two differentiated legal response families. Underflow uses `STATE_CONT02:PRE_RESPONSE_DEFERRED`.

### `GATE:NARR-CONT02:AFTERMATH_CONTINUITY` — SPECIALIZATION
Unlocks specialized aftermath goals while nonaligned baseline continuation remains legal. Goal selection activates only with at least two differentiated legal goal families. Underflow uses `STATE_CONT02:PRE_CONTINUED_GOAL_DEFERRED`.

Composition of these non-foundational gates must not create a de facto foundational tax.

## 8. Time and WSN discipline

No exact timing is authored.

Retained WSN truth:
- E3: `INCONCLUSIVE_TIMED_COVERAGE_BLOCKED`;
- E4: `NOT_RUN_BLOCKED_BY_EXACT_PREREQUISITE`;
- E5: `PASS_BOUNDED_MODEL_ONLY`;
- E8: `INCONCLUSIVE_SCHEDULE_COVERAGE_BLOCKED`.

Therefore this packet makes no claim about exact dates, durations, opening hours, schedules, weather windows, travel times, timed quest objectives, NPC reachability, production persistence, human quality, or aggregate verification.

## 9. Failure and recovery invariants

Representative failures are resolved structurally:

- evidence route disappears → recompute non-private route count; substitute if valid; otherwise defer before comparison activation;
- private disclosure denied → continue without it; the required route count is unchanged;
- affected actor/group rejects a proposal → recompute response families; preserve defer/nonalignment or other lawful alternatives;
- service/site becomes unavailable → substitute, redirect, compensate, defer, or legal terminal failure; never silently require an unavailable role;
- restoration becomes impossible → compensation/changed-goal routes plus explicit history persistence;
- one continued-goal family disappears → recompute; underflow below two defers before choice;
- truth remains unresolved → continued play may proceed without forced mystery closure.

Mutually exclusive branches are never jointly required.

## 10. OPEN ledger

The following remain unresolved and downstream-owned:

1. concrete contested/aftermath world surface selection;
2. concrete faction/institution carriers for social roles;
3. concrete character holders or relationship counterparts;
4. optional private-context holder and any disclosure event;
5. exact new-event chronology beyond relative ordering;
6. exact `GameTimePolicy`, schedules, timed windows, weather/travel interaction, and reachability;
7. concrete `BranchImpactEvidence`;
8. final biographies, factions, ownership, plot resolutions, secrets, endings, and canon;
9. human-quality, production validation, aggregate verification, implementation readiness, release, and canonicalization.

## 11. Self-review

Attacks performed:
- sibling mutable-output leakage;
- route-cardinality underflow before activation and after recovery;
- hidden required private context;
- truth/claim/knowledge/player-exposure collapse;
- composed foundational gate tax;
- actor/site availability soft locks;
- refusal/consent laundering;
- consequence history erasure;
- high-impact authority inflation;
- exact-time/schedule overreach;
- WSN laundering;
- engine coupling;
- concrete canon invention;
- Markdown/YAML mismatch;
- higher-authority inflation.

Result: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in producer self-review.

## 12. Required next gate

One fresh independent/degraded-independent required review must judge the exact immutable producer packet before any `W2-CONTENT-NARR-CONT-02_REVIEWED` token exists.

A clean review may grant only `CLEAN_FOR_BOUNDED_CONTENT_FAN_IN_CONSUMPTION` / token `W2-CONTENT-NARR-CONT-02_REVIEWED` for later bounded `W2-CONTENT-SYN-CONT-02` fan-in.

No integration, verification-PASS, implementation-readiness, engine-selection, release, decision, final-canon, or canonical authority is granted here.
