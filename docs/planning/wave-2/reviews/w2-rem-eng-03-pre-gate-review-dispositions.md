# W2-REM-ENG-04 — Issue #110 pre-gate finding dispositions

**Remediation issue:** #112 / `W2-REM-ENG-04`  
**Frozen substantive predecessor:** Issue #104 head/work `b406193c45c75f6309ea4123d02579d70ebe3591`  
**Frozen predecessor harness/validator:** `1fb26cb6afa02b7061d37f331cf5a132375ecfc4` / `b7209361fa8c52f599d1e7393d28a2d19658887c`  
**Independent review:** Issue #110 work `8941b0fa66f99d7343d8f792f562f58099776582`, review blob `7587f4f2b7487de94a695b1a0ccc7356368100ce`  
**Review disposition:** `CHANGES_NEEDED` — 2 substantive MAJOR / 1 MINOR plus 1 lifecycle BLOCKER  
**Authority:** bounded noncanonical remediation evidence; formal `W2-REV-01` remains required.

## Disposition summary

| Finding | Severity | Disposition | Mechanical closure |
|---|---|---|---|
| `PG-REM3-M01` | MAJOR | **RESOLVED** | Closed kind-specific attempt validation runs before sort/aggregation. Null/empty reset/workspace, non-boolean reset flags, null/string/bool/duplicate normal indices, and a failure-injection normal index all return typed invalid envelopes. |
| `PG-REM3-M02` | MAJOR | **RESOLVED** | Adaptation candidate identity is mandatory and matched to the consuming generation. Exact scenario/adaptation content is bound by a recomputed binding ID; wrong/missing candidate, cross-candidate reuse, and binding substitution fail closed. |
| `PG-REM3-m01` | MINOR | **RESOLVED** | History returns `lineage_valid`, `evidence_valid`, and full `valid`; a linked history containing an invalid generation envelope is not fully valid. |
| `PG-REM3-B01` | lifecycle BLOCKER | **ENFORCED BY TERMINAL ROUTE** | Issue #112 may not publish terminal `STATUS(REVIEW_READY)` until an open draft PR from the exact branch to `main` exists and PR head equals terminal `head_sha`. Terminal status records the exact PR evidence. |
| Issue #104 duplicate injection / candidate attempt / result-failure fixes | regression risk | **PRESERVED** | Existing AG-14…17 and HIST-05 remain invalid/closed; all pre-existing fixture objects reproduce their prior truth classes. |

## `PG-REM3-M01` — closed attempt schema

The frozen v3 candidate could admit null reset/workspace identities, accept duplicate normal indices, and raise `TypeError` for a null normal index. v4 validates every retained attempt before sorting or authority derivation.

For every attempt, identity, kind, result/failure class, nonempty reset/workspace/resource strings, and exact boolean `reset_verified` are validated. `NORMAL` requires a positive unique exact integer `normal_index` and null `injection_id`; `FAILURE_INJECTION` requires null `normal_index` and a nonempty injection ID. Python booleans are explicitly rejected as normal indices even though `bool` subclasses `int`.

Executable closure:

- AG-18 null reset → invalid envelope;
- AG-19 empty reset → invalid envelope;
- AG-20 null workspace → invalid envelope;
- AG-21 empty workspace → invalid envelope;
- AG-22 truthy integer reset flag → invalid envelope;
- AG-23 null normal index → invalid envelope, no exception;
- AG-24 string normal index → invalid envelope;
- AG-25 boolean normal index → invalid envelope;
- AG-26 duplicate positive normal index → invalid envelope;
- AG-27 failure-injection record with normal index → invalid envelope.

After structural validation, all retained normal attempts require verified, pairwise-distinct reset and workspace identities.

**Disposition: RESOLVED.**

## `PG-REM3-M02` — exact adaptation candidate/consumer binding

The frozen v3 validator ignored `AdaptationManifest.candidate_id`, so a missing or relabeled candidate could still receive `ACCEPT`. v4 validates adaptations against an expected consuming candidate and requires a nonempty exact candidate string.

