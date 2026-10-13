#!/usr/bin/env python3
"""Conservative GitHub-state reconciliation for Everfield planning-v1.

Maintenance never grants planning authority. It only reconciles storage state,
materializes missing required transitions, and dispatches exact-main workflows
from a repository-owned allowlist.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, Iterable

API = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
REPO = os.environ.get("GITHUB_REPOSITORY", "vokerg/everfield")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
DRY_RUN = os.environ.get("FRONTIER_MAINTENANCE_DRY_RUN", "").lower() in {"1", "true", "yes"}
ROUTES_PATH = os.environ.get("FRONTIER_ROUTES_PATH", ".github/planning-frontier-routes.json")

TRUSTED_ASSOCIATIONS = {"OWNER", "MEMBER", "COLLABORATOR"}
OPERATIONAL_KINDS = {
    "CLAIM", "ORPHAN_PROBE", "RESUME_INTENT", "RESUME", "RECOVER", "PROGRESS",
    "STATUS", "REVIEW_STATUS", "VERIFICATION_STATUS", "INTEGRATION_STATUS",
    "BOOTSTRAP_RESUME", "BOOTSTRAP_VERIFICATION_STATUS",
}
OWNERSHIP_KINDS = {"CLAIM", "RESUME", "RECOVER", "BOOTSTRAP_RESUME"}
TERMINAL_STATES = {"DONE", "SUPERSEDED", "INVALIDATED"}
TERMINAL_KINDS = {"STATUS", "REVIEW_STATUS", "VERIFICATION_STATUS", "INTEGRATION_STATUS"}
SHA40_RE = re.compile(r"^[0-9a-fA-F]{40}$")
RFC3339_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})$"
)
FACTORY_TRANSITION_RE = re.compile(r"\[FACTORY-TRANSITION-(\d+)\]")
DISPATCH_MARKER_VERSION = "1"
DISPATCH_MARKER_STATES = {"ACCEPTED", "OBSERVED"}
RATE_LIMIT_MESSAGE_MARKERS = (
    "api rate limit exceeded",
    "secondary rate limit",
)

READINESS_ROUTING_DIRECTIVE_ISSUE = 84
READINESS_ROUTING_DIRECTIVE_COMMENT_ID = 5_889_817_307
READINESS_ROUTING_DIRECTIVE_MARKERS = (
    "If readiness remains false, route exact remaining blockers.",
    "A verified `BLOCKED` readiness state may not terminate with no successor",
)
READINESS_RECOVERY_NOTE_MARKER = "Owner-directed readiness recovery"
READINESS_ROUTING_HISTORICAL_SOURCE_ISSUE = 1038

SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS = 21_600
SCHEMA3_ORPHAN_PROBE_MATURITY_SECONDS = 600


class GitHubRateLimitExceeded(RuntimeError):
    """Retryable GitHub API rate exhaustion; grants no maintenance authority."""


def github_api_error(method: str, url: str, code: int, detail: str) -> RuntimeError:
    message = detail
    try:
        parsed = json.loads(detail)
        if isinstance(parsed, dict):
            message = str(parsed.get("message") or detail)
    except json.JSONDecodeError:
        pass

    normalized = message.lower()
    if code in {403, 429} and any(marker in normalized for marker in RATE_LIMIT_MESSAGE_MARKERS):
        return GitHubRateLimitExceeded(
            f"GitHub API {method} {url} deferred by rate limit: {code} {detail}"
        )
    return RuntimeError(f"GitHub API {method} {url} failed: {code} {detail}")


@dataclass(frozen=True)
class OperationalRecord:
    issue_number: int
    comment_id: int
    created_at: str
    kind: str
    state: str | None
    route: str | None
    body: str
    declared_issue: int | None
    mission_id: str | None
    actor_session_id: str | None
    authority_mode: str | None
    ownership_generation_comment_id: int | None
    head_sha: str | None
    work_sha: str | None


def request(method: str, path: str, payload: Any | None = None) -> Any:
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN is required")
    url = path if path.startswith("http") else f"{API}{path}"
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "everfield-frontier-maintenance/3",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read()
            return None if not raw else json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise github_api_error(method, url, exc.code, detail) from exc


def paged(path: str) -> Iterable[dict[str, Any]]:
    sep = "&" if "?" in path else "?"
    page = 1
    while True:
        batch = request("GET", f"{path}{sep}per_page=100&page={page}")
        if not isinstance(batch, list):
            raise RuntimeError(f"expected list from {path}")
        yield from batch
        if len(batch) < 100:
            return
        page += 1


def yaml_scalar_identity(raw: str) -> str | None:
    """Decode at most one YAML scalar quoting layer; never erase quoted data.

    This is a fail-closed, intentionally small scalar subset for schema-3
    operations, not a whole-document YAML parser. JSON-compatible double
    escapes and YAML doubled-single-quote escaping are decoded exactly once.
    Unsupported YAML quoting/escape syntax has no authority.
    """
    value = raw.strip()
    if not value:
        return None
    if value.startswith("'"):
        if re.fullmatch(r"'(?:[^']|'')*'", value) is None:
            return None
        value = value[1:-1].replace("''", "'")
    elif value.startswith('"'):
        try:
            value = json.loads(value)
        except (ValueError, TypeError):
            return None
        if not isinstance(value, str):
            return None
    return value if value and value.lower() not in {"null", "none", "~"} else None


def _operational_yaml_subset_valid(body: str) -> bool:
    """Validate the *entire* operational YAML document before extracting authority.

    This is deliberately narrower than YAML: unsupported valid constructs fail
    closed, and no partial/lexically plausible invalid document is accepted.
    An inline scalar cannot own children; nested mappings and scalar sequences
    are accepted only with consistent indentation and unique simple keys.
    """
    def atom(raw: str) -> bool:
        value = _root_scalar_without_comment(raw).strip()
        if not value:
            return False
        if value.startswith(("[", "{")):
            if not (value.startswith("[") and value.endswith("]")):
                return False
            inner = value[1:-1].strip()
            if not inner:
                return True
            return all(atom(part) and not part.strip().startswith("[")
                       for part in inner.split(","))
        if value.startswith(("!", "&", "*", "|", ">", "?", "-", "%", "@", "{", "}")):
            return False
        if value.startswith('"'):
            try:
                return isinstance(json.loads(value), str)
            except (ValueError, TypeError):
                return False
        if value.startswith("'"):
            return re.fullmatch(r"'(?:[^']|'')*'", value) is not None
        if any(ch in value for ch in ("[", "]", "{", "}", "\t", "\r")):
            return False
        if re.search(r":[ \t]", value) or value.endswith(":"):
            return False
        return not value.startswith(("---", "...", "#"))

    # Each frame tracks a real mapping/sequence, its indent, and seen keys.
    stack: list[dict[str, Any]] = []
    pending_child = False
    previous_indent = -1
    have_document = False
    for line in body.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        have_document = True
        indent = len(line) - len(line.lstrip(" \t"))
        if "\t" in line[:indent]:
            return False
        entry = line[indent:].rstrip()
        if indent > previous_indent:
            if previous_indent >= 0 and not pending_child:
                return False
            is_sequence = entry.startswith("- ")
            stack.append({"indent": indent,
                          "kind": "sequence" if is_sequence else "mapping",
                          "keys": set()})
        else:
            while stack and indent < stack[-1]["indent"]:
                stack.pop()
            if not stack or indent != stack[-1]["indent"]:
                return False
        frame = stack[-1]
        if frame["kind"] == "sequence":
            if not entry.startswith("- ") or not atom(entry[2:]):
                return False
            pending_child = False
        else:
            match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*):(?:[ \t]+(.*))?", entry)
            if match is None or match.group(1) in frame["keys"]:
                return False
            frame["keys"].add(match.group(1))
            raw = match.group(2) or ""
            if raw and not raw.lstrip().startswith("#") and not atom(raw):
                return False
            pending_child = not raw or raw.lstrip().startswith("#")
        previous_indent = indent
    return have_document


def _root_mapping_fields(body: str) -> dict[str, str] | None:
    """Conservatively authenticate direct root fields of one YAML capsule.

    Nested extensions data, secondary examples, complex and escaped mapping
    keys, and duplicate root keys never create schema-3 authority.
    """
    fence = chr(96) * 3
    if body.startswith(fence + "yaml\n"):
        cut = body.find("\n" + fence, len(fence) + 5)
        if cut < 0:
            return None
        body = body[len(fence) + 5:cut]
    elif body.startswith(fence):
        return None
    if not _operational_yaml_subset_valid(body):
        return None
    result: dict[str, str] = {}
    for line in body.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if line[0] in " \t":
            # Only direct root keys grant authority. Indented scalar blocks,
            # nested maps, and lists are never root operational fields.
            continue
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*):[ \t]*(.*)", line)
        if match is None or match.group(1) in result:
            return None
        result[match.group(1)] = match.group(2)
    return result


def _root_scalar_without_comment(raw: str) -> str:
    """Exclude YAML inline comments, preserving hashes inside quotes."""
    quote: str | None = None
    i = 0
    while i < len(raw):
        ch = raw[i]
        if quote == "'":
            if ch == "'" and i + 1 < len(raw) and raw[i + 1] == "'":
                i += 2
                continue
            if ch == "'":
                quote = None
        elif quote == '"':
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                quote = None
        elif ch in {"'", '"'}:
            quote = ch
        elif ch == "#" and (i == 0 or raw[i - 1] in " \t"):
            return raw[:i].rstrip()
        i += 1
    return raw.rstrip()


def scalar(body: str, key: str) -> str | None:
    fields = _root_mapping_fields(body)
    if fields is None or key not in fields:
        return None
    return yaml_scalar_identity(_root_scalar_without_comment(fields[key]))


def integer_scalar(body: str, key: str) -> int | None:
    value = scalar(body, key)
    return int(value) if value and value.isdigit() else None


def list_scalar(body: str, key: str) -> list[str]:
    """Read only a unique, authenticated *root* operational list field.

    Root mapping identity is shared with scalar(), rather than searching
    arbitrarily indented extensions, prose, later fences or block scalars.
    Unsupported YAML structures have no authority: this is intentionally a
    small fail-closed subset, not a second YAML parser.
    """
    fields = _root_mapping_fields(body)
    if fields is None or key not in fields:
        return []

    fence = chr(96) * 3
    if body.startswith(fence + "yaml\n"):
        cut = body.find("\n" + fence, len(fence) + 5)
        if cut < 0:
            return []
        body = body[len(fence) + 5:cut]
    elif body.startswith(fence):
        return []

    lines = body.splitlines()
    key_re = re.compile(rf"^{re.escape(key)}:[ \t]*(.*)$")
    root_indices = [i for i, line in enumerate(lines) if key_re.fullmatch(line)]
    # _root_mapping_fields forbids duplicate/quoted/escaped/complex root keys.
    if len(root_indices) != 1:
        return []

    raw = _root_scalar_without_comment(fields[key]).strip()
    if raw.startswith("["):
        if not raw.endswith("]"):
            return []
        inner = raw[1:-1].strip()
        if not inner:
            return []
        parts = inner.split(",")
        values: list[str] = []
        for part in parts:
            item = _root_scalar_without_comment(part).strip()
            if not item or item.startswith(("[", "{", "!", "&", "*", "|", ">")):
                return []
            parsed = yaml_scalar_identity(item)
            if parsed is None:
                return []
            values.append(parsed)
        return values

    if raw:
        # A root YAML scalar (including a quoted string) is not a sequence.
        # Only authenticated flow [items] and indented "- item" sequences
        # may confer list-typed schema-3 operational authority.
        return []

    values: list[str] = []
    item_indent: int | None = None
    for line in lines[root_indices[0] + 1:]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" \t"))
        if indent == 0:
            break  # Next direct root key, never consume its nested values.
        if "\t" in line[:indent]:
            return []
        match = re.fullmatch(r" +-[ \t]+(.+?)[ \t]*", line)
        if match is None or (item_indent is not None and indent != item_indent):
            return []  # Nested maps or a second-level YAML sequence are invalid.
        if item_indent is None:
            item_indent = indent
        item = _root_scalar_without_comment(match.group(1)).strip()
        if not item or item.startswith(("[", "{", "!", "&", "*", "|", ">")):
            return []
        # Unquoted key/value sequences are mappings, not scalar list entries.
        if item[0] not in {"'", '"'} and re.search(r":[ \t]", item):
            return []
        parsed = yaml_scalar_identity(item)
        if parsed is None:
            return []
        values.append(parsed)
    return values

def immutable_ref(value: str) -> bool:
    """Validate the canonical immutable-ref forms maintenance can prove locally."""
    candidate = value.strip()
    if SHA40_RE.fullmatch(candidate):
        return True
    if candidate.isdigit() and int(candidate) > 0:
        return True
    if "@" in candidate:
        path, work_sha = candidate.rsplit("@", 1)
        return bool(path and SHA40_RE.fullmatch(work_sha))
    return False


def parse_github_server_time(value: str | None) -> datetime | None:
    """Parse authoritative GitHub RFC3339 `created_at`; malformed values fail closed."""
    if not value or RFC3339_RE.fullmatch(value) is None:
        return None
    normalized = value[:-1] + "+00:00" if value[-1] in {"Z", "z"} else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def github_verified_head_advance(
    owner: OperationalRecord, progress: OperationalRecord,
    previous_sha: str, advanced_sha: str,
) -> bool:
    """Require live authenticated task-branch movement and commit ancestry.

    Historical branch reflogs are unavailable through ordinary GitHub reads;
    if the exact advanced head is no longer the live branch tip, provenance is
    unknown and renewal is rejected rather than inferred from comment prose.
    """
    branch = scalar(owner.body, "branch")
    if (
        owner.declared_issue is None
        or branch != f"planning/issue-{owner.declared_issue}"
        or not SHA40_RE.fullmatch(previous_sha)
        or not SHA40_RE.fullmatch(advanced_sha)
    ):
        return False
    progressed_at = parse_github_server_time(progress.created_at)
    if progressed_at is None:
        return False
    try:
        encoded = urllib.parse.quote(branch, safe="/")
        ref = request("GET", f"/repos/{REPO}/git/ref/heads/{encoded}")
        if ref.get("object", {}).get("sha") != advanced_sha:
            return False
        comparison = request(
            "GET", f"/repos/{REPO}/compare/{previous_sha}...{advanced_sha}"
        )
        if (
            comparison.get("status") != "ahead"
            or comparison.get("ahead_by", 0) < 1
            or comparison.get("behind_by", 1) != 0
        ):
            return False
        actual_commit = request("GET", f"/repos/{REPO}/commits/{advanced_sha}")
        committed_at = parse_github_server_time(
            actual_commit.get("commit", {}).get("committer", {}).get("date")
        )
        return committed_at is not None and committed_at <= progressed_at
    except (RuntimeError, urllib.error.URLError, ValueError, TypeError, KeyError):
        return False


def github_verified_recovery_source_head(issue_number: int, source_head: str) -> bool:
    """Read-only proof a recovery source head belongs to the live task branch.

    GitHub exposes no historical reflog. A missing/moved/diverged tip fails
    closed; ancestry alone does not attest the historical time of the intent.
    """
    if type(issue_number) is not int or issue_number <= 0 or not isinstance(source_head, str) or not SHA40_RE.fullmatch(source_head):
        return False
    try:
        path = f"/repos/{REPO}/git/ref/heads/planning/issue-{issue_number}"
        ref = request("GET", path)
        tip = ref.get("object", {}).get("sha")
        if not isinstance(tip, str) or not SHA40_RE.fullmatch(tip):
            return False
        if tip == source_head:
            return True
        compare = request("GET", f"/repos/{REPO}/compare/{source_head}...{tip}")
        return bool(
            compare.get("status") == "ahead"
            and type(compare.get("ahead_by")) is int
            and compare["ahead_by"] >= 1
            and type(compare.get("behind_by")) is int
            and compare["behind_by"] == 0
        )
    except (RuntimeError, urllib.error.URLError, ValueError, TypeError, KeyError, AttributeError):
        return False


def github_verified_terminal_result_heads(
    issue_number: int, head_sha: str | None, work_sha: str | None,
) -> bool:
    """Authenticate BOTH owner terminal result SHAs to one live task tip.

    An exact current tip or its behind-free ancestor is acceptable. GitHub
    has no branch reflog or storage PATCH compare-and-swap; these live reads
    prove current ancestry only and fail closed on any uncertainty.
    """
    if (
        type(issue_number) is not int or issue_number <= 0
        or not isinstance(head_sha, str) or not SHA40_RE.fullmatch(head_sha)
        or not isinstance(work_sha, str) or not SHA40_RE.fullmatch(work_sha)
    ):
        return False
    try:
        ref = request(
            "GET", f"/repos/{REPO}/git/ref/heads/planning/issue-{issue_number}"
        )
        tip = ref.get("object", {}).get("sha")
        if not isinstance(tip, str) or not SHA40_RE.fullmatch(tip):
            return False

        def authenticated_ancestor(source_sha: str) -> bool:
            if source_sha == tip:
                return True
            comparison = request(
                "GET", f"/repos/{REPO}/compare/{source_sha}...{tip}"
            )
            return bool(
                comparison.get("status") == "ahead"
                and type(comparison.get("ahead_by")) is int
                and comparison["ahead_by"] >= 1
                and type(comparison.get("behind_by")) is int
                and comparison["behind_by"] == 0
            )

        return authenticated_ancestor(head_sha) and authenticated_ancestor(work_sha)
    except (RuntimeError, urllib.error.URLError, ValueError, TypeError, KeyError, AttributeError):
        return False


@dataclass(frozen=True)
class OwnershipLeaseState:
    anchor_comment_id: int
    anchor_created_at: datetime
    observed_head_sha: str
    consecutive_evidence: int


def schema3_ownership_lease_state(
    owner: OperationalRecord,
    records: Iterable[OperationalRecord],
    *,
    before_comment_id: int,
    head_verifier: Callable[[OperationalRecord, OperationalRecord, str, str], bool] | None = None,
) -> OwnershipLeaseState | None:
    """Reconstruct the canonical lease anchor through valid PROGRESS renewals.

    This helper intentionally evaluates only temporal/current-generation PROGRESS
    predicates that maintenance can prove from immutable operational comments.
    Ambiguous records have zero renewal effect.
    """
    if (
        owner.kind not in OWNERSHIP_KINDS
        or owner.state != "IN_PROGRESS"
        or not owner.actor_session_id
        or owner.comment_id >= before_comment_id
    ):
        return None
    anchor = parse_github_server_time(owner.created_at)
    observed_head = scalar(owner.body, "observed_head_sha")
    if anchor is None or observed_head is None or not SHA40_RE.fullmatch(observed_head):
        return None

    anchor_comment_id = owner.comment_id
    consecutive_evidence = 0
    for record in sorted(records, key=lambda item: item.comment_id):
        if not (owner.comment_id < record.comment_id < before_comment_id):
            continue
        if (
            record.kind != "PROGRESS"
            or record.state != "IN_PROGRESS"
            or record.declared_issue != owner.declared_issue
            or record.mission_id != owner.mission_id
            or record.actor_session_id != owner.actor_session_id
            or record.ownership_generation_comment_id != owner.comment_id
        ):
            continue
        progress_time = parse_github_server_time(record.created_at)
        progress_head = scalar(record.body, "observed_head_sha")
        progress_basis = scalar(record.body, "progress_basis")
        if (
            progress_time is None
            or progress_time < anchor
            or progress_head is None
            or not SHA40_RE.fullmatch(progress_head)
            or progress_time >= anchor + timedelta(seconds=SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS)
        ):
            continue

        if progress_basis == "HEAD_ADVANCE":
            if (
                progress_head == observed_head
                or head_verifier is None
                or not head_verifier(owner, record, observed_head, progress_head)
            ):
                continue
            observed_head = progress_head
            consecutive_evidence = 0
        elif progress_basis == "EVIDENCE":
            evidence_refs = list_scalar(record.body, "evidence_refs")
            if (
                progress_head != observed_head
                or not evidence_refs
                or not all(immutable_ref(ref) for ref in evidence_refs)
            ):
                continue
            if consecutive_evidence >= 3:
                continue
            consecutive_evidence += 1
        else:
            continue

        anchor = progress_time
        anchor_comment_id = record.comment_id

    return OwnershipLeaseState(
        anchor_comment_id=anchor_comment_id,
        anchor_created_at=anchor,
        observed_head_sha=observed_head,
        consecutive_evidence=consecutive_evidence,
    )


def schema3_owner_unexpired_at(
    owner: OperationalRecord,
    records: Iterable[OperationalRecord],
    at_record: OperationalRecord,
    *,
    head_verifier: Callable[[OperationalRecord, OperationalRecord, str, str], bool] | None = None,
) -> bool | None:
    """Return owner lease liveness at an operational record, or None on bad time."""
    at_time = parse_github_server_time(at_record.created_at)
    if at_time is None:
        return None
    state = schema3_ownership_lease_state(
        owner, records, before_comment_id=at_record.comment_id,
        head_verifier=head_verifier,
    )
    if state is None or at_time < state.anchor_created_at:
        return None
    return at_time < state.anchor_created_at + timedelta(
        seconds=SCHEMA3_TASK_OWNERSHIP_LEASE_SECONDS
    )


def schema3_orphan_probe_mature_at(
    probe: OperationalRecord,
    at_record: OperationalRecord,
) -> bool | None:
    """Return canonical 600-second ORPHAN maturity at a later record."""
    if probe.kind != "ORPHAN_PROBE" or probe.comment_id >= at_record.comment_id:
        return False
    probe_time = parse_github_server_time(probe.created_at)
    at_time = parse_github_server_time(at_record.created_at)
    if probe_time is None or at_time is None:
        return None
    return at_time >= probe_time + timedelta(
        seconds=SCHEMA3_ORPHAN_PROBE_MATURITY_SECONDS
    )


def immutable_comment(comment: dict[str, Any]) -> bool:
    created_at = comment.get("created_at")
    updated_at = comment.get("updated_at")
    return bool(created_at and updated_at and created_at == updated_at)


def trusted_readiness_routing_directive(comment: dict[str, Any]) -> bool:
    """Prove the exact owner directive that requires blocked-readiness routing."""
    if int(comment.get("id") or 0) != READINESS_ROUTING_DIRECTIVE_COMMENT_ID:
        return False
    if comment.get("author_association") not in TRUSTED_ASSOCIATIONS:
        return False
    if not immutable_comment(comment):
        return False
    if not (comment.get("issue_url") or "").endswith(
        f"/issues/{READINESS_ROUTING_DIRECTIVE_ISSUE}"
    ):
        return False
    body = comment.get("body") or ""
    return all(marker in body for marker in READINESS_ROUTING_DIRECTIVE_MARKERS)


def readiness_recovery_recorded(
    comments: Iterable[dict[str, Any]], terminal: OperationalRecord
) -> bool:
    """Recognize a later immutable owner recovery that already routes the dead end."""
    directive_id = str(READINESS_ROUTING_DIRECTIVE_COMMENT_ID)
    for comment in comments:
        if int(comment.get("id") or 0) <= terminal.comment_id:
            continue
        if comment.get("author_association") not in TRUSTED_ASSOCIATIONS:
            continue
        if not immutable_comment(comment):
            continue
        body = comment.get("body") or ""
        if (
            READINESS_RECOVERY_NOTE_MARKER in body
            and directive_id in body
            and "explicit live successors" in body
        ):
            return True
    return False


def parse_operational(issue_number: int, comment: dict[str, Any]) -> OperationalRecord | None:
    body = comment.get("body") or ""
    if comment.get("author_association") not in TRUSTED_ASSOCIATIONS:
        return None
    if not immutable_comment(comment):
        return None
    root = _root_mapping_fields(body)
    # The first direct key of a real schema-3 mapping is protocol, not an
    # extensions container whose child fields mimic a foreign owner record.
    if not root or next(iter(root)) != "protocol":
        return None
    if scalar(body, "protocol") != "planning-v1" or scalar(body, "schema") != "3":
        return None
    kind = scalar(body, "kind")
    if kind not in OPERATIONAL_KINDS:
        return None
    return OperationalRecord(
        issue_number=issue_number,
        comment_id=int(comment["id"]),
        created_at=comment.get("created_at") or "",
        kind=kind,
        state=scalar(body, "state"),
        route=scalar(body, "required_next_route"),
        body=body,
        declared_issue=integer_scalar(body, "issue"),
        mission_id=scalar(body, "mission_id"),
        actor_session_id=scalar(body, "actor_session_id"),
        authority_mode=scalar(body, "authority_mode"),
        ownership_generation_comment_id=integer_scalar(body, "ownership_generation_comment_id"),
        head_sha=scalar(body, "head_sha"),
        work_sha=scalar(body, "work_sha"),
    )


def operational_records_from_comments(issue_number: int, comments: Iterable[dict[str, Any]]) -> list[OperationalRecord]:
    return [record for comment in comments if (record := parse_operational(issue_number, comment))]


def latest_operational_from_comments(issue_number: int, comments: Iterable[dict[str, Any]]) -> OperationalRecord | None:
    records = operational_records_from_comments(issue_number, comments)
    return max(records, key=lambda item: item.comment_id) if records else None


def reconcilable_terminal_from_comments(issue_number: int, comments: Iterable[dict[str, Any]]) -> OperationalRecord | None:
    """Return a terminal only when its owner linkage is conservatively provable.

    This deliberately implements a strict subset of schema-3. Ambiguous or
    externally-retired records remain open for an agent to reconcile rather
    than being auto-closed by maintenance.
    """
    records = operational_records_from_comments(issue_number, comments)
    if not records:
        return None
    latest = max(records, key=lambda item: item.comment_id)
    if latest.kind not in TERMINAL_KINDS or latest.state not in TERMINAL_STATES:
        return None
    if latest.declared_issue != issue_number:
        return None
    if latest.authority_mode != "OWNER":
        return None
    if not latest.mission_id or not latest.actor_session_id:
        return None
    if latest.ownership_generation_comment_id is None:
        return None
    if not latest.head_sha or not latest.work_sha:
        return None
    if not SHA40_RE.fullmatch(latest.head_sha) or not SHA40_RE.fullmatch(latest.work_sha):
        return None

    owner = next(
        (record for record in records if record.comment_id == latest.ownership_generation_comment_id),
        None,
    )
    if owner is None or owner.comment_id >= latest.comment_id:
        return None
    if owner.kind not in OWNERSHIP_KINDS:
        return None
    if owner.declared_issue != issue_number:
        return None
    if owner.actor_session_id != latest.actor_session_id:
        return None
    if owner.mission_id != latest.mission_id:
        return None
    return latest



def closure_authorized_terminal_from_comments(
    issue_number: int, comments: Iterable[dict[str, Any]]
) -> OperationalRecord | None:
    """Conservatively authenticate an OWNER terminal before any storage PATCH.

    Unlike the legacy parser-only reconciliation helper, this consumer requires
    the first-winning, prefix-scoped ownership generation and its unexpired
    GitHub-server lease.  The v5 reconstruction verifies real GitHub branch,
    commit ancestry and commit timestamp for any HEAD_ADVANCE renewal.
    """
    items = list(comments)
    if not items:
        return None
    records = operational_records_from_comments(issue_number, items)
    ids = {record.comment_id for record in records}
    if len(ids) != len(records):
        return None
    for comment in items:
        if not isinstance(comment, dict) or not isinstance(comment.get("id"), int):
            return None
        body = comment.get("body")
        if not isinstance(body, str):
            return None
        # Do not silently skip a malformed, edited or untrusted operational
        # capsule (including one posted after an otherwise valid terminal).
        if (
            comment["id"] not in ids
            and re.search(
                r"(?m)^[ \t]*(?:protocol|schema|kind|ownership_generation_comment_id):",
                body,
            )
        ):
            return None
    if len({comment["id"] for comment in items}) != len(items):
        return None
    if any(parse_github_server_time(record.created_at) is None for record in records):
        return None

    terminal = reconcilable_terminal_from_comments(issue_number, items)
    if terminal is None:
        return None
    owner = next(
        (record for record in records
         if record.comment_id == terminal.ownership_generation_comment_id),
        None,
    )
    expected_branch = f"planning/issue-{issue_number}"
    if (
        owner is None
        or scalar(owner.body, "branch") != expected_branch
        or scalar(terminal.body, "branch") != expected_branch
    ):
        return None

    # Import at call-time to avoid a base/v5 module initialization cycle.
    from frontier_maintenance_v5 import terminal_owner_generation_is_current
    if not terminal_owner_generation_is_current(
        issue_number, terminal, items,
        transition_head_verifier=github_verified_recovery_source_head,
    ):
        return None
    # FSR-1703-M01: sole owner/lease and a syntactically valid SHA do not
    # authenticate terminal result HEAD/work against the live task branch.
    if not github_verified_terminal_result_heads(
        issue_number, terminal.head_sha, terminal.work_sha
    ):
        return None
    return terminal


def closure_authorized_terminal(issue_number: int) -> OperationalRecord | None:
    return closure_authorized_terminal_from_comments(
        issue_number, paged(f"/repos/{REPO}/issues/{issue_number}/comments?")
    )

def reconcilable_terminal(issue_number: int) -> OperationalRecord | None:
    return reconcilable_terminal_from_comments(
        issue_number,
        paged(f"/repos/{REPO}/issues/{issue_number}/comments?"),
    )


def readiness_dead_end_terminal_from_comments(
    issue_number: int,
    comments: Iterable[dict[str, Any]],
    *,
    directive_created_at: str | None = None,
) -> OperationalRecord | None:
    """Return the latest valid blocked readiness decision that illegally dead-ends.

    Publication/integration provenance is not itself a readiness decision and
    therefore cannot erase an earlier still-controlling decision. A genuinely
    newer valid STATUS/VERIFICATION_STATUS readiness decision does supersede an
    older one. Arbitrary `NONE` routes remain uninterpreted.
    """
    records = operational_records_from_comments(issue_number, comments)
    if not records:
        return None

    directive_time = (
        parse_github_server_time(directive_created_at)
        if directive_created_at is not None
        else None
    )
    if directive_created_at is not None and directive_time is None:
        return None

    selected: OperationalRecord | None = None
    for candidate in sorted(records, key=lambda item: item.comment_id, reverse=True):
        if candidate.kind not in {"STATUS", "VERIFICATION_STATUS"}:
            continue
        if candidate.state not in {"DONE", "VERIFICATION_READY"}:
            continue
        if scalar(candidate.body, "terminal") != "true":
            continue
        if candidate.declared_issue != issue_number:
            continue
        if (
            not candidate.mission_id
            or "IMPLEMENTATION-READINESS" not in candidate.mission_id.upper()
        ):
            continue

        expected_authority = (
            "VERIFIER" if candidate.kind == "VERIFICATION_STATUS" else "OWNER"
        )
        if candidate.authority_mode != expected_authority:
            continue
        if candidate.ownership_generation_comment_id is None:
            continue
        if not candidate.head_sha or not candidate.work_sha:
            continue
        if (
            not SHA40_RE.fullmatch(candidate.head_sha)
            or not SHA40_RE.fullmatch(candidate.work_sha)
        ):
            continue

        owner = next(
            (
                record
                for record in records
                if record.comment_id == candidate.ownership_generation_comment_id
            ),
            None,
        )
        if owner is None or owner.comment_id >= candidate.comment_id:
            continue
        if owner.kind not in OWNERSHIP_KINDS:
            continue
        if owner.declared_issue != issue_number:
            continue
        if owner.actor_session_id != candidate.actor_session_id:
            continue
        if owner.mission_id != candidate.mission_id:
            continue
        if schema3_owner_unexpired_at(
            owner, records, candidate, head_verifier=github_verified_head_advance
        ) is not True:
            continue

        if directive_time is not None:
            terminal_time = parse_github_server_time(candidate.created_at)
            if terminal_time is None:
                continue
            if (
                terminal_time < directive_time
                and issue_number != READINESS_ROUTING_HISTORICAL_SOURCE_ISSUE
            ):
                continue

        selected = candidate
        break

    if selected is None:
        return None
    if selected.route is not None:
        return None

    blocked_outcomes = {
        (scalar(selected.body, "candidate_outcome") or "").upper(),
        (scalar(selected.body, "verified_candidate_outcome") or "").upper(),
    }
    implementation_ready = (
        scalar(selected.body, "implementation_ready") or ""
    ).lower()
    if "BLOCKED" not in blocked_outcomes and implementation_ready != "false":
        return None
    return selected


def readiness_dead_end_title(source_issue: int) -> str:
    return (
        f"[PLAN-v1][FACTORY-READINESS-DEAD-END-{source_issue}] "
        f"Recover blocked readiness routing from #{source_issue}"
    )


def find_readiness_dead_end_issue(
    issues: Iterable[dict[str, Any]], source_issue: int
) -> dict[str, Any] | None:
    marker = f"[FACTORY-READINESS-DEAD-END-{source_issue}]"
    return next(
        (
            item
            for item in issues
            if "pull_request" not in item and marker in (item.get("title") or "")
        ),
        None,
    )


def create_readiness_dead_end_issue(source: OperationalRecord) -> dict[str, Any] | None:
    body = (
        "## Factory readiness liveness diagnostic\n\n"
        f"Source readiness issue: #{source.issue_number}\n"
        f"Source terminal comment: {source.comment_id}\n"
        f"Controlling routing directive: Issue #{READINESS_ROUTING_DIRECTIVE_ISSUE} "
        f"comment `{READINESS_ROUTING_DIRECTIVE_COMMENT_ID}`\n\n"
        "The exact authoritative terminal represents implementation readiness as "
        "blocked/not-ready but declares no required successor. The controlling owner "
        "directive requires exact remaining blockers to be routed rather than treating "
        "that state as project-terminal.\n\n"
        "Re-derive current main, canonical binding, the source terminal, and its exact "
        "remaining blockers. Materialize only the smallest successor/recovery required "
        "by the controlling task contract/directive. Do not fabricate readiness PASS, "
        "implementation authority, or reinterpret unrelated legitimate `NONE` routes.\n"
    )
    print(
        f"materialize readiness dead-end diagnostic from #{source.issue_number}: "
        f"terminal {source.comment_id}"
    )
    if DRY_RUN:
        return None
    return request(
        "POST",
        f"/repos/{REPO}/issues",
        {"title": readiness_dead_end_title(source.issue_number), "body": body},
    )


def close_terminal_open_issues(open_issues: list[dict[str, Any]]) -> int:
    closed = 0
    for issue in open_issues:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        terminal = closure_authorized_terminal(number)
        if not terminal:
            continue
        reason = "completed" if terminal.state == "DONE" else "not_planned"
        print(f"reconcile issue #{number}: authenticated {terminal.kind}/{terminal.state} -> closed/{reason}")
        if not DRY_RUN:
            # Recheck the full GitHub history immediately before the mutation;
            # an intervening owner or edited comment must invalidate closure.
            # REST GET/PATCH are not an atomic transaction, so a final race
            # remains possible; never infer stronger authority from this PATCH.
            fresh = closure_authorized_terminal(number)
            if (
                fresh is None
                or fresh.comment_id != terminal.comment_id
                or fresh.ownership_generation_comment_id != terminal.ownership_generation_comment_id
            ):
                continue
            issue_snapshot = request("GET", f"/repos/{REPO}/issues/{number}")
            if not isinstance(issue_snapshot, dict) or issue_snapshot.get("state") != "open":
                continue
            request("PATCH", f"/repos/{REPO}/issues/{number}",
                    {"state": "closed", "state_reason": reason})
        closed += 1
    return closed

def pr_explicitly_rejected(body: str) -> bool:
    disposition = re.search(
        r"(?im)^\s*(?:review\s+)?disposition\s*:\s*`?(CHANGES_NEEDED|CHANGES_REQUIRED)`?(?:\s*[—-].*)?\s*$",
        body,
    )
    disposition_block = re.search(
        r"(?im)^\s*(?:review\s+)?disposition\s*$\n\s*`?(CHANGES_NEEDED|CHANGES_REQUIRED)`?\s*$",
        body,
    )
    self_prohibition = re.search(
        r"(?i)\bthis\s+(?:draft\s+)?PR\s+must\s+not\s+(?:integrate|be\s+merged)\b",
        body,
    )
    return bool(disposition or disposition_block or self_prohibition)


def close_rejected_open_prs(open_prs: list[dict[str, Any]]) -> int:
    closed = 0
    for pr in open_prs:
        if not pr.get("draft") or pr.get("author_association") not in TRUSTED_ASSOCIATIONS:
            continue
        if not pr_explicitly_rejected(pr.get("body") or ""):
            continue
        number = int(pr["number"])
        print(f"retire explicitly rejected draft PR #{number}")
        if not DRY_RUN:
            request("PATCH", f"/repos/{REPO}/pulls/{number}", {"state": "closed"})
        closed += 1
    return closed


def load_routes() -> dict[str, dict[str, Any]]:
    import base64

    encoded = urllib.parse.quote(ROUTES_PATH, safe="/")
    data = request("GET", f"/repos/{REPO}/contents/{encoded}?ref=main")
    raw = base64.b64decode(data["content"]).decode("utf-8")
    routes = json.loads(raw).get("routes", {})
    if not isinstance(routes, dict):
        raise RuntimeError("routes must be an object")
    return routes


def current_main_sha() -> str:
    return request("GET", f"/repos/{REPO}/branches/main")["commit"]["sha"]


def transition_title(source_issue: int) -> str:
    return f"[PLAN-v1][FACTORY-TRANSITION-{source_issue}] Materialize required next route from #{source_issue}"


def is_factory_transition(issue: dict[str, Any]) -> bool:
    return FACTORY_TRANSITION_RE.search(issue.get("title") or "") is not None


def find_open_transition(open_issues: list[dict[str, Any]], source_issue: int) -> dict[str, Any] | None:
    marker = f"[FACTORY-TRANSITION-{source_issue}]"
    return next((item for item in open_issues if "pull_request" not in item and marker in (item.get("title") or "")), None)


def create_transition(source: OperationalRecord, route_cfg: dict[str, Any] | None) -> dict[str, Any] | None:
    body = (
        "## Factory liveness recovery\n\n"
        f"Source terminal issue: #{source.issue_number}\n"
        f"Source terminal comment: {source.comment_id}\n"
        f"Required next route: `{source.route}`\n\n"
        "This issue exists because a terminal episode declared a required continuation but no live selectable "
        "transition was present. Re-derive current main/canonical binding/ownership before acting. Preserve all "
        "review, verification, authority, exact-head, and squash-only gates.\n\n"
        + ("The route is registered for repository-internal workflow dispatch; maintenance may dispatch it on exact current `main`.\n"
           if route_cfg else
           "The route is not executable by maintenance. Materialize the smallest exact successor/recovery issue required by the source contract; do not invent authority.\n")
    )
    print(f"materialize transition from #{source.issue_number}: {source.route}")
    if DRY_RUN:
        return None
    return request("POST", f"/repos/{REPO}/issues", {"title": transition_title(source.issue_number), "body": body})


def matching_fresh_run(workflow: str, main_sha: str, source_created_at: str) -> dict[str, Any] | None:
    path = urllib.parse.quote(workflow, safe="")
    runs = request("GET", f"/repos/{REPO}/actions/workflows/{path}/runs?event=workflow_dispatch&branch=main&per_page=30")
    for run in runs.get("workflow_runs", []):
        if run.get("head_sha") == main_sha and (not source_created_at or (run.get("created_at") or "") >= source_created_at):
            return run
    return None


def trusted_dispatch_marker_from_comments(
    comments: Iterable[dict[str, Any]], source_issue: int, route: str
) -> dict[str, Any] | None:
    for comment in comments:
        body = comment.get("body") or ""
        user_login = ((comment.get("user") or {}).get("login") or "")
        trusted_author = user_login == "github-actions[bot]" or comment.get("author_association") in TRUSTED_ASSOCIATIONS
        if not trusted_author or not immutable_comment(comment):
            continue
        if scalar(body, "factory_frontier_dispatch") != DISPATCH_MARKER_VERSION:
            continue
        if integer_scalar(body, "source_issue") != source_issue:
            continue
        if scalar(body, "route") != route:
            continue
        if scalar(body, "status") not in DISPATCH_MARKER_STATES:
            continue
        main_sha = scalar(body, "main_sha")
        if not main_sha or not SHA40_RE.fullmatch(main_sha):
            continue
        return comment
    return None


def transition_has_dispatch_marker(transition: dict[str, Any], source_issue: int, route: str) -> bool:
    number = int(transition["number"])
    comments = paged(f"/repos/{REPO}/issues/{number}/comments?")
    return trusted_dispatch_marker_from_comments(comments, source_issue, route) is not None


def record_dispatch_marker(
    transition: dict[str, Any], source: OperationalRecord, workflow: str, main_sha: str,
    status: str, run_id: int | None = None,
) -> None:
    if DRY_RUN:
        return
    lines = [
        f"factory_frontier_dispatch: {DISPATCH_MARKER_VERSION}",
        f"source_issue: {source.issue_number}",
        f"source_terminal_comment_id: {source.comment_id}",
        f"route: {source.route}",
        f"status: {status}",
        f"workflow: {workflow}",
        f"main_sha: {main_sha}",
    ]
    if run_id is not None:
        lines.append(f"run_id: {run_id}")
    lines.extend([
        "authority_created: false",
        "note: Repository factory dispatch marker only; downstream evidence and authority gates remain separate.",
    ])
    request("POST", f"/repos/{REPO}/issues/{int(transition['number'])}/comments", {"body": "\n".join(lines)})


def dispatch_registered_route(source: OperationalRecord, cfg: dict[str, Any], transition: dict[str, Any] | None) -> bool:
    if cfg.get("type") != "workflow_dispatch" or transition is None:
        return False
    workflow = cfg.get("workflow")
    if not workflow or cfg.get("ref", "main") != "main":
        raise RuntimeError(f"unsafe route registration for {source.route}: exact main workflow required")
    if source.route is None:
        raise RuntimeError("registered dispatch requires a source route")
    if transition_has_dispatch_marker(transition, source.issue_number, source.route):
        print(f"route {source.route}: transition already has trusted dispatch marker")
        return False

    main_sha = current_main_sha()
    existing = matching_fresh_run(workflow, main_sha, source.created_at)
    if existing:
        print(f"route {source.route}: observed fresh exact-main run {existing.get('id')} at {main_sha}")
        record_dispatch_marker(
            transition, source, workflow, main_sha, "OBSERVED",
            int(existing["id"]) if existing.get("id") is not None else None,
        )
        return False

    inputs = dict(cfg.get("inputs") or {})
    if "reason" in inputs:
        inputs["reason"] = str(inputs["reason"]).format(source_issue=source.issue_number, main_sha=main_sha)
    payload: dict[str, Any] = {"ref": "main"}
    if inputs:
        payload["inputs"] = inputs
    print(f"dispatch {workflow} on main@{main_sha} for route {source.route}")
    if not DRY_RUN:
        path = urllib.parse.quote(workflow, safe="")
        request("POST", f"/repos/{REPO}/actions/workflows/{path}/dispatches", payload)
        record_dispatch_marker(transition, source, workflow, main_sha, "ACCEPTED")
    return True


def predecessor_sources(issue: dict[str, Any]) -> set[int]:
    text = issue.get("body") or ""
    patterns = (
        r"(?im)^\s*predecessor_issue:\s*(\d+)\s*$",
        r"(?i)immediate predecessor:\s*Issue\s*#(\d+)",
        r"(?i)Source terminal issue:\s*#(\d+)",
    )
    found: set[int] = set()
    for pattern in patterns:
        found.update(int(value) for value in re.findall(pattern, text))
    return found


def consumed_nontransition_sources(issues: Iterable[dict[str, Any]]) -> set[int]:
    consumed: set[int] = set()
    for issue in issues:
        if "pull_request" in issue or is_factory_transition(issue):
            continue
        consumed.update(predecessor_sources(issue))
    return consumed


def materialize_missing_transitions(open_issues: list[dict[str, Any]], routes: dict[str, dict[str, Any]]) -> tuple[int, int]:
    created = dispatched = 0
    closed = list(paged(f"/repos/{REPO}/issues?state=closed&sort=updated&direction=desc&since=2026-08-20T00:00:00Z&"))
    recent_issues = [item for item in open_issues + closed if "pull_request" not in item]
    consumed_sources = consumed_nontransition_sources(recent_issues)
    dispatch_keys: set[tuple[str, str]] = set()
    for issue in closed:
        if "pull_request" in issue:
            continue
        number = int(issue["number"])
        source = reconcilable_terminal(number)
        if not source or not source.route or number in consumed_sources:
            continue
        transition = find_open_transition(open_issues, number)
        cfg = routes.get(source.route)
        if not transition:
            transition = create_transition(source, cfg)
            created += 1
            if transition:
                open_issues.append(transition)
        if cfg and transition:
            key = (str(cfg.get("workflow")), current_main_sha())
            if key not in dispatch_keys and dispatch_registered_route(source, cfg, transition):
                dispatch_keys.add(key)
                dispatched += 1
    return created, dispatched


def materialize_readiness_dead_end_diagnostics(
    open_issues: list[dict[str, Any]],
) -> int:
    """Surface only directive-bound implementation-readiness terminal dead ends."""
    directive = request(
        "GET",
        f"/repos/{REPO}/issues/comments/{READINESS_ROUTING_DIRECTIVE_COMMENT_ID}",
    )
    if not trusted_readiness_routing_directive(directive):
        print(
            "readiness dead-end guard: controlling directive missing/drifted; "
            "fail closed without creating diagnostics"
        )
        return 0

    closed = list(
        paged(
            f"/repos/{REPO}/issues?state=closed&sort=updated&direction=desc&"
            "since=2026-09-01T00:00:00Z&"
        )
    )
    recent_issues = [
        item for item in open_issues + closed if "pull_request" not in item
    ]
    by_number = {int(item["number"]): item for item in recent_issues}
    created = 0

    for issue in list(by_number.values()):
        text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}".upper()
        if "IMPLEMENTATION-READINESS" not in text and "IMPLEMENTATION_READINESS" not in text:
            continue
        number = int(issue["number"])
        comments = list(paged(f"/repos/{REPO}/issues/{number}/comments?"))
        source = readiness_dead_end_terminal_from_comments(
            number,
            comments,
            directive_created_at=directive.get("created_at"),
        )
        if source is None:
            continue
        if readiness_recovery_recorded(comments, source):
            continue
        if find_readiness_dead_end_issue(by_number.values(), number):
            continue

        diagnostic = create_readiness_dead_end_issue(source)
        created += 1
        if diagnostic:
            by_number[int(diagnostic["number"])] = diagnostic
            open_issues.append(diagnostic)

    return created


def self_test() -> None:
    def c(
        cid: int, kind: str, state: str, *, issue: int = 10, actor: str = "actor-a",
        mission: str = "M-10", extra: str = "", association: str = "OWNER",
        edited: bool = False,
    ) -> dict[str, Any]:
        created_at = f"2026-08-25T00:00:{cid:02d}Z"
        updated_at = f"2026-08-25T00:01:{cid:02d}Z" if edited else created_at
        return {
            "id": cid,
            "author_association": association,
            "user": {"login": "vokerg" if association == "OWNER" else "outsider"},
            "created_at": created_at,
            "updated_at": updated_at,
            "body": (
                "protocol: planning-v1\n"
                "schema: 3\n"
                f"kind: {kind}\n"
                f"issue: {issue}\n"
                f"mission_id: {mission}\n"
                f"actor_session_id: {actor}\n"
                f"state: {state}\n"
                f"{extra}"
            ),
        }

    claim = c(1, "CLAIM", "IN_PROGRESS")
    valid_done = c(
        2, "STATUS", "DONE",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
            "required_next_route: NEXT\n"
        ),
    )
    assert reconcilable_terminal_from_comments(10, [claim, valid_done]) is not None

    # FSR-1632-B01: these two YAML documents have only root 'extensions'.
    # A nested operational-looking CLAIM / STATUS cannot authorize closure.
    fake_claim = dict(claim, body=(
        "```yaml\nextensions:\n"
        "  protocol: planning-v1\n  schema: 3\n  kind: CLAIM\n"
        "  issue: 10\n  mission_id: M-10\n  actor_session_id: actor-a\n"
        "  state: IN_PROGRESS\n```"
    ))
    fake_done = dict(valid_done, body=(
        "```yaml\nextensions:\n"
        "  protocol: planning-v1\n  schema: 3\n  kind: STATUS\n"
        "  issue: 10\n  mission_id: M-10\n  actor_session_id: actor-a\n"
        "  state: DONE\n  authority_mode: OWNER\n"
        "  ownership_generation_comment_id: 1\n"
        f"  head_sha: {'a' * 40}\n  work_sha: {'b' * 40}\n```"
    ))
    assert parse_operational(10, fake_claim) is None
    assert parse_operational(10, fake_done) is None
    assert reconcilable_terminal_from_comments(10, [fake_claim, fake_done]) is None

    fenced_claim = dict(claim, body="```yaml\n" + claim["body"] + "```")
    fenced_done = dict(valid_done, body="```yaml\n" + valid_done["body"] + "```")
    assert reconcilable_terminal_from_comments(10, [fenced_claim, fenced_done]) is not None

    for shadow in (
        "protocol: planning-v1\nprotocol: planning-v1\n",
        "protocol: planning-v1\n'protocol': other\n",
        'protocol: planning-v1\n"prot\\u006fcol": other\n',
        "protocol: planning-v1\n!!str protocol: other\n",
        "protocol: planning-v1\n<<: *foreign\n",
    ):
        tamper = dict(claim, body=shadow + claim["body"].split("\n", 1)[1])
        assert parse_operational(10, tamper) is None, shadow
    block_only = dict(claim, body=(
        "```yaml\nnote: |\n  protocol: planning-v1\n  schema: 3\n"
        "  kind: CLAIM\n  issue: 10\n```\n"
    ))
    assert parse_operational(10, block_only) is None
    late_fence = dict(claim, body=(
        "Example, not operational:\n```yaml\n" + claim["body"] + "```"
    ))
    assert parse_operational(10, late_fence) is None
    after_first_fence = dict(claim, body=(
        "```yaml\nnotes: ordinary\n```\n\n"
        "```yaml\n" + claim["body"] + "```"
    ))
    assert parse_operational(10, after_first_fence) is None
    assert scalar("protocol: 'planning-v1' # safe\n", "protocol") == "planning-v1"
    assert scalar('protocol: "planning-v1"\n', "protocol") == "planning-v1"
    assert scalar("protocol: '\"planning-v1\"'\n", "protocol") == '"planning-v1"'
    assert scalar("protocol: '\"planning-v1\"'\n", "protocol") != "planning-v1"
    assert scalar('protocol: "a#b" # inline comment\n', "protocol") == "a#b"
    assert scalar('protocol: "\\u0070lanning-v1"\n', "protocol") == "planning-v1"

    # FSR-1644-B01: only authenticated direct-root lists carry authority.
    ref = "e" * 40
    assert list_scalar("extensions:\n  evidence_refs:\n    - " + ref + "\n", "evidence_refs") == []
    assert list_scalar("evidence_refs:\n  - " + ref + "\n", "evidence_refs") == [ref]
    assert list_scalar("```yaml\nevidence_refs:\n  - '" + ref + "'\n```", "evidence_refs") == [ref]
    assert list_scalar("evidence_refs: [" + ref + "]\n", "evidence_refs") == [ref]
    assert list_scalar("extensions:\n  artifact_paths:\n    - game/foo.gd\n", "artifact_paths") == []
    assert list_scalar("artifact_paths:\n  - game/foo.gd\n", "artifact_paths") == ["game/foo.gd"]
    assert list_scalar("artifact_paths:\n  - 'game/foo.gd'\n", "artifact_paths") == ["game/foo.gd"]
    assert list_scalar("artifact_paths:\n  - game/foo.gd\nartifact_paths:\n  - game/bar.gd\n", "artifact_paths") == []
    assert list_scalar("artifact_paths:\n  - game/foo.gd\n  nested:\n    - game/bar.gd\n", "artifact_paths") == []
    assert list_scalar("artifact_paths: |\n  - game/foo.gd\n", "artifact_paths") == []
    assert list_scalar("artifact_paths:\n  - *foreign_alias\n", "artifact_paths") == []
    assert list_scalar("artifact_paths:\n  - [game/foo.gd]\n", "artifact_paths") == []
    assert list_scalar("artifact_paths: [game/foo.gd, game/bar.gd]\n", "artifact_paths") == ["game/foo.gd", "game/bar.gd"]
    assert list_scalar("notes: |\n  artifact_paths:\n    - game/foo.gd\n", "artifact_paths") == []
    assert list_scalar("example, not operational\n```yaml\nartifact_paths:\n  - game/foo.gd\n```", "artifact_paths") == []

    # FSR-1650-B01: schema-3 lists require actual YAML sequences, never
    # a singleton synthesized from direct-root plain or quoted scalars.
    for scalar_literal in (
        ref, "'" + ref + "'", '"' + ref + '"',
        '!!str "' + ref + '"', '&anchor ' + ref, '*anchor',
    ):
        assert list_scalar("evidence_refs: " + scalar_literal + "\n", "evidence_refs") == []
    for scalar_literal in (
        "game/foo.gd", "'game/foo.gd'", '"game/foo.gd"',
        "!!str game/foo.gd", "&anchor game/foo.gd", "*anchor",
    ):
        assert list_scalar("artifact_paths: " + scalar_literal + "\n", "artifact_paths") == []
    for consumer, path in (
        ("source", "game/main.gd"),
        ("review", "docs/planning/reviews/review.md"),
        ("verifier", "docs/planning/wave-2/verification/review.md"),
    ):
        # v7 source/reviewer/verifier file-identity predicates all consume
        # this same base.list_scalar; single-file PR sets cannot be supplied
        # by YAML root scalars or an indented extensions shadow.
        for false_list in (
            "artifact_paths: " + path + "\n",
            'artifact_paths: "' + path + '"\n',
            "extensions:\n  artifact_paths:\n    - " + path + "\n",
        ):
            assert set(list_scalar(false_list, "artifact_paths")) != {path}, consumer
        for real_list in (
            "artifact_paths:\n  - " + path + "\n",
            "artifact_paths: [" + path + "]\n",
        ):
            assert set(list_scalar(real_list, "artifact_paths")) == {path}, consumer
    assert list_scalar("artifact_paths: {}\n", "artifact_paths") == []
    assert list_scalar("artifact_paths: >\n  - game/main.gd\n", "artifact_paths") == []
    assert list_scalar("artifact_paths: game/main.gd # comment\n", "artifact_paths") == []
    assert list_scalar("artifact_paths: 'a#b'\n", "artifact_paths") == []
    assert list_scalar("artifact_paths: \"a\\u002Fb\"\n", "artifact_paths") == []



    # FSR-1661-B01: no lexical list may confer authority from invalid YAML.
    # These were accepted by the predecessor even though YAML parsers reject
    # the whole document. Reject unsupported structures before all consumers.
    for operational_key, one_value in (
        ("evidence_refs", ref),
        ("artifact_paths", "game/main.gd"),
        ("artifact_paths", "docs/planning/reviews/review.md"),
        ("artifact_paths", "docs/planning/wave-2/verification/review.md"),
    ):
        for malformed in (
            f"{operational_key}: [{one_value}]\n  injected: yes\n",
            f"{operational_key}: [{one_value}]\n  - orphan\n",
            f"{operational_key}: [{{foreign: {one_value}}}]\n",
            f"{operational_key}: [{one_value}\n",
            f"{operational_key}:\n  - {one_value}\n    forged: yes\n",
            f"{operational_key}:\n  - {one_value}\n   bad_indent: yes\n",
        ):
            assert list_scalar(malformed, operational_key) == [], malformed
            assert scalar(malformed, "protocol") is None
        for authentic in (
            f"{operational_key}: [{one_value}]\n",
            f"{operational_key}:\n  - {one_value}\n",
        ):
            assert list_scalar(authentic, operational_key) == [one_value], authentic

    invalid_claim = dict(claim, body=claim["body"] + "artifact_paths: [game/main.gd]\n  forged: yes\n")
    assert parse_operational(10, invalid_claim) is None

    later_claim = c(3, "CLAIM", "IN_PROGRESS")
    assert reconcilable_terminal_from_comments(10, [claim, valid_done, later_claim]) is None

    malformed_done = c(
        2, "STATUS", "DONE",
        extra=f"authority_mode: OWNER\nhead_sha: {'a' * 40}\nwork_sha: {'b' * 40}\n",
    )
    assert reconcilable_terminal_from_comments(10, [claim, malformed_done]) is None

    wrong_actor_done = c(
        2, "STATUS", "DONE", actor="actor-b",
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
        ),
    )
    assert reconcilable_terminal_from_comments(10, [claim, wrong_actor_done]) is None

    outsider_done = dict(valid_done, id=4, author_association="NONE", user={"login": "outsider"})
    assert reconcilable_terminal_from_comments(10, [claim, outsider_done]) is None

    edited_done = c(
        2, "STATUS", "DONE", edited=True,
        extra=(
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 1\n"
            f"head_sha: {'a' * 40}\n"
            f"work_sha: {'b' * 40}\n"
        ),
    )
    assert reconcilable_terminal_from_comments(10, [claim, edited_done]) is None
    edited_claim = c(1, "CLAIM", "IN_PROGRESS", edited=True)
    assert reconcilable_terminal_from_comments(10, [edited_claim, valid_done]) is None

    # FSR-1677-B01: the PATCH consumer must reconstruct the first-winning
    # schema-3 owner at the terminal's publication point, not any old owner ID.
    def secure_comment(cid: int, when: str, kind: str, state: str, *,
                       actor: str = "owner-a", extra: str = "",
                       edited: bool = False) -> dict[str, Any]:
        return {
            "id": cid, "author_association": "OWNER",
            "created_at": when,
            "updated_at": "2026-09-15T23:59:59Z" if edited else when,
            "body": (
                "protocol: planning-v1\nschema: 3\n"
                f"kind: {kind}\nissue: 10\nmission_id: M-10\n"
                "branch: planning/issue-10\n"
                f"actor_session_id: {actor}\nstate: {state}\n{extra}"
            ),
        }

    # Legacy lease fixtures isolate temporal/ownership logic; the separate
    # read-only branch-provenance fixtures below exercise real GET/compare.
    original_result_head_verifier = github_verified_terminal_result_heads
    globals()["github_verified_terminal_result_heads"] = (
        lambda issue, head, work: issue == 10
        and bool(head and SHA40_RE.fullmatch(head))
        and bool(work and SHA40_RE.fullmatch(work))
    )

    secure_claim = secure_comment(
        1, "2026-09-15T12:00:00Z", "CLAIM", "IN_PROGRESS",
        extra=f"observed_head_sha: {'a' * 40}\nprevious_ownership_comment_id: null\n",
    )
    def secure_terminal(cid: int, when: str, generation: int, *,
                        actor: str = "owner-a") -> dict[str, Any]:
        return secure_comment(
            cid, when, "STATUS", "DONE", actor=actor,
            extra=(
                "authority_mode: OWNER\n"
                f"ownership_generation_comment_id: {generation}\n"
                f"head_sha: {'a' * 40}\nwork_sha: {'b' * 40}\n"
                "terminal: true\nrequired_next_route: NEXT\n"
            ),
        )

    secure_done = secure_terminal(2, "2026-09-15T13:00:00Z", 1)
    assert closure_authorized_terminal_from_comments(10, [secure_claim, secure_done])
    expired = secure_terminal(2, "2026-09-15T18:00:00Z", 1)
    assert closure_authorized_terminal_from_comments(10, [secure_claim, expired]) is None
    losing = secure_comment(
        2, "2026-09-15T12:01:00Z", "CLAIM", "IN_PROGRESS",
        actor="owner-b",
        extra=f"observed_head_sha: {'a' * 40}\nprevious_ownership_comment_id: null\n",
    )
    losing_done = secure_terminal(
        3, "2026-09-15T13:00:00Z", 2, actor="owner-b"
    )
    assert closure_authorized_terminal_from_comments(
        10, [secure_claim, losing, losing_done]
    ) is None
    unlinked = secure_comment(
        2, "2026-09-15T12:01:00Z", "RESUME", "IN_PROGRESS",
        actor="owner-b",
        extra=(
            "previous_ownership_comment_id: 1\n"
            f"observed_head_sha: {'a' * 40}\n"
            "source_status_comment_id: 1\nwinning_intent_comment_id: 999\n"
        ),
    )
    assert closure_authorized_terminal_from_comments(
        10, [secure_claim, unlinked,
             secure_terminal(3, "2026-09-15T13:00:00Z", 2, actor="owner-b")]
    ) is None
    forged_recover = dict(unlinked, body=unlinked["body"].replace(
        "kind: RESUME", "kind: RECOVER"
    ))
    assert closure_authorized_terminal_from_comments(
        10, [secure_claim, forged_recover,
             secure_terminal(3, "2026-09-15T13:00:00Z", 2, actor="owner-b")]
    ) is None
    assert closure_authorized_terminal_from_comments(
        10, [secure_claim, secure_done, losing]
    ) is None
    assert closure_authorized_terminal_from_comments(
        10, [secure_claim, dict(secure_done, updated_at="2026-09-15T13:01:00Z")]
    ) is None
    assert closure_authorized_terminal_from_comments(
        10, [secure_claim, secure_done,
             dict(losing, body="protocol: planning-v1\nkind: CLAIM\n", updated_at="2026-09-15T12:02:00Z")]
    ) is None

    # The fourth consecutive EVIDENCE renewal cannot rescue an expired owner.
    evidence = [
        secure_comment(
            idx, f"2026-09-15T{hour:02d}:00:00Z", "PROGRESS", "IN_PROGRESS",
            extra=(
                "ownership_generation_comment_id: 1\n"
                f"observed_head_sha: {'a' * 40}\n"
                "progress_basis: EVIDENCE\n"
                f"evidence_refs: [{'c' * 40}]\n"
            ),
        )
        for idx, hour in enumerate((13, 14, 15, 16), start=2)
    ]
    # E1 at 13:00, E2 at 14:00, E3 at 15:00; E4 at 16:00 is invalid.
    # At 21:30 E3 expired, whereas forged E4 would still be live.
    assert closure_authorized_terminal_from_comments(
        10, [secure_claim, *evidence,
             secure_terminal(6, "2026-09-15T21:30:00Z", 1)]
    ) is None

    # FSR-1677-B01: HEAD_ADVANCE evidence must be verified against the real
    # task branch, ahead-only ancestry and a commit timestamp before PROGRESS.
    progressed = secure_comment(
        2, "2026-09-15T17:00:00Z", "PROGRESS", "IN_PROGRESS",
        extra=(
            "ownership_generation_comment_id: 1\n"
            f"observed_head_sha: {'b' * 40}\n"
            "progress_basis: HEAD_ADVANCE\n"
        ),
    )
    renewed_terminal = secure_terminal(3, "2026-09-15T18:30:00Z", 1)
    original_request = request
    def verified_head_mock(method: str, path: str, payload: Any = None) -> Any:
        if method != "GET":
            raise RuntimeError("write forbidden in HEAD_ADVANCE fixture")
        root = f"/repos/{REPO}"
        if path == root + "/git/ref/heads/planning/issue-10":
            return {"object": {"sha": "b" * 40}}
        if path == root + "/compare/" + "a" * 40 + "..." + "b" * 40:
            return {"status": "ahead", "ahead_by": 1, "behind_by": 0}
        if path == root + "/commits/" + "b" * 40:
            return {"commit": {"committer": {"date": "2026-09-15T16:59:59Z"}}}
        raise RuntimeError(f"unexpected test read: {path}")
    try:
        globals()["request"] = verified_head_mock
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, progressed, renewed_terminal]
        )
        def false_branch_mock(method: str, path: str, payload: Any = None) -> Any:
            if path.endswith("/git/ref/heads/planning/issue-10"):
                return {"object": {"sha": "a" * 40}}
            return verified_head_mock(method, path, payload)
        globals()["request"] = false_branch_mock
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, progressed, renewed_terminal]
        ) is None
    finally:
        globals()["request"] = original_request

    # Mutation consumer must re-read ownership before PATCH; first read alone
    # cannot authorize a write, and an issue already closed must be left alone.
    source_terminal = closure_authorized_terminal_from_comments(
        10, [secure_claim, secure_done]
    )
    assert source_terminal is not None
    # FSR-1703-M01: exercise the ACTUAL terminal storage-closure consumer,
    # not a copied owner predicate. All task-ref proofs are read-only.
    globals()["github_verified_terminal_result_heads"] = original_result_head_verifier
    provenance_request = request
    genuine_a, genuine_b, unrelated = "a" * 40, "b" * 40, "f" * 40
    branch_tip = [genuine_b]
    def terminal_provenance_mock(method: str, path: str, payload: Any = None) -> Any:
        if method != "GET":
            raise RuntimeError("forbidden mutation in branch-proof regression")
        root = f"/repos/{REPO}"
        if path == root + "/git/ref/heads/planning/issue-10":
            return {"object": {"sha": branch_tip[0]}}
        if path == root + f"/compare/{genuine_a}...{genuine_b}":
            return {"status": "ahead", "ahead_by": 1, "behind_by": 0}
        return {"status": "diverged", "ahead_by": 1, "behind_by": 1}

    def terminal_with_result_shas(head: str, work: str) -> dict[str, Any]:
        return dict(secure_done, body=secure_done["body"].replace(
            f"head_sha: {genuine_a}", f"head_sha: {head}"
        ).replace(f"work_sha: {genuine_b}", f"work_sha: {work}"))

    try:
        globals()["request"] = terminal_provenance_mock
        # Legitimate ancestor head and newer work SHA, with one live tip.
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, secure_done]
        ) is not None
        # Legitimate no-work same-base terminal on the actual task tip.
        branch_tip[0] = genuine_a
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, terminal_with_result_shas(genuine_a, genuine_a)]
        ) is not None
        branch_tip[0] = genuine_b
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, terminal_with_result_shas(unrelated, genuine_b)]
        ) is None
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, terminal_with_result_shas(genuine_a, unrelated)]
        ) is None
        # Retired/moved/diverged task tip does not authenticate either SHA.
        branch_tip[0] = unrelated
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, secure_done]
        ) is None
        globals()["request"] = lambda *_a, **_kw: (_ for _ in ()).throw(
            RuntimeError("deleted or unreadable task branch")
        )
        assert closure_authorized_terminal_from_comments(
            10, [secure_claim, secure_done]
        ) is None
    finally:
        globals()["request"] = provenance_request

    original_closure = closure_authorized_terminal
    original_dry_run = DRY_RUN
    reads: list[tuple[str, str]] = []
    def patch_mock(method: str, path: str, payload: Any = None) -> Any:
        reads.append((method, path))
        if method == "GET":
            return {"state": "open"}
        if method == "PATCH":
            return {"state": "closed"}
        raise RuntimeError("unexpected mutation fixture method")
    try:
        globals()["DRY_RUN"] = False
        globals()["request"] = patch_mock
        samples = iter([source_terminal, None])
        globals()["closure_authorized_terminal"] = lambda _: next(samples)
        assert close_terminal_open_issues([{"number": 10}]) == 0
        assert not reads
        samples = iter([source_terminal, source_terminal])
        globals()["closure_authorized_terminal"] = lambda _: next(samples)
        assert close_terminal_open_issues([{"number": 10}]) == 1
        assert [method for method, _ in reads] == ["GET", "PATCH"]
    finally:
        globals()["closure_authorized_terminal"] = original_closure
        globals()["DRY_RUN"] = original_dry_run
        globals()["request"] = original_request

    predecessor_prose = "Predecessor review disposition: `CHANGES_NEEDED`. This PR fixes it and requires fresh review."
    assert not pr_explicitly_rejected(predecessor_prose)
    assert pr_explicitly_rejected("Disposition: `CHANGES_NEEDED` — 0 blocker / 1 major")
    assert pr_explicitly_rejected("Review disposition\nCHANGES_REQUIRED")
    assert pr_explicitly_rejected("This draft PR must not be merged.")

    normal_successor = {"title": "[PLAN-v1] successor", "body": "Immediate predecessor: Issue #10"}
    transition = {"title": "[PLAN-v1][FACTORY-TRANSITION-10] Materialize", "body": "Source terminal issue: #10"}
    assert consumed_nontransition_sources([normal_successor]) == {10}
    assert consumed_nontransition_sources([transition]) == set()

    marker_created_at = "2026-08-25T00:00:09Z"
    marker = {
        "id": 9,
        "author_association": "NONE",
        "user": {"login": "github-actions[bot]"},
        "created_at": marker_created_at,
        "updated_at": marker_created_at,
        "body": (
            "factory_frontier_dispatch: 1\n"
            "source_issue: 10\n"
            "route: NEXT\n"
            "status: ACCEPTED\n"
            f"main_sha: {'c' * 40}\n"
        ),
    }
    assert trusted_dispatch_marker_from_comments([marker], 10, "NEXT") is not None
    assert trusted_dispatch_marker_from_comments([marker], 10, "OTHER") is None
    edited_marker = dict(marker, updated_at="2026-08-25T00:01:09Z")
    assert trusted_dispatch_marker_from_comments([edited_marker], 10, "NEXT") is None

    rate_limited = github_api_error(
        "GET",
        "https://api.github.com/repos/vokerg/everfield/pulls",
        403,
        '{"message":"API rate limit exceeded for installation."}',
    )
    assert isinstance(rate_limited, GitHubRateLimitExceeded)
    generic_forbidden = github_api_error(
        "GET",
        "https://api.github.com/repos/vokerg/everfield/pulls",
        403,
        '{"message":"Resource not accessible by integration"}',
    )
    assert isinstance(generic_forbidden, RuntimeError)
    assert not isinstance(generic_forbidden, GitHubRateLimitExceeded)

    assert parse_github_server_time("2026-09-15T12:00:00Z") is not None
    assert parse_github_server_time("2026-09-15T12:00:00.123456Z") is not None
    assert parse_github_server_time("2026-09-15T12:00:00+02:30") is not None
    assert parse_github_server_time("2026-09-15t12:00:00z") is not None
    assert parse_github_server_time("2026-09-15T12:00:00") is None
    assert parse_github_server_time("2026-09-15 12:00:00+00:00") is None
    assert parse_github_server_time("20260915T120000+00:00") is None
    assert parse_github_server_time("not-a-time") is None

    owner = OperationalRecord(
        issue_number=77, comment_id=1, created_at="2026-09-15T12:00:00Z",
        kind="CLAIM", state="IN_PROGRESS", route=None,
        body=f"observed_head_sha: {'a' * 40}\n", declared_issue=77,
        mission_id="M-77", actor_session_id="actor-77", authority_mode=None,
        ownership_generation_comment_id=None, head_sha=None, work_sha=None,
    )
    progress = OperationalRecord(
        issue_number=77, comment_id=2, created_at="2026-09-15T17:00:00Z",
        kind="PROGRESS", state="IN_PROGRESS", route=None,
        body=(
            f"observed_head_sha: {'b' * 40}\n"
            "progress_basis: HEAD_ADVANCE\n"
            "evidence_refs: []\n"
        ),
        declared_issue=77, mission_id="M-77", actor_session_id="actor-77",
        authority_mode=None, ownership_generation_comment_id=1,
        head_sha=None, work_sha=None,
    )
    before_old_boundary = OperationalRecord(
        issue_number=77, comment_id=3, created_at="2026-09-15T18:00:00Z",
        kind="RESUME_INTENT", state="IN_PROGRESS", route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    exact_new_boundary = OperationalRecord(
        issue_number=77, comment_id=4, created_at="2026-09-15T23:00:00Z",
        kind="RESUME_INTENT", state="IN_PROGRESS", route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    assert schema3_owner_unexpired_at(
        owner, [owner, progress], before_old_boundary,
        head_verifier=lambda *_: True,
    ) is True
    assert schema3_owner_unexpired_at(
        owner, [owner, progress], exact_new_boundary,
        head_verifier=lambda *_: True,
    ) is False

    # Nested extensions.evidence_refs must NEVER refresh owner authority.
    # Genuine root refs before lease expiry do renew. Existing E1/E2/E3/E4
    # tests below also enforce the canonical consecutive-EVIDENCE cap.
    nested_evidence_progress = OperationalRecord(
        issue_number=77, comment_id=2, created_at="2026-09-15T17:59:00Z",
        kind="PROGRESS", state="IN_PROGRESS", route=None,
        body=(
            f"observed_head_sha: {'a' * 40}\n"
            "progress_basis: EVIDENCE\n"
            "extensions:\n"
            f"  evidence_refs:\n    - {'e' * 40}\n"
        ),
        declared_issue=77, mission_id="M-77", actor_session_id="actor-77",
        authority_mode=None, ownership_generation_comment_id=1,
        head_sha=None, work_sha=None,
    )
    genuine_evidence_progress = OperationalRecord(
        issue_number=77, comment_id=2, created_at="2026-09-15T17:59:00Z",
        kind="PROGRESS", state="IN_PROGRESS", route=None,
        body=(
            f"observed_head_sha: {'a' * 40}\n"
            "progress_basis: EVIDENCE\n"
            f"evidence_refs:\n  - {'e' * 40}\n"
        ),
        declared_issue=77, mission_id="M-77", actor_session_id="actor-77",
        authority_mode=None, ownership_generation_comment_id=1,
        head_sha=None, work_sha=None,
    )
    shadow_state = schema3_ownership_lease_state(
        owner, [owner, nested_evidence_progress], before_comment_id=3
    )
    authentic_state = schema3_ownership_lease_state(
        owner, [owner, genuine_evidence_progress], before_comment_id=3
    )
    assert shadow_state is not None and shadow_state.anchor_comment_id == 1
    assert shadow_state.consecutive_evidence == 0
    assert authentic_state is not None and authentic_state.anchor_comment_id == 2
    assert authentic_state.consecutive_evidence == 1
    boundary_1800 = OperationalRecord(
        issue_number=77, comment_id=3, created_at="2026-09-15T18:00:00Z",
        kind="RESUME_INTENT", state="IN_PROGRESS", route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    assert not schema3_owner_unexpired_at(
        owner, [owner, nested_evidence_progress], boundary_1800
    )
    assert schema3_owner_unexpired_at(
        owner, [owner, genuine_evidence_progress], boundary_1800
    )


    # FSR-1650-B01 full lease regression: a root scalar at 17:59 is NOT an
    # EVIDENCE renewal of the 12:00 CLAIM, even when it is an immutable SHA.
    # In contrast the genuine root sequence renews until 23:59.
    scalar_evidence_progress = replace(
        genuine_evidence_progress,
        body=(
            f"observed_head_sha: {'a' * 40}\n"
            "progress_basis: EVIDENCE\n"
            f"evidence_refs: {'e' * 40}\n"
        ),
    )
    quoted_scalar_evidence_progress = replace(
        genuine_evidence_progress,
        body=(
            f"observed_head_sha: {'a' * 40}\n"
            "progress_basis: EVIDENCE\n"
            'evidence_refs: "' + 'e' * 40 + '"\n'
        ),
    )
    late_stale_check = replace(boundary_1800, created_at="2026-09-15T18:01:00Z")
    for invalid_progress in (scalar_evidence_progress, quoted_scalar_evidence_progress):
        invalid_state = schema3_ownership_lease_state(
            owner, [owner, invalid_progress], before_comment_id=3
        )
        assert invalid_state is not None
        assert invalid_state.anchor_comment_id == 1
        assert invalid_state.consecutive_evidence == 0
        assert schema3_owner_unexpired_at(
            owner, [owner, invalid_progress], late_stale_check
        ) is False
    assert schema3_owner_unexpired_at(
        owner, [owner, genuine_evidence_progress], late_stale_check
    ) is True

    # Unchanged HEAD_ADVANCE does not renew; a real advance does. An expired
    # ownership generation is never resurrected by later EVIDENCE.
    same_head_advance = replace(
        progress,
        created_at="2026-09-15T17:59:00Z",
        body=f"observed_head_sha: {'a' * 40}\nprogress_basis: HEAD_ADVANCE\n",
    )
    assert schema3_owner_unexpired_at(
        owner, [owner, same_head_advance], late_stale_check
    ) is False
    assert schema3_owner_unexpired_at(
        owner, [owner, progress], late_stale_check,
        head_verifier=lambda *_: True,
    ) is True
    expired_evidence = replace(
        genuine_evidence_progress, created_at="2026-09-15T18:00:00Z"
    )
    assert schema3_owner_unexpired_at(
        owner, [owner, expired_evidence], late_stale_check
    ) is False


    # FSR-1661-M01: a SHA literal without GitHub-proven movement is not
    # HEAD_ADVANCE. This must hold across the original six-hour expiry.
    assert schema3_owner_unexpired_at(
        owner, [owner, progress], late_stale_check
    ) is False
    assert schema3_owner_unexpired_at(
        owner, [owner, progress], late_stale_check,
        head_verifier=lambda *_: False,
    ) is False
    assert schema3_owner_unexpired_at(
        owner, [owner, progress], late_stale_check,
        head_verifier=lambda o, p, old, new: (
            o.comment_id == 1 and p.comment_id == 2
            and old == "a" * 40 and new == "b" * 40
        ),
    ) is True

    # Test the real GitHub-backed verifier with mocked authenticated REST
    # responses: live branch mismatch and false ancestry both fail closed.
    from unittest.mock import patch
    owned_branch = replace(owner, body=(
        "branch: planning/issue-77\n"
        f"observed_head_sha: {'a' * 40}\n"
    ))
    valid_ref = {"object": {"sha": "b" * 40}}
    valid_compare = {"status": "ahead", "ahead_by": 1, "behind_by": 0}
    valid_commit = {"commit": {"committer": {"date": "2026-09-15T16:30:00Z"}}}
    with patch(__name__ + ".request", side_effect=[valid_ref, valid_compare, valid_commit]):
        assert github_verified_head_advance(owned_branch, progress, "a" * 40, "b" * 40)
    with patch(__name__ + ".request", return_value={"object": {"sha": "a" * 40}}):
        assert not github_verified_head_advance(owned_branch, progress, "a" * 40, "b" * 40)
    with patch(__name__ + ".request", side_effect=[
        valid_ref, {"status": "diverged", "ahead_by": 1, "behind_by": 1}
    ]):
        assert not github_verified_head_advance(owned_branch, progress, "a" * 40, "b" * 40)

    malformed_evidence = replace(
        genuine_evidence_progress,
        body=(
            f"observed_head_sha: {'a' * 40}\nprogress_basis: EVIDENCE\n"
            f"evidence_refs: [{'e' * 40}]\n  injected: yes\n"
        ),
    )
    assert schema3_owner_unexpired_at(
        owner, [owner, malformed_evidence], late_stale_check
    ) is False

    evidence_records = [owner]
    for cid, hour in ((2, 13), (3, 14), (4, 15), (5, 16)):
        evidence_records.append(
            OperationalRecord(
                issue_number=77, comment_id=cid,
                created_at=f"2026-09-15T{hour:02d}:00:00Z",
                kind="PROGRESS", state="IN_PROGRESS", route=None,
                body=(
                    f"observed_head_sha: {'a' * 40}\n"
                    "progress_basis: EVIDENCE\n"
                    f"evidence_refs:\n  - {'e' * 40}\n"
                ),
                declared_issue=77, mission_id="M-77", actor_session_id="actor-77",
                authority_mode=None, ownership_generation_comment_id=1,
                head_sha=None, work_sha=None,
            )
        )
    evidence_state = schema3_ownership_lease_state(
        owner, evidence_records, before_comment_id=6
    )
    assert evidence_state is not None
    assert evidence_state.anchor_comment_id == 4
    assert evidence_state.consecutive_evidence == 3

    probe = OperationalRecord(
        issue_number=77, comment_id=10, created_at="2026-09-15T12:00:00Z",
        kind="ORPHAN_PROBE", state=None, route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    early = OperationalRecord(
        issue_number=77, comment_id=11, created_at="2026-09-15T12:09:59Z",
        kind="RESUME_INTENT", state=None, route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    mature = OperationalRecord(
        issue_number=77, comment_id=12, created_at="2026-09-15T12:10:00Z",
        kind="RESUME_INTENT", state=None, route=None, body="",
        declared_issue=77, mission_id="M-77", actor_session_id="actor-78",
        authority_mode=None, ownership_generation_comment_id=None,
        head_sha=None, work_sha=None,
    )
    assert schema3_orphan_probe_mature_at(probe, early) is False
    assert schema3_orphan_probe_mature_at(probe, mature) is True

    readiness_claim = c(
        20, "CLAIM", "IN_PROGRESS", issue=1038,
        actor="readiness-verifier", mission="W2-IMPLEMENTATION-READINESS-CONT-01-VER-01",
        extra=f"observed_head_sha: {'c' * 40}\nprevious_ownership_comment_id: null\n",
    )
    readiness_blocked = c(
        21, "VERIFICATION_STATUS", "DONE", issue=1038,
        actor="readiness-verifier", mission="W2-IMPLEMENTATION-READINESS-CONT-01-VER-01",
        extra=(
            "terminal: true\n"
            "authority_mode: VERIFIER\n"
            "ownership_generation_comment_id: 20\n"
            f"head_sha: {'c' * 40}\n"
            f"work_sha: {'c' * 40}\n"
            "verified_candidate_outcome: BLOCKED\n"
            "implementation_ready: false\n"
            "required_next_route: NONE\n"
        ),
    )
    dead_end = readiness_dead_end_terminal_from_comments(
        1038, [readiness_claim, readiness_blocked]
    )
    assert dead_end is not None
    assert dead_end.comment_id == 21


    integration_claim = c(
        30, "CLAIM", "IN_PROGRESS", issue=1038,
        actor="readiness-integration",
        mission="W2-IMPLEMENTATION-READINESS-CONT-01-VER-01-INTEGRATION",
        extra=f"observed_head_sha: {'c' * 40}\nprevious_ownership_comment_id: null\n",
    )
    integration_done = c(
        31, "INTEGRATION_STATUS", "DONE", issue=1038,
        actor="readiness-integration",
        mission="W2-IMPLEMENTATION-READINESS-CONT-01-VER-01-INTEGRATION",
        extra=(
            "terminal: true\n"
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 30\n"
            f"head_sha: {'c' * 40}\n"
            f"work_sha: {'c' * 40}\n"
            "canonicality: NON_CANONICAL_VERIFICATION_PROVENANCE\n"
        ),
    )
    persisted_dead_end = readiness_dead_end_terminal_from_comments(
        1038,
        [readiness_claim, readiness_blocked, integration_claim, integration_done],
    )
    assert persisted_dead_end is not None
    assert persisted_dead_end.comment_id == 21

    newer_ready_claim = c(
        32, "CLAIM", "IN_PROGRESS", issue=1038,
        actor="new-readiness-verifier",
        mission="W2-IMPLEMENTATION-READINESS-CONT-02-VER-01",
        extra=f"observed_head_sha: {'f' * 40}\nprevious_ownership_comment_id: null\n",
    )
    newer_ready = c(
        33, "VERIFICATION_STATUS", "DONE", issue=1038,
        actor="new-readiness-verifier",
        mission="W2-IMPLEMENTATION-READINESS-CONT-02-VER-01",
        extra=(
            "terminal: true\n"
            "authority_mode: VERIFIER\n"
            "ownership_generation_comment_id: 32\n"
            f"head_sha: {'f' * 40}\n"
            f"work_sha: {'f' * 40}\n"
            "verified_candidate_outcome: READY\n"
            "implementation_ready: true\n"
            "required_next_route: NONE\n"
        ),
    )
    assert readiness_dead_end_terminal_from_comments(
        1038,
        [
            readiness_claim,
            readiness_blocked,
            integration_claim,
            integration_done,
            newer_ready_claim,
            newer_ready,
        ],
    ) is None

    readiness_routed = dict(
        readiness_blocked,
        id=22,
        created_at="2026-08-25T00:00:22Z",
        updated_at="2026-08-25T00:00:22Z",
        body=readiness_blocked["body"].replace(
            "required_next_route: NONE", "required_next_route: EXACT_BLOCKER_ROUTE"
        ),
    )
    assert readiness_dead_end_terminal_from_comments(
        1038, [readiness_claim, readiness_routed]
    ) is None

    unrelated_claim = c(23, "CLAIM", "IN_PROGRESS", issue=2000, mission="OTHER-MISSION")
    unrelated_none = c(
        24, "STATUS", "DONE", issue=2000, mission="OTHER-MISSION",
        extra=(
            "terminal: true\n"
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 23\n"
            f"head_sha: {'d' * 40}\n"
            f"work_sha: {'d' * 40}\n"
            "implementation_ready: false\n"
            "required_next_route: NONE\n"
        ),
    )
    assert readiness_dead_end_terminal_from_comments(
        2000, [unrelated_claim, unrelated_none]
    ) is None

    legacy_readiness_claim = c(
        26, "CLAIM", "IN_PROGRESS", issue=2001,
        actor="legacy-readiness", mission="W2-IMPLEMENTATION-READINESS-LEGACY",
        extra=f"observed_head_sha: {'e' * 40}\nprevious_ownership_comment_id: null\n",
    )
    legacy_readiness_none = c(
        27, "STATUS", "DONE", issue=2001,
        actor="legacy-readiness", mission="W2-IMPLEMENTATION-READINESS-LEGACY",
        extra=(
            "terminal: true\n"
            "authority_mode: OWNER\n"
            "ownership_generation_comment_id: 26\n"
            f"head_sha: {'e' * 40}\n"
            f"work_sha: {'e' * 40}\n"
            "candidate_outcome: BLOCKED\n"
            "implementation_ready: false\n"
            "required_next_route: NONE\n"
        ),
    )
    assert readiness_dead_end_terminal_from_comments(
        2001,
        [legacy_readiness_claim, legacy_readiness_none],
        directive_created_at="2026-09-29T12:00:02Z",
    ) is None
    assert readiness_dead_end_terminal_from_comments(
        1038,
        [readiness_claim, readiness_blocked],
        directive_created_at="2026-09-29T12:00:02Z",
    ) is not None

    readiness_ready = dict(
        readiness_blocked,
        id=25,
        created_at="2026-08-25T00:00:25Z",
        updated_at="2026-08-25T00:00:25Z",
        body=readiness_blocked["body"]
            .replace("verified_candidate_outcome: BLOCKED", "verified_candidate_outcome: READY")
            .replace("implementation_ready: false", "implementation_ready: true"),
    )
    assert readiness_dead_end_terminal_from_comments(
        1038, [readiness_claim, readiness_ready]
    ) is None

    directive_time = "2026-09-29T12:00:02Z"
    directive = {
        "id": READINESS_ROUTING_DIRECTIVE_COMMENT_ID,
        "issue_url": f"https://api.github.com/repos/{REPO}/issues/{READINESS_ROUTING_DIRECTIVE_ISSUE}",
        "author_association": "OWNER",
        "created_at": directive_time,
        "updated_at": directive_time,
        "body": (
            "If readiness remains false, route exact remaining blockers.\n"
            "A verified `BLOCKED` readiness state may not terminate with no successor "
            "while a concrete internally resolvable blocker remains.\n"
        ),
    }
    assert trusted_readiness_routing_directive(directive)
    assert not trusted_readiness_routing_directive(
        dict(directive, updated_at="2026-09-29T12:01:02Z")
    )

    recovery_time = "2026-09-29T12:03:33Z"
    recovery = {
        "id": 5_889_876_653,
        "author_association": "OWNER",
        "created_at": recovery_time,
        "updated_at": recovery_time,
        "body": (
            "## Owner-directed readiness recovery\n"
            f"Directive {READINESS_ROUTING_DIRECTIVE_COMMENT_ID}.\n"
            "The previously open predicates now have explicit live successors.\n"
        ),
    }
    assert readiness_recovery_recorded(
        [readiness_claim, readiness_blocked, recovery], dead_end
    )

    assert readiness_dead_end_title(1038).startswith(
        "[PLAN-v1][FACTORY-READINESS-DEAD-END-1038]"
    )

    print("frontier maintenance self-test: PASS")


def main() -> int:
    if "--self-test" in sys.argv:
        self_test()
        return 0
    open_items = list(paged(f"/repos/{REPO}/issues?state=open&sort=created&direction=asc&"))
    open_prs = list(paged(f"/repos/{REPO}/pulls?state=open&sort=created&direction=asc&"))
    issue_closed = close_terminal_open_issues(open_items)
    pr_closed = close_rejected_open_prs(open_prs)
    readiness_dead_ends_created = materialize_readiness_dead_end_diagnostics(open_items)
    transition_created, dispatched = materialize_missing_transitions(open_items, load_routes())
    print(json.dumps({
        "dry_run": DRY_RUN,
        "terminal_issues_closed": issue_closed,
        "rejected_prs_closed": pr_closed,
        "readiness_dead_ends_created": readiness_dead_ends_created,
        "transitions_created": transition_created,
        "registered_routes_dispatched": dispatched,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
