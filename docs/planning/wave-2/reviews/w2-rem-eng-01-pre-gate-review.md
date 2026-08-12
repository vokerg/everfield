# W2-PG-REM-ENG-01 — Independent pre-gate review of corrected engine admission evidence

**Review mission:** `W2-PG-REM-ENG-01` / Issue #98  
**Reviewed remediation:** `W2-REM-ENG-01` / Issue #93  
**Reviewed immutable work/head:** `b5dfeb87fb53f47dcfa04b9b7140fa7abe419fa6`  
**Reviewed report blob:** `b4b58173aafdb6a230e82ee2d8b2c7ac3254ccfe`  
**Reviewed disposition blob:** `9f77d060d3477e0a8a22c13d6ac340c0837892d3`  
**Reviewed handoff blob:** `76ce68a500dab06b1e8ce7d6aa7c835b049a1978`  
**Source producer:** `W2-ENG-01` / Issue #71 @ `7e5fd79a557fd404e8178b5096b476063d606ec0`  
**Original findings:** `SR-M01`, `PG-ENG-M01`, `PG-ENG-m01`  
**Review authority:** non-authority pre-gate input only; formal aggregate independent review remains `W2-REV-01`.

## 1. Disposition

`CLEAN_FOR_W2_REVIEW_INPUT`

Independent attack found **0 BLOCKER / 0 MAJOR / 0 correction-requiring MINOR** in the exact remediation scope. The corrected packet closes the original reconstructability and deterministic-cap defects sufficiently for downstream evidence consumption. This result does not select an engine, authorize W2-ENG-03 outcomes, establish implementation readiness, or create canonical authority.

## 2. Attack plan and evidence

The review attacked the corrected packet before accepting its rationale:

1. reconstruct `ENG-UNIVERSE-v2` solely from its declared rule and exact member list;
2. check that each universe member has exactly one explicit hard-gate state and operational outcome;
3. perturb the diversity-cap reasoning by changing input/table order and by considering gate-passing challengers in overlapping hypotheses;
4. recheck the load-bearing current first-party challenger facts for Flax, Cocos Creator, and MonoGame, plus the frozen current baselines for the admitted set where a current release identity was load-bearing;
5. inspect authority language for scalar ranking, production selection, readiness leakage, or canonicalization claims.

## 3. Discovery-universe attack — PASS

### 3.1 Construction is bounded and reconstructable

The corrected report defines `ENG-UNIVERSE-v2` as exactly the union of the eight engines named in the frozen Issue #71 candidate and three explicit remediation challengers: Flax Engine, Cocos Creator, and MonoGame. The resulting 11-member list is written explicitly and all unlisted engines are typed as `OUTSIDE_OPERATIONAL_UNIVERSE(ENG-UNIVERSE-v2)`, not as failed candidates.

This is intentionally not an exhaustive market census. That boundedness is important: the original defect was inability to distinguish never-considered, screened-out, and diversity-deferred candidates. The v2 rule now makes those states reconstructable and gives out-of-universe classes explicit reopen conditions rather than silently converting absence into rejection.

### 3.2 Every member has one operational disposition

The negative-screen table contains all 11 exact members and assigns each one operational outcome: five `ADMITTED` and six `DEFERRED_BY_DIVERSITY_CAP`. No member is missing, no member is assigned two terminal outcomes, and no challenger is converted to a false hard-gate failure merely to preserve the original five.

Flax is especially load-bearing for `PG-ENG-M01`: the remediation now records it as hard-gate `PASS` and diversity-deferred, directly eliminating the prior silent-omission path.

### 3.3 Plausible omissions cannot silently masquerade as failures

A future engine not in the 11-member set does not inherit `FAILS_ADMISSION_GATE`; it is outside v2 by construction. Adding one requires a new universe version and provenance. This does not prove all engines were considered, but it does close the auditability defect the remediation was scoped to repair.

## 4. Diversity-cap attack — PASS

The corrected cap is deterministic under the declared packet:

- process hypotheses H1 through H5 in fixed order;
- for each hypothesis choose the first hard-gate-passing member in its frozen representative-priority list that is not already assigned;
- later passing members remain `DEFERRED_BY_DIVERSITY_CAP`;
- the resulting admitted set is explicitly unordered and carries no production-selection authority.

Reordering the outcome table does not change the result because selection depends on the frozen hypothesis lists, not table position. Gate-passing challengers with overlapping memberships also do not create ambiguity: MonoGame loses H1 to Bevy; Cocos loses H2/H3/H4 to earlier representatives; Flax loses H3/H4/H5 to earlier representatives; O3DE and Stride likewise remain deterministic runner-ups.

