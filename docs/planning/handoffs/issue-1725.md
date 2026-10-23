# Issue #1725 — independent existing PR security review handoff

## State and provenance
Mandatory genuinely distinct security review of Issue #1718 source OPEN/DRAFT PR #1723 exact HEAD `186bb42292d2cb43c6c623073e4929e576a90e50`. First winning claim #6132616875 by `existing-pr-independent-semantic-sha-review-1725-gpt6-20261012-cph-01`, derived from main `a57436d194f14f5f2c5b1173a9c2e0ec6468ee7c`, canonical #1147 binding #5675066392 and program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`. Source owner terminal #6131910505 authenticated exact head and in-lease publication; hosted authored run #38303093661 SUCCESS with mutating job SKIPPED.

## Independent result — CHANGES_NEEDED
**1 MAJOR FSR-1725-M01** in `v4.semantic_generation_from_terminal`: semantic `route_consumed: true` authenticates *wrapper* SHA earlier but accepts *successor terminal* using `base.reconcilable_terminal` parser and comment ID only, without checking successor branch HEAD/work against live ref. Independently ran the exact extracted function body in Python 3 with mocked imports: a successor terminal carrying unrelated SHA40 fields is accepted as generation `(10, 2, NEXT)`; SHA verifier never called for that successor. Full module and real API mocks **not independently executed**, so no false clean claim. See `docs/planning/wave-2/reviews/factory-seeding-1718-review.md` for exact chain, fixture, evidence and scope limits.

## Allowed output and next route
New review report plus this new handoff only, reviewer-only draft PR before terminal status and **never integrate reviewer-only PR**. One bounded source remediation must correct successor-terminal SHA authentication; preserve reviewed source and marker-only dispatch semantics; run full independent composed modules and separate adversarial security review before any separately authorized squash-only noncanonical source publication. No source edits, live --apply/PATCH or GitHub PR closure, main changes, canon or production authority.
