# Issue #74 handoff — W2-MIG-01

**Mission:** `W2-MIG-01`  
**Branch:** `planning/issue-74`  
**Ownership generation:** Issue #74 comment `5262345360`  
**Base main:** `21181eb20302a20d81aaec7b81a84acd4fcbbab8`  
**Evidence report commit before handoff:** `42142282882b580e7283c138974015733012a70a`  
**Evidence report blob:** `700fe468f119cece9c4b060cda93e576de50f468`  
**State intended after terminal capsule:** `REVIEW_READY`  
**Required review:** `W2-REV-01`

## Completed work

Produced `docs/planning/wave-2/evidence/migration-fixture-experiment.md` from the task's bounded authoritative packet.

The retained logical experiment exercises exact save/schema/content tuples across:

- rename and explicit field split;
- semantic unit change;
- field removal with structured loss;
- removed-content tombstoning and retired-ID reuse rejection;
- corrupt-source rejection;
- postcondition failure with copy-on-write rollback;
- retry from the unchanged known-good source;
- exact multi-hop route selection and repeated composition;
- unsupported downgrade without an inverse;
- undeclared target-tuple rejection;
- immutable failed/successful attempt lineage.

A self-review caught an evidence-quality defect in the first draft: several negative cases were constants rather than executable checks. Commit `42142282882b580e7283c138974015733012a70a` replaces them with actual routing/package-policy execution. The final retained harness mechanically produced all 12 expected outcomes.

## Material findings

1. The exercised routing contract needs an exact source tuple, target tuple, and registered path rather than a single save-version integer.
2. Source validation + copy-on-write transform + target validation makes the exercised corruption/postcondition failures fail closed at the logical layer.
3. Semantic loss must be explicit. The fixture records `legacy_hint_seen` removal as irreversible after commit.
4. Removed historical content can retain stable identity/count under a tombstone; target reuse of the retired semantic ID is rejected.
5. A forward migration does not imply a safe inverse; T3→T2 remains explicitly unsupported in this corpus.
6. Later successful retries do not erase prior rejection/rollback attempts.

## Scope limits / open work

This producer result is `BOUNDED_PASS` only for the stated logical fixture contract. It does **not** select a physical persistence encoding, storage transaction mechanism, engine serializer/runtime, canonical semantic hash, real gameplay/content schema, retention policy, user repair UX, or production migration architecture. It does not resolve implementation readiness.

The single reference harness also does not prove cross-runtime migration equivalence or large-save performance. Those claims require their own evidence if later decisions depend on them.

## Checks/evidence

- Authoritative foundation blob: `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`.
- Evidence report blob: `700fe468f119cece9c4b060cda93e576de50f468`.
- Recorded fixture result: `12/12 expected outcomes matched` under Python 3.13.5/Linux.
- No producer artifact was merged to `main`.
- No independent review disposition is claimed by this handoff.

## Next action

After the terminal schema-3 `STATUS(REVIEW_READY)` records the exact final branch/work SHA, freeze this branch as a producer input. `W2-REV-01` must independently critique the migration evidence as part of the complete Wave 2 evidence packet. Do not merge this producer branch to `main` as a substitute for the declared review/verification/canonicalization route.