Applying the rule reproduces exactly `{Bevy, Defold, Godot, Unity, Unreal Engine}`. The qualitative reasons for the representative priorities remain experiment-design judgments, but the judgments are now explicit/versioned inputs rather than an unrecorded post-hoc tie-break. That is sufficient for the stated remediation acceptance criterion and does not amount to a scalar engine ranking.

## 5. Current-source spot checks — PASS with retained follow-up risk

Load-bearing current source facts were independently rechecked on 2026-08-12.

### Flax Engine

First-party Flax material confirms release **1.12** dated **2026-05-18**, documents command-line/headless build use, and publishes current licensing/EULA material. The corrected packet's `PASS` plus later exact-account/license follow-up posture is supported.

Sources rechecked:

- https://flaxengine.com/blog/flax-1-12-released/
- https://docs.flaxengine.com/manual/editor/advanced/command-line-access.html
- https://flaxengine.com/licensing/

### Cocos Creator

First-party Cocos material confirms **3.8.8** release notes dated **2025-12-16**, a 2D/3D cross-platform product path, command-line publishing with exit codes, and the explicit warning that command-line execution still requires a GUI environment. The remediation therefore correctly avoids both a false clean automation claim and a hard exclusion, retaining `PASS_WITH_AUTOMATION_AND_TERMS_FOLLOWUP`.

Sources rechecked:

- https://www.cocos.com/en/update
- https://docs.cocos.com/creator/3.8/manual/en/editor/publish/publish-in-command-line.html
- https://docs.cocos.com/creator/3.8/manual/en/editor/publish/index.html

### MonoGame

First-party MonoGame material confirms **3.8.5** released **2026-07-15**, describes MonoGame as a cross-platform game framework, and documents the code-centric/CLI-compatible content-build path. Treating it as a passing framework boundary probe rather than silently excluding it is supported.

Sources rechecked:

- https://monogame.net/blog/2026-07-15-3.8.5-release-2026/
- https://monogame.net/
- https://docs.monogame.net/

### Admitted frozen baselines

Current first-party release material independently confirms the load-bearing frozen baseline identities for Bevy **0.19**, Defold **1.13.0**, Godot **4.7.1-stable**, Unity **6000.3.21f1**, and Unreal Engine **5.8**. The remediation correctly treats these only as starting evidence and requires W2-ENG-03 acquisition-time freshness rather than granting them permanent authority.

No spot check justified converting an `UNKNOWN` or follow-up obligation into PASS authority.

## 6. Original finding closure

| Finding | Independent review result | Why closed |
|---|---|---|
| `SR-M01` | CLOSED | finite/versioned operational universe, exact list, complete explicit screen, typed outside-universe state and reopen rule |
| `PG-ENG-M01` | CLOSED | Flax/Cocos/MonoGame omission boundary is now explicit; Flax is gate-passing and diversity-deferred rather than silently absent |
| `PG-ENG-m01` | CLOSED | fixed H1→H5 processing plus frozen representative-priority lists mechanically reproduce the admitted set without table-order dependence |

The correction is not accepted merely because the original five remain unchanged; it is accepted because their inclusion and every declared challenger's disposition are now reproducible from explicit versioned inputs.

## 7. Authority-boundary attack — PASS

The reviewed packet repeatedly and consistently limits itself to admission/spike-set construction. It does not:

- rank the admitted set for production;
- claim a W2-ENG-03 comparative result;
- select an engine;
- clear implementation readiness;
- waive W2-REV-01;
- create canonical authority.

The five-engine set remains an unordered experiment set, with later equivalent spikes and independent review required before any stronger decision.

## 8. Residual risks and reopen conditions

These are retained risks, not findings requiring correction in this remediation scope:

- the operational universe is intentionally bounded and must be version-bumped if a newly decision-critical engine or hypothesis emerges;
- Cocos GUI-environment and exact product-license constraints remain spike-time evidence obligations;
- Unity/commercial account and automation terms remain freshness-sensitive;
- engine release/version drift must create new exact spike baselines rather than silently reuse frozen strings;
- W2-ENG-03 still must test equivalent workloads and may invalidate the experiment hypotheses or representative choices with evidence.

Reopen this pre-gate conclusion if Issue #93 work identity changes, a cited first-party fact materially drifts before W2-REV-01 consumes it, or a deterministic reconstruction from the declared universe/cap inputs produces a different admitted set.

## 9. Next gate

Treat Issue #93 work `b5dfeb87fb53f47dcfa04b9b7140fa7abe419fa6` as clean noncanonical remediation input for downstream W2-ENG-03/W2-REV-01 dependency resolution. This review itself creates no integration or selection authority. Formal aggregate independent adversarial review remains `W2-REV-01`.