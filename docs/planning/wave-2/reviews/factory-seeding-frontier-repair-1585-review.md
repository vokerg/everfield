# Required adversarial review — #1585 real integration alias remediation

## Scope and frozen source

Review issue: #1589 `FACTORY-SEEDING-FRONTIER-REPAIR-01-REM-03-REV-01`.

Reviewed producer: #1585 terminal `6034246625`, draft PR #1586, exact frozen HEAD `d7679724712af7e97f2928d7f0075036338c18d9`.

Current compatible main during review: `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. Active canonical binding remains #1147 comment `5675066392`, Planning Program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

The frozen source still contains exactly eight paths and the required immutable inherited blobs. The substantive v7 blob is `87433873ecf63865587bc47381b1c6c97668833b`. The single intervening main commit after the source PR base is the disjoint #1587 two-document review-provenance squash; it does not overlap the eight source paths.

## Evidence independently inspected

- Full PR #1586 eight-path patch and exact changed-file blob identities.
- Frozen v7 implementation, including `_integration_field`, `_extension_field`, `_consistent_extension_alias`, `_valid_owner_terminal`, `_exact_causal_source_review`, `_integration_provenance`, `_real_squash_main_sha`, and integration-demand selection.
- Actual GitHub Actions run `37595095259` / `validate-pr` job `112705675889`: checkout was merge ref `d179ef35a7f62ee57d3cfd7fe636c523608f412f`, explicitly `d7679724712af7e97f2928d7f0075036338c18d9` merged into `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. Python compile and composed v1-v7 self-tests all reported PASS. Mutation-capable job `112705677975` was SKIPPED.
- Genuine published source chain for #1583: terminal `6009230681`, original source #1545 / PR #1568 / HEAD `1de1155429bfa657dd6e60c4f5abc969fabd86d5`; recovered source owner chain `5999915299 -> 6008439626 -> 6008441599 -> 6008457546`; required verifier #1575 terminal `6008823087`; required review #1577 terminal `6009157969`; one-parent source squash `ef75cc78a217695097f5d8f6cfb48ea04beaa7de` from `e51703de82b9df3f5e676663d3a04fdc678bd5c6`.
- Source PR #1568 exact six changed blobs and reviewer PR #1582 exact two documentation blobs. The real #1575 verifier is a distinct frozen-head Godot verification episode with PASS evidence; its existence is not in dispute.

Passing authored CI is evidence about the candidate, not a substitute for this review.

## Findings

### FSR-1589-B01 — BLOCKER — required independent verification is not authenticated before implementation-source authority is accepted

The corrected v7 successfully repairs the specific #1581 alias mismatch: `_consistent_extension_alias` recognizes `original_source_issue` / `original_source_pr_number` and newer aliases, and the causal path still authenticates producer ownership, source PR/head, distinct clean review, and the real one-parent squash.

However, the integration acceptance path never validates the independently required verifier.

`_exact_causal_source_review` authenticates:
- source producer issue/terminal/owner;
- source PR and frozen source HEAD;
- distinct required review issue/terminal/owner;
- clean review disposition and zero material findings;
- source/review PR identities and path surfaces.

It does **not** read or validate the top-level `verification_status_comment_id`, nor the #1583 extension fields `independent_verifier_issue`, `independent_verifier_terminal_comment_id`, verifier PR/head, verifier run, or verifier artifact. `_integration_provenance` likewise requires source and review terminal IDs but no verification identity. A search of the frozen v7 source contains no verifier-authentication path.

That means an otherwise identical trusted integration capsule can omit, dangle, or forge the independent verifier provenance and still proceed through the producer/review/PR/squash gates. The authored self-tests do not include a negative verifier-absence/forgery case.

This is a false-authority defect, not a documentation omission. Source #1545's terminal route explicitly required #1575 independent exact-head verification before review and publication; real #1583 records verifier terminal `6008823087`; #1589's mandatory review contract requires the real #1583 chain to be accepted only when that independent verification is genuine. Allowing downstream implementation-demand seeding without authenticating that gate bypasses required verification.

