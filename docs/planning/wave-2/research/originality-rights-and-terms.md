# W2-REM-RIGHTS-01 — Corrected originality, reference-use, provider-terms, and rights policy

**Mission:** `W2-REM-RIGHTS-01` / Issue #95  
**Source mission:** `W2-RIGHTS-01` / Issue #80  
**Source work/head:** `3c262cbf767633e0ca42f6bdf387e262056b4fb0`  
**Source report blob:** `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**Source terminal status:** Issue #80 comment `5270525266`  
**Independent pre-gate review:** Issue #80 comment `5271490456`  
**Canonical foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Machine-readable policy:** `docs/planning/wave-2/research/originality-rights-policy.yaml` blob `aaee1e14ee6d5a2ca55447e56611f0bfc58e8de6`  
**External source recheck:** 2026-08-12  
**State:** `PLANNING_REVISION / EVIDENCE_REQUIRED / NONCANONICAL`

## 1. Scope and authority limits

This revision preserves the producer's core separation between:

1. provenance — where the exact artifact came from;
2. provider/contract permission — what exact provider/product/account terms governed an input/output episode;
3. originality/reference-use evidence — what exact source/reference purpose and similarity/adversarial evidence apply;
4. release-sensitive rights state — whether the declared project evidence policy is satisfied for one exact release scope; and
5. copyrightability/protectability — a separate jurisdiction- and facts-specific question.

It does **not** provide legal advice, decide infringement, certify ownership or copyrightability, authorize release, select production tooling, resolve implementation readiness, or canonicalize any rule merely by existing on this branch.

`ArtifactIdentity.rights_or_terms_state` remains the durable shared state from Wave 1. `CLEAR` means only that the exact declared project evidence requirement is satisfied for the exact declared scope. It is not an attorney opinion, warranty, proof of exclusivity, proof of non-infringement, or proof that copyright exists.

The fail-closed invariant remains:

> A release/package scope cannot be satisfied while any applicable retained artifact is `UNKNOWN`, `RESTRICTED`, or `QUARANTINED`, or while required provenance/terms/license/originality evidence is missing, stale, `NOT_RUN`, `INCONCLUSIVE`, or otherwise unsatisfied.

## 2. What this remediation changes

The frozen Issue #80 candidate remains immutable provenance. This revision corrects only the three pre-gate findings:

- **PG-RIGHTS-M01:** the prior `OriginalityReviewRecord` did not bind reference purpose, allowed/prohibited reuse, or exact current rights/terms evidence as required by Wave-1 §18. This revision introduces `ReferenceUseRecord` as the exact join identity across candidate artifact, references, purpose, reuse permissions, rights/terms/license evidence, scope, risk policy, and originality review.
- **PG-RIGHTS-M02:** the prior release gate delegated originality-review applicability to an undefined “risk policy.” This revision binds exact `ORP-RISK-v1` and compiles a deterministic `OriginalityCheckPlan` before execution/assessment. Unknown/unmatched applicability fails closed.
- **PG-RIGHTS-m01:** stale evidence previously allowed either `UNKNOWN` or `QUARANTINED` without precedence. This revision defines deterministic state precedence and reason codes; stale evidence alone derives `UNKNOWN(STALE_REQUIRED_EVIDENCE)`, while an independent stronger conflict/risk trigger can derive `QUARANTINED` or `RESTRICTED`.

No source candidate branch is edited and no formal `W2-REV-01` disposition is claimed.

## 3. Canonical authority-chain alignment

Wave 1 establishes one requirement-to-decision chain:

```text
TaskContract / TaskClaimContract
  -> EvidenceRequirement under PolicyEpoch
  -> CheckPlan for exact candidate/base/scope
  -> ExecutionEvidenceEnvelope attempts/artifacts
  -> EvidenceSatisfaction
  -> Review / Verification
  -> Decision / readiness / integration eligibility
