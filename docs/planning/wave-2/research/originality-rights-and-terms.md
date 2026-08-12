# W2-RIGHTS-01 — Originality, reference-use, provider-terms, and rights research

**Mission:** `W2-RIGHTS-01` / Issue #80  
**Branch:** `planning/issue-80`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation:** `docs/planning/WAVE-1-FOUNDATIONS-v1.md` blob `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**External research observed:** `2026-08-12T19:47:33+02:00`  
**Task class / decision state:** `PLANNING_RESEARCH / EVIDENCE_REQUIRED`  
**Required independent review:** `W2-REV-01`

## 1. Purpose, scope, and authority limits

This research candidate defines a project policy for:

- reference-use classification;
- generated/external content provenance;
- provider/tool terms evidence;
- originality/similarity review;
- quarantine and escalation;
- release-sensitive rights questions; and
- freshness/reopen behavior.

It does **not** provide legal advice, decide whether a particular work infringes, decide copyright subsistence or ownership in every jurisdiction, decide trademark/privacy/publicity rights, or certify any asset for release merely because a provider assigns output rights or a similarity tool returns a low score.

The intended invariant is narrower and machine-enforceable:

> A release candidate may not silently contain an artifact whose required provenance, provider terms, third-party license/permission, or scoped rights state is `UNKNOWN`, `RESTRICTED`, or `QUARANTINED`.

`ArtifactIdentity.rights_or_terms_state` from the Wave-1 foundation remains the durable project gate. A `CLEAR` state means only **the declared project evidence policy is satisfied for the declared scope**. It is not an attorney opinion, a warranty of non-infringement, proof of exclusivity, or proof that copyright exists.

## 2. Canonical constraints carried forward

The Wave-1 foundation already establishes the following controlling rules:

1. Every retained artifact uses one durable `ArtifactIdentity`; a second locator/hash cannot bypass provenance or quarantine state.
2. `rights_or_terms_state` is one of `CLEAR | RESTRICTED | QUARANTINED | UNKNOWN | NOT_APPLICABLE`.
3. Generated build-time candidates gain no runtime/canonical authority before normal validation and review.
4. Provider-terms and legal-IP research are freshness-sensitive external evidence classes.
5. A stale required terms/legal record makes the dependent decision `INCONCLUSIVE`/OPEN rather than silently valid forever.
6. Multiple AI calls/model names do not automatically create independent originality evidence.
7. No prose, aggregate score, provider ownership clause, or similarity score can upgrade `EVIDENCE_REQUIRED` to a verified release decision by itself.

## 3. Separate the four questions

The project must never collapse these into one “rights score.”

| Question | Example | Evidence class | Can another class answer it? |
|---|---|---|---|
| **Provenance** | Where did this exact artifact come from? | artifact/source/generation lineage | No. A low similarity score does not establish provenance. |
| **Provider/contract permission** | What terms governed the exact generation/upload/tool use? | exact provider/account/product terms | No. Provider assignment does not prove originality or legal protectability. |
| **Originality/similarity signal** | Does the artifact materially resemble known or discovered material? | duplicate/near-duplicate/search/judgment evidence | No. “No match found” is not legal clearance or internet-wide originality proof. |
| **Release-sensitive rights state** | May project policy admit this artifact into a declared release scope? | derived from required records + unresolved risk triggers | No single provider clause, model result, or score may decide alone. |

A fifth question — **copyrightability/protectability** — is jurisdiction- and facts-specific and remains separate from the release-control state. A work can have uncertain protectability without that fact alone proving infringement, and a provider assignment cannot create rights that applicable law does not recognize.

Provider **data-use/training/confidentiality permissions** are also separate from output ownership. An account contract that assigns output can still impose materially different rules on how input/repository/content may be used by the provider. That difference is especially relevant before feeding confidential, licensed, or purpose-restricted material into a generative service.

## 4. Project record types

### 4.1 `RightsProvenanceRecord`

```yaml
RightsProvenanceRecord:
  record_id: <stable>
  artifact_id: <ArtifactIdentity>
  origin_class: PROJECT_NATIVE | GENERATED_PROVIDER | EXTERNAL_REFERENCE | EXTERNAL_ASSET | THIRD_PARTY_OUTPUT | LICENSED_MATERIAL | PUBLIC_DOMAIN_CLAIM | UNKNOWN
  produced_by_or_source_ref: <exact>
  input_artifact_refs: []
  prompt_or_generation_envelope_ref: <optional exact>
  reference_refs: []
  provider_terms_refs: []
  provider_account_contract_ref: <exact or UNKNOWN>
  license_or_permission_refs: []
  source_observed_at: <date/time>
  scope: <research | build-time | distribution | release target>
  provenance_state: COMPLETE | INCOMPLETE | CONFLICTING
