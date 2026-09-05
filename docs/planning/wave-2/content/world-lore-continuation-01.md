# W2-CONTENT-WORLD-CONT-01 — bounded world/lore/history/location continuation

**Issue:** #811  
**State:** PRODUCER CANDIDATE / NONCANONICAL / REQUIRED FRESH ROOT REVIEW PENDING  
**Conflict domain:** `CONTENT`  
**Engine dependency:** none for this bounded planning output

## 1. Authority and frozen inputs

This packet is the activated world/lore/history/location continuation root from the reviewed content frontier. It consumes immutable reviewed inputs and does not edit them.

Frozen routing and authority:

- current producer base: `main@ab3bc02d502243a6194c42960dd3ea854d14766f`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- canonical binding: Issue #6 comment `5245368879`;
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- continuation compiler: Issue #806, exact producer head `ffdb55f3ac103d4f57da9b758df8a3676eb89a09`;
- recovered activation review: Issue #831 terminal comment `5525721241`, disposition `CLEAN_FOR_BOUNDED_CONTENT_FRONTIER_CONTINUATION_ACTIVATION`;
- activation scope: exactly #811–#815;
- reviewed predecessor world files: `world-setting-foundation.md` blob `3caaddf10e27cefb91c35b6a4f374740aa3c6731` and `world-setting-facts.yaml` blob `baa827528994864faa3f50c8b0785dd89a775a14`;
- reviewed fan-in: Markdown blob `accae7e01148f19ef76b4ef0878abd3315901052`, map blob `5858bc3e2d87baa3740b2513b08fb938633bba54`, clean review terminal `5307505361`;
- corrected authored vertical slice: Markdown/YAML blobs `5e94bdb0ca6146bab93264fc8e6763590aa289d2` / `8d341d534ef4a27929aaabdf5b81a6d5ff86b80e`, clean review disposition `CLEAN_FOR_BOUNDED_AUTHORED_CONTENT_CONSUMPTION`;
- reviewed WSN packet: #432/#437, clean bounded-consumption terminal `5308501587`.

The authored slice is a regression/reference fixture only. This continuation is `NOT_CANONICAL`; candidate specificity below is reviewable planning content, not final setting truth.

## 2. Bounded continuation objective

Deepen the existing watershed setting in four places only:

1. make the existing locations more useful to sibling authors through typed place interfaces;
2. add relative historical layers and trace relationships without dates or schedules;
3. add a small set of environmental/land-use tensions that expose consequences without assigning factions, characters, or quests;
4. strengthen fact/claim/mystery and provenance boundaries so later lore can disagree without silently becoming objective truth.

This is not a setting bible. It adds no new region, polity, pantheon, calendar, named settlement, named historical figure, fixed player origin, final ownership, or engine representation.

## 3. Place interfaces

The continuation does not replace the reviewed locations. It adds six bounded interfaces over them. Each interface describes what another content lane may safely ask of the world packet while leaving concrete sibling bindings unresolved.

| Interface | Reviewed locations | Stable world affordance | Explicitly unresolved |
|---|---|---|---|
| `WORLD_IFACE:WATER-DEPENDENCY` | `LOC:UPLAND-CATCHMENT`, `LOC:RIPARIAN-CORRIDOR`, `LOC:CULTIVATION-MOSAIC` | upstream condition can create downstream constraints; water use and habitat pressure remain distinct dimensions | final user groups, allocations, schedules, quantitative flow |
| `WORLD_IFACE:SHARED-WORKS-JUNCTION` | `LOC:OLD-WORKS`, `LOC:RIPARIAN-CORRIDOR`, `LOC:SETTLEMENT-CORE` | inherited works can alter access and water function across more than one zone | original purpose, owner, preferred repair outcome, exact operation calendar |
| `WORLD_IFACE:COMMONS-EDGE` | `LOC:COMMONS-BELT`, `LOC:EDGE-HABITAT` | shared access and habitat pressure can improve or degrade independently | final custodians, quotas, species lists, seasonal closure schedule |
| `WORLD_IFACE:CULTIVATION-MARGIN` | `LOC:CULTIVATION-MOSAIC`, `LOC:RIPARIAN-CORRIDOR`, `LOC:EDGE-HABITAT` | productive use, water condition, and habitat continuity may trade off without one prosperity score | crops, ownership, exact yields, timed planting windows |
| `WORLD_IFACE:HISTORY-TRACE` | `LOC:OLD-WORKS`, `LOC:SETTLEMENT-CORE`, `LOC:COMMONS-BELT` | layered modifications and records can expose evidence from more than one historical layer | one authoritative fragmentation story, named builders, exact dates |
| `WORLD_IFACE:OUTER-CONNECTION` | `LOC:SETTLEMENT-CORE`, `LOC:OUTER-THRESHOLD` | exchange, travel, information, and obligations can enter or leave the bounded setting | neighboring polities, route timetable, external geography, final trade dependency |

