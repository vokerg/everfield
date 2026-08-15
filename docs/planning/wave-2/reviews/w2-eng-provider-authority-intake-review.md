# W2-ENG-PROVIDER-AUTH-REV-01 — Provider authority intake security review

**Schema:** `provider_authority_intake_review_v1`  
**Issue:** #348  
**Task class:** `REQUIRED_SECURITY_AUTHORITY_REVIEW`  
**Review mode:** `DEGRADED_SINGLE_AGENT`, fresh review episode distinct from the producer episode.  
**Claim:** `5302583219`  
**Base:** `main@92204cb2e58c792ef4199fe3562ca2192096f5c0`  
**Canonical binding:** Bootstrap #6 terminal binding `5245368879`; program blob `e3120ec203c4156328770aa86c12fbb7187966dc`; activation `413e729e8d2d5ac2eb138903f3f2ace07283b23e` remains in current-main ancestry.  
**Judged producer:** Issue #347 terminal `5302579528`, work `f118e8d5036995424c94fd5520cb2b863cbe8b1a`, exact head `d47f73254eaa97d0280c748c05dc230b70c7dc6c`, draft PR #349 at the same exact head.  
**Disposition:** **PASS_AUTHORITY_INTAKE_BOUNDARY_WITH_EXTERNAL_TRIGGER — 0 BLOCKER / 0 MAJOR / 0 MINOR**.

Issue #347 / branch `planning/issue-347` was treated as immutable judged input. This review trusts the exact packet only as a non-secret, fail-closed provider-authority intake boundary and exact current `AUTHORITY_REQUIRED_EXACT` diagnosis. It grants no provider permission, credential validity, engine empirical PASS, engine ranking/selection, implementation/readiness, legal/platform/release, verification-PASS, decision, canonical, or integration authority.

## 1. Exact packet and run binding

The producer packet is exactly six commits ahead of frozen source `main@92204cb2e58c792ef4199fe3562ca2192096f5c0` and changes only the eight routed authority-intake/evidence/handoff surfaces. The review bound the following exact producer identities:

- workflow blob: `9606ffdfb5fdeae0aa5e8bd6562767aab9adeb17`;
- probe blob: `a1d4d61e10741e54f5e3a2e32fa85a0d4f48c625`;
- input-contract blob: `a4c40fe1f77ec9557dbe0d76af3e947f188c96be`;
- producer-report blob: `4e69dea00497397872a107572cdd1f4dd143a205`;
- presence-evidence blob: `43c944ec8ff76754cfdb71b426b6a984eb6d3b23`;
- self-test blob: `89ac54c8beea583e745800cd454472504f4747b7`;
- run-identity blob: `0883d81c40e4e947c03bc4ee0074b5867ccf7c5b`;
- producer-handoff blob: `fc1fd4e2f4ea7dcb926b198603aff2c999a63995`.

GitHub Actions run `31888759105` executed from trigger SHA `7e98635c6a28a9ebbb388035ee7631777c682be4`, completed successfully, produced evidence commit `0358a3cd97178b78959b293383af2c66da0451ff`, and uploaded artifact `9247964188` with digest `sha256:a41d14e386ca61ea5624791177626dac1d40846f23f9558a3c0242e14fbf19c6`. The live job record shows every producer step completed successfully. The generated evidence identities and artifact digest match the terminal producer handoff.

## 2. Security and authority attacks

### A1 — Secret-value leakage: PASS

The workflow maps provider secrets only through boolean presence expressions of the form `${{ secrets.NAME != '' }}`. The executable probe accepts only those boolean presence flags and non-secret mode selectors; it has no credential-value command-line or environment interface. The actual run log contains blank mode selectors and `false` presence booleans only. The only checkout credential displayed by the runner is GitHub's masked `***` representation. The persisted and uploaded bundle contains only presence JSON, deterministic self-test JSON, and run identity/hash material. No provider credential value, credential-bearing URL/header, or hash of a provider secret was observed in the code, committed evidence, artifact-producing path, or run log.

### A2 — GitHub expression/environment semantics: PASS

The producer uses the boolean result of secret non-emptiness comparison, not the secret value itself. This is consistent with current GitHub Actions expression/secrets semantics: an unset secret resolves as an empty string, the comparison produces a boolean, and expressions may populate job environment values. The live run independently confirms the expected rendered values: every declared provider presence variable is `false` and no secret value is rendered.

### A3 — Fail-open authority: PASS

The probe structurally cannot turn workflow success or presence into effective authority. A complete Unity mode becomes only `INPUT_PRESENT_UNVALIDATED`; a complete Unreal mode becomes only `INPUT_PRESENT_UNVALIDATED`; both together become only `BOTH_INPUT_SETS_PRESENT_VALIDATION_REQUIRED`. `effective_provider_authority_validated` and `five_candidate_empirical_successor_unlocked` remain hard-false in this presence-only path. The workflow additionally asserts those fail-closed values before evidence publication.