```

Rights/originality evidence follows the same chain. `ORP-R1-2026-08-12` is a planning policy candidate, and `ORP-RISK-v1` is the exact originality applicability policy inside it. A release-sensitive task must instantiate/version an `EvidenceRequirement` that cites that policy (or a later reviewed successor), compile applicability before execution, and retain exact evidence/result identities. No release-time actor may simply decide that a previously required check was “optional.”

Changing a judge-affecting policy or applicability rule creates a new policy/requirement identity; it does not rewrite historical evidence.

## 4. Exact reference-use identity — correction of PG-RIGHTS-M01

### 4.1 `ReferenceUseRecord`

The normative field contract is machine-readable in policy blob `aaee1e14ee6d5a2ca55447e56611f0bfc58e8de6`. The conceptual form is:

```yaml
ReferenceUseRecord:
  record_id: <content-addressed over all identity fields>
  candidate_artifact_id: <ArtifactIdentity>
  reference_artifact_ids: [<exact ArtifactIdentity or exact external source identity>]
  origin_class: <typed>
  reference_class: <typed>
  reference_purpose: <typed>
  allowed_reuse: []
  prohibited_reuse: []
  provider_terms_refs: []
  license_or_permission_refs: []
  current_rights_research_refs: []
  release_scope_ref: <exact>
  originality_risk_policy_id: ORP-RISK-v1
  originality_evidence_requirement_ref: <exact>
  originality_review_ref: <exact>
  freshness_requirement_refs: []
