# Issue #73 handoff — W2-HASH-01

**Mission:** `W2-HASH-01`  
**Branch:** `planning/issue-73`  
**Ownership generation:** Issue #73 comment `5256845092`  
**Base main:** `e4b7ee0a2699a57216146e99b990ab64edaae1d1`  
**Evidence report commit:** `a88dda35df9d84ae82f8ea0219d5bb86c7eda1d4`  
**State intended after terminal capsule:** `REVIEW_READY`  
**Required review:** `W2-REV-01`

## Completed work

Produced `docs/planning/wave-2/evidence/canonical-hash-conformance.md` for candidate encoding `ef-sem-1` and ran a shared adversarial conformance corpus through independently written Python 3.13.5 and Node 22.16.0 adapters.

Final corpus: 29 cases, 18 accepted and 11 rejected. Final Python/Node result objects agree on every accepted canonical byte/hash result and every rejection class. The bounded experiment result is **PASS** for `ef-sem-1`-conforming semantic values only.

Retained evidence identities:

- corpus: `527a5b70cf04ef5fef1ec3247c42364fe766792d0525105e62510656681aa2b7`;
- Python adapter: `2b3619343d1d3a70da27070414f013c51392e4031224a455f81bb87a5bad3902`;
- Node adapter: `791479f5a8d004da4dd6c111e05e89917ac87b840ff8dc02be7e6f6c0a3a89dc`;
- Python final run: `cf643bf2e5e76d27b3e29016954c04135477d7e0d6c3aa241ee5a5d765657f61`;
- Node final run: `48ac0a2f952c178d2099f426c0669bd74f0ddf654f5121565b610ba4096a4e20`.

## Material findings retained

1. Native UTF-8 behavior diverged for an unpaired surrogate: Python rejected while naive Node replacement-encoded. The candidate now requires Unicode-scalar validation before UTF-8; both adapters reject the retained case as `NON_SCALAR_STRING`.
2. A JavaScript falsy-default implementation would have accepted an explicitly empty schema version. Presence-based defaulting corrected it; both adapters reject as `SCHEMA_VERSION`.

## Scope limits / open work

This does not authorize local/native serializer hashes, floats or other untested semantic types, implicit Unicode normalization, production schema/content-package hashing, migration equivalence, persistence encoding, engine selection, or production implementation readiness.

Reopen/version on any new-runtime mismatch, semantic normalization requirement, new authoritative value type/range, schema/content identity rule change, hash-scope/algorithm change, reference identity change, or retained-evidence integrity loss.

## Next action

Freeze this branch after the terminal schema-3 `STATUS(REVIEW_READY)` records the exact final branch/work SHA. `W2-REV-01` must independently critique this evidence before downstream authority is widened. Do not merge this producer branch to `main` as a substitute for the declared review/canonicalization route.