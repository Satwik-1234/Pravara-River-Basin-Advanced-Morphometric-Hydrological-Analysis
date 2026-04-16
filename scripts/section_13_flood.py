# === SECTION 13: FLOOD HAZARD INDICATORS (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask as rio_mask
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

print("\n" + "=" * 60)
print("SECTION 13 — FLOOD HAZARD INDICATORS")
print("=" * 60)

# A. LOADING TWI, SPI, STI
print("\n[A] Loading TWI, SPI, STI arrays...")
with rasterio.open(RASTERS['twi']) as src:
    TWI_ARR2 = src.read(1).astype(np.float32)
    TWI_ARR2[TWI_ARR2 == -9999.0] = np.nan

with rasterio.open(RASTERS['spi']) as src:
    SPI_ARR2 = src.read(1).astype(np.float32)
    SPI_ARR2[SPI_ARR2 == -9999.0] = np.nan

with rasterio.open(RASTERS['sti']) as src:
    STI_ARR2 = src.read(1).astype(np.float32)
    STI_ARR2[STI_ARR2 == -9999.0] = np.nan

# B. FLASH FLOOD POTENTIAL INDEX (FFPI)
print("\n[B] Flash Flood Potential Index (FFPI)...")

def normalise_raster(arr):
    mn, mx = np.nanmin(arr), np.nanmax(arr)
    return (arr - mn) / (mx - mn + 1e-12)

norm_slope = normalise_raster(np.where(np.isnan(SLOPE_ARR), 0, SLOPE_ARR))
norm_twi = normalise_raster(np.where(np.isnan(TWI_ARR2), 0, TWI_ARR2))
norm_spi = normalise_raster(np.log1p(np.where(np.isnan(SPI_ARR2), 0, SPI_ARR2)))

FFPI = (norm_slope * 0.35 + norm_twi * 0.35 + norm_spi * 0.30)
FFPI[np.isnan(DEM_ARR)] = np.nan
save_raster(FFPI.astype(np.float32), os.path.join(OUT_DIR, "FFPI.tif"), RASTERS['dem'])

# C. PER-BASIN HAZARD STATISTICS
HAZARD_ROWS = []
for _, row in gdf_sub.iterrows():
    bid = row['basin_id']
    geom = [row.geometry.__geo_interface__]
    with rasterio.open(os.path.join(OUT_DIR, "FFPI.tif")) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            ffpi_clip = arr_m[0]
            ffpi_mean = float(np.nanmean(ffpi_clip))
        except:
            ffpi_mean = np.nan
    HAZARD_ROWS.append({'basin_id': bid, 'FFPI_mean': ffpi_mean})

df_hazard = pd.DataFrame(HAZARD_ROWS).set_index('basin_id')
df_hazard.to_csv(os.path.join(TABLES_DIR, "flood_hazard_indices.csv"))

print("✅ Section 13 Verbatim Restoral Complete.")