```

A record is **not reusable** if any identity field changes. In particular, the same candidate bytes reviewed as a `FACT_RESEARCH` reference under one permission/release scope cannot reuse that record when the purpose becomes `DIRECT_INCORPORATION`, when the allowed/prohibited reuse set changes, or when the release scope changes.

This closes the prior alias path where an originality result could be carried into a materially different reference-use context merely because `candidate_artifact_id` was unchanged.

### 4.2 Reference-use taxonomy

The producer taxonomy is preserved, now with exact record binding:

| Reference class | Meaning | Default project posture |
|---|---|---|
| `NONE_DECLARED` | no external reference declared for the artifact episode | still requires generated/project-corpus originality policy where applicable; absence of a declared source is not proof of originality |
| `FACTUAL_OR_FUNCTIONAL` | facts, public rules, compatibility requirements, functional/mechanical ideas | reference/citation allowed; source-specific expression is not silently incorporated |
| `GENERAL_CONCEPTUAL` | genre, broad theme, high-level design concept, generic mood vocabulary | traceable conceptual reference; escalate if output converges on distinctive expression |
| `STYLE_OR_CREATOR_NAMED` | named creator/work/style as directional reference | traceable reference with mandatory stronger originality evidence for release-sensitive expressive output |
| `EXPRESSION_SPECIFIC` | distinctive text, image, composition, character, music, dialogue, story passage, code structure | research may be retained if permitted; incorporation requires exact permission/basis and stronger review |
| `DIRECT_ASSET_OR_CODE` | third-party file, code, font, model, texture, audio, dataset, package | exact identity + license/permission/obligation evidence required; public visibility is not a reuse license |
| `MARK_LIKENESS_PERSONA` | trademark, trade dress, logo, real-person likeness/voice/persona | unresolved release-sensitive use stays blocked pending applicable evidence |
| `CONFIDENTIAL_PRIVATE_RESTRICTED` | private, NDA, leaked, access-controlled, or purpose-restricted material | `RESTRICTED` by default; provider transmission and broader release use require exact authority |
| `PUBLIC_DOMAIN_CLAIM` | material believed to be public domain | `UNKNOWN` until exact source/basis, jurisdiction/scope, and required freshness evidence are recorded |

This is a **project risk-control taxonomy**, not a statement that every named-style reference is unlawful or that every factual/functional use is legally safe.

### 4.3 `LicenseOrPermissionRecord`

The release chain previously referred to license/permission refs without defining their minimum evidence shape. The corrected policy defines a bounded record containing source/artifact identity, authority source, license/permission kind, version or grant date, observed time, allowed/prohibited uses, obligations, jurisdiction/scope, expiration/recheck trigger, and immutable evidence ref.

Missing/ambiguous permission cannot support `CLEAR`; the intended release scope must fit within the recorded allowed use/scope; unsatisfied obligations cannot support `CLEAR`.

## 5. Provider/tool terms remain a separate authority question

Provider output allocation does not answer input authority, originality, third-party rights, copyrightability, or release suitability. Provider data-use/training/confidentiality rules also remain separate from output allocation.

The exact provider/product/account/order/renewal epoch must be bound to each generation or ingestion episode when provider permission matters. A model name, operator location, marketing page, or assumption that “this is a business account” is not contract evidence.

### 5.1 Current first-party source recheck

The remediation independently rechecked the producer's load-bearing current facts before preserving them. No material drift requiring a changed policy conclusion was found on 2026-08-12.

| Source ID | First-party source/version used | Normalized fact used by this planning policy | Applicability |
|---|---|---|---|
| `OPENAI-EEA-INDIVIDUAL-2026-01-16` | OpenAI Europe Terms of Use, updated 2026-01-16 | individual EEA/Swiss/UK path; user responsible for input rights; as between user/OpenAI and to extent permitted by law user retains input rights/owns output; output may be non-unique; OpenAI may use content to provide/maintain/develop/improve services; account training opt-out exists; third-party services/output can have separate terms | `CONDITIONAL`; only if the exact episode is actually governed by that contract/account state |
| `OPENAI-BUSINESS-2026-01-01` | OpenAI Services Agreement, updated 2025-12-01, effective 2026-01-01 | business/developer/API path; customer retains input rights/owns output as between parties to extent permitted by law; customer is responsible for input rights/output use; OpenAI states Customer Content is not used to develop/improve Services unless customer explicitly agrees | `CONDITIONAL`; exact agreement/order/service epoch required |
| `OPENAI-SERVICE-TERMS-2026-06-12` | OpenAI Service Terms, updated 2026-06-12 | service-specific/API indemnity terms are conditional and contain exclusions; they are not project-wide legal clearance | `CONDITIONAL` on exact applicable agreement/service |
| `OPENAI-USAGE-2025-10-29` | OpenAI Usage Policies, effective 2025-10-29 | current policy includes IP-rights restrictions and can change | applies only through the governing service/contract path; freshness required |
| `GITHUB-TOS-2026-04-27` | GitHub Terms of Service, effective 2026-04-27 | standard ToS content license and AI-feature input/output license are distinct; the Section J AI-feature opt-out does not erase the separate Section D content license; AI output may resemble third-party/open-source material and users remain responsible for reviewing/validating output and needed permissions | `CONDITIONAL`; exact account/customer agreement, repository visibility, product, and settings must be bound |
| `GITHUB-AI-CONTRACT-PATH-2026-03-05` | GitHub customer-terms update history / current customer agreements | direct business generative-AI contract routing changed for new/renewed subscriptions beginning 2026-03-05; prior/other paths require exact subscription/contract epoch | `NOT_ADMITTED_AS_USED`; no GitHub AI release-generation episode is established here |
| `USCO-AI-COPYRIGHTABILITY-2025-01-29` | U.S. Copyright Office Part 2 announcement, 2025-01-29 | bounded U.S.-specific research: sufficient human-authored expression/selection/arrangement/modification can matter; mere prompting alone is not treated as sufficient authorship by the Office's stated analysis; AI assistance does not automatically bar a larger human-authored work | `LEGAL_RESEARCH_ONLY`; not global ownership/non-infringement clearance |

Authoritative URLs retained from the producer research:

- OpenAI Europe Terms of Use: `https://openai.com/da-DK/policies/eu-terms-of-use/`
- OpenAI Services Agreement: `https://openai.com/policies/services-agreement/`
- OpenAI Service Terms: `https://openai.com/en-GB/policies/service-terms/`
- OpenAI Usage Policies: `https://openai.com/policies/usage-policies/`
- GitHub Terms of Service: `https://docs.github.com/en/site-policy/github-terms/github-terms-of-service`
- GitHub customer terms/update history: `https://github.com/customer-terms/updates`
- U.S. Copyright Office Part 2 announcement: `https://www.copyright.gov/newsnet/2025/1060.html`

