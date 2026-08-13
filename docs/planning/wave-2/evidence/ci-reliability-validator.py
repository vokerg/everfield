#!/usr/bin/env python3
"""Deterministic synthetic CI evidence validator for Everfield W2-REM-CI-03.

Standard library only. The exact fixture corpus is embedded below. Running this
file emits the canonical evidence bundle and SHA-256 digests, and exits nonzero
if any regression produces an unexpected aggregate.
"""

from __future__ import annotations

import copy
import hashlib
import json
import pathlib
import re
import sys
from typing import Any

VALIDATOR_VERSION = "ci-reliability-reference-v4"
VALIDATOR_SOURCE_IDENTITY_ALGORITHM = "sha256-source-with-digest-line-sentinel-v1"
VALIDATOR_SOURCE_DIGEST = "sha256:97a8fa00d338907e32cd97a7ca662b81ea1fc8336ffd7a9e6541b00162c91b5d"
CANONICAL_JSON_ALGORITHM = "sha256-canonical-json-sorted-compact-v1"
PREDECESSOR_ROOT_ALGORITHM = CANONICAL_JSON_ALGORITHM


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_hex_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_digest(value: Any) -> str:
    return "sha256:" + sha256_hex_bytes(canonical_bytes(value))


def normalized_source_bytes(path: pathlib.Path) -> bytes:
    text = path.read_text(encoding="utf-8")
    normalized = re.sub(
        r'^VALIDATOR_SOURCE_DIGEST = ".*"$',
        'VALIDATOR_SOURCE_DIGEST = "__SOURCE_DIGEST__"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    return normalized.encode("utf-8")


def computed_source_digest(path: pathlib.Path) -> str:
    return "sha256:" + sha256_hex_bytes(normalized_source_bytes(path))


PREDECESSOR_EVIDENCE_ARTIFACT = {
    "schema": "predecessor-evidence-v1",
    "candidate_id": "cand-flaky-v1",
    "evidence_envelopes": [
        {
            "envelope_id": "env-flaky-1",
            "candidate_id": "cand-flaky-v1",
            "requirement_id": "CI-EXP-REQ-v3",
            "check_id": "soak",
            "attempts": [
                {
                    "attempt_id": "soak-a1",
                    "ordinal": 1,
                    "result": "FLAKY",
                    "failure_class": "FLAKY",
                    "artifact_key": "soak-pass",
                    "artifact_id": "art-soak-pass-v3",
                    "expected_hash": "db3d050bfe46b76e8df9b877cbbb21112a9f704e817d9076b6ccf070f8a73452",
                }
            ],
        },
        {
            "envelope_id": "env-flaky-1-static",
            "candidate_id": "cand-flaky-v1",
            "requirement_id": "CI-EXP-REQ-v3",
            "check_id": "static",
            "attempts": [
                {
                    "attempt_id": "static-a1",
                    "ordinal": 1,
                    "result": "PASS",
                    "failure_class": None,
                    "artifact_key": "static-invariant",
                    "artifact_id": "art-static-invariant-v3",
                    "expected_hash": "7c47b7ba6d4c0afbf459d890eb6b1435feb095a15815a10f82ea7c3a30d08423",
                }
            ],
        },
    ],
}


def predecessor_root(artifact: dict[str, Any]) -> str:
    return sha256_hex_bytes(canonical_bytes(artifact))


PREDECESSOR_EVIDENCE_ROOT = predecessor_root(PREDECESSOR_EVIDENCE_ARTIFACT)

ARTIFACT_CATALOG = {
    "package-pass": {
        "artifact_id": "art-package-pass-v3",
        "content_hash": "dc9f6e4b62400949d12a88714711ce5cd0c654d768b825fd8151014c310cd40a",
    },
    "short-soak": {
        "artifact_id": "art-short-soak-v3",
        "content_hash": "6868f5813a37470673ab4fa5bc2dfa2de912092b9d02360866627585edb1dfcb",
    },
    "soak-pass": {
        "artifact_id": "art-soak-pass-v3",
        "content_hash": "db3d050bfe46b76e8df9b877cbbb21112a9f704e817d9076b6ccf070f8a73452",
    },
    "static-invariant": {
        "artifact_id": "art-static-invariant-v3",
        "content_hash": "7c47b7ba6d4c0afbf459d890eb6b1435feb095a15815a10f82ea7c3a30d08423",
    },
    "unit-pass": {
        "artifact_id": "art-unit-pass-v3",
        "content_hash": "9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1",
    },
}

QUARANTINE_POLICY = {
    "candidate_id": "cand-flaky-v1",
    "check_id": "soak",
    "expiry_day": 14,
    "policy_version": "ci-reliability-exp-v3-q1",
    "replacement_ids": ["short_soak", "static_invariant"],
    "requirement_id": "CI-EXP-REQ-v3-q1",
}

TRANSITION = {
    "transition_id": "transition-flaky-v1-to-v2",
    "predecessor_candidate_id": "cand-flaky-v1",
    "successor_candidate_id": "cand-flaky-v2",
    "changed_work_identity": "work:remediate-soak-flake:v1",
    "reason": "bounded remediation after retained flaky evidence",
    "predecessor_evidence_root": PREDECESSOR_EVIDENCE_ROOT,
    "predecessor_evidence_artifact_digest": canonical_digest(PREDECESSOR_EVIDENCE_ARTIFACT),
    "predecessor_root_algorithm": PREDECESSOR_ROOT_ALGORITHM,
}

BASE_REPLACEMENT_EVIDENCE = {
    "short_soak": {
        "replacement_evidence_id": "repl-ev-short_soak",
        "replacement_id": "short_soak",
        "candidate_id": "cand-flaky-v1",
        "requirement_id": "CI-EXP-REQ-v3-q1",
        "policy_version": "ci-reliability-exp-v3-q1",
        "result": "PASS",
        "artifact_key": "short-soak",
        "artifact_id": "art-short-soak-v3",
        "expected_hash": "6868f5813a37470673ab4fa5bc2dfa2de912092b9d02360866627585edb1dfcb",
        "source_envelope_id": "env-flaky-1",
        "provenance": "synthetic-fixture-v4",
    },
    "static_invariant": {
        "replacement_evidence_id": "repl-ev-static_invariant",
        "replacement_id": "static_invariant",
        "candidate_id": "cand-flaky-v1",
        "requirement_id": "CI-EXP-REQ-v3-q1",
        "policy_version": "ci-reliability-exp-v3-q1",
        "result": "PASS",
        "artifact_key": "static-invariant",
        "artifact_id": "art-static-invariant-v3",
        "expected_hash": "7c47b7ba6d4c0afbf459d890eb6b1435feb095a15815a10f82ea7c3a30d08423",
        "source_envelope_id": "env-flaky-1",
        "provenance": "synthetic-fixture-v4",
    },
}


def unit_lineage(*, artifact_id: str = "art-unit-pass-v3", expected_hash: str | None = None, restored: bool = True) -> dict[str, Any]:
    exact_hash = ARTIFACT_CATALOG["unit-pass"]["content_hash"]
    events = [
        {"event_id": "unit-pass-e0", "state": "REACHABLE", "observed_hash": exact_hash},
        {"event_id": "unit-e1-loss", "state": "UNREACHABLE", "observed_hash": None},
    ]
    if restored:
        events.append({"event_id": "unit-e2-restore", "state": "REACHABLE", "observed_hash": exact_hash})
    return {
        "artifact_key": "unit-pass",
        "artifact_id": artifact_id,
        "expected_hash": expected_hash or exact_hash,
        "events": events,
    }


FIXTURE_MANIFEST = {
    "schema": "ci-reliability-fixture-v4",
    "base_sha": "c7ba185ed9667b717794c19eaa0834ca41aa4c78",
    "requirement_id": "CI-EXP-REQ-v3",
    "artifact_catalog": ARTIFACT_CATALOG,
    "quarantine_policy": QUARANTINE_POLICY,
    "candidate_ids": {
        "good": "cand-good-v1",
        "product": "cand-product-fail-v1",
        "infra": "cand-infra-retry-v1",
        "flaky": "cand-flaky-v1",
        "remediated": "cand-flaky-v2",
    },
    "predecessor_evidence_artifact": PREDECESSOR_EVIDENCE_ARTIFACT,
    "predecessor_evidence_artifact_digest": canonical_digest(PREDECESSOR_EVIDENCE_ARTIFACT),
    "predecessor_root_algorithm": PREDECESSOR_ROOT_ALGORITHM,
    "transition": TRANSITION,
}

HARNESS_CONTRACT = {
    "harness_version": VALIDATOR_VERSION,
    "validator_source_identity_algorithm": VALIDATOR_SOURCE_IDENTITY_ALGORITHM,
    "validator_source_digest": VALIDATOR_SOURCE_DIGEST,
    "canonical_json_algorithm": CANONICAL_JSON_ALGORITHM,
    "aggregate_semantics": "required-gate-three-state-v2",
    "artifact_lineage_semantics": "stable-artifact-identity-event-lineage-v2",
    "candidate_chain_semantics": "append-only-exact-candidate-v1",
    "candidate_transition_semantics": "validated-reconstructable-predecessor-evidence-root-v2",
    "quarantine_semantics": "exact-versioned-replacement-evidence-artifact-v3",
}


def compile_requirement(applicability: str, condition_applies: bool | None) -> str:
    if applicability == "NOT_APPLICABLE":
        return "NOT_APPLICABLE"
    if applicability == "REQUIRED":
        return "REQUIRED"
    if applicability == "CONDITIONALLY_REQUIRED":
        if condition_applies is None:
            return "UNKNOWN"
        return "REQUIRED" if condition_applies else "NOT_APPLICABLE"
    return "UNKNOWN"


def evaluate_attempt_requirement(case: dict[str, Any]) -> str:
    compiled = compile_requirement(case["applicability"], case.get("condition_applies"))
    if compiled == "NOT_APPLICABLE":
        return "SATISFIED"
    if compiled != "REQUIRED":
        return "INCONCLUSIVE"

    attempts = case.get("attempts", [])
    if not attempts:
        return "UNSATISFIED"

    if any(a["result"] == "NOT_RUN" for a in attempts):
        return "UNSATISFIED"
    if any(a["result"] == "FLAKY" or a.get("failure_class") == "FLAKY" for a in attempts):
        return "UNSATISFIED"
    if any(a["result"] == "FAIL" and a.get("failure_class") == "PRODUCT" for a in attempts):
        return "UNSATISFIED"

    failures = [a for a in attempts if a["result"] == "FAIL"]
    if failures:
        if not case.get("allow_infra_retry", False):
            return "UNSATISFIED"
        if any(a.get("failure_class") != "INFRA" for a in failures):
            return "UNSATISFIED"
        if attempts[-1]["result"] != "PASS":
            return "UNSATISFIED"
        return "SATISFIED"

    return "SATISFIED" if attempts[-1]["result"] == "PASS" else "UNSATISFIED"


REPLACEMENT_REQUIRED_FIELDS = {
    "replacement_evidence_id",
    "replacement_id",
    "candidate_id",
    "requirement_id",
    "policy_version",
    "result",
    "artifact_key",
    "artifact_id",
    "expected_hash",
    "source_envelope_id",
    "provenance",
}


def validate_replacement_record(record: dict[str, Any], policy: dict[str, Any]) -> bool:
    if not REPLACEMENT_REQUIRED_FIELDS.issubset(record):
        return False
    if record["candidate_id"] != policy["candidate_id"]:
        return False
    if record["requirement_id"] != policy["requirement_id"]:
        return False
    if record["policy_version"] != policy["policy_version"]:
        return False
    if record["result"] != "PASS":
        return False
    artifact = ARTIFACT_CATALOG.get(record["artifact_key"])
    if not artifact:
        return False
    return (
        record["artifact_id"] == artifact["artifact_id"]
        and record["expected_hash"] == artifact["content_hash"]
    )


def evaluate_quarantine(case: dict[str, Any]) -> str:
    policy = QUARANTINE_POLICY
    if case["candidate_id"] != policy["candidate_id"]:
        return "INCONCLUSIVE"
    if case["day"] >= policy["expiry_day"]:
        return "INCONCLUSIVE"

    records = case.get("replacement_evidence", {})
    expected_ids = set(policy["replacement_ids"])
    actual_ids = set(records)
    if actual_ids != expected_ids:
        return "INCONCLUSIVE"

    for replacement_id, record in records.items():
        if record.get("replacement_id") != replacement_id:
            return "INCONCLUSIVE"
        if not validate_replacement_record(record, policy):
            return "INCONCLUSIVE"
    return "SATISFIED"


def evaluate_reset(case: dict[str, Any]) -> str:
    if case["root_generation"] > 1 and case["candidate_id"] == case["prior_candidate_id"]:
        return "INCONCLUSIVE"
    return "SATISFIED"


def evaluate_transition(case: dict[str, Any]) -> str:
    transition = case.get("transition")
    if not transition:
        return "INCONCLUSIVE"

    artifact = case.get("predecessor_evidence_artifact")
    if not artifact:
        return "INCONCLUSIVE"
    if transition.get("predecessor_root_algorithm") != PREDECESSOR_ROOT_ALGORITHM:
        return "INCONCLUSIVE"

    artifact_digest = canonical_digest(artifact)
    root = predecessor_root(artifact)

    if artifact_digest != transition.get("predecessor_evidence_artifact_digest"):
        return "INCONCLUSIVE"
    if artifact.get("candidate_id") != transition.get("predecessor_candidate_id"):
        return "INCONCLUSIVE"
    if transition.get("predecessor_candidate_id") == transition.get("successor_candidate_id"):
        return "INCONCLUSIVE"
    if transition.get("successor_candidate_id") != case.get("candidate_id"):
        return "INCONCLUSIVE"
    if not transition.get("changed_work_identity") or not transition.get("reason") or not transition.get("transition_id"):
        return "INCONCLUSIVE"
    if root != transition.get("predecessor_evidence_root"):
        return "INCONCLUSIVE"
    if case.get("claimed_observed_root") != root:
        return "INCONCLUSIVE"
    return "SATISFIED"


def evaluate_retention(case: dict[str, Any]) -> str:
    lineage = case["lineage"]
    artifact = ARTIFACT_CATALOG.get(lineage.get("artifact_key"))
    if not artifact:
        return "INCONCLUSIVE"
    if lineage.get("artifact_id") != artifact["artifact_id"]:
        return "INCONCLUSIVE"
    if lineage.get("expected_hash") != artifact["content_hash"]:
        return "INCONCLUSIVE"
    events = lineage.get("events", [])
    if not events:
        return "INCONCLUSIVE"
    for event in events:
        if event["state"] == "REACHABLE" and event.get("observed_hash") != artifact["content_hash"]:
            return "INCONCLUSIVE"
        if event["state"] == "UNREACHABLE" and event.get("observed_hash") is not None:
            return "INCONCLUSIVE"
    last = events[-1]
    return "SATISFIED" if last["state"] == "REACHABLE" else "INCONCLUSIVE"


def evaluate_case(case: dict[str, Any]) -> str:
    mode = case["mode"]
    if mode == "attempt_requirement":
        return evaluate_attempt_requirement(case)
    if mode == "quarantine":
        return evaluate_quarantine(case)
    if mode == "reset":
        return evaluate_reset(case)
    if mode == "transition":
        return evaluate_transition(case)
    if mode == "retention":
        return evaluate_retention(case)
    return "INCONCLUSIVE"


def make_cases() -> list[dict[str, Any]]:
    wrong_artifact = copy.deepcopy(BASE_REPLACEMENT_EVIDENCE)
    wrong_artifact["short_soak"]["artifact_id"] = "art-wrong"
    omitted_artifact = copy.deepcopy(BASE_REPLACEMENT_EVIDENCE)
    del omitted_artifact["short_soak"]["artifact_id"]

    missing_set = copy.deepcopy(BASE_REPLACEMENT_EVIDENCE)
    del missing_set["static_invariant"]
    extra_set = copy.deepcopy(BASE_REPLACEMENT_EVIDENCE)
    extra = copy.deepcopy(extra_set["short_soak"])
    extra["replacement_evidence_id"] = "repl-ev-extra"
    extra["replacement_id"] = "extra"
    extra_set["extra"] = extra
    wrong_set = copy.deepcopy(BASE_REPLACEMENT_EVIDENCE)
    wrong_set["short_soak"]["replacement_id"] = "not_short_soak"

    wrong_predecessor = copy.deepcopy(TRANSITION)
    wrong_predecessor["predecessor_candidate_id"] = "cand-other-v1"
    same_candidate = copy.deepcopy(TRANSITION)
    same_candidate["successor_candidate_id"] = "cand-flaky-v1"
    substituted_root = copy.deepcopy(TRANSITION)
    substituted_root["predecessor_evidence_root"] = "0" * 64

    return [
        {
            "id": "S1_baseline",
            "mode": "attempt_requirement",
            "applicability": "REQUIRED",
            "attempts": [{"result": "PASS", "failure_class": None}],
            "allow_infra_retry": False,
        },
        {
            "id": "S2_conditional_not_run",
            "mode": "attempt_requirement",
            "applicability": "CONDITIONALLY_REQUIRED",
            "condition_applies": True,
            "attempts": [{"result": "NOT_RUN", "failure_class": None}],
            "allow_infra_retry": False,
        },
        {
            "id": "S3_product_fail_retry",
            "mode": "attempt_requirement",
            "applicability": "REQUIRED",
            "attempts": [
                {"result": "FAIL", "failure_class": "PRODUCT"},
                {"result": "PASS", "failure_class": None},
            ],
            "allow_infra_retry": True,
        },
        {
            "id": "S4_infra_retry",
            "mode": "attempt_requirement",
            "applicability": "REQUIRED",
            "attempts": [
                {"result": "FAIL", "failure_class": "INFRA"},
                {"result": "PASS", "failure_class": None},
            ],
            "allow_infra_retry": True,
        },
        {
            "id": "S5_flaky",
            "mode": "attempt_requirement",
            "applicability": "REQUIRED",
            "attempts": [
                {"result": "FLAKY", "failure_class": "FLAKY"},
                {"result": "PASS", "failure_class": None},
            ],
            "allow_infra_retry": True,
        },
        {
            "id": "S6_quarantine_active_valid",
            "mode": "quarantine",
            "candidate_id": "cand-flaky-v1",
            "day": 7,
            "replacement_evidence": copy.deepcopy(BASE_REPLACEMENT_EVIDENCE),
        },
        {
            "id": "S7_replacement_omitted_artifact_id",
            "mode": "quarantine",
            "candidate_id": "cand-flaky-v1",
            "day": 7,
            "replacement_evidence": omitted_artifact,
        },
        {
            "id": "S8_replacement_wrong_artifact_id",
            "mode": "quarantine",
            "candidate_id": "cand-flaky-v1",
            "day": 7,
            "replacement_evidence": wrong_artifact,
        },
        {
            "id": "S9_same_candidate_reset",
            "mode": "reset",
            "candidate_id": "cand-flaky-v1",
            "prior_candidate_id": "cand-flaky-v1",
            "root_generation": 2,
        },
        {
            "id": "S10_successor_valid",
            "mode": "transition",
            "candidate_id": "cand-flaky-v2",
            "transition": copy.deepcopy(TRANSITION),
            "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR_EVIDENCE_ARTIFACT),
            "claimed_observed_root": PREDECESSOR_EVIDENCE_ROOT,
        },
        {
            "id": "S11_successor_missing_transition",
            "mode": "transition",
            "candidate_id": "cand-flaky-v2",
            "transition": None,
            "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR_EVIDENCE_ARTIFACT),
            "claimed_observed_root": PREDECESSOR_EVIDENCE_ROOT,
        },
        {
            "id": "S12_successor_wrong_predecessor",
            "mode": "transition",
            "candidate_id": "cand-flaky-v2",
            "transition": wrong_predecessor,
            "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR_EVIDENCE_ARTIFACT),
            "claimed_observed_root": PREDECESSOR_EVIDENCE_ROOT,
        },
        {
            "id": "S13_successor_same_candidate_masquerade",
            "mode": "transition",
            "candidate_id": "cand-flaky-v1",
            "transition": same_candidate,
            "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR_EVIDENCE_ARTIFACT),
            "claimed_observed_root": PREDECESSOR_EVIDENCE_ROOT,
        },
        {
            "id": "S14_retention_loss",
            "mode": "retention",
            "lineage": unit_lineage(restored=False),
        },
        {
            "id": "S15_exact_restore",
            "mode": "retention",
            "lineage": unit_lineage(),
        },
        {
            "id": "S16_identity_swap_same_events",
            "mode": "retention",
            "lineage": unit_lineage(artifact_id="art-swapped"),
        },
        {
            "id": "S17_expected_hash_swap_same_events",
            "mode": "retention",
            "lineage": unit_lineage(expected_hash="11d31bcde2b39adf074772ffd52f6431dbef826c3866190be73638d0964b07d1"),
        },
        {
            "id": "S18_quarantine_expired_boundary",
            "mode": "quarantine",
            "candidate_id": "cand-flaky-v1",
            "day": 14,
            "replacement_evidence": copy.deepcopy(BASE_REPLACEMENT_EVIDENCE),
        },
        {
            "id": "S19_replacement_set_missing",
            "mode": "quarantine",
            "candidate_id": "cand-flaky-v1",
            "day": 7,
            "replacement_evidence": missing_set,
        },
        {
            "id": "S20_replacement_set_extra",
            "mode": "quarantine",
            "candidate_id": "cand-flaky-v1",
            "day": 7,
            "replacement_evidence": extra_set,
        },
        {
            "id": "S21_replacement_set_wrong_member",
            "mode": "quarantine",
            "candidate_id": "cand-flaky-v1",
            "day": 7,
            "replacement_evidence": wrong_set,
        },
        {
            "id": "S22_predecessor_root_double_substitution",
            "mode": "transition",
            "candidate_id": "cand-flaky-v2",
            "transition": substituted_root,
            "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR_EVIDENCE_ARTIFACT),
            "claimed_observed_root": "0" * 64,
        },
    ]


EXPECTED = {
    "S1_baseline": "SATISFIED",
    "S2_conditional_not_run": "UNSATISFIED",
    "S3_product_fail_retry": "UNSATISFIED",
    "S4_infra_retry": "SATISFIED",
    "S5_flaky": "UNSATISFIED",
    "S6_quarantine_active_valid": "SATISFIED",
    "S7_replacement_omitted_artifact_id": "INCONCLUSIVE",
    "S8_replacement_wrong_artifact_id": "INCONCLUSIVE",
    "S9_same_candidate_reset": "INCONCLUSIVE",
    "S10_successor_valid": "SATISFIED",
    "S11_successor_missing_transition": "INCONCLUSIVE",
    "S12_successor_wrong_predecessor": "INCONCLUSIVE",
    "S13_successor_same_candidate_masquerade": "INCONCLUSIVE",
    "S14_retention_loss": "INCONCLUSIVE",
    "S15_exact_restore": "SATISFIED",
    "S16_identity_swap_same_events": "INCONCLUSIVE",
    "S17_expected_hash_swap_same_events": "INCONCLUSIVE",
    "S18_quarantine_expired_boundary": "INCONCLUSIVE",
    "S19_replacement_set_missing": "INCONCLUSIVE",
    "S20_replacement_set_extra": "INCONCLUSIVE",
    "S21_replacement_set_wrong_member": "INCONCLUSIVE",
    "S22_predecessor_root_double_substitution": "INCONCLUSIVE",
}


def evidence_bundle(path: pathlib.Path) -> dict[str, Any]:
    actual_source = computed_source_digest(path)
    if actual_source != VALIDATOR_SOURCE_DIGEST:
        raise SystemExit(
            f"validator source identity mismatch: declared={VALIDATOR_SOURCE_DIGEST} observed={actual_source}"
        )

    cases = make_cases()
    aggregates = {case["id"]: evaluate_case(case) for case in cases}
    if aggregates != EXPECTED:
        differences = {
            key: {"expected": EXPECTED.get(key), "observed": aggregates.get(key)}
            for key in sorted(set(EXPECTED) | set(aggregates))
            if EXPECTED.get(key) != aggregates.get(key)
        }
        raise SystemExit("regression mismatch: " + json.dumps(differences, sort_keys=True))

    harness = copy.deepcopy(HARNESS_CONTRACT)
    harness["validator_source_digest"] = actual_source

    result = {
        "schema": "ci-reliability-results-v4",
        "validator_version": VALIDATOR_VERSION,
        "validator_source_digest": actual_source,
        "scenario_aggregates": aggregates,
        "replacement_evidence_positive": copy.deepcopy(BASE_REPLACEMENT_EVIDENCE),
        "candidate_transition_positive": copy.deepcopy(TRANSITION),
        "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR_EVIDENCE_ARTIFACT),
        "predecessor_evidence_artifact_digest": canonical_digest(PREDECESSOR_EVIDENCE_ARTIFACT),
        "predecessor_evidence_root_recomputed": PREDECESSOR_EVIDENCE_ROOT,
        "predecessor_root_algorithm": PREDECESSOR_ROOT_ALGORITHM,
        "retention_loss_lineage": unit_lineage(restored=False),
        "retention_restore_lineage": unit_lineage(),
    }

    return {
        "fixture_manifest": FIXTURE_MANIFEST,
        "fixture_cases": cases,
        "harness_contract": harness,
        "result_object": result,
        "digests": {
            "validator_source": actual_source,
            "fixture_manifest": canonical_digest(FIXTURE_MANIFEST),
            "fixture_cases": canonical_digest(cases),
            "harness_contract": canonical_digest(harness),
            "result_object": canonical_digest(result),
            "predecessor_evidence_artifact": canonical_digest(PREDECESSOR_EVIDENCE_ARTIFACT),
            "predecessor_evidence_root": "sha256:" + PREDECESSOR_EVIDENCE_ROOT,
        },
    }


def main() -> int:
    path = pathlib.Path(__file__).resolve()
    bundle = evidence_bundle(path)
    print(json.dumps(bundle, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
