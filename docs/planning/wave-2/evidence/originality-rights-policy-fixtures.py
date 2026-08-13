#!/usr/bin/env python3
"""Deterministic policy/identity fixture for W2-REM-RIGHTS-03.

Planning evidence only. Standard-library only; not production or legal logic.
Closes Issue #125 findings PG-REM2-RIGHTS-M01 and PG-REM2-RIGHTS-M02.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re

POLICY_ID = "ORIGINALITY-RISK-v2"
POLICY_EPOCH = 2
SERIALIZATION_VERSION = "EVERFIELD-RIGHTS-CANONICAL-JSON-v1"
SCHEMA_VERSION = "EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1"

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

POLICY_INPUT_FIELDS = {
    "policy_id",
    "policy_epoch",
    "artifact_id",
    "reference_use_id",
    "release_scope_ref",
    "origin_class",
    "reference_class",
    "release_scope_class",
    "material_trigger_set",
    "media_kind",
    "references_exist",
    "incorporation_or_release_intent",
    "legal_interpretation_material",
}

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
    "OriginalityEvidenceRequirementSet": {"material_triggers"},
    "SourceEvidenceRoot": {"evidence_entries"},
}

ID_PREFIX = {
    "ReferenceUseRecord": "rur-sha256",
    "OriginalityReviewRecord": "orr-sha256",
    "ReleaseRightsAssessment": "rra-sha256",
    "OriginalityEvidenceRequirementSet": "oers-sha256",
    "SourceEvidenceRoot": "ser-sha256",
}

RECORD_FIELDS = {
    "ReferenceUseRecord": {
        "candidate_artifact_id",
        "source_reference_ids",
        "reference_class",
        "declared_purpose",
        "allowed_reuse",
        "prohibited_reuse",
        "license_or_permission_refs",
        "provider_terms_refs",
        "provider_input_admission_ref",
        "release_scope_ref",
        "provenance_record_ref",
        "originality_risk_policy_ref",
        "source_evidence_root",
    },
    "OriginalityReviewRecord": {
        "candidate_artifact_id",
        "reference_use_id",
        "policy_epoch_ref",
        "compiled_requirement_set_ref",
        "reference_corpus_ref",
        "exact_duplicate_checks",
        "near_duplicate_checks",
        "targeted_external_search_refs",
        "judgment_panel_ref",
        "qualified_legal_review_ref",
        "material_signals",
        "blind_spots",
        "result",
        "legal_conclusion",
    },
    "ReleaseRightsAssessment": {
        "artifact_id",
        "release_scope_ref",
        "provenance_record_ref",
        "reference_use_id",
        "policy_epoch_ref",
        "compiled_requirement_set_ref",
        "provider_terms_refs",
        "license_or_permission_refs",
        "originality_review_ref",
        "unresolved_triggers",
        "derived_rights_or_terms_state",
        "reason_code",
        "derivation_trace",
        "freshness_refs",
        "reopen_conditions",
    },
    "OriginalityEvidenceRequirementSet": {
        "policy_id",
        "policy_epoch",
        "artifact_id",
        "reference_use_id",
        "release_scope_ref",
        "requirements",
        "material_triggers",
        "compiler_trace",
    },
    "SourceEvidenceRoot": {"evidence_entries"},
}

IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,63}:[A-Za-z0-9][A-Za-z0-9._:@/+-]{0,255}$")
CONTENT_ID_RE = {
    k: re.compile(rf"^{re.escape(prefix)}:[0-9a-f]{{64}}$")
    for k, prefix in ID_PREFIX.items()
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
IMMUTABLE_REF_RE = re.compile(
    r"^(?:git-blob:[0-9a-f]{40}|git-commit:[0-9a-f]{40}|repo:[^\s@]+@[0-9a-f]{40}|protected:[A-Za-z0-9._:/+-]+)$"
)


def _is_string(value):
    return isinstance(value, str) and not isinstance(value, bool)


def _nonempty_string(value):
    return _is_string(value) and bool(value) and value == value.strip() and "\x00" not in value


def _identifier(value):
    return _nonempty_string(value) and IDENT_RE.fullmatch(value) is not None


def _content_identity(record_type, value):
    return _nonempty_string(value) and CONTENT_ID_RE[record_type].fullmatch(value) is not None


def _string_list(value, *, allow_empty=True, identifiers=False):
    if not isinstance(value, list):
        return False
    if not allow_empty and not value:
        return False
    validator = _identifier if identifiers else _nonempty_string
    if any(not validator(item) for item in value):
        return False
    return len(value) == len(set(value))


def _normalize(value, *, record_type=None, field_name=None):
    if isinstance(value, dict):
        if any(not _nonempty_string(k) for k in value):
            raise ValueError("object keys must be nonempty strings")
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


def _validate_evidence_entry(entry):
    required = {"kind", "record_id", "content_sha256", "immutable_ref"}
    if not isinstance(entry, dict) or set(entry) != required:
        return False
    if not _nonempty_string(entry["kind"]):
        return False
    if not _identifier(entry["record_id"]):
        return False
    if not _nonempty_string(entry["content_sha256"]) or SHA256_RE.fullmatch(entry["content_sha256"]) is None:
        return False
    if not _nonempty_string(entry["immutable_ref"]) or IMMUTABLE_REF_RE.fullmatch(entry["immutable_ref"]) is None:
        return False
    return True


def validate_record_schema(record_type, payload):
    """Return (valid, reason) under closed authority schema v1."""
    if record_type not in RECORD_FIELDS:
        return False, "UNSUPPORTED_RECORD_TYPE"
    if not isinstance(payload, dict):
        return False, "PAYLOAD_NOT_OBJECT"
    required = RECORD_FIELDS[record_type]
    if set(payload) != required:
        missing = sorted(required - set(payload))
        unknown = sorted(set(payload) - required)
        return False, f"FIELD_SET_MISMATCH:missing={missing}:unknown={unknown}"

    if record_type == "ReferenceUseRecord":
        if not _identifier(payload["candidate_artifact_id"]): return False, "candidate_artifact_id"
        if not _string_list(payload["source_reference_ids"], identifiers=True): return False, "source_reference_ids"
        if payload["reference_class"] not in REFERENCE_CLASSES: return False, "reference_class"
        if not _nonempty_string(payload["declared_purpose"]): return False, "declared_purpose"
        for field in ("allowed_reuse", "prohibited_reuse", "license_or_permission_refs", "provider_terms_refs"):
            if not _string_list(payload[field], identifiers=True): return False, field
        for field in ("provider_input_admission_ref", "release_scope_ref", "provenance_record_ref"):
            if not _identifier(payload[field]): return False, field
        if payload["originality_risk_policy_ref"] != f"{POLICY_ID}@{POLICY_EPOCH}": return False, "originality_risk_policy_ref"
        if not _content_identity("SourceEvidenceRoot", payload["source_evidence_root"]): return False, "source_evidence_root"

    elif record_type == "OriginalityReviewRecord":
        if not _identifier(payload["candidate_artifact_id"]): return False, "candidate_artifact_id"
        if not _content_identity("ReferenceUseRecord", payload["reference_use_id"]): return False, "reference_use_id"
        if payload["policy_epoch_ref"] != f"{POLICY_ID}@{POLICY_EPOCH}": return False, "policy_epoch_ref"
        if not _content_identity("OriginalityEvidenceRequirementSet", payload["compiled_requirement_set_ref"]): return False, "compiled_requirement_set_ref"
        for field in ("reference_corpus_ref", "exact_duplicate_checks", "near_duplicate_checks", "targeted_external_search_refs"):
            if not _string_list(payload[field], identifiers=True): return False, field
        for field in ("material_signals", "blind_spots"):
            if not _string_list(payload[field]): return False, field
        for field in ("judgment_panel_ref", "qualified_legal_review_ref"):
            if not _nonempty_string(payload[field]): return False, field
        if payload["result"] not in {"NO_MATERIAL_SIGNAL_FOUND", "MATERIAL_SIGNAL_FOUND", "INCONCLUSIVE"}: return False, "result"
        if payload["legal_conclusion"] not in {"NONE", "QUALIFIED_REVIEW_REQUIRED", "EXTERNAL_LEGAL_INPUT_RECORDED"}: return False, "legal_conclusion"

    elif record_type == "ReleaseRightsAssessment":
        for field in ("artifact_id", "release_scope_ref", "provenance_record_ref"):
            if not _identifier(payload[field]): return False, field
        if not _content_identity("ReferenceUseRecord", payload["reference_use_id"]): return False, "reference_use_id"
        if payload["policy_epoch_ref"] != f"{POLICY_ID}@{POLICY_EPOCH}": return False, "policy_epoch_ref"
        if not _content_identity("OriginalityEvidenceRequirementSet", payload["compiled_requirement_set_ref"]): return False, "compiled_requirement_set_ref"
        for field in ("provider_terms_refs", "license_or_permission_refs", "freshness_refs", "reopen_conditions"):
            if not _string_list(payload[field], identifiers=field != "reopen_conditions"): return False, field
        if not _content_identity("OriginalityReviewRecord", payload["originality_review_ref"]): return False, "originality_review_ref"
        if not _string_list(payload["unresolved_triggers"]): return False, "unresolved_triggers"
        if payload["derived_rights_or_terms_state"] not in {"CLEAR", "UNKNOWN", "QUARANTINED", "RESTRICTED"}: return False, "derived_rights_or_terms_state"
        if not _nonempty_string(payload["reason_code"]): return False, "reason_code"
        if not _string_list(payload["derivation_trace"], allow_empty=False): return False, "derivation_trace"

    elif record_type == "OriginalityEvidenceRequirementSet":
        if payload["policy_id"] != POLICY_ID or payload["policy_epoch"] != POLICY_EPOCH: return False, "policy"
        if not _identifier(payload["artifact_id"]): return False, "artifact_id"
        if not _content_identity("ReferenceUseRecord", payload["reference_use_id"]): return False, "reference_use_id"
        if not _identifier(payload["release_scope_ref"]): return False, "release_scope_ref"
        req = payload["requirements"]
        if not isinstance(req, dict) or set(req) != set(REQUIREMENT_KINDS): return False, "requirements"
        if any(value not in LEVEL for value in req.values()): return False, "requirements"
        triggers = payload["material_triggers"]
        if not isinstance(triggers, list) or any(type(t) is not str or t not in MATERIAL_TRIGGERS for t in triggers): return False, "material_triggers"
        if len(triggers) != len(set(triggers)): return False, "material_triggers"
        trace = payload["compiler_trace"]
        if not _string_list(trace, allow_empty=False): return False, "compiler_trace"

    elif record_type == "SourceEvidenceRoot":
        entries = payload["evidence_entries"]
        if not isinstance(entries, list) or not entries:
            return False, "evidence_entries"
        if any(not _validate_evidence_entry(entry) for entry in entries):
            return False, "evidence_entry"
        record_ids = [entry["record_id"] for entry in entries]
        if len(record_ids) != len(set(record_ids)):
            return False, "duplicate_or_conflicting_record_id"
        encoded = [canonical_json(_normalize(entry)) for entry in entries]
        if len(encoded) != len(set(encoded)):
            return False, "duplicate_evidence_entry"

    return True, "VALID"


def canonical_payload(record_type, payload):
    valid, reason = validate_record_schema(record_type, payload)
    if not valid:
        raise ValueError(f"schema invalid for {record_type}: {reason}")
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
    try:
        if not _content_identity(record_type, claimed_id):
            return False
        return claimed_id == content_id(record_type, payload)
    except (KeyError, TypeError, ValueError):
        return False


def source_evidence_root(evidence_entries):
    return content_id("SourceEvidenceRoot", {"evidence_entries": evidence_entries})


def _required():
    return {k: "NOT_APPLICABLE" for k in REQUIREMENT_KINDS}


def _join(requirements, contribution):
    out = dict(requirements)
    for key, value in contribution.items():
        if key not in out or value not in LEVEL:
            raise ValueError("unclosed requirement contribution")
        if LEVEL[value] > LEVEL[out[key]]:
            out[key] = value
    return out


def _validate_policy_input(inp):
    if not isinstance(inp, dict) or set(inp) != POLICY_INPUT_FIELDS:
        return "POLICY_UNRESOLVED"
    if inp["policy_id"] != POLICY_ID or inp["policy_epoch"] != POLICY_EPOCH:
        return "POLICY_UNRESOLVED"
    if not _identifier(inp["artifact_id"]):
        return "POLICY_UNRESOLVED"
    if not _content_identity("ReferenceUseRecord", inp["reference_use_id"]):
        return "POLICY_UNRESOLVED"
    if not _identifier(inp["release_scope_ref"]):
        return "POLICY_UNRESOLVED"
    if inp["origin_class"] not in ORIGIN_CLASSES:
        return "POLICY_UNRESOLVED"
    if inp["reference_class"] not in REFERENCE_CLASSES:
        return "POLICY_UNRESOLVED"
    if inp["release_scope_class"] not in RELEASE_SCOPES:
        return "POLICY_UNRESOLVED"
    if inp["media_kind"] not in MEDIA_KINDS:
        return "POLICY_UNRESOLVED"
    for boolean_field in ("references_exist", "incorporation_or_release_intent", "legal_interpretation_material"):
        if type(inp[boolean_field]) is not bool:
            return "POLICY_UNRESOLVED"
    triggers = inp["material_trigger_set"]
    if not isinstance(triggers, list):
        return "POLICY_UNRESOLVED"
    if any(type(t) is not str for t in triggers):
        return "POLICY_UNRESOLVED"
    if any(t not in MATERIAL_TRIGGERS for t in triggers):
        return "POLICY_UNRESOLVED"
    if len(triggers) != len(set(triggers)):
        return "POLICY_UNRESOLVED"
    return None


def _rule_contributions(inp):
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
    baseline = {}
    if references: baseline["known_reference_comparison"] = "REQUIRED"
    if build_or_stronger or incorporation or origin != "PROJECT_NATIVE": baseline["exact_identity"] = "REQUIRED"
    if distribution and references and media_applicable:
        baseline["normalized_identity"] = "REQUIRED"; baseline["near_duplicate_checks"] = "REQUIRED"
    if distribution and ref not in {"FACTUAL_OR_FUNCTIONAL", "GENERAL_CONCEPTUAL"}: baseline["judgment_review"] = "REQUIRED"
    if legal_material or triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"}: baseline["qualified_legal_review"] = "REQUIRED"
    rules.append(("R0_TOTAL_BASELINE", baseline))
    if scope == RELEASE_SCOPES["INTERNAL_RESEARCH"]:
        internal = {}
        if references or origin != "PROJECT_NATIVE": internal["exact_identity"] = "REQUIRED"
        if references: internal["known_reference_comparison"] = "REQUIRED"
        rules.append(("R1_INTERNAL_RESEARCH", internal))
    if build_or_stronger and origin == "PROJECT_NATIVE" and ref in {"FACTUAL_OR_FUNCTIONAL", "GENERAL_CONCEPTUAL", "STYLE_OR_CREATOR_NAMED"}:
        native = {"exact_identity": "REQUIRED"}
        if references:
            native["known_reference_comparison"] = "REQUIRED"; native["judgment_review"] = "REQUIRED"
        if media_applicable and references:
            native["normalized_identity"] = "REQUIRED"; native["near_duplicate_checks"] = "REQUIRED"
        rules.append(("R2_NATIVE_BUILD", native))
    if distribution and ref == "STYLE_OR_CREATOR_NAMED":
        style = {k: "REQUIRED" for k in ("exact_identity", "normalized_identity", "known_reference_comparison", "near_duplicate_checks", "targeted_external_search", "judgment_review")}
        if legal_material or triggers: style["qualified_legal_review"] = "REQUIRED"
        rules.append(("R3_STYLE_OR_CREATOR", style))
    if distribution and ref in {"EXPRESSION_SPECIFIC", "DIRECT_ASSET_OR_CODE"}:
        expression = {k: "REQUIRED" for k in ("exact_identity", "normalized_identity", "known_reference_comparison", "judgment_review")}
        if media_applicable: expression["near_duplicate_checks"] = "REQUIRED"
        if references: expression["targeted_external_search"] = "REQUIRED"
        if legal_material or triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"}: expression["qualified_legal_review"] = "REQUIRED"
        rules.append(("R4_EXPRESSION_OR_DIRECT", expression))
    if distribution and ref == "MARK_LIKENESS_PERSONA":
        mark = {k: "REQUIRED" for k in ("exact_identity", "known_reference_comparison", "targeted_external_search", "judgment_review")}
        if media_applicable:
            mark["normalized_identity"] = "REQUIRED"; mark["near_duplicate_checks"] = "REQUIRED"
        if legal_material or scope >= RELEASE_SCOPES["RELEASE"]: mark["qualified_legal_review"] = "REQUIRED"
        rules.append(("R5_MARK_LIKENESS_PERSONA", mark))
    if ref == "CONFIDENTIAL_PRIVATE_RESTRICTED":
        rules.append(("R6_RESTRICTED_REFERENCE", {"exact_identity": "REQUIRED", "known_reference_comparison": "REQUIRED" if references else "NOT_APPLICABLE", "judgment_review": "REQUIRED", "qualified_legal_review": "REQUIRED"}))
    if triggers:
        triggered = {"known_reference_comparison": "REQUIRED", "judgment_review": "REQUIRED"}
        if media_applicable: triggered["near_duplicate_checks"] = "REQUIRED"
        if references: triggered["targeted_external_search"] = "REQUIRED"
        if triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"} or legal_material: triggered["qualified_legal_review"] = "REQUIRED"
        rules.append(("R7_MATERIAL_TRIGGER", triggered))
    return rules


def compile_policy(inp, *, reverse_rules=False):
    invalid = _validate_policy_input(inp)
    if invalid:
        return {"status": "UNKNOWN", "reason": invalid}
    req = _required()
    rules = _rule_contributions(inp)
    if reverse_rules: rules = list(reversed(rules))
    trace = []
    for rule_id, contribution in rules:
        req = _join(req, contribution); trace.append(rule_id)
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
    try:
        requirement_set_id = content_id("OriginalityEvidenceRequirementSet", payload)
    except (KeyError, TypeError, ValueError):
        return {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    return {"status": "COMPILED", "requirements": req, "compiler_trace": sorted(trace), "requirement_set_id": requirement_set_id, "payload": payload}


def derive_state(requirements, evidence_states, material_triggers, explicit_restriction=False):
    required = [k for k, v in requirements.items() if v == "REQUIRED"]
    independent_risk = set(material_triggers) & {"MATERIAL_SIMILARITY_SIGNAL", "CREDIBLE_COMPLAINT", "CONFLICTING_SOURCE"}
    if independent_risk: return {"state": "QUARANTINED", "reason": "MATERIAL_RISK"}
    stale = [k for k in required if evidence_states.get(k) == "STALE"]
    if stale: return {"state": "UNKNOWN", "reason": "STALE_EVIDENCE", "evidence_kinds": sorted(stale)}
    bad = [k for k in required if evidence_states.get(k) in {None, "MISSING", "CONFLICTING", "OUT_OF_SCOPE", "NOT_RUN", "INCONCLUSIVE"}]
    if bad: return {"state": "UNKNOWN", "reason": "REQUIRED_EVIDENCE_UNSATISFIED", "evidence_kinds": sorted(bad)}
    if explicit_restriction: return {"state": "RESTRICTED", "reason": "EXPLICIT_SCOPE_RESTRICTION"}
    if all(evidence_states.get(k) == "SATISFIED" for k in required): return {"state": "CLEAR", "reason": "ALL_REQUIRED_EVIDENCE_SATISFIED"}
    return {"state": "UNKNOWN", "reason": "UNCLASSIFIED_EVIDENCE_STATE"}


def assert_equal(a, b, label):
    if a != b: raise AssertionError(f"{label}: {a!r} != {b!r}")


def assert_not_equal(a, b, label):
    if a == b: raise AssertionError(f"{label}: values unexpectedly equal")


def assert_raises(fn, label):
    try:
        fn()
    except (KeyError, TypeError, ValueError):
        return
    raise AssertionError(f"{label}: expected closed validation error")


def base_evidence():
    return [
        {"kind": "ProviderTermsRecord", "record_id": "terms:1", "content_sha256": "a" * 64, "immutable_ref": "git-blob:" + "1" * 40},
        {"kind": "RightsProvenanceRecord", "record_id": "prov:1", "content_sha256": "b" * 64, "immutable_ref": "git-blob:" + "2" * 40},
    ]


def base_reference_use():
    return {
        "candidate_artifact_id": "artifact:demo-001",
        "source_reference_ids": ["source:b", "source:a"],
        "reference_class": "STYLE_OR_CREATOR_NAMED",
        "declared_purpose": "visual mood reference only",
        "allowed_reuse": ["reuse:facts", "reuse:high-level-composition"],
        "prohibited_reuse": ["reuse:direct-copy", "reuse:asset-reuse"],
        "license_or_permission_refs": ["license:1"],
        "provider_terms_refs": ["terms:1"],
        "provider_input_admission_ref": "admission:1",
        "release_scope_ref": "scope:release",
        "provenance_record_ref": "prov:1",
        "originality_risk_policy_ref": f"{POLICY_ID}@{POLICY_EPOCH}",
        "source_evidence_root": source_evidence_root(base_evidence()),
    }


def base_policy_input():
    rur_id = content_id("ReferenceUseRecord", base_reference_use())
    return {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "artifact_id": "artifact:demo-001",
        "reference_use_id": rur_id,
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


def example_authority_records(compiled, rur_id):
    review_payload = {
        "candidate_artifact_id": "artifact:demo-001",
        "reference_use_id": rur_id,
        "policy_epoch_ref": f"{POLICY_ID}@{POLICY_EPOCH}",
        "compiled_requirement_set_ref": compiled["requirement_set_id"],
        "reference_corpus_ref": ["source:a", "source:b"],
        "exact_duplicate_checks": ["check:1"],
        "near_duplicate_checks": ["check:2"],
        "targeted_external_search_refs": ["search:1"],
        "judgment_panel_ref": "panel:1",
        "qualified_legal_review_ref": "state:not-applicable",
        "material_signals": [],
        "blind_spots": [],
        "result": "NO_MATERIAL_SIGNAL_FOUND",
        "legal_conclusion": "NONE",
    }
    review_id = content_id("OriginalityReviewRecord", review_payload)
    assessment = {
        "artifact_id": "artifact:demo-001",
        "release_scope_ref": "scope:release",
        "provenance_record_ref": "prov:1",
        "reference_use_id": rur_id,
        "policy_epoch_ref": f"{POLICY_ID}@{POLICY_EPOCH}",
        "compiled_requirement_set_ref": compiled["requirement_set_id"],
        "provider_terms_refs": ["terms:1"],
        "license_or_permission_refs": ["license:1"],
        "originality_review_ref": review_id,
        "unresolved_triggers": [],
        "derived_rights_or_terms_state": "CLEAR",
        "reason_code": "ALL_REQUIRED_EVIDENCE_SATISFIED",
        "derivation_trace": ["compile", "validate", "derive"],
        "freshness_refs": ["fresh:1"],
        "reopen_conditions": ["terms-change"],
    }
    return {"OriginalityReviewRecord": review_payload, "ReleaseRightsAssessment": assessment, "OriginalityEvidenceRequirementSet": compiled["payload"]}


def run():
    results = []
    overlap = base_policy_input()
    compiled = compile_policy(overlap)
    assert_equal(compiled["status"], "COMPILED", "overlap compiles")
    for key in ("exact_identity", "normalized_identity", "known_reference_comparison", "near_duplicate_checks", "targeted_external_search", "judgment_review"):
        assert_equal(compiled["requirements"][key], "REQUIRED", f"overlap strongest {key}")
    assert_equal(compile_policy(overlap, reverse_rules=True)["requirements"], compiled["requirements"], "rule-order independence")
    results.append("T01_OVERLAP_JOIN_ORDER_INDEPENDENT")

    general = base_policy_input(); general["reference_class"] = "GENERAL_CONCEPTUAL"; general["release_scope_class"] = "BUILD_CANDIDATE"
    c_general = compile_policy(general)
    assert_equal(set(c_general["requirements"].values()) <= {"REQUIRED", "NOT_APPLICABLE"}, True, "no CONDITIONAL terminal values")
    results.append("T02_NO_CONDITIONAL_TERMINAL")

    unknown = base_policy_input(); unknown["media_kind"] = "UNDECLARED"
    assert_equal(compile_policy(unknown), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, "unknown fail closed")
    results.append("T03_UNKNOWN_FAILS_CLOSED")

    rur = base_reference_use(); rid = content_id("ReferenceUseRecord", rur)
    assert_equal(validate_claimed_id("ReferenceUseRecord", rur, rid), True, "id recomputes")
    reordered = copy.deepcopy(rur); reordered["source_reference_ids"] = list(reversed(reordered["source_reference_ids"])); reordered["allowed_reuse"] = list(reversed(reordered["allowed_reuse"]))
    assert_equal(content_id("ReferenceUseRecord", reordered), rid, "set ordering canonical")
    results.append("T04_SET_ORDER_CANONICAL")

    for field, mutated_value in (("declared_purpose", "direct implementation reference"), ("release_scope_ref", "scope:internal"), ("provider_terms_refs", ["terms:2"]), ("license_or_permission_refs", ["license:2"]), ("source_reference_ids", ["source:a", "source:c"])):
        mutated = copy.deepcopy(rur); mutated[field] = mutated_value
        assert_not_equal(content_id("ReferenceUseRecord", mutated), rid, f"bound mutation {field}")
    results.append("T05_BOUND_FIELDS_CHANGE_REFERENCE_USE_ID")

    evidence = base_evidence(); root = source_evidence_root(evidence)
    assert_equal(source_evidence_root(list(reversed(evidence))), root, "root set ordering")
    evidence_mut = copy.deepcopy(evidence); evidence_mut[0]["content_sha256"] = "c" * 64
    assert_not_equal(source_evidence_root(evidence_mut), root, "root content mutation")
    results.append("T06_SOURCE_ROOT_RECOMPUTABLE")

    all_required = {k: "REQUIRED" for k in REQUIREMENT_KINDS}; all_sat = {k: "SATISFIED" for k in REQUIREMENT_KINDS}
    for kind in REQUIREMENT_KINDS:
        states = dict(all_sat); states[kind] = "STALE"
        state = derive_state(all_required, states, [])
        assert_equal(state["state"], "UNKNOWN", f"stale state {kind}"); assert_equal(state["reason"], "STALE_EVIDENCE", f"stale reason {kind}")
        assert_equal(derive_state(all_required, states, ["CREDIBLE_COMPLAINT"])["state"], "QUARANTINED", f"risk precedence {kind}")
    results.append("T07_ALL_REQUIRED_KINDS_HAVE_STALE_PRECEDENCE")

    assert_equal(derive_state(all_required, all_sat, [])["state"], "CLEAR", "all satisfied clear")
    results.append("T08_CLEAR_REQUIRES_ALL_REQUIRED_SATISFIED")

    for record_type, payload in example_authority_records(compiled, rid).items():
        cid = content_id(record_type, payload)
        assert_equal(validate_claimed_id(record_type, payload, cid), True, f"{record_type} recompute")
        mutation = copy.deepcopy(payload); first_key = next(k for k in mutation if k != "material_triggers")
        if first_key in {"policy_epoch"}: mutation[first_key] = 999
        elif isinstance(mutation[first_key], str): mutation[first_key] = "mutated:value"
        else: mutation[first_key] = "mutated-value"
        try:
            mutated_id = content_id(record_type, mutation)
            assert_not_equal(mutated_id, cid, f"{record_type} mutation changes id")
        except ValueError:
            pass
    results.append("T09_ALL_AUTHORITY_RECORD_IDS_RECOMPUTABLE")

    malformed_values = [None, False, 7, [], "", "bad identifier with spaces"]
    for field in ("artifact_id", "reference_use_id", "release_scope_ref"):
        missing = base_policy_input(); del missing[field]
        assert_equal(compile_policy(missing), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, f"missing {field}")
        for value in malformed_values:
            bad = base_policy_input(); bad[field] = value
            assert_equal(compile_policy(bad), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, f"malformed {field}={value!r}")
    unknown_field = base_policy_input(); unknown_field["undeclared"] = "x"
    assert_equal(compile_policy(unknown_field), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, "unknown compiler field")
    results.append("T10_COMPILER_BINDINGS_TOTAL_FAIL_CLOSED")

    for triggers in ([{}], [["bad"]], [None], [False], [1], ["UNKNOWN"], ["CREDIBLE_COMPLAINT", "CREDIBLE_COMPLAINT"]):
        bad = base_policy_input(); bad["material_trigger_set"] = triggers
        assert_equal(compile_policy(bad), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, f"malformed triggers {triggers!r}")
    results.append("T11_TRIGGER_MEMBERS_TOTAL_FAIL_CLOSED")

    for mutation_label, mutate in (
        ("empty", lambda _: {}),
        ("missing_provider_terms", lambda p: {k: v for k, v in p.items() if k != "provider_terms_refs"}),
        ("unknown_field", lambda p: {**p, "undeclared": "x"}),
        ("wrong_candidate_type", lambda p: {**p, "candidate_artifact_id": 7}),
    ):
        bad_payload = mutate(copy.deepcopy(rur))
        valid, _ = validate_record_schema("ReferenceUseRecord", bad_payload)
        assert_equal(valid, False, f"ReferenceUseRecord {mutation_label} schema reject")
        assert_equal(validate_claimed_id("ReferenceUseRecord", bad_payload, rid), False, f"ReferenceUseRecord {mutation_label} claimed id reject")
        assert_raises(lambda bp=bad_payload: content_id("ReferenceUseRecord", bp), f"ReferenceUseRecord {mutation_label} content id")
    results.append("T12_AUTHORITY_RECORD_SCHEMA_PRECEDES_ID")

    incomplete_entry = [{"kind": "ProviderTermsRecord"}]
    assert_raises(lambda: source_evidence_root(incomplete_entry), "incomplete source entry")
    wrong_hash = copy.deepcopy(evidence); wrong_hash[0]["content_sha256"] = "not-a-sha"
    assert_raises(lambda: source_evidence_root(wrong_hash), "malformed source hash")
    duplicate = copy.deepcopy(evidence) + [copy.deepcopy(evidence[0])]
    assert_raises(lambda: source_evidence_root(duplicate), "duplicate record id")
    conflicting = copy.deepcopy(evidence); conflicting.append({**copy.deepcopy(evidence[0]), "content_sha256": "d" * 64})
    assert_raises(lambda: source_evidence_root(conflicting), "conflicting duplicate record id")
    results.append("T13_SOURCE_ROOT_SCHEMA_AND_ID_UNIQUENESS")

    records = {"ReferenceUseRecord": rur, **example_authority_records(compiled, rid), "SourceEvidenceRoot": {"evidence_entries": evidence}}
    for record_type, payload in records.items():
        key = next(iter(payload))
        missing = {k: v for k, v in payload.items() if k != key}
        assert_equal(validate_record_schema(record_type, missing)[0], False, f"{record_type} missing field")
        unknown = {**copy.deepcopy(payload), "undeclared": "x"}
        assert_equal(validate_record_schema(record_type, unknown)[0], False, f"{record_type} unknown field")
    results.append("T14_ALL_AUTHORITY_SCHEMAS_CLOSED")

    digest_payload = canonical_json({"tests": results}).encode("utf-8")
    summary = {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "serialization_version": SERIALIZATION_VERSION,
        "schema_version": SCHEMA_VERSION,
        "tests_passed": len(results),
        "tests": results,
        "result_digest_sha256": hashlib.sha256(digest_payload).hexdigest(),
    }
    print(canonical_json(summary))
    return summary


if __name__ == "__main__":
    run()
