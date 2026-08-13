# Issue #112 handoff — W2-REM-ENG-04

## Mission and ownership

- mission: `W2-REM-ENG-04`
- task class: `REMEDIATION / EVIDENCE_REQUIRED`
- branch: `planning/issue-112`
- base: `main@042d140b5d2e0b951da4528e1867514983418d6f`
- ownership claim: Issue #112 comment `5276604598`
- output schema: `bounded_engine_harness_remediation_v4`
- authority: noncanonical planning evidence; formal `W2-REV-01` remains required

## Immutable inputs consumed

- Issue #104 candidate head/work `b406193c45c75f6309ea4123d02579d70ebe3591`
- Issue #104 harness blob `1fb26cb6afa02b7061d37f331cf5a132375ecfc4`
- Issue #104 validator blob `b7209361fa8c52f599d1e7393d28a2d19658887c`
- Issue #104 recovered valid terminal status comment `5276379684`
- Issue #110 review work `8941b0fa66f99d7343d8f792f562f58099776582`
- Issue #110 review artifact blob `7587f4f2b7487de94a695b1a0ccc7356368100ce`
- Issue #110 terminal status comment `5276423996`, disposition `CHANGES_NEEDED`
- current root/canonical authority surfaces: `AGENTS.md`, `docs/planning/START-HERE.md`, `docs/planning/PLANNING-PROGRAM-v1.md`

Frozen predecessor branches were not edited or re-owned.

## Completed work

1. Closed `PG-REM3-M01` with a kind-specific attempt schema enforced before sorting/aggregation. Null/empty reset/workspace identity, non-boolean reset flags, malformed/duplicate normal indices, and invalid failure-injection index shape fail closed as typed invalid envelopes rather than passing or raising.
2. Closed `PG-REM3-M02` by requiring exact nonempty adaptation candidate identity, checking it against the consuming generation, and binding exact candidate/scenario/harness/feature/scenario-contract/adaptation identities in a recomputed content-addressed binding.
3. Closed `PG-REM3-m01` by separating `lineage_valid` and `evidence_valid`; full history `valid` requires both.
4. Preserved Issue #104 duplicate-injection, cross-candidate-attempt, result/failure-matrix, common-slice, reset/resource, repair, S3/S9/S10, and no-engine-selection protections.
5. Added direct executable attacks EQ-16/17, AG-18…29, and HIST-06.
6. Updated the finding disposition packet with exact closure evidence and a fail-closed terminal route for `PG-REM3-B01`.

## Checks and evidence

- `python3 -m py_compile docs/planning/wave-2/evidence/engine-spike-protocol-fixtures.py`: PASS on exact prepared source.
- two full validator executions: PASS; stdout byte-identical.
- all embedded equivalence/aggregate/history assertions: PASS.
- fresh #110 attacks produce typed invalid outcomes, including null-index no-crash behavior.
- preserved #104 cases reproduce their prior truth classes.

Exact prepared identities:

- validator source `sha256:915d84b10fc1744af6d077bcec5025fd95f02877af341082a45e5cfaa90bc8fa`
- validator contract `sha256:5f37d97fa2bb263d87a10bc5cfd9311c744e1b80e83d42c8d6a9b202ccfef269`
- feature slice `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs `sha256:15fd95e053acc634a7df2953ab411895fd47b8ee6145465a7faf6623579d3a6b`
- result object `sha256:f76a166ec79ea08ceb2dc60ad5988f33a108a59cd153fb1157ebf0817fe850ac`
- deterministic stdout `sha256:6f194aa5426c42e545130160da3eeb2d5e36d05ea3296d2b54c4cb9add177baa`

## Bounded self-review

- unresolved substantive BLOCKER: 0
- unresolved substantive MAJOR: 0
- correction-requiring MINOR: 0
- engine execution/scoring/selection: none
- production/readiness/integration/verification/canonicalization authority: none

The lifecycle finding `PG-REM3-B01` is intentionally not waived by prose. Before terminal `STATUS(REVIEW_READY)`, an open draft PR from this exact branch to `main` must be created and re-fetched with PR head exactly equal to the final branch head. The terminal schema-3 status must record that PR/head evidence.

## Remaining terminal sequence

1. Under the active ownership generation, mutation-fence the branch and commit the four declared outputs.
2. Re-run/verify exact committed validator identity if transport changes bytes.
3. Open a draft PR from `planning/issue-112` to `main` solely for review visibility.
4. Re-fetch branch and PR; require exact head equality.
5. Publish terminal schema-3 `STATUS(REVIEW_READY)` with exact work/head, artifact refs, digest evidence, PR number/head, and resolved finding IDs.
6. Stop. Do not merge, integrate, execute engines, or claim `W2-REV-01` authority.