These are current-source observations, not proof of which account contract governs a future Everfield episode. A later freshness trigger requires a new immutable citation/evidence record rather than silently treating this observation as perpetual.

## 6. Originality applicability policy — correction of PG-RIGHTS-M02

### 6.1 Exact policy identity

The exact policy is `ORP-RISK-v1`, inside machine-readable policy blob `aaee1e14ee6d5a2ca55447e56611f0bfc58e8de6`.

It recognizes the following evidence kinds:

- `EXACT_IDENTITY`;
- `NORMALIZED_IDENTITY`;
- `KNOWN_REFERENCE_COMPARISON`;
- `NEAR_DUPLICATE`;
- `TARGETED_EXTERNAL_SEARCH`;
- `JUDGMENT_REVIEW`; and
- `QUALIFIED_LEGAL_REVIEW`.

Each kind compiles to `REQUIRED`, `CONDITIONAL`, or `NOT_APPLICABLE` **before** originality execution or release assessment.

Fail-closed compiler rules are normative:

- missing policy identity -> `UNKNOWN_POLICY`;
- unknown origin/reference class -> `UNKNOWN_POLICY`;
- missing exact release scope for release-sensitive use -> `UNKNOWN_POLICY`;
- no matching rule -> `UNKNOWN_POLICY`;
- an unresolved conditional trigger is treated as `REQUIRED`, not silently false.

If multiple rules apply, the most restrictive applicability wins per evidence kind (`REQUIRED > CONDITIONAL > NOT_APPLICABLE`).

### 6.2 Bounded rule intent

The policy intentionally distinguishes evidence applicability from legal truth:

- generated artifacts with no declared external reference still require exact/normalized/project-known-reference and near-duplicate evidence; external search/judgment/legal review are trigger-dependent;
- factual/conceptual references require exact source identity and known-reference comparison, with stronger evidence triggered by expressive convergence/material signals;
- named-style and expression-specific references require the stronger exact/normalized/known-reference/near-duplicate/targeted-search/judgment set for release-sensitive expressive use;
- direct third-party assets/code primarily require exact identity plus license/permission and obligation evidence; similarity tooling does not replace license authority;
- marks/likeness/persona uses require stronger comparison/review and can trigger qualified legal interpretation where material to release;
- confidential/restricted material is `RESTRICTED` first and cannot become release-clear merely by running similarity checks;
- a public-domain claim requires exact source/status/jurisdiction evidence and current targeted authoritative research; age or lack of notice is not a sufficient shortcut.

`QUALIFIED_LEGAL_REVIEW` is **conditional**, not an assertion that every artifact requires counsel. It is triggered only where the project policy identifies an unresolved legal interpretation material to the intended release/use.

### 6.3 `OriginalityCheckPlan`

The compiler output binds:

```yaml
OriginalityCheckPlan:
  policy_id: ORP-RISK-v1
  evidence_requirement_ref: <exact>
  candidate_artifact_id: <exact>
  reference_use_record_ref: <exact>
  release_scope_ref: <exact>
  applicable_rule_ids: []
  evidence_kind_applicability: {}
  conditional_trigger_resolutions: {}
```

`NOT_APPLICABLE` is resolved before execution. `NOT_RUN` is an execution result and never aliases `NOT_APPLICABLE`. A required `NOT_RUN`/`INCONCLUSIVE` cannot satisfy the evidence requirement.