The generation additionally stores the exact adaptation plus a content-addressed binding over candidate, scenario, harness, feature slice, exact scenario-contract identity, and exact adaptation identity. Before attempt authority, the validator independently revalidates the adaptation against the generation candidate and recomputes the binding ID.

Executable closure:

- EQ-16 wrong candidate → `REJECT`;
- EQ-17 missing candidate → `REJECT`;
- AG-28 candidate-B adaptation with a correctly recomputed B binding reused by candidate-A generation → invalid envelope;
- AG-29 correct adaptation with substituted binding ID → invalid envelope.

Repair history continues to reject untyped candidate changes; a later candidate-transition mechanism must be a separately reviewed typed protocol rather than implicit relabeling.

**Disposition: RESOLVED.**

## `PG-REM3-m01` — explicit lineage versus evidence validity

The frozen v3 history object could return top-level `valid=true` when lineage was coherent even though a generation had `valid_envelope=false`. v4 makes the distinction explicit:

- `lineage_valid` covers generation IDs, predecessor links, same-candidate continuity, changed work, and repair refs;
- `evidence_valid` requires every generation envelope to be structurally valid;
- full `valid` requires both.

HIST-06 is a validly linked two-generation repair in which generation 2 has malformed attempt evidence. It deterministically returns `lineage_valid=true`, `evidence_valid=false`, `valid=false`.

**Disposition: RESOLVED.**

## `PG-REM3-B01` — review visibility

The lifecycle finding concerned Issue #104's historical terminalization. Issue #104 was subsequently recovered and correctly republished at comment `5276379684` with draft PR #111 bound to exact head `b406193c45c75f6309ea4123d02579d70ebe3591`; that history remains immutable provenance.

Issue #112 independently inherits the current canonical rule. Its final lifecycle is fail-closed: commit the exact remediation payload, create an **open draft** PR from `planning/issue-112` to `main`, re-fetch the PR and branch, require exact PR-head/final-head equality, and only then publish terminal schema-3 `STATUS(REVIEW_READY)`. The terminal comment is the authoritative evidence for this procedural closure; no prose in this file can substitute for it.

## Regression and deterministic evidence

The v4 validator uses Python standard library only. Syntax compilation passed. Two complete executions from exact identical source bytes produced byte-identical stdout and all embedded assertions passed.

Exact identities:

- validator source: `sha256:915d84b10fc1744af6d077bcec5025fd95f02877af341082a45e5cfaa90bc8fa`
- validator contract: `sha256:5f37d97fa2bb263d87a10bc5cfd9311c744e1b80e83d42c8d6a9b202ccfef269`
- feature slice: `sha256:9a2523c4870146b09233397f3773f7a27b1e0135c24a6767d16e34a791aab104`
- scenario manifest: `sha256:be4d7473b01da6b428cd5f3be48de083abd161a4899471303f3ccfeef45c725f`
- fixture inputs: `sha256:15fd95e053acc634a7df2953ab411895fd47b8ee6145465a7faf6623579d3a6b`
- result object: `sha256:f76a166ec79ea08ceb2dc60ad5988f33a108a59cd153fb1157ebf0817fe850ac`
- deterministic stdout: `sha256:6f194aa5426c42e545130160da3eeb2d5e36d05ea3296d2b54c4cb9add177baa`

No engine was executed, scored, ranked, or selected. No production, implementation-readiness, integration, verification, release, or canonicalization authority is claimed.

## Bounded self-review

Substantive remediation result: **0 unresolved BLOCKER / 0 unresolved MAJOR / 0 correction-requiring MINOR**.

`PG-REM3-B01` is a lifecycle precondition rather than a semantic payload defect. It is not considered closed until the exact draft-PR/head check is completed and recorded in the terminal Issue #112 status. Formal aggregate `W2-REV-01` remains required after this bounded remediation.
