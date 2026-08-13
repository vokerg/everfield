#!/usr/bin/env python3
"""Deterministic policy/identity fixture for W2-REM-RIGHTS-02.

Planning evidence only. Standard-library only; not production or legal logic.
"""
from __future__ import annotations

import copy
import hashlib
import json

POLICY_ID = "ORIGINALITY-RISK-v2"
POLICY_EPOCH = 2
SERIALIZATION_VERSION = "EVERFIELD-RIGHTS-CANONICAL-JSON-v1"

ORIGIN_CLASSES = {
    "PROJECT_NATIVE",
    "GENERATED_PROVIDER",
    "EXTERNAL_REFERENCE",
    "EXTERNAL_ASSET",
    "THIRD_PARTY_OUTPUT",
    "LICENSED_MATERIAL",
    "PUBLIC_DOMAIN_CLAIM",
}
REFERENCE_CLASSES = {
    "FACTUAL_OR_FUNCTIONAL",
    "GENERAL_CONCEPTUAL",
    "STYLE_OR_CREATOR_NAMED",
    "EXPRESSION_SPECIFIC",
    "DIRECT_ASSET_OR_CODE",
    "MARK_LIKENESS_PERSONA",
    "CONFIDENTIAL_PRIVATE_RESTRICTED",
    "PUBLIC_DOMAIN_CLAIM",
}
RELEASE_SCOPES = {
    "INTERNAL_RESEARCH": 0,
    "BUILD_CANDIDATE": 1,
    "DISTRIBUTION_CANDIDATE": 2,
    "RELEASE": 3,
}
MEDIA_KINDS = {"NONE", "TEXT", "IMAGE", "AUDIO", "VIDEO", "CODE", "MIXED"}
MATERIAL_TRIGGERS = {
    "MATERIAL_SIMILARITY_SIGNAL",
    "CREDIBLE_COMPLAINT",
    "CONFLICTING_SOURCE",
    "TERMS_AMBIGUITY",
    "PERMISSION_AMBIGUITY",
    "SCOPE_AMBIGUITY",
}
REQUIREMENT_KINDS = (
    "exact_identity",
    "normalized_identity",
    "known_reference_comparison",
    "near_duplicate_checks",
    "targeted_external_search",
    "judgment_review",
    "qualified_legal_review",
)
LEVEL = {"NOT_APPLICABLE": 0, "REQUIRED": 1}

# Fields normalized as mathematical sets before content identity is derived.
SET_FIELDS = {
    "ReferenceUseRecord": {
        "source_reference_ids",
        "allowed_reuse",
        "prohibited_reuse",
        "license_or_permission_refs",
        "provider_terms_refs",
    },
    "OriginalityReviewRecord": {
        "reference_corpus_ref",
        "exact_duplicate_checks",
        "near_duplicate_checks",
        "targeted_external_search_refs",
        "material_signals",
        "blind_spots",
    },
    "ReleaseRightsAssessment": {
        "provider_terms_refs",
        "license_or_permission_refs",
        "unresolved_triggers",
        "freshness_refs",
        "reopen_conditions",
    },
    "OriginalityEvidenceRequirementSet": {
        "material_triggers",
    },
    "SourceEvidenceRoot": {"evidence_entries"},
}

ID_PREFIX = {
    "ReferenceUseRecord": "rur-sha256",
    "OriginalityReviewRecord": "orr-sha256",
    "ReleaseRightsAssessment": "rra-sha256",
    "OriginalityEvidenceRequirementSet": "oers-sha256",
    "SourceEvidenceRoot": "ser-sha256",
}

