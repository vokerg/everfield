# Issue #386 required remediation review - W2-CONTENT-WORLD-REM-REV-01

## Disposition

`CHANGES_NEEDED`

Trust mode: `DEGRADED_SINGLE_AGENT`.

Finding count: **0 BLOCKER / 0 MAJOR / 2 correction-requiring MINOR**.

This is the mandatory fresh review of the exact immutable Issue #382 / `W2-CONTENT-WORLD-REM-01` remediation packet. The predecessor MAJOR findings are structurally closed by the remediation, but the exact successor packet still contains two correction-requiring consistency/regression defects. Therefore it is not clean for `W2-CONTENT-SYN-01` fan-in.

This review does not mutate the judged remediation, author replacement world content, integrate anything, grant fan-in authority, or make any content canonical.

## Frozen judged identity

- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- review claim main/base: `32637bf66d8e76a4f029c9ca74f983cbe5535ffb`
- review winning claim: Issue #386 comment `5305984671`
- content-frontier compiler work: `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`
- content-frontier activation review terminal: Issue #372 comment `5305598079`

Immutable producer predecessor:
- Issue #366 / `W2-CONTENT-WORLD-01`
- claim `5305649840`
- terminal `5305661660`
- work `8dc85721e446727f4b2eb59b0c35bd98edb53f20`
- exact terminal head `6f77a245e4905d33448f6dc7e0d898f6e4db3d43`
- draft PR #377

Immutable predecessor required review:
- Issue #378 / `W2-CONTENT-WORLD-REV-01`
- terminal `5305684626`
- exact review work/head `0b04440221a63e3906cf24991c846116e68f0cca`
- disposition `CHANGES_NEEDED`
- findings 0 BLOCKER / 2 MAJOR / 0 MINOR
- exact findings `W2-CONTENT-WORLD-REV-M01`, `W2-CONTENT-WORLD-REV-M02`
- noncanonical review-provenance squash publication `79f5bd62f7d03ecd954e94a485b0734bd80f1b86`

Exact judged remediation:
- Issue #382 / `W2-CONTENT-WORLD-REM-01`
- claim `5305696218`
- terminal `5305711075`
- exact work/head `01da67730e18bd9497d264d3a3514122e6793ab7`
- draft PR #385 at the exact same head
- PR base at remediation terminalization: `main@79f5bd62f7d03ecd954e94a485b0734bd80f1b86`
- PR state at review claim: open, draft, not merged; current mergeability did not confer review or integration authority
- changed paths exactly:
  - `docs/planning/wave-2/content/world-setting-foundation.md`
  - `docs/planning/wave-2/content/world-setting-facts.yaml`
  - `docs/planning/handoffs/issue-382.md`

The exact #382 branch and PR were frozen before substantive review and were not modified by this episode.

## Review method and required attacks

The review reconciled the exact #382 Markdown/YAML/handoff surfaces against the frozen #366 producer, the first required review #378, current canonical planning authority, and the #386 contract. It attacked:

1. frozen identity and provenance;
2. objective fact versus proposition/claim authority;
3. holder/source/perspective representation without mutable sibling bindings;
4. exposure/knowledge versus truth separation;
5. fail-closed claim-to-fact promotion paths;
6. era-order completeness;
7. event containment and present-start semantics;
8. event precedence and cross-era compatibility;
9. Markdown/YAML consistency;
10. regressions in topology/causality, sibling independence, engine neutrality, noncanonicality, bounded scope, originality, assumptions/reopen routes, and WSN evidence discipline;
11. scope expansion;
12. authority inflation.

## Predecessor finding retest

### W2-CONTENT-WORLD-REV-M01 - structural closure PASS

The remediation materially closes the predecessor MAJOR at the structural level.

The machine surface now has a separate proposition/claim layer instead of overloading objective fact authority or exposure state. `PROP:*` and `CLM:*` identities are stable. Claims carry `IN_WORLD_CLAIM_ONLY`, a provisional holder role, a perspective key, proposition reference, stance, knowledge/exposure, branch scope, truth relation, and `truth_effect: NONE`. The exact two fragmentation accounts use `ROLE:HISTORY-BEARER` without consuming a concrete mutable sibling character or faction.

