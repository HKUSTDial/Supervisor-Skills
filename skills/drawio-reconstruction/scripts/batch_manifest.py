#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}


def iter_images(source_dir, recursive):
    pattern = "**/*" if recursive else "*"
    for path in sorted(source_dir.glob(pattern)):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            yield path


def output_pair_available(drawio_path, preview_path, overwrite, reserved, sources):
    outputs = {drawio_path.resolve(), preview_path.resolve()}
    if outputs & reserved or outputs & sources:
        return False
    return overwrite or (not drawio_path.exists() and not preview_path.exists())


def unique_output_pair(output_dir, stem, overwrite, reserved, sources):
    index = 1
    while True:
        suffix = "" if index == 1 else f"-v{index}"
        drawio = output_dir / f"{stem}{suffix}.drawio"
        preview = output_dir / f"{stem}{suffix}_preview.png"
        if output_pair_available(drawio, preview, overwrite, reserved, sources):
            return drawio, preview
        index += 1


def make_manifest(source_dir, output_dir, recursive=False, overwrite=False):
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    images = list(iter_images(source_dir, recursive))
    sources = {path.resolve() for path in images}
    reserved = set()
    entries = []

    for index, image_path in enumerate(images, start=1):
        drawio_path, preview_path = unique_output_pair(
            output_dir,
            image_path.stem,
            overwrite,
            reserved,
            sources,
        )
        reserved.update({drawio_path.resolve(), preview_path.resolve()})
        entries.append(
            {
                "index": index,
                "status": "pending",
                "image": str(image_path.resolve()),
                "drawio": str(drawio_path),
                "preview": str(preview_path),
            }
        )

    return {
        "source_dir": str(source_dir),
        "output_dir": str(output_dir),
        "recursive": recursive,
        "overwrite": overwrite,
        "image_extensions": sorted(IMAGE_EXTENSIONS),
        "entries": entries,
    }


def print_summary(manifest):
    entries = manifest["entries"]
    print(f"source_dir: {manifest['source_dir']}")
    print(f"output_dir: {manifest['output_dir']}")
    print(f"entries: {len(entries)}")
    for entry in entries:
        print(
            f"{entry['index']:03d} [{entry['status']}] "
            f"{Path(entry['image']).name} -> {Path(entry['drawio']).name}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Create a Draw.io reconstruction batch manifest from an image folder."
    )
    parser.add_argument("source_dir", help="Directory containing reference images")
    parser.add_argument(
        "--output-dir",
        help="Directory for generated .drawio and .png files (defaults to source_dir)",
    )
    parser.add_argument(
        "--manifest",
        help="Manifest path (defaults to <output-dir>/drawio_batch_manifest.json)",
    )
    parser.add_argument("--recursive", action="store_true", help="Scan image files recursively")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow manifest entries to target existing output paths",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write the manifest JSON file instead of only printing a summary",
    )
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"missing directory: {source_dir}")
        return 1

    output_dir = Path(args.output_dir) if args.output_dir else source_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = make_manifest(
        source_dir,
        output_dir,
        recursive=args.recursive,
        overwrite=args.overwrite,
    )
    print_summary(manifest)

    if args.write:
        manifest_path = (
            Path(args.manifest)
            if args.manifest
            else output_dir / "drawio_batch_manifest.json"
        )
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"wrote: {manifest_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
