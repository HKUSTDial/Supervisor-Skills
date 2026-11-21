#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import re


def _float_attr(element, name, default=0.0):
    try:
        return float(element.attrib.get(name, default))
    except (TypeError, ValueError):
        return default


def _geometry(cell):
    geo = cell.find("mxGeometry")
    if geo is None:
        return None
    x = _float_attr(geo, "x")
    y = _float_attr(geo, "y")
    width = _float_attr(geo, "width")
    height = _float_attr(geo, "height")
    return x, y, width, height


def _inside(child, parent, tolerance=1.0):
    cx, cy, cw, ch = child
    px, py, pw, ph = parent
    return (
        cx >= px - tolerance
        and cy >= py - tolerance
        and cx + cw <= px + pw + tolerance
        and cy + ch <= py + ph + tolerance
    )


def _semantic_containment_failures(cells_by_id):
    workflow_re = re.compile(r"^(step|num|numtxt|icon|title|body|arr)[1-5]$")
    core_re = re.compile(r"^core_(title|bar|icon\d+|text\d+|sep\d+)$")
    evidence_re = re.compile(r"^(evidence_title|ev\d+|ev_icon\d+|ev_title\d+|ev_body\d+)$")
    outcome_re = re.compile(r"^out_(title|person|check|check_mark|row\d+|icon\d+|text\d+)$")
    user_re = re.compile(
        r"^(user_title|request_bubble|request_tail|request_text|left_person|role|mini_.*)$"
    )
    why_re = re.compile(r"^why_(title|bullet\d+|text\d+)$")

    rules = [
        ("user_panel", user_re),
        ("workflow_box", workflow_re),
        ("workflow_box", core_re),
        ("evidence_panel", evidence_re),
        ("outcome_panel", outcome_re),
        ("why_box", why_re),
    ]

    failures = []
    for container_id, matcher in rules:
        container = cells_by_id.get(container_id)
        if container is None:
            continue
        container_geo = _geometry(container)
        if container_geo is None:
            continue

        for cell_id, cell in cells_by_id.items():
            if cell_id == container_id or not matcher.match(cell_id):
                continue
            geo = _geometry(cell)
            if geo is None:
                continue
            if not _inside(geo, container_geo):
                failures.append(
                    f"{cell_id} is outside {container_id}: "
                    f"cell=({geo[0]:.1f},{geo[1]:.1f},{geo[2]:.1f},{geo[3]:.1f}) "
                    f"container=({container_geo[0]:.1f},{container_geo[1]:.1f},"
                    f"{container_geo[2]:.1f},{container_geo[3]:.1f})"
                )

    for prefix in ("out", "ev"):
        for i in range(10):
            row = cells_by_id.get(f"{prefix}_row{i}" if prefix == "out" else f"{prefix}{i}")
            if row is None:
                continue
            row_geo = _geometry(row)
            if row_geo is None:
                continue
            child_ids = (
                [f"{prefix}_icon{i}", f"{prefix}_text{i}"]
                if prefix == "out"
                else [f"{prefix}_icon{i}", f"{prefix}_title{i}", f"{prefix}_body{i}"]
            )
            for child_id in child_ids:
                child = cells_by_id.get(child_id)
                if child is None:
                    continue
                child_geo = _geometry(child)
                if child_geo is None:
                    continue
                if not _inside(child_geo, row_geo, tolerance=2.0):
                    failures.append(
                        f"{child_id} is outside {row.attrib.get('id')}: "
                        f"cell=({child_geo[0]:.1f},{child_geo[1]:.1f},"
                        f"{child_geo[2]:.1f},{child_geo[3]:.1f}) "
                        f"container=({row_geo[0]:.1f},{row_geo[1]:.1f},"
                        f"{row_geo[2]:.1f},{row_geo[3]:.1f})"
                    )
    return failures


def _style_value(style, key):
    prefix = key + "="
    for part in style.split(";"):
        if part.startswith(prefix):
            return part[len(prefix):]
    return None


def _plain_text(value):
    value = value.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("&nbsp;", " ")
    return value.strip()


def _estimated_text_failures(vertices):
    failures = []
    risky_text_ids = re.compile(
        r"^(request_text|body[1-5]|out_text\d+|ev_title\d+|ev_body\d+|why_title|why_text\d+)$"
    )
    for cell in vertices:
        cell_id = cell.attrib.get("id", "<no-id>")
        if not risky_text_ids.match(cell_id):
            continue
        value = _plain_text(cell.attrib.get("value", ""))
        if not value:
            continue
        geo = _geometry(cell)
        if geo is None:
            continue
        width = geo[2]
        height = geo[3]
        if width <= 0 or height <= 0:
            continue
        style = cell.attrib.get("style", "")
        try:
            font_size = float(_style_value(style, "fontSize") or 14)
        except ValueError:
            font_size = 14

        # Conservative estimate for wrapped presentation text. It catches common
        # Draw.io exports where text renders outside a too-short text box.
        chars_per_line = max(5, int(width / max(font_size * 0.58, 1)))
        line_count = 0
        for explicit_line in value.splitlines() or [value]:
            explicit_line = explicit_line.strip()
            if not explicit_line:
                line_count += 1
                continue
            words = explicit_line.split()
            current = 0
            lines = 1
            for word in words:
                needed = len(word) if current == 0 else current + 1 + len(word)
                if needed > chars_per_line:
                    lines += 1
                    current = len(word)
                else:
                    current = needed
            line_count += lines
        required = line_count * font_size * 1.12 + 6
        if height + 1 < required:
            failures.append(
                f"{cell_id} text box may clip: "
                f"height={height:.1f}, estimated_required={required:.1f}, "
                f"fontSize={font_size:.1f}, text={value[:60]!r}"
            )
    return failures


