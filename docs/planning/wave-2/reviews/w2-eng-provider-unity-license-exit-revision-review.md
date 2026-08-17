# W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-02 — required review

## Disposition

`PASS_BOUNDED_PROVIDER_UNITY_LICENSE_EXIT_REVISION`

- BLOCKER: 0
- MAJOR: 0
- correction-requiring MINOR: 0
- non-correction review-environment limitation: 1

This is a bounded security/authority review of immutable Issue #512 / draft PR #514 only. It grants no integration-by-review, provider authentication/PASS, Unity license authority, engine selection, implementation/readiness, production/commercial/legal/platform/release authority, verification-PASS, decision, or canonical authority.

## Frozen candidate

- current main / merge base: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- producer terminal: Issue #512 comment `5312707781`, `REVIEW_READY`
- judged branch: `planning/issue-512`
- judged draft PR: #514
- exact judged head: `d333d00c2e9af4e7711245feae156334b6a01a85`
- corrected validator blob: `69d45fa7bde9bd7879460ac661bac83228f113a6`
- Issue #512 handoff blob: `88aeb3f97424e9a07704e4aadd912b677921041c`
- frozen predecessor head: `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b`
- frozen predecessor validator blob: `e15c9df7eaab9f8a5a6cd96e945b93cbfdb29a7c`
- triggering review: Issue #510 comment `5311555047`, `CHANGES_NEEDED`
- trust mode: `DEGRADED_SINGLE_AGENT`

PR #514 remained open, draft, unmerged and mergeable at review freeze, with base `main@538b8a3...` and head `d333d00...`.

## Scope and provenance checks

`main@538b8a3...` to judged head is seven commits ahead / zero behind with merge base exactly current main and exactly three paths: carried `docs/planning/handoffs/issue-508.md`, current `docs/planning/handoffs/issue-512.md`, and `tools/planning/engine_provider_effective_validator.py`.

Frozen predecessor `defa1fa6...` to judged head is four commits ahead / zero behind with merge base exactly the predecessor and exactly two paths: the validator plus Issue #512 handoff. Therefore the Issue #508 handoff is carried predecessor provenance and there is no workflow, generated evidence, policy, S7, or unrelated content path in the revision delta. Historical evaluator evidence is not mutated.

## Finding reconciliation

### M01 — exit 3 uncertainty: CLOSED

The production failure classifier now maps exit `3` to stage `LICENSE_STATUS_AUTHENTICATION_OR_AUTHORIZATION_FAILED` and durable blocker `UNITY_SERVICE_ACCOUNT_AUTHENTICATION_OR_AUTHORIZATION_FAILED`. Neither field selects authentication versus authorization. Exit `4` remains `LICENSE_STATUS_CONFIGURATION_REQUIRED` / `UNITY_LICENSE_STATUS_CONFIGURATION_REQUIRED`; exit `6` remains operation failure; timeout/transient and unknown nonzero remain fail-closed bounded classes.

### m02 — production decision-path coverage: CLOSED

The corrected source introduces one pure `unity_license_status_decision(result, data)` path. `validate_unity()` calls that same function, copies its authentication/license/stage/state/blocker decisions, and returns before editor installation whenever `proceed_to_editor` is false. The deterministic self-test calls that same production decision function rather than a parallel predicate.

The source self-test directly covers exit `0` active, exit `0` inactive, exit `3`, exit `4` with valid-active and invalid envelopes, exit `6`, timeout, transient network, and unknown nonzero. It includes an aggregate invariant requiring every nonzero decision to keep `authentication_validated`, `license_validated`, and `proceed_to_editor` false.

## Fresh adversarial mechanical replay

The reviewer independently replayed the exact changed pure decision logic transcribed from repository blob `69d45fa7...` with the required cases plus a conflicting top-level `active` marker. Results were fail-closed as required:

- exit 0 + `data.active=true`: authentication/license true, editor progression true;
- exit 0 + `data.active=false`: authenticated command, license false, progression false;
- exit 3 + active envelope: auth false, license false, auth-or-authz stage/blocker, progression false;
- exit 4 + active envelope: configuration-required, auth/license/progression false;
- exit 4 + invalid envelope: configuration-required, auth/license/progression false;
- exit 6: operation-failed, auth/license/progression false;
- timeout/transient: transient failure, auth/license/progression false;
- unknown nonzero: process-failed, auth/license/progression false;
- exit 0 with conflicting top-level `active` plus nested active: envelope rejected and progression false.

This mechanically attacks the false-PASS/editor risk that drove the prior review.

## Secret and provider-independence review

Unity service-account transport remains environment-only through `UNITY_SERVICE_ACCOUNT_ID` and `UNITY_SERVICE_ACCOUNT_SECRET`; the command path supplies secrets to the redaction set and evidence records only bounded process metadata. The existing redactor suppresses password/token/authorization/secret/cookie-bearing lines. The decision helper takes only sanitized process/data values and has no provider/network/secret access.

The exact Unity baseline remains `6000.5.6f1`. The producer-relative changed-path fence contains no workflow/evidence file and source inspection found no independently changed Unreal/GHCR provider route. Historical provider evidence, including evaluator run `31988648526`, is outside the revision delta and retains its original labels. Revised exit semantics are prospective only.

## Exact-source verification evidence and degraded limitation

The reviewer fetched the repository object by exact validator blob identity `69d45fa7bde9bd7879460ac661bac83228f113a6` and reviewed the source and changed production/self-test paths from that object. Issue #512 terminal evidence binds the same exact blob and records a byte-identity rehash followed by:

- `python3 -m py_compile tools/planning/engine_provider_effective_validator.py` — PASS;
- `python3 tools/planning/engine_provider_effective_validator.py --self-test` — PASS, 38/38;
- Unity/Unreal credential variables absent; no provider credential consumed.

The reviewer runtime did not expose the connector-fetched repository blob as a byte-preserving local filesystem object, so the full-file commands could not be independently repeated against a local mount. Instead, fresh review evidence consists of exact-object source reconstruction/inspection plus independent execution of the changed pure decision logic and its adversarial cases. This is recorded as a degraded-review environment limitation, not a correction-requiring finding; no claim is made that the reviewer independently reran the full 38-case file. Reopen if stronger isolated checkout/multi-agent execution becomes available and the canonical independence gate can be tightened.

## Authority and next gate

The code findings from Issue #510 are mechanically closed. This review PASS authorizes no integration by itself. If repository authority separately permits publication, it must be squash-only and noncanonical unless separately canonicalized. After any clean reviewed publication, a fresh trusted-main pre-secret `py_compile` plus full `--self-test` gate and one fresh credentialed evaluator/recorder episode remain mandatory before any new provider conclusion.

Mandatory reopen condition: `MULTI_AGENT_OR_ISOLATED_CONTEXT_AVAILABLE` for stronger independent execution, or any drift in judged head/blob/base/path identities.
