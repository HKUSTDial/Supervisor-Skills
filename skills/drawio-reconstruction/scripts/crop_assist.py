#!/usr/bin/env python3
import argparse
import json
import math
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw


def parse_box(value):
    parts = [int(float(part.strip())) for part in value.replace(" ", "").split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("expected x,y,w,h")
    x, y, w, h = parts
    if w <= 0 or h <= 0:
        raise argparse.ArgumentTypeError("roi width/height must be positive")
    return x, y, w, h


def parse_point(value):
    parts = [int(float(part.strip())) for part in value.replace(" ", "").split(",")]
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("expected x,y")
    return parts[0], parts[1]


def parse_boxes(values):
    return [parse_box(value) for value in values or []]


def clamp_box(box, width, height):
    x, y, w, h = box
    x1 = max(0, min(width, x))
    y1 = max(0, min(height, y))
    x2 = max(0, min(width, x + w))
    y2 = max(0, min(height, y + h))
    return x1, y1, max(1, x2 - x1), max(1, y2 - y1)


def median_color(pixels):
    rs = sorted(p[0] for p in pixels)
    gs = sorted(p[1] for p in pixels)
    bs = sorted(p[2] for p in pixels)
    mid = len(pixels) // 2
    return rs[mid], gs[mid], bs[mid]


def estimate_background(image):
    width, height = image.size
    border = max(4, min(16, min(width, height) // 15))
    samples = []
    for y in range(height):
        for x in range(width):
            if x < border or y < border or x >= width - border or y >= height - border:
                samples.append(image.getpixel((x, y))[:3])
    return median_color(samples)


def color_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))


def make_foreground_mask(image, background, threshold):
    width, height = image.size
    mask = [bytearray(width) for _ in range(height)]
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))[:3]
            mx = max(r, g, b)
            mn = min(r, g, b)
            sat = mx - mn
            dark = mx < 210
            colored = sat > 28 and mx < 248
            far = color_distance((r, g, b), background) > threshold
            if far and (dark or colored):
                mask[y][x] = 1
    return mask


