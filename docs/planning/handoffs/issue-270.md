# Issue #270 handoff — W2-REM-ACC-08

## Identity

- Mission: `W2-REM-ACC-08`
- Task class: bounded blocking accessibility remediation
- Branch: `planning/issue-270`
- Winning claim: Issue #270 comment `5292959267`
- Claim base: `main@ace13b7c93b037f4cfa9fb98e4f09e267db68440`
- Producer actor/session: `w2-rem-acc-08-gpt56sol-20260814-1347-frontier`
- Trust mode: `DEGRADED_SINGLE_AGENT`

## Routed finding

- Source review: Issue #269 / `W2-REV-ACC-08`
- Terminal review comment: `5292556689`
- Exact review head: `79c3ebe86eaacaedbbee6766a70aadc43845d1f1`
- Exact review work: `50f3cc0ace1f94ebac4130d77c1a7a2066bd03da`
- Disposition: `CHANGES_NEEDED`
- Finding: `W2-REV-ACC08-M01` / MAJOR
- Finding class: omitted current XAG 112 source clauses plus incomplete expected-set oracle

## Immutable inputs

- Integrated v7 policy blob: `4cf9113bc6c4c663db360594e54b5403cc9e5588`
- Integrated v7 report blob: `1a1ec00e6b8143d7f233d58ecc3889d8f7c1550f`
- Logical v6 policy blob: `80e278315d6b7a108d89da3f5a99086a8ef91bf7`
- Canonical Planning Program v1 blob: `e3120ec203c4156328770aa86c12fbb7187966dc`

## Produced packet

- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml`
  - v8 blob: `f1d07ef936f6187529ffc1e84d3fd2f2b4f06b96`
- `docs/planning/wave-2/research/accessibility-current-requirements.md`
  - v8 report blob: `260abddcec26584c62a3bb213ac6e6ea0f90ad0a`
- substantive work boundary: `1a2a97fb5561c3ec9cd1db151db18f104f2040dd`

## Exact bounded correction

The v8 overlay preserves exact v7 as immutable input and adds exactly three XAG 112 atomic identities:

1. `XAG112-SCALED-MAP-NONSCROLLING-NAVIGATION`
2. `XAG112-SUBMENU-PERSISTENT-RETURN-LINK`
3. `XAG112-SAME-INPUT-FOCUS-ESCAPE`

Source semantics are kept bounded:

- scaled/zoomed game-map UI conditionally requires a non-scrolling alternative navigation method; the supplementary text-list example is nonexclusive;
- every applicable submenu has a persistent return link to at least one source-permitted target, main menu or initial interactive screen;
- same-input focus escape is the normal requirement; a clear prompt is required only when escape necessarily uses navigation inconsistent with the rest of the interface.

No pre-existing v7 semantic record is replaced or removed. The reviewed XAG 116 `default_time_limit_exceeds_20_hours` correction remains preserved.

## Mechanical result

- XAG 112 atomic identities: `14`
- XAG 108–123 atomic identities: `113`
- composed XAG 101–123 identities: `218`
- inherited XAG 101–107 identities: `105`
- XAG 116 identities: `4`
- corrected XAG 116 >20-hour exception: `PRESERVED`

Validator v8 rejects omission of any new identity, duplicate/extra records, scaled-map trigger laundering, example-to-requirement inflation, submenu alternative inversion, focus-fallback inversion, conditional-prompt loss, unrelated-v7 redefinition, and regression of the v7 XAG 116 correction.

## Producer self-review

```yaml
unresolved_blocker: 0
unresolved_major: 0
correction_requiring_minor: 0
finding_state: RESOLVED_PENDING_FRESH_REVIEW
```

Producer self-review is not independent acceptance.

## Preserved fail-closed state

```yaml
empirical_accessibility_evidence: NOT_RUN
mapping_complete: false
IR-BLOCKER-ACCESSIBILITY-CURRENT: OPEN
W2-REV-M02: OPEN_BOUNDED
full_xag_108_123_review_complete: false
production_implementation_ready: false
legal_compliance_claimed: false
platform_certification_claimed: false
verification_pass_authority: false
integration_authorized: false
canonicality: NOT_CANONICAL
```

Issue #269 terminated negatively after the XAG 112 defect and did not accept untouched XAG 113–123. This remediation does not upgrade that historical result.

## Required next

1. Open and bind an exact-head draft PR for this producer packet.
2. Publish terminal schema-3 `STATUS(REVIEW_READY)` with exact policy/report/handoff blobs and PR head.
3. Perform one fresh independent/degraded-independent review of this exact remediation before any producer integration eligibility.
4. Even after a clean bounded remediation review, complete the required corrected XAG 108–123 review for the untouched XAG 113–123 scope before routing empirical accessibility evidence.

Any eventual integration is separate, repository-authorized, and squash-only. This packet grants no accessibility PASS, readiness, implementation, release, legal/compliance, platform certification, verification-PASS, decision, integration, or canonical authority.