def _image_payload(style):
    for part in style.split(";"):
        if part.startswith("image="):
            return part[len("image="):]
    return None


def _duplicate_icon_failures(cells_by_id):
    failures = []
    groups = [
        ("evidence icons", re.compile(r"^ev_icon\d+$")),
        ("core-strip icons", re.compile(r"^core_icon\d+$")),
        ("workflow step icons", re.compile(r"^icon\d+$")),
        ("outcome row icons", re.compile(r"^out_icon\d+$")),
    ]
    for label, matcher in groups:
        seen = {}
        for cell_id, cell in sorted(cells_by_id.items()):
            if not matcher.match(cell_id):
                continue
            payload = _image_payload(cell.attrib.get("style", ""))
            if not payload:
                continue
            if payload in seen:
                failures.append(
                    f"{label} reuse the same image payload: {seen[payload]} and {cell_id}"
                )
            else:
                seen[payload] = cell_id
    return failures


def _image_encoding_failures(cells_by_id):
    failures = []
    for cell_id, cell in sorted(cells_by_id.items()):
        payload = _image_payload(cell.attrib.get("style", ""))
        if not payload:
            continue
        if payload.startswith("data:image/svg+xml") and "#" in payload:
            failures.append(
                f"{cell_id} SVG data URL contains raw '#'; encode colors as %23"
            )
    return failures


def _complex_visual_svg_failures(cells_by_id):
    failures = []
    complex_re = re.compile(
        r"(iceberg|character|mascot|scene|illustration|artwork|"
        r"monitor|dashboard|lab|laboratory|robot_arm|outcome|metaphor)",
        re.IGNORECASE,
    )
    for cell_id, cell in sorted(cells_by_id.items()):
        style = cell.attrib.get("style", "")
        payload = _image_payload(style) or ""
        value = _plain_text(cell.attrib.get("value", ""))
        haystack = f"{cell_id} {value}"
        if complex_re.search(haystack) and payload.startswith("data:image/svg+xml"):
            failures.append(
                f"{cell_id} appears to be a complex visual but uses SVG; use a PNG crop "
                "unless the user explicitly requested vector editability"
            )
    return failures


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_drawio.py path/to/file.drawio", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing: {path}", file=sys.stderr)
        return 1

    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid XML: {exc}", file=sys.stderr)
        return 1

    cells = root.findall(".//mxCell")
    vertices = root.findall(".//mxCell[@vertex='1']")
    edges = root.findall(".//mxCell[@edge='1']")
    cells_by_id = {c.attrib.get("id", ""): c for c in cells if c.attrib.get("id")}
    images = [
        c for c in cells
        if "shape=image" in c.attrib.get("style", "") or "image=" in c.attrib.get("style", "")
    ]
    text_cells = [c for c in vertices if c.attrib.get("value")]

    raw_html_leaks = []
    for c in cells:
        value = c.attrib.get("value", "")
        if "&lt;font" in value or "font style" in value:
            raw_html_leaks.append(c.attrib.get("id", "<no-id>"))

    print(f"path: {path}")
    print(f"cells: {len(cells)}")
    print(f"vertices: {len(vertices)}")
    print(f"edges: {len(edges)}")
    print(f"image/svg cells: {len(images)}")
    print(f"text cells: {len(text_cells)}")
    if raw_html_leaks:
        print(f"warning: possible raw HTML/font leaks in cells: {', '.join(raw_html_leaks)}")

    layout_failures = []
    model = root.find(".//mxGraphModel")
    if model is not None:
        page_width = _float_attr(model, "pageWidth")
        page_height = _float_attr(model, "pageHeight")
        vertices_with_geo = []
        max_x = 0.0
        max_y = 0.0
        for cell in vertices:
            geo = _geometry(cell)
            if geo is None:
                continue
            vertices_with_geo.append((cell, geo))
            max_x = max(max_x, geo[0] + geo[2])
            max_y = max(max_y, geo[1] + geo[3])

        if page_width and page_height and max_x <= page_width + 2.0 and max_y <= page_height + 2.0:
            page_geo = (0.0, 0.0, page_width, page_height)
            for cell, geo in vertices_with_geo:
                cell_id = cell.attrib.get("id", "<no-id>")
                if geo[2] == 0 and geo[3] == 0:
                    continue
                if not _inside(geo, page_geo, tolerance=2.0):
                    layout_failures.append(
                        f"{cell_id} is outside page: "
                        f"cell=({geo[0]:.1f},{geo[1]:.1f},{geo[2]:.1f},{geo[3]:.1f}) "
                        f"page=({page_width:.1f},{page_height:.1f})"
                    )
        elif page_width and page_height:
            print(
                "warning: pageWidth/pageHeight smaller than content bounding box; "
                "skipping page containment check"
            )

    layout_failures.extend(_semantic_containment_failures(cells_by_id))
    layout_failures.extend(_estimated_text_failures(vertices))
    layout_failures.extend(_duplicate_icon_failures(cells_by_id))
    layout_failures.extend(_image_encoding_failures(cells_by_id))
    layout_failures.extend(_complex_visual_svg_failures(cells_by_id))
    if layout_failures:
        print("layout failures:")
        for failure in layout_failures:
            print(f"- {failure}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
