# Public release checklist

- [ ] Confirm that [DOI 10.5281/zenodo.22851757](https://doi.org/10.5281/zenodo.22851757) resolves publicly and contains the intended files.
- [ ] Confirm the Zenodo creator list, affiliations and ORCID identifiers.
- [ ] Add the final GitHub repository URL to the Zenodo record.
- [x] Release the GitHub analysis code under the MIT License.
- [ ] Confirm that Zenodo marks author-generated data as CC BY 4.0 and documents all third-party licences separately.
- [ ] Verify redistribution rights for every processed or third-party data layer.
- [ ] Test the Zenodo download and repository workflow from a clean directory.
- [ ] Run `python scripts/check_repository.py --root .` and confirm a clean result.
- [ ] Run `python scripts/run_all.py --root . --dry-run` and review the execution order.
- [ ] With the released data installed, execute all five notebooks and compare regenerated outputs with the submitted figures and tables.
