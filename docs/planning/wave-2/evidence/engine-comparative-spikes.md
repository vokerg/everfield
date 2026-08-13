# W2-ENG-03 — Comparative autonomous engine spikes

**Mission:** `W2-ENG-03` / Issue #82  
**Task class / decision state:** `PLANNING_EXPERIMENT / EVIDENCE_REQUIRED`  
**Execution episode:** `w2-eng-03-agent-20260813-0825-01`  
**Base:** `main@042d140b5d2e0b951da4528e1867514983418d6f`  
**Result:** **INCONCLUSIVE — EXECUTION ENVIRONMENT CANNOT MATERIALIZE ANY ADMITTED ENGINE TOOLCHAIN**  
**Engine selection authority:** **NONE**  
**Production/readiness/canonicalization authority:** **NONE**  
**Required independent review:** `W2-REV-01`

## 1. Scope and non-goals

Issue #82 asks for equivalent S1–S10 comparative spikes across the admitted Bevy, Defold, Godot, Unity, and Unreal candidates. This episode does not turn an unavailable toolchain into synthetic evidence. It records the exact immutable planning inputs, refreshes acquisition-time engine baselines from first-party sources, probes the actual execution host twice, attempts to establish the required acquisition path, and fails closed when no admitted engine can be materialized.

The result is therefore `INCONCLUSIVE`, not a winner, score, recommendation, implementation-readiness decision, or engine ADR. No candidate-specific project was created, no engine process was started, and no S1–S10 result is represented as PASS. Every required candidate/scenario cell remains `NOT_RUN`.

## 2. Exact immutable input packet

The historical prerequisite tokens remain graph provenance. Substantive execution consumes the corrected/superseding packet where repository state provides one.

| Surface | Exact input used | Authority boundary |
|---|---|---|
| canonical Wave-1 foundation | `docs/planning/WAVE-1-FOUNDATIONS-v1.md` on current canonical history | planning foundation; implementation readiness remains blocked |
| authority/evidence compiler | Issue #87 `W2-REM-AUTH-01` work `28cbecc13f679da0b43793525a9befd384df9a6d`; corrected contract blob `a2cd16e1a20568f72a04e90eea4453b7fb880146`; terminal `5252368521` | required by durable Issue #82 directive `5255386532`; historical Issue #69 remains only prerequisite/provenance |
| engine admission | Issue #93 `W2-REM-ENG-01` work/head `b5dfeb87fb53f47dcfa04b9b7140fa7abe419fa6`; report blob `b4b58173aafdb6a230e82ee2d8b2c7ac3254ccfe`; terminal `5270940239` | finite `ENG-UNIVERSE-v2`; admitted set remains unordered |
| engine harness | Issue #112 `W2-REM-ENG-04` work/head `6c5777ca56d43e22cba9b5e776e436d11b846325`; harness blob `58e6e0832e36fdc4dd2bee7d1984e12e3fa4fc9f`; validator blob `7837695c91365273b2c89f3852b401c2f127af54`; terminal `5276691786` | `W2-ENG-HARNESS-v4`; exact candidate/adaptation/attempt binding and no-laundering rules |
| semantic hash evidence | Issue #73 `W2-HASH-01` work/head `fadb5af8e30e554ed813e94b23ba65fc3b9709ad`; terminal `5257041297`; candidate `ef-sem-1` | bounded PASS only for the reviewed semantic model; native engine hashes receive no authority |
| platform scope | Issue #92 `W2-REM-PLAT-01` work/head `9d51099be4d53eff876104f482e3c163d34519e3`; report blob `d6a20c2200cedad97ede36beb9871d420ca7a8ca`; source-record blob `f2a9333436c9cbc4fe91ec71507997f46f2247e4`; terminal `5270335386` | `PLAT-PC-FIRST-R1` remains reversible planning evidence, not release authority |

No frozen predecessor branch was edited or re-owned.

## 3. Acquisition-time baseline refresh — 2026-08-13

The admission report explicitly requires W2-ENG-03 to recheck releases and other freshness-sensitive facts at acquisition. First-party refresh produced the following bounded baseline facts:

