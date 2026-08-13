# Issue #101 handoff — W2-PG-REM-CI-02

## Status

`REVIEW_READY`

## Disposition

`CHANGES_NEEDED`

Severity: `0 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR`.

## Scope completed

- Independently reviewed frozen Issue #99 work/head `7cbfddf90d885c4fe2b1dd6433f6157a9453b0e0` without modifying or re-owning it.
- Recomputed all three published Appendix A compact-JSON SHA-256 digests exactly.
- Inspected the exact Issue #99 branch delta and reviewed tree for the claimed v3 evaluator/validator artifact.
- Attacked replacement ArtifactIdentity evidence, successor transition/predecessor-root proof, retained-artifact identity/hash replay, preserved retry/applicability semantics, and authority boundaries.
- Recorded two MAJOR findings requiring one bounded remediation successor.

## Review artifact

- `docs/planning/wave-2/reviews/w2-rem-ci-02-pre-gate-review.md`
- `docs/planning/handoffs/issue-101.md`

## Immutable reviewed provenance

- Issue #99 work/head: `7cbfddf90d885c4fe2b1dd6433f6157a9453b0e0`
- Issue #99 report blob: `0d821317792fd1be06bf56c51ceee09f7e72c549`
- Issue #99 disposition blob: `b992ea5a6929575f619557a03bed730d973de1f3`
- Issue #99 handoff blob: `2f468bfc8e657eaf3530222783f43ec34a1e7020`
- Issue #97 review work/head: `091221bf92699910a01775b4368a7618106f5e14`
- Issue #97 review artifact: `533d4192fecf3e550e57ca630fcea79b9ae17326`
- Issue #101 claim comment: `5276032249`
- exact base main: `c7ba185ed9667b717794c19eaa0834ca41aa4c78`

## Independent checks

Published digests independently reproduced:

- fixture manifest: `sha256:8068cbc8563faf1c91c983b85baaa25be443236da3cd3980c1c27952d90c14ae`
- harness contract: `sha256:fe185e57a52b16c4c14fea1ab7c34bfe2198ef835cb244c3ebed89ffcafecfa5`
- result object: `sha256:dd171542b1b00b94f8e679cd40e575a0b826df410b0d82216b497f5794da07e6`

The hashes authenticate the Appendix A declarations but not evaluator execution.

## Findings

### `PG-REM-CI2-M01` — MAJOR

The frozen Issue #99 packet publishes input/descriptor/result JSON but no executable v3 validator, immutable validator artifact/ref, or deterministic executable specification. The exact branch adds only three Markdown files. The claimed S1-S17 verdicts and validator-enforcement semantics therefore cannot be independently reproduced. Quarantine-expiry and replacement-set mismatch regression outcomes are also absent from the published result corpus despite being acceptance-preserved behaviors.

Required correction: publish and content-bind an executable deterministic validator plus complete runnable corpus, including expiry/replacement-set regressions, so the result digest can be reproduced from exact frozen inputs without trusting prose.

### `PG-REM-CI2-M02` — MAJOR

The S10 result retains a declared predecessor evidence root and an identical `observed` root, but no predecessor evidence-envelope chain, immutable content-addressed chain reference, or root canonicalization/version rule. `source_envelope_id: env-flaky-1` is only a dangling identifier. A reviewer cannot reconstruct the predecessor root or detect substituting both root fields together.

Required correction: retain the exact predecessor evidence chain or immutable content-addressed reference plus canonical-root algorithm/version; bind it into the transition result and add a root-substitution negative fixture.

## Preserved observations

- S6 durable replacement records materially improve ArtifactIdentity/hash/provenance binding.
- S15/S16/S17 correctly express exact restoration versus identity/hash substitution at the declared-object level.
- `NOT_RUN`, PRODUCT, INFRA, FLAKY, same-candidate reset, and retention-loss outcomes remain explicitly represented.
- CI provider, universal INFRA classifier, production, readiness, integration, and canonicalization authority remain unclaimed.

## Next recommended action

Create one bounded remediation successor for `PG-REM-CI2-M01` and `PG-REM-CI2-M02`, from then-current `main`, consuming Issue #99 and this review only at immutable SHAs. Do not edit `planning/issue-99`. The successor should publish the exact executable validator/corpus and predecessor evidence-lineage artifact/ref, run the required negative fixtures, self-review to zero unresolved BLOCKER/MAJOR, and freeze at `STATUS(REVIEW_READY)`.

Formal aggregate independent adversarial review remains `W2-REV-01`; this pre-gate review does not replace or bypass it.