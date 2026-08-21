# W2-ENG provider GHCR manifest media review

## Review identity

- mission: `W2-ENG-PROVIDER-GHCR-MANIFEST-MEDIA-REV-01`;
- review Issue: #631;
- trust mode: `DEGRADED_SINGLE_AGENT`;
- review claim: Issue #631 comment `5374850966`;
- judged producer: Issue #629 / draft PR #630;
- exact immutable judged head:
  `7549c9f1264f3ddb15fe3102c627043e986e36d9`;
- exact base/current main:
  `74d13979d27cc0a0046252e8f1aeff9380b3da89`.

The producer branch and PR remained exact-head, open, draft, and untouched. The
review branch contains only this report and its handoff; no provider secret was
consumed.

## Disposition

`PASS_BOUNDED_UNREAL_MANIFEST_MEDIA_REMEDIATION`

Findings:

- BLOCKER: 0;
- MAJOR: 0;
- correction-requiring MINOR: 0.

## Frozen candidate

The exact diff contains only:

1. `tools/planning/engine_provider_effective_validator.py`;
2. `docs/planning/handoffs/issue-629.md`.

The executable change replaces the previous two-value Accept contract with a
bounded three-value contract that adds
`application/vnd.oci.image.index.v1+json`. It does not change GHCR origin,
repository path, bearer challenge validation, token exchange, tag selection,
digest handling, Docker/editor/native gates, provider unlock predicates, or
authority fields.

## Adversarial review

### Current trigger and reproduction — PASS

The fresh trusted-main trigger reached token exchange HTTP `200` with a valid
token response, then received manifest resource retry HTTP `404`. A bounded
account-side reproduction showed the private EpicGames package and UE 5.8 tags
were available, the prior Accept set returned `404`, and the OCI image-index
Accept returned `200`. This is a precise media-negotiation defect, not a PAT
or Unity diagnostic.

### Request and secret boundary — PASS

The new constant is used for both the initial GHCR request and the bearer
retry. The bearer remains local, no new host/path is introduced, redirects
remain fail-closed, and no token, Authorization header, response body, cookie,
or hash is emitted. The change does not broaden token scopes or alter package
identity.

### Downstream and authority preservation — PASS

The fix only allows the manifest/index response to be received. Existing
manifest digest validation, Docker login, digest-pinned image, editor
discovery, native S3, provider independence, historical 50-cell preservation,
and all authority flags remain unchanged. Accepting an image index cannot set
provider PASS by itself.

### Verification — PASS

From an extracted archive of the immutable producer head:

- `python3 -m py_compile tools/planning/engine_provider_effective_validator.py` passed;
- the complete validator `--self-test` passed;
- the new `ghcr_manifest_accepts_oci_image_index` case passed;
- `git diff --check` passed;
- no protected credential or provider secret was used.

## Conclusion

No correction is required for the bounded manifest-media objective. The exact
candidate may proceed through separately authorized squash-only integration,
followed by one fresh trusted-main evaluator inspecting Unreal only. Unity and
historical diagnostics remain out of scope.

## Authority boundary

`NOT_CANONICAL` review provenance only. No provider PASS, entitlement, engine
selection, readiness, verification-PASS, decision, integration, or canonical
authority is granted.
