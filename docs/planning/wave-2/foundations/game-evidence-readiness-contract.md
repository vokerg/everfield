# W2-GAME-GATE-01 — Core game/experience evidence readiness contract

**Mission:** `W2-GAME-GATE-01` / Issue #196  
**Task class / decision state:** `PLANNING_REVISION / CANONICAL_CANDIDATE`  
**Claim base:** `main@f4cd3125531450d44ed397d7dd830b55d01b5254`  
**Canonical Planning Program blob:** `e3120ec203c4156328770aa86c12fbb7187966dc`  
**Immutable W1-SYN-GAME input:** `e74e0b0c95e85f69718868eedae324a298f02f3e`  
**Authority:** noncanonical planning/readiness structure only. No gameplay implementation, production, release, engine, verification, or canonical authority is created.

## 1. Problem and correction

Wave 1 explicitly retained six producer experiment families as `UNRUN / REQUIRED EVIDENCE`: `RDF-E1..E8`, `GDF-E1..E9`, `EPA-E1..E9`, `WSN-E1..E9`, `EXP-E1..E9`, and `AGE-E1..E10`. That is exactly **54 immutable experiment identities**.

The current Wave-2 promotion graph compiled technical/factory/platform/accessibility/rights/evaluator evidence lanes but did not compile the unresolved core game/player-experience debt into a typed game-evidence lane or readiness blocker. Therefore a synthesis/readiness path could inspect a technically coherent ledger while omitting whether the intended sandbox itself has empirical support.

This revision repairs only that omission. It does **not** declare all 54 experiments globally blocking, does not retroactively mark any Wave-1 experiment PASS, and does not create 54 tasks.

The normative machine-readable accounting is `game-evidence-dependency-map.yaml`.

## 2. Immutable provenance

The exact producer sources are:

| Family | Producer mission | exact work SHA | immutable producer path | count |
|---|---|---|---|---:|
| RDF | W1-TEC-02 | `c13389cf1df7ab8e2515a5267bd56869082df1b2` | `docs/planning/wave-1/proposals/runtime-data-foundation.md` | 8 |
| GDF | W1-DES-01 | `10e1f3cda1f77be81210f769c2224f943810c97b` | `docs/planning/wave-1/proposals/game-design-foundation.md` | 9 |
| EPA | W1-DES-02 | `498679b5c3a473d220723794e66799463ed3ba6f` | `docs/planning/wave-1/proposals/economy-progression-automation.md` | 9 |
| WSN | W1-DES-03 | `d19ddc43c9e5f22c6f14e5c978c30a4e6a2f0d8b` | `docs/planning/wave-1/proposals/world-social-narrative-content.md` | 9 |
| EXP | W1-EXP-01 | `64be52c55d751b37e8d8c4a1758873f4dec64998` | `docs/planning/wave-1/proposals/experience-accessibility-media.md` | 9 |
| AGE | W1-EVAL-01 | `a29a9c08f64947b383f4ca6a19fb88032d93777d` | `docs/planning/wave-1/proposals/automated-game-evaluation.md` | 10 |

The exact W1-SYN-GAME work `e74e0b0c95e85f69718868eedae324a298f02f3e` states that all producer experiments remain `UNRUN / REQUIRED EVIDENCE` until executed. This contract preserves that historical state. A later stronger evidence question can supersede an original question only through explicit immutable provenance; it does not rewrite the original experiment as having run.

## 3. Accounting invariant

Every one of the 54 IDs appears exactly once in the dependency map with exactly one accounting state:

- `GROUPED` — retained in a named versioned bounded tranche;
- `SUPERSEDED` — replaced by a stronger equivalent evidence question with immutable provenance, while the original historical experiment remains unrun;
- `DEFERRED` — retained behind a typed prerequisite/reopen trigger because its execution surface does not yet exist;
- `RETAINED` — reserved for a separately retained question when grouping would weaken its meaning.

Current accounting is 42 `GROUPED`, 4 `SUPERSEDED`, 8 `DEFERRED`, 0 omitted, 0 duplicated.

The four explicit stronger-equivalent mappings are deliberately narrow:

