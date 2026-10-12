---
name: drawio-reconstruction
description: Reconstructs one or more reference diagrams into high-fidelity, editable Draw.io files. Use native Draw.io elements for text and structure, SVG for simple icons, and cropped or transparent PNGs for complex visuals. Use when the user provides diagram images, research figures, architecture diagrams, slide images, UI screenshots, or image folders. Each image requires independent icon and reconstruction review passes. Batch requests begin with a manifest and one worker per image when available.
---

# Draw.io Reconstruction

Use this skill for high-quality reconstruction of diagram images into `.drawio` files.

## Fidelity Contract

The primary goal is visual fidelity to the reference image. Editability is secondary.

Do not treat semantic equivalence as success. A generic icon, generic curve, generic font size, approximate panel, or approximate background is a defect when the reference has a specific visual style.

Script checks only prove technical validity. A diagram is not complete merely because `.drawio` opens, exports, or passes `check_drawio.py` / `batch_verify.py`. Completion requires visual comparison against the reference at full size.

Quality findings are repair instructions, not a terminal delivery state. Preserve the latest valid `.drawio`, preview, and prepared assets throughout both repair loops. For every repair round, start a fresh Producer instance with the current artifacts and concrete FIX list, then start a fresh read-only Reviewer for the regenerated version. Do not rely on sending input to a completed agent: some runtimes return its cached final response without starting a new turn. Do not add a fixed review-round limit or convert a reviewer finding into a separate acceptance-manifest failure. Retry transient agent or service errors without discarding completed work. Never close, interrupt, replace, or abandon an active producer or reviewer merely because it is slow or still working; wait without a time limit and use non-destructive status checks.

## Mandatory Role Separation

These gates come before file generation and delivery. A producer may inspect its own work, but self-inspection is only a preflight check. A producer must never issue `PASS` for an artifact it created, and a coordinator must not substitute its own judgment for a required independent reviewer.

Record the producer and reviewer literal task/thread/agent identifiers in `<stem>.audit.md`; a role label such as `main coordinator` is not an identifier. Take both identifiers from the agent-launch metadata returned to the coordinator, never from an Agent's invented role label or self-description. Before accepting either gate, the coordinator must verify that the producer identifier and reviewer identifier are present and different. If identity cannot be verified, review remains pending. A reviewer that recognizes it created or edited a submitted artifact must refuse review.

Keep the audit lightweight and append one row per review round: `phase | artifact_version | producer_id | reviewer_id | verdict | fix_ids | artifact_sha256`. Increment `artifact_version` after every repair, use literal unique agent identifiers, and bind the verdict to hashes of the reviewed files. The Producer returns `READY_FOR_REVIEW` with its id, version, and hashes. The read-only Reviewer returns a signed result with its own id, the same version and full hash set, and `PASS` or `FIX`; it never edits the audit. The coordinator copies that result verbatim into the row. Every producer and reviewer identifier in the audit must be globally unique across all rounds and phases; never reuse a completed agent.

0. **Reference immutability gate:** Resolve the reference image path before writing anything and choose a distinct preview path. Never export, copy, or write any output over the reference image. Use `<stem>_preview.png` by default, including when the reference itself is a PNG. Give reviewers the unchanged reference and the separate preview.
1. **Icon production gate:** If the image contains icons, start exactly one clean Icon Producer Agent for that image **before creating or editing any icon asset or `.drawio` file**. The reconstruction producer must not prepare the icons itself.
2. **Icon review gate:** After icon preparation, start a fresh Icon Review Agent that did not create the assets and cannot edit them. Only this reviewer may return `PASS`. Every `FIX` starts a fresh Icon Repair Producer with the current assets and FIX list, followed by a new read-only Icon Reviewer instance.
3. **Reconstruction production gate:** After icon review passes, start a fresh Reconstruction Producer that did not prepare or review the icon assets. It builds the complete diagram, exports the preview, and returns `READY_FOR_REVIEW`, never `PASS`.
4. **Reconstruction review gate:** After the complete preview is exported, start a fresh Reconstruction Review Agent that did not build or edit the diagram. Only this reviewer may return final `PASS`. Every `FIX` starts a fresh Reconstruction Repair Producer with the current `.drawio` and FIX list; it re-exports and rebuilds the placement sheet, then a new read-only Reconstruction Reviewer checks that version.

If an independent reviewer cannot be started, preserve the artifacts and report that independent review is pending. Do not let a producer self-accept and do not claim `PASS`.

