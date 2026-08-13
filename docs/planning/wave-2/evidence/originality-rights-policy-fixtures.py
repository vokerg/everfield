#!/usr/bin/env python3
"""Deterministic delta fixture for W2-REM-RIGHTS-05.

Planning evidence only; not production or legal logic. The unchanged Issue #142
fixture is loaded from its exact Git blob. This layer changes only
PG-REM4-RIGHTS-M01: duplicate derived-state material triggers fail closed, and
the malformed matrix/regression summary explicitly covers that set surface.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import subprocess

BASE_ISSUE = 142
BASE_HEAD_SHA = "4b61b276bb28bb114a650e003a7a5d0aeb77411a"
BASE_FIXTURE_BLOB = "39fcdc292cd37661a061c6d3027715106b3a3d27"
BASE_SOURCE_SHA256 = "6d078060db7f6a1f43fccc1c3d86cc8bacae51d61dfe40dd6e85d76bf19772f5"
MALFORMED_MATRIX_VERSION = "EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v2"


def _load_base_source() -> bytes:
    source = subprocess.check_output(["git", "cat-file", "blob", BASE_FIXTURE_BLOB])
    if hashlib.sha256(source).hexdigest() != BASE_SOURCE_SHA256:
        raise AssertionError("Issue #142 fixture byte SHA-256 mismatch")
    observed_blob = subprocess.check_output(["git", "hash-object", "--stdin"], input=source, text=False).decode().strip()
    if observed_blob != BASE_FIXTURE_BLOB:
        raise AssertionError("Issue #142 fixture Git blob mismatch")
    return source


_base_source = _load_base_source()
_NS = {"__name__": "_w2_rem_rights_04_base"}
exec(compile(_base_source, f"git-blob:{BASE_FIXTURE_BLOB}", "exec"), _NS)

# Re-export the unchanged bounded policy fixture surface for direct consumers.
for _name, _value in tuple(_NS.items()):
    if not _name.startswith("__") and _name != "MALFORMED_MATRIX_VERSION":
        globals()[_name] = _value

_BASE_DERIVE_STATE = _NS["derive_state"]
_BASE_MALFORMED_MATRIX = _NS["run_malformed_scalar_matrix"]
_BASE_RUN = _NS["run"]
_NS["MALFORMED_MATRIX_VERSION"] = MALFORMED_MATRIX_VERSION


def derive_state(requirements, evidence_states, material_triggers, explicit_restriction=False):
    """Issue #148 delta: duplicate set-like triggers are malformed and fail closed."""
    if isinstance(material_triggers, list) and all(
        _NS["_closed_member"](item, _NS["MATERIAL_TRIGGERS"]) for item in material_triggers
    ):
        if len(material_triggers) != len(set(material_triggers)):
            return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    return _BASE_DERIVE_STATE(requirements, evidence_states, material_triggers, explicit_restriction)


_NS["derive_state"] = derive_state


def _duplicate_trigger_regressions():
    required = {kind: "REQUIRED" for kind in _NS["REQUIREMENT_KINDS"]}
    satisfied = {kind: "SATISFIED" for kind in _NS["REQUIREMENT_KINDS"]}
    expected = {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    for trigger in sorted(_NS["MATERIAL_TRIGGERS"]):
        _NS["assert_equal"](
            derive_state(required, satisfied, [trigger, trigger]), expected,
            f"duplicate derived trigger fails closed {trigger}",
        )
    ordered = ["SCOPE_AMBIGUITY", "TERMS_AMBIGUITY"]
    _NS["assert_equal"](
        derive_state(required, satisfied, ordered),
        derive_state(required, satisfied, list(reversed(ordered))),
        "valid unique derived trigger order is non-authoritative",
    )
    for nested in (["TERMS_AMBIGUITY", ["SCOPE_AMBIGUITY"]], [{"trigger": "TERMS_AMBIGUITY"}]):
        _NS["assert_equal"](
            derive_state(required, satisfied, nested), expected,
            f"nested malformed derived trigger fails closed {nested!r}",
        )


def run_malformed_scalar_matrix():
    """Inherited 462 scalar cases plus all six duplicate closed-domain triggers."""
    matrix = _BASE_MALFORMED_MATRIX()
    required = {kind: "REQUIRED" for kind in _NS["REQUIREMENT_KINDS"]}
    satisfied = {kind: "SATISFIED" for kind in _NS["REQUIREMENT_KINDS"]}
    expected = {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    for trigger in sorted(_NS["MATERIAL_TRIGGERS"]):
        got = derive_state(required, satisfied, [trigger, trigger])
        if got != expected:
            raise AssertionError(f"duplicate trigger set not fail-closed: {trigger} => {got!r}")
    matrix.pop("digest_sha256", None)
    matrix["version"] = MALFORMED_MATRIX_VERSION
    matrix["case_count"] += len(_NS["MATERIAL_TRIGGERS"])
    matrix["digest_sha256"] = hashlib.sha256(_NS["canonical_json"](matrix).encode()).hexdigest()
    return matrix


_NS["run_malformed_scalar_matrix"] = run_malformed_scalar_matrix


def run():
    """Run inherited T01-T15/audit plus the bounded duplicate-trigger regression."""
    _duplicate_trigger_regressions()
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        summary = _BASE_RUN()
    tests = list(summary["tests"]) + ["T16_DERIVED_TRIGGER_SET_TOTAL_FAIL_CLOSED"]
    matrix = run_malformed_scalar_matrix()
    audit = {
        "valid_domain_combinations_checked": summary["valid_domain_combinations_checked"],
        "reverse_rule_order_requirement_mismatches": summary["reverse_rule_order_requirement_mismatches"],
        "nonclosed_requirement_outputs": summary["nonclosed_requirement_outputs"],
        "audit_digest_sha256": summary["audit_digest_sha256"],
    }
    digest_payload = _NS["canonical_json"]({"tests": tests, "matrix": matrix, "audit": audit}).encode("utf-8")
    summary.update({
        "malformed_matrix_version": MALFORMED_MATRIX_VERSION,
        "tests_passed": len(tests),
        "tests": tests,
        "malformed_scalar_cases": matrix["case_count"],
        "uncaught_exception_count": matrix["uncaught_exception_count"],
        "result_digest_sha256": hashlib.sha256(digest_payload).hexdigest(),
    })
    print(_NS["canonical_json"](summary))
    return summary


if __name__ == "__main__":
    run()
