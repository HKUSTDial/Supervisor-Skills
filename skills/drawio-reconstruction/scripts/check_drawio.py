#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import re


def _file_header_failures(data):
    """Reject byte prefixes that Draw.io Desktop cannot identify reliably."""
    failures = []
    if not data:
        return ["file is empty"]
    if data.startswith(b"\xef\xbb\xbf"):
        failures.append("UTF-8 BOM is not allowed; write plain UTF-8")
    elif data[:1] != b"<":
        failures.append(
            "file must begin at byte 0 with '<' (XML declaration or <mxfile>); "
            "remove leading whitespace or other bytes"
        )
    return failures


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


def _parent_containment_failures(cells_by_id):
    """Check explicit mxGraph parent/child geometry without assuming cell names."""
    failures = []
    for cell_id, cell in cells_by_id.items():
        if cell.attrib.get("vertex") != "1":
            continue
        parent_id = cell.attrib.get("parent")
        if parent_id in (None, "0", "1"):
            continue
        parent = cells_by_id.get(parent_id)
        if parent is None or parent.attrib.get("vertex") != "1":
            continue
        child_geo = _geometry(cell)
        parent_geo = _geometry(parent)
        if child_geo is None or parent_geo is None:
            continue
        parent_local = (0.0, 0.0, parent_geo[2], parent_geo[3])
        if not _inside(child_geo, parent_local, tolerance=2.0):
            failures.append(
                f"{cell_id} is outside explicit parent {parent_id}: "
                f"child-local=({child_geo[0]:.1f},{child_geo[1]:.1f},"
                f"{child_geo[2]:.1f},{child_geo[3]:.1f}) "
                f"parent-size=({parent_geo[2]:.1f},{parent_geo[3]:.1f})"
            )
    return failures


def _image_payload(style):
    for part in style.split(";"):
        if part.startswith("image="):
            return part[len("image="):]
    return None


def _image_encoding_failures(cells_by_id):
    failures = []
    for cell_id, cell in sorted(cells_by_id.items()):
        style = cell.attrib.get("style", "")
        if re.search(
            r"(?:^|;)image=data:image/[a-z0-9.+-]+;base64,",
            style,
            re.IGNORECASE,
        ):
            failures.append(
                f"{cell_id} raster data URL contains a raw MIME semicolon; "
                "encode it as %3B so Draw.io does not split the image style"
            )
        payload = _image_payload(style)
        if not payload:
            continue
        if payload.startswith("data:image/svg+xml") and "#" in payload:
            failures.append(
                f"{cell_id} SVG data URL contains raw '#'; encode colors as %23"
            )
    return failures


def _edge_route_points(edge_geometry):
    """Return actual edge endpoints/waypoints, excluding label offsets."""
    for point in edge_geometry.findall("mxPoint"):
        if point.attrib.get("as") in {"sourcePoint", "targetPoint"}:
            yield point
    for points in edge_geometry.findall("Array[@as='points']"):
        yield from points.findall("mxPoint")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: check_drawio.py path/to/file.drawio", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing: {path}", file=sys.stderr)
        return 1

    data = path.read_bytes()
    header_failures = _file_header_failures(data)
    if header_failures:
        print("file-header failures:")
        for failure in header_failures:
            print(f"- {failure}")
        return 1

    try:
        root = ET.fromstring(data.decode("utf-8"))
    except Exception as exc:
        print(f"invalid XML: {exc}", file=sys.stderr)
        return 1

    if root.tag != "mxfile":
        print(f"invalid Draw.io root element: expected mxfile, got {root.tag}", file=sys.stderr)
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

        if page_width and page_height:
            page_geo = (0.0, 0.0, page_width, page_height)
            for cell, geo in vertices_with_geo:
                cell_id = cell.attrib.get("id", "<no-id>")
                if geo[2] == 0 and geo[3] == 0:
                    continue
                if not _inside(geo, page_geo, tolerance=0.0):
                    layout_failures.append(
                        f"{cell_id} is outside page: "
                        f"cell=({geo[0]:.1f},{geo[1]:.1f},{geo[2]:.1f},{geo[3]:.1f}) "
                        f"page=({page_width:.1f},{page_height:.1f})"
                    )
            for edge in edges:
                edge_id = edge.attrib.get("id", "<no-id>")
                edge_geo = edge.find("mxGeometry")
                if edge_geo is None:
                    continue
                for point in _edge_route_points(edge_geo):
                    if "x" not in point.attrib or "y" not in point.attrib:
                        continue
                    x = _float_attr(point, "x")
                    y = _float_attr(point, "y")
                    if not (0.0 <= x <= page_width and 0.0 <= y <= page_height):
                        layout_failures.append(
                            f"{edge_id} route point is outside page: "
                            f"point=({x:.1f},{y:.1f}) "
                            f"page=({page_width:.1f},{page_height:.1f})"
                        )

    layout_failures.extend(_parent_containment_failures(cells_by_id))
    layout_failures.extend(_image_encoding_failures(cells_by_id))
    if layout_failures:
        print("layout failures:")
        for failure in layout_failures:
            print(f"- {failure}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
