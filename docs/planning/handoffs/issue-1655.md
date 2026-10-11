# Issue #1655 — independent executable verification of frozen public-text navigation #1626

## Role, eligibility and current work state

Mandatory distinct scoped Godot 4.7.1 runtime verifier, mission `IMPLEMENTATION-VERIFY-PUBLIC-TEXT-NAVIGATION-1626-02`. Independent from broader producer/resume #1626 authoring execution (`frontier-resume-public-text-navigation-1626-gpt6-20261011-1206-01`) and prior #1642 empirical measurement. Fresh first-valid unedited schema-3 CLAIM **#6109052214**, verifier actor `frontier-distinct-public-text-verifier-1655-gpt6-20261011-1432-cph-01`. Post-CLAIM rechecked GitHub server times, sole valid owner, canonical program/binding and exact source PR. Branch `planning/issue-1655` created from exact then-current `main@3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`.

**State: HOSTED SOURCE VERIFICATION NOT YET TERMINAL.** Authoring read-only workflow alone confers no proof. Will bind actual hosted run/jobserver/artifact only after exact final-verifier-PR-HEAD execution. If runner finds source defect, record negative, handoff original source #1626, do not fabricate PASS.

## Frozen corrected producer source and authority

- Source Issue #1626 original owner CLAIM #6107400582, prior corrected viewport probe HANDOFF #6107651917, valid separate producer HANDOFF RESUME_INTENT #6107889528 / RESUME #6107894292 and **latest HANDOFF_READY #6107964587**. Exact OPEN/DRAFT source PR **#1641 HEAD `d4d6ce1f55670fa6c7986a05cf82a2face4d398d`** is not source verified by earlier #1642.
- Only source PR changed paths and immutable GitHub Git blob identities:
  1. `game/components/public_text_navigation/public_text_navigation.gd` `b081bfe234c18884650992d7251b55effbec8c2f`;
  2. `game/tests/public_text_navigation/public_text_navigation_smoke.gd` `ff355251c9b2f303c5c9ba1633a6a0b18b6689a3`;
  3. `game/tests/public_text_navigation/public_text_fit_smoke.gd` `a64c88036f95f4b9e7a84219fb3bd5ebd8b6bd9a`;
  4. `docs/planning/handoffs/issue-1626.md` `c5a2fc1e8270bfdec2d7d903a804a4bbe3184883`.
- Previous independent measurement verification #1642 terminal #6107838152, old #1645 verifier only, 13 scenarios with 7 nominally over 134px at 960x540; it does **not** prove new pagination/real scene fit or accessibility. Current source isolated navigation smoke is new and not covered by common first-playable CI.
- Canonical planning program Issue #1147 binding #5675066392, program blob `fd4cf1119c3f86acc3af620024eea72235e81ce4`, activation ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`.

## Exclusive immutable verifier branch/PR scope

Only two own branch paths may change:
- `.github/workflows/verify-public-text-navigation-1626.yml` initial Git blob **`28f8bbc4886dfcac5343b973221ec627df97b6f3`**, new pinned read-only workflow, not an inherited old-verifier mutation;
- `docs/planning/handoffs/issue-1655.md`, this durable handoff.

Workflow triggers only on relevant verifier-only PR file changes targeting main, GitHub Actions read-only permissions, runner Ubuntu 24.04, SHA-pinned checkout & artifact upload. Crucially source checkout is immutable **`d4d6ce1f55670fa6c7986a05cf82a2face4d398d`**, never verifier PR code or default main. Assert all four exact source blob IDs and reviewed project `game/project.godot` Git blob `9da4153ed378945ef5e9634e0e5cae48289845d8`, archive source/published provider Git tree, Git/source SHA manifest, verifier PR HEAD and run identity.

Reviewed immutable official Godot artifact lock `docs/planning/wave-2/evidence/ci/engine-toolchain-artifact-lock.json` blob `4a88990ae24768eb4f83a8a1311e2a830834649f`, ZIP URL `https://github.com/godotengine/godot/releases/download/4.7.1-stable/Godot_v4.7.1-stable_linux.x86_64.zip`, sha256 **`c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`**, binary full version **`4.7.1.stable.official.a13da4feb`**. Download, enforce SHA check before executing. On exact source, call `godot --headless --path game --script res://tests/public_text_navigation/public_text_navigation_smoke.gd`, require exit 0, **exactly one** full-line `EVERFIELD_PUBLIC_TEXT_NAV_PASS checks=N` with N positive, zero source `SCRIPT ERROR`, `Parse Error`, `Assertion failed`, `[EVERFIELD][PUBLIC-TEXT-NAV][FAIL]`. New source smoke covers 13 reviewed provider cases, exact text/line breaks and SHA preservation, next/back bounds, no private text leakage, fail-closed malformed inputs, read-only session state and provider contract. Execute existing first-playable and movement/interaction regressions with same locked engine and negative marker rejection. Archive raw stdout/stderr, immutable runner/source/verifier identities, SHA256 manifests and all CI artifacts; log failures must be preserved.

## Required next steps and terminal gates

1. Open DRAFT verifier-only pull request against current main from owned branch and enumerate exactly two changed paths.
2. Inspect genuine **final PR HEAD** `pull_request` Actions run, exact source checkout, engine/toolchain download/hash checks, isolated positive N sentinel and regression exit statuses, actual uploaded artifact ZIP/archive SHA manifest. If evidence handoff is updated after first hosted run, rerun on **new final verifier HEAD** and use only that for terminal. Never infer PASS from producer tests or PR green unrelated regression workflow.
3. On real final-head positive result, post unedited in-lease `VERIFICATION_STATUS(DONE,result=PASS)` with exact final HEAD/work/source identities, actual run/job/artifact IDs and digest, scoped PASS evidence; route back to valid source Issue #1626 HANDOFF continuation to owner REVIEW_READY and **fresh genuinely independent adversarial source code/security review**. If FAIL, record genuine terminal negative/hand off bounded correction and keep source draft.
4. **Never** merge verifier-only PR, older verifier/reviewer drafts or producer source from verifier role. No mutation of source PR #1641, sibling route-history #1651, shared scene #1629, live providers, main/game or canon. Successful runtime execution certifies only isolated source behavior, not actual world scene integration, viewport clipping/accessibility, consent/truth, final engine, readiness, production or release. Later separately owned current-main-compatible source integration strictly **squash-only NONCANONICAL** after genuine required review gates.
