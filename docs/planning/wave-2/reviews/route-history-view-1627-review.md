# Required independent adversarial review — route-history source #1627

**Review issue / mission:** #1643, `IMPLEMENTATION-DEMAND-ROUTE-HISTORY-VIEW-04-REV-01`
**Reviewer generation:** first-valid unedited schema-3 CLAIM #6107719360, separate actor `frontier-independent-route-history-review-1643-gpt6-20261011-1144-01`.
**Frozen producer:** #1627 terminal REVIEW_READY #6107453981, draft PR #1630 at HEAD `ba8325232de970400352782e77506e5b1dfba91b`, unmerged.
**Disposition:** **CHANGES_NEEDED** — **1 BLOCKER / 2 MAJOR / 0 correction-requiring MINOR**. Review-only; not a gameplay-source or verification merge authorization.

## Exact canonical, ownership, compatibility and source evidence

Current `main` at the review baseline is `3d7ce70fbc4e1c26224f01c6aa3a3fc18cf3902d`. Active canonical Planning Program Issue #1147 unedited INTEGRATION_STATUS #5675066392 binds exact blob `fd4cf1119c3f86acc3af620024eea72235e81ce4` and activation main ancestor `87c85cecfa9a2ffa464c4b36816a138bf41441af`. Reviewer first valid CLAIM #6107719360, immediately rechecked as sole operational contender. Reviewer is distinct from original producer `frontier-implement-route-history-1627-gpt6-20261011-0932-01`, producer HANDOFF successor `frontier-resume-route-history-1627-gpt6-20261011-1109-01`, and scoped verifier `frontier-verify-route-history-1635-gpt6-20261011-1055-01`. Producer HANDOFF #6106737792, winning RESUME_INTENT #6107443578, RESUME #6107445592 and terminal #6107453981 are chronologically in lease, and the original source is still unmerged and open/draft. Independent GitHub compare from this main to the producer HEAD reports three commits ahead, zero behind and **exactly three added files**:

| Source path | Verified immutable blob |
| --- | --- |
| `game/components/route_history_view/route_history_view.gd` | `8539cd5afb990a5702100e5ae2abdab38b27debe` |
| `game/tests/route_history_view/route_history_view_smoke.gd` | `bf968b39d7a161e2f44e5ff94f5536607b89db9d` |
| `docs/planning/handoffs/issue-1627.md` | `75b37ba2c7d38f9cf3371590ac476d80af116448` |

The verified existing producers on main were re-read: `game/components/session_state/session_state.gd` blob `97a0d4f35f9ffe3ed813a67d24daeb3aff08f398`; public World presentation `8e498156bb9a5413f53a84b14fc279c4be6c8f23`; consequence presentation `419688e17515bf5f67b383182c0b6330111ce4be`; scene controller `game/main.gd` blob `921ff7a1ce28ed4df4a67a7645752d7b441603f7`. Their world/consequence title IDs match the source lookup table; `COMMONS_HEARING_OPENED` uses the already-published hearing heading. No Anwen/private ID appears in the accepted event map; unknown/private IDs fail with a constant diagnostic rather than being echoed.

**Real independent runtime evidence, scoped:** #1635 `VERIFICATION_STATUS(DONE,result=PASS)` #6107400681, its verifier-only draft PR #1637 HEAD `f845de3f2eba9a021d72b34941729007aa372f1c`, actual read-only GitHub Actions `pull_request` run [38126793303](https://github.com/vokerg/everfield/actions/runs/38126793303) at that exact verifier HEAD with `verify-frozen-source` job #114432721224 `success`. Job steps checked out immutable source HEAD, verified source hashes and reviewed Godot 4.7.1 ZIP lock SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`, and ran new isolated `EVERFIELD_ROUTE_HISTORY_VIEW_PASS checks=33` plus existing first-playable and movement regression smokes. Genuine archived artifact #11697318047 SHA256 `fb04134e038e74b89d98bf65a6216e73e20d695c5da6d726c9f4ecdd6bd8ac90` is reported in verified terminal. This **establishes tested positive/selected negative behavior only**, not adversarial acceptance or full visual/accessibility certification. The current reviewer independently read actual source, provider contracts, API metadata, run/job conclusion and steps, not the archived ZIP content, and **did not independently run Godot** (no local binary in the reviewer environment). Negative witnesses below follow deterministically from inspected code, not claims of executed Godot negatives.

## FSR-1643-B01 — BLOCKER: forged session history passes and fabricates completed public commitment

`build_view` authenticates only `typeof(snapshot) == TYPE_DICTIONARY`, `mystery_state == UNKNOWN_BY_DESIGN`, and `history` as an array of recognized strings. It does **not** validate the session snapshot contract or history against the other published state fields (`commitment`, `outcome`, `completed`, `negotiation_open`, etc.), nor bind input to a trusted `SessionState.snapshot()` producer. This exact negative witness uses *real reviewed providers*:

```gdscript
var session = SessionState.new()
var forged = session.snapshot()          # all fields represent an empty uncompleted route
forged["history"] = ["RECORDS_FIRST_PACKAGE_FILED"]
var view = HistoryView.new().build_view(
    forged, OldWorksWorld.new(), Consequences.new())
# Deterministic by reviewed source: view["ok"] == true;
# view["entries"][0]["title"] == "Records First — Package Filed";
# session.snapshot()["history"] remains [], completed remains false.
```

