# W2-CONTENT-SOCIAL-REM-01 — social claim typing and gate-contract remediation

**Issue:** #387  
**State:** REMEDIATION CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT_SOCIAL`  
**Engine dependency:** none for this bounded planning correction  
**Required next gate:** fresh independent/degraded-independent required content-root review

## 1. Exact binding and composition

This packet is the bounded successor required by Issue #384 / `W2-CONTENT-SOCIAL-REV-01`. It closes only findings `W2-CONTENT-SOCIAL-REV-M01` and `W2-CONTENT-SOCIAL-REV-M02` and grants no fan-in, integration, verification, readiness, release, decision, implementation, engine-selection, or canonical authority.

Exact immutable inputs:

- claim base / current `main` at claim: `32637bf66d8e76a4f029c9ca74f983cbe5535ffb`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`, binding comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive `5277825639`; parallel-frontier directive `5305563203`;
- frozen producer Issue #367: claim `5305656863`, terminal `5305675516`, exact head `db5d8ff86f4faeafa4a816412a2170cde979fb67`, PR #380;
- frozen required review Issue #384: claim `5305707061`, terminal `5305720735`, review work `f92392a7ded55701b21ca498e2575b5766fa4fd4`, exact head `f10657602500ea30b4cff209082106e037f92fab`, PR #388, disposition `CHANGES_NEEDED`;
- review provenance was squash-published noncanonically at `main@32637bf66d8e76a4f029c9ca74f983cbe5535ffb`.

The machine-readable successor is a reconstructable composition: the exact frozen #367 producer packet plus the explicit corrections in this remediation packet. Every producer semantic not replaced by M01/M02 remains unchanged. The fresh reviewer must attack both the immutable producer surface and these corrections; neither predecessor branch is mutated.

Preserved reviewed-good surface includes the same six actor IDs, ten topology edge IDs, multidimensional relationship model with retained `SocialHistoryEvent` history, zero foundational social gates, four bounded branch patterns, baseline ordinary-play alternatives, provisional sibling role interfaces, originality boundary, and unrun `WSN-E1/E2/E5/E7/E8/E9` evidence obligations.

## 2. M01 — orthogonal social claim/belief representation

The old single `information_scopes` enum mixed exposure (`PUBLIC`, `INSTITUTIONAL`, `PRIVATE`, `SECRET`), epistemic/dispute state (`DISPUTED`), and branch applicability (`BRANCH_SPECIFIC`). That enum is replaced by a typed `SocialClaimBelief` contract whose dimensions are orthogonal.

A record requires:

- stable `claim_id`;
- `holder_ref` and `source_refs` for perspective/provenance holders;
- provisional `proposition_ref` (`PROP_ROLE:*`);
- `authority_status`: `TESTIMONY | INSTITUTIONAL_RECORD | RUMOR | ANALYSIS | DISPUTED_RECORD`;
- `holder_epistemic_state`: `ASSERTS | BELIEVES | DOUBTS | WITHHOLDS | UNKNOWN`;
- `dispute_status`: `UNCONTESTED_CLAIM | DISPUTED | CORROBORATION_PENDING | RETRACTED`;
- `knowledge_state`: `HELD_BY_SOURCE | KNOWN_TO_HOLDER | DISCLOSED_TO_PLAYER | NOT_DISCLOSED_TO_PLAYER`;
- `exposure_scope`: `PUBLIC | INSTITUTIONAL | PRIVATE | SECRET`;
- independent `confidentiality`;
- explicit `provenance_refs`;
- nullable `branch_scope`, otherwise a provisional `NARR_BRANCH_ROLE:*` ref;
- nullable external `objective_fact_ref` (`WORLD_FACT_ROLE:*`);
- `truth_relation`: `UNKNOWN_TO_SOCIAL_ROOT | EXTERNALLY_BOUND_CONSISTENT | EXTERNALLY_BOUND_CONTRADICTED`;
- mandatory `objective_fact_authority: false`.

**Fail-closed authority rule:** this social root may reference a separately reviewed objective fact, but it can never create, promote, or inherit objective-fact authority from testimony, institutional confidence, rumor, analysis, corroboration state, player exposure, or branch applicability. `objective_fact_authority` must remain `false` here. A faction assertion therefore cannot become world truth merely because an institution records or repeats it.

This preserves W1-SYN-GAME's separation between objective facts, character/social knowledge and belief, player discovery, secrets, and branch facts without consuming mutable sibling output.

## 3. M02 — exact `ProgressionGateContract` v1 completion

The frozen W1-SYN-GAME contract at work `e74e0b0c95e85f69718868eedae324a298f02f3e` requires every gate to expose:

`version`, `gate_id`, `gate_class`, `blocks_or_unlocks`, `requirements`, `routes`, `visibility_or_discovery`, `miss_failure_recovery`, `branch_scope`, `evidence_requirements`, and `exception_rationale`.

