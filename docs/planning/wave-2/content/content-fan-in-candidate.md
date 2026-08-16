# W2-CONTENT-SYN-01 — reviewed-root content fan-in candidate

**Issue:** #422  
**State:** SYNTHESIS CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT_FANIN`  
**Engine dependency:** none for this bounded synthesis  
**Required next gate:** fresh independent/degraded-independent required synthesis review

## 1. Purpose and frozen identity

This packet is the compiler-declared fan-in successor that becomes eligible only after the world, social, character, and narrative roots have each completed their required review chains. It reconciles those reviewed roots without rewriting them, upgrading them to canon, fabricating empirical evidence, selecting an engine, or authorizing implementation.

Claim base is `main@ff261a900fd475764a08c48336dfb4afb22bdfb0`. Canonical Planning Program v1 remains blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`. Owner directives are `5277825639` and `5305563203`. The content-frontier compiler is Issue #365 work `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`, with clean activation review Issue #372 terminal `5305598079`.

The exact current-main root blobs are frozen in `content-fan-in-map.yaml`:

| Root | Markdown blob | YAML blob | Clean review |
|---|---|---|---|
| world | `3caaddf10e27cefb91c35b6a4f374740aa3c6731` | `baa827528994864faa3f50c8b0785dd89a775a14` | #414 / `5307253433` |
| social | `7a4c5431aa08597b96778b5a89b98dbd9d103401` | `16c55eb0dba4530a4936b6da3695e752d8f21e68` | #391 / `5306043969` |
| character | `14a26367abb763860c691e2501ab8c118a497ad2` | `f836fdf69ac5ecba03b5d711b366ed6765e007db` | #411 / `5306750686` |
| narrative | `4e31fb0e812f4dcbc65303740c252553d07f7286` | `75844d9c24f5ed2073a2c36a782c52f8b7d5c127` | #419 / `5307411116` |

Every cited clean review disposition is `CLEAN_FOR_BOUNDED_CONTENT_FANIN`. Root producer/remediation/review branches remain immutable provenance. This fan-in owns only mappings, cross-root constraints, explicit deferrals, and the residual contradiction ledger.

The machine-readable artifact `docs/planning/wave-2/content/content-fan-in-map.yaml` is authoritative for exact binding records and invariants; this document explains its synthesis decisions.

## 2. Binding discipline: exact only when the roots actually support it

The central rule is fail-closed composition. A provisional role receives an `EXACT` binding only when one reviewed target uniquely satisfies the relevant semantics. Where several targets are compatible, the fan-in records a `SET`; where several IDs jointly implement one interface, it records `COMPOSITE`; where the role points to a contract or narrative structure rather than one entity, it records `STRUCTURAL`; and where reviewed evidence is insufficient, it records `UNRESOLVED`.

That distinction prevents fan-in from becoming an undocumented canon-writing episode. Representative exact bindings include:

- world `ROLE:LOCAL-CIVIC-STEWARD` → social `FAC-COMMONS-01`;
- world `ROLE:LAND-USE-CUSTODIAN` → `FAC-FIELDWARD-01`;
- social `WORLD_ROLE:HUB_COMMUNITY` → `LOC:SETTLEMENT-CORE`;
- social `WORLD_ROLE:CULTIVATION_ZONE` → `LOC:CULTIVATION-MOSAIC`;
- character `WORLD_ROLE:shared_worksite_or_infrastructure` → `LOC:OLD-WORKS`;
- character `FACTION_ROLE:craft_or_service_network` → `FAC-MAKERS-01`;
- character `FACTION_ROLE:civic_coordination_body` → `FAC-COMMONS-01`;
- character `FACTION_ROLE:mutual_aid_network` → `COM-NEIGHBOR-01`;
- narrative `CHAR_ROLE:RETURNING_TIE` → `CHAR:tomas_irel`.

Those bindings carry **no authority effect**. They state compatibility and interface resolution only.

Several roles deliberately stay plural or unresolved:

