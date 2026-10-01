# Old Works world/evidence presentation — implementation-fed candidate

## Status and authority

- mission: `CONTENT-DEMAND-OLD-WORKS-WORLD-01`
- issue: #1378
- demand intake: #1377
- implementation source: #1343 / PR #1370
- implementation source head observed by the intake: `5aefb403b35bde1ab754b9feca2916e3f5b4ea03`
- authored vertical-slice source: `VS:OLD-WORKS-ACCOUNTS-01`
- corrected authored-slice YAML blob: `8d341d534ef4a27929aaabdf5b81a6d5ff86b80e`
- clean remediation review: #449, `CLEAN_FOR_BOUNDED_AUTHORED_CONTENT_CONSUMPTION`
- world-setting facts blob: `baa827528994864faa3f50c8b0785dd89a775a14`
- canonical Planning Program blob: `fd4cf1119c3f86acc3af620024eea72235e81ce4`
- canonical binding: Issue #1147 comment `5675066392`
- canonicality: `NOT_CANONICAL`

This packet is candidate presentation content for the already-running Old Works first-playable slice. It does not alter gameplay code, choose a final site or polity, settle historical causation, grant implementation/readiness/release authority, or promote any claim to objective truth.

## Frozen content boundaries

The packet preserves the reviewed source model exactly where authority matters:

- `LOC:OLD-WORKS` is the slice-local contested/shared-use site, not a globally selected contested common.
- The inherited works are legacy shared infrastructure with water-or-route and historical-evidence functions.
- Coordinated maintenance fragmented before the patchwork present, but exact chronology remains relative and date-free.
- `CLM:FRAGMENTATION-ACCOUNT-A` asserts and `CLM:FRAGMENTATION-ACCOUNT-B` denies the single-dominant-cause proposition; both remain `IN_WORLD_CLAIM_ONLY` with `truth_effect: NONE`.
- `MYS:FRAGMENTATION-CAUSE` remains `UNKNOWN_BY_DESIGN`.
- Public record and material trace are distinct nonprivate evidence surfaces. Neither route reveals `INFO:anwen_contested_record_provenance_gap`.
- Restoration is not intrinsically the preferred outcome, and presentation may not silently create ownership, consent, legitimacy, representation, or final historical authority.

## Bounded location identity

For this playable instance, the **Old Works** read as a maintained-through-use place rather than a ruin frozen at one moment.

The player crosses a compact working yard where inherited stone channels, timber walkways, patched housings, reused fittings, and newer braces sit beside one another. Some parts still carry water or foot traffic; other sections are bypassed, capped, or repurposed. No single visual layer is labeled “original.” The point of the place is legible accumulation: coordinated works existed, later maintenance became patchwork, and current people continue to use and argue over what remains.

This presentation is intentionally compatible with more than one historical explanation. Mismatched materials, repairs over repairs, and incomplete labels are evidence of change and reuse, not evidence of one final cause.

### Spatial reading

The first-playable stations form one short evidence-to-decision walk:

1. **Archive Ledger** — a sheltered record table at the yard edge; public documentation can be read without private access.
2. **Material Trace** — an exposed repair seam where several construction/maintenance layers can be compared directly.
3. **Defer Conclusion** — a quiet overlook beside the same works; uncertainty is presented as an explicit legal state, not as failure to play.
4. **Commons Hearing** — a cleared shared-use space within sight of the works; evidence can inform negotiation without becoming truth.
5. **Project Table** — a practical work surface near the current repair access; commitment concerns what to do next, not what history must mean.

These are presentation relationships only. They do not establish final property boundaries, offices, institutional ownership, or exact geography outside the bounded scene.

## Implementation-facing presentation strings

### Place and approach

| ID | Surface | Candidate player-facing text |
| --- | --- | --- |
| `OW_WORLD_TITLE` | scene title | **The Old Works** |
| `OW_WORLD_SUBTITLE` | scene subtitle | **Inherited channels, patched routes, unfinished arguments.** |
| `OW_WORLD_ENTRY` | entry cue | **Old stone, newer timber, and repairs from more than one hand meet in the same working yard. Nothing here explains itself in one layer.** |
| `OW_WORLD_ROUTE_CUE` | traversal cue | **The ledger table, exposed repair seam, hearing space, and project table all face the same inherited works.** |

### Archive Ledger / public record

The public record must expose disagreement without exposing Anwen's deny-by-default secret.