```

### 4.2 `ProviderTermsRecord`

```yaml
ProviderTermsRecord:
  terms_id: <stable>
  provider: <name>
  product_or_service: <exact>
  account_contract_class: <exact or UNKNOWN>
  terms_url: <authoritative>
  terms_version_or_effective_date: <exact>
  observed_at: <date/time>
  normalized_facts_used: []
  data_use_or_training_facts: []
  additional_terms_refs: []
  applicability: APPLIES | CONDITIONAL | NOT_APPLICABLE | UNKNOWN
  invalidation_triggers: []
```

The account/contract class is not inferred from an operator's geographic location, a model name, or a provider marketing page. Business/API/enterprise and individual services may use different agreements, including materially different content-use/training defaults.

### 4.3 `OriginalityReviewRecord`

```yaml
OriginalityReviewRecord:
  review_id: <stable>
  candidate_artifact_id: <exact>
  reference_corpus_ref: <content-addressed set>
  exact_duplicate_checks: []
  near_duplicate_checks: []
  targeted_external_search_refs: []
  judgment_panel_ref: <optional>
  material_signals: []
  blind_spots: []
  result: NO_MATERIAL_SIGNAL_FOUND | MATERIAL_SIGNAL | NEAR_DUPLICATE | EXACT_DUPLICATE | INCONCLUSIVE | NOT_RUN
  legal_conclusion: NONE
```

### 4.4 `ReleaseRightsAssessment`

```yaml
ReleaseRightsAssessment:
  assessment_id: <stable>
  artifact_id: <exact>
  release_scope_ref: <exact>
  provenance_record_ref: <exact>
  provider_terms_refs: []
  license_or_permission_refs: []
  originality_review_ref: <optional/required by risk policy>
  unresolved_triggers: []
  derived_rights_or_terms_state: CLEAR | RESTRICTED | QUARANTINED | UNKNOWN | NOT_APPLICABLE
  derivation_trace: []
  freshness_refs: []
  reopen_conditions: []