- `WORLD_ROLE:CONTESTED_COMMON`, `WORLD_ROLE:COMMON_RESOURCE`, and the character contested-project role can refer to `LOC:OLD-WORKS`, `LOC:RIPARIAN-CORRIDOR`, or `LOC:COMMONS-BELT`; this fan-in does not pick the game's final central project site.
- `ROLE:HISTORY-BEARER` can be supported by the Hearth Archive, Neighbor Network, Anwen, or Tomas. Because the world packet carries two conflicting fragmentation accounts under the same generic holder role, later content must bind distinct holders or explicitly model distinct source/perspective provenance; it may not silently make one concrete holder assert and deny the same proposition.
- narrative `FACTION_ROLE:CUSTODIAN` remains a set because civic, land-use, and record custody are materially different reviewed functions.
- narrative `FACTION_ROLE:OUTSIDE_PRESSURE` remains unresolved because world facts explicitly leave external polity details `UNKNOWN_BY_DESIGN`. Creating a named or final outside faction here would violate the reviewed world boundary.
- social `WORLD_ROLE:SENSITIVE_SITE` remains unresolved because no reviewed world location is universally classified that way.

The fan-in therefore resolves interface compatibility without pretending that reviewed abstractions are final content instances.

## 3. World truth, claims, beliefs, knowledge, and player exposure remain orthogonal

The four roots use different information layers, but they compose without authority collapse:

1. **World objective/constraint records** retain the only candidate objective-fact authority in this packet. They remain noncanonical.
2. **World propositions and in-world claims** are perspectives about propositions; claim presence, confidence, or discovery cannot create a fact.
3. **Social `SocialClaimBelief` records** retain `objective_fact_authority: false`. An external fact reference can point to a separately reviewed world fact but does not transfer fact authority to the social assertion.
4. **Character information records** retain local candidate truth/holder semantics and default-deny access. Relationship state, faction standing, shared provisional roles, generated text, or player visibility do not grant character knowledge.
5. **Narrative knowledge/discovery layers** may expose evidence to the player without changing objective truth, character knowledge, confidentiality, or claim authority.

This preserves the reviewed fail-closed boundary around the fragmentation mystery. `WF:FRAGMENTATION-CAUSE` remains `UNKNOWN_BY_DESIGN`; `CLM:FRAGMENTATION-ACCOUNT-A` and `-B` remain conflicting in-world accounts with no truth effect. Neither Anwen's provenance expertise, Tomas's testimony capability, the Hearth Archive's records, social corroboration, nor narrative discovery can settle the mystery without a separate reviewed authority change.

Generated prose is likewise presentation/candidate material only. It cannot promote a claim to objective truth or directly mutate authoritative state; any later authoritative effect must pass through a validated command/effect boundary.

## 4. Chronology reconciles by order constraints, not invented dates

The world root provides the only reviewed cross-root chronology spine:

`ERA:PRE-WORKS` → `ERA:WORKS-BUILDOUT` → `ERA:PATCHWORK-PRESENT`

with event order:

`EVT:WORKS-BUILDOUT` → `EVT:WORKS-FRAGMENTATION` → `EVT:PATCHWORK-PRESENT-START` → `EVT:PLAYER-ENTRY`.

Narrative orientation/invitation is bound to the `EVT:PLAYER-ENTRY` boundary. Story-state progression is therefore at or after player entry unless a record is explicitly retrospective evidence.

The four character relationship-history events and future social history records do not currently carry an exact position on the world chronology. Fan-in does **not** infer that position from their existence or wording. A chronology-sensitive authored instance must add an explicit order constraint before using one of those events as pre-entry or post-entry evidence.

The reviewed `GameTimePolicy` deferral also remains intact: no exact policy version, exact calendar value, or duration is invented. `TIME_WINDOW:WITNESS_AVAILABILITY` and `TIME_WINDOW:CONSEQUENCE_RESPONSE` remain typed timed-window interfaces that require a later reviewed policy binding before executable timed content or `WSN-E4` can run.

## 5. Progression gates compose without becoming foundational

The fan-in carries eleven reviewed `ProgressionGateContract` v1 gates: six social and five narrative. Their combined foundational count remains **zero**.

Social gates remain specialist, optional, or branch-exclusive. Narrative gates remain optional, specialist, or branch-exclusive. In particular:

- `GATE-SOC-COALITION-COMMITMENT-01` and `GATE:NARR:PUBLIC_COMMITMENT` are distinct contracts. They may participate in the same authored branch instance but are not aliases and do not create a hidden universal political/relationship gate.
- ordinary community interaction, basic repair/crafting, baseline cultivation, baseline movement/exploration, public information, ordinary mutual aid, and other shared foundational play remain legal without satisfying any gate in this fan-in;
- sensitive testimony retains relationship and evidence/record substitutes; relationship state alone does not unlock secrets;
- branch-exclusive routes preserve visible consequences, recovery/alternatives, and later evidence obligations rather than collapsing to one standing score or preferred lifestyle.

