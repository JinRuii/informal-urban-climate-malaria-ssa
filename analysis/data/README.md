# Local analysis data (not tracked by Git)

Download the companion data from [Zenodo (DOI: 10.5281/zenodo.22851757)](https://doi.org/10.5281/zenodo.22851757). From the deposit, copy the contents of `01_main_analysis/malaria_rui/data/` into this directory.

Expected layout:

```text
analysis/data/
├── country/
│   └── country_SSA_HE2.{shp,shx,dbf,prj,cpg,...}
├── HI406_days/
│   └── [ten annual exposure rasters for 2011–2020]
├── overall/
│   └── admin_Africa_with_RoofVul_SSA_HE6_flood_malaria.{shp,shx,dbf,prj,cpg,...}
├── slum pop/
│   └── subsaharan_africa_slum_population.tif
└── WBGT30_days/
    └── [ten annual exposure rasters for 2011–2020]
```

The main administrative-unit Shapefile contains the analysis-ready variables used by the notebooks. The country layer supplies boundaries and regional labels. Shapefiles are multi-file datasets: keep all sidecar components together and do not rename individual components.

The retained source package describes the administrative-unit layer as 4,320 features and the country/region layer as 44 features, both in EPSG:4326. Individual models apply missingness and validity filters, so their analytical sample sizes are smaller.

## Important scope limitation

The Zenodo package does not contain every upstream flood, malaria or intermediate raster layer used earlier in preprocessing. The retained malaria indicators are population-weighted derived estimates mapped from source administrative-unit means to the analysis grid. These files support the retained analysis workflow but do not reconstruct every upstream preprocessing step.

Do not commit any file placed in this directory. The repository `.gitignore` keeps only this README under version control.