Work only in the target directory or target files named by the user. Do not repair, overwrite, or improve neighboring diagrams because they look related. If the requested target is ambiguous, inspect and report the ambiguity before editing.

Never silently rewrite the user's content. If the user asks for larger fonts or a more professional PPT style, first distinguish:

- **Layout-only refinement**: increase font size, resize boxes, improve spacing, align elements, adjust line breaks without changing words.
- **Content compression**: shorten sentences, remove details, rewrite labels. Ask permission before doing this.

## Batch Folder Workflow

Use this workflow when the user provides a directory of images or asks for batch reconstruction.

### Batch Intent And Agent Gate

Before opening images for detailed visual analysis, decide whether the request is a batch reconstruction task:

- Treat the request as batch reconstruction when it names a folder, multiple image files, a glob/pattern, or any target that resolves to **2 or more image entries**.
- For **2 or more image entries**, do not start one-by-one reconstruction or detailed per-image analysis in the parent agent. Create the manifest, then immediately start sub-agents.
- Assign **one sub-agent per image** by default. Each sub-agent gets exactly one image and an exclusive write set for that image's `.drawio`, exported `.png`, audit file, and private asset/crop directory.
- The parent agent may briefly inspect thumbnails or file metadata only to confirm scope, naming, orientation, and obvious shared style constraints. It must not reconstruct or deeply audit individual images before the sub-agent split.
- If no multi-agent/subagent tool is available, report that limitation before continuing; do not silently fall back to serial reconstruction.

Parallelism is mandatory for multi-image work when sub-agent tooling is available. If the request names a folder, multiple image files, or any target that resolves to **2 or more images**, split work across sub-agents after creating the manifest. Do this even if the user does not explicitly say "parallel", "agents", or "batch". The only fallback is an environment with no multi-agent/subagent tool; in that case, report the limitation before continuing.

1. Identify the input directory, output directory, naming convention, and overwrite policy.
2. Create a batch manifest:

   ```bash
   python ~/.codex/skills/drawio-reconstruction/scripts/batch_manifest.py path/to/images --output-dir path/to/output --write
   ```

3. Review the manifest before editing. Process only entries in the manifest unless the user expands scope.
4. For each image, define the expected `<stem>.drawio`, `<stem>_preview.png`, and lightweight `<stem>.audit.md` outputs in the target output directory. The preview path must never equal the reference path.
5. When the manifest has **2 or more image entries**, immediately split manifest entries into disjoint worker-agent work sets before reconstruction begins:
   - Start one worker per image.
   - Assign each worker exclusive output files.
   - Tell workers they are not alone in the codebase and must not revert or edit other workers' outputs.
   - Each worker must follow the same full workflow required for reconstructing that image as a standalone single-image task, including both independently reviewed repair loops. Batch mode is only a scheduling strategy; it does not reduce fidelity, inventory, icon preparation, reconstruction, export, check, or visual-review requirements.
   - Give each worker this quality contract: produce `.drawio`, `<stem>_preview.png`, and `<stem>.audit.md`; create the visible-element inventory; use one Icon Producer plus a fresh Icon Reviewer; reconstruct the diagram; create the placed-icon review sheet; and use a fresh Reconstruction Reviewer.
   - The parent aggregates results and may report additional defects, but it does not replace either independent reviewer. Any parent finding starts a fresh repair Producer on the current artifacts, followed by a new independent read-only Reviewer instance.
6. After reconstruction, run batch verification:

   ```bash
   python ~/.codex/skills/drawio-reconstruction/scripts/batch_verify.py path/to/output/drawio_batch_manifest.json
   ```

7. The parent must open every exported preview and compare it with the reference. When it finds a defect, start a fresh Reconstruction Repair Producer on the current artifacts and defect list, then require a fresh independent read-only Reviewer after repair. Do not return work to a completed worker.
8. Report completed entries, skipped entries, transient retries, and any user-stopped work without discarding successful outputs from other entries.

Default batch outputs:

- `drawio_batch_manifest.json`
- `<image-stem>.drawio`
- `<image-stem>_preview.png`
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

Do not treat a `needs-fix` item as a terminal run failure. Keep the relevant repair loop active and preserve the best current artifacts until every item is accepted or the user explicitly asks to stop.

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

## Icon Preparation Repair Loop

Run this loop after the visible-element inventory identifies the icons and before full Draw.io construction. An icon is any compact non-text symbol, logo, badge artwork, pictogram, or repeated visual mark. Keep people, large scenes, screenshots, and dense illustrations in the normal crop workflow unless they function as compact icons.