This preserves route plurality and the anti-grind boundary inherited from the social root.

## 6. Branches, consequences, and history remain scoped

Social branch patterns remain bounded and do not gain permanence authority merely because they can map into a narrative branch family.

- `SOC-BRANCH-DISCLOSURE-01` can structurally instantiate `BRANCH_FAMILY:DISCLOSURE_OR_WITHHOLDING`, but only with explicit audience, exposure, history, and branch-effect records.
- `SOC-BRANCH-COMMON-USE-01` can feed either `PUBLIC_ALIGNMENT` or, where a concrete high-impact transformation actually satisfies the consequence contract, `COMMONS_TRANSFORMATION`. Ordinary shared-use disagreement does **not** become irreversible by association.
- social access and aid branches remain bounded social state unless a later reviewed narrative contract explicitly raises their scope.

For narrative high-impact branches, the reviewed consequence contract remains controlling: irreversible effects require branch impact; high-impact choices require affected-goal/lost-content signaling; restoration cannot erase meaningful history; and when restoration is impossible, compensation or alternative goals are required. Every high-impact route must preserve meaningful continued play and at least one shared foundational gameplay route.

Relationship/history semantics also remain multidimensional. Social `trust`, `reliability`, `reciprocity`, `value_alignment`, `public_standing`, and derived `access_state` are not flattened into the character dimensions `TRUST`, `WARMTH`, `RESPECT`, `OBLIGATION`, `RIVALRY`, and `CAUTION`. Related concepts such as trust or reciprocity/obligation are explicitly **related, not identical**. Recovery may change current dimensions but does not erase `SocialHistoryEvent` or `REL_EVT:*` history.

## 7. Quest-role fan-in stays instance-oriented

The five narrative quest roles now have reviewed cross-root candidate surfaces without becoming final quests:

- `QROLE:INVESTIGATE_CONFLICTING_ACCOUNTS` binds the fragmentation mystery/proposition/claims, Old Works evidence surface, archive/community memory, and Anwen/Tomas witness candidates. It requires multiple claims, independent evidence, and no forced truth conclusion.
- `QROLE:NEGOTIATE_SHARED_USE` can draw from Old Works, riparian, or commons sites; Commons/Fieldward/Makers/Neighbor social actors; and Selka/Maelin character pressures. The concrete disputed site is selected per authored instance, not here.
- `QROLE:COMMIT_TO_PROJECT` can use reviewed project sites, social stakeholders, Oren/Selka pressure, and the public-alignment or common-transformation families. A concrete project must expose costs and affected goals before commitment; irreversible use requires the full branch-impact contract.
- `QROLE:REPAIR_OR_REFRAME` can use Old Works, Makers/Neighbor/Archive, Jori/Maelin/Anwen, and existing durable relationship-history records. Repair cannot erase history or automatically grant information access.
- `QROLE:AFTERMATH_AMBITION` remains branch-specific within the watershed and may involve Oren or Tomas, while preserving unrelated meaningful long-horizon goals and selecting no canonical ending.

These bindings make later authored content testable while keeping final plot, project, actor assignment, and ending choices outside this synthesis authority.

## 8. Originality, generation, and evaluator boundaries

The four reviewed roots' originality boundaries remain intact. This fan-in imports no external fictional names, characters, locations, quest lines, dialogue, or protected expressive content. Any later concrete external reference still requires explicit purpose/provenance/originality review and rights review where applicable.

Generated-content authority also remains unchanged: generated candidates may assist presentation or bounded build-time content work, but grounding failure must fail closed or use a declared fallback, and generation never receives direct canonical-state mutation authority.

Evaluator/critic outputs likewise remain evidence inputs, not canon or truth authority. `WSN-E9` is specifically retained to calibrate narrative-critic disagreement rather than to convert consensus into correctness.

## 9. WSN evidence debt is bound, not executed

The existing WSN identities are reused exactly; no duplicate experiment IDs are created and no experiment is marked passed. All remain `UNRUN_REQUIRED_EVIDENCE`:

