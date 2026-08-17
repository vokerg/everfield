# Issue #499 handoff — W2-ENG-PROVIDER-UNITY-AUTOAUTH-AMBIG-REM-01

## State

Bounded remediation candidate for `W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01` is ready for one fresh required security/authority review.

## Provenance and frozen inputs

- Issue #499 claim `5311042292`;
- branch `planning/issue-499`;
- base/current-main identity at claim: `d7a749bb38a73d08ba63ad62296781b6d0b4c0ea`;
- canonical Planning Program v1 blob `e3120ec203c4156328770aa86c12fbb7187966dc`, binding Issue #6 comment `5245368879`, activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e`;
- immutable source producer Issue #495 / draft PR #496, exact head `9ea697d0b00f41a52940d37c6c3da14fc575abdf`, judged validator blob `d73399df23e29f84607056a972f3fc80e3d49b88`;
- immutable required review Issue #497, terminal comment `5311026366`, review PR #498 exact head `838f5e3a32cb37575a93252c6fc912c31d208bb6`;
- review disposition `CHANGES_NEEDED`, finding `W2-ENG-PROVIDER-UNITY-AUTOAUTH-REV-M01`;
- independent Unreal human gate remains Issue #480.

The task branch was created from exact current `main` and fast-forwarded to the exact immutable #495 producer head to reconstruct the judged candidate without mutating #495/#496. Issue #495 handoff remains byte-identical on this branch at blob `0bce92d35109b39f9e5dd71b0869f8c483dd65cf`.

## Exact finding closure

The required review found that `unity_license_status_envelope()` accepted a response that contained a top-level `active` marker together with nested `data.active`, even though the candidate contract required top-level/ambiguous active markers to fail closed.

This remediation adds only the bounded guard:

```python
if "active" in data:
    return False, None
```

and one deterministic pure regression case proving `{"active": false, "data": {"active": true}}` is rejected.

The exact producer-to-remediation comparison after correction is one modified path with four added lines and zero deleted lines. Exact nested `data.active=true` and `data.active=false` acceptance remains unchanged; missing, non-boolean and top-level-only cases remain rejected. No Unity auth transport, license gating, editor/native-S3, Unreal/GHCR, provider-independence, credential transport or authority semantics are otherwise changed.

## Drift correction before terminal fence

An intermediate task commit accidentally changed the embedded Unreal Python S3 script token `and` to `&&`. That drift was detected immediately by exact producer-to-branch comparison and reverted before handoff/PR publication. The cumulative producer-head comparison now contains only the four intended Unity parser/test additions; the Unreal baseline is byte-identical to the judged producer.

## Verification boundary

No provider credential was used and no credentialed provider execution was performed from this branch. The repository's credentialed evaluator remains trusted-main-only. This remediation does not claim trusted-main `py_compile`, full `--self-test`, Unity authentication, license state, editor installation, native S3 or provider PASS. Fresh required review must inspect exact source coherence; reviewed publication must still be followed by the trusted-main pre-secret syntax/full-self-test gate and one fresh credentialed evaluator/recorder episode.

## Required review attacks

1. freeze the exact remediation PR head/base/draft/path identity before judging;
2. prove the final producer-head delta is limited to the top-level `active` fail-closed guard, its deterministic regression case, and this remediation handoff;
3. prove conflicting top-level plus nested `active` fails closed while exact nested active/inactive envelopes remain valid;
4. prove missing/non-boolean/top-level-only active envelopes remain rejected;
5. verify the rest of the #495 candidate, including service-account environment-only transport and first unattended `unity license status` command, is unchanged;
6. verify exact Unity 6000.5.6f1 editor/native-S3, Unreal/GHCR and independent-provider semantics are unchanged;
7. verify no branch credential execution occurred and trusted-main pre-secret syntax/full-self-test remains mandatory before Secrets;
8. do not infer provider/auth/license success from review.

## Required route

A fresh independent/degraded-independent security/authority review is mandatory before any implementation publication. A clean review may authorize only separately governed noncanonical publication; one fresh trusted-main evaluator/recorder episode remains mandatory afterward.

## Authority boundary

`NOT_CANONICAL`. Bounded parser ambiguity remediation only. No provider credential/PASS, Unity license authority, engine selection, implementation readiness, commercial/production/legal/release, verification-PASS, decision, integration or canonical authority.