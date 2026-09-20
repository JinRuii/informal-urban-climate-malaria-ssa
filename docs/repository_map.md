# Repository map

## Public source files

- `README.md`: study overview, setup, data placement and run instructions.
- `environment.yml` and `requirements.txt`: reproducible environment entry points.
- `analysis/figure1/`: Figure 1 descriptive and spatial analysis.
- `analysis/figure2_3/`: main weighted models, nonlinear associations and Figures 2–3.
- `analysis/figure4/`: dual-stage classification and Figure 4.
- `analysis/supplementary/`: supplementary maps, tables and robustness analyses.
- `scripts/check_repository.py`: public-release safety and notebook-integrity checks.
- `scripts/run_all.py`: ordered notebook execution.

## Local-only paths

- `analysis/data/`: Zenodo data copied by the user.
- `analysis/**/figures/`: generated figures.
- `analysis/**/tables/`: generated tables.
- `analysis/figure2_3/model_outputs/`: model summaries and predictions.
- Figure 4 `result4_*` files: generated source tables.

These paths are excluded from Git. Manuscripts, Supplementary Information documents, references and archives are not part of this repository.