### A4 — Unity account/license separation: PASS

The contract and executable distinguish service-account authentication from editor-license authorization. `service_account_serial` requires account presence plus separate serial material; offline and floating modes remain presence-only until later effective license validation. The packet never treats account authentication as a valid Unity `6000.5.6f1` editor license. Current Unity CLI semantics independently support this separation between unattended service-account authentication and licensing/activation workflows.

### A5 — Unreal entitlement/content identity: PASS

The packet does not treat repository-local `GITHUB_TOKEN` as EpicGames/UnrealEngine entitlement. A future dedicated token must prove effective access to the exact EpicGames/UnrealEngine 5.8 identity, while a preseed route requires a supplied location plus expected SHA-256 followed by retrieval/version/content validation. Current Epic source-access semantics independently require the relevant Epic/GitHub account linking, authorization/EULA path, and EpicGames organization access; token presence alone is therefore correctly insufficient.

### A6 — Deterministic negative fixtures: PASS

The self-test records all required negatives as true: empty input is exact authority-required; empty input never unlocks; partial Unity input is rejected; one provider never unlocks; both complete presence sets remain unvalidated; presence never becomes effective authority. The live workflow ran this exact self-test and its separate fail-closed assertion successfully.

### A7 — Exact current diagnosis / no overclaim: PASS

The machine record and prose say only that the **declared intake contract** currently has unset/invalid Unity and Unreal modes and that all declared input-presence signals measured false. The packet does not claim that arbitrary repository, owner, or provider credentials do not exist outside this workflow's observable contract. `AUTHORITY_REQUIRED_EXACT` is therefore bounded to the measured contract rather than inflated into a global absence claim.

### A8 — Branch/workflow trust: PASS

The producer handoff explicitly forbids treating the mutable draft branch as a trusted credential destination or treating future workflow success as authority. Any later credential-consuming/effective-validation path must have its own trusted/reviewed lifecycle before it can unlock W2-ENG. The current workflow's `contents: write` permission was used only to persist the non-secret evidence packet on the producer task branch before terminalization; it does not create integration or provider authority.

### A9 — Historical engine evidence / authority inflation: PASS

Issue #82 terminal `5276916603` remains the source of 5 candidates × 10 scenarios = 50 historical `NOT_RUN` cells. The producer packet preserves all 50 and promotes zero. No reduced Bevy/Defold/Godot comparison, S1–S10 PASS, engine ranking/selection, gameplay/high-throughput implementation, production/readiness, provider/legal/platform/release, verification-PASS, decision, canonical, or integration authority is created.

### A10 — Producer PR state: PASS

Draft PR #349 is exact at producer head `d47f73254eaa97d0280c748c05dc230b70c7dc6c` and is explicitly visibility/review only. Draft state, mergeability, and `REVIEW_READY` do not grant publication authority. Any eventual `main` publication remains a separately authorized squash-only action.

## 3. Severity accounting

```yaml
blocker_findings: 0
major_findings: 0
minor_findings: 0
correction_requiring_minor_findings: 0
review_trust_mode: DEGRADED_SINGLE_AGENT
```

No material security, fail-closed, provenance, or authority defect was found in the bounded current-state intake/diagnosis. Same-model review is recorded explicitly as degraded independence rather than represented as human or separately isolated review.

## 4. Exact external/configuration reopen predicate

The trusted current packet remains terminal at `AUTHORITY_REQUIRED_EXACT`. Repository-local work must not manufacture a replacement task while the actual provider inputs are absent.

The frontier may reopen only when an authorized operator supplies, through an appropriately trusted lifecycle:

1. exactly one declared Unity mode for baseline `6000.5.6f1` — `service_account_serial`, `offline_file`, or `floating`; and
2. exactly one declared Unreal Engine 5.8 mode — `github_token` or `preseed`.

That configuration event is **not** provider validation. After it occurs, a fresh reviewed effective-validation/content-identity episode must prove Unity license authorization and exact Unreal 5.8 authorized/preseed identity without secret leakage. Only a later trusted result that validates both providers may route one fresh five-candidate W2-ENG empirical episode.

## 5. Review result

Disposition is `PASS_AUTHORITY_INTAKE_BOUNDARY_WITH_EXTERNAL_TRIGGER`. The exact Issue #347 packet is trustworthy only as the reviewed fail-closed intake boundary and current external-authority diagnosis described above.

No remediation successor, generic CI/environment task, reduced empirical comparison, or integration action is authorized by this review. Any eventual publication to `main` remains separately authorized and squash-only.