```

This record derives the `ArtifactIdentity.rights_or_terms_state`; it does not replace `ArtifactIdentity`.

## 5. Reference-use taxonomy

Reference use is classified at ingestion and again if a source is later incorporated more directly than originally declared.

| Class | Meaning | Default project posture | Release-sensitive trigger |
|---|---|---|---|
| `FACTUAL_OR_FUNCTIONAL` | facts, public rules, functional/mechanical ideas, compatibility requirements | reference allowed with citation/provenance; do not copy protected expression unnecessarily | direct expressive copying or source-specific assets/code |
| `GENERAL_CONCEPTUAL` | genre, broad theme, high-level design concept, generic mood vocabulary | reference allowed with provenance | output converges on distinctive source expression |
| `STYLE_OR_CREATOR_NAMED` | named creator/work/style as a directional reference | allowed only as a traceable reference; escalated originality review for release artifacts materially influenced by it | distinctive characters/composition/text/audio/visual expression appears in output |
| `EXPRESSION_SPECIFIC` | distinctive text, image, composition, character, music, dialogue, story passage, source code structure | research/reference may be retained if lawful; incorporation requires explicit license/permission/public-domain basis or separate scoped determination | any direct or near-direct incorporation without evidence |
| `DIRECT_ASSET_OR_CODE` | third-party file, code, font, model, texture, audio, dataset, package | `UNKNOWN` until exact license/permission and obligations are recorded; then scoped state derived | missing/ambiguous license, incompatible obligation, prohibited distribution |
| `MARK_LIKENESS_PERSONA` | trademark, trade dress, logo, real-person likeness/voice/persona | `UNKNOWN`/`QUARANTINED` for release use until the applicable issue is specifically resolved | commercial/release use or authenticity-confusing depiction |
| `CONFIDENTIAL_PRIVATE_RESTRICTED` | private, confidential, NDA, leaked, access-controlled, or purpose-restricted material | `RESTRICTED` by default; do not feed into providers or release pipeline absent exact permission and provider/data terms | any use outside authorized purpose/scope |
| `PUBLIC_DOMAIN_CLAIM` | material believed to be public domain | `UNKNOWN` until jurisdiction/source/basis is recorded; never infer from age or lack of notice alone | jurisdiction or status ambiguity |

The taxonomy is a **project risk-control policy**, not a statement that every named-style reference is unlawful or that every factual/functional use is legally safe.

## 6. Current provider/tool terms evidence

The table records first-party terms checked on 2026-08-12. Applicability to actual Everfield generation episodes remains conditional unless the exact account/product contract is bound in the corresponding generation envelope.

| Terms ID | Current first-party source/version | Normalized facts consumed | Everfield applicability now |
|---|---|---|---|
| `OPENAI-EEA-INDIVIDUAL-2026-01-16` | OpenAI Europe Terms of Use, updated 2026-01-16 | user is responsible for Content and must have rights/licenses/permissions for Input; as between user/OpenAI and to extent permitted by law user retains Input rights and owns Output; Output may be non-unique; Third Party Services/Output have their own terms; OpenAI may use Content to provide/maintain/develop/improve services and the individual account offers a training opt-out; output must be evaluated for the use case | `CONDITIONAL` — applies only to episodes actually governed by these individual EEA/Swiss/UK terms; exact account/data-control state still belongs in episode evidence |
| `OPENAI-BUSINESS-2026-01-01` | OpenAI Services Agreement, updated 2025-12-01, effective 2026-01-01 | agreement is for API/Enterprise/Business and other business/developer services; Customer retains Input rights/owns Output as between parties to extent permitted by law; Customer is responsible for Input rights and Output use; OpenAI states it will not use Customer Content to develop/improve Services unless Customer explicitly agrees; applicable policy version can depend on agreement/order/renewal/service timing | `CONDITIONAL` — exact business/account/order contract not established here |
| `OPENAI-SERVICE-TERMS-2026-06-12` | OpenAI Service Terms, updated 2026-06-12 | API IP indemnity exists only under the applicable Agreement and has material exclusions, including known/likely infringement, ignored safeguards, certain modifications/combinations, lack of Input rights, trademark-related trade/commerce claims, and Third Party Offering output | `CONDITIONAL`; **never** general project clearance |
| `OPENAI-USAGE-2025-10-29` | OpenAI Usage Policies, effective 2025-10-29 | current policies prohibit attempts to infringe others' IP rights and may be updated | applies to OpenAI-service use according to the governing agreement/policy version; freshness required |
| `GITHUB-TOS-2026-04-27` | GitHub Terms of Service, effective 2026-04-27 | user owns/responsible for their content; must have right to post third-party content and comply with licenses; under the standard ToS the license granted to GitHub/Affiliates for `Your Content` includes service development/improvement and AI/ML training; public-repository settings grant service-level viewing/forking permissions; individual AI Feature inputs/outputs also have an AI-development-use license unless opted out, while the ToS states that opt-out does not remove the separate Section D content license; GitHub AI Feature output can resemble third-party/open-source material and user must determine needed licenses and review/validate output | `CONDITIONAL` — standard ToS path is current research; exact GitHub account/customer agreement, repository visibility, and relevant settings must be bound before a release-sensitive contract/data-use claim |
| `GITHUB-AI-CONTRACT-PATH-2026-03-05` | GitHub Customer Terms updates + Additional Product Terms | individual/non-business Copilot use can be governed by ToS Section J; business/enterprise contract paths differ; for new/renewed direct GitHub business subscriptions from 2026-03-05 GitHub Generative AI Services Terms replace the deprecated Copilot Product Specific Terms path | `NOT_ADMITTED_AS_USED` — no Copilot/other GitHub AI generation episode is established by this mission; if used later, exact product/license/subscription date is mandatory evidence |
| `USCO-AI-COPYRIGHTABILITY-2025-01-29` | U.S. Copyright Office, Copyright and AI Part 2 announcement, 2025-01-29 | under U.S. Copyright Office analysis, generative-AI output is protectable only where sufficient expressive elements are human-authored; human-authored arrangement/modification can matter; mere prompting by itself is not enough; AI assistance does not automatically bar protection of a larger human-authored work | `LEGAL_RESEARCH_ONLY`; U.S.-specific and not an Everfield ownership/non-infringement conclusion |

### 6.1 Exact authoritative URLs

- `OPENAI-EEA-INDIVIDUAL-2026-01-16`: `https://openai.com/da-DK/policies/eu-terms-of-use/`
- `OPENAI-BUSINESS-2026-01-01`: `https://openai.com/en-GB/policies/services-agreement/`
- `OPENAI-SERVICE-TERMS-2026-06-12`: `https://openai.com/en-GB/policies/service-terms/`
- `OPENAI-USAGE-2025-10-29`: `https://openai.com/policies/usage-policies/`
- `GITHUB-TOS-2026-04-27`: `https://docs.github.com/en/site-policy/github-terms/github-terms-of-service`
- `GITHUB-AI-CONTRACT-PATH-2026-03-05`: `https://github.com/customer-terms/updates` and `https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features`
- `USCO-AI-COPYRIGHTABILITY-2025-01-29`: `https://www.copyright.gov/newsnet/2025/1060.html`