### 6.4 Corrected `OriginalityReviewRecord`

```yaml
OriginalityReviewRecord:
  review_id: <stable>
  candidate_artifact_id: <exact>
  reference_use_record_ref: <exact>
  policy_id: ORP-RISK-v1
  evidence_requirement_ref: <exact>
  check_plan_ref: <exact>
  reference_corpus_ref: <content-addressed set>
  exact_duplicate_checks: []
  normalized_identity_checks: []
  known_reference_checks: []
  near_duplicate_checks: []
  targeted_external_search_refs: []
  judgment_panel_ref: <optional/required per compiled plan>
  qualified_legal_review_ref: <optional/required per compiled plan>
  material_signals: []
  blind_spots: []
  result: NO_MATERIAL_SIGNAL_FOUND | MATERIAL_SIGNAL | NEAR_DUPLICATE | EXACT_DUPLICATE | INCONCLUSIVE | NOT_RUN
  legal_conclusion: NONE
```

The `reference_use_record_ref` must bind the same candidate artifact and exact reference-use context. This makes purpose/permission/scope part of the originality authority rather than an adjacent prose assumption.

## 7. Similarity evidence remains escalation evidence, never a clearance oracle

The producer's staged evidence posture is preserved:

1. exact identity/hash/source matches;
2. normalized identity where media permits;
3. known-reference comparison against exact attached references, prior accepted Everfield artifacts, and quarantined/blocked artifacts whose expression must not be reintroduced;
4. versioned near-duplicate mechanisms with retained algorithm/threshold/coverage limits;
5. targeted external search where the compiled policy requires it;
6. structured judgment using `JudgmentPanelRecord` semantics where required, with evaluator fingerprints/correlation/trust limits; and
7. qualified legal interpretation only where the compiled policy's material trigger requires it.

A score or “no match found” may trigger or inform review. It may not prove originality, independent creation, non-infringement, copyrightability, or release suitability; it may not cure missing provenance/license/provider evidence. Material disagreement remains visible rather than averaged into a PASS.

## 8. Deterministic rights-state derivation — correction of PG-RIGHTS-m01

### 8.1 Precedence

For one exact release scope, the corrected derivation uses this precedence:

1. `RESTRICTED` — evidence establishes a known scope limitation/prohibited use or the recorded permission is narrower than intended release scope.
2. `QUARANTINED` — an unresolved material conflict/risk exists, such as material similarity, an unpermitted exact/near-direct third-party match, active license/terms conflict, credible complaint/contrary source, or unresolved mark/likeness/persona/confidentiality risk.
3. `UNKNOWN` — required evidence is missing/stale/incomplete/unknown, provider contract or policy applicability is unknown, or required originality evidence is `NOT_RUN`/`INCONCLUSIVE`.
4. `CLEAR` — only when no higher-precedence state matches and all required evidence/freshness/license obligations are satisfied with no unresolved material signal.

Every derived state retains reason codes and a derivation trace.

### 8.2 Stale evidence rule

Stale required provider/legal evidence **by itself** derives:

```text
UNKNOWN(STALE_REQUIRED_EVIDENCE)
```

A stale event does not rewrite the historical assessment; `prior_assessment_ref` preserves the earlier state/evidence. If the same assessment also has an independent stronger trigger — for example a newly discovered material similarity conflict — the normal precedence yields `QUARANTINED` while retaining the stale-evidence reason in history/diagnostics. A known explicit permission restriction yields `RESTRICTED`.

This gives one mechanical outcome rather than permitting implementations to choose `UNKNOWN` or `QUARANTINED` for the same facts.

## 9. Corrected release-sensitive assessment

