#!/usr/bin/env python3
"""Deterministic reconstruction fixture for W2-REM-SIM-01.

Planning-experiment evidence only. This does not implement production game logic
and does not provide shared-kernel, engine-selection, readiness, or release authority.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

CORPUS_FILE = "sim-parity-corpus-v1.json"
RESULT_FILE = "sim-parity-model-result-v1.json"
CORPUS_DOMAIN = b"everfield.sim-parity-corpus.v1\0"
RESULT_DOMAIN = b"everfield.sim-parity-model-result.v1\0"
EXPECTED_CORPUS_SCHEMA = "SIM-PARITY-CORPUS-v1"
EXPECTED_RULES_VERSION = "sim.parity.synthetic.v1"
EXPECTED_CONTENT_VERSION = "sim.parity.content.v1"

def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_corpus(path: Path) -> tuple[dict[str, Any], bytes, str]:
    raw = path.read_bytes()
    parsed = json.loads(raw.decode("utf-8"))
    canonical = canonical_bytes(parsed)
    if raw != canonical:
        raise SystemExit("corpus file is not exact canonical UTF-8 JSON bytes")
    if parsed.get("schema") != EXPECTED_CORPUS_SCHEMA:
        raise SystemExit("unexpected corpus schema")
    if parsed.get("rules_version") != EXPECTED_RULES_VERSION:
        raise SystemExit("unexpected rules version")
    if parsed.get("content_version") != EXPECTED_CONTENT_VERSION:
        raise SystemExit("unexpected content version")
    return parsed, raw, sha256(CORPUS_DOMAIN + raw)

def _reason_for_amount(action: str, n: Any) -> str | None:
    if isinstance(n, bool) or not isinstance(n, int):
        return "INVALID_AMOUNT"
    if action in {"earn", "spend", "gain_xp"}:
        return None if n >= 0 else "INVALID_AMOUNT"
    if action == "advance_day":
        return None if n == 1 else "INVALID_DAY_STEP"
    if action == "craft_crate":
        return None if n == 1 else "INVALID_AMOUNT"
    return None if n > 0 else "INVALID_AMOUNT"

def apply_mutable(state: dict[str, Any], action: list[Any]) -> tuple[bool, str | None]:
    """Evaluator A: mutate in place, rolling back rejected actions."""
    before = copy.deepcopy(state)
    if not isinstance(action, list) or len(action) != 2:
        return False, "UNKNOWN_ACTION"
    name, n = action
    if not isinstance(name, str):
        return False, "UNKNOWN_ACTION"
    known = {
        "earn", "spend", "buy_seed", "plant", "advance_day", "sell_crop",
        "gain_xp", "gather_wood", "craft_crate",
    }
    if name not in known:
        return False, "UNKNOWN_ACTION"
    amount_reason = _reason_for_amount(name, n)
    if amount_reason:
        return False, amount_reason

    reason: str | None = None
    if name == "earn":
        state["coins"] += n
    elif name == "spend":
        if state["coins"] < n:
            reason = "INSUFFICIENT_COINS"
        else:
            state["coins"] -= n
    elif name == "buy_seed":
        if state["coins"] < 2 * n:
            reason = "INSUFFICIENT_COINS"
        else:
            state["coins"] -= 2 * n
            state["seed"] += n
    elif name == "plant":
        if state["seed"] < n:
            reason = "INSUFFICIENT_SEED"
        else:
            state["seed"] -= n
            state["pending_crop"] += n
    elif name == "advance_day":
        state["day"] += 1
        state["crop"] += state["pending_crop"]
        state["pending_crop"] = 0
        state["energy"] = 10
    elif name == "sell_crop":
        if state["crop"] < n:
            reason = "INSUFFICIENT_CROP"
        else:
            state["crop"] -= n
            state["coins"] += 4 * n
    elif name == "gain_xp":
        state["xp"] += n
        state["level"] = 1 + state["xp"] // 10
        if state["level"] >= 2 and "workshop" not in state["unlocks"]:
            state["unlocks"].append("workshop")
            state["unlocks"].sort()
    elif name == "gather_wood":
        if state["energy"] < n:
            reason = "INSUFFICIENT_ENERGY"
        else:
            state["energy"] -= n
            state["wood"] += n
    elif name == "craft_crate":
        if "workshop" not in state["unlocks"]:
            reason = "WORKSHOP_LOCKED"
        elif state["wood"] < 3:
            reason = "INSUFFICIENT_WOOD"
        else:
            state["wood"] -= 3
            state["coins"] += 5

    if reason is not None:
        state.clear()
        state.update(before)
        return False, reason
    return True, None

def apply_pure(state: dict[str, Any], action: list[Any]) -> tuple[dict[str, Any], bool, str | None]:
    """Evaluator B: return a copied next state; never mutate rejected input."""
    if not isinstance(action, list) or len(action) != 2:
        return copy.deepcopy(state), False, "UNKNOWN_ACTION"
    name, n = action
    if not isinstance(name, str):
        return copy.deepcopy(state), False, "UNKNOWN_ACTION"
    known = {
        "earn", "spend", "buy_seed", "plant", "advance_day", "sell_crop",
        "gain_xp", "gather_wood", "craft_crate",
    }
    if name not in known:
        return copy.deepcopy(state), False, "UNKNOWN_ACTION"
    amount_reason = _reason_for_amount(name, n)
    if amount_reason:
        return copy.deepcopy(state), False, amount_reason

    next_state = copy.deepcopy(state)
    if name == "earn":
        next_state["coins"] = state["coins"] + n
    elif name == "spend":
        if state["coins"] < n:
            return copy.deepcopy(state), False, "INSUFFICIENT_COINS"
        next_state["coins"] = state["coins"] - n
    elif name == "buy_seed":
        if state["coins"] < 2 * n:
            return copy.deepcopy(state), False, "INSUFFICIENT_COINS"
        next_state["coins"] = state["coins"] - 2 * n
        next_state["seed"] = state["seed"] + n
    elif name == "plant":
        if state["seed"] < n:
            return copy.deepcopy(state), False, "INSUFFICIENT_SEED"
        next_state["seed"] = state["seed"] - n
        next_state["pending_crop"] = state["pending_crop"] + n
    elif name == "advance_day":
        next_state["day"] = state["day"] + 1
        next_state["crop"] = state["crop"] + state["pending_crop"]
        next_state["pending_crop"] = 0
        next_state["energy"] = 10
    elif name == "sell_crop":
        if state["crop"] < n:
            return copy.deepcopy(state), False, "INSUFFICIENT_CROP"
        next_state["crop"] = state["crop"] - n
        next_state["coins"] = state["coins"] + 4 * n
    elif name == "gain_xp":
        next_state["xp"] = state["xp"] + n
        next_state["level"] = 1 + next_state["xp"] // 10
        next_state["unlocks"] = sorted(
            set(state["unlocks"]) | ({"workshop"} if next_state["level"] >= 2 else set())
        )
    elif name == "gather_wood":
        if state["energy"] < n:
            return copy.deepcopy(state), False, "INSUFFICIENT_ENERGY"
        next_state["energy"] = state["energy"] - n
        next_state["wood"] = state["wood"] + n
    elif name == "craft_crate":
        if "workshop" not in state["unlocks"]:
            return copy.deepcopy(state), False, "WORKSHOP_LOCKED"
        if state["wood"] < 3:
            return copy.deepcopy(state), False, "INSUFFICIENT_WOOD"
        next_state["wood"] = state["wood"] - 3
        next_state["coins"] = state["coins"] + 5
    return next_state, True, None

def run_mutable(corpus: dict[str, Any]) -> list[dict[str, Any]]:
    results = []
    for scenario in corpus["scenarios"]:
        state = copy.deepcopy(corpus["initial_state"])
        trace = []
        accepted_count = 0
        for index, action in enumerate(scenario["actions"], start=1):
            pre = copy.deepcopy(state)
            accepted, reason = apply_mutable(state, action)
            if accepted:
                accepted_count += 1
            trace.append({
                "index": index,
                "action": action,
                "accepted": accepted,
                "reason": reason,
                "pre_state": pre,
                "post_state": copy.deepcopy(state),
            })
        results.append({
            "id": scenario["id"],
            "accepted": accepted_count,
            "rejected": len(scenario["actions"]) - accepted_count,
            "final_state": copy.deepcopy(state),
            "trace": trace,
        })
    return results

def run_pure(corpus: dict[str, Any]) -> list[dict[str, Any]]:
    results = []
    for scenario in corpus["scenarios"]:
        state = copy.deepcopy(corpus["initial_state"])
        trace = []
        accepted_count = 0
        for index, action in enumerate(scenario["actions"], start=1):
            pre = copy.deepcopy(state)
            next_state, accepted, reason = apply_pure(state, action)
            if accepted:
                accepted_count += 1
            state = next_state
            trace.append({
                "index": index,
                "action": action,
                "accepted": accepted,
                "reason": reason,
                "pre_state": pre,
                "post_state": copy.deepcopy(state),
            })
        results.append({
            "id": scenario["id"],
            "accepted": accepted_count,
            "rejected": len(scenario["actions"]) - accepted_count,
            "final_state": copy.deepcopy(state),
            "trace": trace,
        })
    return results

def build_result(corpus: dict[str, Any], corpus_digest: str, source_digest: str) -> dict[str, Any]:
    mutable = run_mutable(corpus)
    pure = run_pure(corpus)
    if canonical_bytes(mutable) != canonical_bytes(pure):
        raise SystemExit("independent evaluator disagreement")
    return {
        "schema": "SIM-PARITY-MODEL-RESULT-v1",
        "evidence_version": "W2-REM-SIM-01-v1",
        "corpus_schema": corpus["schema"],
        "corpus_sha256": corpus_digest,
        "evaluator_source_sha256": source_digest,
        "independent_evaluator_agreement": {
            "evaluators": ["mutable_rollback", "pure_copy"],
            "scenario_count": len(mutable),
            "exact_normalized_trace_result_equality": True,
        },
        "scenarios": mutable,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path)
    parser.add_argument("--expected-result", type=Path)
    parser.add_argument("--emit-result", type=Path)
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    corpus_path = args.corpus or (here / CORPUS_FILE)
    expected_path = args.expected_result or (here / RESULT_FILE)

    corpus, corpus_raw, corpus_digest = load_corpus(corpus_path)
    source_digest = sha256(Path(__file__).read_bytes())
    result = build_result(corpus, corpus_digest, source_digest)
    result_raw = canonical_bytes(result)
    result_digest = sha256(RESULT_DOMAIN + result_raw)

    if expected_path.exists():
        expected_raw = expected_path.read_bytes()
        if expected_raw != result_raw:
            raise SystemExit("retained result bytes do not match fresh evaluator output")

    if args.emit_result:
        args.emit_result.write_bytes(result_raw)

    summary = {
        "status": "PASS",
        "corpus_file_sha256": sha256(corpus_raw),
        "corpus_sha256": corpus_digest,
        "evaluator_source_sha256": source_digest,
        "result_file_sha256": sha256(result_raw),
        "result_sha256": result_digest,
        "scenario_count": len(result["scenarios"]),
        "agreement": result["independent_evaluator_agreement"],
        "shared_kernel_execution_count": 0,
        "parity_pass": 0,
        "parity_fail": 0,
        "parity_inconclusive": len(result["scenarios"]),
    }
    print(canonical_bytes(summary).decode("utf-8"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
