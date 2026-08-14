# W2-REM-ACC-11 — restore the XAG 114 title exception

**Mission:** `W2-REM-ACC-11` / Issue #282  
**Winning claim:** comment `5293260434`  
**Claim base:** `main@89d6fab07dae08bb34a85fe41354050144a0d3a9`  
**Required full review:** Issue #281 winning claim `5293197877`, terminal `CHANGES_NEEDED` comment `5293245321`, review head `08fee5742c95935d45fc85ab536ea56223923be0`, work `9efd4fac68c96a28d63a1ee7fdbc3592ae2aba8a`  
**Finding:** `W2-REV-ACC11-M01` / MAJOR — `SOURCE_EXCEPTION_OMISSION_AND_VALIDATOR_INCOMPLETENESS`  
**Immutable producer input:** policy v9 blob `5cf18195bdfcb377aac7727b65b2d8a479ef8ac3`, report v9 blob `3665805bb6391bc0c7b6b27ca2f70b7f0b88aaae`  
**Authority:** bounded noncanonical remediation only; fresh independent/degraded-independent scoped review remains mandatory.

## 1. Scope

Issue #281 performed the required fresh full corrected XAG 108–123 review but terminated early on the first reproducible material defect. The inherited record `XAG114-CRITICAL-TEXT-READING-LEVEL` preserved two exceptions—narrative/story text and proper names—but omitted the source-qualified **titles** exception. The inherited validator likewise had no load-bearing rejection fixture for that omission.

This remediation consumes exact v9 as immutable input and changes only that exception set plus the minimum mechanical validator/report metadata needed to make the omission rejectable. It adds, removes, splits, or renames no XAG identity and does not accept the remainder of XAG 114 or XAG 115–123.

## 2. Fresh source reconstruction

The current first-party Microsoft XAG 114 (`UI context`, XAG v3.2, page last updated 2026-03-04; re-observed 2026-08-14) retains the reading-level guidance for UI text critical to gameplay understanding or settings management and expressly excludes narrative/story material and proper names **or titles** from that guidance.

The corrected atomic record therefore keeps the existing trigger and lower-secondary threshold unchanged and makes the exception set explicit:

```yaml
exceptions:
  - narrative_or_story_text
  - proper_names
  - titles
```

`titles` remains a source-qualified exception. It is not generalized into all labels, all UI text, or unrelated proper nouns, and it is not converted into trigger or requirement semantics.

## 3. Mechanical correction

`ACCESSIBILITY-POLICY-VALIDATOR-v10` resolves exact v9 through the inherited XAG 108–123 lineage and requires the final `XAG114-CRITICAL-TEXT-READING-LEVEL` exception set to include all three source-qualified classes.

The load-bearing fixtures are:

1. narrative/story text + proper names + titles → **PASS**;
2. the same record with `titles` omitted → **REJECT_EXCEPTION_SET_MISMATCH**;
3. the complete exception set plus invented `all_ui_labels` → **REJECT_EXCEPTION_SCOPE_INFLATION**.

The validator also rejects changes to the reading-level trigger, seven-to-nine-school-year reference, evidence/gap routing, any unrelated v9-composed record, or the reviewed XAG 112/XAG 116 corrections.

## 4. Preservation proof

The identity/count contract is unchanged:

- XAG 114: **16** atomic records;
- XAG 112: **14** atomic records;
- XAG 108–123: **113** atomic records;
- inherited XAG 101–107: **105** atomic records;
- composed XAG 101–123: **218** atomic records.

The following prior corrections remain immutable composition inputs:

- XAG 116 default-over-20-hours exception;
- XAG 112 scaled/zoomed-map non-scrolling alternative navigation;
- XAG 112 universal return navigation on every applicable submenu with main-menu / initial-interactive-screen alternatives;
- XAG 112 same-input focus escape with the source-conditional prompt fallback.

No evidence or gap route changes. No unrelated XAG 108–123 record changes.

## 5. Finding disposition and bounded self-review

`W2-REV-ACC11-M01` is **RESOLVED_PENDING_FRESH_SCOPED_REVIEW** in this producer packet:

- `titles` explicitly represented as an XAG 114 reading-level exception: **YES**;
- omission of `titles` mechanically rejected: **YES**;
- exception generalized beyond the source: **NO**;
- trigger or reading-level threshold changed: **NO**;
- identity/count changed: **NO**;
- XAG 112 reviewed corrections changed: **NO**;
- XAG 116 reviewed correction changed: **NO**;
- unrelated v9 semantics changed: **NO**;
- empirical accessibility PASS claimed: **NO**;
- full corrected XAG 108–123 review claimed complete: **NO**.

Bounded producer self-review finds **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR** in this remediation scope. Producer self-review is provenance only and does not satisfy the required fresh independent scoped review.

## 6. Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
xag_114_remainder_accepted: false
untouched_xag_115_123_accepted: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #281's early-negative boundary remains authoritative. This bounded repair does not resume or complete its unreviewed remainder and does not make an empirical accessibility successor eligible.

## 7. Required next transition

Freeze this remediation at an exact terminal head with an exact-head draft PR, then perform a fresh independent/degraded-independent scoped review of this exact v10 correction.

If that bounded review is clean, the producer packet may become eligible for separately authorized squash-only noncanonical integration. After any such integration, a fresh full corrected XAG 108–123 review must resume/restart across the still-unaccepted remainder before empirical accessibility evidence work can become eligible.
