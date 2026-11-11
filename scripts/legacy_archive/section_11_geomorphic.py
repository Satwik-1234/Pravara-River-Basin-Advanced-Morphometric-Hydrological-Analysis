# === SECTION 11: GEOMORPHIC INDICES (SL, SPI, TWI, STI) ===
import os, sys
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.mask import mask as rio_mask

# --- HELPER: SL INDEX ---
def calculate_sl_index(stream_gdf, dem_arr, dem_transform, k=10):
    sl_indices = []
    for _, row in stream_gdf.iterrows():
        geom = row.geometry
        if geom.geom_type == 'MultiLineString': geom = max(geom.geoms, key=lambda g: g.length)
        coords = list(geom.coords)
        if len(coords) < k+1: sl_indices.append(np.nan); continue
        elevs = []
        for p in coords:
            r, c = rasterio.transform.rowcol(dem_transform, p[0], p[1])
            elevs.append(dem_arr[r, c] if 0<=r<dem_arr.shape[0] and 0<=c<dem_arr.shape[1] else np.nan)
        elevs = np.array(elevs); valid = ~np.isnan(elevs)
        if np.sum(valid) < k: sl_indices.append(np.nan); continue
        # SL = (dH/dL) * L_total
        dh = elevs[0] - elevs[-1]
        dl = geom.length
        sl_indices.append((dh/dl) * dl if dl>0 else np.nan)
    return sl_indices

# --- CALCULATION SUITE ---
print("🏔️ Computing Geomorphic Indices (Verbatim)...")

# SL Index
gdf_SL = gdf_so.copy()
gdf_SL['SL_index'] = calculate_sl_index(gdf_SL, DEM_ARR, DEM_TRANSFORM)
gdf_SL.to_file(os.path.join(SHAPES_DIR, "streams_sl.shp"))

# SPI & STI (Simplified logic from master)
cell_area = DEM_RES * DEM_RES
# Approximation for As using flow accumulation
As_arr = FACC_ARR * cell_area
slope_rad = np.radians(SLOPE_ARR)
tan_beta = np.tan(slope_rad); tan_beta[tan_beta < 0.001] = 0.001
sin_beta = np.sin(slope_rad); sin_beta[sin_beta < 0.001] = 0.001

SPI_ARR = As_arr * tan_beta
# STI = (As/22.13)**0.6 * (sin_beta/0.0896)**1.3
STI_ARR = ((As_arr / 22.13) ** 0.6) * ((sin_beta / 0.0896) ** 1.3)

# TWI = ln(As / tan_beta)
TWI_ARR = np.log(As_arr / tan_beta + 1e-6)
TWI_ARR[~np.isfinite(TWI_ARR)] = np.nan

# Save Rasters
save_raster(SPI_ARR.astype(np.float32), os.path.join(OUT_DIR, "spi.tif"), RASTERS['dem'])
save_raster(STI_ARR.astype(np.float32), os.path.join(OUT_DIR, "sti.tif"), RASTERS['dem'])
save_raster(TWI_ARR.astype(np.float32), os.path.join(OUT_DIR, "twi.tif"), RASTERS['dem'])

print("✅ Section 11 Geomorphic Indices Restored.")