These interfaces are intentionally cross-domain hooks. `SOCIAL_ROLE:*`, `CHAR_ROLE:*`, and `NARR_ROLE:*` references may consume them provisionally; this root cannot bind those roles to concrete sibling entities.

## 4. Relative history continuation

The reviewed era order remains exactly:

`ERA:PRE-WORKS` -> `ERA:WORKS-BUILDOUT` -> `ERA:PATCHWORK-PRESENT`.

This continuation adds **historical layers**, not new dated eras:

- `HIST_LAYER:PRIOR-USE`: traces of landscape/community use that predate coordinated works. It is contained by `ERA:PRE-WORKS` and may overlap the earliest evidence later incorporated into the works.
- `HIST_LAYER:COORDINATED-WORKS`: evidence that multiple works were once maintained or understood as a connected system. It is contained by `ERA:WORKS-BUILDOUT`.
- `HIST_LAYER:FRAGMENTED-PRACTICE`: evidence that maintenance, use, or interpretation became locally divergent. It occurs after `EVT:WORKS-BUILDOUT` and is compatible with, but does not explain, `EVT:WORKS-FRAGMENTATION`.
- `HIST_LAYER:PRESENT-ADAPTATION`: current repair, abandonment, repurposing, and informal adaptation. It is contained by `ERA:PATCHWORK-PRESENT` after `EVT:PATCHWORK-PRESENT-START`.

The layers support relative constraints only. They do not assert years, durations, season counts, day/night timing, weather chronology, travel time, NPC schedules, opening hours, or timed quest windows. Those remain blocked by exact time/schedule evidence debt, including WSN-E3, WSN-E4, and WSN-E8.

### Trace rule

A historical trace has a stable `TRACE:*` identity, one or more location references, a layer reference, an observation authority, and an interpretation state. A physical observation may be candidate-objective while its explanation remains disputed or unknown. For example, a visibly modified channel can be represented as an observation without deciding who modified it or why.

## 5. Bounded historical traces

Four candidate traces deepen the reviewed foundation without resolving its mysteries:

1. `TRACE:WORKS-MULTI-LAYER-MODIFICATION` — `LOC:OLD-WORKS`. Distinct repair or repurposing layers are observable; attribution and exact chronology remain unresolved.
2. `TRACE:RIPARIAN-ROUTE-REALIGNMENT` — `LOC:RIPARIAN-CORRIDOR` + `LOC:OLD-WORKS`. Physical evidence supports that access/water-use relationships changed across historical layers; the trigger and dates remain unresolved.
3. `TRACE:COMMONS-BOUNDARY-NEGOTIATION` — `LOC:COMMONS-BELT` + `LOC:EDGE-HABITAT`. Repeated signs of negotiated use boundaries are representable; this does not establish permanent ownership or one continuous institution.
4. `TRACE:OUTER-EXCHANGE-RESIDUE` — `LOC:OUTER-THRESHOLD` + `LOC:SETTLEMENT-CORE`. Material/information exchange with places outside the bounded watershed is supported as an interface; external regions and polities remain deliberately unfrozen.

None of these traces supplies the single cause of fragmentation. No trace promotes an in-world claim to objective truth.

## 6. Environmental and land-use tensions

The packet adds four candidate tension frames. A tension is not a quest, faction conflict, or moral verdict; it is a typed world condition that sibling lanes may instantiate later.

### `TENSION:UPSTREAM-DOWNSTREAM-STEWARDSHIP`

- world basis: `WORLD_IFACE:WATER-DEPENDENCY`;
- dimensions: upstream access/use, downstream water condition, cultivation reliability, habitat condition;
- rule: improving one dimension may create cost or constraint in another;
- sibling hooks: `SOCIAL_ROLE:WATER-DEPENDENT-USER`, `NARR_ROLE:CONSEQUENCE-WITNESS`;
- prohibited inference: no fixed water rights, rationing schedule, drought calendar, or final beneficiary.

### `TENSION:WORKS-REPAIR-REPURPOSE-RELEASE`

- world basis: `WORLD_IFACE:SHARED-WORKS-JUNCTION`;
- dimensions: structural condition, current usefulness, historical evidence, access consequence, ecological consequence;
- rule: restoration is not automatically superior to repurpose, partial stabilization, or deliberate non-restoration;
- sibling hooks: `SOCIAL_ROLE:PUBLIC-WORKS-STAKE`, `CHAR_ROLE:HISTORY-INTERPRETER`, `NARR_ROLE:WORKS-CHOICE`;
- prohibited inference: no universal optimal state and no original-purpose answer.

