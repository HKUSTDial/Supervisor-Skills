#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
CHECK_SCRIPT = SCRIPT_DIR / "check_drawio.py"
EXPORT_SCRIPT = SCRIPT_DIR / "export_drawio.py"


def load_jobs(target):
    target = Path(target)
    if target.is_file() and target.suffix.lower() == ".json":
        manifest = json.loads(target.read_text(encoding="utf-8"))
        jobs = []
        for entry in manifest.get("entries", []):
            drawio = Path(entry["drawio"])
            preview = Path(entry.get("preview") or drawio.with_suffix(".png"))
            jobs.append((drawio, preview))
        return jobs

    if target.is_file() and target.suffix.lower() == ".drawio":
        return [(target, target.with_suffix(".png"))]

    if target.is_dir():
        return [(path, path.with_suffix(".png")) for path in sorted(target.glob("*.drawio"))]

    raise FileNotFoundError(f"missing target: {target}")


def run_command(cmd):
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result.returncode


def verify_job(drawio_path, preview_path, skip_export=False):
    if not drawio_path.exists():
        print(f"[missing] {drawio_path}")
        return False

    print(f"[check] {drawio_path}")
    check_code = run_command([sys.executable, str(CHECK_SCRIPT), str(drawio_path)])
    if check_code != 0:
        return False

    if not skip_export:
        print(f"[export] {preview_path}")
        export_code = run_command(
            [sys.executable, str(EXPORT_SCRIPT), str(drawio_path), str(preview_path)]
        )
        if export_code != 0:
            return False

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Batch check and export Draw.io reconstruction outputs."
    )
    parser.add_argument(
        "target",
        help="Manifest JSON, a .drawio file, or a directory containing .drawio files",
    )
    parser.add_argument(
        "--no-export",
        action="store_true",
        help="Run XML/layout checks without exporting PNG previews",
    )
    args = parser.parse_args()

    try:
        jobs = load_jobs(args.target)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not jobs:
        print("no .drawio files to verify")
        return 1

    passed = 0
    failed = 0
    for drawio_path, preview_path in jobs:
        if verify_job(drawio_path, preview_path, skip_export=args.no_export):
            passed += 1
        else:
            failed += 1

    print(f"summary: passed={passed} failed={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