The event ID is in `CONSEQUENCE_TITLES`; `_valid_public_sources` accepts genuine providers, and `get_text("OW_CONSEQ_RECORDS_TITLE")` returns the reported positive nonempty title. Thus an internally contradictory / substituted snapshot falsely projects a publicly completed action without any matching session commitment or completion. The smoke tests exercise forged **unknown IDs and wrong types**, but never valid-allowlist IDs in a false session state. It would be unsound to publish such a source as a provenance-safe public route-history readout or imply consent/completion. The reviewed `SessionState.append_history` itself accepts allowlisted IDs independent of progression state; the source must specify an enforceable trusted-snapshot/state consistency boundary rather than treating the allowlist as event authenticity. **Required correction:** reject inconsistent/untrusted route histories without accidentally rejecting legitimate deferral, hearing reopen, repeat records, repair, records-first, reset, or explicit nonconsent. Add executable negative and positive Godot coverage and reverify exact corrected source HEAD.

## FSR-1643-M01 — MAJOR: forged provider contracts can authorize arbitrary public title prose

`_valid_public_sources` accepts any two `TYPE_OBJECT` values exposing `get_contract`/`has_text`/`get_text` (world) and `get_contract`/`get_text` (consequence). It checks only two readily spoofed contract fields in each dictionary, not immutable reviewed provider identity, complete contract, or a fail-closed approved title-value mapping. `_public_title` then directly trusts nonempty arbitrary `get_text` strings. A synthetic RefCounted provider returning `{"mystery_state":"UNKNOWN_BY_DESIGN","public_record_exposes_private_information":false}`, `has_text("OW_ARCHIVE_TITLE")==true`, and `get_text("OW_ARCHIVE_TITLE")=="FORGED PUBLIC FACT"` passes the tested world-source conditions; a likewise forged consequence contract with `deferral_is_consent_in_waiting:false` passes its conditions. A snapshot with `history:["PUBLIC_RECORD_REVIEWED"]` then renders the injected title. No private disclosure is asserted for the genuine reviewed providers; this is a **conditional API trust-boundary** defect for substituted/malicious sources, contrary to the required forged-contract negative scope. Add distinct spoofed-source negative/real-source positive tests and guard title authenticity on the route-history boundary. Do not infer a live exploitation path through the currently unmodified scene.

## FSR-1643-M02 — MAJOR: unbounded history/line expansion is not a bounded presentation contract

Neither `SessionState.append_history` nor `HistoryView.build_view` places any count or rendered-text bound. For every array entry `build_view` allocates an entry Dictionary, a string line, a joined final string and a deep duplicate of the entries. A valid, allowed repeat like `COMMONS_HEARING_OPENED` may occur arbitrarily many times; a forged snapshot can also supply an arbitrarily large allowed-event array, with no reject/truncate/page predicate. The exact test fixture has only seven events; its 33-check success says nothing about extremely long session histories or a finite visible panel. Consequences are unbounded display text, memory and processing, potentially hiding nonconsent/reopening context in the UI; there is no viewport/pagination evidence. **Required correction:** enforce an explicit finite, testable policy (bounded record/paging/window and deterministic visible text) preserving true order, duplicates, and full session history semantics; test edge/boundary/oversize inputs and fail closed rather than silently rewriting history. Empirical viewport/accessibility certification remains separate.

## Positive controls and scope limitations

- Empty genuine snapshot yields no fabricated entry; genuine allowlisted deferral → reopened hearing → records-first run keeps event order, indices, duplicate hearing, reviewed providers and immutable `UNKNOWN_BY_DESIGN`; 33-check independent locked engine smoke proves these tested cases.
- Unknown/private event IDs and malformed history types currently reject with constant player-facing failure and no private ID echo; returned entry mutation does not poison source snapshots/providers, and scene/shared CI/sibling component paths are not touched.
- Reviewed provider APIs supply exact legacy approved World/Consequence titles. No false global gating of separate public-text #1626 work, no assertion that current controller uses this unwired component, no runtime exploit or secret disclosure claimed. Source #1630 is an isolated component awaiting the blocked fan-in #1629 after each scoped chain completes.
- No local Godot executable or reviewed headless fixture injection was available to this independent reviewer. The B01 witness is deterministic direct source reasoning; M01/M02 are adversarial interface/complexity reasoning. Treat them as **unresolved correction-requiring findings**, not PASS.
- Review-only two-document output must never be integrated as game source; this report does not self-authorize remediation, verification, integration, canonicalization, truth/consent legitimacy, accessibility certification, production or release.

## Required-next-route and disposition

**`REVIEW_STATUS(CHANGES_NEEDED)`** with **1 BLOCKER (FSR-1643-B01), 2 MAJOR (FSR-1643-M01/M02), 0 correction-requiring MINOR**. Materialize **one** bounded required remediation successor inheriting frozen exact source HEAD and independent verifier evidence, correcting only the route-history component/test plus its new handoff from fresh main. Demand a fresh locked Godot 4.7.1 actual exact-corrected-head scoped verification, then a **different** independent adversarial review of corrected code before any separately owned squash-only NONCANONICAL source integration. Leave original PR #1630 and verifier-only PR #1637 draft/unmerged/frozen. Fan-in #1629 remains blocked; no new global gate.