These normalized source records are frozen by this report's Git blob. The live URLs remain external authorities and must be rechecked when a freshness trigger fires.

### 6.2 Data-use terms are an input-admission concern

A reference can be lawful to inspect yet still be inappropriate to upload to a particular provider under its license, confidentiality, data-use, or purpose restrictions. Therefore provider admission must evaluate both:

1. whether the project may use/incorporate the source; and
2. whether the project may transmit that source to the selected provider/account under the exact provider and source terms.

This is why `CONFIDENTIAL_PRIVATE_RESTRICTED` defaults to `RESTRICTED`, and why moving between individual/business/provider products requires a new terms record rather than inheriting prior admission.

## 7. Provider-output ownership is not release clearance

The project MUST treat the following propositions separately:

1. **Provider contract allocation:** a provider may state that, as between provider and customer/user and to the extent permitted by law, the customer/user owns or is assigned output rights.
2. **Input authority:** the user/customer may still be responsible for having rights to the supplied input/reference material.
3. **Provider data-use rights:** provider contracts/settings may differ materially in how input/output/repository content can be used for service or model development.
4. **Output uniqueness:** providers may expressly warn that output is not unique or may resemble third-party content.
5. **Third-party material:** third-party outputs, packages, code, assets, or services may carry separate terms/licenses.
6. **Copyrightability:** applicable law may or may not recognize protectable authorship in a particular generated artifact.
7. **Non-infringement:** neither provider assignment nor copyrightability answers whether a particular output infringes third-party rights.
8. **Release suitability:** Everfield's project gate must evaluate the exact artifact, provenance, terms, licenses, similarity signals, and declared release scope.

Therefore these are invalid shortcuts:

- `provider_says_user_owns_output -> CLEAR`;
- `provider_offers_IP_indemnity -> CLEAR`;
- `low_similarity_score -> CLEAR`;
- `no_search_result -> CLEAR`;
- `AI_generated -> public_domain`;
- `publicly_accessible -> licensed_for_incorporation`;
- `repository_is_public -> third_party_content_is_free_to_reuse`.

## 8. Originality and similarity evidence policy

### 8.1 Goal

The goal is to find material warning signals and retain an auditable review trail. It is **not** to prove universal originality or render a legal infringement judgment.

### 8.2 Minimum staged checks

The `OriginalityReviewRecord` may include media-appropriate stages:

1. **Exact identity:** byte/content hash and exact known-source matches.
2. **Normalized identity:** normalized text/code/token or metadata-stripped equivalents where appropriate.
3. **Near-duplicate heuristics:** perceptual image/audio/code/text similarity mechanisms whose algorithm/version/threshold are recorded.
4. **Known-reference comparison:** compare against the exact content-addressed reference corpus attached to the generation/task.
5. **Targeted external search:** when risk triggers justify it, search distinctive fragments/features against authoritative/public sources and retain query/time/result provenance.
6. **Judgment review:** structured AI/evaluator panel may assess dimensions such as distinctive composition, character design, phrasing, melody, or code structure, but its correlation/fingerprint/trust limits must be explicit.

### 8.3 Scores are escalation-only

A similarity score or classifier threshold may:

- trigger extra review;
- route an artifact to quarantine;
- prioritize targeted search;
- identify a likely duplicate.

It may **not**, by itself:

- prove copyright infringement;
- prove non-infringement;
- prove originality;
- prove independent creation;
- waive a missing license;
- clear an unknown provider contract; or
- authorize release.

