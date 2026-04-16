# === SECTION 12: ANOMALY & LINEAMENT ANALYSIS (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter

# --- SINUOSITY ---
def compute_sinuosity(geom):
    if geom.geom_type == 'MultiLineString': geom = max(geom.geoms, key=lambda g: g.length)
    coords = list(geom.coords)
    actual = geom.length
    straight = np.sqrt((coords[-1][0]-coords[0][0])**2 + (coords[-1][1]-coords[0][1])**2)
    return actual / straight if straight > 0 else 1.0

print("🔍 Executing Geomorphic Anomaly Audit...")
gdf_so['SI'] = gdf_so.geometry.apply(compute_sinuosity)

# --- GAI (Geomorphic Anomaly Index) ---
# Normalised composite of relief, slope anomaly, and curvature
def normalise(arr):
    v_min, v_max = np.nanmin(arr), np.nanmax(arr)
    return (arr - v_min) / (v_max - v_min + 1e-12)

# Using TRI and Slope as proxies for anomaly detection
n_TRI = normalise(TRI_ARR)
n_Slope = normalise(SLOPE_ARR)
GAI_ARR = (n_TRI + n_Slope) / 2.0
GAI_ARR = gaussian_filter(GAI_ARR, sigma=2)

save_raster(GAI_ARR.astype(np.float32), os.path.join(OUT_DIR, "gai_anomaly.tif"), RASTERS['dem'])

# Export Sinuosity results
si_stats = gdf_so.groupby(ORDER_COL)['SI'].mean()
si_stats.to_csv(os.path.join(TABLES_DIR, "sinuosity_stats.csv"))

print("✅ Section 12 Anomaly Analysis Restored.")