def _normalize(value, *, record_type=None, field_name=None):
    if isinstance(value, dict):
        return {
            k: _normalize(v, record_type=record_type, field_name=k)
            for k, v in sorted(value.items())
        }
    if isinstance(value, list):
        normalized = [
            _normalize(v, record_type=record_type, field_name=field_name)
            for v in value
        ]
        if record_type and field_name in SET_FIELDS.get(record_type, set()):
            encoded = [canonical_json(v) for v in normalized]
            if len(encoded) != len(set(encoded)):
                raise ValueError(f"duplicate set member: {record_type}.{field_name}")
            normalized = [
                v for _, v in sorted(zip(encoded, normalized), key=lambda pair: pair[0])
            ]
        return normalized
    if value is None or isinstance(value, (str, int, bool)):
        return value
    raise TypeError(f"unsupported canonical type: {type(value)!r}")

def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def canonical_payload(record_type, payload):
    normalized = _normalize(copy.deepcopy(payload), record_type=record_type)
    return canonical_json(
        {
            "serialization_version": SERIALIZATION_VERSION,
            "record_type": record_type,
            "payload": normalized,
        }
    ).encode("utf-8")

def content_id(record_type, payload):
    if record_type not in ID_PREFIX:
        raise ValueError(f"unsupported record type: {record_type}")
    domain = f"everfield:rights:{record_type}:v1\0".encode("utf-8")
    digest = hashlib.sha256(domain + canonical_payload(record_type, payload)).hexdigest()
    return f"{ID_PREFIX[record_type]}:{digest}"

def validate_claimed_id(record_type, payload, claimed_id):
    return claimed_id == content_id(record_type, payload)

def source_evidence_root(evidence_entries):
    payload = {"evidence_entries": evidence_entries}
    return content_id("SourceEvidenceRoot", payload)

def _required():
    return {k: "NOT_APPLICABLE" for k in REQUIREMENT_KINDS}

def _join(requirements, contribution):
    out = dict(requirements)
    for key, value in contribution.items():
        if value not in LEVEL:
            raise ValueError(f"unclosed requirement level: {value}")
        if LEVEL[value] > LEVEL[out[key]]:
            out[key] = value
    return out

def _validate_policy_input(inp):
    if inp.get("policy_id") != POLICY_ID or inp.get("policy_epoch") != POLICY_EPOCH:
        return "POLICY_UNRESOLVED"
    if inp.get("origin_class") not in ORIGIN_CLASSES:
        return "POLICY_UNRESOLVED"
    if inp.get("reference_class") not in REFERENCE_CLASSES:
        return "POLICY_UNRESOLVED"
    if inp.get("release_scope_class") not in RELEASE_SCOPES:
        return "POLICY_UNRESOLVED"
    if inp.get("media_kind") not in MEDIA_KINDS:
        return "POLICY_UNRESOLVED"
    for boolean_field in (
        "references_exist",
        "incorporation_or_release_intent",
        "legal_interpretation_material",
    ):
        if type(inp.get(boolean_field)) is not bool:
            return "POLICY_UNRESOLVED"
    triggers = inp.get("material_trigger_set")
    if not isinstance(triggers, list):
        return "POLICY_UNRESOLVED"
    if len(triggers) != len(set(triggers)):
        return "POLICY_UNRESOLVED"
    if any(t not in MATERIAL_TRIGGERS for t in triggers):
        return "POLICY_UNRESOLVED"
    return None

