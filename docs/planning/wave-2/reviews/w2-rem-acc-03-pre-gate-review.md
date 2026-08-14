# W2-PG-REM-ACC-03 — independent scoped review of XAG 102–106 atomization

**Mission:** `W2-PG-REM-ACC-03` / Issue #242  
**Reviewed producer:** `W2-REM-ACC-03` / Issue #240  
**Reviewed exact head:** `bccd22e35f84a5894586d9494e1963ebdef7dc02`  
**Reviewed work:** `f4671c3c295437a64d82ffc51e228c826fcce40e`  
**Reviewed PR:** #241  
**Review trust mode:** `DEGRADED_SINGLE_AGENT_FRESH_REVIEW_EPISODE`  
**Disposition:** `CHANGES_NEEDED`

## 1. Immutable input reconstruction

The review consumed Issue #240 only at the frozen terminal identities. The three producer artifacts reproduce the declared Git blobs:

- `docs/planning/wave-2/research/accessibility-current-requirements.md` → `3fd5eae49f26da2f357f8a1d337a3f3f3ef0f8fa`;
- `docs/planning/wave-2/research/accessibility-requirements-policy.yaml` → `9c21efdeed2ddff96d6cc1d0ccf2893b9304ccc4`;
- `docs/planning/handoffs/issue-240.md` → `d7bbf3ba74cf4d88cc3935072590e66280bcbea7`.

The exact predecessor policy on reviewed base `cc973dd5e758bef20ba588ab1440ae82ec1ec2b6` reproduces blob `d4f934d1731800b3966adeae82c4a57b9af737b8`. PR #241 is open/draft with exact head `bccd22e35f84a5894586d9494e1963ebdef7dc02` and changes only the declared accessibility report, accessibility policy, and Issue #240 handoff. No branch mutation or unrelated scope leakage was observed.

## 2. Current-source reconstruction

The reviewer independently re-read the current first-party Microsoft XAG v3.2 implementation-guideline surfaces for XAG 102–106 on 2026-08-14:

- XAG 102: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102`
- XAG 103: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103`
- XAG 104: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104`
- XAG 105: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105`
- XAG 106: `https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/106`

All five current English pages still report `Last updated on 2026-03-04`. The review found no source-version drift that invalidates the bounded packet wholesale.

## 3. Mechanical reconstruction

The declared expected inventories reproduce arithmetically and by unique stable identity:

| page | declared / reproduced expected IDs |
|---|---:|
| XAG 102 | 12 |
| XAG 103 | 8 |
| XAG 104 | 29 |
| XAG 105 | 5 |
| XAG 106 | 23 |
| **new total** | **77** |

The exact integrated predecessor contributes the declared 11 XAG 101 plus 17 XAG 107 expected IDs, so the composed count is `28 + 77 = 105`.

The structural validator contract correctly requires identity/set/count equality, nonempty conditional triggers, reference integrity, summary-only XAG 108–123, `NOT_RUN` empirical evidence, `mapping_complete: false`, and OPEN blocker state. Those preserved fail-closed aggregate conditions remain intact.

However, the advertised semantic-drift protection is not mechanically sufficient. The validator accepts any nonempty `required_semantics` and any nonempty trigger; it does not bind the source-significant predicates below to immutable semantic expectations. Consequently the current packet can report `xag_102_106_inventory: PASS` while source semantics have been weakened or made non-deterministic. The review therefore cannot return CLEAN.

## 4. Findings

### PG-REM-ACC03-M01 — MAJOR — XAG 106 source obligations are weakened by invented/narrowing predicates

**Affected records:**

- `XAG106-CONTEXT-CHANGE-INITIATED-NARRATED`
- `XAG106-PROPER-NAME-PRONUNCIATION`

**Current first-party semantics:**

1. XAG 106 says that context change **should be player initiated**, and after a context change the player should be notified via narration of the new context. The source does not add a `where possible` exception to the player-initiation obligation.
2. XAG 106 says to provide a mechanism for the player to understand how to pronounce a proper name, technical term, or word of indeterminate language. The implementation guideline does not condition that obligation on a separate subjective determination that the term `requires pronunciation help`.

**Producer semantics:**

- the context record stores `context_change_player_initiated_where_possible: true`, introducing an unregistered source exception;
- the pronunciation record triggers only when `proper_name_technical_term_or_word_of_indeterminate_language_requires_pronunciation_help`, narrowing the source term-class trigger behind an extra subjective predicate.

**Why MAJOR:** the page is declared `ATOMICALLY_EXPANDED`, but either representation can allow a product/applicability evaluation to pass while omitting a source obligation. The current structural validator does not reject either weakening because both records still have nonempty triggers and nonempty `required_semantics`. This contradicts the packet's source-faithful atomicity and semantic-drift rejection claims.

**Required correction:** Issue #245 / `W2-REM-ACC-04` must remove the invented `where_possible` weakening, remove the subjective pronunciation-help gate, and add semantic fixtures/contracts that reject recurrence while preserving all aggregate fail-closed state.

### PG-REM-ACC03-m01 — MINOR (correction required) — XAG 104 significant-pause threshold is not deterministically evaluable

**Affected record:** `XAG104-SPEAKER-ID-REFRESH`.

Microsoft's current XAG 104 wording says the speaker name needs to reappear after a speaker change or after a significant pause described as `greater than 1-2 minutes`. The producer preserves that wording only as the scalar string `significant_pause_minutes: '>1-2'` while the trigger refers generically to a `significant_pause`.

That is source-adjacent but not machine-deterministic: `>1-2` is neither a typed threshold nor an explicit uncertainty interval/evaluation rule. The validator can therefore mark applicability/trigger totality PASS without defining how an evaluator treats a pause between one and two minutes.

**Required correction:** Issue #245 must retain the exact source phrase but encode a deterministic fail-closed interpretation or explicit UNKNOWN interval state that cannot silently satisfy the clause. Add an adversarial semantic fixture for this field.

## 5. Negative attacks that passed

The review did **not** find a BLOCKER or a separate MAJOR in these bounded areas:

- the 77-member expected inventory arithmetic is internally consistent and stable-ID unique;
- XAG 102, XAG 103, and XAG 105 sampled load-bearing thresholds/conditions match the current implementation-guideline surface;
- XAG 108–123 remain `GUIDELINE_SUMMARY_ONLY` and are not promoted by this overlay;
- every new empirical evidence catalog entry remains `NOT_RUN` and page gaps remain OPEN;
- `mapping_complete` remains false and `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains OPEN;
- no legal/compliance, Valve Verified, implementation, production, release, readiness, verification, integration, decision, or canonical authority is claimed;
- PR #241 does not expand outside the declared three-file remediation/handoff surface.

These negative results do not cure the source-semantic findings above.

## 6. Disposition and downstream route

`CHANGES_NEEDED`.

Issue #240 is **not** accepted as reviewed bounded remediation input and is **not** eligible for integration on the basis of this review. The one bounded correction route is Issue #245 / `W2-REM-ACC-04`. After that successor terminalizes at an exact immutable head, a fresh independent/degraded-independent scoped review of the corrected semantic records is required.

`W2-REV-M02` remains `OPEN_BOUNDED`; XAG 108–123 atomic mapping and required empirical accessibility evidence remain unresolved independently of these findings. No readiness or canonicalization authority is created by this review.