### `TENSION:COMMONS-ACCESS-HABITAT-PRESSURE`

- world basis: `WORLD_IFACE:COMMONS-EDGE`;
- dimensions: shared access, productive use, habitat pressure, cultural continuity;
- rule: access restriction and access expansion may each produce mixed consequences;
- sibling hooks: `SOCIAL_ROLE:COMMONS-STAKE`, `CHAR_ROLE:LOCAL-USER`, `NARR_ROLE:ACCESS-CONSEQUENCE`;
- prohibited inference: no final custodian, quota, species calendar, or morality score.

### `TENSION:CULTIVATION-MARGIN-TRADEOFF`

- world basis: `WORLD_IFACE:CULTIVATION-MARGIN`;
- dimensions: productive capacity, water demand, habitat continuity, route/access condition;
- rule: a change must expose affected dimensions rather than collapse them into one progress value;
- sibling hooks: `SOCIAL_ROLE:LAND-USE-STAKE`, `NARR_ROLE:LAND-USE-CONSEQUENCE`;
- prohibited inference: no crop catalogue, property regime, yield curve, or season schedule.

## 7. Lore authority model

The predecessor separation remains mandatory:

- `CANDIDATE_OBJECTIVE`: reviewable candidate world truth in this packet, still noncanonical project-wide;
- `CANDIDATE_CONSTRAINT`: design invariant;
- `UNKNOWN_BY_DESIGN`: deliberately unresolved truth;
- `DISPUTED_IN_WORLD`: a fact-level state intentionally represented as disputed;
- `PROVISIONAL_INTERFACE`: cross-domain placeholder;
- `IN_WORLD_CLAIM_ONLY`: testimony, rumor, belief, tradition, annotation, or interpretation that cannot mutate objective facts by itself.

This continuation adds a `lore_records` surface with three record forms:

- `OBSERVATION`: what is materially observable or mechanically represented;
- `INTERPRETATION`: an in-world explanatory claim about an observation;
- `ABSENCE`: a bounded statement that the packet does not currently establish a requested answer.

An interpretation may reference an observation but cannot inherit its truth authority. An `ABSENCE` is not evidence that the opposite proposition is true.

## 8. Lore records

The machine-readable companion contains a minimal set:

- `LORE:OLD-WORKS-LAYERS-OBSERVED` — observation that inherited works show multiple modification layers; does not identify builders or purpose.
- `LORE:FRAGMENTATION-LOCAL-ACCOUNT` — interpretation that local stewardship divergence mattered; `IN_WORLD_CLAIM_ONLY`, `ABOUT_UNKNOWN_BY_DESIGN` with respect to `WF:FRAGMENTATION-CAUSE`.
- `LORE:OUTER-EXCHANGE-OBSERVED` — observation that the bounded setting has evidence of exchange beyond itself; does not define external geography.
- `LORE:ANOMALY-CAUSE-ABSENT` — explicit absence of a resolved ontology for seasonal anomalies; prevents generated lore from filling the gap.

The existing contradictory fragmentation accounts remain valid regression cases. This continuation neither chooses between them nor creates a third authoritative answer.

## 9. Branch applicability

All continuation records declare branch applicability explicitly:

- `BRANCH:BASELINE` means the candidate is part of the baseline continuation packet;
- `BRANCH:PROVISIONAL` means it is an interface or hypothesis that requires downstream binding;
- no new permanent mutually exclusive world branch is authorized here.

A downstream branch may add scoped state, but it may not silently rewrite historical traces or promote an interpretation into objective fact. Cross-root contradiction resolution belongs at `W2-CONTENT-SYN-CONT-01` after all five roots are clean-reviewed.

## 10. Sibling interfaces and independence

This root emits typed hooks only. It does not read sibling mutable output and does not require sibling completion.

Provisional hooks intentionally use domain-owned namespaces:

- `SOCIAL_ROLE:WATER-DEPENDENT-USER`, `SOCIAL_ROLE:PUBLIC-WORKS-STAKE`, `SOCIAL_ROLE:COMMONS-STAKE`, `SOCIAL_ROLE:LAND-USE-STAKE`;
- `CHAR_ROLE:HISTORY-INTERPRETER`, `CHAR_ROLE:LOCAL-USER`;
- `NARR_ROLE:CONSEQUENCE-WITNESS`, `NARR_ROLE:WORKS-CHOICE`, `NARR_ROLE:ACCESS-CONSEQUENCE`, `NARR_ROLE:LAND-USE-CONSEQUENCE`.

