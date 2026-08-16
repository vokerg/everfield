# W2-CONTENT-SOCIAL-REV-01 — required review of bounded factions/social topology

**Issue:** #384  
**Role:** fresh required content-root review  
**Trust:** `DEGRADED_SINGLE_AGENT`  
**Judged producer:** Issue #367 / `W2-CONTENT-SOCIAL-01`  
**Disposition:** `CHANGES_NEEDED`  
**Findings:** 0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR  
**Canonicality:** `NOT_CANONICAL`

## 1. Frozen judged identity

This review freezes the producer rather than repairing it.

- current `main` at review claim: `79f5bd62f7d03ecd954e94a485b0734bd80f1b86`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding comment: Bootstrap Issue #6 comment `5245368879`;
- canonical activation SHA: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive: Issue #84 comment `5277825639`;
- owner parallel-frontier directive: Issue #84 comment `5305563203`;
- content compiler work: `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`;
- clean activation review: Issue #372 terminal comment `5305598079`;
- producer Issue #367 claim: `5305656863`;
- producer terminal `STATUS(REVIEW_READY)`: `5305675516`;
- producer branch: `planning/issue-367`;
- producer base: `dd84256de5033cb9873eb10589847be1d403b042`;
- exact producer head: `db5d8ff86f4faeafa4a816412a2170cde979fb67`;
- exact producer PR: #380, draft at the frozen head;
- judged files exactly:
  - `docs/planning/wave-2/content/factions-social-topology.md`;
  - `docs/planning/wave-2/content/factions-social-topology.yaml`;
  - `docs/planning/handoffs/issue-367.md`.

Current `main` is a direct descendant of the producer base through the separately published world-review provenance commit; no current-main change mutates the three judged social paths. The producer packet therefore remains reconstructable and reviewable at its exact frozen head.

## 2. Authoritative cross-contracts checked

The review compared the producer against the exact immutable game/content foundations it cites, especially:

- W1-DES-03 work `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b`;
- W1-SYN-GAME work `e74e0b0c95e85f69718868eedae324a298f02f3e`;
- current canonical `docs/planning/WAVE-1-FOUNDATIONS-v1.md`;
- Issue #367's exact contract and the clean content-frontier activation review.

Relevant immutable rules include:

1. gameplay/continuity-relevant truth must be explicit structured state rather than prose-only authority;
2. objective facts, character knowledge/beliefs, player discovery, secrets, chronology, and branch facts remain distinguishable;
3. relationship/social meaning must not collapse into one universal affection/standing scalar and material history must survive recovery where meaning depends on it;
4. every material progression gate uses `ProgressionGateContract` semantics, including stable classification, blocks/unlocks, explicit requirements/routes, route-level lifestyle impacts, visibility/discovery, miss/failure/recovery, branch scope where applicable, and evidence requirements;
5. social/narrative gates may not silently become foundational downstream;
6. branch-exclusive/high-impact choices bind branch-impact/alternative-content obligations;
7. generated/authored prose does not create objective/canonical truth;
8. WSN evidence remains empirical debt until executed under its own authority.

## 3. Passed attacks

### 3.1 Frozen identity and ownership surface — PASS

PR #380 is the exact producer visibility PR at `db5d8ff86f4faeafa4a816412a2170cde979fb67`. Its changed surface is exactly the producer handoff, Markdown candidate, and YAML candidate. No sibling content path is changed.

### 3.2 Actor and topology integrity — PASS

The packet defines six stable candidate actor IDs and ten stable typed social edges. Edge endpoints resolve to declared actors, actor responsibilities are bounded, and conflicts are framed as competing priorities rather than universal moral/progression authority.

### 3.3 Relationship multidimensionality and retained history — PASS

The packet rejects a universal aggregate score, declares separate `trust`, `reliability`, `reciprocity`, `value_alignment`, `public_standing`, and derived `access_state` dimensions, and declares meaningful `SocialHistoryEvent` retention. The examples explicitly permit dimensions to diverge and prevent recovery from deleting the meaning of prior events. This satisfies the bounded root-level anti-flattening obligation.

### 3.4 Hidden foundational gating — PASS, subject to M02 contract completeness

