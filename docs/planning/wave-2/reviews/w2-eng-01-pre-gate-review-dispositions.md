# W2-ENG-01 pre-gate review finding dispositions

**Remediation mission:** `W2-REM-ENG-01` / Issue #93  
**Source mission:** `W2-ENG-01` / Issue #71  
**Source frozen head/work:** `7e5fd79a557fd404e8178b5096b476063d606ec0`  
**Source report blob:** `cfdec22eac4865bf80fd05ea3a35270828505bbc`  
**Source handoff blob:** `7ecf85da7f69a12f27f7d251da77ecde12c2be04`  
**Source terminal status:** Issue #71 comment `5251694382`  
**Author self-review:** Issue #71 comment `5252180471`  
**Independent pre-gate review:** Issue #71 comment `5270780071`  
**Remediation claim:** Issue #93 comment `5270794299`  
**Corrected report blob:** `b4b58173aafdb6a230e82ee2d8b2c7ac3254ccfe`  
**Formal independent review:** still `W2-REV-01`; this document is remediation provenance, not a schema-3 `REVIEW_STATUS`.

## Disposition summary

| Finding | Severity | Disposition | Mechanical/process evidence |
|---|---|---|---|
| `SR-M01` incomplete/reconstructability-defective discovery universe | MAJOR | RESOLVED | exact finite `ENG-UNIVERSE-v2`; every member receives an explicit screen outcome; unlisted engines are `OUTSIDE_OPERATIONAL_UNIVERSE` with reopen policy |
| `PG-ENG-M01` same universe defect independently confirmed by omitted Flax candidate | MAJOR | RESOLVED | Flax, Cocos Creator, and MonoGame are explicit current challengers; Flax passes hard gates and is explicitly diversity-deferred rather than silently absent |
| `PG-ENG-m01` diversity-cap tie-break not deterministic | MINOR | RESOLVED | five explicit hypothesis slots plus exact frozen per-hypothesis representative-priority lists applied in deterministic H1→H5 order |

No finding is waived or resolved solely by prose saying the original five were reasonable.

## SR-M01 / PG-ENG-M01 — RESOLVED

### Source defect

The frozen Issue #71 producer report named the five admitted engines and only three plausible exclusions. It did not establish a finite screen universe, so a later reviewer could not distinguish:

- a candidate that was deliberately outside scope;
- a candidate that was screened and failed a hard gate;
- a candidate that passed gates but lost the five-slot diversity cap; or
- a candidate that was simply never considered.

The independent review demonstrated materiality with Flax Engine: current first-party evidence shows a maintained general-purpose engine, documented headless CLI automation, and published licensing, yet the frozen report contained no reconstructable reason for its omission.

### Correction: exact operational universe

The remediation freezes `ENG-UNIVERSE-v2` before its outcome table. It contains exactly 11 members:

- Bevy;
- Defold;
- Godot;
- Unity;
- Unreal Engine;
- GameMaker;
- O3DE;
- Stride;
- Flax Engine;
- Cocos Creator;
- MonoGame.

The construction is explicitly bounded: all eight engines named by the frozen producer plus three fixed remediation challengers covering the omission boundaries raised during review. The report does **not** claim this is every engine in existence.

Every member has an explicit hard-gate state and operational outcome. Any unlisted engine is explicitly `OUTSIDE_OPERATIONAL_UNIVERSE(ENG-UNIVERSE-v2)`, not treated as rejected. The report also states the exact conditions for creating a later `ENG-UNIVERSE-v3`.

### Challenger evidence

#### Flax Engine

Current first-party evidence observed 2026-08-12 supports:

- Flax 1.12 release post dated 2026-05-18;
- documented `-headless` / `-build` command-line automation;
- published licensing/EULA/source-access terms.

Result: `PASS` hard gates and `DEFERRED_BY_DIVERSITY_CAP` after hypothesis assignment.

This directly closes the omission demonstrated in the independent review.

#### Cocos Creator

Current first-party evidence supports:

- Cocos Creator 3.8.8 release notes dated 2025-12-16 and a July 2026 Cocos staff statement that the 3.x line continues to be maintained;
- integrated 2D/3D game-development scope;
- documented command-line publishing with a material GUI-environment requirement;
- currently published Cocos User Agreement dated 2022-09-01, which permits free game development with Creator but explicitly points to product-specific software-license terms that still must be captured for exact use.

