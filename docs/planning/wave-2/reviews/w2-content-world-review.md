# Issue #378 required review - W2-CONTENT-WORLD-REV-01

## Disposition

`CHANGES_NEEDED`

Trust mode: `DEGRADED_SINGLE_AGENT`.

Finding count: **0 BLOCKER / 2 MAJOR / 0 MINOR**.

This is the mandatory fresh content-root review of exact producer Issue #366 / `W2-CONTENT-WORLD-01`. It judges the frozen producer packet only. It does not edit the producer branch, author replacement world content, grant fan-in authority, integrate anything, or make any content canonical.

## Frozen judged identity

- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- canonical binding: Issue #6 comment `5245368879`
- canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- current review base main: `dd84256de5033cb9873eb10589847be1d403b042`
- content-frontier compiler work: `fd2fb7d816cf23d60bcc54bd25c7d9a4eaae3dbb`
- activation review Issue #372 terminal: `5305598079`
- activation review head: `656930c36d90a166776485cbaf196c39a32fe97e`
- producer Issue #366 winning claim: `5305649840`
- producer Issue #366 terminal status: `5305661660`
- producer substantive work: `8dc85721e446727f4b2eb59b0c35bd98edb53f20`
- producer exact terminal head: `6f77a245e4905d33448f6dc7e0d898f6e4db3d43`
- producer draft PR: #377, exact head `6f77a245e4905d33448f6dc7e0d898f6e4db3d43`, base `main@dd84256de5033cb9873eb10589847be1d403b042`
- producer changed paths: exactly the world foundation prose, world facts YAML, and Issue #366 handoff

The producer packet was frozen before substantive review. No CI/check status existed on the exact producer head; this planning review therefore relies on exact packet inspection and contract reconciliation rather than treating absent checks as evidence.

## Review scope and attacks

The review reconciled the exact producer contract, producer diff, current Wave 1 canonical foundation, content-frontier map, and the sibling root contracts for social, character, and narrative work. It attacked:

- frozen identity and ownership surface;
- internal topology and causal consistency;
- chronology and machine-checkability;
- fact authority, knowledge, belief, secret, dispute, unknown, and branch boundaries;
- sibling-output independence and provisional cross-domain interfaces;
- accidental canon inflation;
- originality/reference leakage;
- boundedness and scope expansion;
- relevant game/system interfaces;
- hidden engine coupling;
- WSN evidence duplication or laundering;
- machine-readable integrity;
- authority inflation.

## Findings

### W2-CONTENT-WORLD-REV-M01 - MAJOR - Belief and in-world claim state is not representable in the typed surface

Issue #366 explicitly requires an `objective fact vs belief/secret/disputed/branch-specific` distinction. The prose also states that a map, inscription, rumor, testimony, tradition, or NPC statement may be evidence or belief without becoming objective truth, and that downstream content must bind such claims to the appropriate fact/knowledge scope.

The machine-readable vocabulary does not provide a belief or in-world claim representation. Its authority classes are limited to `CANDIDATE_OBJECTIVE`, `CANDIDATE_CONSTRAINT`, `DISPUTED_IN_WORLD`, `UNKNOWN_BY_DESIGN`, and `PROVISIONAL_INTERFACE`. Its knowledge states are `PUBLIC`, `DISCOVERABLE`, `SECRET`, `SYSTEM_ONLY`, and `NOT_APPLICABLE`.

Those dimensions cannot encode an actor or source holding a proposition that may be false, incomplete, perspective-bound, or even unanimously believed without being objective truth. `DISPUTED_IN_WORLD` is not a substitute: a belief may be undisputed and still false or merely unverified, and a dispute requires multiple claims whose holders and propositions remain distinguishable. `SECRET` is exposure state, not epistemic truth status.

This is material because the companion YAML is declared to be the checkable identity/fact/chronology surface and the prose says it cannot override that surface. Leaving belief and claim semantics prose-only forces later character/narrative/fan-in work either to invent a second incompatible representation or to overload objective/disputed authority classes, creating exactly the fact/knowledge leakage the contract requires this root to prevent.

Required bounded correction:

1. Add an explicit typed in-world claim/belief interface separate from objective fact authority.
2. Bind each such claim to a stable claim identity and enough source/holder/perspective identity to distinguish who asserts or believes what.
3. Bind the proposition to an exact fact/proposition reference or another explicit bounded representation without requiring concrete mutable sibling character/faction outputs.
4. Make truth/authority independent from exposure (`PUBLIC`, `SECRET`, etc.).
5. Add a checkable invariant or equivalent fail-closed rule proving an in-world claim or belief cannot become `CANDIDATE_OBJECTIVE` merely because prose states it.
6. Keep this correction at world-interface level; do not expand the remediation into a full character belief system.