1. `RDF-E4` → `W2-MIG-01`, current artifact blob `700fe468f119cece9c4b060cda93e576de50f468`.
2. `EXP-E3` → `W2-REM-ACC-02`, current artifact blob `50e6770cc490ef74c44faa3ae9eba115b4c1eb7a`; the stronger question remains OPEN/incomplete and `IR-BLOCKER-ACCESSIBILITY-CURRENT` remains OPEN.
3. `AGE-E5` → `W2-PROTECT-01`, current artifact blob `9f0c42bb82a1bddd97f028b9ba8e94c791e3705a`; production provider/security questions remain OPEN.
4. `AGE-E6` → `W2-EVAL-01`, current artifact blob `50723345e6fffddebdbcd7bff1de6458b5989cf1`; material evaluator drift was detected and no universal evaluator authority exists.

No other Wave-1 experiment is claimed satisfied by later Wave-2 work.

## 4. Typed dependency semantics

The canonical Wave-1 foundation distinguishes `BLOCKS_DECISION`, `BLOCKS_IMPLEMENTATION_SCOPE`, `BLOCKS_RELEASE_SCOPE`, `INFORMS_DECISION`, and `CALIBRATES_EVALUATOR`. This contract uses those edges directly.

The main correction is that **game evidence is scoped, not a mega-gate**:

- foundational sandbox/economy/progression evidence can block `SCOPE-CORE-GAMEPLAY-v1`;
- world/narrative evidence blocks only the corresponding implementation/release scope when that scope exists;
- player-surface, style, audio, localization, mature-economy, and generated-content evidence can be release-sensitive or decision-informing without blocking unrelated implementation;
- evaluator experiments calibrate the evaluator identities whose output is consumed; synthetic agents never become human preference authority;
- runtime experiments whose executable surfaces do not exist remain deferred rather than fabricated as present-tense blockers.

Scheduler readiness therefore follows only the dependency edges relevant to the target scope.

## 5. `IR-BLOCKER-GAME-EVIDENCE`

This revision defines one stable readiness entry:

```yaml
blocker_id: IR-BLOCKER-GAME-EVIDENCE
category: PRODUCT
scope: DOMAIN
scope_id: SCOPE-CORE-GAMEPLAY-v1
state: OPEN
blocks:
  - CORE_GAMEPLAY_IMPLEMENTATION
  - GAMEPLAY_IMPLEMENTATION_READINESS_DECISION
does_not_globally_block:
  - NON_GAMEPLAY_PLANNING_EXPERIMENTS
  - UNRELATED_TOOLING_PLANNING
```

The blocker exists because the intended core sandbox claims—multiple viable lifestyles, no hidden universal route, bounded low-decision burden, automation that increases agency instead of ending play, reachable progression, and evaluator-policy diversity adequate for those claims—remain empirically unproven.

### Resolution predicate

The blocker may resolve only when all of the following hold:

1. the bounded `W2-GAME-EV-CORE-v1` tranche executes against one exact versioned abstract/shared game model with immutable attempt lineage;
2. every mandatory member emits its own result record even when several questions share one run family;
3. required `FAIL`, `INCONCLUSIVE`, or `NOT_RUN` remains unsatisfied rather than averaged away;
4. evidence supports at least two materially viable lifestyle trajectories, no unexplained universal dominant route, bounded chore burden with non-passive automation escalation, supported progression reachability, and sufficient synthetic-policy diversity for the claims consumed;
5. the packet receives the required independent aggregate review and all material findings are dispositioned by a fresh synthesis/readiness ledger.

Resolution is only for the covered core-gameplay implementation scope. It does not settle final balance, engine choice, content depth, mature-game economy, player-surface release quality, accessibility, or release readiness.

## 6. First bounded empirical frontier — `W2-GAME-EV-CORE-v1`

The first empirical successor is intentionally one bounded tranche, not twelve tasks. Its 12 retained experiment identities are:

- `GDF-E1` lifestyle trajectory viability;
- `GDF-E2` dominant-route red team;
- `GDF-E3` chore-burden traces;
- `GDF-E4` automation escalation;
- `EPA-E1` source/sink lifecycle;
- `EPA-E2` lifestyle viability tournament;
- `EPA-E3` dominant-route exploit search;
- `EPA-E4` automation payback/burden sweep;
- `EPA-E5` switching/catch-up simulation;
- `EPA-E7` progression reachability/fuzz;
- `AGE-E3` persona diversity benchmark;
- `AGE-E4` exploit-search benchmark.

