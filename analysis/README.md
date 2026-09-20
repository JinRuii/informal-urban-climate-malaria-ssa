# Analysis notebooks

The five notebooks are organized in manuscript order and retain their original analytical logic. Embedded cell outputs and execution counts are removed for a compact, reviewable Git history.

Run notebooks from their own directories. The repository runner does this automatically:

```bash
python scripts/run_all.py --root . --dry-run
python scripts/run_all.py --root .
```

## Order and dependencies

1. `figure1/figure1.ipynb` reads the administrative-unit and country Shapefiles.
2. `figure2_3/figure2_3.ipynb` estimates the main models and writes local model summaries used by its plotting cells.
3. `figure4/figure4.ipynb` writes Figure 4 source tables, including the regional-decomposition input used by the supplementary notebook.
4. `supplementary/supplementary.ipynb` creates supplementary maps, descriptive tables and Figure 4 regional decomposition.
5. `supplementary/sensitivity.ipynb` runs robustness analyses and writes supplementary sensitivity tables and figures.

All generated artifacts are ignored by Git. The data must first be placed under `analysis/data/` according to [data/README.md](data/README.md).

Before committing changes, run:

```bash
python scripts/check_repository.py --root .
```
