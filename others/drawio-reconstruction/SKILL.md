---
name: drawio-reconstruction
description: "Reconstructs reference images into high-fidelity, editable Draw.io files with rendered previews: native Draw.io elements carry text and structure, SVG covers simple icons that match the reference, and cropped or transparent PNGs preserve complex visuals. Use when the user wants a diagram image, research figure, architecture diagram, slide, UI screenshot, or image folder turned into `.drawio` XML; batch requests use a manifest with bounded parallelism when available and a full-fidelity serial fallback otherwise."
---

# Draw.io Reconstruction

Use this skill for high-quality reconstruction of diagram images into `.drawio` files.

## Helper Script Location

Resolve `SKILL_DIR` to the absolute directory containing this `SKILL.md` before running any bundled helper. Use the resolved skill location provided by the runtime; never assume the skill is installed under `~/.codex`, `~/.agents`, or any other fixed directory.

All commands below use `$SKILL_DIR` to mean that resolved absolute directory.

## Fidelity Contract

The primary goal is visual fidelity to the reference image. Editability is secondary.

Do not treat semantic equivalence as success. A generic icon, generic curve, generic font size, approximate panel, or approximate background is a defect when the reference has a specific visual style.

Script checks only prove technical validity. A diagram is not complete merely because `.drawio` opens, exports, or passes `check_drawio.py` / `batch_verify.py`. Completion requires visual comparison against the reference at full size.

Work only in the target directory or target files named by the user. Do not repair, overwrite, or improve neighboring diagrams because they look related. If the requested target is ambiguous, inspect and report the ambiguity before editing.

Never silently rewrite the user's content. If the user asks for larger fonts or a more professional PPT style, first distinguish:

- **Layout-only refinement**: increase font size, resize boxes, improve spacing, align elements, adjust line breaks without changing words.
- **Content compression**: shorten sentences, remove details, rewrite labels. Ask permission before doing this.

## Batch Folder Workflow

Use this workflow when the user provides a directory of images or asks for batch reconstruction.

### Batch Intent And Scheduling

Before opening images for detailed visual analysis, decide whether the request is a batch reconstruction task:

- Treat the request as batch reconstruction when it names a folder, multiple image files, a glob/pattern, or any target that resolves to **2 or more image entries**.
- Create and review the manifest before detailed per-image work begins.
- When sub-agent tooling is available and useful, use a bounded worker pool no larger than the available concurrency and the number of pending images. Give each active worker exactly one image and an exclusive write set for that image's `.drawio`, exported `.png`, audit file, and private asset/crop directory. Reuse a free slot for the next image instead of trying to start every worker at once.
- When sub-agent tooling is unavailable, disabled, capacity-limited, or unnecessary for a small batch, process entries serially in manifest order. Preserve the same inventory, reconstruction, export, check, and visual-audit requirements.
- Tell the user about scheduling limitations only when they materially affect timing or delivery. Do not block a valid batch solely because parallel execution is unavailable.
- The coordinating agent may inspect thumbnails or file metadata to confirm scope, naming, orientation, and shared style constraints before choosing the schedule.

1. Identify the input directory, output directory, naming convention, and overwrite policy.
2. Create a batch manifest:

   ```bash
   python "$SKILL_DIR/scripts/batch_manifest.py" path/to/images --output-dir path/to/output --write
   ```

3. Review the manifest before editing. Process only entries in the manifest unless the user expands scope.
4. For each image, define the expected `<stem>.drawio`, `<stem>.png`, and lightweight `<stem>.audit.md` outputs in the target output directory.
5. Choose a bounded parallel schedule or a serial schedule:
   - Assign exclusive output files for each active entry.
   - Tell workers they are not alone in the codebase and must not revert or edit other workers' outputs.
   - Require every entry to follow the same full workflow as a standalone single-image task. Batch mode is only a scheduling strategy; it does not reduce fidelity, inventory, reconstruction, export, check, or visual-audit requirements.
   - Apply this quality gate to every entry: produce `.drawio`, `.png`, and `<stem>.audit.md`; create the complete visible-element inventory; classify non-text visuals; use crops/SVG/native elements according to the normal medium rules; run required checks/exports; visually compare the exported preview against the reference; mark unresolved visual defects instead of claiming completion.
   - Keep final batch verification, visual inspection, audit review, and the user-facing completion report with the coordinating agent.
6. After reconstruction, run batch verification:

   ```bash
   python "$SKILL_DIR/scripts/batch_verify.py" path/to/output/drawio_batch_manifest.json
   ```

7. Open every exported preview and compare it with the reference. Do not trust worker completion or script success alone.
8. Report completed entries, skipped entries, failures, and any images that need review.

