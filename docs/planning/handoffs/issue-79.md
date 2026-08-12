# Issue #79 handoff — W2-PLAT-01

**Mission:** `W2-PLAT-01`  
**Branch:** `planning/issue-79`  
**Ownership generation:** Issue #79 comment `5269656708`  
**Base main:** `c7ba185ed9667b717794c19eaa0834ca41aa4c78`  
**Authoritative foundation blob:** `a252e3c93702f3ebaecd3e888944a23dbe1b0e1d`  
**Research report blob:** `f47ad96baea765580ad9d016d527c932ce3b2768`  
**Research report commit:** `e972f9cb985d78cc11ea379de5afbc5e11f63ca8`  
**State intended after terminal capsule:** `REVIEW_READY`  
**Required review:** `W2-REV-01`

## Completed work

Produced `docs/planning/wave-2/research/target-platform-scope.md` from the bounded authoritative packet plus current first-party external platform sources.

The report:

- records a freshness-sensitive evidence register for Valve/Steam, Microsoft/Windows/XAG, Apple/macOS, Nintendo, and PlayStation;
- distinguishes observed platform facts from sequencing inference;
- compares four platform-envelope alternatives;
- recommends `PLAT-PC-FIRST-R1` as a **planning/research candidate**, not a release promise;
- makes supported Windows 11 desktop the primary evidence target;
- makes Steam Deck/SteamOS via the normal Windows build a required compatibility evidence target;
- keeps native Linux desktop, macOS Apple silicon, and Microsoft Store PC packaging conditional;
- keeps Xbox/PlayStation/Nintendo partner-gated and mobile/tablet product scope deferred;
- defines downstream input, display/performance, save/platform-service, localization, accessibility, engine-fit, packaging, and CI implications;
- preserves explicit open commitments and source/version-triggered reopen conditions.

## Material findings

1. A Windows-only scope is too narrow for the current planning problem because it does not exercise controller-complete UX, non-Windows portability, small-display behavior, or engine exit cost early enough.
2. A simultaneous desktop-tri-platform or PC+console launch assumption is too strong for the current evidence state and would turn a planning input into an implicit release commitment.
3. The lowest-regret bounded candidate is PC-first: supported Windows as primary execution baseline, Steam Deck/SteamOS compatibility as required portability/UX evidence, and macOS/native-Linux/storefront/console expansion gated by later evidence.
4. Steam Deck compatibility criteria supply concrete, current testable requirements for controller-only flow, glyph switching, controller text entry, small-display/default-performance behavior, and device-warning handling without requiring native Linux as an immediate release target.
5. Windows 10 Home/Pro is outside normal support as of 2025-10-14, so the candidate uses supported Windows 11 rather than inheriting stale historical minimum-OS language from storefront documentation.
6. Console certification details remain partly partner-gated. The report therefore records them as unknown/deferred until official access and explicit scope promotion rather than inventing requirements from memory.
7. Internationalization architecture is required before shipping-language selection: player-visible strings, Unicode/layout stress, durable IDs, and asset-text identification can be tested without promising translations.
8. `IR-BLOCKER-PLATFORM-SCOPE` is narrowed enough for downstream research, but this producer does not claim the production-readiness blocker is resolved.

## External evidence posture

External facts are sourced from first-party documentation and were observed on 2026-08-12. The report explicitly notes important limitations:

- Steam survey results are an optional Steam-user sample, not total-market truth;
- Steamworks platform pages contain some historical minimum-OS text that is not used as a 2026 lifecycle baseline;
- Microsoft XAGs are best-practice guidance, not a legal-compliance checklist;
- Apple tooling availability does not prove acceptable port cost/performance;
- console SDK/certification details cannot be assumed before partner/program access.

The report uses event/version freshness triggers instead of inventing an arbitrary maximum age.

## Scope limits / open work

This work does not:

- select or verify an engine;
- choose final launch platforms or storefronts;
- set final PC minimum/recommended hardware;
- choose shipping languages;
- define a multiplayer/account/cloud/commerce backend;
- verify current applicable accessibility requirements for the selected scope;
- establish console certification compliance;
- resolve any implementation-readiness blocker by producer assertion;
- replace `W2-REV-01`.

Downstream open questions include native Linux value versus Proton, macOS product relevance, supported Windows version/hardware floor, localization commitments, online/platform-service scope, console timing, and whether engine/accessibility evidence requires changing the recommended sequence.

## Producer self-review

Self-review against Issue #79 acceptance criteria, `AGENTS.md` planning-output requirements, and the canonical Wave 1 foundation:

- BLOCKER: 0
- MAJOR: 0
- MINOR requiring correction before terminalization: 0
- bounded scope without false release commitment: PASS
- current first-party source/date/scope recorded: PASS
- evidence versus inference separated: PASS
- alternatives versus recommendation separated: PASS
- engine/accessibility/packaging/input/localization implications explicit: PASS
- dependencies/interfaces explicit: PASS
- observability/evaluation explicit: PASS
- failure modes and risks explicit: PASS
- unresolved questions explicit: PASS
- reopen/freshness conditions explicit: PASS
- required independent critique retained: PASS
- production/readiness authority leakage: none identified

## Downstream work unblocked after valid terminal status

Publishing a valid schema-3 `STATUS(REVIEW_READY)` for this exact final branch head satisfies the declared `W2-PLAT-01_REVIEW_READY` prerequisite used by:

- `W2-ACC-01`;
- `W2-ENG-03` (subject to its other hard prerequisites);
- eventual `W2-REV-01` input collection.

No downstream issue is claimed by this episode.

## Next action

After the terminal schema-3 `STATUS(REVIEW_READY)` binds the exact final branch/work SHA, freeze `planning/issue-79`.

`W2-REV-01` must independently attack the candidate’s source freshness, PC-first inference, required-versus-conditional target split, Deck/controller requirements, localization/accessibility implications, partner-gated unknowns, and production-readiness boundary. Do not treat this producer self-review, a PR, or any later `main` integration as the independent review disposition.

Any future integration into `main` must remain squash-only and follow the declared review/integration authority.
