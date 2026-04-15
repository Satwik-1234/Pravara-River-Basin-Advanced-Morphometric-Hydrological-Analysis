# 📂 data/ — Input GIS Files

This directory stores all raw input files required to run the analysis pipeline.

**These files are NOT tracked by Git** (see `.gitignore`) because they are large binary GIS files. You must obtain and place them here manually.

---

## Files Required

```
data/
├── Filled DEM.tif              ← Hydrologically filled SRTM 30m DEM
├── Flow Direction.tif          ← D8 flow direction grid
├── FlowAccumilation.tif        ← Flow accumulation grid
├── SteamOrder.shp              ← Stream polylines with Strahler order (+ .dbf, .shx, .prj)
├── SteamOrder.dbf
├── SteamOrder.shx
├── SteamOrder.prj
├── Pourpoints_3.shp            ← 3 pour point outlets (+ sidecars)
├── Pourpoints_3.dbf
├── Pourpoints_3.shx
├── Pourpoints_3.prj
├── Pravrabasin.shp             ← Basin/subbasin polygon boundaries (+ sidecars)
├── Pravrabasin.dbf
├── Pravrabasin.shx
└── Pravrabasin.prj
```

## Google Colab Usage

If running in Google Colab, you do NOT need to put files in this directory. Instead:

1. Package all your files into `Morphomtery_layers-Final.zip`
2. Upload the zip to your Colab session storage
3. Run `section_00_zip_extraction.py` — it will auto-extract and detect all files

## Getting the Data

- **SRTM DEM:** https://earthexplorer.usgs.gov (30m, free)
- **Bhuvan Portal (India):** https://bhuvan.nrsc.gov.in (30m Cartosat DEM available)
- **QGIS Workflow:**
  1. Download SRTM tile (N19E073 for Pravara)
  2. Fill sinks: Raster → Hydrology → Fill Sinks
  3. Compute flow direction, accumulation, stream order
  4. Delineate watershed using pour points

See `docs/DATA_REQUIREMENTS.md` for detailed preprocessing instructions.
