# Informal urban conditions, climate exposure and malaria burden in sub-Saharan Africa

Code companion for the manuscript **“Informal urban conditions shape heat- and flood-related malaria burden across sub-Saharan Africa.”**

The study integrates slum-population-weighted heat and flood exposure, an Environmental Deprivation Index (EDI), and malaria infection, incidence and mortality across more than 3,900 subnational units. The analysis evaluates two stage-specific ecological transitions: infection to incidence and incidence to mortality.

> **Publication status:** manuscript under submission. **Zenodo DOI: not yet assigned.** Add the final paper and Zenodo links before making this repository public.

## What is and is not included

This repository contains analysis code, environment specifications, execution instructions and data-layout documentation. It intentionally contains **no research data, manuscript files, Supplementary Information documents, reference PDFs, archives, generated figures or generated model outputs**.

The analysis data will be released separately through Zenodo after the authors complete the repository metadata and licensing checks. See [Data Availability](docs/data_availability.md) and the [data-layout contract](analysis/data/README.md).

## Repository layout

```text
.
├── analysis/
│   ├── data/                 # local Zenodo data; ignored by Git
│   ├── figure1/              # Figure 1 workflow
│   ├── figure2_3/            # models and Figures 2–3
│   ├── figure4/              # Figure 4 workflow
│   └── supplementary/        # supplementary and sensitivity analyses
├── docs/                     # data, repository and release documentation
├── scripts/                  # repository checks and ordered execution
├── environment.yml           # recommended conda environment
└── requirements.txt          # pip alternative
```

For a detailed map, see [docs/repository_map.md](docs/repository_map.md).

## Analysis map

| Order | Notebook | Main purpose |
|---:|---|---|
| 1 | `analysis/figure1/figure1.ipynb` | Environmental exposure, burden-transition and country-level descriptive panels for Figure 1 |
| 2 | `analysis/figure2_3/figure2_3.ipynb` | Weighted models, nonlinear associations, regional moderation and Figures 2–3 |
| 3 | `analysis/figure4/figure4.ipynb` | Dual-stage contribution classification and Figure 4 source tables/panels |
| 4 | `analysis/supplementary/supplementary.ipynb` | Supplementary maps, trends, descriptive statistics and regional decomposition |
| 5 | `analysis/supplementary/sensitivity.ipynb` | Weighting, exposure-definition, threshold, fixed-effect, influence and inference sensitivity analyses |

## Installation

The recommended route is conda/mamba on Python 3.11:

```bash
conda env create -f environment.yml
conda activate malaria-ssa-repro
```

Alternatively, create a Python 3.10–3.12 virtual environment and run:

```bash
python -m pip install -r requirements.txt
```

The notebooks use geospatial libraries with compiled dependencies. A conda-forge environment is usually easier to reproduce than a pip-only installation.

## Obtain and place the data

1. Download the companion Zenodo record after its DOI is added here.
2. From the Zenodo package, locate `01_main_analysis/malaria_rui/data/`.
3. Copy the **contents** of that directory into `analysis/data/` without renaming its subdirectories.
4. Read [analysis/data/README.md](analysis/data/README.md) and verify the expected files.

The resulting local tree should begin as follows:

```text
analysis/data/
├── country/
├── HI406_days/
├── overall/
├── slum pop/
└── WBGT30_days/
```

Git ignores all files in `analysis/data/` except its README.

## Validate and run

Check the public-repository contents before execution:

```bash
python scripts/check_repository.py --root .
```

Preview the execution order without running notebooks:

```bash
python scripts/run_all.py --root . --dry-run
```

After the Zenodo data are in place, execute the full workflow:

```bash
python scripts/run_all.py --root .
```

Each notebook is executed from its own directory so that its relative paths remain stable. Generated tables, figures and executed notebook outputs are local artifacts and are excluded from Git.

## Reproduction scope and limitations

The retained Zenodo package is designed to reproduce analyses from processed, analysis-ready spatial products. It does not contain every upstream flood, malaria or intermediate raster layer used earlier in preprocessing. In particular, the retained malaria indicators were mapped from source administrative-unit means to the slum-population analysis grid; they are population-weighted derived estimates rather than a new calculation from original malaria rasters.

Accordingly, this repository supports review and rerunning of the retained analysis workflow, but not complete reconstruction of every upstream data-processing step. Additional provenance details are in [docs/data_availability.md](docs/data_availability.md).

## Citation

The paper, dataset DOI, repository URL and full author list have not yet been finalized. Before public release, replace [CITATION_TEMPLATE.txt](CITATION_TEMPLATE.txt) with a validated `CITATION.cff` and add the paper citation here. Do not invent or pre-register a DOI in this repository.

## License

No software license has yet been authorized by the authors. Until a license is selected, copyright is retained and no reuse permission is granted. Replace [LICENSE_PLACEHOLDER.md](LICENSE_PLACEHOLDER.md) with the approved license before public release. Third-party datasets may have separate terms and must not be relicensed by this repository.

## Author release checks

The repository is structurally ready for review, but the author team must complete the short [release checklist](docs/release_checklist.md) before publishing it on GitHub.
