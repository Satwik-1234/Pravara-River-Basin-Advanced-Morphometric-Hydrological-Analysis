# 📂 Data Requirements & Input File Guide

## Overview

All input data files should be placed in the `data/` directory, or packaged into a single zip file and uploaded to Google Colab. The pipeline expects all rasters and vectors to be in the **same projected CRS** — UTM Zone 43N (EPSG:32643) by default.

---

## Required Input Files

### 1. Filled DEM (`Filled DEM.tif`)

| Property | Value |
|----------|-------|
| **Type** | GeoTIFF raster |
| **Resolution** | 30 m (SRTM standard) |
| **Value type** | Float32 — elevation in metres |
| **Preprocessing** | Must be **hydrologically filled** (no sinks) |
| **Source** | SRTM via USGS EarthExplorer or Bhuvan portal |
| **QGIS tool** | Raster → Analysis → Fill Nodata + Hydrology → Fill Sinks |
| **ArcGIS tool** | Spatial Analyst → Hydrology → Fill |

> ⚠️ A DEM with sinks will cause incorrect flow direction and accumulation results. Always fill before running the pipeline.

---

### 2. Flow Direction (`Flow Direction.tif`)

| Property | Value |
|----------|-------|
| **Type** | GeoTIFF raster |
| **Algorithm** | D8 (eight-direction flow model) |
| **Value encoding** | ArcGIS: 1=E, 2=SE, 4=S, 8=SW, 16=W, 32=NW, 64=N, 128=NE |
| **Derived from** | Filled DEM |
| **QGIS tool** | Saga → Terrain Analysis → Flow Direction (D8) |
| **ArcGIS tool** | Spatial Analyst → Hydrology → Flow Direction |

---

### 3. Flow Accumulation (`FlowAccumilation.tif`)

| Property | Value |
|----------|-------|
| **Type** | GeoTIFF raster |
| **Value type** | Int32 or Float32 — number of upstream cells |
| **Derived from** | Flow Direction |
| **QGIS tool** | Saga → Hydrology → Flow Accumulation |
| **ArcGIS tool** | Spatial Analyst → Hydrology → Flow Accumulation |

> **Tip:** Log-transform for visualisation: `np.log1p(flow_acc)`

---

### 4. Stream Order Network (`SteamOrder.shp`)

| Property | Value |
|----------|-------|
| **Type** | Polyline shapefile |
| **Attribute field** | `grid_code` — Strahler stream order (integer) |
| **Segments** | ~3,610 for the Pravara basin |
| **Source** | Derived from flow accumulation threshold + stream ordering |
| **QGIS tool** | Saga → Channels & Drainage → Strahler Order |
| **ArcGIS tool** | Spatial Analyst → Hydrology → Stream Order |

> **Note:** The field name `grid_code` is the default from ArcGIS. If your field is named differently (e.g., `ORDER`, `Strahler`), update `ORDER_COL` in `section_02_data_paths.py`.

---

### 5. Pour Points (`Pourpoints_3.shp`)

| Property | Value |
|----------|-------|
| **Type** | Point shapefile |
| **Records** | 3 points (one per subbasin outlet) |
| **Placement** | Must be placed ON the stream network, snapped to the highest flow accumulation cell at each outlet |
| **ArcGIS tool** | Snap Pour Points, then Watershed |

> ⚠️ Pour points must be precisely on stream cells. Use "Snap Pour Points" with a tolerance of 1–2 cells before running watershed delineation.

---

### 6. Basin/Subbasin Polygons (`Pravrabasin.shp`)

| Property | Value |
|----------|-------|
| **Type** | Polygon shapefile |
| **Records** | 5 polygons (3 subbasins + 2 others in the current version) |
| **Key attribute** | `AreaSqkm` column contains subbasin labels like "Subbasin-2" |
| **Derived from** | Watershed delineation from pour points |
| **ArcGIS tool** | Spatial Analyst → Hydrology → Watershed |

> **3-Subbasin Note:** When a clean 3-polygon shapefile (`pravra3.shp`) is available, update line ~355 in `section_02_data_paths.py` and re-run. The pipeline auto-detects the count and adapts.

---

## Optional/Derived Rasters

These are **automatically computed** by `section_02_data_paths.py` from the Filled DEM if not provided:

| Raster | Derived From | How |
|--------|-------------|-----|
| `slope.tif` | Filled DEM | `numpy` gradient + trigonometry |
| `aspect.tif` | Filled DEM | `numpy` gradient |
| `hillshade.tif` | Filled DEM + slope | Sun azimuth 315°, elevation 45° |
| `TWI.tif` | Flow accumulation + slope | `ln(As / tan(β))` |
| `SPI.tif` | Flow accumulation + slope | `As × tan(β)` |
| `CN.tif` | Slope (proxy for soil) | SCS curve number assignment |
| `RUSLE_*.tif` | DEM + flow acc | R, K, LS, C, P factor rasters |

---

## File Naming Conventions

The auto-detection in `section_00_zip_extraction.py` matches on **keywords** in filenames (case-insensitive):

| Layer | Keywords Detected |
|-------|-------------------|
| DEM | `dem`, `srtm`, `elevation`, `filled`, `fill` |
| Flow Direction | `flowdir`, `flow_dir`, `fdir`, `direction` |
| Flow Accumulation | `flowacc`, `flow_acc`, `facc`, `accumulation` |
| Stream Order | `strahler`, `streamorder`, `stream_order`, `order`, `steam` |
| Subbasin | `subbasin`, `sub_basin`, `watershed`, `basin`, `catchment`, `pravra` |
| Pour Points | `pour`, `outlet`, `pp` |

> If your filenames don't match, you can manually set paths in `section_02_data_paths.py` under the `DATA_PATHS` dictionary.

---

## CRS / Projection Setup

```python
# Expected CRS — set in section_02_data_paths.py
UTM_EPSG = 32643   # UTM Zone 43N — covers Pravara basin correctly

# To check your CRS in Python:
import geopandas as gpd
gdf = gpd.read_file("data/Pravrabasin.shp")
print(gdf.crs)   # should output: EPSG:32643

# To reproject if needed:
gdf = gdf.to_crs(epsg=32643)
gdf.to_file("data/Pravrabasin_utm.shp")
```

---

## Zip File Structure

If using the zip upload method for Google Colab, your zip should contain all files at the root level (not in nested subdirectories):

```
Morphomtery_layers-Final.zip
├── Filled DEM.tif
├── Flow Direction.tif
├── FlowAccumilation.tif
├── SteamOrder.shp
├── SteamOrder.dbf
├── SteamOrder.shx
├── SteamOrder.prj
├── Pourpoints_3.shp
├── Pourpoints_3.dbf
├── Pourpoints_3.shx
├── Pourpoints_3.prj
├── Pravrabasin.shp
├── Pravrabasin.dbf
├── Pravrabasin.shx
└── Pravrabasin.prj
```

> **Sidecar files** (`.dbf`, `.shx`, `.prj`, `.cpg`) must accompany each `.shp` or it will fail to load.
