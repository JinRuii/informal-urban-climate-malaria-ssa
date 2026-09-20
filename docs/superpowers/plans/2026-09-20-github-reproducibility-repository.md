# GitHub Reproducibility Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a code-first GitHub companion repository for the sub-Saharan Africa malaria manuscript, with all research data and manuscript documents kept outside GitHub on Zenodo.

**Architecture:** Keep five cleaned Jupyter notebooks under `analysis/`, add a small `scripts/` validation/runner layer, and document a strict Zenodo data contract. Use portable ASCII paths and preserve each notebook's own working directory.

**Tech Stack:** Python 3.10+, Jupyter notebooks, geopandas/pandas/numpy/matplotlib/scipy/statsmodels/patsy/shapely/rasterio/openpyxl.

---

### Task 1: Create repository metadata and documentation

**Files:**
- Create: `README.md`
- Create: `LICENSE_PLACEHOLDER.md`
- Create: `CITATION_TEMPLATE.txt`
- Create: `.gitignore`
- Create: `requirements.txt`
- Create: `environment.yml`
- Create: `analysis/README.md`
- Create: `analysis/data/README.md`
- Create: `docs/data_availability.md`
- Create: `docs/repository_map.md`

- [ ] **Step 1: Add top-level README**
  Include the confirmed manuscript title, a short study description, a repository tree, exact run order, a table mapping notebooks to Figure 1/Figures 2–3/Figure 4/Supplementary outputs, the Zenodo status sentence `Zenodo DOI: not yet assigned`, the processed-data limitation, and a release checklist. State explicitly that this repository contains no data, manuscripts, supplementary DOCX files, PDFs, archives, or generated outputs.

- [ ] **Step 2: Add data contract docs**
  `analysis/data/README.md` must list the expected Zenodo-extracted paths (`overall/`, `country/`, `HI406_days/`, `WBGT30_days/`, `slum pop/`), required Shapefile component sets, raster year range, and the fact that the user must obtain the data from Zenodo. `docs/data_availability.md` must distinguish retained analysis-ready products from excluded upstream layers.

- [ ] **Step 3: Add environment files and publication placeholders**
  Put the existing package names in `requirements.txt`, add a compatible conda environment in `environment.yml`, and keep author/DOI/repository fields in `CITATION_TEMPLATE.txt` visibly marked as requiring author confirmation. Do not invent a software license; explain that `LICENSE_PLACEHOLDER.md` must be replaced before public release.

- [ ] **Step 4: Add ignore rules**
  Exclude research data, generated figures/results, manuscript formats, archives, notebook checkpoints, local environments, and cloud-sync files. Keep `analysis/data/README.md` trackable via negation rules.

- [ ] **Step 5: Commit metadata**
  Run `git add README.md LICENSE_PLACEHOLDER.md CITATION_TEMPLATE.txt .gitignore requirements.txt environment.yml analysis/README.md analysis/data/README.md docs` and commit with `docs: add repository metadata and data contract`.

### Task 2: Copy and clean the five unique notebooks

**Files:**
- Create: `analysis/figure1/figure1.ipynb`
- Create: `analysis/figure2_3/figure2_3.ipynb`
- Create: `analysis/figure4/figure4.ipynb`
- Create: `analysis/supplementary/supplementary.ipynb`
- Create: `analysis/supplementary/sensitivity.ipynb`

- [ ] **Step 1: Copy source notebooks**
  Copy only the unique notebooks from `E:\处理\wenjing\子刊2 撒哈拉以南健康\malaria_rui\...`; do not copy data, figures, manuscripts, references, archives, or duplicate SI package files.

- [ ] **Step 2: Clear embedded outputs**
  Set every code cell's `outputs` to `[]` and `execution_count` to `null` while preserving source and Markdown cells.

- [ ] **Step 3: Normalize paths mechanically**
  Update only paths required by the new layout. Do not alter statistical expressions.

- [ ] **Step 4: Validate notebook JSON and code compilation**
  Load all five notebooks as JSON, assert no outputs and no execution counts, compile every code cell, and fail on local absolute path literals.

- [ ] **Step 5: Commit notebooks**
  Run `git add analysis` and commit with `refactor: clean analysis notebooks for public repository`.

### Task 3: Add reproducibility checks and runner

**Files:**
- Create: `scripts/check_repository.py`
- Create: `scripts/run_all.py`

- [ ] **Step 1: Implement repository checker**
  Recursively scan Git-tracked files, fail on prohibited extensions, fail on files larger than 50 MB, parse every notebook, check empty outputs, compile code cells, and report absolute Windows paths. Accept `--root` and return exit code 0 only when all checks pass.

- [ ] **Step 2: Implement dry-run runner**
  `run_all.py --root . --dry-run` prints the five notebook paths in execution order. Without `--dry-run`, run each notebook with `jupyter nbconvert --execute`, write executed copies under the ignored `.executed/` directory, preserve the clean source notebooks, and stop on the first failure.

- [ ] **Step 3: Add script usage docs**
  Document both commands in `README.md` and `analysis/README.md`, noting that full execution requires the Zenodo data tree and produces ignored local outputs.

- [ ] **Step 4: Commit scripts**
  Run `git add scripts README.md analysis/README.md` and commit with `chore: add repository checks and runner`.

### Task 4: Final validation and handoff manifest

**Files:**
- Create: `docs/release_checklist.md`
- Create: `docs/tracked_files_manifest.txt`

- [ ] **Step 1: Run repository checker**
  Run `python scripts/check_repository.py --root .`; expect five valid notebooks and no prohibited files.

- [ ] **Step 2: Run runner dry-run**
  Run `python scripts/run_all.py --root . --dry-run`; expect Figure 1, Figures 2–3, Figure 4, Supplementary, Sensitivity.

- [ ] **Step 3: Inspect tracked manifest**
  Save sorted `git ls-files` output to `docs/tracked_files_manifest.txt` and verify no data, manuscript, PDF, archive, or generated output files are tracked.

- [ ] **Step 4: Add release checklist**
  Require authors to add the Zenodo DOI, confirm author metadata, choose a code license, confirm third-party data rights, and test a clean clone with the Zenodo data tree before publishing.

- [ ] **Step 5: Commit final validation**
  Run `git add docs` and commit with `release: add validation manifest and checklist`.