def components(mask):
    height = len(mask)
    width = len(mask[0]) if height else 0
    seen = [bytearray(width) for _ in range(height)]
    out = []
    for sy in range(height):
        for sx in range(width):
            if not mask[sy][sx] or seen[sy][sx]:
                continue
            q = deque([(sx, sy)])
            seen[sy][sx] = 1
            area = 0
            x1 = x2 = sx
            y1 = y2 = sy
            while q:
                x, y = q.popleft()
                area += 1
                x1 = min(x1, x)
                x2 = max(x2, x)
                y1 = min(y1, y)
                y2 = max(y2, y)
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < width and 0 <= ny < height and mask[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = 1
                        q.append((nx, ny))
            out.append(
                {
                    "bbox": [x1, y1, x2 - x1 + 1, y2 - y1 + 1],
                    "area": area,
                    "centroid": [(x1 + x2) / 2.0, (y1 + y2) / 2.0],
                }
            )
    return out


def component_distance(a, b):
    ax, ay, aw, ah = a["bbox"]
    bx, by, bw, bh = b["bbox"]
    dx = max(0, max(ax, bx) - min(ax + aw, bx + bw))
    dy = max(0, max(ay, by) - min(ay + ah, by + bh))
    return math.hypot(dx, dy)


def component_point_distance(component, point):
    x, y, w, h = component["bbox"]
    px, py = point
    dx = max(0, x - px, px - (x + w))
    dy = max(0, y - py, py - (y + h))
    return math.hypot(dx, dy)


def filter_components(comps, roi_size):
    width, height = roi_size
    roi_area = width * height
    min_area = max(12, int(roi_area * 0.0007))
    min_dim = max(5, int(min(width, height) * 0.018))
    kept = []
    rejected = []
    for comp in comps:
        x, y, w, h = comp["bbox"]
        area = comp["area"]
        aspect = max(w / max(h, 1), h / max(w, 1))
        fill = area / max(w * h, 1)
        long_rule = aspect > 12 and fill < 0.35
        tiny = area < min_area and max(w, h) < min_dim
        if tiny or long_rule:
            comp["reject_reason"] = "tiny" if tiny else "long_thin"
            rejected.append(comp)
        else:
            kept.append(comp)
    return kept, rejected


def bbox_union(comps):
    if not comps:
        return None
    x1 = min(c["bbox"][0] for c in comps)
    y1 = min(c["bbox"][1] for c in comps)
    x2 = max(c["bbox"][0] + c["bbox"][2] for c in comps)
    y2 = max(c["bbox"][1] + c["bbox"][3] for c in comps)
    return [x1, y1, x2 - x1, y2 - y1]


def expand_box(box, pad, width, height):
    x, y, w, h = box
    x1 = max(0, int(round(x - pad)))
    y1 = max(0, int(round(y - pad)))
    x2 = min(width, int(round(x + w + pad)))
    y2 = min(height, int(round(y + h + pad)))
    return [x1, y1, max(1, x2 - x1), max(1, y2 - y1)]


def intersects(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


def overlap_area(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    x1 = max(ax, bx)
    y1 = max(ay, by)
    x2 = min(ax + aw, bx + bw)
    y2 = min(ay + ah, by + bh)
    if x2 <= x1 or y2 <= y1:
        return 0
    return (x2 - x1) * (y2 - y1)


def to_source_box(roi, local_box):
    rx, ry, _, _ = roi
    x, y, w, h = local_box
    return [rx + x, ry + y, w, h]


def choose_seed(kept, anchor):
    if not kept:
        return None
    if anchor is not None:
        return min(kept, key=lambda c: component_point_distance(c, anchor))
    return max(kept, key=lambda c: c["area"])


def cluster_from_seed(kept, seed, max_gap):
    cluster = [seed]
    changed = True
    while changed:
        changed = False
        for comp in kept:
            if comp in cluster:
                continue
            if min(component_distance(comp, existing) for existing in cluster) <= max_gap:
                cluster.append(comp)
                changed = True
    return cluster


def crop_candidate(image, box):
    x, y, w, h = box
    return image.crop((x, y, x + w, y + h))


def draw_preview(roi_image, candidates, kept, rejected, out_path):
    preview = roi_image.convert("RGB")
    draw = ImageDraw.Draw(preview)
    for comp in rejected:
        x, y, w, h = comp["bbox"]
        draw.rectangle((x, y, x + w, y + h), outline="#cccccc", width=1)
    for comp in kept:
        x, y, w, h = comp["bbox"]
        draw.rectangle((x, y, x + w, y + h), outline="#54a24b", width=1)
    colors = ["#ff3b30", "#007aff", "#ff9500", "#af52de"]
    for index, cand in enumerate(candidates):
        x, y, w, h = cand["local_box"]
        color = colors[index % len(colors)]
        draw.rectangle((x, y, x + w, y + h), outline=color, width=3)
        draw.text((x + 4, y + 4), str(index + 1), fill=color)
    preview.save(out_path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate code-assisted crop candidates for complex diagram icons."
    )
    parser.add_argument("image", help="Source reference image")
    parser.add_argument("--roi", required=True, type=parse_box, help="Rough ROI as x,y,w,h in source pixels")
    parser.add_argument("--anchor", type=parse_point, help="Optional target point as x,y in source pixels")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Optional source-space exclusion box x,y,w,h for neighboring text/bullets/rules. Can repeat.",
    )
    parser.add_argument("--output-dir", required=True, help="Directory for crop candidates")
    parser.add_argument("--name", default="crop", help="Output filename prefix")
    parser.add_argument("--threshold", type=float, default=26.0, help="Foreground/background color distance")
    parser.add_argument("--padding", type=float, default=0.07, help="Safe padding ratio around foreground bbox")
    args = parser.parse_args()

    image_path = Path(args.image)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    source = Image.open(image_path).convert("RGB")
    roi = clamp_box(args.roi, *source.size)
    rx, ry, rw, rh = roi
    excludes = []
    for box in parse_boxes(args.exclude):
        ex, ey, ew, eh = box
        local = [ex - rx, ey - ry, ew, eh]
        x1 = max(0, local[0])
        y1 = max(0, local[1])
        x2 = min(rw, local[0] + local[2])
        y2 = min(rh, local[1] + local[3])
        if x2 > x1 and y2 > y1:
            excludes.append([x1, y1, x2 - x1, y2 - y1])
    roi_image = source.crop((rx, ry, rx + rw, ry + rh))
    local_anchor = None
    if args.anchor is not None:
        local_anchor = (args.anchor[0] - rx, args.anchor[1] - ry)

    background = estimate_background(roi_image)
    mask = make_foreground_mask(roi_image, background, args.threshold)
    comps = components(mask)
    kept, rejected = filter_components(comps, roi_image.size)
    if excludes:
        filtered = []
        for comp in kept:
            box = comp["bbox"]
            area = box[2] * box[3]
            excluded_area = sum(overlap_area(box, ex) for ex in excludes)
            if excluded_area / max(area, 1) > 0.18:
                comp["reject_reason"] = "excluded_region"
                rejected.append(comp)
            else:
                filtered.append(comp)
        kept = filtered

    seed = choose_seed(kept, local_anchor)
    if seed is None:
        print("no foreground components found")
        return 1

    max_gap = max(10, int(min(rw, rh) * 0.14))
    cluster = cluster_from_seed(kept, seed, max_gap)
    cluster_box = bbox_union(cluster)
    all_box = bbox_union(kept)
    base_pad = max(6, int(round(max(cluster_box[2], cluster_box[3]) * args.padding)))

    raw_candidates = [
        ("target_pad", expand_box(cluster_box, base_pad, rw, rh), cluster),
        ("target_tight", expand_box(cluster_box, max(4, int(base_pad * 0.55)), rw, rh), cluster),
    ]
    if all_box and all_box != cluster_box:
        all_pad = max(6, int(round(max(all_box[2], all_box[3]) * args.padding)))
        raw_candidates.append(("all_foreground", expand_box(all_box, all_pad, rw, rh), kept))

    seen_boxes = set()
    candidates = []
    for label, local_box, members in raw_candidates:
        box_key = tuple(local_box)
        if box_key in seen_boxes:
            continue
        seen_boxes.add(box_key)
        source_box = to_source_box(roi, local_box)
        reject_hits = [
            c for c in rejected if intersects(local_box, c["bbox"]) and c.get("area", 0) > 8
        ]
        touches_roi_edge = (
            local_box[0] <= 0
            or local_box[1] <= 0
            or local_box[0] + local_box[2] >= rw
            or local_box[1] + local_box[3] >= rh
        )
        cand = {
            "label": label,
            "local_box": local_box,
            "source_box": source_box,
            "member_count": len(members),
            "rejected_component_hits": len(reject_hits),
            "warnings": [],
        }
        if touches_roi_edge:
            cand["warnings"].append("candidate touches ROI edge; rough ROI may be too tight")
        if reject_hits:
            cand["warnings"].append("candidate includes rejected small/line components; inspect for bullets/text")
        candidates.append(cand)

    for index, cand in enumerate(candidates, start=1):
        crop_path = out_dir / f"{args.name}_{index}_{cand['label']}.png"
        crop_candidate(source, cand["source_box"]).save(crop_path)
        cand["file"] = str(crop_path)

    preview_path = out_dir / f"{args.name}_preview.png"
    draw_preview(roi_image, candidates, kept, rejected, preview_path)

    result = {
        "image": str(image_path.resolve()),
        "roi": list(roi),
        "anchor": list(args.anchor) if args.anchor else None,
        "exclude": excludes,
        "background_rgb": list(background),
        "component_count": len(comps),
        "kept_component_count": len(kept),
        "rejected_component_count": len(rejected),
        "preview": str(preview_path),
        "candidates": candidates,
    }
    json_path = out_dir / f"{args.name}_candidates.json"
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(f"preview: {preview_path}")
    print(f"json: {json_path}")
    for index, cand in enumerate(candidates, start=1):
        warnings = "; ".join(cand["warnings"]) if cand["warnings"] else "ok"
        print(f"{index}. {cand['label']} source_box={cand['source_box']} {warnings}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
