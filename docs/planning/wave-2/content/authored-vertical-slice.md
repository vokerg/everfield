# W2-CONTENT-VS-01 — bounded authored vertical quest slice

**Issue:** #434  
**Slice ID:** `SLICE:OLD-WORKS-CONFLICTING-ACCOUNTS-01`  
**Working title:** *The Two Accounts at the Old Works*  
**State:** authored candidate / noncanonical  
**Engine dependency:** none for this bounded authored-planning packet  
**Required next gate:** fresh independent/degraded-independent review of this exact slice

## 1. Scope and frozen authority

This is exactly one authored questline instantiated from the reviewed content fan-in. It is a concrete testable content candidate, not canon, not gameplay implementation, not human-quality evidence, and not empirical WSN evidence.

Frozen inputs:

- current source `main`: `3de6f8f276cd1479ceccdea7362420f1e0efa030`;
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`;
- compiler Issue #365 map blob: `109eca8d2851db118bffe83398b49d68fdb50b31`, which declares `W2-CONTENT-VS-01` as the deferred fan-in successor;
- fan-in Issue #422 work/head: `db4bfbcc7387425989ec5902103e53953db9576b` / `f6edd59b7d029474b3de95b8f57e71e7e14e5573`;
- fan-in candidate/map blobs: `accae7e01148f19ef76b4ef0878abd3315901052` / `5858bc3e2d87baa3740b2513b08fb938633bba54`;
- fan-in integration status: `5307537330`;
- required fan-in review Issue #426 terminal `5307505361`, work/head `fccbc2812a422f06007c5d565fb3a4e3c887e76c` / `00cb20796871f9b3eb921382d388b215013130c5`, review blob `a154468dcd617c2cb8926b1edb78afe7d4f1942b`, disposition `CLEAN_FOR_BOUNDED_CONTENT_CONSUMPTION`;
- fan-in review integration status: `5307528080`.

The machine-readable companion `authored-vertical-slice.yaml` is authoritative for exact slice IDs, route predicates, information-control records, branch impacts, relationship/history events, and evidence debt.

## 2. Slice-local concretion without canon promotion

The reviewed fan-in deliberately leaves several roles plural or unresolved until a concrete content instance exists. This slice activates only the minimum two such deferrals and does so **locally**:

1. `OPEN:SYN:COMMON-RESOURCE-CONCRETION` selects `LOC:OLD-WORKS` as this quest's contested/shared-use site. It does not make Old Works the game's universal or final central project.
2. `OPEN:SYN:HISTORY-BEARER-CONCRETION` assigns the two conflicting world claims to distinct source perspectives for this quest:
   - `CLM:FRAGMENTATION-ACCOUNT-A` → `FAC-ARCHIVE-01`, institutional-record perspective;
   - `CLM:FRAGMENTATION-ACCOUNT-B` → `COM-NEIGHBOR-01`, lived-community-memory perspective.

That distinct-holder choice satisfies the fan-in constraint against silently giving one concrete holder two incompatible claims. It has no truth effect. `MYS:FRAGMENTATION-CAUSE` remains `UNKNOWN_BY_DESIGN`; neither account is promoted to `WF:FRAGMENTATION-CAUSE`.

The civic decision surface reuses reviewed `LOC:SETTLEMENT-CORE` plus `FAC-COMMONS-01`. Optional contextual witnesses are `CHAR:tomas_irel` and `CHAR:anwen_rell`, both already listed by the fan-in for investigation/provenance use.

## 3. Quest premise

After `EVT:PLAYER-ENTRY`, the player encounters two incompatible accounts of why the inherited works fragmented. The playable question is **not** “which account becomes true?” It is:

> How should the community make a bounded shared-use/repair decision at the Old Works when the historical cause remains unresolved and some contextual testimony may be confidential?

That framing lets one authored quest exercise reviewed world truth boundaries, social process, character information control, route plurality, relationship history, branch consequences, recovery, and later WSN evidence surfaces without inventing a canonical mystery answer.

The quest composes three reviewed narrative roles:

- `QROLE:INVESTIGATE_CONFLICTING_ACCOUNTS`;
- `QROLE:NEGOTIATE_SHARED_USE`;
- `QROLE:REPAIR_OR_REFRAME`.

No timed quest role, exact schedule, or exact `GameTimePolicy` is introduced.

## 4. Nontrivial lifecycle and route graph

The baseline route is deliberately not `start -> goal`.

### 4.1 Entry and two-source comparison

`QNODE:ORIENT` occurs at or after `EVT:PLAYER-ENTRY` and exposes only the existence of conflicting accounts. The player must then acquire both:

- `QNODE:ACCOUNT-A` — Account A with `FAC-ARCHIVE-01` provenance;
- `QNODE:ACCOUNT-B` — Account B with `COM-NEIGHBOR-01` provenance.

`QNODE:COMPARE` requires both sources and records their contradiction while preserving unresolved truth.

### 4.2 Meaningful optional contextual route

From comparison, the player may add context or skip it:

- `ROUTE:TOMAS-CONTEXT` uses `CHAR:tomas_irel`. Any `GATE:NARR:TRUSTED_TESTIMONY_ACCESS` evaluation remains a **SPECIALIZATION** gate under its reviewed contract. Relationship state alone cannot satisfy it. If Tomas declines or consent is absent, no testimony leaks and the quest remains solvable.
- `ROUTE:ANWEN-PROVENANCE` uses `CHAR:anwen_rell` and the **OPTIONAL** `GATE:NARR:DEEP_HISTORY_INQUIRY`. It adds provenance analysis, never truth authority.
- `ROUTE:NO-WITNESS` proceeds with the two independently sourced claims plus site inspection.

The optional routes therefore change available context and later confidentiality state without becoming mandatory gates.

### 4.3 Independent site evidence

`QNODE:INSPECT-OLD-WORKS` grounds a slice-local observation to `LOC:OLD-WORKS`. Its relation to the fragmentation cause is explicitly `INCONCLUSIVE`. If inspection cannot distinguish the accounts, `FAIL:INSPECTION-INCONCLUSIVE` routes to `RECOVERY:NEGOTIATE-WITH-UNCERTAINTY`; the authoring packet does not tune the evidence until one account wins.

### 4.4 Shared-use negotiation

`QNODE:NEGOTIATE` brings the unresolved evidence packet to a bounded shared-use process involving `FAC-COMMONS-01`, `FAC-ARCHIVE-01`, and `COM-NEIGHBOR-01`.

Three constraints are mandatory:

- no hidden foundational gate;
- ordinary baseline services and shared play remain available;
- the decision packet labels unresolved truth and any evidence gap explicitly.

The negotiation does not authorize an irreversible transformation of the Old Works.

### 4.5 Disclosure branch and terminal outcomes

If the player obtained restricted Tomas context, `QNODE:DISCLOSURE-DECISION` instantiates `BRANCH_FAMILY:DISCLOSURE_OR_WITHHOLDING`:

- `BRANCH:DISCLOSE-WITH-CONSENT` may include Tomas's testimony only after explicit disclosure consent;
- `BRANCH:WITHHOLD-RESTRICTED` excludes the testimony content and source identity while publicly marking an evidence gap.

If no restricted testimony was acquired, the quest does **not** manufacture a disclosure branch. It ends in `OUTCOME:PUBLIC-UNRESOLVED-NO-RESTRICTED`.

The two branch outcomes are:

- `OUTCOME:OPEN-PROVENANCE-PACKET`;
- `OUTCOME:CONFIDENTIALITY-PRESERVED`.

Both preserve later `QROLE:NEGOTIATE_SHARED_USE` and `QROLE:REPAIR_OR_REFRAME` goals. Neither is a canonical ending.

## 5. Failure and recovery are first-class

The slice retains four explicit fail-closed conditions:

| Failure | Trigger | Recovery |
|---|---|---|
| `FAIL:TOMAS-DECLINES` | optional direct testimony is unavailable or consent is absent | Anwen provenance route or no-witness route |
| `FAIL:INSPECTION-INCONCLUSIVE` | physical inspection cannot distinguish historical cause accounts | negotiate with uncertainty |
| `FAIL:SINGLE-CAUSE-PROMOTION` | any route tries to turn a claim/testimony/observation into the objective fragmentation cause | reject transition; return to comparison with mystery unresolved |
| `FAIL:UNAUTHORIZED-DISCLOSURE` | restricted Tomas content is selected for publication without explicit consent | reject publication; strip restricted content; return to disclosure decision |

Each failure preserves a legal continuation. No failure is silently removed to make the quest appear solvable.

## 6. Truth, knowledge, exposure, and confidentiality

The slice maintains four separate information records:

- `SLICE_INFO:ACCOUNT-A` — in-world claim only, Archive provenance;
- `SLICE_INFO:ACCOUNT-B` — in-world claim only, Neighbor provenance;
- `SLICE_INFO:TOMAS-CONTEXT` — character testimony candidate only, restricted until explicit disclosure consent;
- `SLICE_INFO:OLD-WORKS-OBSERVATION` — authored slice observation only, inconclusive relative to the world mystery.

The following are prohibited:

- claim presence or confidence becoming objective truth;
- player exposure becoming another character's knowledge;
- relationship or faction standing granting testimony access;
- generated summaries granting knowledge or authority;
- withholding private testimony being misrepresented as proof that the testimony is true or false.

A public packet may state that an evidence gap exists. Without consent it may not expose Tomas's testimony content or source identity.

## 7. Progression gates: zero foundational

The shared contract remains `ProgressionGateContract` version `1`, with foundational gate count `0`.

This slice references only optional/specialist gates:

| Gate | Reviewed class | Slice use | Required for completion |
|---|---|---|---|
| `GATE:NARR:TRUSTED_TESTIMONY_ACCESS` | `SPECIALIZATION` | optional Tomas context | no |
| `GATE:NARR:DEEP_HISTORY_INQUIRY` | `OPTIONAL` | optional Anwen provenance | no |
| `GATE-SOC-ARCHIVE-SENSITIVE-01` | `OPTIONAL` | optional archival enrichment only | no |

No gate is reclassified. No relationship score, public-standing scalar, or optional/specialist gate is required for baseline completion.

## 8. Branch impact and reversibility

Both authored disclosure branches reuse the reviewed high-impact `BRANCH_FAMILY:DISCLOSURE_OR_WITHHOLDING` and are `CONDITIONALLY_REVERSIBLE`.

### `BRANCH:DISCLOSE-WITH-CONSENT`

Before commitment, the player is told that public disclosure propagates testimony beyond the direct conversation and that stopping later distribution cannot erase the durable fact that disclosure happened.

`SLICE_IMPACT:DISCLOSE-WITH-CONSENT` records:

- authorized testimony may enter the public packet;
- every claim remains provenance-labeled and unresolved;
- future distribution can stop, but disclosure history remains;
- repair/reframe and shared-use negotiation stay available.

### `BRANCH:WITHHOLD-RESTRICTED`

Before commitment, the player is told that the public packet will omit restricted testimony and visibly retain an evidence gap. A later consented disclosure can reopen the public-record route, but prior confidentiality history remains.

`SLICE_IMPACT:WITHHOLD-RESTRICTED` records:

- restricted content is absent from the public packet;
- the evidence gap is explicit rather than hidden;
- both public claim records remain available;
- repair/reframe and shared-use negotiation stay available.

No irreversible consequence is authored, so compensation for impossible restoration is not triggered. The packet nevertheless carries explicit branch-impact records, mitigation, continued goals, and foundational-play preservation.

## 9. Multidimensional relationships and durable history

The slice preserves the fan-in rule that social and character dimensions are not one universal score.

Character dimensions remain `TRUST`, `WARMTH`, `RESPECT`, `OBLIGATION`, `RIVALRY`, `CAUTION`; social dimensions remain `trust`, `reliability`, `reciprocity`, `value_alignment`, `public_standing`, `access_state`.

Two slice-local relationship events are durable:

- `SLICE_REL_EVT:TOMAS-AUTHORIZED-DISCLOSURE` — bounded `RESPECT` increase after consented disclosure;
- `SLICE_REL_EVT:TOMAS-CONFIDENTIALITY-HONORED` — bounded `TRUST` increase after honoring confidentiality.

Both are explicitly at or after `EVT:PLAYER-ENTRY`; both preserve history after later relationship changes; neither changes knowledge automatically.

A separate `SLICE_SOCIAL:COMMONS-PROCESS-RECORD` retains process history without synthesizing a universal standing score or access grant. Public standing cannot substitute for private trust, confidentiality permission, character knowledge, or objective truth.

## 10. Chronology and timing remain bounded

All non-retrospective slice nodes and slice-created relationship events occur at or after `EVT:PLAYER-ENTRY`. No exact date is authored.

This packet does not bind:

- an exact `GameTimePolicy`;
- a concrete NPC schedule;
- a witness-availability duration;
- a consequence-response duration;
- an exact calendar.

`WSN-E4` therefore remains `NOT_RUN / BLOCKED_BY_EXACT_PREREQUISITE`.

## 11. Generated-content and originality boundary

Generated presentation may create wording variants or summaries only when grounded to the exact slice/fan-in refs. It cannot create objective facts, secrets, character knowledge, relationship state, branch facts, authoritative transitions, or canon. Grounding failure must use a declared fallback or remain inconclusive.

The slice adopts no external fictional expression. The working title and all slice-local IDs are provisional Everfield candidate material. Any later external reference requires explicit purpose, provenance, originality review, and rights review where applicable.

## 12. WSN evidence debt

Authorship does not upgrade any WSN result. The slice maps its claims to the existing experiment IDs only:

| WSN ID | Slice surface | Required later attack |
|---|---|---|
| `WSN-E1` | claim/branch compatibility | inject contradictions; reject truth or incompatible-branch promotion |
| `WSN-E2` | testimony, exposure, relationships, generation | attempt unauthorized knowledge/secret leaks through every non-authoritative route |
| `WSN-E3` | quest graph, alternatives, failures/recovery, gates | search route combinations for dead ends, cycles, missing substitutes, and soft locks |
| `WSN-E4` | timing/schedule interface | remain `NOT_RUN` until reviewed time policy + concrete schedules exist |
| `WSN-E5` | branch impacts and durable history | persist/reload/migrate branch state, history, continued goals, and mitigation |
| `WSN-E6` | generated presentation | reject ungrounded generation and direct authoritative mutation |
| `WSN-E7` | witness routes + disclosure branches | prove route/branch variants are semantically distinct rather than presentation aliases |
| `WSN-E8` | multidimensional relationship/history + continuations | run long-horizon traces without scalar collapse or history erasure |
| `WSN-E9` | truth separation + branch significance + originality | preserve critic disagreement without granting truth/canon authority |

No duplicate WSN identity is created and no authored outcome is represented as empirical PASS.

## 13. Residual open-binding ledger

The slice resolves only what its scope requires:

- common-resource concretion → `LOC:OLD-WORKS`, **slice-local only**;
- history-bearer concretion → distinct Account A / Account B holders, **slice-local only**.

The following remain open:

- `OPEN:SYN:OUTSIDE-PRESSURE` — not activated; no external polity is named;
- `OPEN:SYN:SENSITIVE-SITE` — not activated;
- `OPEN:SYN:CHARACTER-EVENT-CHRONOLOGY` — existing root relationship events are not used for chronology-sensitive claims; new slice events have explicit order constraints;
- `OPEN:SYN:SOCIAL-PROPOSITION-FACT-BINDINGS` — no social assertion is bound into objective fact authority;
- `OPEN:SYN:GAME-TIME-POLICY` — still blocks timed execution and `WSN-E4`;
- `OPEN:SYN:SEMANTIC-GRAPH-VERSION` — remains unbound; this packet claims no executable graph-schema evidence.

## 14. Self-review and authority boundary

Self-review attacked:

- unsupported cross-root concretion;
- truth/claim/knowledge/exposure/confidentiality leakage;
- trivial route collapse or a disguised `start -> goal`;
- hidden foundational or reclassified progression gates;
- relationship scalar flattening and history erasure;
- weak branch signaling, recovery, mitigation, or continued goals;
- generated-content authority inflation;
- invented time policy/schedules;
- external-polity or hidden-canon invention;
- WSN evidence laundering;
- engine/implementation/readiness/release/decision/integration authority inflation.

Result: `0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR` in this authored-content scope.

Disposition: `SELF_REVIEW_CLEAN_PENDING_FRESH_REQUIRED_REVIEW`.

A fresh reviewer must judge the exact producer packet before bounded downstream consumption. Suggested mission: `W2-CONTENT-VS-01-REV-01`.

This packet grants **no** canon, empirical WSN PASS, engine selection, gameplay/high-throughput implementation, implementation readiness, verification-PASS, provider/legal/platform/release, decision, or integration authority.
