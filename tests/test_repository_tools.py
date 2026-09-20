import json
import tempfile
import unittest
from pathlib import Path

from scripts import check_repository, run_all


def write_notebook(path: Path, source: str, *, outputs=None, execution_count=None) -> None:
    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": execution_count,
                "metadata": {},
                "outputs": outputs or [],
                "source": source.splitlines(keepends=True),
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook), encoding="utf-8")


class RepositoryCheckerTests(unittest.TestCase):
    def test_clean_notebook_has_no_errors(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "clean.ipynb"
            write_notebook(path, "value = 1\n")

            self.assertEqual(check_repository.check_notebook(path), [])

    def test_notebook_reports_outputs_execution_paths_and_syntax(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "bad.ipynb"
            write_notebook(
                path,
                "source = r'C:\\private\\data.csv'\nif True print('broken')\n",
                outputs=[{"name": "stdout", "output_type": "stream", "text": ["stale"]}],
                execution_count=9,
            )

            errors = "\n".join(check_repository.check_notebook(path))

            self.assertIn("embedded output", errors)
            self.assertIn("execution count", errors)
            self.assertIn("absolute Windows path", errors)
            self.assertIn("syntax error", errors)

    def test_prohibited_extension_is_reported(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            path = root / "analysis" / "data.csv"
            path.parent.mkdir(parents=True)
            path.write_text("secret,data\n", encoding="utf-8")

            errors = check_repository.check_file(root, Path("analysis/data.csv"))

            self.assertTrue(any("prohibited extension" in error for error in errors))


class RunnerTests(unittest.TestCase):
    def test_notebook_plan_has_manuscript_order(self):
        root = Path("repo")

        self.assertEqual(
            run_all.notebook_plan(root),
            [
                root / "analysis/figure1/figure1.ipynb",
                root / "analysis/figure2_3/figure2_3.ipynb",
                root / "analysis/figure4/figure4.ipynb",
                root / "analysis/supplementary/supplementary.ipynb",
                root / "analysis/supplementary/sensitivity.ipynb",
            ],
        )

    def test_execution_command_writes_to_ignored_copy(self):
        root = Path("repo")
        notebook = root / "analysis/figure1/figure1.ipynb"

        command, output_directory = run_all.execution_command(root, notebook)

        self.assertIn("--execute", command)
        self.assertNotIn("--inplace", command)
        self.assertEqual(output_directory, root / ".executed/analysis/figure1")
        self.assertIn(str(output_directory), command)


if __name__ == "__main__":
    unittest.main()
