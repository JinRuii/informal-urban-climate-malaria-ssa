# GitHub reproducibility repository design

## Objective

Create a public, code-first companion repository for the manuscript **“Informal urban conditions shape heat- and flood-related malaria burden across sub-Saharan Africa.”** The repository must let readers understand and rerun the retained analysis while keeping research data and manuscript files outside GitHub.

## Source boundary

- Read from `E:\处理\wenjing\子刊2 撒哈拉以南健康` without modifying it.
- Use the five unique analysis notebooks from `malaria_rui`: Figure 1, Figures 2–3, Figure 4, supplementary analyses, and sensitivity analyses.
- Do not copy manuscript DOCX files, supplementary-material DOCX files, reference PDFs, archives, raw data, processed data, source-data tables, generated model outputs, or generated figures.
- Do not copy the duplicated supplementary notebook package because its notebooks are byte-for-byte duplicates of the main analysis copy.

## Approaches considered

1. **Mirror the working directory.** Fast, but it would expose data, duplicates, large notebook outputs, unpublished documents, and cloud-sync debris. Rejected.
2. **Code-first reproducibility repository with a Zenodo data contract.** Keep cleaned notebooks and documentation on GitHub; publish the data separately on Zenodo and define exactly where users place it. Chosen because it matches the author’s publication plan and the strongest patterns in the reference repositories.
3. **Full Python-package refactor.** Move all notebook logic into reusable modules and add unit tests. This would be cleaner long term but is too invasive before publication and could change scientific behavior without a complete rerun. Deferred.

## Repository layout

```text
informal-urban-climate-malaria-ssa/
├── README.md
├── CITATION.cff
├── .gitignore
├── environment.yml
├── requirements.txt
├── analysis/
│   ├── README.md
│   ├── data/README.md
│   ├── figure1/figure1.ipynb
│   ├── figure2_3/figure2_3.ipynb
│   ├── figure4/figure4.ipynb
│   └── supplementary/
│       ├── supplementary.ipynb
│       └── sensitivity.ipynb
├── docs/
│   ├── data_availability.md
│   ├── repository_map.md
│   └── superpowers/specs/...
└── scripts/
    ├── check_repository.py
    └── run_all.py
```

## Notebook handling

- Preserve code and Markdown cell order.
- Clear all cell outputs and execution counts to remove about 20 MB of embedded output and avoid stale results.
- Normalize notebook names and directory names to portable ASCII forms.
- Preserve the existing relative layout so scientific path behavior changes as little as possible.
- Make only mechanical path updates required by the renamed folders.
- Do not rewrite statistical formulas or analytical logic.

## Data flow

1. A user clones GitHub and creates the documented environment.
2. A user downloads the separate Zenodo archive after its DOI is published.
3. The user places the extracted data under `analysis/data/` following `analysis/data/README.md`.
4. `scripts/check_repository.py` verifies required files and confirms that prohibited data files are not tracked elsewhere.
5. `scripts/run_all.py` executes notebooks in manuscript order from their own working directories.

The README will state `Zenodo DOI: not yet assigned` instead of inventing a DOI. The release checklist will require replacing that status once the record is published.

## Documentation design

The main README will follow the useful patterns found in the reference repositories:

- one-paragraph study overview;
- direct links/placeholders for the paper and Zenodo record;
- concise repository map;
- tested/expected software and hardware notes;
- exact setup and execution order;
- mapping from notebooks to manuscript figures and supplementary outputs;
- explicit scope and provenance limitations;
- citation and licensing status;
- release checklist for authors.

WeatherNext and Biomni additionally demonstrate the value of separating large external assets from code, documenting automatic/manual data acquisition, and keeping detailed material under `docs/`. The two article-companion repositories emphasize manuscript-output mapping, runtime/hardware expectations, and a short top-level workflow.

## Licensing and citation

- Include a schema-valid `CITATION.cff` only when author-confirmed names are available. Until then, provide a plain-text citation template in the README that explicitly says author and identifier metadata still require confirmation.
- Do not assign a code license on the authors’ behalf. State clearly that a license must be selected before public release and that the absence of a license means reuse permission has not yet been granted.
- Keep third-party data licensing and redistribution rights in the Zenodo/data documentation.

## Validation

- Validate every notebook as JSON and compile every code cell to catch syntax damage.
- Verify outputs and execution counts are empty.
- Scan tracked files for prohibited data/document/archive extensions and large files.
- Scan notebook source for local absolute paths and obvious secrets.
- Test the repository checker in the data-absent state.
- Test the runner’s dry-run mode without requiring unpublished data.
- Initialize a local Git repository and inspect the tracked-file manifest before handoff.

## Acceptance criteria

- The new folder exists independently under `F:\Codex_Work`.
- The source directory is unchanged.
- No research data, manuscripts, PDFs, archives, generated results, or reference files are present.
- Five unique cleaned notebooks are present and syntactically valid.
- A new user can identify the environment, expected data layout, run order, output mapping, and current reproduction limitations from the README and docs.
- Zenodo and publication identifiers are clearly marked as pending where not yet known.
