# === SECTION 3: MORPHOMETRIC PARAMETER CALCULATION ===
import os, sys
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.mask import mask as rio_mask
from shapely.geometry import mapping, Point as _SPoint
from scipy import stats

# Assuming dependencies from Section 1/2 are present in global scope if run sequentially
# or providing local definitions. For modular execution, we include core helpers.

def compute_linear_aspects(gdf_streams_clipped, order_col, basin_id):
    rows = []
    orders = sorted(gdf_streams_clipped[order_col].unique())
    for u in orders:
        segs = gdf_streams_clipped[gdf_streams_clipped[order_col] == u]
        nu, lu = len(segs), segs.geometry.length.sum()
        rows.append({'basin_id': basin_id, 'order': u, 'Nu': nu, 'Lu': lu, 'Lsm': lu/nu if nu>0 else 0})
    df = pd.DataFrame(rows).set_index('order')
    df['Rb'] = np.nan
    for i in range(len(df)-1):
        o1, o2 = orders[i], orders[i+1]
        if df.loc[o2, 'Nu'] > 0: df.loc[o1, 'Rb'] = df.loc[o1, 'Nu'] / df.loc[o2, 'Nu']
    df['RL'] = np.nan
    for i in range(1, len(df)):
        o_prev, o_curr = orders[i-1], orders[i]
        if df.loc[o_prev, 'Lsm'] > 0: df.loc[o_curr, 'RL'] = df.loc[o_curr, 'Lsm'] / df.loc[o_prev, 'Lsm']
    Rb_vals = df['Rb'].dropna(); Rbm = Rb_vals.mean() if len(Rb_vals) > 0 else np.nan
    wRbm = np.nan
    if len(Rb_vals) > 0:
        rb_l, wt_l = [], []
        for i in range(len(orders)-1):
            o1, o2 = orders[i], orders[i+1]
            if not np.isnan(df.loc[o1, 'Rb']) and df.loc[o2, 'Nu'] > 0:
                rb_l.append(df.loc[o1, 'Rb']); wt_l.append(df.loc[o1, 'Nu'] + df.loc[o2, 'Nu'])
        if len(rb_l) > 0: wRbm = np.average(rb_l, weights=wt_l)
    return df.reset_index(), Rbm, wRbm

def longest_flow_path(basin_geom):
    try:
        obb = basin_geom.minimum_rotated_rectangle; coords = list(obb.exterior.coords)
        return max(_SPoint(coords[0]).distance(_SPoint(coords[1])), _SPoint(coords[1]).distance(_SPoint(coords[2])))
    except Exception:
        b = basin_geom.bounds; return np.sqrt((b[2]-b[0])**2 + (b[3]-b[1])**2)

def hypsometric_integral(dem_clipped):
    vals = dem_clipped[~np.isnan(dem_clipped)].flatten()
    if len(vals) < 10: return np.nan, None, None
    mn, mx, mu = vals.min(), vals.max(), vals.mean()
    if mx - mn == 0: return np.nan, None, None
    HI = (mu - mn) / (mx - mn); thresholds = np.percentile(vals, np.linspace(0, 100, 101))
    return HI, 1 - np.linspace(0, 1, 101), (thresholds - mn) / (mx - mn)

# --- EXECUTION BLOCK ---
# Accessing global vars assuming sequential run or prior scripts execution
print("🛠️ Computing Verbatim Morphometry Suite...")
clipped_parts = []
for _, row in gdf_sub.iterrows():
    clip = gpd.clip(gdf_so[[ORDER_COL, 'geometry']], row.geometry)
    if clip is not None and len(clip) > 0:
        clip = clip.copy(); clip['basin_id'] = row['basin_id']; clipped_parts.append(clip)
gdf_so_sub = pd.concat(clipped_parts, ignore_index=True)

LINEAR_PER_ORDER, LINEAR_SUMMARY = {}, []
for bid in gdf_sub['basin_id']:
    segs = gdf_so_sub[gdf_so_sub['basin_id'] == bid]
    df_lin, Rbm, wRbm = compute_linear_aspects(segs, ORDER_COL, bid)
    LINEAR_PER_ORDER[bid] = df_lin
    LINEAR_SUMMARY.append({'basin_id': bid, 'total_streams_N': df_lin['Nu'].sum(), 'total_length_m': df_lin['Lu'].sum(), 'max_order': df_lin['order'].max(), 'Rbm': round(Rbm, 4)})

AREAL = []
for _, row in gdf_sub.iterrows():
    bid, geom = row['basin_id'], row.geometry
    A_km2, P_km, Lb_km = geom.area/1e6, geom.length/1e3, longest_flow_path(geom)/1e3
    segs = gdf_so_sub[gdf_so_sub['basin_id'] == bid]; L_km = segs.geometry.length.sum()/1e3
    N1 = len(segs[segs[ORDER_COL] == 1]); Nu_t = len(segs)
    Dd, Fs = L_km/A_km2, Nu_t/A_km2; T = N1/P_km
    Ff, Re, Rc = A_km2/(Lb_km**2), (2/Lb_km)*np.sqrt(A_km2/np.pi), (4*np.pi*A_km2)/(P_km**2)
    AREAL.append({'basin_id': bid, 'Area_km2': round(A_km2, 4), 'Drainage_Density_Dd': round(Dd, 4), 'Stream_Frequency_Fs': round(Fs, 4), 'Texture_Ratio_T': round(T, 4), 'Form_Factor_Ff': round(Ff, 4), 'Elongation_Ratio_Re': round(Re, 4), 'Circularity_Ratio_Rc': round(Rc, 4)})

RELIEF, HYPS = [], {}
for _, row in gdf_sub.iterrows():
    bid = row['basin_id']
    with rasterio.open(DATA_PATHS['dem']) as src:
        arr, _ = rio_mask(src, [mapping(row.geometry)], crop=True, nodata=src.nodata)
        clip = arr[0].astype(np.float32); clip[clip == src.nodata] = np.nan
    vals = clip[~np.isnan(clip)]
    H = vals.max()-vals.min(); HI, r_a, r_e = hypsometric_integral(clip)
    if r_a is not None: HYPS[bid] = (r_a, r_e)
    RELIEF.append({'basin_id': bid, 'Elev_Min_m': vals.min(), 'Elev_Max_m': vals.max(), 'Basin_Relief_H_m': H, 'Hypsometric_HI': round(HI, 4)})

df_master = pd.DataFrame(AREAL).set_index('basin_id').join(pd.DataFrame(RELIEF).set_index('basin_id')).join(pd.DataFrame(LINEAR_SUMMARY).set_index('basin_id'))
df_master.to_csv(os.path.join(TABLES_DIR, "morphometric_master_table.csv"))
print("✅ Section 03 Verbatim Restoral Complete.")