| Candidate | Acquisition-time fact used | First-party source | Effect on this episode |
|---|---|---|---|
| Bevy | Bevy 0.19 announced 2026-06-19 | `https://bevy.org/news/bevy-0-19/` | use 0.19 family for acquisition; no Rust toolchain is present |
| Defold | 1.13.0 is the current stable release found; 1.13.1 is beta | `https://defold.com/2026/06/22/Defold-1-13-0/` | use 1.13.0 stable; Java exists but `bob.jar` does not |
| Godot | 4.7.1-stable released 2026-07-14 | `https://godotengine.org/article/maintenance-release-godot-4-7-1/` | frozen 4.7.1 starting point; no Godot executable is present |
| Unity | official archive's newest visible release at check time is 6000.5.6f1, 2026-07-29 | `https://unity.com/releases/editor/archive` | producer's 6000.3.21f1 must not be silently described as latest; no Unity executable/acquisition path is present |
| Unreal Engine | Unreal Engine 5.8 is available | `https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show` | use 5.8 family for acquisition; no Unreal executable/acquisition path is present |

This refresh is not a compatibility verdict. It only prevents silently executing against stale version labels.

## 4. Execution-host evidence

Two read-only probes ten seconds apart produced the same material capability state. The normalized host object is:

```json
{"cpus":5,"dns":{"github.com":false,"sh.rustup.rs":false,"unity.com":false,"unrealengine.com":false},"java":["openjdk version \"21.0.11\" 2026-04-21","OpenJDK Runtime Environment (build 21.0.11+10-1-deb13u2-Debian)"],"kernel":"Linux 6.18.35 x86_64 GNU/Linux","mem_kib":6219544,"node":"v22.16.0","python":"Python 3.13.5","schema":"W2-ENG-03-HOST-PROBE-v1","tools":{"Unity":"MISSING","UnrealEditor":"MISSING","bob":"MISSING","cargo":"MISSING","godot":"MISSING","godot4":"MISSING","java":"/usr/bin/java","rustc":"MISSING","unity":"MISSING"}}
```

Canonical-JSON SHA-256: `2dc08ccab66590ab6c30b1ada624770505e6731da5de92c2492a6defd85b9f29`.

Observed probe details:

- Linux `6.18.35`, x86_64;
- 5 logical CPUs;
- `6219544 KiB` memory (~5.9 GiB);
- ~38 GiB free filesystem space at probe time;
- Python `3.13.5`, Node `22.16.0`, Java `21.0.11` available;
- Rust/Cargo, Godot, Defold Bob, Unity, and Unreal Editor absent;
- DNS resolution failed for `github.com`, `sh.rustup.rs`, `unity.com`, and `unrealengine.com` in both passes.

A direct acquisition probe also returned `curl: (6) Could not resolve host` for GitHub release assets and `sh.rustup.rs`. The browsing/research channel can inspect public source pages, but it does not place binaries into the isolated execution host and therefore cannot substitute for an engine installation.

## 5. Acquisition and attempt ledger

W2-ENG-HARNESS-v4 requires exact candidate identity, an accepted adaptation, a common resource/start profile, at least two normal attempts for comparable authority, and the required failure-injection evidence. None of those run-level objects may be fabricated before a real engine/toolchain exists.

| Candidate | Required first executable surface | Local state | Acquisition attempt | Outcome |
|---|---|---|---|---|
| Bevy | `cargo`/`rustc` and Bevy 0.19 dependency materialization | both missing | Rustup/GitHub path cannot resolve from host | `NOT_RUN: TOOLCHAIN_UNAVAILABLE` |
| Defold | Java + exact 1.13.0 `bob.jar` | Java present; Bob missing | public GitHub release path cannot resolve from host | `NOT_RUN: TOOLCHAIN_UNAVAILABLE` |
| Godot | 4.7.1 Linux executable + export material | executable missing | public release asset path cannot resolve from host | `NOT_RUN: TOOLCHAIN_UNAVAILABLE` |
| Unity | exact Linux editor + valid activation/account state for unattended use | editor missing | official site cannot resolve from host; no activation state is materialized | `NOT_RUN: TOOLCHAIN_UNAVAILABLE` |
| Unreal Engine | exact 5.8 Linux editor/source build + required authenticated/source package state | editor missing | official site cannot resolve from host; no authenticated engine package is materialized | `NOT_RUN: TOOLCHAIN_UNAVAILABLE` |

Manual interventions performed: **none** beyond read-only tool/path/DNS probes. No account login, license acceptance, GUI interaction, hidden editor state, engine-specific code generation, or candidate substitution occurred.

### 5.1 S1–S10 result matrix