`INV:CLAIM-NO-FACT-PROMOTION` and `INV:PROPOSITION-NOT-FACT` make the core authority separation fail closed: a claim cannot create, mutate, or substitute a `CANDIDATE_OBJECTIVE` fact merely by existing, and a proposition carries `NONE_PROPOSITION_ONLY` objective authority. `INV:CLAIM-EXPOSURE-SEPARATE-FROM-TRUTH` also keeps knowledge/exposure independent from truth and fact authority.

No reviewed path promotes either contradictory account into `WF:FRAGMENTATION-CAUSE`; that fact remains `UNKNOWN_BY_DESIGN` with `HAS_SINGLE_RESOLVED_CAUSE: false`.

The structural predecessor MAJOR is therefore closed. The exact packet nevertheless fails clean disposition because of `W2-CONTENT-WORLD-REM-REV-MIN01` below.

### W2-CONTENT-WORLD-REV-M02 - structural closure PASS

The remediation materially closes the predecessor chronology MAJOR.

The machine surface now defines three eras with unique contiguous `order_index` values `0..2`, explicitly orders each adjacent pair in `chronology.era_precedes`, assigns every declared event to exactly one declared era, and separates event-level precedence from era ordering.

The exact event chain is:

`EVT:WORKS-BUILDOUT` -> `EVT:WORKS-FRAGMENTATION` -> `EVT:PATCHWORK-PRESENT-START` -> `EVT:PLAYER-ENTRY`.

The first two events are contained in `ERA:WORKS-BUILDOUT`; present-start and player-entry are contained in `ERA:PATCHWORK-PRESENT`. `EVT:PATCHWORK-PRESENT-START` is explicitly an `ERA_START_BOUNDARY` and precedes player entry in the same era.

The invariant set checks contiguous era indices, complete adjacent-era precedence, event-era resolution, event-precedence acyclicity, non-backward cross-era precedence, and present-start containment. Relative chronology remains date-free and does not invent final `GameTimePolicy` semantics.

No unresolved material chronology defect was found. The predecessor M02 MAJOR is closed.

## New correction-requiring findings

### W2-CONTENT-WORLD-REM-REV-MIN01 - correction-requiring MINOR - claim prose/schema drift and validation overstatement

The remediation's claim architecture is materially sound, but the exact Markdown and YAML do not fully agree, and the prose overstates one machine invariant.

First, the Markdown states that both contradictory fragmentation accounts remain `UNRESOLVED_AGAINST_WORLD_FACT`. The exact YAML instead assigns both claims `truth_relation: ABOUT_UNKNOWN_BY_DESIGN`. Both values exist in the declared vocabulary, but the packet explicitly says prose cannot override the typed surface. This exact mismatch therefore prevents a clean prose/YAML consistency result.

Second, the Markdown says `INV:CLAIM-REFERENCES-RESOLVE` requires claim, proposition, holder role, branch, and exposure references to resolve within declared vocabulary. The machine invariant actually requires required claim fields to exist and only explicitly requires `holder_ref` to resolve to `provisional_roles` and `proposition_ref` to resolve to `propositions`. Knowledge vocabulary membership is separately constrained by `INV:CLAIM-EXPOSURE-SEPARATE-FROM-TRUTH`; branch vocabulary membership is not explicitly required by the invariant set. The prose therefore describes a stronger validation envelope than the typed packet actually declares.

Severity is MINOR rather than MAJOR because the core M01 architecture remains present and no exact claim currently performs an unauthorized objective-fact promotion. Correction is nevertheless required before clean fan-in because #386 requires zero correction-requiring MINOR findings.

Required bounded correction:
1. choose the semantically intended truth relation for both example accounts and make Markdown/YAML exactly agree;
2. make the machine invariant set and prose agree on validation of claim authority, stance, knowledge, branch scope, and truth-relation vocabulary membership, preferably by strengthening the fail-closed machine validation rather than weakening the reviewed authority boundary;
3. preserve the separate proposition/claim architecture, provisional holder/perspective model, exposure/truth separation, and no-promotion rule.

