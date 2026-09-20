# Public release checklist

- [ ] Confirm that [DOI 10.5281/zenodo.22851757](https://doi.org/10.5281/zenodo.22851757) resolves publicly and contains the intended files.
- [ ] Confirm the Zenodo creator list, affiliations and ORCID identifiers.
- [ ] Add the final GitHub repository URL to the Zenodo record.
- [ ] Replace `LICENSE_PLACEHOLDER.md` with the author-approved software licence.
- [ ] Select and record a separate, rights-compatible Zenodo data licence.
- [ ] Verify redistribution rights for every processed or third-party data layer.
- [ ] Test the Zenodo download and repository workflow from a clean directory.
- [ ] Run `python scripts/check_repository.py --root .` and confirm a clean result.
- [ ] Run `python scripts/run_all.py --root . --dry-run` and review the execution order.
- [ ] With the released data installed, execute all five notebooks and compare regenerated outputs with the submitted figures and tables.
