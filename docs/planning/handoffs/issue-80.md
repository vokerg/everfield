# Issue #80 handoff — W2-RIGHTS-01

**Mission:** `W2-RIGHTS-01`  
**Issue:** #80  
**Branch:** `planning/issue-80`  
**Ownership generation:** Issue #80 comment `5270356007`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Research report:** `docs/planning/wave-2/research/originality-rights-and-terms.md`  
**Research report blob:** `bda0551c446c93492c9d8e809d087d592dfcdae3`  
**External research observed:** `2026-08-12T19:47:33+02:00`  
**Intended terminal state:** `REVIEW_READY`  
**Required formal review:** `W2-REV-01`

## Completed work

Produced the bounded Wave-2 rights/originality/provider-terms research candidate required by Issue #80.

The report defines:

- four orthogonal evidence questions: provenance, provider/contract permission, originality/similarity signal, and release-sensitive rights state;
- copyrightability/protectability as a separate jurisdiction/facts question rather than a provider-output shortcut;
- `RightsProvenanceRecord`, `ProviderTermsRecord`, `OriginalityReviewRecord`, and `ReleaseRightsAssessment` schemas;
- a reference-use taxonomy covering factual/functional, generalized conceptual, named-style/creator references, expression-specific references, direct assets/code, marks/likeness/persona, confidential/restricted material, and public-domain claims;
- a first-party provider/tool terms matrix for current OpenAI individual EEA terms, OpenAI business/API terms, OpenAI service terms/conditional API indemnity, OpenAI usage policies, current GitHub ToS/AI terms contract paths, and a bounded U.S. Copyright Office AI-copyrightability research anchor;
- an explicit rule that provider output allocation/assignment is not originality, non-infringement, copyrightability, or release clearance;
- provider input/data-use/training permissions as a separate admission concern, including the material difference between standard GitHub ToS content-use rights and OpenAI business customer-content improvement defaults;
- staged exact/normalized/near-duplicate/known-reference/targeted-search/judgment originality evidence;
- escalation-only similarity scores that cannot independently clear release;
- fail-closed `UNKNOWN` / `RESTRICTED` / `QUARANTINED` transitions and clearing rules;
- artifact-level release gate criteria;
- exact provider/product/account-contract admission states and no inherited admission between provider products/contracts;
- freshness/reopen triggers for provider terms, account/order/renewal/data-use state, target jurisdiction, legal authority changes, licenses, complaints, and release-scope changes.

## External authority packet embedded in report

The report itself acts as the immutable normalized citation record once frozen by blob. It records exact source IDs, version/effective dates, observed date, normalized facts consumed, authoritative URLs, conditional applicability, and freshness triggers.

Load-bearing current first-party sources checked:

- OpenAI Europe Terms of Use — updated 2026-01-16;
- OpenAI Services Agreement — updated 2025-12-01, effective 2026-01-01;
- OpenAI Service Terms — updated 2026-06-12;
- OpenAI Usage Policies — effective 2025-10-29;
- GitHub Terms of Service — effective 2026-04-27;
- GitHub Customer Terms update history / Additional Product Terms — current 2026 contract routing including the 2026-03-05 generative-AI business-contract transition;
- U.S. Copyright Office Part 2 announcement — 2025-01-29, used only as bounded U.S.-specific legal research.

No operator location, plan name, model name, or marketing page is treated as proof of the actual provider account contract. Exact generation episodes must bind their real provider/product/account/order/renewal terms before release-sensitive reliance.

## Key policy conclusions

1. Provider assignment/ownership language cannot set `rights_or_terms_state=CLEAR` by itself.
2. A low similarity score or absence of a search match cannot establish originality or non-infringement.
3. Third-party output remains subject to its own source/terms evidence rather than inheriting a wrapper provider's output allocation.
4. Publicly accessible or public-repository content is not presumed licensed for incorporation.
5. Unknown provider contracts, missing/ambiguous licenses, incomplete provenance, stale terms, and release-scope drift fail closed.
6. Material similarity, license conflicts, unresolved mark/likeness/confidentiality issues, third-party-output uncertainty, or credible contrary evidence quarantine the artifact.
7. `CLEAR` means only that the declared project evidence policy is satisfied for the declared scope; it is not legal advice or a warranty.
8. U.S. Copyright Office human-authorship guidance is recorded as jurisdiction-specific research and is not generalized into an Everfield global copyright conclusion.

## Self-review

Final producer self-review against Issue #80 acceptance criteria and canonical Wave-1 constraints:

- unresolved BLOCKER: 0;
- unresolved MAJOR: 0;
- correction-requiring MINOR: 0;
- source/version/date captured for current provider/legal research: PASS;
- reference-use taxonomy: PASS;
- provider terms matrix: PASS;
- exact account/product applicability kept conditional where not evidenced: PASS;
- provider data-use/training differences captured: PASS;
- provenance separated from originality and rights/release state: PASS;
- similarity score prevented from becoming legal truth or sole clearance: PASS;
- unknown/restricted/quarantined material cannot silently ship: PASS;
- quarantine/escalation/clearing rules: PASS;
- provider/legal freshness and reopen triggers: PASS;
- no unsupported global legal conclusion: PASS;
- no release, implementation-readiness, or canonicalization authority claimed: PASS;
- required formal review remains `W2-REV-01`: PASS.

A producer self-review correction was made before this handoff: the initial draft did not explicitly capture provider input/data-use/training differences. The final report now records them and makes them part of provider/input admission and release gating.

## Remaining risks / open questions

- the exact OpenAI and GitHub account/customer-contract classes for future release-content episodes are not established by this planning research and must be captured per generation/storage epoch;
- no GitHub Copilot/AI release artifact is assumed to exist; if introduced, its exact contract path and subscription/renewal epoch must be recorded;
- media-specific similarity mechanisms and thresholds are not selected yet and require evidence without becoming clearance oracles;
- actual third-party asset/code/font/audio/model/data licenses and their packaging obligations remain future artifact-specific evidence;
- global copyright, trademark, likeness/persona, moral-rights, database-right, and other jurisdiction-specific legal questions remain scoped/open until material to a release decision;
- protected handling for confidential licenses/legal analyses remains to be designed;
- formal aggregate adversarial review has not run.

## Next action

Cold-review the exact branch diff against current `main`, verify ownership remains uncontested, and publish owner schema-3 `STATUS(REVIEW_READY)` for the exact final branch head and report/handoff blobs if clean. Then freeze `planning/issue-80`.

Do **not** interpret this producer research, self-review, a PR, or any future noncanonical main integration as the formal `W2-REV-01` disposition or as legal/release clearance.
