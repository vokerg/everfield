# W2-CONTENT-CHAR-REM-01 — relationship-history and information-control remediation

**Issue:** #409  
**State:** REMEDIATION CANDIDATE / NONCANONICAL  
**Conflict domain:** `CONTENT_CHARACTER`  
**Required next gate:** fresh independent/degraded-independent required character-root review

## 1. Binding and composition

This is the bounded successor required by Issue #407 / `W2-CONTENT-CHAR-REV-01`. It closes only `W2-CONTENT-CHAR-REV-M01` and `W2-CONTENT-CHAR-REV-M02`; it grants no fan-in, integration, verification, readiness, release, decision, gameplay implementation, engine-selection, or canonical authority.

Claim base is `main@5121f352477a08718e6a39d97086b336d2a68a11`. Canonical Planning Program v1 remains blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`. Owner directives are `5277825639` and `5305563203`.

The frozen producer is Issue #368: original claim `5305676233`, recovery claim `5306622605`, terminal `5306628907`, work `3d1cc79dcd6a2179887aab7df967417201627bad`, head `215e2647382caf31171889452f1e44e56533f996`, PR #383, Markdown blob `f4f481f7f6cdbe1edd09bb436ea20fe606a99fab`, YAML blob `97dc6977b0fade501f328302dc7dc6fa12bab42a`.

The frozen required review is Issue #407: claim `5306640676`, terminal `5306658515`, review work `d00488a78a7c09dc9e58b0d280c1e1f39920527b`, head `4afdc3d111a12f562b31cfe84dc1d136f132a726`, PR #408, disposition `CHANGES_NEEDED`. That review provenance is already squash-published noncanonically at the claim-base `main`.

The YAML successor is a deterministic overlay on the exact frozen #368 YAML blob. Composition is `PATCH_EXISTING_COLLECTIONS_BY_STABLE_ID`: `relationship_event_patches` key by `event_id`, `information_record_patches` key by `info_id`, and every unmentioned base field is preserved byte-derived from the frozen blob. Composition fails closed if the base blob or expected collection counts do not match. Neither predecessor branch is mutated.

## 2. M01 — durable relationship-history semantics

All four existing `REL_EVT:*` records now have a mechanically required shape for:

- typed cause and bounded character-domain detail;
- resulting relationship-dimension/history flags;
- who knows the event, player-visibility state, and nonparticipant disclosure rule;
- whether repair is possible and its mode, with repair forbidden from erasing history;
- evidence class that may justify later current-dimension change, while the event remains durable.

The four existing histories remain: Anwen/Selka uncertainty-method disagreement; Jori/Maelin unasked support and perceived obligation; Jori/Oren joint attempt with contested method/risk; Maelin/Selka burden objection despite procedural validity. No new world, faction, narrative, or current relationship fact is inferred from these records.

## 3. M02 — uniform information-control semantics

One `INFO_CONTROL_V1` contract now applies to all five existing `INFO:*` records. For every record:

- `current_holders` must equal the producer `known_by` set;
- every current holder has explicit acquisition provenance with holder, mode, source scope, and source authority;
- access is default-deny and may arise only through `EXPLICIT_HOLDER_DISCLOSURE` or later `VALIDATED_AUTHORITY_EFFECT`;
- relationship state, shared provisional role, generated content, or player-visible content cannot grant character access;
- player exposure is separately represented and defaults to `NOT_ASSERTED`; it grants neither character knowledge nor objective truth;
- BELIEF/testimony and provisional interfaces cannot promote objective truth.

Acquisition is explicit without inventing sibling canon: Anwen uses direct inspection of this record's provenance analysis; Tomas and Oren hold their BELIEF records by self-inference with `BELIEF_ONLY` authority; Selka uses first-person memory of her own candidate decision; Jori uses self-knowledge of his own interpretation and Maelin retains the producer's explicit disclosure from Jori.

## 4. Preserved regression surface

The exact six character IDs, eight relationship IDs/current qualitative dimensions, four event IDs, five information IDs and their authority/truth/holder sets, six change-arc IDs, provisional sibling interfaces, anti-grind rules, progression-gate discipline, generation/canon rules, originality boundary, and evidence debt remain unchanged outside M01/M02.

The remediation consumes no mutable sibling output, creates no foundational relationship gate, creates no universal affection scalar, and does not turn BELIEF, SECRET, testimony, generated prose, player exposure, relationship state, or provisional interfaces into objective truth or knowledge authority. All WSN evidence remains `UNRUN_REQUIRED_EVIDENCE`.

## 5. Self-review and next gate

Mechanical checks require exact base blob identity, 6 characters, 8 relationships, 4 relationship events, 5 information records, and 6 change arcs; every event must satisfy the full M01 contract; every information holder must have acquisition provenance; all information access must remain default-deny; and no WSN PASS or stronger authority may appear.

Self-review disposition: `SELF_REVIEW_CLEAN_PENDING_FRESH_REQUIRED_REVIEW`.

- `W2-CONTENT-CHAR-REV-M01`: `REMEDIATED_PENDING_FRESH_REVIEW`.
- `W2-CONTENT-CHAR-REV-M02`: `REMEDIATED_PENDING_FRESH_REVIEW`.

A fresh required review of the exact composed packet is mandatory. Only `CLEAN_FOR_BOUNDED_CONTENT_FANIN` with no unresolved correction-requiring finding may satisfy the character-root prerequisite for `W2-CONTENT-SYN-01`. Any later publication is separately authorized, squash-only, and noncanonical unless separate canonicalization authority exists.
