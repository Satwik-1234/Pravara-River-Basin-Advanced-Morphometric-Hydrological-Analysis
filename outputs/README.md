# 📂 outputs/ — Generated Results

This directory is populated when you run the analysis pipeline. It is NOT tracked by Git.

## Directory Structure (auto-created at runtime)

```
outputs/
├── maps/                   ← PNG maps @ 300 DPI (Sections 4, 10–13, 14–18)
│   ├── hydrology/          ← Maps from Sections 14–18
│   └── conservation/       ← Maps from Section 16
│
├── tables/                 ← CSV result tables
│   └── hydrology_SWC_consolidated.csv   ← Master summary table
│
├── html/                   ← Interactive Plotly HTML charts
│   ├── 07_*.html           ← Section 7 interactive visualizations
│   ├── 14c_*.html          ← Flood frequency curves
│   ├── 15c_*.html          ← RUSLE erosion bars
│   └── 18c_*.html          ← Stream power charts
│
├── hydrology/              ← CSVs from Sections 14–18
│   ├── rainfall_frequency.csv
│   ├── runoff_scscn.csv
│   ├── time_of_concentration_peak_discharge.csv
│   ├── RUSLE_soil_erosion.csv
│   ├── stream_order_power.csv
│   └── channel_hydraulics.csv
│
├── conservation/           ← SWC planning outputs
│   ├── conservation_potential.csv
│   └── checkdam_suitability.csv
│
├── unit_hydrograph/        ← UH outputs
│   ├── 17_unit_hydrographs.png
│   └── snyder_unit_hydrograph_params.csv
│
├── shapefiles/             ← Exported GIS layers
│   └── checkdam_suitability.shp
│
├── report/                 ← Auto-generated report
│   └── pravara_basin_morphometry_report.pdf
│
├── CN.tif                  ← Curve Number raster
├── RUSLE_R.tif             ← R-factor raster
├── RUSLE_K.tif             ← K-factor raster
├── RUSLE_LS.tif            ← LS-factor raster
├── RUSLE_C.tif             ← C-factor raster
├── RUSLE_P.tif             ← P-factor raster
├── RUSLE_A.tif             ← Annual soil loss raster (t/ha/yr)
├── percolation_potential.tif
└── contour_trench_suitability.tif
```