1. Start exactly one clean **Icon Producer Agent per image for the first round**. Do not start one producer per icon, and never have multiple icon producers active for the same image at once.
2. Give it only the reference image, the icon portion of the inventory, approximate target display sizes and backgrounds, the private `<stem>_icons/` directory, and the medium rules in this skill.
3. Preserve the main workflow's medium decision instead of forcing screenshots. Use native Draw.io or SVG for simple badges, numbered circles, clocks, calendars, databases, targets, and other clean geometric symbols when they can match the reference. Use PNG crops for complex or style-specific artwork. A simple icon must not become a raster crop merely because an Icon Producer exists.
4. Require the Icon Producer to write:
   - one PNG or SVG file only for entries whose selected medium needs a file
   - `<stem>_icons/icons.json` with `id`, nullable `file`, `source_bbox`, `recommended_size`, `intended_background`, and `medium`
   - one or more `<stem>_icons/icons-review*.png` sheets, showing source context, the exact source bbox, and the prepared native/SVG/crop result on the intended background at actual target size and at 2x
5. Keep final page layout, text, connectors, and `.drawio` construction out of the Icon Producer's scope. Its completion response is `READY_FOR_REVIEW`, never `PASS`.
6. Never put every icon into one tall review image. Use stable-order shards of at most **8 icon rows** and keep every sheet at most 2200 px high. Use `icons-review.png` for one shard or `icons-review-001.png`, `icons-review-002.png`, ... for multiple shards. Record the complete ordered sheet list in the audit.
7. Make the evidence literal rather than decorative: an `actual` panel is pasted at 1 source pixel to 1 sheet pixel and a `2x` panel at exactly 2 sheet pixels per source pixel. Never scale either panel down to fit a fixed cell; enlarge the row/sheet or start another shard. Show a source-context panel extending beyond the bbox with the bbox outlined, so the Reviewer can see clipped continuations and neighboring text/borders. The context panel does not replace the exact-bbox panel.
8. Start a fresh **Icon Review Agent** with the unchanged reference, icon inventory, `icons.json`, and every `icons-review*.png` shard. It cannot edit files. It checks medium choice, identity, family/style, shape, stroke, color, full edges and shadows, contamination, transparency/matte seams, clarity at actual size, and duplicate reuse. Foreground artwork touching an asset edge, a continuing stroke/shadow outside the proposed source bbox, or partial neighboring text/borders is a blocking FIX unless the unchanged reference visibly clips the same artwork at that boundary.
9. Only an Icon Review Agent returns `PASS` or an itemized `FIX` keyed by icon id. Its result must include one explicit verdict for every icon id, in `icons.json` order; the reviewed id set must exactly equal the manifest id set with no omissions or duplicates. A whole-sheet PASS without this per-icon ledger is invalid. For every `FIX`, start a fresh Icon Repair Producer with exclusive access to the existing icon directory, current assets, and prior FIX list; require changed file hashes or timestamps for the requested items. Then start a new fresh read-only Icon Reviewer instance. Do not reuse any completed agent's cached response as a new production or review result.
10. Continue without a fixed round or time limit. Once the independent icon review passes, hand the assets to reconstruction. Final placement still requires independent review after embedding.

Use this compact review result format:

```text
PASS
producer_id: <literal-id-from-launch-metadata>
reviewer_id: <literal-agent-id>
artifact_version: <version-reviewed>
artifact_sha256: <complete-reviewed-hash-set>
icon_verdicts:
- <first-icon-id-in-icons.json>: PASS
- <next-icon-id-in-icons.json>: PASS
- ... one entry for every remaining icon id in exact manifest order
non_icon_fixes: none
```

or:

```text
FIX
producer_id: <literal-id-from-launch-metadata>
reviewer_id: <literal-agent-id>
artifact_version: <version-reviewed>
artifact_sha256: <complete-reviewed-hash-set>
icon_verdicts:
- <first-icon-id-in-icons.json>: PASS
- <failing-icon-id>: FIX - <visible defect>; <specific repair requested>
- ... one entry for every remaining icon id in exact manifest order
non_icon_fixes: <none or itemized full-page fixes>
```