All six declared social gates are classified `SPECIALIZATION`, `OPTIONAL`, or `BRANCH_EXCLUSIVE`; none is `FOUNDATIONAL`. Each names a bounded unlock surface and states a baseline alternative or ordinary-play survival rule. The producer also includes reopen conditions if a downstream common foundational goal starts depending on a social gate.

No current record makes faction standing the sole route to baseline cultivation, repair/crafting, movement/exploration, public information, ordinary community participation, or ordinary mutual aid.

### 3.5 Branch/consequence boundedness — PASS

The four branch patterns have stable IDs, bounded involved actors, typed effect classes, and explicit non-authority for permanence. Baseline play/mobility protections appear where relevant. The coalition gate identifies conflicting simultaneous coalition endorsement as the branch-exclusive social surface and binds future branch-impact/alternative-content evidence rather than claiming that evidence has already passed.

### 3.6 Sibling independence — PASS

World, character, and narrative dependencies are represented with provisional typed role references (`WORLD_ROLE:*`, `CHAR_ROLE:*`, `NARR_ROLE:*`). The packet does not consume mutable outputs from Issues #366, #368, or #369. Reconciliation is correctly deferred to content fan-in.

### 3.7 Originality/reference boundary — PASS

The packet declares the candidate actors/topology as newly authored Everfield planning material and limits external inspiration to generic institutional concepts. It does not import named external fictional canon, and it preserves later provenance/originality/rights review requirements for specific references.

### 3.8 WSN evidence discipline — PASS

`WSN-E1`, `WSN-E2`, `WSN-E5`, `WSN-E7`, `WSN-E8`, and `WSN-E9` are explicitly `UNRUN_REQUIRED_EVIDENCE` in the machine packet. The producer does not claim prose authorship satisfies them.

### 3.9 Scope and authority — PASS

The producer remains engine-neutral and noncanonical. It does not author final world geography/history, principal-character biographies/arcs, a final main plot/quest/dialogue corpus, runtime implementation, engine selection, implementation readiness, release, verification-PASS, decision, or canonical authority.

## 4. MAJOR findings

### W2-CONTENT-SOCIAL-REV-M01 — social information typing conflates truth/belief, exposure, and branch applicability

**Severity:** MAJOR  
**Status:** OPEN / correction required before clean fan-in review

The producer prose correctly says a faction's confidence in a claim cannot promote it to objective truth, and `SOC-INV-008` states that prose/generated text cannot create objective fact by assertion. The machine-readable model, however, has only one `information_scopes` enumeration:

- `PUBLIC`;
- `INSTITUTIONAL`;
- `PRIVATE`;
- `DISPUTED`;
- `SECRET`;
- `BRANCH_SPECIFIC`.

Those values mix independent semantic axes:

- `PUBLIC` / `INSTITUTIONAL` / `PRIVATE` / `SECRET` describe exposure/access or confidentiality;
- `DISPUTED` describes epistemic/authority status;
- `BRANCH_SPECIFIC` describes applicability/truth scope.

The packet contains no stable typed social claim/belief record binding a claim identity, claimant/holder/perspective, proposition/fact reference, epistemic status, exposure/knowledge state, provenance/source, and branch applicability as separate fields. Actor prose obligations and the no-prose-promotion invariant do not provide that representation.

This is materially weaker than the frozen W1-DES-03 / W1-SYN-GAME rule that objective fact, character knowledge/belief, player discovery, secrets, and branch facts remain distinguishable. A later fan-in would otherwise have to invent whether a `DISPUTED` item is public or secret, whether a `SECRET` is objectively true or merely believed, and whose belief/assertion a social claim represents. Contradiction and leakage checks cannot mechanically preserve the distinction from this root alone.

**Required bounded correction:** add an orthogonal typed in-world social claim/belief interface (name is not prescribed) that, at minimum:

1. has a stable claim/belief identity;
2. binds a claimant/holder/source or provisional actor/character role;
3. binds a proposition/fact reference or another explicitly bounded proposition representation;
4. separates truth/authority or dispute status from visibility/exposure/knowledge state and from branch scope;
5. permits false, incomplete, disputed, secret, or branch-scoped beliefs without promoting them to objective truth;
6. fail-closes prose/institutional assertion from creating `CANDIDATE_OBJECTIVE` authority;
7. remains sibling-independent through provisional typed refs rather than consuming mutable world/character outputs.

This correction is an interface-level social-root correction, not permission to author final character belief systems or world facts.