- `WSN-E1` contradiction injection → cross-root bindings, chronology, information authority, and branch compatibility;
- `WSN-E2` knowledge/secret leakage → information layers, relationship/history, and quest access;
- `WSN-E3` quest solvability search → quest roles, gates, branches, failure/recovery/substitutes;
- `WSN-E4` NPC schedule conflict simulation → chronology/time interfaces; still not runnable until concrete schedules and a reviewed time policy exist;
- `WSN-E5` branching consequence persistence → high-impact branches, alternatives, durable history, and migration obligations;
- `WSN-E6` generated-content grounding tournament → generated-content grounding and mutation authority boundaries;
- `WSN-E7` semantic-sameness audit → alias/binding distinctions, gates, relationships, actor/route/consequence distinctions;
- `WSN-E8` long-horizon social/NPC simulation → durable histories, branch alternatives, actor diversity, non-degenerate trajectories;
- `WSN-E9` narrative critic disagreement calibration → truth/claim separation, branch significance, consequence quality, and originality judgments.

The fan-in makes those later attacks better specified. It does not itself constitute empirical evidence.

## 10. Residual open-binding ledger

No unresolved blocker, major, or correction-requiring minor was found in the bounded synthesis. The remaining open items are typed deferrals with explicit activation conditions:

| Open item | Class | Why it remains open | Required before |
|---|---|---|---|
| history-bearer concretion | nonblocking typed deferral | several reviewed evidence/testimony holders are compatible; conflicting accounts require explicit perspective provenance | a concrete quest naming account holders |
| common-resource / contested-project concretion | nonblocking typed deferral | several reviewed world sites satisfy the role | a concrete project/quest instance |
| outside-pressure identity | deliberate unknown boundary | external polity details remain `UNKNOWN_BY_DESIGN` | content naming/asserting an external polity |
| sensitive-site identity | nonblocking typed deferral | no universal sensitive site is reviewed | sensitive access/disclosure instance |
| character-event world chronology | nonblocking typed deferral | relationship events have meaning but no reviewed exact world position | chronology-sensitive use |
| social proposition → world fact bindings | authority deferral | social proposition roles are not objective facts | an externally bound social truth relation |
| exact `GameTimePolicy` | required downstream policy binding | exact timing remains deliberately deferred | executable timed content / `WSN-E4` |
| exact `GameSemanticGraph` version | required downstream schema binding | narrative leaves the graph version provisional | executable graph evidence/compiler work |

These are not hidden contradictions. Later work must activate the listed route rather than inventing a value opportunistically.

## 11. Self-review

Self-review attacked cross-root identifier collision, overbinding of provisional roles, chronology contradiction, fact/claim/belief/knowledge/exposure leakage, hidden foundational progression gates, branch irreversibility inflation, relationship flattening, history erasure, quest softlock/recovery gaps, invented external canon, generated-content authority inflation, originality-boundary loss, WSN evidence inflation, and engine/readiness/canonical authority inflation.

Result:

- unresolved BLOCKER: `0`;
- unresolved MAJOR: `0`;
- unresolved correction-requiring MINOR: `0`;
- residual open bindings are explicitly typed/routed and are not treated as resolved facts;
- all WSN evidence remains unrun;
- engine selection remains false/ungranted;
- gameplay/high-throughput implementation authority remains false/ungranted;
- implementation readiness, verification-PASS, release, decision, integration, and canonical-content authority remain false/ungranted.

Self-review disposition: `SELF_REVIEW_CLEAN_PENDING_FRESH_REQUIRED_REVIEW`.

## 12. Required next gate

A fresh independent/degraded-independent required review of the **exact** synthesis packet is mandatory. Suggested mission: `W2-CONTENT-SYN-01-REV-01`.

The reviewer must re-attack frozen identity and four-root provenance, exact-vs-ambiguous binding decisions, world/social/character/narrative information authority separation, chronology/branch compatibility, social+narrative gate composition, relationship/history semantics, quest failure/recovery and high-impact consequences, the honesty of every residual deferral, originality/evaluator boundaries, WSN state, and authority inflation.

Only a clean disposition `CLEAN_FOR_BOUNDED_CONTENT_CONSUMPTION` with zero unresolved correction-requiring finding may satisfy the reviewed-fan-in prerequisite for later bounded content consumers or appropriately authorized WSN routes. That disposition itself grants no integration or canonical authority. Any publication to `main` is a separate fresh authority episode and, if permitted, must be squash-only and remain noncanonical unless explicit canonicalization authority later says otherwise.