For both formats, reject an empty ledger, a missing id, a duplicate id, an extra id, or any order different from `icons.json`. A `FIX` ledger may contain `PASS` entries for unaffected icons, but every icon must still appear exactly once. The coordinator saves the Reviewer response verbatim as `<stem>_icons/review-result-<phase>-<version>.txt`, captures workspace hashes before and after read-only review, and runs `scripts/validate_review_result.py` with the actual launch-metadata ids, version, manifest, and every reviewed artifact. A nonzero validator exit, a workspace mutation, or a missing result file invalidates the verdict; do not copy it into the accepted audit row. The coordinator must never rewrite, normalize, summarize, or create a substitute result to make validation pass; retry with a fresh Reviewer on the same immutable artifacts.

## Icon Construction Rules

Before writing icon SVGs or embedding crops, make an icon inventory from the current reference. Give every visible compact symbol its own stable id, source bounding box, intended meaning, target display size, background, and selected medium. Derive these entries only from the submitted image; do not assume a fixed diagram template or a predefined set of semantic roles.

For each map entry:

- Use a source-image crop for complex, style-specific, or detailed symbols.
- Use a distinct SVG or native Draw.io symbol only for simple clean icons that can match the reference style.
- Keep stroke width, color, proportions, and size consistent with the reference, not with a generic icon set.
- For every SVG, compute the rendered bounds of every primitive including stroke width, caps, joins, markers, filters, and shadows. All bounds must fit inside the `viewBox` with visible padding; any primitive extending outside it is a blocking preflight failure even if a full-page preview hides the clipping.
- Do not copy one icon and only change its position or label.
- Do not use a generic placeholder icon unless the reference itself uses that same repeated placeholder.
- If a symbol is not simple and clean, crop that specific symbol from the reference instead of substituting an unrelated SVG.

