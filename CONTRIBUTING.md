# Contributing Guide

Thank you for your interest in contributing!

## How to Contribute

### Reporting Issues
Open an Issue with:
- Section number where the error occurs (e.g., "Section 15 — RUSLE")
- Error message (full traceback)
- Your input data characteristics (DEM resolution, CRS, number of subbasins)
- Python and library versions (`pip list | grep -E "geopandas|rasterio|numpy"`)

### Submitting Changes

1. **Fork** the repository
2. **Create a branch:** `git checkout -b fix/section15-K-factor`
3. **Make changes** following the code style guide below
4. **Test your changes** with the Pravara dataset
5. **Commit:** `git commit -m "Fix: K-factor slope threshold in section 15"`
6. **Push:** `git push origin fix/section15-K-factor`
7. **Open a Pull Request** with a clear description

## Code Style Guide

- Follow PEP 8 (max line length 100)
- Use f-strings for all string formatting
- Add docstrings to every function (NumPy style)
- Variable naming conventions:
  - Raster arrays: `UPPER_ARR` (e.g., `DEM_ARR`, `SLOPE_ARR`)
  - GeoDataFrames: `gdf_xxx` (e.g., `gdf_sub`, `gdf_so`)
  - DataFrames of results: `df_xxx` (e.g., `df_rusle`, `df_hg`)
  - Constants: `ALL_CAPS` (e.g., `DEM_RES`, `UTM_EPSG`)
  - File paths: end with `_DIR`, `_PATH`, or `_FILE`

## Adding a New Analysis Section

1. Create `scripts/section_XX_newanalysis.py` following the existing template
2. Add the section entry to `README.md` table
3. Add parameter definitions to `docs/PARAMETERS_REFERENCE.md`
4. Add methodology to `docs/methodology/XX_newanalysis.md`
5. Add outputs to `outputs/README.md`
6. Update `CHANGELOG.md`

## Priority Improvement Areas

| Area | Difficulty | Impact |
|------|-----------|--------|
| Replace slope-proxy C-factor with Sentinel-2 NDVI LULC | Medium | High |
| Replace slope-proxy K-factor with NBSS&LUP soil data | Low | High |
| Add IMD gridded rainfall for spatially distributed R-factor | Medium | High |
| Add SWAT model integration | Hard | Very High |
| Add Streamlit web dashboard | Medium | High |
| Add unit tests for morphometry functions | Low | Medium |
| Add ground-truth validation for check dam suitability | Low | Medium |