### W2-CONTENT-SOCIAL-REV-M02 — gate records are not mechanically complete `ProgressionGateContract` instances

**Severity:** MAJOR  
**Status:** OPEN / correction required before clean fan-in review

W1-SYN-GAME defines `ProgressionGateContract` as the shared typed object preventing social/narrative/economy/automation prerequisites from becoming a hidden canonical playthrough. The exact contract includes, among other fields:

- `version`;
- `gate_id`;
- `gate_class`;
- `blocks_or_unlocks`;
- explicit `requirements`;
- routes with stable `route_id`, `route_kind`, `prerequisite_refs`, and route-level `lifestyle_impacts`;
- `visibility_or_discovery`;
- `miss_failure_recovery`;
- optional `branch_scope`;
- `evidence_requirements`;
- `exception_rationale`.

The six producer `gates` records do provide stable IDs/classes, blocks/unlocks, routes/prerequisites, recovery, baseline alternatives, evidence requirements, and branch scope where applicable. They do **not** encode contract version, explicit gate-level requirements, route-level `lifestyle_impacts`, `visibility_or_discovery`, or explicit exception rationale/null semantics. The absence of `lifestyle_impacts` and `visibility_or_discovery` is not cosmetic: the same Wave-1 contract requires gate/route state to compile into semantic-graph reachability and requires progressive discovery/legibility and lifestyle viability to remain observable rather than implicit.

`baseline_alternative` prose/scalars and generic evidence labels are useful but are not mechanically equivalent to route-level lifestyle impacts and gate visibility/discovery. A later fan-in would need to invent those required semantics rather than reconcile already-typed root data.

**Required bounded correction:** make all six social gate records explicitly conform to, or mechanically compile without invention into, the frozen `ProgressionGateContract` semantics. At minimum:

1. bind contract version/shape explicitly;
2. encode gate-level requirements as an explicit list, including empty where none exist;
3. encode route-level lifestyle impacts for every route;
4. encode visibility/discovery semantics for every gate;
5. preserve explicit recovery, branch scope, evidence requirements, and baseline alternatives;
6. state exception rationale/null semantics rather than relying on omission;
7. keep all six current non-foundational classifications unless a material design change requires reviewed reclassification;
8. preserve the coalition branch-exclusive obligation to identify unavailable/conflicting social content and require later `BranchImpactEvidence`/alternative-content evidence before any high-impact irreversible decision.

This is a schema/contract-completeness correction. It does not require empirical WSN execution and must not turn social gates into implementation schemas or foundational progression.

## 5. Finding count and disposition

- BLOCKER: 0
- MAJOR: 2
- correction-requiring MINOR: 0
- trust profile: `DEGRADED_SINGLE_AGENT`
- disposition: `CHANGES_NEEDED`

The producer's relationship topology, anti-grind/history model, bounded actors/edges, provisional sibling interfaces, originality boundary, WSN evidence discipline, and authority boundary remain useful predecessor work. They must be preserved unless a correction directly requires a change.

The exact producer packet at `db5d8ff86f4faeafa4a816412a2170cde979fb67` is **not clean for `W2-CONTENT-SYN-01` fan-in** because M01 and M02 are unresolved.

## 6. Required downstream route

Route exactly one bounded remediation successor:

`W2-CONTENT-SOCIAL-REM-01` — remediate social claim/belief typing and `ProgressionGateContract` completeness.

The remediation must:

- create fresh successor copies on its own branch rather than modifying `planning/issue-367` or this review branch;
- close exactly M01/M02 while preserving the passed attacks above;
- remain engine-neutral and noncanonical;
- execute no WSN experiment merely to satisfy authored-structure corrections;
- open an exact-head draft PR and terminalize `REVIEW_READY`;
- receive a fresh independent/degraded-independent required review that binds the exact remediation packet and re-attacks both findings plus regressions.

Only a clean fresh review of the remediation may satisfy this root's review prerequisite for later content fan-in.

## 7. Authority boundary

This review grants no producer mutation authority, fan-in authority, engine selection, gameplay/high-throughput implementation, implementation readiness, WSN empirical PASS, production/release, verification-PASS, decision, integration, or canonical authority.

Any publication of this review into `main` is a separate squash-only convergence decision and remains noncanonical review provenance unless a separate authority explicitly grants something stronger.