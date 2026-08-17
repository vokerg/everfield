# Issue #503 handoff — W2-ENG-PROVIDER-UNITY-AUTOAUTH-AMBIG-REM-INT-REC-01

## State

Byte-identical current-main recovery of the clean-reviewed Unity automatic-auth ambiguity remediation is prepared for exact-head squash publication under owner convergence authority.

## Recovery provenance

- Issue #503 claim `5311137711`;
- branch `planning/issue-503`;
- recovery base `main@8598d196d00ce4c34f1bfd2b9d66d1c91da00236`;
- canonical Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding Issue #6 comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- owner convergence directive Issue #84 comment `5277825639`;
- immutable source remediation Issue #499 terminal comment `5311082200`, stale draft PR #500 exact head `cbcc41156984f237299fa3f6cd64f042df755aa5`;
- clean required review Issue #501 terminal comment `5311115926`, disposition `PASS_BOUNDED_PROVIDER_UNITY_AUTOAUTH_AMBIG_REMEDIATION`, 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR;
- review PR #502 exact head `60776633e108c0042076876e9367a6c07b5cfd69`, squash-published as noncanonical review provenance at `8598d196d00ce4c34f1bfd2b9d66d1c91da00236`;
- Issue #501 integration status `5311123945`, owner convergence ledger record `5311124503`.

## Exact recovered implementation bytes

The recovery reuses the exact clean-reviewed blobs without textual reconstruction or semantic conflict resolution:

- `tools/planning/engine_provider_effective_validator.py` -> `112e8140a145fdf80556414358dbdd524416f9fa`;
- `docs/planning/handoffs/issue-495.md` -> `0bce92d35109b39f9e5dd71b0869f8c483dd65cf`;
- `docs/planning/handoffs/issue-499.md` -> `b2522465a90b03697e323210ee0ebda480df1ca3`.

Only this Issue #503 recovery handoff is new provenance. No implementation byte may differ from the reviewed packet. If any exact blob identity fails, this recovery is invalid and requires a fresh semantic review route rather than repair in place.

## Why recovery is required

PR #500 was exact-head and mergeable when Issue #499 terminalized on `main@8d4c8e29…`. The required review then terminalized cleanly and its review-only PR #502 was separately squash-published under owner convergence. That publication advanced `main` to `8598d196…` and left immutable PR #500 stale/unmergeable. The reviewed implementation therefore must be re-materialized byte-identically on current-main ancestry before publication; the frozen #499/#500 branch remains untouched.

## Verification and execution boundary

No provider credential is used and no credentialed provider execution occurs from this recovery branch. The recovery itself does not claim `py_compile`, validator `--self-test`, Unity authentication, active license, editor installation, native S3, or provider PASS.

After squash publication, the trusted-main evaluator must still run its pre-secret `python3 -m py_compile` and complete validator `--self-test` gate before provider Secrets are introduced, followed by one fresh credentialed evaluator/recorder episode. Only that fresh trusted-main evidence may advance the Unity provider frontier. Unreal remains independently human-gated by Issue #480.

## Integration boundary

Because the semantic packet is byte-identical to the exact clean-reviewed #499 candidate and the only new path is recovery provenance, no fresh semantic review is required if current-main compatibility and exact blob identity remain clean. Owner convergence directive `5277825639` authorizes squash-only noncanonical publication after those exact checks, with expected-head protection.

## Authority boundary

`NOT_CANONICAL`. Byte-identical recovery/publication only. No semantic change authority, provider credential/PASS, Unity license authority, engine selection, implementation readiness, commercial/production/legal/release, verification-PASS, decision, or canonical authority.