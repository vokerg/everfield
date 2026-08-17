# Issue #516 — corrected Unity license-exit required-review handoff

## Identity

- Mission: `W2-ENG-PROVIDER-UNITY-LICENSE-EXIT-REV-02`
- Task class: `REQUIRED_REVIEW`
- Claim: Issue #516 comment `5312726772`
- Branch: `planning/issue-516`
- Base/current main at claim: `538b8a3b46b8b095bc43206d4a0ad4fdc151616a`
- Canonical binding: Issue #6 comment `5245368879`
- Canonical program blob: `e3120ec203c4156328770aa86c12fbb7187966dc`
- Canonicality: `NOT_CANONICAL`
- Trust mode: `DEGRADED_SINGLE_AGENT`

## Frozen judged candidate

- producer Issue #512 terminal: `5312707781`, `REVIEW_READY`
- producer PR: #514, draft
- producer head: `d333d00c2e9af4e7711245feae156334b6a01a85`
- validator blob: `69d45fa7bde9bd7879460ac661bac83228f113a6`
- producer handoff blob: `88aeb3f97424e9a07704e4aadd912b677921041c`
- frozen predecessor head: `defa1fa6c2cc8dd39a84a864b34b36c47dbaa77b`
- triggering review Issue #510 terminal: `5311555047`, `CHANGES_NEEDED`

The judged branch was not modified by this reviewer.

## Review result

Disposition: `PASS_BOUNDED_PROVIDER_UNITY_LICENSE_EXIT_REVISION`.

Findings: 0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR. One non-correction reviewer-runtime limitation is recorded in the report.

Both Issue #510 findings are mechanically closed:

- exit `3` preserves authentication-or-authorization uncertainty in both stage and durable blocker;
- the same pure `unity_license_status_decision` path is consumed by `validate_unity` and deterministic tests, with editor progression gated directly on its output.

Fresh adversarial replay of the changed pure decision logic covered exit 0 active/inactive, exit 3, exit 4 valid/invalid envelope, exit 6, timeout/transient, unknown nonzero, and a conflicting top-level `active` marker. Every nonzero path kept authentication/license/progression false.

## Scope and evidence

Main-to-candidate compare is seven ahead / zero behind with merge base exactly current main and only three paths: frozen Issue #508 handoff provenance, Issue #512 handoff, and the validator. Frozen #508 producer-to-candidate compare contains only the validator plus Issue #512 handoff. No workflow, generated historical evidence, policy, S7, or unrelated content path is in the revision delta.

The reviewer fetched the exact repository validator object by blob `69d45fa7...`, inspected production and self-test source, and independently executed the changed pure decision logic. Issue #512 exact-byte terminal verification for the same blob records `py_compile` PASS and full `--self-test` PASS 38/38 with provider credential variables absent. The reviewer runtime did not expose connector-fetched bytes as a local filesystem object, so the full-file commands were not repeated locally; this degraded evidence limitation is explicit and is a mandatory reopen condition if stronger isolated checkout/multi-agent execution becomes available.

## Review artifact

`docs/planning/wave-2/reviews/w2-eng-provider-unity-license-exit-revision-review.md`

## Authority boundary and next gate

Review PASS does not grant integration-by-review. Any publication requires separate repository authority and squash-only integration. After any clean reviewed publication, one fresh trusted-main pre-secret `py_compile` + full `--self-test` gate and one fresh credentialed evaluator/recorder episode remain mandatory before any new provider conclusion.

No provider authentication/PASS, Unity license, engine selection, implementation/readiness, production/commercial/legal/platform/release, verification-PASS, decision, canonicalization, or canonical authority is granted by this review.