def _rule_contributions(inp):
    """Closed rule set. Multiple matches are merged with REQUIRED dominance."""
    scope = RELEASE_SCOPES[inp["release_scope_class"]]
    ref = inp["reference_class"]
    origin = inp["origin_class"]
    references = inp["references_exist"]
    media_applicable = inp["media_kind"] != "NONE"
    distribution = scope >= RELEASE_SCOPES["DISTRIBUTION_CANDIDATE"]
    build_or_stronger = scope >= RELEASE_SCOPES["BUILD_CANDIDATE"]
    triggers = set(inp["material_trigger_set"])
    legal_material = inp["legal_interpretation_material"]
    incorporation = inp["incorporation_or_release_intent"]

    rules = []

    # Total conservative baseline: covers every admitted tuple.
    baseline = {}
    if references:
        baseline["known_reference_comparison"] = "REQUIRED"
    if build_or_stronger or incorporation or origin != "PROJECT_NATIVE":
        baseline["exact_identity"] = "REQUIRED"
    if distribution and references and media_applicable:
        baseline["normalized_identity"] = "REQUIRED"
        baseline["near_duplicate_checks"] = "REQUIRED"
    if distribution and ref not in {"FACTUAL_OR_FUNCTIONAL", "GENERAL_CONCEPTUAL"}:
        baseline["judgment_review"] = "REQUIRED"
    if legal_material or triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"}:
        baseline["qualified_legal_review"] = "REQUIRED"
    rules.append(("R0_TOTAL_BASELINE", baseline))

    # Internal research is still evidence-bound when external/generated/reference material is used.
    if scope == RELEASE_SCOPES["INTERNAL_RESEARCH"]:
        internal = {}
        if references or origin != "PROJECT_NATIVE":
            internal["exact_identity"] = "REQUIRED"
        if references:
            internal["known_reference_comparison"] = "REQUIRED"
        rules.append(("R1_INTERNAL_RESEARCH", internal))

    # Build candidate native/general material: resolve former CONDITIONALs with typed predicates.
    if build_or_stronger and origin == "PROJECT_NATIVE" and ref in {
        "FACTUAL_OR_FUNCTIONAL",
        "GENERAL_CONCEPTUAL",
        "STYLE_OR_CREATOR_NAMED",
    }:
        native = {"exact_identity": "REQUIRED"}
        if references:
            native["known_reference_comparison"] = "REQUIRED"
            native["judgment_review"] = "REQUIRED"
        if media_applicable and references:
            native["normalized_identity"] = "REQUIRED"
            native["near_duplicate_checks"] = "REQUIRED"
        rules.append(("R2_NATIVE_BUILD", native))

    if distribution and ref == "STYLE_OR_CREATOR_NAMED":
        style = {
            "exact_identity": "REQUIRED",
            "normalized_identity": "REQUIRED",
            "known_reference_comparison": "REQUIRED",
            "near_duplicate_checks": "REQUIRED",
            "targeted_external_search": "REQUIRED",
            "judgment_review": "REQUIRED",
        }
        if legal_material or triggers:
            style["qualified_legal_review"] = "REQUIRED"
        rules.append(("R3_STYLE_OR_CREATOR", style))

    if distribution and ref in {"EXPRESSION_SPECIFIC", "DIRECT_ASSET_OR_CODE"}:
        expression = {
            "exact_identity": "REQUIRED",
            "normalized_identity": "REQUIRED",
            "known_reference_comparison": "REQUIRED",
            "judgment_review": "REQUIRED",
        }
        if media_applicable:
            expression["near_duplicate_checks"] = "REQUIRED"
        if references:
            expression["targeted_external_search"] = "REQUIRED"
        if legal_material or triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"}:
            expression["qualified_legal_review"] = "REQUIRED"
        rules.append(("R4_EXPRESSION_OR_DIRECT", expression))

    if distribution and ref == "MARK_LIKENESS_PERSONA":
        mark = {
            "exact_identity": "REQUIRED",
            "known_reference_comparison": "REQUIRED",
            "targeted_external_search": "REQUIRED",
            "judgment_review": "REQUIRED",
        }
        if media_applicable:
            mark["normalized_identity"] = "REQUIRED"
            mark["near_duplicate_checks"] = "REQUIRED"
        if legal_material or scope >= RELEASE_SCOPES["RELEASE"]:
            mark["qualified_legal_review"] = "REQUIRED"
        rules.append(("R5_MARK_LIKENESS_PERSONA", mark))

    # High-risk material can never be made clear merely by similarity checks.
    if ref == "CONFIDENTIAL_PRIVATE_RESTRICTED":
        rules.append(
            (
                "R6_RESTRICTED_REFERENCE",
                {
                    "exact_identity": "REQUIRED",
                    "known_reference_comparison": "REQUIRED" if references else "NOT_APPLICABLE",
                    "judgment_review": "REQUIRED",
                    "qualified_legal_review": "REQUIRED",
                },
            )
        )

    if triggers:
        triggered = {
            "known_reference_comparison": "REQUIRED",
            "judgment_review": "REQUIRED",
        }
        if media_applicable:
            triggered["near_duplicate_checks"] = "REQUIRED"
        if references:
            triggered["targeted_external_search"] = "REQUIRED"
        if triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"} or legal_material:
            triggered["qualified_legal_review"] = "REQUIRED"
        rules.append(("R7_MATERIAL_TRIGGER", triggered))

    return rules

