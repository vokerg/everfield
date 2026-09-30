# W2-READY-PLATFORM-CLOSE-01 — First-playable platform-scope closure candidate

**Issue:** #1337  
**Mission:** `W2-READY-PLATFORM-CLOSE-01`  
**Claim:** comment `5889954076`  
**Claim/base main:** `271ceee5a8af967403b2cba460afdb493fa14ac1`  
**Canonical binding:** Issue #1147 comment `5675066392`  
**Canonical Planning Program blob:** `fd4cf1119c3f86acc3af620024eea72235e81ce4`  
**Canonical activation:** `87c85cecfa9a2ffa464c4b36816a138bf41441af`  
**Human implementation-transition directive:** Issue #84 comment `5889817307`  
**Selected engine:** Godot `4.7.1-stable`  
**Candidate result:** `SATISFIED_FOR_FIRST_PLAYABLE_SCOPE`  
**Canonicality:** `NOT_CANONICAL`

## 1. Exact question

Issue #1038 terminal verification comment `5651326367` truthfully preserved
`platform_scope_predicate: OPEN_BOUNDED`. The missing condition was not a
shipping-platform decision. Issue #1031 defined its satisfaction route as a
separately authorized target product/platform implementation scope.

The 2026-09-29 owner directive now supplies the bounded implementation purpose:
converge on a Godot `4.7.1-stable` first playable, while retaining independent
review/verification and explicitly withholding production/release authority.

This packet asks only whether the already reviewed reversible platform envelope
`PLAT-PC-FIRST-R1` is sufficiently bounded to start that first-playable scope.

## 2. Frozen repository evidence

The platform lineage is reconstructable and materially consistent:

- Issue #79 terminal `5269737407`: original reversible PC-first candidate.
- Issue #92 terminal `5270335386`: corrected freshness/provenance packet at
  exact head `9d51099be4d53eff876104f482e3c163d34519e3`.
- Corrected report blob:
  `d6a20c2200cedad97ede36beb9871d420ca7a8ca`.
- Immutable normalized source-record blob:
  `f2a9333436c9cbc4fe91ec71507997f46f2247e4`.
- Issue #100 terminal `5271940062`: independent disposition
  `CLEAN_FOR_W2_REVIEW_INPUT`, 0 BLOCKER / 0 MAJOR /
  0 correction-requiring MINOR.
- Issue #92 integration `5277976287` and Review #100 integration
  `5278072607`: exact packets published on main only as noncanonical
  planning/review provenance.
- Issue #1031 terminal `5651299741`: platform scope remained OPEN because the
  reversible planning candidate had not yet been separately authorized as the
  implementation target scope.
- Issue #1038 terminal verification `5651326367`: PASSed that blocked
  representation and preserved the same OPEN_BOUNDED platform predicate.
- Issue #84 owner directive `5889817307`: directs a bounded Godot first
  playable after exact readiness closures and fresh verification.

No source above grants a release commitment. This closure does not convert one
into such a commitment.

## 3. Current-source freshness check — 2026-09-29

Only facts capable of changing the PC-first envelope were refreshed.

### Windows support baseline

Microsoft's current Windows 11 Home and Pro lifecycle page still marks the
product family **In Support**. Current listed releases include 25H2 and 26H1;
therefore the first-playable target can remain a supported Windows 11 64-bit
desktop without freezing a release-shipping minimum OS here.

Source:
`https://learn.microsoft.com/lifecycle/products/windows-11-home-and-pro`

### Steam Deck / SteamOS compatibility surface

Valve's current Steam Deck and Steam Machine compatibility documentation still
requires the load-bearing Deck behaviors consumed by the reviewed envelope:
controller access to all content, active-input glyph correctness,
controller-usable text input when text entry exists, playable default
performance (30 fps at 800p on Deck), supported Deck resolution, and readable
small-display text. Windows builds without native Linux builds continue to run
through Proton for this compatibility surface.

Source:
`https://partner.steamgames.com/doc/steamhardware/compat`

### Directional Steam-user evidence