| ID | Surface | Candidate player-facing text |
| --- | --- | --- |
| `OW_ARCHIVE_TITLE` | station title | **Archive Ledger** |
| `OW_ARCHIVE_PROMPT` | interaction prompt | **Read the public record.** |
| `OW_ARCHIVE_BODY_01` | ledger text | **The surviving entries agree that coordinated upkeep broke apart. They do not agree that one cause explains why.** |
| `OW_ARCHIVE_BODY_02` | ledger text | **One recorded account argues for a single dominant cause. Another rejects that reading. Both remain recorded as accounts, not findings.** |
| `OW_ARCHIVE_BODY_03` | ledger text | **Later pages list local repairs, bypasses, and changed uses without resolving the older dispute.** |
| `OW_ARCHIVE_EXIT` | post-read cue | **The ledger gives you claims and a sequence of changes—not a verdict. Compare it with something independent, or leave the conclusion open.** |

The archive surface intentionally does **not** identify a hidden provenance gap, reveal private testimony, or imply that record custody authenticates either causal claim.

### Material Trace / independent evidence

| ID | Surface | Candidate player-facing text |
| --- | --- | --- |
| `OW_TRACE_TITLE` | station title | **Material Trace** |
| `OW_TRACE_PROMPT` | interaction prompt | **Inspect the repair seam.** |
| `OW_TRACE_BODY_01` | observation | **A dressed stone channel continues beneath a later timber crossing. Their wear patterns do not match exactly.** |
| `OW_TRACE_BODY_02` | observation | **Several fasteners and braces were added after the surrounding surface had already weathered. Some older fixing points are empty.** |
| `OW_TRACE_BODY_03` | observation | **The trace supports a history of alteration and repeated maintenance. It does not identify a single cause for the fragmentation.** |
| `OW_TRACE_EXIT` | post-read cue | **This is independent material evidence within the inspected surface, not proof of either account.** |

The phrases “supports” and “independent” are deliberately scoped to the visible alteration history. They do not claim that every material feature has independent provenance, and they do not convert observation count into truth strength.

### Explicit truth deferral

| ID | Surface | Candidate player-facing text |
| --- | --- | --- |
| `OW_DEFER_TITLE` | station title | **Leave the Cause Open** |
| `OW_DEFER_PROMPT` | interaction prompt | **Record that the evidence is insufficient for a final conclusion.** |
| `OW_DEFER_RESULT` | result | **You can act on the present condition without pretending the old dispute is settled.** |

### Shared environmental cues

These cues may be distributed across labels, hover text, or low-cost scene dressing:

- `OW_ENV_CHANNEL_PATCHWORK`: **Old channel edge; later patch; another repair over that.**
- `OW_ENV_BYPASS`: **A capped opening sits beside a narrower working bypass.**
- `OW_ENV_REUSED_FITTING`: **A reused fitting carries marks from more than one placement.**
- `OW_ENV_LEDGER_TO_TRACE`: **The ledger records repairs in general; the seam shows one place where change is physically visible.**
- `OW_ENV_TRACE_TO_HEARING`: **From the repair seam, the hearing space remains in view: observation can travel into debate without becoming a verdict.**
- `OW_ENV_HEARING_TO_PROJECT`: **The project table is close enough to the works to make tradeoffs concrete, but no repair plan answers the historical mystery by itself.**

## Presentation invariants

Any later implementation consumption of this packet must preserve all of the following:

1. `MYS:FRAGMENTATION-CAUSE = UNKNOWN_BY_DESIGN` before and after every interaction.
2. `CLM:FRAGMENTATION-ACCOUNT-A` and `CLM:FRAGMENTATION-ACCOUNT-B` remain claims with zero truth effect.
3. Public-record access does not reveal `INFO:anwen_contested_record_provenance_gap`; only the reviewed explicit-holder-disclosure or separately validated-authority routes may do so.
4. The material trace may establish bounded observations about alteration/maintenance layers; it may not select a causal winner.
5. “Independent evidence” is scoped to the inspected material surface and must not be inferred from mere visual difference, count, repetition, or institutional provenance.
6. The player may legally defer a truth conclusion after the required public record; uncertainty is not a hidden failure state.
7. Scene dressing cannot establish final owner, custodian, office holder, polity, chronology, original purpose, or universal restoration preference.
8. Presentation strings have no direct fact, secret, knowledge, branch, relationship, canonical, or authority mutation effect.
9. Ordinary progression through the implemented slice remains possible without private-secret content.
10. No candidate string may reinterpret repair-pilot, records-first, or later completion as proof of a historical causal account.

## Consumption boundary

This packet is deliberately small. It supplies presentation strings/IDs and enough local texture for the existing first playable to stop reading as debug stations. It does not author Commons Hearing participant dialogue (#1379), commitment consequence presentation (#1380), gameplay code, voice casting, final art direction, final map geometry, final chronology, or a broader Old Works quest backlog.

Fresh required review of this exact packet is mandatory before integration or implementation consumption.