Every route requires `route_id`, `route_kind`, `prerequisite_refs`, and `lifestyle_impacts`. All six social gates now instantiate these fields explicitly with `version: 1` and explicit `exception_rationale: null`.

| Gate | Class | Gate-level requirements | Visibility/discovery | Branch scope |
|---|---|---|---|---|
| `GATE-SOC-COMMONS-DELEGATION-01` | `SPECIALIZATION` | one declared route; no unresolved material public-work obligation relevant to delegation | purpose, route classes, denial reason visible | `null` |
| `GATE-SOC-FIELDWARD-SHARED-STOCK-01` | `SPECIALIZATION` | one route; requested stock/support available under declared scarcity rule | scarcity, routes, denial reason visible | `null` |
| `GATE-SOC-MAKERS-COMMISSION-01` | `OPTIONAL` | one route; no unresolved material commission default | commission requirements, routes, denial reason visible | `null` |
| `GATE-SOC-ARCHIVE-SENSITIVE-01` | `OPTIONAL` | one route; exposure scope and confidentiality/purpose permit disclosure | public records remain discoverable; sensitive purpose visible without leaking secret content | `null` |
| `GATE-SOC-WAYKEEPER-SPONSOR-01` | `OPTIONAL` | one route; no active declared safety constraint blocks requested support | baseline movement plus sponsorship routes/safety denial visible | `null` |
| `GATE-SOC-COALITION-COMMITMENT-01` | `BRANCH_EXCLUSIVE` | public-commitment route; commitment compatible with current social-dispute branch | consequence class, conflicting endorsement exclusion, ordinary-service alternative visible before commitment | `NARR_BRANCH_ROLE:SOCIAL_DISPUTE` |

All pre-existing route IDs and route kinds are preserved. Every route now has a nonempty `lifestyle_impacts` list. The declared impacts are bounded to specialist/optional/branch-specific play and explicitly preserve baseline lifestyles. No gate is reclassified to `FOUNDATIONAL`.

The coalition gate remains `BRANCH_EXCLUSIVE`, preserves ordinary services, and still requires `WSN-E5`, `BRANCH_IMPACT_EVIDENCE`, and `ALTERNATIVE_CONTENT_SUFFICIENCY`. This correction does not grant permanence or irreversible branch authority.

## 4. Regression boundaries preserved

The following passed #384 results remain invariant:

1. actor set stays exactly six candidate social actors and topology stays exactly ten typed edges;
2. relationship meaning remains multidimensional; `access_state` remains derived rather than a universal power score;
3. meaningful social history remains append-only in interpretation and survives recovery;
4. there are still zero foundational social gates;
5. ordinary community interaction, basic making/repair, baseline cultivation, baseline movement/exploration, public information, and ordinary mutual aid remain outside faction-standing gates;
6. branch patterns remain bounded and grant no permanence authority;
7. world/character/narrative references remain provisional typed interfaces rather than mutable sibling-output consumption;
8. no specific external fictional source is introduced and reference/originality review remains required for later concrete references;
9. `WSN-E1`, `WSN-E2`, `WSN-E5`, `WSN-E7`, `WSN-E8`, and `WSN-E9` remain `UNRUN_REQUIRED_EVIDENCE`; prose authorship is not evidence PASS;
10. the packet remains engine-neutral, noncanonical, and nonimplementation planning only.

## 5. Mechanical self-review

Self-review re-attacked M01 information-dimension conflation and assertion-to-fact promotion, M02 gate shape/route completeness, hidden foundational gates, relationship flattening, sibling leakage, branch regressions, canon inflation, scope expansion, duplicate WSN work, originality leakage, and Markdown/YAML drift.

Mechanical results:

- actor IDs: 6;
- edge IDs: 10;
- gates: 6;
- foundational gates: 0;
- branch patterns: 4;
- all gate contract versions: `1`;
- every gate has explicit `requirements`, `visibility_or_discovery`, recovery, `branch_scope`, evidence, and `exception_rationale`;
- every route has `lifestyle_impacts`;
- `SocialClaimBelief.promotion_forbidden = true` and objective-fact authority is fail-closed;
- WSN PASS claims: 0;
- unresolved self-review findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR.

Disposition: `SELF_REVIEW_CLEAN_PENDING_FRESH_REQUIRED_REVIEW`.

## 6. Finding disposition and next gate

- `W2-CONTENT-SOCIAL-REV-M01`: **REMEDIATED_PENDING_FRESH_REVIEW**.
- `W2-CONTENT-SOCIAL-REV-M02`: **REMEDIATED_PENDING_FRESH_REVIEW**.

A fresh required review must re-attack both findings and the preserved regression surface. Only a clean fresh review may satisfy the social root's review prerequisite for later `W2-CONTENT-SYN-01` fan-in. Remediation completion alone does not grant fan-in or integration authority.

No engine choice, gameplay/high-throughput implementation, implementation readiness, empirical WSN PASS, verification-PASS, release, decision, integration, or canonical authority is claimed here.
