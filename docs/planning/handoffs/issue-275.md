# Issue #275 handoff — W2-REM-ACC-09

## Identity

- mission: `W2-REM-ACC-09`
- issue: #275
- winning claim: `5293060848`
- actor/session: `w2-rem-acc-09-gpt56sol-20260814-1403-frontier`
- branch: `planning/issue-275`
- claim base: `main@3f06e40020201493eaed138394889a6f7f09fda7`
- substantive work head before handoff: `29e6ecf627d36c0bf718ac3bc7512e1b7adfb02d`

## Routing provenance

- required scoped review: Issue #273 / `W2-REV-ACC-09`
- review terminal comment: `5293049701`
- review exact head: `ff66673fa36bae8a190a2bd3205f3059e2fb1b67`
- review exact work: `791a3991c135a4a2d842f86242a88eaeda172a26`
- review disposition: `CHANGES_NEEDED`
- routed finding: `W2-REV-ACC09-M01` / MAJOR / `SOURCE_QUANTIFIER_WEAKENING_AND_INCOMPLETE_VALIDATOR_ORACLE`
- prior producer: Issue #270 / `W2-REM-ACC-08`
- prior producer terminal comment: `5292997562`
- prior producer exact head: `284b9b2723f07f828202f3ce053d7eaae51e7e89`
- immutable policy v8 blob: `f1d07ef936f6187529ffc1e84d3fd2f2b4f06b96`
- immutable report v8 blob: `260abddcec26584c62a3bb213ac6e6ea0f90ad0a`
- canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

## Produced artifacts

- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`
  - v9 blob: `5cf18195bdfcb377aac7727b65b2d8a479ef8ac3`
- `docs/planning/wave-2/research/accessibility-current-requirements.md`
  - v9 report blob: `3665805bb6391bc0c7b6b27ca2f70b7f0b88aaae`
- this handoff

## Bounded correction

The v9 overlay consumes exact v8 and corrects only `XAG112-SUBMENU-PERSISTENT-RETURN-LINK` so that the source requirement is mechanically universal over the applicable submenu collection.

The corrected contract requires, for **every applicable submenu**, at least one persistent return path to either `main_menu_screen` or `initial_interactive_screen`. Those targets remain alternatives; both are not simultaneously required. If no applicable submenus exist, the clause is `NOT_APPLICABLE` rather than a positive coverage claim.

The mechanical validator includes a load-bearing multi-submenu fixture in which one submenu has a valid path and another has none; that candidate is required to reject with `REJECT_UNIVERSAL_COVERAGE_FAILURE`. It also includes a one-submenu fixture using only `initial_interactive_screen` to prove alternative-target semantics remain intact.

## Preservation / self-review

Bounded producer self-review: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

Preserved from exact v8:

- XAG 112 identity count: `14`
- XAG 108–123 identity count: `113`
- composed XAG 101–123 identity count: `218`
- inherited XAG 101–107 identity count: `105`
- `XAG112-SCALED-MAP-NONSCROLLING-NAVIGATION`: unchanged v8 semantics
- `XAG112-SAME-INPUT-FOCUS-ESCAPE`: unchanged v8 semantics
- XAG 116 default-over-20-hours correction: preserved
- no unrelated v8 semantic record redefined

Fail-closed state remains:

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
untouched_xag_113_123_accepted: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #269's negative early termination still did not accept untouched XAG 113–123. This bounded remediation does not substitute for the later fresh full corrected XAG 108–123 review.

## Required next gate

Freeze the task at the exact post-handoff branch head and exact-head draft PR, then perform a **fresh independent/degraded-independent scoped review** of this exact v9 packet. Producer self-review cannot satisfy that gate.

Until a clean fresh review exists, this producer packet is not integration-eligible. Even a clean bounded review would grant only eligibility for separately authorized squash-only noncanonical integration; it would not grant empirical accessibility PASS, full corrected-mapping acceptance, readiness, implementation, release, legal/compliance, platform certification, verification-PASS, decision, or canonical authority.
