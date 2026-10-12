# Issue #1651 — public route-history remediation handoff

**HANDOFF_READY — NOT REVIEW_READY, NOT VERIFIED, NOT INTEGRATED.**

## Authority and immutability

Mandatory blocking remediation following independent review #1643 terminal #6107756342 (1 BLOCKER FSR-1643-B01, 2 MAJOR FSR-1643-M01/M02, 0 MINOR); review-only draft PR #1649 HEAD b91ce4d6b407a7af641dd836850ace2d68426f82. First valid sole claimant for this source task: Issue #1651 CLAIM #6107767990 (server 2026-10-11T09:52:41Z), distinct actor frontier-route-history-remediate-1651-gpt6-20261011-1156-01. Separate from original #1627 producer, #1627 continuation, required reviewer #1643 and scoped verifier #1635.

Current main at episode baseline 3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d, canonical Issue #1147 binding #5675066392, canonical program blob fd4cf1119c3f86acc3af620024eea72235e81ce4, activation ancestor 87c85cecfa9a2ffa464c4b36816a138bf41441af. Frozen source #1627 draft PR #1630 HEAD ba8325232de970400352782e77506e5b1dfba91b, original verifier-only PR #1637 HEAD f845de3f2eba9a021d72b34941729007aa372f1c. Both unmerged and unchanged. Original 33-check Godot 4.7.1 PASS #38126793303 is verification of the OLD SOURCE ONLY.

## Exactly four scoped paths

- game/components/route_history_view/route_history_view.gd — corrected source blob 8f32a8e925d8fb0765e91ef102ad0827a0b88958
- game/tests/route_history_view/route_history_view_smoke.gd — new adversarial Godot suite blob 298916bbdd839e2094c4e2695e305f1142bb3e30
- docs/planning/handoffs/issue-1627.md — byte-identical inherited original blob 75b37ba2c7d38f9cf3371590ac476d80af116448
- docs/planning/handoffs/issue-1651.md — this new owned handoff; record its final blob in the issue STATUS

Branch planning/issue-1651 is based on main, not original source branch. No scene, sibling public-text, canonical source, shared CI, prior source/reviewer/verifier code or unrelated producer paths changed.

## Corrected findings

**FSR-1643-B01:** The former source accepted recognized history IDs regardless of contradictory session completion flags. New read-only _history_consistent replays the exact published main.gd event-ordered state transitions and compares all seven current state fields and required nine-key snapshot contract. Hearing requires record plus trace or explicit truth deferral; commitments require open hearing; each outcome requires a matching earlier selected commitment. The exact completed, outcome, commitment, hearing, investigated record, inspected trace and deferred-truth values must match the replay. The source maintains legal repeated deferral/reopened hearing, repeated choices and earlier completion retained after later reassessment. The published controller also permits completion while a newly reopened hearing is open: the new code and regression honor that, rather than inventing a new gate. Forged initial empty session + an allowlisted completed outcome, hearing or commitment fails closed.

This is strict **cross-state consistency**, not cryptographic origin attestation: a fully self-consistent forged Dictionary is not provably historical. The separately reviewed scene fan-in must supply genuine SessionState.snapshot() from the published controller and must never treat the model as a sovereign provenance oracle.

**FSR-1643-M01:** Model now accepts only live objects whose get_script() matches the two exact preloaded reviewed World and Consequence presentation scripts, plus the actual nonprivate, nonconsent and no-mutation contract guards. A contract-compatible arbitrary RefCounted implementation cannot substitute text from a made-up get_text; real provider getters remain the sole source of approved public title text. No private Anwen text, new narrative, consent conclusion or historical truth is added.

**FSR-1643-M02:** A finite explicit MAX_HISTORY_EVENTS=256 input budget rejects oversize snapshots without echoing IDs or silently deleting history. All accepted history events are fully state-checked; each numbered requested page materializes only PAGE_SIZE=8 entries and lines. Return metadata count (total), page, page_count, page_size, window_start/end, has_previous/has_next makes all ordered duplicates and reopening/nonconsent reachable. Invalid pages fail closed. The original session history is immutable. Eight entries are a model budget, NOT an empirical claim of fitting the published 422x134 visible label and NOT accessibility certification; UI navigation remains for separate shared fan-in.

The new isolated Godot SceneTree test exercises empty and reset, original genuine seven-event records-first path, matching states, contradictory forged allowed-ID completion/choice/hearing and malformed shapes, provider spoofing despite matching contract flags, genuine repair path and changed commitment after re-open, controller-permitted completion during open hearing, repeated hearing/nonconsent 39-event history rebuilt across all pages, finite text/page flags, oversize >256, no private ID echo and preservation of source/returned snapshots.

## Source episode test limitation — independent verification remains mandatory

No local Godot binary is installed; container DNS/internet cannot obtain the reviewed 4.7.1 executable. A separate local Python check only sanity-checked the intended seven-event replay and is **NOT Godot syntax/runtime evidence**. No new source-head Godot test has executed. Do not promote source to REVIEW_READY on producer-authored logic, old 33-check source-verifier PASS or green unrelated CI.

**Next mandatory route:** materialize one distinct independent read-only Godot verifier issue and draft verification-only workflow based on old frozen #1635 workflow source blob a24ddb04896b2cebbca606b8746d51dfb4578c4d, but explicitly pin the ACTUAL FINAL PR HEAD OF #1651, corrected model/test blob identities and byte-identical #1627 handoff. Require reviewed engine ZIP SHA256 c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba and exact Godot version 4.7.1.stable.official.a13da4feb. On a read-only exact-head hosted runner, run godot --headless --path game --script res://tests/route_history_view/route_history_view_smoke.gd and demand EVERFIELD_ROUTE_HISTORY_VIEW_PASS checks=N, exit 0, no SCRIPT ERROR / Parse Error / Assertion failed / [EVERFIELD][ROUTE-HISTORY][FAIL], plus actual original first-playable and movement regression suites. Archive raw logs/source SHA/binary ZIP SHA/version/run and job identity. Independently inspect final verifier workflow PR head and artifact before claiming PASS.

If execution fails, valid HANDOFF RESUME on existing #1651 is needed to correct the two owned source/test files and repeat final-head independent verification. If it genuinely passes, valid HANDOFF RESUME on #1651 must recheck current main, winning ownership, exact PR head and verification evidence before owner STATUS(REVIEW_READY). Then a **new separate required independent adversarial source reviewer** must find 0 BLOCKER, 0 MAJOR and 0 correction-requiring MINOR before any separately authorized **squash-only NONCANONICAL** source integration. Keep all verifier/review-only PRs draft/unmerged. Scene fan-in #1629 still separately gated by scoped route-history #1651 and public-text #1626 chains.

No integration, canonicality, engine-selection, gameplay truth/consent, accessibility certification, implementation-readiness, production or release authority.
