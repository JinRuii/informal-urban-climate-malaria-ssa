"""Execute the five analysis notebooks in manuscript order."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


NOTEBOOKS = (
    Path("analysis/figure1/figure1.ipynb"),
    Path("analysis/figure2_3/figure2_3.ipynb"),
    Path("analysis/figure4/figure4.ipynb"),
    Path("analysis/supplementary/supplementary.ipynb"),
    Path("analysis/supplementary/sensitivity.ipynb"),
)

REQUIRED_DATA = (
    Path("analysis/data/overall/admin_Africa_with_RoofVul_SSA_HE6_flood_malaria.shp"),
    Path("analysis/data/country/country_SSA_HE2.shp"),
    Path("analysis/data/slum pop/subsaharan_africa_slum_population.tif"),
    Path("analysis/data/HI406_days"),
    Path("analysis/data/WBGT30_days"),
)


def notebook_plan(root: Path) -> list[Path]:
    return [root / path for path in NOTEBOOKS]


def missing_data(root: Path) -> list[Path]:
    return [root / path for path in REQUIRED_DATA if not (root / path).exists()]


def execution_command(root: Path, notebook: Path) -> tuple[list[str], Path]:
    relative_parent = notebook.relative_to(root).parent
    output_directory = root / ".executed" / relative_parent
    command = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--ExecutePreprocessor.timeout=-1",
        "--output",
        notebook.name,
        "--output-dir",
        str(output_directory),
        notebook.name,
    ]
    return command, output_directory


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="repository root")
    parser.add_argument("--dry-run", action="store_true", help="print the execution order only")
    arguments = parser.parse_args(argv)
    root = arguments.root.resolve()

    notebooks = notebook_plan(root)
    missing_notebooks = [path for path in notebooks if not path.is_file()]
    if missing_notebooks:
        print("Missing notebooks:", file=sys.stderr)
        for path in missing_notebooks:
            print(f"- {path}", file=sys.stderr)
        return 1

    print("Notebook execution order:")
    for index, notebook in enumerate(notebooks, start=1):
        print(f"{index}. {notebook.relative_to(root)}")

    if arguments.dry_run:
        return 0

    absent_data = missing_data(root)
    if absent_data:
        print("\nRequired Zenodo data are missing:", file=sys.stderr)
        for path in absent_data:
            print(f"- {path}", file=sys.stderr)
        print("See analysis/data/README.md for the expected layout.", file=sys.stderr)
        return 2

    for index, notebook in enumerate(notebooks, start=1):
        command, output_directory = execution_command(root, notebook)
        output_directory.mkdir(parents=True, exist_ok=True)
        print(f"\n[{index}/{len(notebooks)}] Executing {notebook.relative_to(root)}")
        try:
            subprocess.run(command, cwd=notebook.parent, check=True)
        except subprocess.CalledProcessError as error:
            print(f"Execution failed with exit code {error.returncode}: {notebook}", file=sys.stderr)
            return error.returncode or 1

    print(f"\nExecuted notebook copies are under {root / '.executed'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