After creating or editing icons, run `check_drawio.py` for generic XML, Draw.io Desktop-compatible byte-zero file headers, page-boundary, explicit parent-containment, and embedded-image encoding checks. The independent Icon Reviewer must compare `icons.json` and every `icons-review*.png` shard against the reference and reject unintended asset reuse; the checker cannot infer whether repeated symbols are semantically intentional.

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
  python ~/.codex/skills/drawio-reconstruction/scripts/crop_assist.py reference.png --roi x,y,w,h --anchor x,y --exclude x,y,w,h --output-dir crops --name icon_name
  ```

- Inspect the generated preview and candidates visually before embedding a crop. The script proposes bounds; the model still decides which candidate best matches the reference.
- Use `--exclude` boxes for nearby elements that are inside the rough ROI but not part of the target artwork, especially bullets, body text, title rules, numbered badges, panel borders, and divider lines.
- Safe padding should preserve full strokes, arrowheads, shadows, antialiasing, and immediate intentional whitespace. It should not expand into general empty space.
- Do not crop tightly to visible strokes unless tight cropping is required to avoid neighboring content. A clipped stroke, cut-off arrowhead, missing shadow, or artwork touching the crop edge is a blocking defect.
- Do not include neighboring bullets, labels, title rules, card borders, divider lines, or unrelated same-color marks. If more padding would pull in a neighbor, use the tighter valid candidate and handle the background with transparency or color matching.
- Prefer transparent PNG when the surrounding panel/background is not uniform.
- If transparency is not possible or cleanup creates halos, place the crop on a same-color background block.
- If the crop background color does not match the Draw.io panel, crop tighter, remove the background, recolor/match the crop background, or set the containing panel/background to match.
- If the crop is complex and still has background mismatch after ordinary cleanup, use an available image editing/generation tool to repair or neutralize only the background; do not alter the semantic foreground.
- When embedding a raster as a data URI inside an `mxCell` style, percent-encode the MIME separator semicolon, for example `image=data:image/png%3Bbase64,...`. A raw `data:image/png;base64,...` is split by Draw.io's style parser and can export as a missing image.
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

For every text role, capture approximate font size, weight, color, line height, alignment, and available box size. Do not apply typography baselines from an unrelated diagram style; derive them from the current reference.

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
4. Classify non-text visuals and run the Icon Preparation Repair Loop when icons exist.
5. Rebuild the diagram with native Draw.io elements wherever feasible for text and structure, using the reviewed icon assets.
6. Use source-image crops or transparent PNGs for complex/style-specific visuals; use SVG/native only for simple clean icons that pass shape/style matching.
7. Export a PNG preview with Draw.io CLI and run the checker.
8. Run the Reconstruction Repair Loop on the full exported diagram.
9. Report changed files and remaining quality risks only after the loop passes or the user asks to stop.

Default outputs:

- `<name>.drawio`
- `<name>_preview.png`
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

## Reconstruction Repair Loop

Run this loop after the first complete `.drawio` and PNG preview exist.

1. The Reconstruction Producer performs technical checks and may self-audit, but its self-audit cannot produce acceptance.
2. When icons exist, require the Reconstruction Producer to create one or more `<stem>_icons/placement-review*.png` sheets from the **actual exported preview**. Use the same stable-order, at-most-8-row, at-most-2200-px-high sharding and literal 1:1/2x scale rules as icon preparation. For every icon, show both an outlined source-context panel and an outlined final-preview-context panel extending beyond their bboxes, plus exact source/final crops at actual size and 2x. These sheets must expose final background, scale, placement, clipping, surrounding text/card/border/connector collisions, and overlap; prepared assets alone are insufficient.
3. Start a fresh Reconstruction Review Agent that did not build or edit the diagram. Give it only the unchanged reference, exported preview, audit inventory, `<stem>_icons/icons.json`, and every `placement-review*.png` shard when icons exist. The reviewer cannot edit files.
4. The reviewer must inspect the full page and every placement-review row and return one explicit verdict for every icon id. The reviewed id set must exactly equal the icon manifest id set. A missing shard or id, clipped edge, wrong crop, visible matte/rectangle, wrong scale or position, border collision, neighboring partial text/border inside a crop, or connector touching/covering an icon is blocking even when it is subtle in the full-page view. Do not apply a “minor difference” exception to compact visuals.
5. Only the Reconstruction Review Agent returns `PASS` or `FIX`. In both cases it must use the same complete `icon_verdicts` ledger format and exact-order validation defined above; a `FIX` entry also states the visible mismatch and requested correction. Empty, missing, duplicate, extra, or reordered ids invalidate the whole verdict. Non-icon full-page defects are listed separately and do not replace the icon ledger.
6. For every `FIX`, start a fresh **Reconstruction Repair Producer Agent** with exclusive access to the current `.drawio`, preview, placement sheets, and FIX list. It must repair current files rather than restart from the reference.
7. Require changed hashes or timestamps for requested artifacts, re-export, rerun `check_drawio.py`, regenerate every `placement-review*.png` shard, then start a new fresh read-only Reconstruction Reviewer instance with the prior FIX list. Do not reuse any completed agent's cached response as a new production or review result.
8. Continue without a fixed round or time limit until the independent reviewer returns `PASS` or the user explicitly asks to stop. A quality finding starts another repair round; it does not authorize deletion of current deliverables.

Use the same compact result contract for reconstruction. A Producer returns `READY_FOR_REVIEW` with `producer_id`, `artifact_version`, changed paths, and SHA-256 hashes. A Reviewer returns `PASS` or `FIX` with its own `reviewer_id`, the exact `artifact_version`, the complete ordered `icon_verdicts` ledger when icons exist, and itemized non-icon fixes when applicable. Reject a verdict whose version or hashes do not match the submitted artifacts; also reject mismatched ledger ids.

For batch jobs, keep successful image outputs available while another image is being repaired or retried. Do not fail the entire batch because one image needs another round.

## Using A User-Approved Reference Diagram

If the user provides a manually adjusted screenshot or `.drawio` file as a quality reference, use it as the style source before changing another diagram.

Prefer the `.drawio` file when available because it exposes real geometry:

- Extract font sizes by semantic role.
- Extract geometry ratios for the visible structures in that reference: container and card dimensions, title/body text boxes, icon size, label height, row height, and padding.
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
python ~/.codex/skills/drawio-reconstruction/scripts/check_drawio.py path/to/file.drawio
python ~/.codex/skills/drawio-reconstruction/scripts/export_drawio.py path/to/file.drawio path/to/preview.png
```

For batch jobs:

```bash
python ~/.codex/skills/drawio-reconstruction/scripts/batch_manifest.py path/to/images --output-dir path/to/output --write
python ~/.codex/skills/drawio-reconstruction/scripts/batch_verify.py path/to/output/drawio_batch_manifest.json
```

The checker catches XML validity and common containment failures; it is not a substitute for visual inspection. After export, inspect the rendered PNG against the reference before final response.

## Final Response

Keep the final response short:

- Link to the `.drawio` file.
- Link to the rendered `.png` preview.
- Mention whether crops or SVG/native elements were used for major visual elements.
- Mention any remaining manual review point, especially if visual audit items remain unresolved.