Default batch outputs:

- `drawio_batch_manifest.json`
- `<image-stem>.drawio`
- `<image-stem>.png`
- `<image-stem>.audit.md`

Do not overwrite existing outputs unless the user explicitly asks. If an output exists, either skip it or create a clearly named revision such as `<stem>-v2.drawio`.

## Mandatory Reference Inventory

Before reconstructing each image, create a visible-element inventory. For complex or batch work, write it to `<stem>.audit.md`; for a very small single image, maintain it in working notes and still perform the same checks.

The inventory must cover every visible region and element:

- canvas size, background, grid, texture, gradients, shadows, page boundary
- title, subtitle, section headers, footer, page number
- panels, cards, containers, dividers, badges, numbered markers
- every text block and label
- every icon, artwork, screenshot, logo, chart, thumbnail, or decorative visual
- every arrow, curve, connector, loop, bracket, dashed path, and arrowhead
- all spacing relationships that define the layout

Each inventory item must include:

- `id`
- approximate region or bbox
- content / visual description
- selected medium: native / SVG / crop / generated-cleanup
- style notes: color, stroke, font, size, shadow, curve geometry, padding
- status: pending / done / needs-fix / accepted

Do not begin final delivery until all visible inventory items are accepted or explicitly reported as unresolved.

## Reconstruction Strategy

Use the best medium for visual fidelity. Do not globally default all non-text visuals to screenshots, and do not globally redraw all visuals as SVG. The deciding question is: which method best matches the reference after export?

Prefer **Draw.io native elements** for:

- editable text, headings, labels, chips, callouts
- boxes, panels, dividers, simple tables, simple charts, badges
- structural arrows/connectors when native geometry can match the reference
- repeated layout structure that should remain easy to edit

Use **PNG crop / screenshot by default** for:

- complex icons, detailed symbols, decorative illustrations, and mixed-object visuals
- style-specific icon families where a generic SVG would not match the reference
- visual metaphors and scene-like artwork: icebergs, people, environments, dashboards, monitors, lab scenes, rooms, landscapes, workflow scenes
- real UI screenshots, phone/dashboard strips, app thumbnails, evidence screenshots, dense mini-diagrams
- people, cartoon characters, expressive faces, hands, body poses, or human-computer scenes
- anything where exact visual fidelity matters more than editability
- any non-text visual that would take many paths, gradients, masks, or manual approximations to redraw
- any visual element where an SVG/native attempt would simplify, omit, or visibly distort important details

Use **SVG/native only** for:

- simple clean icons whose reference shape and style can be matched, not merely named semantically
- icons with simple outline/fill geometry, 1-2 main colors, no essential texture, no dense internal detail, and a clear reference style that can be reproduced
- repeated simple icon families where SVG can preserve the same stroke width, proportions, colors, and scale as the reference
- small source icons where the crop would be blurry or background-contaminated and a shape-level SVG match is feasible
- elements where the user explicitly needs vector editability

Do not use a generic standard icon just because the semantic label matches. Database, chart, document, target, brain, robot, phone, clipboard, cursor, lightbulb, molecule, beaker, monitor, and similar icons still require a shape/style check against the reference.

## Medium Decision Rules

Classify each visual element before reconstructing it.

1. If it is text or structure, use Draw.io native elements.
2. If it is a visual element with distinctive reference style, dense detail, gradients, shadows, multi-object composition, or scene/metaphor content, crop it unless the user explicitly requests vector editability.
3. If it is a simple clean icon, use SVG/native only when the SVG can match the reference's shape, stroke, proportions, fill, and visual family.
4. If an SVG would be semantically correct but visually generic, do not use it. Crop the reference or create a closer shape-level SVG.
5. If a crop is blurry, contaminated, or has a visible rectangle, first fix the crop/background. Switch to SVG only if the visual is simple and the SVG match is closer to the reference than the crop.
6. If crop background seams are visible, try transparent PNG cleanup or match the crop background to the containing panel.
7. If ordinary cleanup leaves halos, ragged edges, watermarks, JPEG blocks, or mismatched panels, place the crop on a same-color background block, crop tighter, or use an available image editing/generation tool to repair only the background.
8. If neither crop nor SVG/native is acceptable, mark the item `needs-fix` in the audit instead of silently substituting a poor drawing.

Blocking medium defects:

- generic substitute icon where the reference has a style-specific icon
- complex visual redrawn as simplified SVG without a user-requested vector-editability reason
- blurry crop of a simple icon when a clean shape-level SVG would match better
- cropped complex artwork with visible background seams, halos, missing strokes, clipped shadows, or unrelated neighboring text/borders
- missing prominent icon, decorative mark, or detailed visual

