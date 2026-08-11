# Issue #73 handoff — W2-HASH-01

**Mission:** `W2-HASH-01`  
**Branch:** `planning/issue-73`  
**Ownership generation:** Issue #73 comment `5256845092`  
**Base main:** `e4b7ee0a2699a57216146e99b990ab64edaae1d1`  
**Evidence report commit:** `897e938fa5dc45aae8527f15e11be97b8df1d848`  
**State intended after terminal capsule:** `REVIEW_READY`  
**Required review:** `W2-REV-01`

## Completed work

Produced `docs/planning/wave-2/evidence/canonical-hash-conformance.md` for candidate encoding `ef-sem-1` and ran a shared adversarial conformance corpus through independently written Python 3.13.5 and Node 22.16.0 adapters.

Final retained corpus: 32 cases, 18 accepted and 14 rejected. Final Python/Node result objects agree on every accepted canonical byte/hash result and every rejection class. The bounded experiment result is **PASS** for `ef-sem-1`-conforming semantic values only.

Retained/reproducible evidence identities:

- corpus: `e0f797eb3ada91e1758874f7306682d5cd55dd582cbd3601c60f351aceea487b`;
- Python adapter: `0dadbddbf5a2c16f933c43b24260ba21f7af91566f8b712748a05ed746e89eda`;
- Node adapter: `bf9ce7116d8051e814eab544e6127c4f3833ccb210562a51b6f30e540d99074e`;
- Python final run: `9eec1d5111c14294eb4eec27adbdb1bce69ca79ea1d0ccbee34b6137b0d185ae`;
- Node final run: `8ee5a9626fc96468e235fa63490ea29427ef5671671308d1c6234852292791ab`.

## Material findings retained

1. Native UTF-8 behavior diverged for an unpaired surrogate: Python rejected while naive Node replacement-encoded. The candidate now requires Unicode-scalar validation before UTF-8; both adapters reject the retained case as `NON_SCALAR_STRING`.
2. Numeric-syntax fuzzing found the Python integer grammar could let `--1` reach an uncaught conversion error while Node rejected it. Both adapters now enforce the same explicit signed-integer grammar, with retained `--1`, `+1`, and `-01` rejection cases.
3. A JavaScript falsy-default implementation would have accepted an explicitly empty schema version. Presence-based defaulting corrected it; both adapters reject as `SCHEMA_VERSION`.

## Scope limits / open work

This does not authorize local/native serializer hashes, floats or other untested semantic types, implicit Unicode normalization, production schema/content-package hashing, migration equivalence, persistence encoding, engine selection, or production implementation readiness.

Reopen/version on any new-runtime mismatch, semantic normalization requirement, new authoritative value type/range, schema/content identity rule change, hash-scope/algorithm change, reference identity change, or retained-evidence integrity loss.

## Next action

Freeze this branch after the terminal schema-3 `STATUS(REVIEW_READY)` records the exact final branch/work SHA. `W2-REV-01` must independently critique this evidence before downstream authority is widened. Do not merge this producer branch to `main` as a substitute for the declared review/canonicalization route.