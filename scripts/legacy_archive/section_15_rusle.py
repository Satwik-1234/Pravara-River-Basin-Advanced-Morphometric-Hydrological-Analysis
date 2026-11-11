# === SECTION 15: RUSLE SOIL EROSION MODEL (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd

print("\n" + "=" * 70)
print("SECTION 15 — RUSLE SOIL EROSION")
print("=" * 70)

# R-FACTOR
elev_mean = np.nanmean(DEM_ARR)
R_ARR = 650.0 * (1.0 + 0.05 * (DEM_ARR - elev_mean) / (np.nanstd(DEM_ARR) + 1e-6))
R_ARR = np.clip(R_ARR, 400.0, 1000.0)

# K-FACTOR
slope_safe = np.where(np.isnan(SLOPE_ARR), 0, SLOPE_ARR)
K_ARR = np.where(slope_safe < 3, 0.25, np.where(slope_safe < 8, 0.20, np.where(slope_safe < 15, 0.15, 0.10)))

# LS-FACTOR (Moore et al. 1991)
As_arr = np.where(np.isnan(FACC_ARR), 0, FACC_ARR) * DEM_RES
slope_rad = np.radians(np.maximum(slope_safe, 0.01))
LS_ARR = ((As_arr / 22.13) ** 0.4) * ((np.sin(slope_rad) / 0.0896) ** 1.3)
LS_ARR = np.clip(LS_ARR, 0, 50)

# C & P FACTORS
C_ARR = np.where(slope_safe < 3, 0.20, np.where(slope_safe < 15, 0.45, 0.15))
P_ARR = np.where(slope_safe < 8, 0.55, 1.0)

# ANNUAL SOIL LOSS (A)
A_ARR = R_ARR * K_ARR * LS_ARR * C_ARR * P_ARR
A_ARR[np.isnan(DEM_ARR)] = np.nan
save_raster(A_ARR.astype(np.float32), os.path.join(OUT_DIR, "RUSLE_A.tif"), RASTERS["dem"])

print("✅ Section 15 Verbatim Restoral Complete.")