These identifiers are unresolved interfaces, not concrete factions, characters, quests, or ownership assignments. Sibling roots may accept, reject, split, or map them during their own reviewed work. Concrete reconciliation belongs at fan-in.

## 11. Vertical-slice regression use

The corrected authored vertical slice may test only reviewed semantic behavior: deny-by-default secret authority, substitute evidence/testimony routes, optional objectives, recoverability, branch consequence, and solvability without privileged knowledge. Its concrete names, people, locations, events, and plot are not imported into this packet.

A mismatch with slice fiction is not automatically a defect if the world continuation preserves the reviewed invariant. A mismatch with a reviewed semantic constraint is a review finding.

## 12. WSN evidence discipline

This packet preserves the exact bounded WSN status:

- E1 PASS;
- E2 PASS;
- E3 INCONCLUSIVE — timed coverage blocked;
- E4 NOT_RUN — exact time/schedule prerequisites absent;
- E5 PASS — bounded model only;
- E6 PASS;
- E7 PASS;
- E8 INCONCLUSIVE — schedule/reachability blocked;
- E9 PASS.

Therefore no record here claims a concrete schedule, weather calendar, NPC reachability guarantee, timed-window completeness, production persistence, human-quality PASS, or aggregate verification PASS. Prose cannot upgrade evidence.

## 13. Assumptions and reopen conditions

- `ASM:WORLD-CONT-01`: the six place interfaces are sufficient for the next bounded sibling tranche without new regions. Reopen if a clean sibling review proves a missing world interface is a hard dependency.
- `ASM:WORLD-CONT-02`: relative historical layers are sufficient before `GameTimePolicy`. Reopen if downstream content cannot express a required relation without exact time semantics.
- `ASM:WORLD-CONT-03`: the four tension frames expose enough cross-location consequence structure without concrete social ownership. Reopen if fan-in finds an unrepresentable conflict.
- `ASM:WORLD-CONT-04`: observations and interpretations can remain separate through generated-content tooling. Reopen if evaluation demonstrates authority leakage.

Explicit reopen routes:

- reviewed sibling requires incompatible topology or history -> `W2-CONTENT-SYN-CONT-01` contradiction reconciliation;
- WSN evidence invalidates a causal or authority assumption -> reopen only affected continuation records;
- originality review finds material expressive similarity -> quarantine and rewrite affected candidate content;
- exact time/schedule semantics become necessary -> route scoped `GameTimePolicy` prerequisite rather than inventing dates here;
- concrete engine dependency emerges -> record the scoped technical dependency only; do not retroactively make engine selection a root prerequisite.

## 14. Checkable packet rules

The companion YAML is the controlling machine-readable surface. At minimum it must prove:

1. every continuation interface references only reviewed location IDs;
2. every historical layer binds to a reviewed era and no exact date/duration fields exist;
3. every trace has explicit observation authority and interpretation state;
4. every tension references declared interfaces and keeps affected dimensions separate;
5. every lore interpretation remains `IN_WORLD_CLAIM_ONLY` and cannot promote fact authority;
6. every sibling hook uses a provisional typed namespace and no concrete sibling entity IDs appear;
7. no vertical-slice concrete fiction is adopted as world truth;
8. WSN E3/E4/E8 limitations and E5 bounded-model limitation remain explicit;
9. no new branch grants canon, implementation, integration, verification, release, or decision authority.

## 15. Self-review

Producer self-review: **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in this bounded root scope.

Attacks performed:

- no predecessor file was edited;
- no sibling mutable output is consumed;
- no exact calendar, schedule, travel-time, weather-window, or NPC-reachability claim is introduced;
- historical observations and interpretations remain separate;
- fragmentation and supernatural ontology remain unresolved;
- location/tension records do not bind final factions, characters, quests, or ownership;
- the vertical slice remains noncanonical reference only;
- WSN outcomes are preserved without prose promotion;
- output scope remains exactly the two #811 candidate files plus `docs/planning/handoffs/issue-811.md`;
- downstream fan-in is not materialized early.

## 16. Required fresh root review and authority boundary

The immutable producer head requires one fresh independent/degraded-independent root review before any fan-in consumption. The reviewer must attack invented canon, chronology/time overreach, objective-fact/claim leakage, hidden sibling dependency, mutable-path overlap, vertical-slice authority inflation, WSN evidence laundering, originality boundaries, and scope growth.

A clean root review may authorize only bounded fan-in consumption of the exact reviewed root token. This packet grants no final canon, engine selection, gameplay/high-throughput implementation, implementation readiness, empirical WSN PASS, verification PASS, release, integration, decision, or canonical authority.