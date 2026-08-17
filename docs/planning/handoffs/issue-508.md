# Issue #508 — Unity license-status exit classification remediation handoff

## Identity

- Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REM-01`
- Task class: `BLOCKING_REMEDIATION`
- Claim: Issue #508 comment `5311443502`
- Branch: `planning/issue-508`
- Claimed base / current compatible main: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- Canonical binding: Bootstrap Issue #6 comment `5245368879`
- Canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Canonicality: `NOT_CANONICAL`

## Triggering immutable evidence

The already-published provider-effective evidence for evaluator run `31988648526` / recorder run `31988661897` records Unity `license status` exit `4`, no timeout, a valid structured license-status envelope, `authentication_validated=false`, and `license_validated=false`. Its immutable evidence blob is `c17c9771a37ed1d8706f27dfef13db8754b5a50a`; Issue #504 terminalized that evidence at comment `5311174296`, and Issue #506 squash-published it to `main@538b8a3b46b8b095bc43206d4a0ad4fdc151616a` without upgrading authority.

Historical evidence is unchanged by this remediation.

## Remediation

`tools/planning/engine_provider_effective_validator.py` now classifies failed Unity `license status` processes with bounded, fail-closed stage/blocker enums:

- exit `3` → authentication/authorization failure;
- exit `4` → `LICENSE_STATUS_CONFIGURATION_REQUIRED` / `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`;
- exit `6` → operation failure;
- timeout or bounded transient-network signature → transient failure;
- other nonzero exit → generic process failure.

A valid structured license envelope on any nonzero process result remains diagnostic-only: it does not establish authentication, an active license, editor eligibility, provider PASS, or any downstream authority. The existing exit-0 envelope gate remains intact. Unreal behavior and the 50 historical `NOT_RUN` cells are unchanged.

## Exact implementation identity

- First implementation commit: `11882faa7469dbd53276a3a2efe1d73527a0a3ce`
- Immediate corrective commit restoring an accidental unrelated embedded Unreal-script transcription before review: `5b5dc8dfd8aef747c36400f1733a163bbdbd836e`
- Final validator blob: `e15c9df7eaab9f8a5a6cd96e945b93cbfdb29a7c`
- Base validator blob reconstructed for verification: `112e8140a145fdf80556414358dbdd524416f9fa`

The base validator was reconstructed locally and its Git blob SHA matched `112e8140a145fdf80556414358dbdd524416f9fa` exactly before patching. The final locally tested file computes Git blob SHA `e15c9df7eaab9f8a5a6cd96e945b93cbfdb29a7c`, matching the repository write result exactly.

## Non-secret verification

Performed without provider credentials:

```text
python3 -m py_compile tools/planning/engine_provider_effective_validator.py
PASS

python3 tools/planning/engine_provider_effective_validator.py --self-test
PASS — 38/38 deterministic cases
```

The added deterministic coverage includes exit-0 active/inactive structured envelopes, exit `3`, exit `4` with valid envelope, exit `4` with invalid envelope, exit `6`, timeout, transient-network classification, unknown nonzero exit, and the invariant that no nonzero process result can establish authentication/license success.

Repository compare from `538b8a3b46b8b095bc43206d4a0ad4fdc151616a` to final implementation head showed only `tools/planning/engine_provider_effective_validator.py` before this handoff was added. The accidental unrelated embedded Unreal-script change was detected by that compare and restored before review; final validator content matches the locally tested blob.

No provider credential was consumed on this branch. No workflow, secret, generated evidence, policy, Unreal behavior, S7 work, or historical evidence was modified.

## Required next gate

Open an exact-head draft PR to current `main`, then route exactly one fresh independent or degraded-independent security/authority review of this remediation. The reviewer must attack:

- Unity exit-code semantics and fail-closed unknown handling;
- valid-envelope/nonzero handling and false authentication/license/PASS risk;
- secret isolation and bounded evidence fields;
- preservation of Unreal/provider independence;
- historical evidence immutability;
- authority inflation.

The reviewer must not repair this producer branch.

After a passing review and separately authorized squash-only publication, the next provider episode must start from trusted `main` with a pre-secret syntax/full-self-test gate before any fresh credentialed evaluator/recorder execution.

## Authority boundary

This handoff grants no integration authority, provider authentication/PASS, Unity license authority, engine selection, implementation/readiness, verification-PASS, production/commercial/legal/platform/release authority, decision, content fan-in, or canonicalization authority.