## Icon Reconstruction Discipline

Before writing icon SVGs or embedding crops, make a role-to-symbol map from the reference. For example:

- Planning: brain, checklist, planning symbol
- Tool Use: wrench, crossed tools, terminal, tool symbol
- Memory: database cylinder, storage, memory symbol
- Verification: shield, checkmark, audit, validation symbol
- Evidence cards: schema/table, logs/document, execution tree/plan, metrics/gauge

For each map entry:

- Use a source-image crop for complex, style-specific, or detailed symbols.
- Use a distinct SVG or native Draw.io symbol only for simple clean icons that can match the reference style.
- Keep stroke width, color, proportions, and size consistent with the reference, not with a generic icon set.
- Do not copy one icon and only change its position or label.
- Do not use a generic placeholder icon unless the reference itself uses that same repeated placeholder.
- If a symbol is not simple and clean, crop that specific symbol from the reference instead of substituting an unrelated SVG.

After creating or editing icons, run `check_drawio.py`. Duplicate image payloads in evidence icons, core-strip icons, workflow-step icons, or outcome-row icons are blocking failures unless the reference intentionally repeats the same symbol.

## Screenshot Crop Rules

Use screenshots/PNG crops when:

- the illustration is too complex to redraw efficiently
- exact visual style matters more than editability
- SVG attempts still look poor or generic
- the user supplied or approved a good crop
- the visual is a complex icon whose details would be lost in a hand-drawn SVG
- the visual is a real UI screenshot, phone strip, dashboard thumbnail, dense evidence artifact, person, scene, or visual metaphor

When using screenshots:

- Avoid screenshots for editable text or structural layout.
- Crop around the target foreground artwork, not around the whole surrounding region.
- Start from a rough ROI, identify the foreground bbox, then add modest safe padding.
- Use the crop helper when possible:

  ```bash
  python "$SKILL_DIR/scripts/crop_assist.py" reference.png --roi x,y,w,h --anchor x,y --exclude x,y,w,h --output-dir crops --name icon_name
  ```

- Inspect the generated preview and candidates visually before embedding a crop. The script proposes bounds; the model still decides which candidate best matches the reference.
- `crop_assist.py` requires Pillow. If Pillow is unavailable, request approval before changing the environment, then install the bundled optional dependency with `python -m pip install -r "$SKILL_DIR/requirements.txt"`. Do not silently skip crop inspection.
- Use `--exclude` boxes for nearby elements that are inside the rough ROI but not part of the target artwork, especially bullets, body text, title rules, numbered badges, panel borders, and divider lines.
- Safe padding should preserve full strokes, arrowheads, shadows, antialiasing, and immediate intentional whitespace. It should not expand into general empty space.
- Do not crop tightly to visible strokes unless tight cropping is required to avoid neighboring content. A clipped stroke, cut-off arrowhead, missing shadow, or artwork touching the crop edge is a blocking defect.
- Do not include neighboring bullets, labels, title rules, card borders, divider lines, or unrelated same-color marks. If more padding would pull in a neighbor, use the tighter valid candidate and handle the background with transparency or color matching.
- Prefer transparent PNG when the surrounding panel/background is not uniform.
- If transparency is not possible or cleanup creates halos, place the crop on a same-color background block.
- If the crop background color does not match the Draw.io panel, crop tighter, remove the background, recolor/match the crop background, or set the containing panel/background to match.
- If the crop is complex and still has background mismatch after ordinary cleanup, use an available image editing/generation tool to repair or neutralize only the background; do not alter the semantic foreground.
- Check exported PNG for visible seams, antialiasing halos, jagged transparency, blur, or mismatched background. Do not leave visible rectangular crop seams.

## Curves And Arrows

For every arrow or curve, match the reference before choosing implementation.

Create an arrow inventory:

- source element and target element
- start/end anchors
- direction
- line type: solid, dashed, dotted, curved, vertical, horizontal, loop
- stroke width, color, arrowhead type and size
- bend points, corner radius, and whether the path passes in front of or behind panels
- semantic role: workflow transition, feedback loop, evidence support, callout, decorative cue

Implementation order:

1. Native Draw.io connectors for structural connectors when they can match the reference.
2. SVG path for special braces, curved arrows, loop arrows, rounded return paths, or decorative arrows that native Draw.io cannot match.
3. PNG crop only for highly specific non-editable decorative marks.

Large loop arrows, dashed feedback curves, and rounded return paths must match the reference path geometry. Do not replace them with approximate generic connectors.

## Typography And Layout