```yaml
ReleaseRightsAssessment:
  assessment_id: <stable>
  artifact_id: <exact ArtifactIdentity>
  release_scope_ref: <exact>
  reference_use_record_refs: []
  provider_terms_refs: []
  license_or_permission_refs: []
  originality_policy_id: ORP-RISK-v1
  originality_check_plan_refs: []
  originality_evidence_satisfaction_refs: []
  freshness_requirement_refs: []
  unresolved_triggers: []
  reason_codes: []
  prior_assessment_ref: <optional exact historical assessment>
  derived_rights_or_terms_state: CLEAR | RESTRICTED | QUARANTINED | UNKNOWN | NOT_APPLICABLE
  derivation_trace: []
```

For every release/package artifact where rights/terms are applicable, the gate requires at minimum:

1. exact `ArtifactIdentity`;
2. complete provenance;
3. exact `ReferenceUseRecord` for every material reference/use context;
4. exact provider/product/account contract evidence if provider permission/data-use terms matter;
5. fresh provider terms for the actual episode epoch;
6. exact license/permission/public-domain-basis evidence for incorporated external material;
7. all license/permission obligations satisfied for the exact release scope;
8. exact `ORP-RISK-v1` (or reviewed successor) policy and compiled originality check plan;
9. all `REQUIRED` originality evidence satisfied; no required `NOT_RUN`/`INCONCLUSIVE`;
10. no unresolved material similarity or other higher-precedence risk trigger;
11. no unresolved mark/likeness/persona/confidentiality trigger where applicable;
12. all required freshness records current; and
13. a reconstructable derivation to the final state.

A low score, provider output assignment, provider indemnity clause, public repository visibility, public accessibility, lack of a search result, or “AI generated” label is never a standalone route to `CLEAR`.

## 10. Freshness and immutable evidence

Wave-1 `FreshnessRequirement` remains controlling for `PROVIDER_TERMS` and `LEGAL_IP_RESEARCH`.

Each relied-upon freshness record must bind:

- immutable evidence/citation ref;
- observed date;
- source version/scope;
- invalidation triggers;
- typed rerequest predicate; and
- dependent decision refs.

Provider terms reopen when provider/product/account/subscription/customer-contract class, relevant data-use/training controls, contract/policy version/effective date, order/renewal epoch, third-party service path, or material ownership/input/indemnity/data-use clause changes.

Legal/IP research reopens when target jurisdiction/distribution/commercial scope changes, authoritative guidance changes, the project makes a stronger claim than the existing source supports, or a complaint/conflict/new source creates contrary evidence.

No arbitrary maximum age is imposed where source version/effective date/event is the meaningful invalidation trigger. Staleness makes the dependent assessment OPEN/`UNKNOWN` unless a higher-precedence independent trigger yields `RESTRICTED`/`QUARANTINED`.

## 11. Provider/input admission remains separate from release clearance

A source may be lawful/appropriate to inspect but not appropriate to transmit to a specific provider under confidentiality, license, purpose, or provider data-use terms. Therefore admission evaluates both:

1. whether the project may inspect/use/incorporate the source for the declared purpose; and
2. whether the project may transmit it to the exact provider/product/account under the governing source/provider terms.

Admission for one provider product/account does not inherit to another. `ChatGPT individual`, `Business/Enterprise`, API, a third-party model surfaced inside another product, connector/browse output, and GitHub AI contract paths require their own exact applicable evidence when used in a release-sensitive generation chain.

Third-party output never inherits a wrapper provider's output-allocation clause; it retains its own origin/terms/source requirements.

## 12. Failure modes retained and corrected controls

