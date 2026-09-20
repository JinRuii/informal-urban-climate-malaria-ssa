# Public release checklist

- [ ] Publish the Zenodo record and replace every `not yet assigned` DOI status with the final DOI.
- [ ] Confirm the ordered author list, affiliations and ORCID identifiers.
- [ ] Replace `CITATION_TEMPLATE.txt` with a schema-valid `CITATION.cff`.
- [ ] Add the final GitHub repository URL and archived release DOI.
- [ ] Replace `LICENSE_PLACEHOLDER.md` with the author-approved software licence.
- [ ] Select and record a separate, rights-compatible Zenodo data licence.
- [ ] Verify redistribution rights for every processed or third-party data layer.
- [ ] Add original dataset citations, versions and access dates to the manuscript.
- [ ] Test the Zenodo download and repository workflow from a clean directory.
- [ ] Run `python scripts/check_repository.py --root .` and confirm a clean result.
- [ ] Run `python scripts/run_all.py --root . --dry-run` and review the execution order.
- [ ] With the released data installed, execute all five notebooks and compare regenerated outputs with the submitted figures and tables.