### W2-CONTENT-WORLD-REM-REV-MIN02 - correction-requiring MINOR - unrelated WR-03 modal weakening

The frozen #366 producer's `WR-03` says resource-relevant world state **must be able to represent** bounded use, regeneration, stewardship, substitution, or access change where materially relevant.

The #382 remediation changes that requirement in both Markdown and YAML to world state **can represent** those dimensions. Neither predecessor M01 nor M02 required weakening this world-rule obligation. The change therefore exceeds the directly necessary correction surface and regresses an otherwise passed producer constraint.

Severity is MINOR because the underlying model is not removed and no downstream implementation is authorized by this packet, but the semantic weakening must be corrected to preserve the immutable producer's passed boundary.

Required bounded correction: restore the producer-strength `must be able to represent` obligation consistently in both Markdown and YAML, without otherwise rewriting world rules.

## Passed attacks and preserved boundaries

Subject to the two correction-requiring findings above, the following attacks are clean in the exact judged packet:

- **Frozen identity/provenance:** PASS. Producer, predecessor review, remediation claim/terminal/head/PR, and three-path surface reconcile.
- **Core fact/claim authority separation:** PASS. Proposition/claim state is distinct from objective/design fact authority.
- **Holder/perspective independence:** PASS. Stable provisional roles and perspective keys do not consume mutable sibling outputs.
- **Exposure/truth separation:** PASS structurally. Knowledge state does not itself determine truth relation or fact authority.
- **Claim-to-fact promotion resistance:** PASS structurally. Exact claim authority and `truth_effect` cannot independently promote objective fact authority.
- **Era completeness:** PASS. All eras are uniquely, contiguously, and explicitly ordered.
- **Event containment:** PASS. Every event resolves to a declared era; present-start/player-entry semantics agree between surfaces.
- **Event precedence:** PASS. Event order is explicit, acyclic, and era-compatible.
- **Topology/causality:** PASS. Reviewed location/edge and upstream/downstream properties are preserved.
- **Sibling independence:** PASS. Cross-domain references remain provisional typed interfaces.
- **Engine neutrality:** PASS. No logical world identity or authority depends on engine/runtime-specific types.
- **Noncanonical boundary:** PASS. The packet remains explicitly noncanonical and does not freeze working labels as canon.
- **Bounded scope:** PASS. No final factions, principal cast, quest/dialogue corpus, exact calendar, runtime schema, or gameplay implementation is introduced.
- **Originality/reference boundary:** PASS within the exact packet. No protected external names, characters, locations, quest lines, dialogue, or expressive structures are adopted as authority.
- **Assumptions/reopen routes:** PASS. Existing assumptions and scoped reopen triggers remain present.
- **WSN evidence discipline:** PASS. `WSN-E1..WSN-E9` are not executed, duplicated, marked PASS/SATISFIED, or replaced by authored content.
- **Authority inflation:** PASS. No engine selection, gameplay/high-throughput implementation, implementation readiness, release, verification-PASS, integration, decision, or canonical authority is claimed.

## Required next route

The exact #382 remediation packet is **not** `CLEAN_FOR_BOUNDED_CONTENT_FANIN` because #386 requires zero correction-requiring MINOR findings.

Route exactly one bounded blocking remediation successor: Issue #389 / `W2-CONTENT-WORLD-REM-02`. Its scope is only `W2-CONTENT-WORLD-REM-REV-MIN01` and `W2-CONTENT-WORLD-REM-REV-MIN02` plus directly necessary consistency edits.

The successor must preserve the structural closure of predecessor M01/M02 and every passed boundary above. After correction, a fresh independent or degraded-independent required review of the exact corrected packet is mandatory before any `CLEAN_FOR_BOUNDED_CONTENT_FANIN` disposition.

## Authority boundary

`CHANGES_NEEDED` grants no content fan-in, integration, verification, decision, readiness, release, engine-selection, empirical WSN-PASS, or canonical authority. The judged remediation remains immutable provenance. Any later publication to `main` remains a separately authorized, squash-only integration decision and does not by itself canonicalize content.