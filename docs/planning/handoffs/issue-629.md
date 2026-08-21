# Issue #629 handoff — accept OCI image-index Unreal manifests

## State

The narrow current-main remediation is complete on the claimed branch. It
changes only the GHCR manifest Accept contract and its deterministic self-test;
Unity, credentials, scopes, package paths, tag selection, downstream gates, and
authority predicates are unchanged.

## Frozen trigger

- mission: `W2-ENG-PROVIDER-GHCR-MANIFEST-MEDIA-01`;
- claim: Issue #629 comment `5374821714`;
- base/current main: `74d13979d27cc0a0046252e8f1aeff9380b3da89`;
- fresh evaluator run: `32521917620`, attempt 1;
- evaluator job: `96895743693`;
- artifact: `9460837845`, digest
  `sha256:f71dfd04ce82a2503fb6881e761435d08fe961be48b3bceb7d72c7a6bcfed009`.

The fresh protected result was GHCR token exchange `200` with a valid token
response, followed by manifest resource retry `404` and
`RESOURCE_RETRY_FAILED`. Unity was explicitly out of scope.

## Implementation

`registry_request()` now requests the observed OCI image-index media type in
addition to the existing OCI image-manifest and JSON types. The new bounded
self-test asserts that both OCI index and OCI manifest media types remain in
the request contract.

Account-side reproduction against the private EpicGames package showed:

- tags-list `200`;
- the validator's previous Accept set returned manifest `404`;
- an OCI image-index Accept returned manifest `200`.

No credential value, Authorization material, response body, or hash was added
to the repository or evidence.

## Verification

- `python3 -m py_compile tools/planning/engine_provider_effective_validator.py` passed;
- full `--self-test` passed, including
  `ghcr_manifest_accepts_oci_image_index`;
- `git diff --check` passed;
- substantive commit: `3fd748399a95604dd0318c0daf7f991e6a8dad62`.

## Required continuation

1. Recheck current main, ownership, and remote branch.
2. Commit this handoff as the second task-branch commit.
3. Open and verify an exact-head draft PR.
4. Route one fresh degraded-independent review of the immutable candidate.
5. After clean review, squash-integrate only under existing authority.
6. Run one fresh trusted-main evaluator; inspect Unreal only. Do not rerun Unity
   or historical identity diagnostics.

## Authority boundary

`NOT_CANONICAL`. Review-ready remediation only. No provider PASS, entitlement,
engine selection, readiness, verification-PASS, integration, decision, or
canonical authority is granted.