If tools disagree materially, result is `INCONCLUSIVE` or `MATERIAL_SIGNAL`, not an averaged-away PASS.

### 8.4 Reference corpus identity

At minimum the comparison corpus includes:

- all explicit source/reference artifacts attached to the generation episode;
- prior accepted Everfield artifacts that could be accidentally duplicated;
- quarantined/blocked artifacts whose expression must not be reintroduced under a new locator;
- any specific external work identified by a material-similarity signal.

An internet-wide absence of matches is not asserted; coverage gaps remain in the record.

## 9. Quarantine and escalation state machine

### 9.1 Default transitions

```text
new artifact
  -> provenance/terms/license evidence complete? no -> UNKNOWN
  -> explicit restricted material or prohibited scope? yes -> RESTRICTED
  -> unresolved material risk trigger? yes -> QUARANTINED
  -> declared project evidence policy satisfied for scope -> CLEAR
```

A later freshness or new-evidence event may transition `CLEAR -> UNKNOWN` or `CLEAR -> QUARANTINED`. Historical evidence is retained; it is not rewritten.

### 9.2 Mandatory `UNKNOWN` triggers

- generation provider/product/account contract class is missing for a release artifact where provider permission matters;
- external asset/code/license source is missing or ambiguous;
- claimed public-domain status lacks recorded basis/scope;
- a provider/source terms version required by policy is stale;
- the artifact's provenance chain is incomplete or conflicting;
- the release jurisdiction/distribution scope expands beyond the evidence scope.

### 9.3 Mandatory `QUARANTINED` triggers

- exact/near-direct match to a third-party source without adequate incorporation permission;
- material similarity to a named/reference work that cannot be bounded by existing evidence;
- a license/terms conflict with intended distribution or modification;
- trademark/likeness/persona/confidentiality issue relevant to planned use remains unresolved;
- third-party output is present but its own terms/source rights are not resolved;
- a credible complaint or newly discovered source contradicts the current state;
- a previously clear artifact becomes dependent on stale provider/legal evidence.

### 9.4 `RESTRICTED`

Use when evidence supports only a narrower scope than release, for example:

- internal research reference only;
- no redistribution;
- no commercial use;
- attribution/share-alike/source-disclosure obligation not yet compatible with intended packaging;
- confidential/private purpose-limited material.

`RESTRICTED` material can remain retained as provenance/evidence, but cannot silently enter a broader release package.

### 9.5 Clearing quarantine

A quarantine may clear only through a new exact evidence package that disposes the trigger, such as:

- exact permission/license evidence and fulfilled obligations;
- independently regenerated/reworked artifact with a new identity and no inherited material signal;
- corrected source/provider terms evidence;
- bounded targeted review showing the signal was a false match within the declared policy scope;
- scoped qualified legal determination where project policy requires legal interpretation.

Changing a filename/hash wrapper without changing the underlying artifact or evidence does not clear quarantine.

## 10. Release-sensitive gate

For every artifact included in a release/package scope where rights/terms are applicable:

1. exact `ArtifactIdentity` exists;
2. exact provenance record exists and is complete;
3. actual generation/tool provider contract is identified if relevant;
4. provider terms evidence is fresh for that exact product/account/service epoch;
5. provider input/data-use terms permit the exact source material to be transmitted for the declared purpose;
6. all external incorporated material has exact license/permission/public-domain-basis evidence;
7. license obligations are compiled into packaging/distribution requirements and satisfied;
8. risk policy says whether originality review is required, and required review is not `NOT_RUN`/`INCONCLUSIVE`;
9. no material unresolved similarity signal exists;
10. no applicable mark/likeness/persona/confidentiality trigger remains unresolved;
11. `ArtifactIdentity.rights_or_terms_state == CLEAR` for the exact release scope;
12. the derivation is reconstructable and has explicit freshness/reopen triggers.

If a release candidate contains one required artifact in `UNKNOWN`, `RESTRICTED`, or `QUARANTINED`, the rights gate is **not satisfied**. The project may narrow/remove the artifact or release scope, obtain new evidence, or record a later owner/legal policy decision through the normal authority chain; it may not fabricate clearance.

## 11. Provider/tool admission policy for an AI-built project

Because providers and tool contracts can change independently, every generative or ingestion tool that contributes a release artifact must be admitted by exact contract evidence.

### 11.1 Admission states