Extract typography from the reference image before assigning sizes:

- main title
- subtitle
- section titles
- card titles
- card bodies
- labels/chips
- footer/page number
- icon-label pairs

For every text role, capture approximate font size, weight, color, line height, alignment, and available box size. Do not apply SIGMOD running-example font baselines unless the reference is explicitly a SIGMOD-style running example.

Treat every text change as a box-model change:

`text -> text box -> card/row -> containing panel -> neighboring layout`.

Hard failures:

- text visually larger but the background card/panel was not resized
- text box height smaller than rendered text height
- text touches borders, overlaps icons, or extends outside rows/cards
- awkward line breaks not present in the reference when space is available
- parent cards fit text but no longer fit inside the panel
- footer or slide boundary is pushed into content

## Default Workflow

1. Identify the reference image and target output directory.
2. Create or update the batch manifest when processing folders or multiple images.
3. For each image, create the reference inventory and style token notes.
4. Rebuild the diagram with native Draw.io elements wherever feasible for text and structure.
5. Classify every non-text visual with the medium decision rules.
6. Use source-image crops or transparent PNGs for complex/style-specific visuals; use SVG/native only for simple clean icons that pass shape/style matching.
7. Export a PNG preview with Draw.io CLI.
8. Run the checker. Treat any layout failure as a blocking defect, not a warning.
9. Perform a full visual audit against the reference at full size, item by item.
10. Iterate on layout, sizing, alignment, font sizes, crops, icons, and arrows until both technical checks and visual audit pass.
11. Report changed files and remaining quality risks.

Default outputs:

- `<name>.drawio`
- `<name>.png`
- `<name>.audit.md` for batch or complex reconstructions

## Mandatory Visual Audit

Before final response, compare the exported PNG against the reference at full size and explicitly check every inventory item.

Blocking defects:

- missing visible element
- generic substitute icon
- wrong icon/artwork style, stroke, scale, or internal detail
- wrong curve, loop, dashed path, arrow route, arrowhead, or connector layering
- wrong title/body font size, weight, line break, color, or alignment
- text overlap, clipping, border touching, or awkward wrapping not in the reference
- wrong panel/card size, corner radius, shadow, border, or spacing
- background mismatch, missing gradient/grid/texture, or wrong page boundary
- crop seam, blur, halo, bad transparency, wrong crop boundary, or neighboring content inside crop
- script-only pass without reference comparison
- any inventory item still marked `needs-fix`

If any item fails, continue editing. Do not present the diagram as finished.

For batch jobs, the parent agent must open every exported preview and every worker audit file before final response. Worker completion is not delivery acceptance.

## Using A User-Approved Reference Diagram

If the user provides a manually adjusted screenshot or `.drawio` file as a quality reference, use it as the style source before changing another diagram.

Prefer the `.drawio` file when available because it exposes real geometry:

- Extract font sizes by semantic role.
- Extract geometry ratios: card width/height, title/body text box heights, icon size, role-label height, evidence panel height, outcome row height, and padding.
- Apply those role-based values to the target diagram before subjective visual adjustments.
- Preserve the target diagram's wording. Use the reference for typography, spacing, icon sizing, and layout density only.
- If the reference `.drawio` has stale page metadata but exports correctly, use the content bounding box and exported PNG for validation.

## Redline Feedback

If the user provides a screenshot with red boxes or annotations:

- Treat each marked region as a blocking defect.
- Do not reinterpret the request as a new reconstruction unless asked.
- First fix containment, clipping, overflow, wrong crop, wrong icon style, wrong arrow path, and wrong typography in the marked regions.
- Preserve the user's current text and manual edits.
- If a red box marks a cartoon/illustration/visual metaphor, consider replacing SVG recreation with a crop from the reference.

## Verification

Always verify the `.drawio` after edits:

```bash
python "$SKILL_DIR/scripts/check_drawio.py" path/to/file.drawio
python "$SKILL_DIR/scripts/export_drawio.py" path/to/file.drawio path/to/preview.png
```

For batch jobs:

```bash
python "$SKILL_DIR/scripts/batch_manifest.py" path/to/images --output-dir path/to/output --write
python "$SKILL_DIR/scripts/batch_verify.py" path/to/output/drawio_batch_manifest.json
```

The checker catches XML validity and common containment failures; it is not a substitute for visual inspection. After export, inspect the rendered PNG against the reference before final response.

## Final Response

Keep the final response short:

- Link to the `.drawio` file.
- Link to the rendered `.png` preview.
- Mention whether crops or SVG/native elements were used for major visual elements.
- Mention any remaining manual review point, especially if visual audit items remain unresolved.
