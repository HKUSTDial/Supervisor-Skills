#!/usr/bin/env python3
"""Validate an independent visual-review response before accepting its verdict."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


FIELD_RE = re.compile(r"^([a-z0-9_]+):\s*(.*?)\s*$", re.IGNORECASE)
ICON_RE = re.compile(r"^-\s+([^:]+):\s*(PASS|FIX)\b", re.IGNORECASE)
HASH_RE = re.compile(r"^([^=;]+)=([0-9a-fA-F]{64})$")


def _field(lines: list[str], name: str) -> str | None:
    wanted = name.lower()
    for line in lines:
        match = FIELD_RE.match(line.strip())
        if match and match.group(1).lower() == wanted:
            return match.group(2).strip()
    return None


def _manifest_ids(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    icons = data.get("icons") if isinstance(data, dict) else data
    if not isinstance(icons, list):
        raise ValueError("icons.json must contain an icons list")
    ids = [item.get("id") for item in icons if isinstance(item, dict)]
    if len(ids) != len(icons) or any(not isinstance(item, str) or not item for item in ids):
        raise ValueError("every icon entry must have a non-empty string id")
    if len(ids) != len(set(ids)):
        raise ValueError("icons.json contains duplicate ids")
    return ids


def _icon_verdicts(lines: list[str]) -> list[tuple[str, str]]:
    try:
        start = next(i for i, line in enumerate(lines) if line.strip().lower() == "icon_verdicts:")
    except StopIteration as exc:
        raise ValueError("missing icon_verdicts section") from exc
    verdicts: list[tuple[str, str]] = []
    for line in lines[start + 1 :]:
        stripped = line.strip()
        if stripped and not stripped.startswith("-") and stripped.endswith(":"):
            break
        match = ICON_RE.match(stripped)
        if match:
            verdicts.append((match.group(1).strip(), match.group(2).upper()))
    return verdicts


def _hashes(lines: list[str]) -> dict[str, str]:
    raw = _field(lines, "artifact_sha256")
    result: dict[str, str] = {}
    if raw:
        entries = [part.strip() for part in raw.split(";")]
    else:
        try:
            start = next(
                i for i, line in enumerate(lines)
                if line.strip().lower() == "artifact_sha256:"
            )
        except StopIteration as exc:
            raise ValueError("missing artifact_sha256") from exc
        entries = []
        for line in lines[start + 1 :]:
            stripped = line.strip()
            if not stripped.startswith("-"):
                break
            value = stripped[1:].strip()
            if ":" not in value:
                raise ValueError(f"invalid artifact_sha256 entry: {value!r}")
            name, digest = value.rsplit(":", 1)
            entries.append(f"{name.strip()}={digest.strip()}")
    if not entries:
        raise ValueError("empty artifact_sha256")
    for entry in entries:
        match = HASH_RE.match(entry)
        if not match:
            raise ValueError(f"invalid artifact_sha256 entry: {entry!r}")
        name, digest = match.group(1).strip(), match.group(2).lower()
        if name in result:
            raise ValueError(f"duplicate artifact hash name: {name}")
        result[name] = digest
    return result


def _artifacts(values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"artifact must be NAME=PATH: {value!r}")
        name, raw_path = value.split("=", 1)
        name = name.strip()
        path = Path(raw_path).expanduser().resolve()
        if not name or name in result:
            raise ValueError(f"empty or duplicate artifact name: {name!r}")
        if not path.is_file():
            raise ValueError(f"artifact does not exist: {path}")
        result[name] = path
    return result


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(args: argparse.Namespace) -> list[str]:
    errors: list[str] = []
    lines = args.result.read_text(encoding="utf-8").splitlines()
    nonempty = [line.strip() for line in lines if line.strip()]
    verdict = nonempty[0].upper() if nonempty else ""
    if verdict not in {"PASS", "FIX"}:
        errors.append("first non-empty line must be PASS or FIX")

    expected_fields = {
        "producer_id": args.producer_id,
        "reviewer_id": args.reviewer_id,
        "artifact_version": args.artifact_version,
    }
    for name, expected in expected_fields.items():
        actual = _field(lines, name)
        if actual != expected:
            errors.append(f"{name} mismatch: expected {expected!r}, got {actual!r}")
    if args.producer_id == args.reviewer_id:
        errors.append("producer_id and reviewer_id must differ")

    try:
        expected_ids = _manifest_ids(args.icons)
        actual_verdicts = _icon_verdicts(lines)
        actual_ids = [item[0] for item in actual_verdicts]
        if actual_ids != expected_ids:
            errors.append("icon_verdicts ids/order do not exactly match icons.json")
        if verdict == "PASS" and any(item[1] != "PASS" for item in actual_verdicts):
            errors.append("overall PASS contains an icon FIX")
        if verdict == "FIX" and not any(item[1] == "FIX" for item in actual_verdicts):
            non_icon = _field(lines, "non_icon_fixes")
            if not non_icon or non_icon.lower() == "none":
                errors.append("overall FIX has neither an icon FIX nor non_icon_fixes")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(str(exc))

    try:
        claimed = _hashes(lines)
        artifacts = _artifacts(args.artifact)
        if set(claimed) != set(artifacts):
            errors.append("artifact_sha256 names do not exactly match submitted artifacts")
        else:
            for name, path in artifacts.items():
                actual = _sha256(path)
                if claimed[name] != actual:
                    errors.append(f"artifact hash mismatch for {name}")
    except (OSError, ValueError) as exc:
        errors.append(str(exc))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    parser.add_argument("--icons", type=Path, required=True)
    parser.add_argument("--producer-id", required=True)
    parser.add_argument("--reviewer-id", required=True)
    parser.add_argument("--artifact-version", required=True)
    parser.add_argument("--artifact", action="append", default=[], metavar="NAME=PATH")
    args = parser.parse_args()
    errors = validate(args)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("review result: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
