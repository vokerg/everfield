#!/usr/bin/env python3
"""Deterministic rights-policy fixture for W2-REM-RIGHTS-04.

Planning evidence only. Standard-library only; not production or legal logic.
Supersedes the executable fixture from Issue #129 only for the bounded
PG-REM3-RIGHTS-M01 fail-closed scalar/domain remediation.
"""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import re

POLICY_ID = "ORIGINALITY-RISK-v2"
POLICY_EPOCH = 2
POLICY_REF = f"{POLICY_ID}@{POLICY_EPOCH}"
SERIALIZATION_VERSION = "EVERFIELD-RIGHTS-CANONICAL-JSON-v1"
SCHEMA_VERSION = "EVERFIELD-RIGHTS-AUTHORITY-SCHEMA-v1"
MALFORMED_MATRIX_VERSION = "EVERFIELD-RIGHTS-MALFORMED-SCALAR-MATRIX-v1"
NOT_APPLICABLE = "NOT_APPLICABLE"

ORIGIN_CLASSES = {
    "PROJECT_NATIVE", "GENERATED_PROVIDER", "EXTERNAL_REFERENCE",
    "EXTERNAL_ASSET", "THIRD_PARTY_OUTPUT", "LICENSED_MATERIAL",
    "PUBLIC_DOMAIN_CLAIM",
}
REFERENCE_CLASSES = {
    "FACTUAL_OR_FUNCTIONAL", "GENERAL_CONCEPTUAL", "STYLE_OR_CREATOR_NAMED",
    "EXPRESSION_SPECIFIC", "DIRECT_ASSET_OR_CODE", "MARK_LIKENESS_PERSONA",
    "CONFIDENTIAL_PRIVATE_RESTRICTED", "PUBLIC_DOMAIN_CLAIM",
}
RELEASE_SCOPES = {
    "INTERNAL_RESEARCH": 0, "BUILD_CANDIDATE": 1,
    "DISTRIBUTION_CANDIDATE": 2, "RELEASE": 3,
}
MEDIA_KINDS = {"NONE", "TEXT", "IMAGE", "AUDIO", "VIDEO", "CODE", "MIXED"}
MATERIAL_TRIGGERS = {
    "MATERIAL_SIMILARITY_SIGNAL", "CREDIBLE_COMPLAINT", "CONFLICTING_SOURCE",
    "TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY",
}
REQUIREMENT_KINDS = (
    "exact_identity", "normalized_identity", "known_reference_comparison",
    "near_duplicate_checks", "targeted_external_search", "judgment_review",
    "qualified_legal_review",
)
LEVEL = {"NOT_APPLICABLE": 0, "REQUIRED": 1}
RULE_IDS = {f"R{i}_{name}" for i, name in (
    (0, "TOTAL_BASELINE"), (1, "INTERNAL_RESEARCH"), (2, "NATIVE_BUILD"),
    (3, "STYLE_OR_CREATOR"), (4, "EXPRESSION_OR_DIRECT"),
    (5, "MARK_LIKENESS_PERSONA"), (6, "RESTRICTED_REFERENCE"),
    (7, "MATERIAL_TRIGGER"),
)}

POLICY_INPUT_FIELDS = {
    "policy_id", "policy_epoch", "artifact_id", "reference_use_id",
    "release_scope_ref", "origin_class", "reference_class",
    "release_scope_class", "material_trigger_set", "media_kind",
    "references_exist", "incorporation_or_release_intent",
    "legal_interpretation_material",
}
SET_FIELDS = {
    "ReferenceUseRecord": {
        "source_reference_ids", "allowed_reuse", "prohibited_reuse",
        "license_or_permission_refs", "provider_terms_refs",
    },
    "OriginalityReviewRecord": {
        "reference_corpus_ref", "exact_duplicate_checks", "near_duplicate_checks",
        "targeted_external_search_refs", "material_signals", "blind_spots",
    },
    "ReleaseRightsAssessment": {
        "provider_terms_refs", "license_or_permission_refs", "unresolved_triggers",
        "freshness_refs", "reopen_conditions",
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
        "candidate_artifact_id", "source_reference_ids", "reference_class",
        "declared_purpose", "allowed_reuse", "prohibited_reuse",
        "license_or_permission_refs", "provider_terms_refs",
        "provider_input_admission_ref", "release_scope_ref",
        "provenance_record_ref", "originality_risk_policy_ref",
        "source_evidence_root",
    },
    "OriginalityReviewRecord": {
        "candidate_artifact_id", "reference_use_id", "policy_epoch_ref",
        "compiled_requirement_set_ref", "reference_corpus_ref",
        "exact_duplicate_checks", "near_duplicate_checks",
        "targeted_external_search_refs", "judgment_panel_ref",
        "qualified_legal_review_ref", "material_signals", "blind_spots",
        "result", "legal_conclusion",
    },
    "ReleaseRightsAssessment": {
        "artifact_id", "release_scope_ref", "provenance_record_ref",
        "reference_use_id", "policy_epoch_ref", "compiled_requirement_set_ref",
        "provider_terms_refs", "license_or_permission_refs",
        "originality_review_ref", "unresolved_triggers",
        "derived_rights_or_terms_state", "reason_code", "derivation_trace",
        "freshness_refs", "reopen_conditions",
    },
    "OriginalityEvidenceRequirementSet": {
        "policy_id", "policy_epoch", "artifact_id", "reference_use_id",
        "release_scope_ref", "requirements", "material_triggers", "compiler_trace",
    },
    "SourceEvidenceRoot": {"evidence_entries"},
}
SOURCE_EVIDENCE_KINDS = {
    "ArtifactIdentity", "RightsProvenanceRecord", "SourceReferenceIdentity",
    "LicenseOrPermissionRecord", "ProviderTermsRecord",
    "ProviderInputAdmissionRecord", "OriginalityRiskPolicy",
}
REVIEW_RESULTS = {
    "NO_MATERIAL_SIGNAL_FOUND", "MATERIAL_SIGNAL", "NEAR_DUPLICATE",
    "EXACT_DUPLICATE", "INCONCLUSIVE", "NOT_RUN",
}
RIGHTS_STATES = {"CLEAR", "RESTRICTED", "QUARANTINED", "UNKNOWN", NOT_APPLICABLE}
RIGHTS_REASON_CODES = {
    "MATERIAL_RISK", "STALE_EVIDENCE", "REQUIRED_EVIDENCE_UNSATISFIED",
    "EXPLICIT_SCOPE_RESTRICTION", "ALL_REQUIRED_EVIDENCE_SATISFIED",
    "UNCLASSIFIED_EVIDENCE_STATE", "POLICY_UNRESOLVED", NOT_APPLICABLE,
}
EVIDENCE_STATES = {
    "SATISFIED", "STALE", "MISSING", "CONFLICTING", "OUT_OF_SCOPE",
    "NOT_RUN", "INCONCLUSIVE",
}

IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,63}:[A-Za-z0-9][A-Za-z0-9._:@/+-]{0,255}$")
CONTENT_ID_RE = {
    kind: re.compile(rf"^{re.escape(prefix)}:[0-9a-f]{{64}}$")
    for kind, prefix in ID_PREFIX.items()
}
ANY_CONTENT_ID_RE = re.compile(r"^(?:rur|orr|rra|oers|ser)-sha256:[0-9a-f]{64}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
IMMUTABLE_REF_RE = re.compile(
    r"^(?:git-blob:[0-9a-f]{40}|git-commit:[0-9a-f]{40}|"
    r"repo:[^\s@]+@[0-9a-f]{40}|protected:[A-Za-z0-9._:/+-]+)$"
)

def _is_string(value):
    return type(value) is str

def _closed_member(value, domain):
    """Membership for externally supplied scalar values; never hashes non-strings."""
    return _is_string(value) and value in domain

def _closed_mapping_member(value, mapping):
    """Mapping membership/index precondition for externally supplied scalar values."""
    return _is_string(value) and value in mapping

def _nonempty_string(value):
    return _is_string(value) and bool(value) and value == value.strip() and "\x00" not in value

def _identifier(value):
    return _nonempty_string(value) and IDENT_RE.fullmatch(value) is not None

def _content_identity(record_type, value):
    return (
        _closed_mapping_member(record_type, CONTENT_ID_RE)
        and _nonempty_string(value)
        and CONTENT_ID_RE[record_type].fullmatch(value) is not None
    )

def _immutable_ref(value):
    return _nonempty_string(value) and IMMUTABLE_REF_RE.fullmatch(value) is not None

def _authority_identity(value):
    if not _nonempty_string(value):
        return False
    return (
        _identifier(value)
        or ANY_CONTENT_ID_RE.fullmatch(value) is not None
        or _immutable_ref(value)
        or value == POLICY_REF
    )

def _authority_identity_or_na(value):
    return value == NOT_APPLICABLE or _authority_identity(value)

def _string_list(value, *, allow_empty=True, validator=_nonempty_string, unique=True):
    if not isinstance(value, list) or (not allow_empty and not value):
        return False
    if any(not validator(item) for item in value):
        return False
    return not unique or len(value) == len(set(value))

def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def _normalize(value, *, record_type=None, field_name=None):
    if isinstance(value, dict):
        if any(not _nonempty_string(key) for key in value):
            raise ValueError("object keys must be nonempty strings")
        return {
            key: _normalize(item, record_type=record_type, field_name=key)
            for key, item in sorted(value.items())
        }
    if isinstance(value, list):
        normalized = [_normalize(item, record_type=record_type, field_name=field_name) for item in value]
        if _closed_mapping_member(record_type, SET_FIELDS) and field_name in SET_FIELDS[record_type]:
            encoded = [canonical_json(item) for item in normalized]
            if len(encoded) != len(set(encoded)):
                raise ValueError(f"duplicate set member: {record_type}.{field_name}")
            normalized = [item for _, item in sorted(zip(encoded, normalized), key=lambda pair: pair[0])]
        return normalized
    if value is None or isinstance(value, (str, int, bool)):
        return value
    raise TypeError(f"unsupported canonical type: {type(value)!r}")

def _validate_evidence_entry(entry):
    required = {"kind", "record_id", "content_sha256", "immutable_ref"}
    if not isinstance(entry, dict) or set(entry) != required:
        return False
    if not _closed_member(entry["kind"], SOURCE_EVIDENCE_KINDS):
        return False
    if not _authority_identity(entry["record_id"]):
        return False
    if not _nonempty_string(entry["content_sha256"]) or SHA256_RE.fullmatch(entry["content_sha256"]) is None:
        return False
    if not _immutable_ref(entry["immutable_ref"]):
        return False
    return True

def validate_record_schema(record_type, payload):
    """Return (valid, reason) under the closed authority schema v1, never raising."""
    if not _closed_mapping_member(record_type, RECORD_FIELDS):
        return False, "UNSUPPORTED_RECORD_TYPE"
    if not isinstance(payload, dict):
        return False, "PAYLOAD_NOT_OBJECT"
    if any(not _nonempty_string(key) for key in payload):
        return False, "NONSTRING_OR_EMPTY_FIELD_NAME"
    required = RECORD_FIELDS[record_type]
    if set(payload) != required:
        missing = sorted(required - set(payload))
        unknown = sorted(set(payload) - required)
        return False, f"FIELD_SET_MISMATCH:missing={missing}:unknown={unknown}"

    if record_type == "ReferenceUseRecord":
        if not _identifier(payload["candidate_artifact_id"]): return False, "candidate_artifact_id"
        if not _string_list(payload["source_reference_ids"], validator=_authority_identity): return False, "source_reference_ids"
        if not _closed_member(payload["reference_class"], REFERENCE_CLASSES): return False, "reference_class"
        if not _nonempty_string(payload["declared_purpose"]): return False, "declared_purpose"
        for field in ("allowed_reuse", "prohibited_reuse"):
            if not _string_list(payload[field]): return False, field
        for field in ("license_or_permission_refs", "provider_terms_refs"):
            if not _string_list(payload[field], validator=_authority_identity): return False, field
        if not _authority_identity_or_na(payload["provider_input_admission_ref"]): return False, "provider_input_admission_ref"
        if not _identifier(payload["release_scope_ref"]): return False, "release_scope_ref"
        if not _authority_identity(payload["provenance_record_ref"]): return False, "provenance_record_ref"
        if not (_is_string(payload["originality_risk_policy_ref"]) and payload["originality_risk_policy_ref"] == POLICY_REF): return False, "originality_risk_policy_ref"
        if not _content_identity("SourceEvidenceRoot", payload["source_evidence_root"]): return False, "source_evidence_root"

    elif record_type == "OriginalityReviewRecord":
        if not _identifier(payload["candidate_artifact_id"]): return False, "candidate_artifact_id"
        if not _content_identity("ReferenceUseRecord", payload["reference_use_id"]): return False, "reference_use_id"
        if not (_is_string(payload["policy_epoch_ref"]) and payload["policy_epoch_ref"] == POLICY_REF): return False, "policy_epoch_ref"
        if not _content_identity("OriginalityEvidenceRequirementSet", payload["compiled_requirement_set_ref"]): return False, "compiled_requirement_set_ref"
        for field in ("reference_corpus_ref", "exact_duplicate_checks", "near_duplicate_checks", "targeted_external_search_refs"):
            if not _string_list(payload[field], validator=_authority_identity): return False, field
        if not _authority_identity_or_na(payload["judgment_panel_ref"]): return False, "judgment_panel_ref"
        if not _authority_identity_or_na(payload["qualified_legal_review_ref"]): return False, "qualified_legal_review_ref"
        for field in ("material_signals", "blind_spots"):
            if not _string_list(payload[field]): return False, field
        if not _closed_member(payload["result"], REVIEW_RESULTS): return False, "result"
        if not (_is_string(payload["legal_conclusion"]) and payload["legal_conclusion"] == "NONE"): return False, "legal_conclusion"

    elif record_type == "ReleaseRightsAssessment":
        if not _identifier(payload["artifact_id"]): return False, "artifact_id"
        if not _identifier(payload["release_scope_ref"]): return False, "release_scope_ref"
        if not _authority_identity(payload["provenance_record_ref"]): return False, "provenance_record_ref"
        if not _content_identity("ReferenceUseRecord", payload["reference_use_id"]): return False, "reference_use_id"
        if not (_is_string(payload["policy_epoch_ref"]) and payload["policy_epoch_ref"] == POLICY_REF): return False, "policy_epoch_ref"
        if not _content_identity("OriginalityEvidenceRequirementSet", payload["compiled_requirement_set_ref"]): return False, "compiled_requirement_set_ref"
        for field in ("provider_terms_refs", "license_or_permission_refs"):
            if not _string_list(payload[field], validator=_authority_identity): return False, field
        review_ref = payload["originality_review_ref"]
        if review_ref != NOT_APPLICABLE and not _content_identity("OriginalityReviewRecord", review_ref): return False, "originality_review_ref"
        triggers = payload["unresolved_triggers"]
        if not isinstance(triggers, list): return False, "unresolved_triggers"
        if any(not _closed_member(item, MATERIAL_TRIGGERS) for item in triggers): return False, "unresolved_triggers"
        if len(triggers) != len(set(triggers)): return False, "unresolved_triggers"
        if not _closed_member(payload["derived_rights_or_terms_state"], RIGHTS_STATES): return False, "derived_rights_or_terms_state"
        if not _closed_member(payload["reason_code"], RIGHTS_REASON_CODES): return False, "reason_code"
        if not _string_list(payload["derivation_trace"], allow_empty=False, unique=False): return False, "derivation_trace"
        if not _string_list(payload["freshness_refs"], validator=_authority_identity): return False, "freshness_refs"
        if not _string_list(payload["reopen_conditions"]): return False, "reopen_conditions"

    elif record_type == "OriginalityEvidenceRequirementSet":
        if not (_is_string(payload["policy_id"]) and payload["policy_id"] == POLICY_ID): return False, "policy_id"
        if type(payload["policy_epoch"]) is not int or type(payload["policy_epoch"]) is bool or payload["policy_epoch"] != POLICY_EPOCH: return False, "policy_epoch"
        if not _identifier(payload["artifact_id"]): return False, "artifact_id"
        if not _content_identity("ReferenceUseRecord", payload["reference_use_id"]): return False, "reference_use_id"
        if not _identifier(payload["release_scope_ref"]): return False, "release_scope_ref"
        requirements = payload["requirements"]
        if not isinstance(requirements, dict) or set(requirements) != set(REQUIREMENT_KINDS): return False, "requirements"
        if any(not _closed_mapping_member(value, LEVEL) for value in requirements.values()): return False, "requirements"
        triggers = payload["material_triggers"]
        if not isinstance(triggers, list) or any(not _closed_member(item, MATERIAL_TRIGGERS) for item in triggers): return False, "material_triggers"
        if triggers != sorted(set(triggers)): return False, "material_triggers"
        trace = payload["compiler_trace"]
        if not isinstance(trace, list) or not trace or any(not _closed_member(item, RULE_IDS) for item in trace): return False, "compiler_trace"
        if trace != sorted(set(trace)) or "R0_TOTAL_BASELINE" not in trace: return False, "compiler_trace"

    elif record_type == "SourceEvidenceRoot":
        entries = payload["evidence_entries"]
        if not isinstance(entries, list) or not entries: return False, "evidence_entries"
        if any(not _validate_evidence_entry(entry) for entry in entries): return False, "evidence_entry"
        record_ids = [entry["record_id"] for entry in entries]
        if len(record_ids) != len(set(record_ids)): return False, "duplicate_or_conflicting_record_id"
        encoded = [canonical_json(_normalize(entry)) for entry in entries]
        if len(encoded) != len(set(encoded)): return False, "duplicate_evidence_entry"

    return True, "VALID"

def canonical_payload(record_type, payload):
    valid, reason = validate_record_schema(record_type, payload)
    if not valid:
        raise ValueError(f"schema invalid for {record_type!r}: {reason}")
    normalized = _normalize(copy.deepcopy(payload), record_type=record_type)
    return canonical_json({
        "serialization_version": SERIALIZATION_VERSION,
        "record_type": record_type,
        "payload": normalized,
    }).encode("utf-8")

def content_id(record_type, payload):
    if not _closed_mapping_member(record_type, ID_PREFIX):
        raise ValueError(f"unsupported record type: {record_type!r}")
    domain = f"everfield:rights:{record_type}:v1\0".encode("utf-8")
    digest = hashlib.sha256(domain + canonical_payload(record_type, payload)).hexdigest()
    return f"{ID_PREFIX[record_type]}:{digest}"

def validate_claimed_id(record_type, payload, claimed_id):
    try:
        return _content_identity(record_type, claimed_id) and claimed_id == content_id(record_type, payload)
    except (KeyError, TypeError, ValueError):
        return False

def source_evidence_root(evidence_entries):
    return content_id("SourceEvidenceRoot", {"evidence_entries": evidence_entries})

def _required():
    return {kind: "NOT_APPLICABLE" for kind in REQUIREMENT_KINDS}

def _join(requirements, contribution):
    out = dict(requirements)
    for key, value in contribution.items():
        if not _closed_mapping_member(key, out) or not _closed_mapping_member(value, LEVEL):
            raise ValueError("unclosed requirement contribution")
        if LEVEL[value] > LEVEL[out[key]]:
            out[key] = value
    return out

def _validate_policy_input(inp):
    if not isinstance(inp, dict) or any(not _nonempty_string(k) for k in inp) or set(inp) != POLICY_INPUT_FIELDS:
        return "POLICY_UNRESOLVED"
    if not (_is_string(inp["policy_id"]) and inp["policy_id"] == POLICY_ID):
        return "POLICY_UNRESOLVED"
    if type(inp["policy_epoch"]) is not int or type(inp["policy_epoch"]) is bool or inp["policy_epoch"] != POLICY_EPOCH:
        return "POLICY_UNRESOLVED"
    if not _identifier(inp["artifact_id"]): return "POLICY_UNRESOLVED"
    if not _content_identity("ReferenceUseRecord", inp["reference_use_id"]): return "POLICY_UNRESOLVED"
    if not _identifier(inp["release_scope_ref"]): return "POLICY_UNRESOLVED"
    if not _closed_member(inp["origin_class"], ORIGIN_CLASSES): return "POLICY_UNRESOLVED"
    if not _closed_member(inp["reference_class"], REFERENCE_CLASSES): return "POLICY_UNRESOLVED"
    if not _closed_mapping_member(inp["release_scope_class"], RELEASE_SCOPES): return "POLICY_UNRESOLVED"
    if not _closed_member(inp["media_kind"], MEDIA_KINDS): return "POLICY_UNRESOLVED"
    for field in ("references_exist", "incorporation_or_release_intent", "legal_interpretation_material"):
        if type(inp[field]) is not bool: return "POLICY_UNRESOLVED"
    triggers = inp["material_trigger_set"]
    if not isinstance(triggers, list): return "POLICY_UNRESOLVED"
    if any(not _closed_member(item, MATERIAL_TRIGGERS) for item in triggers): return "POLICY_UNRESOLVED"
    if len(triggers) != len(set(triggers)): return "POLICY_UNRESOLVED"
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
        baseline["normalized_identity"] = "REQUIRED"
        baseline["near_duplicate_checks"] = "REQUIRED"
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
            native["known_reference_comparison"] = "REQUIRED"
            native["judgment_review"] = "REQUIRED"
        if media_applicable and references:
            native["normalized_identity"] = "REQUIRED"
            native["near_duplicate_checks"] = "REQUIRED"
        rules.append(("R2_NATIVE_BUILD", native))

    if distribution and ref == "STYLE_OR_CREATOR_NAMED":
        style = {kind: "REQUIRED" for kind in (
            "exact_identity", "normalized_identity", "known_reference_comparison",
            "near_duplicate_checks", "targeted_external_search", "judgment_review",
        )}
        if legal_material or triggers: style["qualified_legal_review"] = "REQUIRED"
        rules.append(("R3_STYLE_OR_CREATOR", style))

    if distribution and ref in {"EXPRESSION_SPECIFIC", "DIRECT_ASSET_OR_CODE"}:
        expression = {kind: "REQUIRED" for kind in (
            "exact_identity", "normalized_identity", "known_reference_comparison", "judgment_review",
        )}
        if media_applicable: expression["near_duplicate_checks"] = "REQUIRED"
        if references: expression["targeted_external_search"] = "REQUIRED"
        if legal_material or triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"}:
            expression["qualified_legal_review"] = "REQUIRED"
        rules.append(("R4_EXPRESSION_OR_DIRECT", expression))

    if distribution and ref == "MARK_LIKENESS_PERSONA":
        mark = {kind: "REQUIRED" for kind in (
            "exact_identity", "known_reference_comparison", "targeted_external_search", "judgment_review",
        )}
        if media_applicable:
            mark["normalized_identity"] = "REQUIRED"
            mark["near_duplicate_checks"] = "REQUIRED"
        if legal_material or scope >= RELEASE_SCOPES["RELEASE"]: mark["qualified_legal_review"] = "REQUIRED"
        rules.append(("R5_MARK_LIKENESS_PERSONA", mark))

    if ref == "CONFIDENTIAL_PRIVATE_RESTRICTED":
        rules.append(("R6_RESTRICTED_REFERENCE", {
            "exact_identity": "REQUIRED",
            "known_reference_comparison": "REQUIRED" if references else "NOT_APPLICABLE",
            "judgment_review": "REQUIRED",
            "qualified_legal_review": "REQUIRED",
        }))

    if triggers:
        triggered = {"known_reference_comparison": "REQUIRED", "judgment_review": "REQUIRED"}
        if media_applicable: triggered["near_duplicate_checks"] = "REQUIRED"
        if references: triggered["targeted_external_search"] = "REQUIRED"
        if triggers & {"TERMS_AMBIGUITY", "PERMISSION_AMBIGUITY", "SCOPE_AMBIGUITY"} or legal_material:
            triggered["qualified_legal_review"] = "REQUIRED"
        rules.append(("R7_MATERIAL_TRIGGER", triggered))
    return rules

def _compiled_requirements(inp, *, reverse_rules=False):
    requirements = _required()
    rules = _rule_contributions(inp)
    if reverse_rules:
        rules = list(reversed(rules))
    trace = []
    for rule_id, contribution in rules:
        requirements = _join(requirements, contribution)
        trace.append(rule_id)
    return requirements, sorted(trace)

def compile_policy(inp, *, reverse_rules=False):
    if _validate_policy_input(inp):
        return {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    requirements, trace = _compiled_requirements(inp, reverse_rules=reverse_rules)
    payload = {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "artifact_id": inp["artifact_id"],
        "reference_use_id": inp["reference_use_id"],
        "release_scope_ref": inp["release_scope_ref"],
        "requirements": requirements,
        "material_triggers": sorted(inp["material_trigger_set"]),
        "compiler_trace": trace,
    }
    try:
        requirement_set_id = content_id("OriginalityEvidenceRequirementSet", payload)
    except (KeyError, TypeError, ValueError):
        return {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    return {
        "status": "COMPILED", "requirements": requirements,
        "compiler_trace": trace, "requirement_set_id": requirement_set_id,
        "payload": payload,
    }

def derive_state(requirements, evidence_states, material_triggers, explicit_restriction=False):
    if not isinstance(requirements, dict) or set(requirements) != set(REQUIREMENT_KINDS):
        return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    if any(not _closed_mapping_member(value, LEVEL) for value in requirements.values()):
        return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    if not isinstance(evidence_states, dict):
        return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    if not isinstance(material_triggers, list) or any(not _closed_member(item, MATERIAL_TRIGGERS) for item in material_triggers):
        return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    if any(
        _closed_mapping_member(kind, evidence_states)
        and not _closed_member(evidence_states[kind], EVIDENCE_STATES)
        for kind in REQUIREMENT_KINDS
    ):
        return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}
    if type(explicit_restriction) is not bool:
        return {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}

    required = [kind for kind, value in requirements.items() if value == "REQUIRED"]
    independent_risk = set(material_triggers) & {"MATERIAL_SIMILARITY_SIGNAL", "CREDIBLE_COMPLAINT", "CONFLICTING_SOURCE"}
    if independent_risk: return {"state": "QUARANTINED", "reason": "MATERIAL_RISK"}
    stale = [kind for kind in required if evidence_states.get(kind) == "STALE"]
    if stale: return {"state": "UNKNOWN", "reason": "STALE_EVIDENCE", "evidence_kinds": sorted(stale)}
    bad = [kind for kind in required if evidence_states.get(kind) in {None, "MISSING", "CONFLICTING", "OUT_OF_SCOPE", "NOT_RUN", "INCONCLUSIVE"}]
    if bad: return {"state": "UNKNOWN", "reason": "REQUIRED_EVIDENCE_UNSATISFIED", "evidence_kinds": sorted(bad)}
    if explicit_restriction: return {"state": "RESTRICTED", "reason": "EXPLICIT_SCOPE_RESTRICTION"}
    if all(evidence_states.get(kind) == "SATISFIED" for kind in required): return {"state": "CLEAR", "reason": "ALL_REQUIRED_EVIDENCE_SATISFIED"}
    return {"state": "UNKNOWN", "reason": "UNCLASSIFIED_EVIDENCE_STATE"}

def assert_equal(a, b, label):
    if a != b:
        raise AssertionError(f"{label}: {a!r} != {b!r}")

def assert_not_equal(a, b, label):
    if a == b:
        raise AssertionError(f"{label}: values unexpectedly equal")

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
        "allowed_reuse": ["facts", "high-level composition"],
        "prohibited_reuse": ["direct copy", "asset reuse"],
        "license_or_permission_refs": ["license:1"],
        "provider_terms_refs": ["terms:1"],
        "provider_input_admission_ref": NOT_APPLICABLE,
        "release_scope_ref": "scope:release",
        "provenance_record_ref": "prov:1",
        "originality_risk_policy_ref": POLICY_REF,
        "source_evidence_root": source_evidence_root(base_evidence()),
    }

def base_policy_input():
    return {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "artifact_id": "artifact:demo-001",
        "reference_use_id": content_id("ReferenceUseRecord", base_reference_use()),
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
    review = {
        "candidate_artifact_id": "artifact:demo-001",
        "reference_use_id": rur_id,
        "policy_epoch_ref": POLICY_REF,
        "compiled_requirement_set_ref": compiled["requirement_set_id"],
        "reference_corpus_ref": ["source:a", "source:b"],
        "exact_duplicate_checks": ["check:1"],
        "near_duplicate_checks": ["check:2"],
        "targeted_external_search_refs": ["search:1"],
        "judgment_panel_ref": "panel:1",
        "qualified_legal_review_ref": NOT_APPLICABLE,
        "material_signals": [],
        "blind_spots": [],
        "result": "NO_MATERIAL_SIGNAL_FOUND",
        "legal_conclusion": "NONE",
    }
    review_id = content_id("OriginalityReviewRecord", review)
    assessment = {
        "artifact_id": "artifact:demo-001",
        "release_scope_ref": "scope:release",
        "provenance_record_ref": "prov:1",
        "reference_use_id": rur_id,
        "policy_epoch_ref": POLICY_REF,
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
    return {
        "OriginalityReviewRecord": review,
        "ReleaseRightsAssessment": assessment,
        "OriginalityEvidenceRequirementSet": compiled["payload"],
    }

MALFORMED_VALUES = [
    None, False, True, 0, 7, -1, 1.5, "", "UNDECLARED", [], {}, ["x"], {"x": 1},
]

def _record_templates():
    rur = base_reference_use()
    rid = content_id("ReferenceUseRecord", rur)
    compiled = compile_policy(base_policy_input())
    records = {"ReferenceUseRecord": rur, **example_authority_records(compiled, rid)}
    records["SourceEvidenceRoot"] = {"evidence_entries": base_evidence()}
    return compiled, records

def run_malformed_scalar_matrix():
    """Generated matrix for every closed authority scalar/domain field in this fixture."""
    compiled, records = _record_templates()
    cases = []
    uncaught = []

    def check(label, fn, expected):
        for value in MALFORMED_VALUES:
            try:
                got = fn(copy.deepcopy(value))
                ok = expected(got)
            except Exception as exc:
                uncaught.append({"label": label, "value": repr(value), "exception": f"{type(exc).__name__}:{exc}"})
                ok = False
            cases.append({"field": label, "value": repr(value), "accepted": bool(ok)})
            if not ok:
                raise AssertionError(f"malformed scalar not fail-closed: {label}={value!r}")

    for field in ("origin_class", "reference_class", "release_scope_class", "media_kind", "policy_id", "policy_epoch"):
        def compiler_case(value, field=field):
            bad = base_policy_input()
            bad[field] = value
            return compile_policy(bad)
        check(
            f"PolicyInput.{field}",
            compiler_case,
            lambda got: got == {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"},
        )

    for field in ("references_exist", "incorporation_or_release_intent", "legal_interpretation_material"):
        safe_values = [v for v in MALFORMED_VALUES if type(v) is not bool]
        old = list(MALFORMED_VALUES)
        try:
            globals()["MALFORMED_VALUES"] = safe_values
            def compiler_bool_case(value, field=field):
                bad = base_policy_input()
                bad[field] = value
                return compile_policy(bad)
            check(
                f"PolicyInput.{field}",
                compiler_bool_case,
                lambda got: got == {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"},
            )
        finally:
            globals()["MALFORMED_VALUES"] = old

    scalar_record_fields = [
        ("ReferenceUseRecord", "reference_class"),
        ("ReferenceUseRecord", "originality_risk_policy_ref"),
        ("OriginalityReviewRecord", "policy_epoch_ref"),
        ("OriginalityReviewRecord", "result"),
        ("OriginalityReviewRecord", "legal_conclusion"),
        ("ReleaseRightsAssessment", "policy_epoch_ref"),
        ("ReleaseRightsAssessment", "derived_rights_or_terms_state"),
        ("ReleaseRightsAssessment", "reason_code"),
        ("OriginalityEvidenceRequirementSet", "policy_id"),
        ("OriginalityEvidenceRequirementSet", "policy_epoch"),
    ]
    for record_type, field in scalar_record_fields:
        template = records[record_type]
        def record_case(value, record_type=record_type, field=field, template=template):
            bad = copy.deepcopy(template)
            bad[field] = value
            return validate_record_schema(record_type, bad)
        check(
            f"{record_type}.{field}",
            record_case,
            lambda got: got[0] is False,
        )

    for requirement_kind in REQUIREMENT_KINDS:
        template = records["OriginalityEvidenceRequirementSet"]
        def requirement_case(value, requirement_kind=requirement_kind, template=template):
            bad = copy.deepcopy(template)
            bad["requirements"][requirement_kind] = value
            return validate_record_schema("OriginalityEvidenceRequirementSet", bad)
        check(
            f"OriginalityEvidenceRequirementSet.requirements.{requirement_kind}",
            requirement_case,
            lambda got: got[0] is False,
        )

    root_template = records["SourceEvidenceRoot"]
    def source_kind_case(value):
        bad = copy.deepcopy(root_template)
        bad["evidence_entries"][0]["kind"] = value
        return validate_record_schema("SourceEvidenceRoot", bad)
    check(
        "SourceEvidenceRoot.evidence_entries[].kind",
        source_kind_case,
        lambda got: got[0] is False,
    )

    def record_type_case(value):
        return validate_record_schema(value, {})
    check("validate_record_schema.record_type", record_type_case, lambda got: got[0] is False)

    for requirement_kind in REQUIREMENT_KINDS:
        def evidence_state_case(value, requirement_kind=requirement_kind):
            requirements = {kind: "REQUIRED" for kind in REQUIREMENT_KINDS}
            states = {kind: "SATISFIED" for kind in REQUIREMENT_KINDS}
            states[requirement_kind] = value
            return derive_state(requirements, states, [])
        check(
            f"derive_state.evidence_states.{requirement_kind}",
            evidence_state_case,
            lambda got: got == {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"},
        )

    def trigger_case(value):
        requirements = {kind: "REQUIRED" for kind in REQUIREMENT_KINDS}
        states = {kind: "SATISFIED" for kind in REQUIREMENT_KINDS}
        return derive_state(requirements, states, [value])
    check(
        "derive_state.material_triggers[]",
        trigger_case,
        lambda got: got == {"state": "UNKNOWN", "reason": "POLICY_UNRESOLVED"},
    )

    matrix = {
        "version": MALFORMED_MATRIX_VERSION,
        "case_count": len(cases),
        "uncaught_exception_count": len(uncaught),
        "uncaught": uncaught,
    }
    matrix["digest_sha256"] = hashlib.sha256(canonical_json(matrix).encode()).hexdigest()
    return matrix

def run_finite_domain_audit():
    """Reproduce Issue #129's 802,816 valid-domain order-independence audit."""
    trigger_values = sorted(MATERIAL_TRIGGERS)
    trigger_sets = [
        [trigger_values[i] for i in range(len(trigger_values)) if mask & (1 << i)]
        for mask in range(1 << len(trigger_values))
    ]
    checked = 0
    order_mismatches = 0
    nonclosed_outputs = 0
    digest = hashlib.sha256()
    audit_base = base_policy_input()
    for origin, reference, release, triggers, media, refs, incorporation, legal in itertools.product(
        sorted(ORIGIN_CLASSES),
        sorted(REFERENCE_CLASSES),
        sorted(RELEASE_SCOPES),
        trigger_sets,
        sorted(MEDIA_KINDS),
        (False, True),
        (False, True),
        (False, True),
    ):
        inp = dict(audit_base)
        inp.update({
            "origin_class": origin,
            "reference_class": reference,
            "release_scope_class": release,
            "material_trigger_set": triggers,
            "media_kind": media,
            "references_exist": refs,
            "incorporation_or_release_intent": incorporation,
            "legal_interpretation_material": legal,
        })
        if _validate_policy_input(inp) is not None:
            raise AssertionError("valid audit tuple rejected")
        forward, _ = _compiled_requirements(inp, reverse_rules=False)
        reverse, _ = _compiled_requirements(inp, reverse_rules=True)
        if forward != reverse:
            order_mismatches += 1
        if set(forward) != set(REQUIREMENT_KINDS) or any(not _closed_mapping_member(v, LEVEL) for v in forward.values()):
            nonclosed_outputs += 1
        digest.update(canonical_json({
            "origin": origin, "reference": reference, "release": release,
            "triggers": sorted(triggers), "media": media, "refs": refs,
            "incorporation": incorporation, "legal": legal,
            "requirements": forward,
        }).encode())
        checked += 1
    return {
        "valid_domain_combinations_checked": checked,
        "reverse_rule_order_requirement_mismatches": order_mismatches,
        "nonclosed_requirement_outputs": nonclosed_outputs,
        "audit_digest_sha256": digest.hexdigest(),
    }

def run():
    results = []

    overlap = base_policy_input()
    compiled = compile_policy(overlap)
    assert_equal(compiled["status"], "COMPILED", "overlap compiles")
    for key in ("exact_identity", "normalized_identity", "known_reference_comparison", "near_duplicate_checks", "targeted_external_search", "judgment_review"):
        assert_equal(compiled["requirements"][key], "REQUIRED", f"overlap strongest {key}")
    assert_equal(compile_policy(overlap, reverse_rules=True)["requirements"], compiled["requirements"], "rule-order independence")
    results.append("T01_OVERLAP_JOIN_ORDER_INDEPENDENT")

    general = base_policy_input()
    general["reference_class"] = "GENERAL_CONCEPTUAL"
    general["release_scope_class"] = "BUILD_CANDIDATE"
    c_general = compile_policy(general)
    assert_equal(set(c_general["requirements"].values()) <= {"REQUIRED", "NOT_APPLICABLE"}, True, "no CONDITIONAL terminal values")
    results.append("T02_NO_CONDITIONAL_TERMINAL")

    unknown = base_policy_input()
    unknown["media_kind"] = "UNDECLARED"
    assert_equal(compile_policy(unknown), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, "unknown fail closed")
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

    evidence = base_evidence()
    root = source_evidence_root(evidence)
    assert_equal(source_evidence_root(list(reversed(evidence))), root, "root set ordering")
    evidence_mut = copy.deepcopy(evidence)
    evidence_mut[0]["content_sha256"] = "c" * 64
    assert_not_equal(source_evidence_root(evidence_mut), root, "root content mutation")
    results.append("T06_SOURCE_ROOT_RECOMPUTABLE")

    all_required = {kind: "REQUIRED" for kind in REQUIREMENT_KINDS}
    all_sat = {kind: "SATISFIED" for kind in REQUIREMENT_KINDS}
    for kind in REQUIREMENT_KINDS:
        states = dict(all_sat)
        states[kind] = "STALE"
        state = derive_state(all_required, states, [])
        assert_equal(state["state"], "UNKNOWN", f"stale state {kind}")
        assert_equal(state["reason"], "STALE_EVIDENCE", f"stale reason {kind}")
        assert_equal(derive_state(all_required, states, ["CREDIBLE_COMPLAINT"])["state"], "QUARANTINED", f"risk precedence {kind}")
    results.append("T07_ALL_REQUIRED_KINDS_HAVE_STALE_PRECEDENCE")

    assert_equal(derive_state(all_required, all_sat, [])["state"], "CLEAR", "all satisfied clear")
    results.append("T08_CLEAR_REQUIRES_ALL_REQUIRED_SATISFIED")

    for record_type, payload in example_authority_records(compiled, rid).items():
        cid = content_id(record_type, payload)
        assert_equal(validate_claimed_id(record_type, payload, cid), True, f"{record_type} recompute")
        mutation = copy.deepcopy(payload)
        first_key = next(iter(mutation))
        mutation[first_key] = "mutated:value" if isinstance(mutation[first_key], str) else "mutated-value"
        try:
            assert_not_equal(content_id(record_type, mutation), cid, f"{record_type} mutation changes id")
        except ValueError:
            pass
    results.append("T09_ALL_AUTHORITY_RECORD_IDS_RECOMPUTABLE")

    malformed_values = [None, False, 7, [], {}, "", "bad identifier with spaces"]
    for field in ("artifact_id", "reference_use_id", "release_scope_ref"):
        missing = base_policy_input()
        del missing[field]
        assert_equal(compile_policy(missing), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, f"missing {field}")
        for value in malformed_values:
            bad = base_policy_input()
            bad[field] = value
            assert_equal(compile_policy(bad), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, f"malformed {field}={value!r}")
    unknown_field = base_policy_input()
    unknown_field["undeclared"] = "x"
    assert_equal(compile_policy(unknown_field), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, "unknown compiler field")
    results.append("T10_COMPILER_BINDINGS_TOTAL_FAIL_CLOSED")

    for triggers in ([{}], [["bad"]], [None], [False], [1], ["UNKNOWN"], ["CREDIBLE_COMPLAINT", "CREDIBLE_COMPLAINT"]):
        bad = base_policy_input()
        bad["material_trigger_set"] = triggers
        assert_equal(compile_policy(bad), {"status": "UNKNOWN", "reason": "POLICY_UNRESOLVED"}, f"malformed triggers {triggers!r}")
    results.append("T11_TRIGGER_MEMBERS_TOTAL_FAIL_CLOSED")

    for label, mutate in (
        ("empty", lambda _: {}),
        ("missing_provider_terms", lambda p: {k: v for k, v in p.items() if k != "provider_terms_refs"}),
        ("unknown_field", lambda p: {**p, "undeclared": "x"}),
        ("wrong_candidate_type", lambda p: {**p, "candidate_artifact_id": 7}),
    ):
        bad_payload = mutate(copy.deepcopy(rur))
        assert_equal(validate_record_schema("ReferenceUseRecord", bad_payload)[0], False, f"ReferenceUseRecord {label} schema reject")
        assert_equal(validate_claimed_id("ReferenceUseRecord", bad_payload, rid), False, f"ReferenceUseRecord {label} claimed id reject")
        assert_raises(lambda payload=bad_payload: content_id("ReferenceUseRecord", payload), f"ReferenceUseRecord {label} content id")
    sentinel = copy.deepcopy(rur)
    sentinel["provider_input_admission_ref"] = NOT_APPLICABLE
    assert_equal(validate_record_schema("ReferenceUseRecord", sentinel)[0], True, "inherited NOT_APPLICABLE sentinel")
    results.append("T12_AUTHORITY_RECORD_SCHEMA_PRECEDES_ID")

    assert_raises(lambda: source_evidence_root([{"kind": "ProviderTermsRecord"}]), "incomplete source entry")
    wrong_hash = copy.deepcopy(evidence)
    wrong_hash[0]["content_sha256"] = "not-a-sha"
    assert_raises(lambda: source_evidence_root(wrong_hash), "malformed source hash")
    wrong_kind = copy.deepcopy(evidence)
    wrong_kind[0]["kind"] = "UnversionedNewAuthorityKind"
    assert_raises(lambda: source_evidence_root(wrong_kind), "unknown source kind")
    wrong_id = copy.deepcopy(evidence)
    wrong_id[0]["record_id"] = "opaque bare id with spaces"
    assert_raises(lambda: source_evidence_root(wrong_id), "malformed source record id")
    duplicate = copy.deepcopy(evidence) + [copy.deepcopy(evidence[0])]
    assert_raises(lambda: source_evidence_root(duplicate), "duplicate record id")
    conflicting = copy.deepcopy(evidence)
    conflicting.append({**copy.deepcopy(evidence[0]), "content_sha256": "d" * 64})
    assert_raises(lambda: source_evidence_root(conflicting), "conflicting duplicate record id")
    results.append("T13_SOURCE_ROOT_SCHEMA_AND_ID_UNIQUENESS")

    records = {
        "ReferenceUseRecord": rur,
        **example_authority_records(compiled, rid),
        "SourceEvidenceRoot": {"evidence_entries": evidence},
    }
    for record_type, payload in records.items():
        key = next(iter(payload))
        missing = {k: v for k, v in payload.items() if k != key}
        assert_equal(validate_record_schema(record_type, missing)[0], False, f"{record_type} missing field")
        unknown = {**copy.deepcopy(payload), "undeclared": "x"}
        assert_equal(validate_record_schema(record_type, unknown)[0], False, f"{record_type} unknown field")
    review_template = example_authority_records(compiled, rid)["OriginalityReviewRecord"]
    for result in REVIEW_RESULTS:
        candidate = copy.deepcopy(review_template)
        candidate["result"] = result
        assert_equal(validate_record_schema("OriginalityReviewRecord", candidate)[0], True, f"inherited review result {result}")
    assessment_template = example_authority_records(compiled, rid)["ReleaseRightsAssessment"]
    na_assessment = copy.deepcopy(assessment_template)
    na_assessment["originality_review_ref"] = NOT_APPLICABLE
    na_assessment["derived_rights_or_terms_state"] = NOT_APPLICABLE
    na_assessment["reason_code"] = NOT_APPLICABLE
    assert_equal(validate_record_schema("ReleaseRightsAssessment", na_assessment)[0], True, "inherited assessment NOT_APPLICABLE")
    results.append("T14_ALL_AUTHORITY_SCHEMAS_CLOSED")

    matrix = run_malformed_scalar_matrix()
    assert_equal(matrix["uncaught_exception_count"], 0, "malformed scalar matrix has zero uncaught exceptions")
    results.append("T15_ALL_AUTHORITY_SCALARS_TOTAL_FAIL_CLOSED")

    audit = run_finite_domain_audit()
    assert_equal(audit["valid_domain_combinations_checked"], 802816, "finite domain cardinality")
    assert_equal(audit["reverse_rule_order_requirement_mismatches"], 0, "finite domain order independence")
    assert_equal(audit["nonclosed_requirement_outputs"], 0, "finite domain closed outputs")

    digest_payload = canonical_json({"tests": results, "matrix": matrix, "audit": audit}).encode("utf-8")
    summary = {
        "policy_id": POLICY_ID,
        "policy_epoch": POLICY_EPOCH,
        "serialization_version": SERIALIZATION_VERSION,
        "schema_version": SCHEMA_VERSION,
        "malformed_matrix_version": MALFORMED_MATRIX_VERSION,
        "tests_passed": len(results),
        "tests": results,
        "malformed_scalar_cases": matrix["case_count"],
        "uncaught_exception_count": matrix["uncaught_exception_count"],
        **audit,
        "result_digest_sha256": hashlib.sha256(digest_payload).hexdigest(),
    }
    print(canonical_json(summary))
    return summary

if __name__ == "__main__":
    run()
