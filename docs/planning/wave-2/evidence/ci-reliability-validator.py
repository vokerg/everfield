#!/usr/bin/env python3
"""W2-REM-CI-04 deterministic synthetic CI evidence validator; stdlib only."""
from __future__ import annotations

import copy
import hashlib
import json
import pathlib
import re
from typing import Any

VALIDATOR_VERSION = "ci-reliability-reference-v5"
SOURCE_ID_ALGORITHM = "sha256-source-with-digest-line-sentinel-v1"
VALIDATOR_SOURCE_DIGEST = "sha256:75dc8a78c1489b0afbe39047261f5bfeed77a08d970885cb670d77f3d3d8d8d3"
CANONICAL_ALGORITHM = "sha256-canonical-json-sorted-compact-v1"


def cbytes(v: Any) -> bytes:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(v: Any) -> str:
    return "sha256:" + hashlib.sha256(cbytes(v)).hexdigest()


def normalized_source(path: pathlib.Path) -> bytes:
    text = path.read_text(encoding="utf-8")
    return re.sub(
        r'^VALIDATOR_SOURCE_DIGEST = ".*"$',
        'VALIDATOR_SOURCE_DIGEST = "__SOURCE_DIGEST__"',
        text,
        count=1,
        flags=re.MULTILINE,
    ).encode()


def source_digest(path: pathlib.Path) -> str:
    return "sha256:" + hashlib.sha256(normalized_source(path)).hexdigest()