Because no candidate reached generation/adaptation validation, no valid `AttemptRecord` exists. At the plan level, all required executions remain `NOT_RUN` rather than being promoted to synthetic attempts.

| Candidate | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bevy | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Defold | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Godot | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Unity | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Unreal Engine | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

Counts: `0 PASS_FOR_COMPARISON`, `0 FAIL`, `0 FLAKY`, `0 executed INCONCLUSIVE`, `50 NOT_RUN`.

The absence of FAIL does **not** imply success. It means execution never began.

## 6. Required evidence surfaces and why they remain unknown

The task requires state/capture, merge-conflict, failure/recovery, profile, package, continuation, attempt-cost, and manual-intervention evidence. Every one remains unknown because the engine executables were unavailable before S1.

- state/hash: no engine-native state was emitted; `ef-sem-1` is not used as a surrogate engine run;
- capture: no engine window/frame existed;
- merge conflict: no candidate project/workspace existed;
- failure injection/recovery: no engine attempt lineage existed;
- profiling: no candidate workload executed;
- packaging: no candidate build/export pipeline executed;
- continuation: no candidate partial state existed to hand to a fresh context;
- CI: no engine command existed to place under CI;
- cost: only host/acquisition probing cost is observed; build/edit/test/recovery cost is unknown.

## 7. Sensitivity, Pareto, and exit-risk treatment

No comparative Pareto frontier is valid from this episode. Any ranking would be an artifact of acquisition availability, familiarity, or prose rather than equivalent S1–S10 evidence.

The only observed sensitivity is **execution-environment dependence**: a network-disabled, pre-toolchain host collapses all five candidates to the same `NOT_RUN` class. That is a factory/evidence-surface finding, not an engine-quality finding.

Bounded exit risks to carry forward:

- Bevy requires a reproducible Rust/Cargo dependency acquisition surface;
- Defold requires exact retained Bob/engine artifacts;
- Godot requires exact retained editor/export artifacts;
- Unity additionally requires an unattended installation/activation/account path whose state is explicitly captured;
- Unreal additionally requires a materialized authenticated/source/prebuilt acquisition path and likely a larger resource envelope before equivalent work is credible.

These are acquisition risks only. They do not rank engine fitness.

## 8. Disposition

**Result: `INCONCLUSIVE_ENVIRONMENT_BLOCKED`.**

This is a complete record of this execution episode, not completion of the empirical engine comparison. The evidence supports exactly these conclusions:

1. current repository inputs can identify the five admitted candidates and the v4 equivalence/no-laundering contract;
2. acquisition-time release labels changed materially for Godot and Unity relative to frozen producer prose and must be refreshed before future runs;
3. the present execution host cannot materialize any admitted engine toolchain;
4. therefore no S1–S10 comparative claim, score, sensitivity ranking, Pareto dominance claim, engine ADR, or readiness advancement is authorized.

A future rerun requires either a network-enabled execution context or exact pre-seeded engine/toolchain artifacts, plus enough resource/account state to satisfy each candidate's real acquisition path. That rerun must preserve this failed episode as provenance rather than replacing it.

## 9. Failure modes, reopen conditions, and downstream use

Reopen this empirical comparison when any of the following becomes true:

- an execution context can resolve/download the exact public toolchains;
- exact pre-seeded toolchain artifacts are supplied to the isolated host;
- Unity/Unreal unattended acquisition/activation/authentication can be represented without hidden manual state;
- the common host/resource class is revised through review because an admitted candidate cannot credibly run within it;
- an admitted baseline changes before execution;
- the admission set or v4 harness changes.

`W2-SIM-01` and `W2-REV-01` may consume this episode only as **INCONCLUSIVE/NOT_RUN evidence**. They must not interpret `REVIEW_READY` lifecycle state, PR visibility, issue closure, or absence of FAIL as engine-comparison success.

## 10. Bounded self-review

- hidden hard failures: 0; all acquisition failures are explicit;
- fabricated attempts: 0;
- candidate substitutions: 0;
- engine scores/ranks: 0;
- engine selection: none;
- unresolved empirical comparison: **all five candidates / all ten scenarios**;
- report-level BLOCKER/MAJOR requiring correction before independent review: 0 identified;
- required independent adversarial review: `W2-REV-01`.

The correct lifecycle action is to freeze this noncanonical evidence packet for review, not to manufacture engine execution that did not occur.