A single versioned simplified/abstract game model may jointly exercise these questions, but evidence must preserve a per-ID outcome and cannot infer human fun from synthetic-agent agreement.

The derived successor mission name is `W2-GAME-EV-01`. This task **derives** that frontier but does not create the successor issue; issue creation remains a separate lowest-priority scheduling action.

## 7. Later bounded tranches and deferrals

The dependency map keeps later work bounded by purpose:

- `W2-GAME-EV-STRUCTURE-v1` — system/content coupling and domain-decomposition evidence;
- `W2-GAME-EV-MATURE-v1` — mature sinks/economy robustness, primarily mature/release sensitive;
- `W2-GAME-EV-CONTENT-v1` — semantic content depth/sameness;
- `W2-GAME-EV-WORLD-STRUCT-v1` — fact, knowledge, quest, schedule, branch-persistence structural evidence;
- `W2-GAME-EV-WORLD-CONTENT-v1` — generated narrative and long-horizon social/world release evidence;
- `W2-GAME-EV-PLAYER-SURFACE-v1` — discovery, input, capture, localization, and paired player/simulation surface evidence;
- `W2-GAME-EV-MEDIA-v1` — visual/audio/provenance evidence;
- `W2-GAME-EV-EVALUATOR-v1` — game-specific oracle, semantic coverage, subjective, and routing calibration.

Runtime questions such as engine-adapter parity, RNG isolation, long accelerated simulation, and workload reproducibility remain `DEFERRED` until their declared executable surface exists. Deferral preserves debt; it is not PASS.

## 8. W2-SYN-01 consumption

Issue #85 / W2-SYN-01 terminalized before Issue #196 was created. Its exact packet is immutable historical synthesis input and must not be edited in place.

For any **fresh** synthesis that claims full product/core-game implementation readiness:

1. `IR-BLOCKER-GAME-EVIDENCE` (or an independently reviewed superseding entry) must appear in the readiness ledger;
2. the blocker remains OPEN until its exact evidence/review predicate is satisfied;
3. technical/factory/engine/accessibility/rights/platform evidence cannot silently clear it;
4. a narrower synthesis may omit the blocker only when its declared readiness scope excludes `SCOPE-CORE-GAMEPLAY-v1`.

Because the existing #85 ledger predates this correction, it is insufficient by itself to establish current full core-game/product implementation readiness. That does not rewrite #85's historical terminal state.

## 9. W2-READY-01 consumption

W2-READY-01 is required to cold-start from the complete current `[PLAN-v1]` graph. Therefore:

- it must inspect Issue #196 rather than verifying only the frozen #85 files;
- while this revision is pending required aggregate review, it cannot positively establish that the #85 ledger is complete for full core-game/product implementation readiness;
- after this revision is independently reviewed, a candidate ledger that omits the OPEN game-evidence blocker (or reviewed equivalent) fails closed for the covered core-game scope;
- a positive verification may still be possible for an explicitly narrower scope that excludes the blocked core-gameplay implementation scope.

If #86 has already frozen an outcome before this revision becomes review-authoritative, the current graph change is a reopen/reverification trigger for any claim whose scope includes core gameplay readiness.

## 10. Review and lifecycle

Required independent critique remains **formal aggregate `W2-REV-01`**. The already-completed aggregate review episode predates this packet and therefore cannot be treated as review of these bytes.

The lifecycle is:

`W2-GAME-GATE-01 REVIEW_READY`
→ required fresh/authorized W2-REV-01 aggregate review episode
→ disposition findings
→ fresh synthesis/readiness revision if the blocker is accepted or modified
→ W2-READY-01 verification of the exact updated ledger
→ only then can a covered readiness decision advance.

No step is skipped merely because a PR is mergeable or provenance has been integrated.

## 11. Self-review

- immutable experiment identities expected: **54**
- identities present in map: **54**
- duplicates: **0**
- omissions: **0**
- original unrun experiments upgraded to PASS without explicit stronger equivalent: **0**
- first empirical tranche size: **12**
- one-issue-per-experiment fanout created: **NO**
- synthetic players treated as human fun oracle: **NO**
- engine selected: **NO**
- gameplay implementation authorized: **NO**
- production implementation authorized: **NO**
- release authorized: **NO**
- canonicality claimed: **NO**
- required next gate after terminalization: **fresh/authorized W2-REV-01 aggregate review**
