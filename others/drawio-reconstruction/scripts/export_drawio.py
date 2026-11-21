#!/usr/bin/env python3
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


DRAWIO_CANDIDATES = (
    Path("/Applications/draw.io.app/Contents/MacOS/draw.io"),
    Path("/Applications/drawio.app/Contents/MacOS/drawio"),
    Path("/usr/bin/drawio"),
    Path("/usr/local/bin/drawio"),
)


def _resolve_executable(value):
    expanded = Path(os.path.expandvars(value)).expanduser()
    if expanded.is_file():
        return str(expanded)
    return shutil.which(value)


def _windows_candidates():
    candidates = []
    for variable in ("ProgramFiles", "ProgramW6432"):
        base = os.environ.get(variable)
        if base:
            candidates.append(Path(base) / "draw.io" / "draw.io.exe")
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        candidates.append(Path(local_app_data) / "Programs" / "draw.io" / "draw.io.exe")
    return candidates


def find_drawio(explicit_path=None):
    configured = explicit_path or os.environ.get("DRAWIO_PATH")
    if configured:
        resolved = _resolve_executable(configured)
        if resolved:
            return resolved
        raise FileNotFoundError(
            f"configured Draw.io executable not found: {configured} "
            "(--drawio-path or DRAWIO_PATH)"
        )

    for path in (*DRAWIO_CANDIDATES, *_windows_candidates()):
        if path.exists():
            return str(path)
    return shutil.which("drawio") or shutil.which("draw.io")


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Export a .drawio file to PNG with Draw.io Desktop/CLI."
    )
    parser.add_argument("input", help="Input .drawio file")
    parser.add_argument("output", nargs="?", help="Output PNG path")
    parser.add_argument(
        "--drawio-path",
        help="Draw.io executable path; overrides DRAWIO_PATH and automatic detection",
    )
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args(sys.argv[1:])

    input_path = Path(args.input).expanduser()
    if not input_path.exists():
        print(f"missing: {input_path}", file=sys.stderr)
        return 1

    output_path = Path(args.output).expanduser() if args.output else input_path.with_suffix(".png")
    try:
        drawio = find_drawio(args.drawio_path)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if not drawio:
        print(
            "Draw.io CLI not found; install Draw.io Desktop or set DRAWIO_PATH",
            file=sys.stderr,
        )
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [drawio, "-x", "-f", "png", "-s", "1", "-o", str(output_path), str(input_path)]
    try:
        result = subprocess.run(cmd, text=True, capture_output=True)
    except OSError as exc:
        print(f"failed to start Draw.io CLI {drawio}: {exc}", file=sys.stderr)
        return 1
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0:
        return result.returncode
    if not output_path.exists() or output_path.stat().st_size == 0:
        print(f"export failed: {output_path}", file=sys.stderr)
        return 1
    print(f"exported: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