def compile_policy(inp, *, reverse_rules=False):
    invalid = _validate_policy_input(inp)
    if invalid:
        return {"status": "UNKNOWN", "reason": invalid}

    req = _required()
    rules = _rule_contributions(inp)
    if reverse_rules:
        rules = list(reversed(rules))
    trace = []
    for rule_id, contribution in rules:
        req = _join(req, contribution)
        trace.append(rule_id)

    # Closed output: CONDITIONAL is not a legal terminal compiler value.
    if any(v not in LEVEL for v in req.values()):
        raise AssertionError("compiler emitted non-closed requirement")
    payload = {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "artifact_id": inp["artifact_id"],
        "reference_use_id": inp["reference_use_id"],
        "release_scope_ref": inp["release_scope_ref"],
        "requirements": req,
        "material_triggers": sorted(inp["material_trigger_set"]),
        "compiler_trace": sorted(trace),
    }
    return {
        "status": "COMPILED",
        "requirements": req,
        "compiler_trace": sorted(trace),
        "requirement_set_id": content_id("OriginalityEvidenceRequirementSet", payload),
        "payload": payload,
    }

def derive_state(requirements, evidence_states, material_triggers, explicit_restriction=False):
    required = [k for k, v in requirements.items() if v == "REQUIRED"]
    independent_risk = set(material_triggers) & {
        "MATERIAL_SIMILARITY_SIGNAL",
        "CREDIBLE_COMPLAINT",
        "CONFLICTING_SOURCE",
    }
    if independent_risk:
        return {"state": "QUARANTINED", "reason": "MATERIAL_RISK"}
    stale = [k for k in required if evidence_states.get(k) == "STALE"]
    if stale:
        return {"state": "UNKNOWN", "reason": "STALE_EVIDENCE", "evidence_kinds": sorted(stale)}
    bad = [
        k
        for k in required
        if evidence_states.get(k) in {None, "MISSING", "CONFLICTING", "OUT_OF_SCOPE", "NOT_RUN", "INCONCLUSIVE"}
    ]
    if bad:
        return {"state": "UNKNOWN", "reason": "REQUIRED_EVIDENCE_UNSATISFIED", "evidence_kinds": sorted(bad)}
    if explicit_restriction:
        return {"state": "RESTRICTED", "reason": "EXPLICIT_SCOPE_RESTRICTION"}
    if all(evidence_states.get(k) == "SATISFIED" for k in required):
        return {"state": "CLEAR", "reason": "ALL_REQUIRED_EVIDENCE_SATISFIED"}
    return {"state": "UNKNOWN", "reason": "UNCLASSIFIED_EVIDENCE_STATE"}

def assert_equal(a, b, label):
    if a != b:
        raise AssertionError(f"{label}: {a!r} != {b!r}")

def assert_not_equal(a, b, label):
    if a == b:
        raise AssertionError(f"{label}: values unexpectedly equal")

def base_policy_input():
    return {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "artifact_id": "artifact:demo-001",
        "reference_use_id": "rur:demo",
        "release_scope_ref": "scope:release",
        "origin_class": "PROJECT_NATIVE",
        "reference_class": "STYLE_OR_CREATOR_NAMED",
        "release_scope_class": "RELEASE",
        "material_trigger_set": [],
        "media_kind": "IMAGE",
        "references_exist": True,
        "incorporation_or_release_intent": True,
        "legal_interpretation_material": False,
    }