- `ADMITTED_FOR_RESEARCH` — may produce disposable/non-release planning artifacts under known terms.
- `ADMITTED_FOR_BUILD_CANDIDATES` — may produce candidates, but release still requires artifact-level rights/provenance policy.
- `ADMITTED_FOR_RELEASE_PIPELINE` — exact account/product terms, provider data-use settings, and project data/use constraints are current for the declared scope.
- `NOT_ADMITTED` — provider/product terms unknown, stale, incompatible, or not yet evaluated.

### 11.2 No inherited admission

Admission for `ChatGPT individual` does not imply admission for `API`, `Business`, a third-party model exposed inside another product, or third-party output returned through browsing/connectors. Admission for one GitHub AI contract path does not imply another customer/subscription path.

The exact provider/service/account contract and relevant data-use controls belong in the generation envelope. A human-readable model name is insufficient identity.

## 12. U.S. AI copyrightability research — bounded use

The U.S. Copyright Office's January 29, 2025 Part 2 announcement says its current analysis requires sufficient human-authored expressive elements for protection of generative-AI output; human-authored material perceivable in output and creative arrangement/modification can qualify, while mere provision of prompts does not by itself. AI assistance also does not automatically bar protection of a larger human-authored work.

Project consequence:

- do not assert that provider-assigned output is necessarily copyright-protected;
- record human-authorship/selection/arrangement/modification evidence if a later U.S. copyright-protectability claim depends on it;
- do not infer that uncertain/nonexistent copyright protection makes an artifact automatically safe to use, globally public-domain, or non-infringing;
- target-jurisdiction and actual artifact facts remain required for any release-sensitive legal conclusion.

No conclusion is made here about Everfield's eventual copyright registration, protectability in Denmark/EU or other jurisdictions, or infringement exposure.

## 13. Alternatives considered

### A. Provider-ownership-only policy

**Rule:** if provider terms assign Output, mark artifact clear.

**Rejected.** It conflates bilateral provider allocation with input authority, uniqueness, provider data-use rights, third-party rights, copyrightability, and release suitability. Current OpenAI and GitHub contract paths themselves demonstrate why the exact provider/account terms matter.

### B. Similarity-score clearance

**Rule:** if a model/perceptual score is below threshold, mark clear.

**Rejected.** Coverage is incomplete, tools are probabilistic/correlated, legal similarity is context-specific, and a score cannot cure missing provenance/license evidence.

### C. Ban all external references

**Rule:** no external references may be used at all.

**Rejected as the default.** It is unnecessarily broad for factual/functional/general research, discards useful provenance, and does not solve accidental similarity. High-risk classes are instead traced, bounded, and quarantined when needed.

### D. Orthogonal provenance + terms + originality + release gate

**Adopted planning candidate.** It preserves machine-auditable state, allows broad research without silent incorporation, and fails closed on unknown/restricted material without pretending the project has a universal legal oracle.

## 14. Observability and audit requirements

The evidence chain should retain at minimum:

- exact artifact ID/content hash;
- origin class and source/generation lineage;
- exact provider, product/service, account-contract class, terms epoch, and relevant data-use settings;
- input/reference artifact IDs;
- license/permission IDs and obligations;
- declared use/release scope;
- originality check algorithms/versions/thresholds/corpora/queries/results;
- evaluator fingerprints and correlation/trust limits for judgment review;
- every quarantine/restriction event and disposition;
- terms/legal source observation date/version/scope;
- release assessment derivation and reopen triggers.

If protected/private evidence is required, retain a protected evidence envelope rather than leaking the evidence into ordinary public artifacts.

## 15. Failure modes and controls

| Failure mode | Consequence | Control |
|---|---|---|
| provider assignment treated as legal clearance | third-party/copyrightability issues hidden | orthogonal records; provider clause never sole gate |
| provider account class ignored | wrong output/data-use terms assumed | exact account/product/order/renewal terms binding |
| confidential/reference input sent under incompatible provider terms | source license/confidentiality breach risk | input-admission check includes provider data-use terms/settings |
| low similarity score Goodharted | false negative becomes release PASS | escalation-only score semantics; coverage/blind spots retained |
| reference laundering | quarantined source reappears under new hash/name | ArtifactIdentity provenance refs + blocked corpus comparison |
| stale provider terms | output created under wrong/unknown contract assumption | provider terms freshness + generation-epoch binding |
| third-party output laundering | browse/connector result treated as provider-owned | origin `THIRD_PARTY_OUTPUT`; own terms/source record required |
| public-repo assumption | publicly viewable material treated as freely reusable | exact license/permission required for incorporation |
| license obligation loss | attribution/source/disclosure/share obligations missed | compile obligations into release/package checks |
| AI legal overclaim | model invents global answer | scoped research states; unresolved legal interpretation stays OPEN |
| duplicate AI reviewers | correlated calls mistaken for independence | JudgmentPanelRecord correlation/trust fields |
| legal-scope drift | prior assessment silently applied to new territory/storefront/use | release scope bound + reopen on scope change |

