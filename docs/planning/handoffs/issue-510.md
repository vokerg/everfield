# Issue #510 — Unity license-exit remediation required-review handoff

## Identity

- Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-01`
- Task class: `REQUIRED_REVIEW`
- Claim: Issue #510 comment `5311536139`
- Branch: `planning/issue-510`
- Base: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- Trust mode: `DEGRADED_SINGLE_AGENT`
- Producer session excluded: `frontier-drain-provider-unity-license-exit-rem-gpt56sol-20260817-01`
- Canonical binding: Issue #6 comment `5245368879`
- Canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonical activation: `413e729e8d2d5ac2eb138903f3f2ace07283b23e`
- Canonicality: `NOT_CANONICAL`

## Judged immutable candidate

- Producer Issue #508 terminal status: `5311500674`
- Producer PR: #509, draft
- Frozen PR base: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- Frozen PR head: `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b`
- Validator blob: `e15c9df7eaab9f8a5a6cd96e945b93cbfdb29a7c`
- Producer handoff blob: `9f5c79a7259f9d82f18509f630429715e5807e2c`
- Changed paths: exactly the validator and `docs/planning/handoffs/issue-508.md`
- Source evidence blob: `c17c9771a37ed1d8706f27dfef13db8754b5a50a`

## Review artifact

- Report: `docs/planning/wave-2/reviews/w2-eng-provider-unity-license-exit-remediation-review.md`
- Report blob: `494d30b6a43731cb6d954f9e582fcc07d5ddaad0`
- Disposition: `CHANGES_NEEDED`
- BLOCKER: 0
- MAJOR: 1
- correction-requiring MINOR: 1

## Findings

### `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-M01` — MAJOR

Exit `3` is documented as authentication **or authorization** failure, and the candidate stage preserves that disjunction, but the durable blocker remains `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_FAILED`. The blocker therefore over-attributes the cause and can misroute remediation. Revision must use a bounded blocker preserving authentication-or-authorization uncertainty and update tests/handoff accordingly.

### `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-m02` — correction-requiring MINOR

The new valid-envelope/nonzero tests exercise the process classifier and component predicates rather than the `validate_unity` integration path. Add deterministic integration-level synthetic tests asserting final provider state/booleans for exit `3`, exit `4` valid/invalid envelope, exit `6`, timeout/transient, unknown nonzero, and exit `0` active/inactive controls. No provider credentials or network calls are needed.

## Positive checks retained

- Exit `4` is correctly classified prospectively as `LICENSE_STATUS_CONFIGURATION_REQUIRED` / `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`.
- A valid envelope on exit `4` remains diagnostic-only; authentication/license stay false and editor/native-S3 does not execute.
- Exit `6`, transient, and unknown nonzero cases remain fail-closed.
- Conflicting/top-level `active` ambiguity guard remains intact.
- Secret transport/redaction and bounded evidence fields are unchanged.
- The final embedded Unreal script contains Python `and`, not the accidental intermediate `&&` drift.
- Historical evaluator evidence `31988648526` remains immutable with its original labels.
- Trusted-main workflow still runs syntax/full-self-test before credential-bearing validation.
- No provider credential was consumed by the review branch.

## Verification note

Producer provenance records exact-blob `py_compile` PASS and 38/38 `--self-test` PASS. The connector-only reviewer environment did not provide an executable checkout of the frozen blob, so those full-script commands were not independently rerun and are not used to waive the test-coverage finding. A non-secret reviewer semantic probe reconstructed from exact fetched candidate snippets confirmed the actual exit-0/3/4/6/unknown gate behavior. The corrected candidate's fresh review must independently execute the exact frozen blob's syntax and full self-test before any PASS disposition.

## Required next gate

PR #509 must not integrate. Route a bounded remediation/revision that:

1. preserves exit-3 authentication-or-authorization uncertainty in the durable blocker;
2. adds integration-level deterministic provider-output tests;
3. preserves the correct exit-4 fail-closed behavior, historical evidence immutability, secret isolation, Unreal/provider independence, and authority boundaries;
4. opens an exact-head draft PR and routes one fresh required review.

No credentialed execution is authorized on remediation or review branches. After a clean reviewed, separately authorized squash-only publication, the next provider episode must begin on trusted `main` with pre-secret syntax/full-self-test gates.

## Authority boundary

This review grants no integration authority, provider authentication/PASS, Unity license authority, engine selection, implementation/readiness, verification-PASS, production/commercial/legal/platform/release authority, decision, content fan-in, or canonicalization authority.