def base_reference_use():
    return {
        "candidate_artifact_id": "artifact:demo-001",
        "source_reference_ids": ["source:b", "source:a"],
        "reference_class": "STYLE_OR_CREATOR_NAMED",
        "declared_purpose": "visual mood reference only",
        "allowed_reuse": ["facts", "high-level-composition"],
        "prohibited_reuse": ["direct-copy", "asset-reuse"],
        "license_or_permission_refs": ["license:1"],
        "provider_terms_refs": ["terms:1"],
        "provider_input_admission_ref": "admission:1",
        "release_scope_ref": "scope:release",
        "provenance_record_ref": "prov:1",
        "originality_risk_policy_ref": f"{POLICY_ID}@{POLICY_EPOCH}",
        "source_evidence_root": "ser-sha256:placeholder",
    }

def run():
    results = []

    overlap = base_policy_input()
    compiled = compile_policy(overlap)
    assert_equal(compiled["status"], "COMPILED", "overlap compiles")
    for key in (
        "exact_identity",
        "normalized_identity",
        "known_reference_comparison",
        "near_duplicate_checks",
        "targeted_external_search",
        "judgment_review",
    ):
        assert_equal(compiled["requirements"][key], "REQUIRED", f"overlap strongest {key}")
    assert_equal(
        compile_policy(overlap, reverse_rules=True)["requirements"],
        compiled["requirements"],
        "rule-order independence",
    )
    results.append("T01_OVERLAP_JOIN_ORDER_INDEPENDENT")

    general = base_policy_input()
    general["reference_class"] = "GENERAL_CONCEPTUAL"
    general["release_scope_class"] = "BUILD_CANDIDATE"
    c_general = compile_policy(general)
    assert_equal(
        set(c_general["requirements"].values()) <= {"REQUIRED", "NOT_APPLICABLE"},
        True,
        "no CONDITIONAL terminal values",
    )
    results.append("T02_NO_CONDITIONAL_TERMINAL")

    unknown = base_policy_input()
    unknown["media_kind"] = "UNDECLARED"
    assert_equal(
        compile_policy(unknown),
        {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"},
        "unknown fail closed",
    )
    results.append("T03_UNKNOWN_FAILS_CLOSED")

    rur = base_reference_use()
    rid = content_id("ReferenceUseRecord", rur)
    assert_equal(validate_claimed_id("ReferenceUseRecord", rur, rid), True, "id recomputes")
    reordered = copy.deepcopy(rur)
    reordered["source_reference_ids"] = list(reversed(reordered["source_reference_ids"]))
    reordered["allowed_reuse"] = list(reversed(reordered["allowed_reuse"]))
    assert_equal(content_id("ReferenceUseRecord", reordered), rid, "set ordering canonical")
    results.append("T04_SET_ORDER_CANONICAL")

    for field, mutated_value in (
        ("declared_purpose", "direct implementation reference"),
        ("release_scope_ref", "scope:internal"),
        ("provider_terms_refs", ["terms:2"]),
        ("license_or_permission_refs", ["license:2"]),
        ("source_reference_ids", ["source:a", "source:c"]),
    ):
        mutated = copy.deepcopy(rur)
        mutated[field] = mutated_value
        assert_not_equal(content_id("ReferenceUseRecord", mutated), rid, f"bound mutation {field}")
    results.append("T05_BOUND_FIELDS_CHANGE_REFERENCE_USE_ID")

    evidence = [
        {
            "kind": "ProviderTermsRecord",
            "record_id": "terms:1",
            "content_sha256": "a" * 64,
            "immutable_ref": "blob:terms",
        },
        {
            "kind": "RightsProvenanceRecord",
            "record_id": "prov:1",
            "content_sha256": "b" * 64,
            "immutable_ref": "blob:prov",
        },
    ]
    root = source_evidence_root(evidence)
    assert_equal(source_evidence_root(list(reversed(evidence))), root, "root set ordering")
    evidence_mut = copy.deepcopy(evidence)
    evidence_mut[0]["content_sha256"] = "c" * 64
    assert_not_equal(source_evidence_root(evidence_mut), root, "root content mutation")
    results.append("T06_SOURCE_ROOT_RECOMPUTABLE")

    all_required = {k: "REQUIRED" for k in REQUIREMENT_KINDS}
    all_sat = {k: "SATISFIED" for k in REQUIREMENT_KINDS}
    for kind in REQUIREMENT_KINDS:
        states = dict(all_sat)
        states[kind] = "STALE"
        state = derive_state(all_required, states, [])
        assert_equal(state["state"], "UNKNOWN", f"stale state {kind}")
        assert_equal(state["reason"], "STALE_EVIDENCE", f"stale reason {kind}")
        quarantined = derive_state(all_required, states, ["CREDIBLE_COMPLAINT"])
        assert_equal(quarantined["state"], "QUARANTINED", f"risk precedence {kind}")
    results.append("T07_ALL_REQUIRED_KINDS_HAVE_STALE_PRECEDENCE")

    clear_state = derive_state(all_required, all_sat, [])
    assert_equal(clear_state["state"], "CLEAR", "all satisfied clear")
    results.append("T08_CLEAR_REQUIRES_ALL_REQUIRED_SATISFIED")

    # Content identities for every authority-bearing record type.
    example_records = {
        "OriginalityReviewRecord": {
            "candidate_artifact_id": "artifact:demo-001",
            "reference_use_id": rid,
            "policy_epoch_ref": f"{POLICY_ID}@{POLICY_EPOCH}",
            "compiled_requirement_set_ref": compiled["requirement_set_id"],
            "reference_corpus_ref": ["source:a", "source:b"],
            "exact_duplicate_checks": ["check:1"],
            "near_duplicate_checks": ["check:2"],
            "targeted_external_search_refs": ["search:1"],
            "judgment_panel_ref": "panel:1",
            "qualified_legal_review_ref": "NOT_APPLICABLE",
            "material_signals": [],
            "blind_spots": [],
            "result": "NO_MATERIAL_SIGNAL_FOUND",
            "legal_conclusion": "NONE",
        },
        "ReleaseRightsAssessment": {
            "artifact_id": "artifact:demo-001",
            "release_scope_ref": "scope:release",
            "provenance_record_ref": "prov:1",
            "reference_use_id": rid,
            "policy_epoch_ref": f"{POLICY_ID}@{POLICY_EPOCH}",
            "compiled_requirement_set_ref": compiled["requirement_set_id"],
            "provider_terms_refs": ["terms:1"],
            "license_or_permission_refs": ["license:1"],
            "originality_review_ref": "review:1",
            "unresolved_triggers": [],
            "derived_rights_or_terms_state": "CLEAR",
            "reason_code": "ALL_REQUIRED_EVIDENCE_SATISFIED",
            "derivation_trace": ["compile", "validate", "derive"],
            "freshness_refs": ["fresh:1"],
            "reopen_conditions": ["terms-change"],
        },
        "OriginalityEvidenceRequirementSet": compiled["payload"],
    }
    for record_type, payload in example_records.items():
        cid = content_id(record_type, payload)
        assert_equal(validate_claimed_id(record_type, payload, cid), True, f"{record_type} recompute")
        mutation = copy.deepcopy(payload)
        first_key = next(k for k in mutation if k not in {"material_triggers"})
        mutation[first_key] = "mutated-value"
        assert_not_equal(content_id(record_type, mutation), cid, f"{record_type} mutation changes id")
    results.append("T09_ALL_AUTHORITY_RECORD_IDS_RECOMPUTABLE")

    digest_payload = canonical_json({"tests": results}).encode("utf-8")
    summary = {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "serialization_version": SERIALIZATION_VERSION,
        "tests_passed": len(results),
        "tests": results,
        "result_digest_sha256": hashlib.sha256(digest_payload).hexdigest(),
    }
    print(canonical_json(summary))
    return summary

if __name__ == "__main__":
    run()