**Required correction:** bind the integration to a distinct trusted closed verifier issue and exact immutable `VERIFICATION_STATUS` terminal, validate its ownership/actor independence, source issue/terminal/PR/head association, PASS/disposition and zero blocking/correction findings, verifier-only PR/head/path scope, and any exact evidence fields the canonical source contract requires. Missing, edited, dangling, foreign, conflicting, or source/reviewer-substituted verifier evidence must fail closed. Add positive real-#1575/#1583 coverage and negative absent/dangling/edited/wrong-source/wrong-head/wrong-actor/wrong-PR/non-PASS verifier fixtures.

### FSR-1589-M01 — MAJOR — contradictory recognized aliases outside `extensions` are ignored rather than rejected

The task explicitly requires disagreement/duplication and foreign top-level-or-extension provenance fields to fail closed.

The new `_consistent_extension_alias` only scans the two-space fields inside the sole `extensions:` section. `_integration_field` separately scans top-level authority fields, but the integration schema does not require or reject top-level `original_source_issue`, `source_producer_issue`, `original_source_pr_number`, or the related alias vocabulary.

Therefore a capsule containing, for example, a contradictory top-level `original_source_issue: 9999` plus `extensions.original_source_issue: 1545` resolves the extension alias to `1545`; the contradictory recognized top-level provenance field is not part of the alias conflict test and is not otherwise rejected. The same placement ambiguity applies to the recognized source PR alias family. Existing self-tests exercise conflicts and duplicates inside `extensions`, but not foreign or contradictory recognized aliases at top level.

This does not by itself confer authority because the extension value still flows through the deeper source/review/PR/squash gates, so it is lower severity than B01. It nevertheless violates the explicit fail-closed parser contract and leaves ambiguous provenance accepted by an authority-sensitive parser.

**Required correction:** define allowed placement/schema for the recognized provenance aliases and reject those keys when present outside their permitted section; reject duplicate/foreign aliases across top-level and extensions, not only duplicates within extensions. Add adversarial top-level/extension cross-placement conflict, duplicate, null and foreign-key fixtures.

## Other reviewed behavior

No additional material defect was found in the inspected bounded areas:

- The historical `original_source_issue` / `original_source_pr_number` vocabulary is now recognized when correctly placed and agreement among multiple recognized extension aliases is enforced.
- Producer/reviewer identities remain independently resolved rather than trusted from scalar aliases alone.
- Canonical six-hour first-owner / STALE recovery reconstruction is materially stronger than the rejected predecessors and covers winning intent, maturity, source anchor, observed head and later competing ownership.
- Source publication validation binds an actual merged PR, exact source HEAD, one-parent squash and exact published file blob/status identity.
- Latest implementation source selection uses verified squash ancestry rather than issue number, and consumed-latest does not backfill older history.
- v5/v6 inherited surfaces and workflow blob remain the expected frozen blobs.
- Pull-request CI is read-only and mutation-capable maintenance is excluded from pull-request runs.

These points do not waive B01 or M01.

## Disposition

**CHANGES_NEEDED.**

Finding counts:
- BLOCKER: **1**
- MAJOR: **1**
- correction-requiring MINOR: **0**

The source PR #1586 must remain unmerged. This reviewer has no authority to modify the source or publish it. Required next route is bounded blocking remediation of FSR-1589-B01 and FSR-1589-M01 on a new producer generation, followed by fresh exact-head read-only CI and a new distinct required adversarial review. Only a later clean required-review terminal may unlock a separately owner-authorized, current-main-compatible, expected-head, squash-only **NONCANONICAL** publication.

No canonical, gameplay, truth, consent, persistence, accessibility, implementation-readiness, production, legal, shipping, or release authority is granted by this review.