Result: `PASS_WITH_AUTOMATION_AND_TERMS_FOLLOWUP`, then `DEFERRED_BY_DIVERSITY_CAP`.

The GUI and product-license constraints remain visible instead of being converted into either a silent exclusion or a false clean PASS.

#### MonoGame

Current first-party evidence supports:

- MonoGame 3.8.5 release dated 2026-07-15;
- repository-native .NET game framework workflow;
- CLI/CI content-building and `mgcb` command-line tooling;
- Microsoft Public License posture with separately identified third-party portions.

Result: `PASS`, then `DEFERRED_BY_DIVERSITY_CAP` as the code-first framework boundary runner-up.

### Outside-universe control

The corrected report lists example outside classes — specialized genre tools, additional visual/no-code engines, additional frameworks/libraries, additional commercial/source-available editors, and unsupported/no-current-primary-baseline tools — and gives each a reopen trigger.

This makes “not in v2” a machine-readable scope statement rather than an unstated negative conclusion.

## PG-ENG-m01 — RESOLVED

### Source defect

The frozen producer justified the selected five after the fact but did not provide a reproducible way to resolve overlap between multiple hard-gate-passing engines in the same decision hypothesis. A challenger such as Flax could therefore be accepted or rejected by changing qualitative emphasis after seeing the candidate list.

### Correction: frozen representative assignment

The corrected report declares five experiment hypotheses before applying the outcome table:

1. `H1_CODE_FIRST_REPOSITORY_NATIVE`;
2. `H2_LEAN_INTEGRATED_2D_FIRST`;
3. `H3_OPEN_GENERAL_PURPOSE_EDITOR`;
4. `H4_MAINSTREAM_COMMERCIAL_EDITOR_TERMS_RISK`;
5. `H5_HEAVYWEIGHT_3D_SOURCE_PLATFORM_BREADTH`.

It then freezes exact representative-priority lists for each hypothesis. The algorithm is:

1. process H1 through H5 in order;
2. for each hypothesis, select the first hard-gate-passing member in its frozen list that has not already been assigned;
3. keep later hard-gate-passing members as `DEFERRED_BY_DIVERSITY_CAP`;
4. do not produce a scalar score or production ranking.

This mechanically reproduces:

- Bevy;
- Defold;
- Godot;
- Unity;
- Unreal Engine.

The output remains unordered. Changing a priority list requires a new admission/cap version and provenance; it cannot happen silently during W2-ENG-03.

## Producer self-review source corrections

During remediation self-review, two source/provenance defects in the first #93 draft were corrected before terminalization:

1. Flax 1.12's first-party release-post date was corrected from 2026-05-19 to **2026-05-18**, and an unsupported exact build-version string was removed.
2. The first draft's qualitative lexicographic tie-break was replaced by exact frozen representative-priority lists so the cap result is mechanically reproducible.

MonoGame 3.8.5's 2026-07-15 release was independently rechecked against the first-party MonoGame release post before this disposition was written.

## Self-review

Against Issue #93 acceptance criteria and only the declared remediation scope:

- unresolved BLOCKER: 0;
- unresolved MAJOR: 0;
- correction-requiring MINOR: 0;
- exact source #71 provenance retained: PASS;
- author + independent findings explicitly dispositioned: PASS;
- finite/versioned operational universe: PASS;
- every universe member has explicit outcome: PASS;
- outside-universe state/reopen rule: PASS;
- Flax current challenger evidence: PASS;
- Cocos current challenger evidence + risks: PASS;
- MonoGame current challenger evidence: PASS;
- deterministic five-slot assignment: PASS;
- original admitted set reproduced without scalar score or engine-selection authority: PASS;
- current terms/platform/source risks retained: PASS;
- W2-ENG-03 / readiness / canonicalization authority: NOT CLAIMED;
- required formal review remains `W2-REV-01`: PASS.

## Authority limits and next gate

This remediation repairs discovery/admission auditability. It does not prove that the admitted engines are suitable for Everfield, that a deferred engine is inferior, or that any engine should be selected for production.

Equivalent comparative spikes remain the job of W2-ENG-03. Formal aggregate independent adversarial review remains `W2-REV-01`. The corrected Issue #93 packet should supersede the frozen Issue #71 producer payload as the substantive W2-ENG-01 input while Issue #71 remains immutable historical provenance.