### W2-CONTENT-WORLD-REV-M02 - MAJOR - The machine chronology does not encode the prose era ordering it claims to make checkable

The prose presents a relative history ordered as `ERA:PRE-WORKS`, `ERA:WORKS-BUILDOUT`, then `ERA:PATCHWORK-PRESENT`, with buildout and fragmentation events inside the works era and present-start/player-entry events inside the present era.

The YAML declares all three eras and event-to-era memberships, but `chronology.precedes` contains only:

- `ERA:PRE-WORKS -> EVT:WORKS-BUILDOUT`
- `EVT:WORKS-BUILDOUT -> EVT:WORKS-FRAGMENTATION`
- `EVT:WORKS-FRAGMENTATION -> EVT:PATCHWORK-PRESENT-START`
- `EVT:PATCHWORK-PRESENT-START -> EVT:PLAYER-ENTRY`

It never orders `ERA:WORKS-BUILDOUT` or `ERA:PATCHWORK-PRESENT` themselves. The sole chronology invariant, `INV:CHRONOLOGY-ACYCLIC`, only requires the `precedes` graph to be acyclic. An acyclic but underconstrained graph can therefore pass while era ordering or event containment conflicts with the prose.

This violates the producer contract requirement that chronology and world invariants be internally checkable rather than prose-only. It is material at fan-in because narrative events could be inserted with inconsistent era relationships while the current invariant still reports success.

Required bounded correction:

1. Encode explicit relative era ordering or interval/containment semantics for all declared eras.
2. Define how event `era` membership interacts with that ordering.
3. Strengthen the machine invariant set so the declared prose sequence and event containment are mechanically checkable, not inferred from YAML list order or labels.
4. Preserve relative chronology. Exact dates, day lengths, season lengths, and final `GameTimePolicy` mapping remain downstream and are not required to close this finding.

## Passed attacks

The following review attacks found no unresolved material defect in the bounded producer scope:

- **Frozen identity:** PASS. Producer claim, terminal status, work SHA, head SHA, PR base/head, and three-path change surface reconcile.
- **Topology/internal causality:** PASS. Stable location IDs, core triangle, directed upstream/downstream relation, old-works cross-zone relation, and outer-threshold reachability are coherently represented.
- **Sibling independence:** PASS. Cross-domain references remain provisional role interfaces; no mutable social, character, or narrative output is consumed.
- **Engine neutrality:** PASS. Logical identities and world facts do not depend on engine scenes, assets, editor objects, components, or runtime-specific types.
- **Canon boundary:** PASS. The packet consistently marks itself noncanonical and does not promote working labels or candidate facts to project canon.
- **Scope/boundedness:** PASS. No final factions, principal cast, plot/quest catalog, dialogue corpus, implementation schema, or gameplay implementation was smuggled into the root.
- **Originality boundary:** PASS within the judged packet. The proposal uses generic functional design vocabulary and explicitly rejects importing protected names, characters, locations, quest lines, dialogue, or copied expressive structure.
- **Assumptions/reopen routes:** PASS. Material world assumptions and concrete downstream reopen triggers are explicit.
- **WSN evidence discipline:** PASS. `WSN-E1..WSN-E9` remain on existing evidence routes; no prose or typed fact is represented as empirical PASS/SATISFIED, and no duplicate WSN experiment is created.
- **Authority inflation:** PASS. No engine selection, gameplay/high-throughput implementation, implementation readiness, release, verification-PASS, decision, integration, or canonical authority is claimed.

## Required next route

The exact producer packet is not clean for `W2-CONTENT-SYN-01` fan-in. Route **exactly one bounded remediation successor** that preserves the frozen Issue #366 producer provenance and corrects only the material finding set above plus any directly necessary consistency edits.

The remediation must not mutate `planning/issue-366` or rewrite its terminal history. It may produce a fresh successor candidate on its own branch and must preserve all passed boundaries, especially engine neutrality, sibling independence, noncanonicality, bounded scope, originality discipline, and unchanged WSN evidence status.

After remediation, a fresh independent or degraded-independent required review of the exact remediated packet is mandatory. The remediation cannot self-review itself into fan-in authority.

## Authority boundary

Disposition `CHANGES_NEEDED` grants no fan-in authority and no integration authority. This review is noncanonical review provenance only. It does not select an engine, authorize gameplay/high-throughput implementation, establish readiness/release/verification PASS, settle WSN evidence, make world content canonical, or create decision authority. Any later integration into `main` remains separately authorized and squash-only.