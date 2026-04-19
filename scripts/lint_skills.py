#!/usr/bin/env python3
"""Structural linter for Supervisor-Skills SKILL.md files.

Enforces the hard rules for SKILL.md structure:
 - SKILL.md body (after frontmatter) is at most 500 lines
 - description is 40..80 words, third person, contains at least one "Use when" clause
 - no em-dash in SKILL.md or references/*.md
 - no CJK characters in SKILL.md
 - every "See: references/X.md" pointer resolves
 - no nested references (references/X.md may not link to references/Y.md)
 - references/*.md longer than 100 lines must have a table of contents in the first 20 lines
 - no Claude or Anthropic attribution strings

Exit 0 on clean, 1 on any violation. Prints one line per violation.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

SKILL_ROOT = Path("plugins/phd-research/skills")

EM_DASH = "\u2014"
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
REF_POINTER = re.compile(r"See:\s+references/([A-Za-z0-9_\-./]+\.md)")
REF_LINK = re.compile(r"\[[^\]]+\]\((?:\./)?references/([A-Za-z0-9_\-./]+\.md)\)")
BANNED_ATTRIB = [
    "Co-Authored-By: Claude",
    "Generated with [Claude Code]",
    "🤖 Generated with",
    "Anthropic SDK",  # only flags as attribution in skill files, not in script strings themselves
]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter dict, body). Raises ValueError on malformed."""
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opener '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing YAML frontmatter closer '---'")
    fm_text = text[4:end]
    body = text[end + 5 :]

    fm: dict[str, str] = {}
    current_key = None
    current_val: list[str] = []
    for line in fm_text.splitlines():
        m = re.match(r"^([a-zA-Z_\-]+):\s*(.*)$", line)
        if m and not line.startswith(" "):
            if current_key is not None:
                fm[current_key] = "\n".join(current_val).strip()
            current_key = m.group(1)
            current_val = [m.group(2)]
        else:
            current_val.append(line)
    if current_key is not None:
        fm[current_key] = "\n".join(current_val).strip()
    return fm, body


def check_description(desc: str) -> list[str]:
    errors: list[str] = []
    clean = desc.replace(">-", "").replace(">", "").replace("\n", " ").strip()
    words = [w for w in clean.split() if w]
    if not (40 <= len(words) <= 80):
        errors.append(f"description has {len(words)} words; must be 40..80")
    first_person = re.search(r"\b(I|my|we|our|us)\b", clean, re.IGNORECASE)
    if first_person:
        errors.append(
            "description contains first-person pronoun; must be third person"
        )
    if "Use when" not in clean and "use when" not in clean:
        errors.append("description must contain at least one 'Use when' clause")
    return errors


def check_body(body: str, max_lines: int = 500) -> list[str]:
    errors: list[str] = []
    lines = body.splitlines()
    if len(lines) > max_lines:
        errors.append(f"body has {len(lines)} lines; must be <= {max_lines}")
    if EM_DASH in body:
        first = body.find(EM_DASH)
        line_no = body[:first].count("\n") + 1
        errors.append(f"em-dash found at body line {line_no}")
    m = CJK.search(body)
    if m:
        line_no = body[: m.start()].count("\n") + 1
        errors.append(
            f"CJK character {m.group()!r} found at body line {line_no}; SKILL.md is English-only"
        )
    for banned in BANNED_ATTRIB:
        if banned in body:
            errors.append(f"banned attribution string found: {banned!r}")
    return errors


def check_pointers(skill_dir: Path, body: str) -> list[str]:
    errors: list[str] = []
    targets: set[str] = set()
    for m in REF_POINTER.finditer(body):
        targets.add(m.group(1))
    for m in REF_LINK.finditer(body):
        targets.add(m.group(1))
    for target in targets:
        ref = skill_dir / "references" / target
        if not ref.exists():
            errors.append(f"pointer to missing reference: references/{target}")
    return errors


def check_reference_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text()
    except UnicodeDecodeError:
        errors.append(f"{path}: not valid UTF-8")
        return errors
    if EM_DASH in text:
        first = text.find(EM_DASH)
        line_no = text[:first].count("\n") + 1
        errors.append(f"{path}: em-dash at line {line_no}")
    for banned in BANNED_ATTRIB:
        if banned in text:
            errors.append(f"{path}: banned attribution {banned!r}")
    # nested references check
    for m in REF_POINTER.finditer(text):
        errors.append(
            f"{path}: nested reference pointer 'See: references/{m.group(1)}' is forbidden"
        )
    # ToC check for files > 100 lines
    lines = text.splitlines()
    if len(lines) > 100:
        head = "\n".join(lines[:20]).lower()
        if (
            "table of contents" not in head
            and "## contents" not in head
            and "toc" not in head
        ):
            errors.append(
                f"{path}: file has {len(lines)} lines but no table of contents in first 20 lines"
            )
    return errors


def lint_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill_dir}: missing SKILL.md")
        return errors

    try:
        text = skill_md.read_text()
    except UnicodeDecodeError:
        errors.append(f"{skill_md}: not valid UTF-8")
        return errors

    try:
        fm, body = parse_frontmatter(text)
    except ValueError as e:
        errors.append(f"{skill_md}: {e}")
        return errors

    if "name" not in fm:
        errors.append(f"{skill_md}: frontmatter missing 'name'")
    else:
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-]{0,62}[a-z0-9]", fm["name"]):
            errors.append(
                f"{skill_md}: name {fm['name']!r} must be kebab-case, 2..64 chars, [a-z0-9-]"
            )
        if fm["name"] != skill_dir.name:
            errors.append(
                f"{skill_md}: frontmatter name {fm['name']!r} must match directory name {skill_dir.name!r}"
            )

    if "description" not in fm:
        errors.append(f"{skill_md}: frontmatter missing 'description'")
    else:
        errors.extend(f"{skill_md}: {e}" for e in check_description(fm["description"]))

    errors.extend(f"{skill_md}: {e}" for e in check_body(body))
    errors.extend(f"{skill_md}: {e}" for e in check_pointers(skill_dir, body))

    ref_dir = skill_dir / "references"
    if ref_dir.is_dir():
        for ref_md in sorted(ref_dir.rglob("*.md")):
            errors.extend(check_reference_file(ref_md))

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    os.chdir(repo_root)

    if not SKILL_ROOT.is_dir():
        print(f"lint: SKILL_ROOT {SKILL_ROOT} does not exist; nothing to lint.")
        return 0

    skill_dirs = [p for p in sorted(SKILL_ROOT.iterdir()) if p.is_dir()]
    if not skill_dirs:
        print(f"lint: no skills under {SKILL_ROOT}; nothing to lint.")
        return 0

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        all_errors.extend(lint_skill(skill_dir))

    if all_errors:
        print(f"lint: {len(all_errors)} violation(s)")
        for e in all_errors:
            print(f"  {e}")
        return 1

    print(f"lint: {len(skill_dirs)} skill(s) clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
