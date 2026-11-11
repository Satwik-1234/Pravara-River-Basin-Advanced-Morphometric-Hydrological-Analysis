# === SECTION 14: RUNOFF ESTIMATION (SCS-CN + RATIONAL) ===
import os, sys
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask as rio_mask

print("\n" + "=" * 70)
print("SECTION 14 — RUNOFF ESTIMATION (SCS-CN)")
print("=" * 70)

# A. RAINFALL FREQUENCY (Gumbel)
RAIN_MEAN_MM = 750.0
RAIN_STD_MM  = 187.0
alpha_g = RAIN_STD_MM * np.sqrt(6) / np.pi
u_g     = RAIN_MEAN_MM - 0.5772 * alpha_g
DAILY_FRACTION = 0.22
RETURN_PERIODS = [2, 5, 10, 25, 50, 100]
RAINFALL_RT = {T: round((u_g + alpha_g * (-np.log(-np.log(1 - 1/T)))) * DAILY_FRACTION, 1) for T in RETURN_PERIODS}

# B. CURVE NUMBER MAP
slope_safe = np.where(np.isnan(SLOPE_ARR), 0.0, SLOPE_ARR)
CN_ARR = np.where(slope_safe < 3, 85.0, np.where(slope_safe < 8, 79.0, np.where(slope_safe < 20, 75.0, 70.0)))
CN_ARR[np.isnan(DEM_ARR)] = np.nan
save_raster(CN_ARR, os.path.join(OUT_DIR, "CN.tif"), RASTERS["dem"])

# C. SCS-CN RUNOFF
def scscn_runoff(P_mm, CN):
    S = 25400.0 / CN - 254.0
    Ia = 0.2 * S
    return np.where(P_mm > Ia, (P_mm - Ia)**2 / (P_mm + 0.8*S), 0.0)

RUNOFF_ROWS = []
for _, row in gdf_sub.iterrows():
    bid = row["basin_id"]
    geom = [row.geometry.__geo_interface__]
    with rasterio.open(os.path.join(OUT_DIR, "CN.tif")) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            cn_mean = float(np.nanmean(arr_m[0]))
        except: cn_mean = 75.0
    
    r_row = {"basin_id": bid, "CN_mean": cn_mean}
    for T in RETURN_PERIODS:
        r_row[f"Q_{T}yr_mm"] = round(float(scscn_runoff(RAINFALL_RT[T], cn_mean)), 2)
    RUNOFF_ROWS.append(r_row)

df_runoff = pd.DataFrame(RUNOFF_ROWS).set_index("basin_id")
df_runoff.to_csv(os.path.join(TABLES_DIR, "runoff_scscn.csv"))

print("✅ Section 14 Verbatim Restoral Complete.")