Valve's latest visible Steam Hardware & Software Survey is **August 2026**:
Windows is 93.95% of participating systems and Windows 11 64-bit is 70.97% of
all surveyed systems. As required by the reviewed decision rule, this remains
directional evidence only and is not the authority selecting the platform.

Source:
`https://store.steampowered.com/hwsurvey/hw/`

### Freshness disposition

No refreshed fact triggers a `PLAT-PC-FIRST-R1` flip/reopen condition.
The decisive basis remains reversibility, evidence coverage, a supported
primary desktop baseline, and containment of partner-gated unknowns.

## 4. Exact bounded first-playable platform scope

The closure candidate binds parent envelope `PLAT-PC-FIRST-R1` to the
following implementation scope:

### Required primary execution target

- **Windows 11 64-bit desktop** on a Microsoft-supported Home/Pro release at
  execution time.
- The exact OS release/build used by automated and human first-playable runs
  must be recorded with the implementation evidence.
- No minimum shipping OS, hardware floor, storefront, or release-support period
  is selected by this closure.

### Required portability / UX evidence target during the first-playable tranche

- **Steam Deck / SteamOS via the normal Windows build and Proton** remains the
  required compatibility evidence target from `PLAT-PC-FIRST-R1`.
- When the slice exposes the relevant surface, evidence must cover controller
  access, active glyphs, controller-usable text entry, 1280x800 layout/readability,
  and representative default-performance behavior.
- This is an implementation/test obligation for the bounded slice, not a claim
  of Steam Deck Verified status, native Linux support, or launch support.

### Conditional or deferred surfaces

- native Linux desktop: conditional;
- macOS Apple silicon: conditional;
- additional PC storefronts: optional/conditional;
- Xbox, PlayStation, Nintendo: deferred and partner-gated;
- iOS/iPadOS/Android: deferred product scope.

The Godot project must keep persistent gameplay meaning and platform services
separable enough that these deferred targets can be reopened without rewriting
canonical gameplay state semantics.

## 5. Why this closes only the first-playable predicate

The old OPEN state had two layers that must not be conflated:

1. a reviewed reversible platform envelope already existed; and
2. no authority had bound that envelope to the implementation transition.

The owner directive `5889817307` now provides the missing bounded transition
purpose. It directs a Godot first playable, explicitly distinguishes it from
production/release, and requires the exact readiness closures to be reviewed
and then independently re-verified.

Therefore this producer concludes:

`platform_scope_predicate = SATISFIED_FOR_FIRST_PLAYABLE_SCOPE`

for the exact packet above, **subject to required Review #1340 and later
aggregate readiness verification**.

It does **not** conclude:

- shipping-platform commitment;
- Steam storefront commitment or exclusivity;
- Steam Deck Verified status;
- native Linux/macOS support;
- console/mobile support;
- platform certification;
- production/release readiness;
- aggregate implementation readiness.

## 6. Fail-closed reopen conditions

Reopen this root token before or during first-playable verification if:

1. Windows 11 ceases to be a supported/credible primary desktop baseline for
   the target evidence scope;
2. the selected Godot version cannot execute the required Windows/Deck evidence
   path as assumed;
3. Deck/SteamOS criteria materially change or the Windows-build/Proton path is
   no longer viable;
4. accessibility evidence shows this input/display envelope is insufficient;
5. measured implementation cost makes the required Deck evidence target
   disproportionate or invalidates reversibility;
6. product authority promotes native Linux, macOS, console, mobile, or a
   specific storefront into a mandatory first-playable requirement;
7. any exact source identity or controlling authority used here is invalidated.

Release/certification commitments always require their own later authority;
their absence does not reopen this bounded first-playable root unless they
become an explicit dependency of the first-playable scope.

## 7. Required next route and authority boundary

Required independent review:
`W2-READY-PLATFORM-CLOSE-REV-01` / Issue #1340.

A clean review may make only this exact root token consumable by the bounded
readiness reconciliation route. Producer authorship cannot self-grant aggregate
implementation readiness.

This packet grants no production/release/legal/certification authority, no
final canon, no integration-by-authorship authority, and no implementation
beyond whatever a later fresh readiness verifier explicitly authorizes.