PREDECESSOR = {
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
PREDECESSOR_ROOT = hashlib.sha256(cbytes(PREDECESSOR)).hexdigest()

ARTIFACTS = {
    "package-pass": ("art-package-pass-v3", "dc9f6e4b62400949d12a88714711ce5cd0c654d768b825fd8151014c310cd40a"),
    "short-soak": ("art-short-soak-v3", "6868f5813a37470673ab4fa5bc2dfa2de912092b9d02360866627585edb1dfcb"),
    "soak-pass": ("art-soak-pass-v3", "db3d050bfe46b76e8df9b877cbbb21112a9f704e817d9076b6ccf070f8a73452"),
    "static-invariant": ("art-static-invariant-v3", "7c47b7ba6d4c0afbf459d890eb6b1435feb095a15815a10f82ea7c3a30d08423"),
    "unit-pass": ("art-unit-pass-v3", "9f13dde3b3dd154a952368dfefa81a2813eca62b49ed97a0a65aaa48085ef2a1"),
}
CATALOG = {k: {"artifact_id": v[0], "content_hash": v[1]} for k, v in ARTIFACTS.items()}

POLICY = {
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
    "predecessor_evidence_root": PREDECESSOR_ROOT,
    "predecessor_evidence_artifact_digest": digest(PREDECESSOR),
    "predecessor_root_algorithm": CANONICAL_ALGORITHM,
}

# Exact immutable synthetic execution evidence for each quarantine replacement.
# These bytes are included in the frozen packet and content-bound below.
REPLACEMENT_EXECUTION_ENVELOPES = {
    "repl-env-short-soak-v1": {
        "schema": "replacement-execution-envelope-v1",
        "source_envelope_id": "repl-env-short-soak-v1",
        "replacement_evidence_id": "repl-ev-short_soak-v1",
        "candidate_id": "cand-flaky-v1",
        "requirement_id": POLICY["requirement_id"],
        "policy_version": POLICY["policy_version"],
        "replacement_id": "short_soak",
        "check_id": "short_soak",
        "result": "PASS",
        "artifact_key": "short-soak",
        "artifact_id": ARTIFACTS["short-soak"][0],
        "expected_hash": ARTIFACTS["short-soak"][1],
        "provenance": {
            "provenance_id": "prov-short-soak-v1",
            "value": "w2-rem-ci-04-synthetic-execution-v1",
        },
    },
    "repl-env-static-invariant-v1": {
        "schema": "replacement-execution-envelope-v1",
        "source_envelope_id": "repl-env-static-invariant-v1",
        "replacement_evidence_id": "repl-ev-static_invariant-v1",
        "candidate_id": "cand-flaky-v1",
        "requirement_id": POLICY["requirement_id"],
        "policy_version": POLICY["policy_version"],
        "replacement_id": "static_invariant",
        "check_id": "static_invariant",
        "result": "PASS",
        "artifact_key": "static-invariant",
        "artifact_id": ARTIFACTS["static-invariant"][0],
        "expected_hash": ARTIFACTS["static-invariant"][1],
        "provenance": {
            "provenance_id": "prov-static-invariant-v1",
            "value": "w2-rem-ci-04-synthetic-execution-v1",
        },
    },
}
REPLACEMENT_ENVELOPE_DIGESTS = {
    envelope_id: digest(envelope) for envelope_id, envelope in REPLACEMENT_EXECUTION_ENVELOPES.items()
}
REPLACEMENT_ENVELOPE_SET_DIGEST = digest(REPLACEMENT_EXECUTION_ENVELOPES)

REPLACEMENTS = {
    "short_soak": {
        "replacement_evidence_id": "repl-ev-short_soak-v1",
        "replacement_id": "short_soak",
        "check_id": "short_soak",
        "candidate_id": "cand-flaky-v1",
        "requirement_id": POLICY["requirement_id"],
        "policy_version": POLICY["policy_version"],
        "result": "PASS",
        "artifact_key": "short-soak",
        "artifact_id": ARTIFACTS["short-soak"][0],
        "expected_hash": ARTIFACTS["short-soak"][1],
        "source_envelope_id": "repl-env-short-soak-v1",
        "source_envelope_digest": REPLACEMENT_ENVELOPE_DIGESTS["repl-env-short-soak-v1"],
        "provenance": copy.deepcopy(REPLACEMENT_EXECUTION_ENVELOPES["repl-env-short-soak-v1"]["provenance"]),
    },
    "static_invariant": {
        "replacement_evidence_id": "repl-ev-static_invariant-v1",
        "replacement_id": "static_invariant",
        "check_id": "static_invariant",
        "candidate_id": "cand-flaky-v1",
        "requirement_id": POLICY["requirement_id"],
        "policy_version": POLICY["policy_version"],
        "result": "PASS",
        "artifact_key": "static-invariant",
        "artifact_id": ARTIFACTS["static-invariant"][0],
        "expected_hash": ARTIFACTS["static-invariant"][1],
        "source_envelope_id": "repl-env-static-invariant-v1",
        "source_envelope_digest": REPLACEMENT_ENVELOPE_DIGESTS["repl-env-static-invariant-v1"],
        "provenance": copy.deepcopy(REPLACEMENT_EXECUTION_ENVELOPES["repl-env-static-invariant-v1"]["provenance"]),
    },
}
EXPECTED_REPLACEMENT_EVIDENCE_IDS = {
    replacement_id: record["replacement_evidence_id"] for replacement_id, record in REPLACEMENTS.items()
}
EXPECTED_SOURCE_ENVELOPE_IDS = {
    replacement_id: record["source_envelope_id"] for replacement_id, record in REPLACEMENTS.items()
}
REQUIRED_REPLACEMENT_FIELDS = {
    "replacement_evidence_id",
    "replacement_id",
    "check_id",
    "candidate_id",
    "requirement_id",
    "policy_version",
    "result",
    "artifact_key",
    "artifact_id",
    "expected_hash",
    "source_envelope_id",
    "source_envelope_digest",
    "provenance",
}


def lineage(artifact_id: str | None = None, expected_hash: str | None = None, restored: bool = True) -> dict[str, Any]:
    aid, ahash = ARTIFACTS["unit-pass"]
    events = [
        {"event_id": "unit-pass-e0", "state": "REACHABLE", "observed_hash": ahash},
        {"event_id": "unit-e1-loss", "state": "UNREACHABLE", "observed_hash": None},
    ]
    if restored:
        events.append({"event_id": "unit-e2-restore", "state": "REACHABLE", "observed_hash": ahash})
    return {
        "artifact_key": "unit-pass",
        "artifact_id": artifact_id or aid,
        "expected_hash": expected_hash or ahash,
        "events": events,
    }


FIXTURE_MANIFEST = {
    "schema": "ci-reliability-fixture-v5",
    "base_sha": "042d140b5d2e0b951da4528e1867514983418d6f",
    "requirement_id": "CI-EXP-REQ-v3",
    "artifact_catalog": CATALOG,
    "quarantine_policy": POLICY,
    "candidate_ids": {
        "good": "cand-good-v1",
        "product": "cand-product-fail-v1",
        "infra": "cand-infra-retry-v1",
        "flaky": "cand-flaky-v1",
        "remediated": "cand-flaky-v2",
    },
    "replacement_execution_envelopes": REPLACEMENT_EXECUTION_ENVELOPES,
    "replacement_envelope_digests": REPLACEMENT_ENVELOPE_DIGESTS,
    "replacement_envelope_set_digest": REPLACEMENT_ENVELOPE_SET_DIGEST,
    "predecessor_evidence_artifact": PREDECESSOR,
    "predecessor_evidence_artifact_digest": digest(PREDECESSOR),
    "predecessor_root_algorithm": CANONICAL_ALGORITHM,
    "transition": TRANSITION,
}
HARNESS = {
    "harness_version": VALIDATOR_VERSION,
    "validator_source_identity_algorithm": SOURCE_ID_ALGORITHM,
    "validator_source_digest": VALIDATOR_SOURCE_DIGEST,
    "canonical_json_algorithm": CANONICAL_ALGORITHM,
    "aggregate_semantics": "required-gate-three-state-v2",
    "artifact_lineage_semantics": "stable-artifact-identity-event-lineage-v2",
    "candidate_chain_semantics": "append-only-exact-candidate-v1",
    "candidate_transition_semantics": "validated-reconstructable-predecessor-evidence-root-v2",
    "quarantine_semantics": "exact-replacement-record-and-source-envelope-v4",
    "replacement_evidence_semantics": "unique-id-content-addressed-source-envelope-provenance-v1",
}


def attempt(case: dict[str, Any]) -> str:
    app = case["applicability"]
    if app == "CONDITIONALLY_REQUIRED":
        app = (
            "REQUIRED"
            if case.get("condition_applies") is True
            else ("NOT_APPLICABLE" if case.get("condition_applies") is False else "UNKNOWN")
        )
    if app == "NOT_APPLICABLE":
        return "SATISFIED"
    if app != "REQUIRED":
        return "INCONCLUSIVE"
    seq = case.get("attempts", [])
    if not seq or any(x["result"] == "NOT_RUN" for x in seq):
        return "UNSATISFIED"
    if any(x["result"] == "FLAKY" or x.get("failure_class") == "FLAKY" for x in seq):
        return "UNSATISFIED"
    if any(x["result"] == "FAIL" and x.get("failure_class") == "PRODUCT" for x in seq):
        return "UNSATISFIED"
    fails = [x for x in seq if x["result"] == "FAIL"]
    if fails:
        if not case.get("allow_infra_retry") or any(x.get("failure_class") != "INFRA" for x in fails):
            return "UNSATISFIED"
        return "SATISFIED" if seq[-1]["result"] == "PASS" else "UNSATISFIED"
    return "SATISFIED" if seq[-1]["result"] == "PASS" else "UNSATISFIED"


def replacement_ok(
    replacement_id: str,
    record: dict[str, Any],
    source_envelopes: dict[str, dict[str, Any]],
) -> bool:
    if not REQUIRED_REPLACEMENT_FIELDS.issubset(record):
        return False
    if record.get("replacement_id") != replacement_id:
        return False
    if record.get("check_id") != replacement_id:
        return False
    if record.get("replacement_evidence_id") != EXPECTED_REPLACEMENT_EVIDENCE_IDS.get(replacement_id):
        return False
    if record.get("source_envelope_id") != EXPECTED_SOURCE_ENVELOPE_IDS.get(replacement_id):
        return False
    if record.get("candidate_id") != POLICY["candidate_id"] or record.get("requirement_id") != POLICY["requirement_id"]:
        return False
    if record.get("policy_version") != POLICY["policy_version"] or record.get("result") != "PASS":
        return False
    artifact = CATALOG.get(record.get("artifact_key"))
    if not artifact or record.get("artifact_id") != artifact["artifact_id"] or record.get("expected_hash") != artifact["content_hash"]:
        return False

    source_id = record["source_envelope_id"]
    envelope = source_envelopes.get(source_id)
    if not envelope:
        return False
    expected_digest = REPLACEMENT_ENVELOPE_DIGESTS.get(source_id)
    if not expected_digest or digest(envelope) != expected_digest or record.get("source_envelope_digest") != expected_digest:
        return False
    expected_envelope = REPLACEMENT_EXECUTION_ENVELOPES.get(source_id)
    if envelope != expected_envelope:
        return False

    bound_fields = (
        "replacement_evidence_id",
        "candidate_id",
        "requirement_id",
        "policy_version",
        "replacement_id",
        "check_id",
        "result",
        "artifact_key",
        "artifact_id",
        "expected_hash",
        "provenance",
    )
    return all(record.get(field) == envelope.get(field) for field in bound_fields)


def quarantine(case: dict[str, Any]) -> str:
    if case["candidate_id"] != POLICY["candidate_id"] or case["day"] >= POLICY["expiry_day"]:
        return "INCONCLUSIVE"
    records = case.get("replacement_evidence", {})
    source_envelopes = case.get("replacement_execution_envelopes", {})
    if set(records) != set(POLICY["replacement_ids"]):
        return "INCONCLUSIVE"
    if digest(source_envelopes) != REPLACEMENT_ENVELOPE_SET_DIGEST:
        return "INCONCLUSIVE"
    evidence_ids = [r.get("replacement_evidence_id") for r in records.values()]
    source_ids = [r.get("source_envelope_id") for r in records.values()]
    if None in evidence_ids or len(set(evidence_ids)) != len(evidence_ids):
        return "INCONCLUSIVE"
    if None in source_ids or len(set(source_ids)) != len(source_ids):
        return "INCONCLUSIVE"
    return (
        "SATISFIED"
        if all(replacement_ok(rid, record, source_envelopes) for rid, record in records.items())
        else "INCONCLUSIVE"
    )


def transition(case: dict[str, Any]) -> str:
    t, evidence = case.get("transition"), case.get("predecessor_evidence_artifact")
    if not t or not evidence:
        return "INCONCLUSIVE"
    edigest, root = digest(evidence), hashlib.sha256(cbytes(evidence)).hexdigest()
    exact = (
        edigest == digest(PREDECESSOR)
        and edigest == t.get("predecessor_evidence_artifact_digest")
        and root == PREDECESSOR_ROOT
        and t.get("predecessor_evidence_root") == PREDECESSOR_ROOT
        and t.get("predecessor_root_algorithm") == CANONICAL_ALGORITHM
        and evidence.get("candidate_id") == TRANSITION["predecessor_candidate_id"]
        and t.get("predecessor_candidate_id") == TRANSITION["predecessor_candidate_id"]
        and t.get("successor_candidate_id") == TRANSITION["successor_candidate_id"]
        and t.get("predecessor_candidate_id") != t.get("successor_candidate_id")
        and case.get("candidate_id") == TRANSITION["successor_candidate_id"]
        and t.get("changed_work_identity") == TRANSITION["changed_work_identity"]
        and t.get("reason") == TRANSITION["reason"]
        and t.get("transition_id") == TRANSITION["transition_id"]
        and case.get("claimed_observed_root") == PREDECESSOR_ROOT
    )
    return "SATISFIED" if exact else "INCONCLUSIVE"


def retention(case: dict[str, Any]) -> str:
    l = case["lineage"]
    a = CATALOG.get(l.get("artifact_key"))
    if not a or l.get("artifact_id") != a["artifact_id"] or l.get("expected_hash") != a["content_hash"]:
        return "INCONCLUSIVE"
    events = l.get("events", [])
    if not events:
        return "INCONCLUSIVE"
    for event in events:
        if event["state"] == "REACHABLE" and event.get("observed_hash") != a["content_hash"]:
            return "INCONCLUSIVE"
        if event["state"] == "UNREACHABLE" and event.get("observed_hash") is not None:
            return "INCONCLUSIVE"
    return "SATISFIED" if events[-1]["state"] == "REACHABLE" else "INCONCLUSIVE"


def evaluate(case: dict[str, Any]) -> str:
    mode = case["mode"]
    if mode == "attempt":
        return attempt(case)
    if mode == "quarantine":
        return quarantine(case)
    if mode == "transition":
        return transition(case)
    if mode == "retention":
        return retention(case)
    if mode == "reset":
        return (
            "INCONCLUSIVE"
            if case["root_generation"] > 1 and case["candidate_id"] == case["prior_candidate_id"]
            else "SATISFIED"
        )
    return "INCONCLUSIVE"


def qcase(case_id: str, records: dict[str, Any], envelopes: dict[str, Any] | None = None, day: int = 7) -> dict[str, Any]:
    return {
        "id": case_id,
        "mode": "quarantine",
        "candidate_id": "cand-flaky-v1",
        "day": day,
        "replacement_evidence": records,
        "replacement_execution_envelopes": copy.deepcopy(
            REPLACEMENT_EXECUTION_ENVELOPES if envelopes is None else envelopes
        ),
    }


def cases() -> list[dict[str, Any]]:
    omitted, wrong = copy.deepcopy(REPLACEMENTS), copy.deepcopy(REPLACEMENTS)
    del omitted["short_soak"]["artifact_id"]
    wrong["short_soak"]["artifact_id"] = "art-wrong"
    missing = copy.deepcopy(REPLACEMENTS)
    del missing["static_invariant"]
    extra = copy.deepcopy(REPLACEMENTS)
    extra_record = copy.deepcopy(extra["short_soak"])
    extra_record["replacement_id"] = "extra"
    extra["extra"] = extra_record
    wrong_member = copy.deepcopy(REPLACEMENTS)
    moved = wrong_member.pop("short_soak")
    moved["replacement_id"] = "wrong_soak"
    wrong_member["wrong_soak"] = moved

    wrong_pred = copy.deepcopy(TRANSITION)
    wrong_pred["predecessor_candidate_id"] = "cand-other-v1"
    same = copy.deepcopy(TRANSITION)
    same["successor_candidate_id"] = "cand-flaky-v1"
    bad_root = copy.deepcopy(TRANSITION)
    bad_root["predecessor_evidence_root"] = "0" * 64
    bad_work = copy.deepcopy(TRANSITION)
    bad_work["changed_work_identity"] = "work:substituted:v1"
    bad_tid = copy.deepcopy(TRANSITION)
    bad_tid["transition_id"] = "transition-substituted"
    bad_reason = copy.deepcopy(TRANSITION)
    bad_reason["reason"] = "different remediation reason"
    bad_evidence = copy.deepcopy(PREDECESSOR)
    bad_evidence["evidence_envelopes"][0]["attempts"][0]["attempt_id"] = "soak-substituted"
    bad_evidence_t = copy.deepcopy(TRANSITION)
    bad_evidence_t["predecessor_evidence_artifact_digest"] = digest(bad_evidence)
    bad_evidence_t["predecessor_evidence_root"] = hashlib.sha256(cbytes(bad_evidence)).hexdigest()

    substituted_evidence_id = copy.deepcopy(REPLACEMENTS)
    substituted_evidence_id["short_soak"]["replacement_evidence_id"] = "repl-ev-evil"
    duplicate_evidence_id = copy.deepcopy(REPLACEMENTS)
    duplicate_evidence_id["static_invariant"]["replacement_evidence_id"] = duplicate_evidence_id["short_soak"]["replacement_evidence_id"]
    dangling_envelope = copy.deepcopy(REPLACEMENTS)
    dangling_envelope["short_soak"]["source_envelope_id"] = "repl-env-does-not-exist"
    wrong_envelope = copy.deepcopy(REPLACEMENTS)
    wrong_envelope["short_soak"]["source_envelope_id"] = wrong_envelope["static_invariant"]["source_envelope_id"]
    wrong_envelope["short_soak"]["source_envelope_digest"] = wrong_envelope["static_invariant"]["source_envelope_digest"]
    substituted_provenance = copy.deepcopy(REPLACEMENTS)
    substituted_provenance["short_soak"]["provenance"] = {
        "provenance_id": "prov-evil",
        "value": "producer-substituted",
    }
    bad_envelope_result = copy.deepcopy(REPLACEMENT_EXECUTION_ENVELOPES)
    bad_envelope_result["repl-env-short-soak-v1"]["result"] = "FAIL"
    bad_envelope_artifact = copy.deepcopy(REPLACEMENT_EXECUTION_ENVELOPES)
    bad_envelope_artifact["repl-env-short-soak-v1"]["artifact_id"] = "art-substituted"
    duplicate_source_envelope = copy.deepcopy(REPLACEMENTS)
    duplicate_source_envelope["static_invariant"]["source_envelope_id"] = duplicate_source_envelope["short_soak"]["source_envelope_id"]
    duplicate_source_envelope["static_invariant"]["source_envelope_digest"] = duplicate_source_envelope["short_soak"]["source_envelope_digest"]

    return [
        {"id": "S1_baseline", "mode": "attempt", "applicability": "REQUIRED", "attempts": [{"result": "PASS", "failure_class": None}]},
        {"id": "S2_conditional_not_run", "mode": "attempt", "applicability": "CONDITIONALLY_REQUIRED", "condition_applies": True, "attempts": [{"result": "NOT_RUN", "failure_class": None}]},
        {"id": "S3_product_fail_retry", "mode": "attempt", "applicability": "REQUIRED", "allow_infra_retry": True, "attempts": [{"result": "FAIL", "failure_class": "PRODUCT"}, {"result": "PASS", "failure_class": None}]},
        {"id": "S4_infra_retry", "mode": "attempt", "applicability": "REQUIRED", "allow_infra_retry": True, "attempts": [{"result": "FAIL", "failure_class": "INFRA"}, {"result": "PASS", "failure_class": None}]},
        {"id": "S5_flaky", "mode": "attempt", "applicability": "REQUIRED", "allow_infra_retry": True, "attempts": [{"result": "FLAKY", "failure_class": "FLAKY"}, {"result": "PASS", "failure_class": None}]},
        qcase("S6_quarantine_active_valid", copy.deepcopy(REPLACEMENTS)),
        qcase("S7_replacement_omitted_artifact_id", omitted),
        qcase("S8_replacement_wrong_artifact_id", wrong),
        {"id": "S9_same_candidate_reset", "mode": "reset", "candidate_id": "cand-flaky-v1", "prior_candidate_id": "cand-flaky-v1", "root_generation": 2},
        {"id": "S10_successor_valid", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": copy.deepcopy(TRANSITION), "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": PREDECESSOR_ROOT},
        {"id": "S11_successor_missing_transition", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": None, "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": PREDECESSOR_ROOT},
        {"id": "S12_successor_wrong_predecessor", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": wrong_pred, "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": PREDECESSOR_ROOT},
        {"id": "S13_successor_same_candidate_masquerade", "mode": "transition", "candidate_id": "cand-flaky-v1", "transition": same, "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": PREDECESSOR_ROOT},
        {"id": "S14_retention_loss", "mode": "retention", "lineage": lineage(restored=False)},
        {"id": "S15_exact_restore", "mode": "retention", "lineage": lineage()},
        {"id": "S16_identity_swap_same_events", "mode": "retention", "lineage": lineage(artifact_id="art-swapped")},
        {"id": "S17_expected_hash_swap_same_events", "mode": "retention", "lineage": lineage(expected_hash="11d31bcde2b39adf074772ffd52f6431dbef826c3866190be73638d0964b07d1")},
        qcase("S18_quarantine_expired_boundary", copy.deepcopy(REPLACEMENTS), day=14),
        qcase("S19_replacement_set_missing", missing),
        qcase("S20_replacement_set_extra", extra),
        qcase("S21_replacement_set_wrong_member", wrong_member),
        {"id": "S22_predecessor_root_double_substitution", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": bad_root, "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": "0" * 64},
        {"id": "S23_changed_work_identity_substitution", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": bad_work, "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": PREDECESSOR_ROOT},
        {"id": "S24_transition_id_substitution", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": bad_tid, "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": PREDECESSOR_ROOT},
        {"id": "S25_transition_reason_substitution", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": bad_reason, "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR), "claimed_observed_root": PREDECESSOR_ROOT},
        {"id": "S26_predecessor_artifact_substitution", "mode": "transition", "candidate_id": "cand-flaky-v2", "transition": bad_evidence_t, "predecessor_evidence_artifact": bad_evidence, "claimed_observed_root": hashlib.sha256(cbytes(bad_evidence)).hexdigest()},
        qcase("S27_replacement_evidence_id_substitution", substituted_evidence_id),
        qcase("S28_duplicate_replacement_evidence_id", duplicate_evidence_id),
        qcase("S29_dangling_source_envelope", dangling_envelope),
        qcase("S30_wrong_source_envelope", wrong_envelope),
        qcase("S31_substituted_provenance", substituted_provenance),
        qcase("S32_source_envelope_result_mismatch", copy.deepcopy(REPLACEMENTS), bad_envelope_result),
        qcase("S33_source_envelope_artifact_mismatch", copy.deepcopy(REPLACEMENTS), bad_envelope_artifact),
        qcase("S34_duplicate_source_envelope_identity", duplicate_source_envelope),
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
    "S23_changed_work_identity_substitution": "INCONCLUSIVE",
    "S24_transition_id_substitution": "INCONCLUSIVE",
    "S25_transition_reason_substitution": "INCONCLUSIVE",
    "S26_predecessor_artifact_substitution": "INCONCLUSIVE",
    "S27_replacement_evidence_id_substitution": "INCONCLUSIVE",
    "S28_duplicate_replacement_evidence_id": "INCONCLUSIVE",
    "S29_dangling_source_envelope": "INCONCLUSIVE",
    "S30_wrong_source_envelope": "INCONCLUSIVE",
    "S31_substituted_provenance": "INCONCLUSIVE",
    "S32_source_envelope_result_mismatch": "INCONCLUSIVE",
    "S33_source_envelope_artifact_mismatch": "INCONCLUSIVE",
    "S34_duplicate_source_envelope_identity": "INCONCLUSIVE",
}


def bundle(path: pathlib.Path) -> dict[str, Any]:
    observed_source = source_digest(path)
    if observed_source != VALIDATOR_SOURCE_DIGEST:
        raise SystemExit(
            f"validator source identity mismatch: declared={VALIDATOR_SOURCE_DIGEST} observed={observed_source}"
        )
    corpus = cases()
    aggregates = {case["id"]: evaluate(case) for case in corpus}
    if aggregates != EXPECTED:
        diff = {
            key: {"expected": EXPECTED.get(key), "observed": aggregates.get(key)}
            for key in sorted(set(EXPECTED) | set(aggregates))
            if EXPECTED.get(key) != aggregates.get(key)
        }
        raise SystemExit("regression mismatch: " + json.dumps(diff, sort_keys=True))
    harness = copy.deepcopy(HARNESS)
    harness["validator_source_digest"] = observed_source
    result = {
        "schema": "ci-reliability-results-v5",
        "validator_version": VALIDATOR_VERSION,
        "validator_source_digest": observed_source,
        "scenario_aggregates": aggregates,
        "replacement_evidence_positive": copy.deepcopy(REPLACEMENTS),
        "replacement_execution_envelopes": copy.deepcopy(REPLACEMENT_EXECUTION_ENVELOPES),
        "replacement_envelope_digests": copy.deepcopy(REPLACEMENT_ENVELOPE_DIGESTS),
        "replacement_envelope_set_digest": REPLACEMENT_ENVELOPE_SET_DIGEST,
        "candidate_transition_positive": copy.deepcopy(TRANSITION),
        "predecessor_evidence_artifact": copy.deepcopy(PREDECESSOR),
        "predecessor_evidence_artifact_digest": digest(PREDECESSOR),
        "predecessor_evidence_root_recomputed": PREDECESSOR_ROOT,
        "predecessor_root_algorithm": CANONICAL_ALGORITHM,
        "retention_loss_lineage": lineage(restored=False),
        "retention_restore_lineage": lineage(),
    }
    return {
        "fixture_manifest": FIXTURE_MANIFEST,
        "fixture_cases": corpus,
        "harness_contract": harness,
        "result_object": result,
        "digests": {
            "validator_source": observed_source,
            "fixture_manifest": digest(FIXTURE_MANIFEST),
            "fixture_cases": digest(corpus),
            "harness_contract": digest(harness),
            "result_object": digest(result),
            "replacement_execution_envelopes": digest(REPLACEMENT_EXECUTION_ENVELOPES),
            "predecessor_evidence_artifact": digest(PREDECESSOR),
            "predecessor_evidence_root": "sha256:" + PREDECESSOR_ROOT,
        },
    }


if __name__ == "__main__":
    print(json.dumps(bundle(pathlib.Path(__file__).resolve()), sort_keys=True, indent=2))
