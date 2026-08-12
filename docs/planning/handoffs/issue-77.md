# Issue #77 handoff — W2-CI-01

**Mission:** `W2-CI-01`  
**Branch:** `planning/issue-77`  
**Ownership generation:** Issue #77 comment `5264276879`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation blob:** `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Evidence report blob:** `7f9cb919c5e28299b7edbb1ea5495138d1509791`  
**Evidence report commit:** `928df2bc5a609957ba3080c3f9ba11fad5f5bed6`  
**State intended after terminal capsule:** `REVIEW_READY`  
**Required review:** `W2-REV-01`

## Completed work

Produced `docs/planning/wave-2/evidence/ci-reliability-experiment.md` from the bounded authoritative packet.

The experiment defines and executes a provider-independent synthetic `EvidenceRequirement -> CheckPlan -> attempts/artifacts -> EvidenceSatisfaction` fixture with 11 scenarios covering:

- required, conditionally required, optional, and not-applicable checks;
- required `NOT_RUN` versus `NOT_APPLICABLE`;
- PRODUCT fail/retry, INFRA fail/retry, and FLAKY/retry lineages;
- active quarantine with explicit replacement evidence;
- quarantine expiry and post-remediation return to the normal requirement;
- retained artifact loss, exact restoration, and wrong-hash restoration.

The exact reference harness is embedded in the evidence report.

## Material findings

1. Required `NOT_RUN` stays gating and cannot be reclassified as `NOT_APPLICABLE` by absence of execution.
2. A same-candidate PRODUCT failure remains `UNSATISFIED` even if a later attempt passes; retry cannot launder the failure.
3. Explicitly permitted INFRA retry can recover to `SATISFIED` while retaining every failed attempt, but the real infra/product classifier remains an unresolved trust surface.
4. FLAKY plus later PASS remains `UNSATISFIED`.
5. Quarantine can satisfy only through an explicit temporary requirement version with replacement evidence; expiry reopens the requirement automatically.
6. Required evidence loss reopens aggregate state to `INCONCLUSIVE`; exact content restoration restores satisfaction, while wrong-hash restoration does not.
7. The bounded fixture supports reconstructable aggregate satisfaction without treating a mutable green label as authority.

## Exact experiment evidence

- Fixture digest: `b382dc1b0c7b7b93b111328c1a4fdc95b492d4713117fcec2e4801904440c0ae`.
- Reference harness digest: `879ec2a11549b609ad001efb1ba810c096ee0b3077bda19ed711dc1ce6a0748c`.
- Canonical 11-scenario result-object digest: `57628e3bc66d694367f99ba035f70884ad729cb1a8a74c9bcdf228b09e693263`.
- Execution environment: Python `3.13.5`, Linux `6.18.35-x86_64`, glibc `2.41`.
- Evidence report blob: `7f9cb919c5e28299b7edbb1ea5495138d1509791`.

## Scope limits / open work

This is a `BOUNDED_PASS` only for provider-independent semantic behavior exercised by the fixture.

It does not:

- validate GitHub Actions or another provider's enforcement mechanics;
- solve INFRA-versus-PRODUCT classification generally;
- define a canonical universal `EvidenceSatisfaction` enum;
- close `IR-BLOCKER-EVIDENCE-FOUNDATION`;
- authorize production/gameplay implementation;
- replace independent `W2-REV-01`.

Open questions retained in the report include infra classification evidence, same-candidate retry limits, quarantine external state representation, retention audit cadence, provider expiry enforcement, and exact-byte restoration across mirrors.

## Producer self-review

Self-review against Issue #77 acceptance criteria and the canonical Wave 1 foundation:

- BLOCKER: 0
- MAJOR: 0
- MINOR requiring correction before terminalization: 0
- retry laundering negative control retained: PASS
- missing-required-evidence negative control retained: PASS
- `NOT_APPLICABLE` versus `NOT_RUN` separation: PASS
- flake lineage retention: PASS
- quarantine expiry/replacement lifecycle: PASS
- artifact loss/restoration reopen behavior: PASS
- provider mechanics remain explicitly experimental/noncanonical: PASS
- production/readiness authority leakage: none identified

## Next action

After the terminal schema-3 `STATUS(REVIEW_READY)` binds the exact final branch/work SHA, freeze `planning/issue-77`.

`W2-REV-01` must independently critique this exact work state. Do not treat producer self-review, a PR, or any later main integration as the independent review disposition. Any integration into `main` must remain squash-only and follow the declared review/integration authority.