## 16. Freshness requirements

### Provider terms

Recheck when any of these changes:

- provider or product/service;
- account/subscription/customer-contract class;
- repository visibility or provider data-use/training settings where relevant;
- terms effective/version date;
- order/renewal date where it selects policy version;
- model/service moves through a third-party offering;
- provider changes output ownership, input rights, indemnity, data-use, acceptable-use, or third-party-output clauses;
- a release artifact was generated under a different terms epoch from the one currently evaluated.

### Legal/IP research

Recheck when:

- target jurisdiction or distribution/commercial scope changes;
- authoritative office/court/statute guidance materially changes;
- the project makes a stronger claim than the source supports (for example copyright registration or ownership rather than internal risk gating);
- a complaint, takedown, conflict, or newly discovered source creates contrary evidence.

No arbitrary maximum age is assigned where contract version/effective date or legal event is the meaningful invalidation trigger.

## 17. Open questions

1. Which exact OpenAI account/product contract governs each future release-content generation pipeline: individual EEA terms, Business/Enterprise, API, or another agreement/order?
2. Which OpenAI/GitHub provider data-use/training controls and repository visibility states apply to project content at each generation/storage epoch?
3. Will GitHub AI Features/Copilot generate any release artifact, and if so under which exact individual/customer/subscription terms epoch?
4. Which external asset/code/font/audio/model/data licenses will be admitted, and how will their obligations compile into package/release checks?
5. Which media-specific duplicate/near-duplicate mechanisms provide useful warning coverage without becoming false clearance oracles?
6. What risk classes require targeted external search and/or qualified legal determination before a release state can become `CLEAR`?
7. Which release jurisdictions/storefronts will make trademark, likeness/persona, moral-rights, database-right, or other local questions material?
8. What project policy is appropriate if a valuable AI-generated artifact has no known infringement signal but protectability/exclusivity is uncertain?
9. What protected-evidence mechanism should hold confidential license agreements or legal analysis without leaking them into public project state?

## 18. Reopen conditions

Reopen this candidate or dependent rights states if:

- any load-bearing provider terms/policy source changes;
- actual provider/account contract contradicts the conditional matrix here;
- repository visibility/data-use controls change in a way relevant to project inputs/content;
- a new release provider/tool is introduced without terms admission;
- a license/permission is revoked, expires, or is discovered to have different scope;
- a material similarity/duplicate signal or third-party complaint appears;
- a new legal authority materially changes a load-bearing legal research proposition;
- target jurisdiction/distribution/commercial scope expands;
- W2-REV-01 finds a BLOCKER/MAJOR against this policy.

## 19. Producer acceptance check

Against Issue #80 acceptance criteria:

- source/version/date for current provider/legal sources: **PASS**;
- reference-use taxonomy: **PASS**;
- provider terms matrix: **PASS**, with actual account applicability explicitly conditional/unknown where not evidenced;
- provider data-use/training differences captured as input-admission evidence: **PASS**;
- originality/similarity evidence policy: **PASS**;
- similarity score prevented from becoming legal truth/sole clearance: **PASS**;
- provenance separated from originality and release-sensitive rights state: **PASS**;
- unknown/restricted/quarantined material cannot silently satisfy release gate: **PASS**;
- quarantine/escalation/reopen rules: **PASS**;
- freshness triggers: **PASS**;
- unsupported legal conclusion: **none intentionally made**;
- release/canonicalization/implementation authority: **not claimed**;
- required formal independent review: **W2-REV-01 remains required**.

**Producer disposition:** `REVIEW_READY_CANDIDATE / EVIDENCE_REQUIRED`. The report is ready for independent adversarial review after terminal provenance is bound; it is not a verified legal or release decision.
