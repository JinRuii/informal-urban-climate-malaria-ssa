"""Validate that the public repository contains code and documentation only."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


MAX_FILE_BYTES = 50 * 1024 * 1024
PROHIBITED_EXTENSIONS = {
    ".7z",
    ".cpg",
    ".csv",
    ".dbf",
    ".doc",
    ".docm",
    ".docx",
    ".eps",
    ".feather",
    ".geojson",
    ".gpkg",
    ".grib",
    ".grib2",
    ".gz",
    ".jpeg",
    ".jpg",
    ".nc",
    ".parquet",
    ".pdf",
    ".png",
    ".prj",
    ".rar",
    ".sbn",
    ".sbx",
    ".shp",
    ".shx",
    ".svg",
    ".tar",
    ".tif",
    ".tiff",
    ".tsv",
    ".xls",
    ".xlsx",
    ".zip",
}
WINDOWS_ABSOLUTE_PATH = re.compile(r"(?<![A-Za-z0-9_])[A-Z]:[\\/]")
REQUIRED_NOTEBOOKS = {
    Path("analysis/figure1/figure1.ipynb"),
    Path("analysis/figure2_3/figure2_3.ipynb"),
    Path("analysis/figure4/figure4.ipynb"),
    Path("analysis/supplementary/supplementary.ipynb"),
    Path("analysis/supplementary/sensitivity.ipynb"),
}


def tracked_files(root: Path) -> list[Path]:
    completed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=True,
        capture_output=True,
    )
    return [Path(item.decode("utf-8")) for item in completed.stdout.split(b"\0") if item]


def check_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [f"{path}: invalid notebook JSON ({error})"]

    if notebook.get("nbformat") != 4:
        errors.append(f"{path}: expected notebook format 4")

    for cell_index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue

        if cell.get("outputs"):
            errors.append(f"{path}: cell {cell_index} contains embedded output")
        if cell.get("execution_count") is not None:
            errors.append(f"{path}: cell {cell_index} contains an execution count")

        source = "".join(cell.get("source", []))
        if WINDOWS_ABSOLUTE_PATH.search(source):
            errors.append(f"{path}: cell {cell_index} contains an absolute Windows path")
        try:
            compile(source, f"{path}:cell-{cell_index}", "exec")
        except SyntaxError as error:
            errors.append(
                f"{path}: cell {cell_index} has a syntax error at line "
                f"{error.lineno}: {error.msg}"
            )
    return errors


def check_file(root: Path, relative_path: Path) -> list[str]:
    errors: list[str] = []
    path = root / relative_path
    if not path.is_file():
        return [f"{relative_path}: tracked path is missing"]
    if relative_path.suffix.lower() in PROHIBITED_EXTENSIONS:
        errors.append(f"{relative_path}: prohibited extension in public repository")
    if path.stat().st_size > MAX_FILE_BYTES:
        errors.append(f"{relative_path}: file exceeds the 50 MB repository limit")
    if relative_path.suffix.lower() == ".ipynb":
        errors.extend(check_notebook(path))
    return errors


def scan_repository(root: Path) -> tuple[list[str], list[Path]]:
    try:
        files = tracked_files(root)
    except (OSError, subprocess.CalledProcessError) as error:
        return [f"Cannot read Git tracked files: {error}"], []

    errors: list[str] = []
    for relative_path in files:
        errors.extend(check_file(root, relative_path))

    tracked_notebooks = {path for path in files if path.suffix.lower() == ".ipynb"}
    missing = REQUIRED_NOTEBOOKS - tracked_notebooks
    unexpected = tracked_notebooks - REQUIRED_NOTEBOOKS
    for path in sorted(missing):
        errors.append(f"{path}: required notebook is not tracked")
    for path in sorted(unexpected):
        errors.append(f"{path}: unexpected notebook is tracked")
    return errors, files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    arguments = parser.parse_args(argv)
    root = arguments.root.resolve()

    errors, files = scan_repository(root)
    if errors:
        print("Repository check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    notebook_count = sum(path.suffix.lower() == ".ipynb" for path in files)
    print(
        f"Repository check passed: {len(files)} tracked files, "
        f"{notebook_count} clean notebooks, no prohibited artifacts."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