| Failure mode | Corrected control |
|---|---|
| provider assignment treated as release clearance | provider/contract allocation remains orthogonal; never sole state authority |
| reference-purpose laundering | `ReferenceUseRecord.record_id` changes when purpose/reuse/scope/evidence changes |
| originality-result reuse across permission scope | review binds exact `reference_use_record_ref`; mismatch rejects reuse |
| undefined “risk policy” silently marks review optional | exact `ORP-RISK-v1` compilation before execution; unknown/unmatched fails closed |
| low-similarity Goodharting | similarity evidence escalation-only; required evidence/coverage gaps retained |
| missing/ambiguous license | exact `LicenseOrPermissionRecord`; missing/unsatisfied cannot clear |
| stale provider/legal source | deterministic `UNKNOWN(STALE_REQUIRED_EVIDENCE)` plus prior-state retention |
| stale evidence plus independent material conflict | higher precedence `QUARANTINED`; both reasons retained |
| known permission narrower than release | `RESTRICTED`; cannot silently broaden scope |
| reference/artifact laundering through new locator | shared `ArtifactIdentity` + reference-use provenance; wrapper hash/name does not reset state |
| correlated AI reviewers mistaken for independence | `JudgmentPanelRecord` evaluator/correlation/trust semantics remain required |
| scope/jurisdiction drift | exact release scope + freshness reopen |

## 13. Deterministic self-check cases

Policy blob `aaee1e14ee6d5a2ca55447e56611f0bfc58e8de6` declares eight mechanical cases:

- changing reference purpose while reusing an originality result -> reject; new `ReferenceUseRecord` required;
- changing release scope while reusing the same record -> reject;
- no matching originality policy rule -> `UNKNOWN_POLICY`, never `CLEAR`;
- unresolved conditional trigger -> treat evidence as `REQUIRED`;
- stale terms only after prior `CLEAR` -> `UNKNOWN(STALE_REQUIRED_EVIDENCE)` with prior assessment retained;
- stale terms plus material-similarity conflict -> `QUARANTINED` with both facts retained;
- explicit license scope restriction dominates missing optional similarity tooling -> `RESTRICTED`;
- low similarity score with missing license -> cannot clear.

These are planning-policy conformance examples, not proof that a future implementation exists or is correct.

## 14. Remaining open questions

The source producer's legitimate unknowns remain open rather than being papered over:

- exact OpenAI/GitHub account/customer-contract classes for future release-content episodes;
- whether GitHub AI/Copilot ever contributes a release artifact and under which exact contract/subscription epoch;
- exact external asset/code/font/audio/model/data licenses and packaging obligations;
- calibrated media-specific similarity algorithms/thresholds and their blind spots;
- which concrete artifact/scope triggers require qualified legal interpretation;
- target release jurisdictions/storefronts and resulting trademark, likeness/persona, moral-rights, database-right, or other local questions;
- protected-evidence handling for confidential licenses/legal analysis; and
- formal aggregate `W2-REV-01` review.

These unknowns intentionally prevent stronger release/readiness claims; they do not invalidate the bounded planning policy.

## 15. Remediation acceptance check

Against Issue #95 acceptance criteria:

- immutable provenance to Issue #80 work/status/review: **PASS**;
- PG-RIGHTS-M01 reference-use authority corrected: **PASS**;
- PG-RIGHTS-M02 exact risk-policy/applicability authority corrected: **PASS**;
- PG-RIGHTS-m01 deterministic stale-evidence state corrected: **PASS**;
- purpose/allowed-prohibited reuse/current rights/terms/scope/artifact/originality bound by one exact reference-use identity: **PASS**;
- changed use/scope cannot reuse prior record identity: **PASS**;
- applicability compiles `REQUIRED | CONDITIONAL | NOT_APPLICABLE` before execution; unknown fails closed: **PASS**;
- required evidence remains in requirement -> check-plan -> evidence -> satisfaction chain: **PASS**;
- current provider/legal source facts rechecked and kept conditional/bounded: **PASS**;
- similarity/provider assignment/public visibility shortcuts remain forbidden: **PASS**;
- no unsupported legal conclusion added: **PASS**;
- release/implementation/canonicalization authority: **not claimed**;
- formal independent review: **W2-REV-01 remains required**.

**Remediation candidate disposition:** `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`, subject to self-review of the exact final branch state and later required independent `W2-REV-01`.
