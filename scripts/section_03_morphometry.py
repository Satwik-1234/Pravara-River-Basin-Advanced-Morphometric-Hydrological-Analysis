print("SECTION 3 Ã¢â‚¬â€ MORPHOMETRIC PARAMETER CALCULATION")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. LINEAR ASPECTS  (stream order statistics)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[A] Computing Linear Aspects...")

def compute_linear_aspects(gdf_streams_clipped, order_col, basin_id):
    """
    Compute stream order statistics for one subbasin.
    Returns per-order DataFrame and summary ratios.
    """
    rows = []
    orders = sorted(gdf_streams_clipped[order_col].unique())

    for u in orders:
        segs = gdf_streams_clipped[gdf_streams_clipped[order_col] == u]
        nu   = len(segs)
        lu   = segs.geometry.length.sum()
        lsm  = lu / nu if nu > 0 else 0
        rows.append({'basin_id': basin_id, 'order': u,
                     'Nu': nu, 'Lu': lu, 'Lsm': lsm})

    df = pd.DataFrame(rows).set_index('order')

    # Bifurcation ratio Rb = Nu / Nu+1
    df['Rb'] = np.nan
    for i in range(len(df) - 1):
        o1, o2 = orders[i], orders[i+1]
        if df.loc[o2, 'Nu'] > 0:
            df.loc[o1, 'Rb'] = df.loc[o1, 'Nu'] / df.loc[o2, 'Nu']

    # Stream length ratio RL = Lsm(u) / Lsm(u-1)
    df['RL'] = np.nan
    for i in range(1, len(df)):
        o_prev, o_curr = orders[i-1], orders[i]
        if df.loc[o_prev, 'Lsm'] > 0:
            df.loc[o_curr, 'RL'] = df.loc[o_curr, 'Lsm'] / df.loc[o_prev, 'Lsm']

    # Mean bifurcation ratio (arithmetic)
    Rb_vals = df['Rb'].dropna()
    Rbm = Rb_vals.mean() if len(Rb_vals) > 0 else np.nan

    # Weighted mean bifurcation ratio (Strahler, 1957)
    wRbm = np.nan
    if len(Rb_vals) > 0:
        rb_list, wt_list = [], []
        for i in range(len(orders) - 1):
            o1, o2 = orders[i], orders[i+1]
            rb_val = df.loc[o1, 'Rb']
            if not np.isnan(rb_val) and df.loc[o2, 'Nu'] > 0:
                rb_list.append(rb_val)
                wt_list.append(df.loc[o1, 'Nu'] + df.loc[o2, 'Nu'])

        if len(rb_list) > 0:
            wts_arr = np.array(wt_list)
            if wts_arr.sum() > 0:
                wRbm = np.average(rb_list, weights=wts_arr)

    return df.reset_index(), Rbm, wRbm


# Spatial join: streams to subbasins
# Ã¢â€â‚¬Ã¢â€â‚¬ Correct: clip stream network to each subbasin, then tag basin_id Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
clipped_parts = []
for _, basin_row in gdf_sub.iterrows():
    bid  = basin_row['basin_id']
    clip = gpd.clip(gdf_so[[ORDER_COL, 'geometry']], basin_row.geometry)
    if clip is not None and len(clip) > 0:
        clip = clip.copy()
        clip['basin_id'] = bid
        clipped_parts.append(clip)

if clipped_parts:
    gdf_so_sub = pd.concat(clipped_parts, ignore_index=True)
else:
    # Last-resort fallback: intersects join (may double-count boundary segs)
    gdf_so_sub = gpd.sjoin(
        gdf_so[[ORDER_COL, 'geometry']],
        gdf_sub[['basin_id', 'geometry']],
        how='left', predicate='intersects'
    ).dropna(subset=['basin_id'])
    print("  Ã¢Å¡Â Ã¯Â¸Â  Falling back to intersects join Ã¢â‚¬â€ check CRS alignment.")

LINEAR_PER_ORDER = {}   # basin_id Ã¢â€ â€™ DataFrame
LINEAR_SUMMARY   = []   # one row per basin

for bid in gdf_sub['basin_id']:
    segs = gdf_so_sub[gdf_so_sub['basin_id'] == bid]
    if len(segs) == 0:
        print(f"  Ã¢Å¡Â Ã¯Â¸Â  No stream segments found for basin {bid}")
        continue
    df_lin, Rbm, wRbm = compute_linear_aspects(segs, ORDER_COL, bid)
    LINEAR_PER_ORDER[bid] = df_lin

    total_N = df_lin['Nu'].sum()
    total_L = df_lin['Lu'].sum()
    max_ord = df_lin['order'].max()

    LINEAR_SUMMARY.append({
        'basin_id'       : bid,
        'total_streams_N': total_N,
        'total_length_m' : total_L,
        'max_order'      : max_ord,
        'Rbm'            : round(Rbm, 4),
        'wRbm'           : round(wRbm, 4) if not np.isnan(wRbm) else np.nan,
    })
    print(f"  {bid}: {total_N} streams | max order {max_ord} | Rbm={Rbm:.3f}")

df_linear_summary = pd.DataFrame(LINEAR_SUMMARY).set_index('basin_id')
print("\n  Stream Order Summary (all basins):")
for bid, df in LINEAR_PER_ORDER.items():
    print(f"\n  [{bid}]")
    print(df[['order','Nu','Lu','Lsm','Rb','RL']].to_string(index=False))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. AREAL ASPECTS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[B] Computing Areal Aspects...")

from shapely.geometry import Point as _SPoint
def longest_flow_path(basin_geom, facc_arr=None, transform=None, res_m=None):
    """
    Approximate basin length (Lb) as the major axis of the minimum rotated
    bounding rectangle Ã¢â‚¬â€ a standard GIS proxy used when full D8 tracing is
    not available (Schumm, 1956).
    """
    try:
        obb    = basin_geom.minimum_rotated_rectangle
        coords = list(obb.exterior.coords)
        side1  = _SPoint(coords[0]).distance(_SPoint(coords[1]))
        side2  = _SPoint(coords[1]).distance(_SPoint(coords[2]))
        lb     = max(side1, side2)   # longest axis of the OBB (metres)
    except Exception:
        b  = basin_geom.bounds       # (minx, miny, maxx, maxy)
        lb = np.sqrt((b[2]-b[0])**2 + (b[3]-b[1])**2)
    return lb


AREAL = []

for _, row in gdf_sub.iterrows():
    bid   = row['basin_id']
    geom  = row.geometry

    A  = geom.area          # mÃ‚Â²
    P  = geom.length        # m
    Lb = longest_flow_path(geom, FACC_ARR, DEM_TRANSFORM, DEM_RES)

    # Streams inside basin
    segs = gdf_so_sub[gdf_so_sub['basin_id'] == bid]
    total_stream_length = segs.geometry.length.sum() if len(segs) > 0 else 0
    Nu_total = len(segs)

    # ----- parameters -----
    A_km2   = A   / 1e6
    P_km    = P   / 1e3
    Lb_km   = Lb  / 1e3
    L_km    = total_stream_length / 1e3

    Dd = L_km  / A_km2 if A_km2 > 0 else np.nan   # Drainage density  [km/kmÃ‚Â²]
    Fs = Nu_total / A_km2 if A_km2 > 0 else np.nan # Stream frequency  [streams/kmÃ‚Â²]
    # Ã¢â€â‚¬Ã¢â€â‚¬ Correct Texture Ratio: use first-order streams only Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    segs_first_order = segs[segs[ORDER_COL] == 1]   # first-order (Strahler) only
    N1 = len(segs_first_order)                       # count of 1st-order streams

    T  = N1 / P_km  if P_km  > 0 else np.nan        # Texture ratio (Smith, 1950)
    Ff = A_km2   / (Lb_km**2)     if Lb_km > 0 else np.nan  # Form factor (Horton,1932)
    Re = (2 / Lb_km) * np.sqrt(A_km2 / np.pi) if Lb_km > 0 else np.nan  # Elongation ratio
    Rc = (4 * np.pi * A_km2) / (P_km**2)  if P_km > 0 else np.nan       # Circularity ratio
    Cc = P_km / (2 * np.sqrt(np.pi * A_km2)) if A_km2 > 0 else np.nan   # Compactness coeff
    Lg = 1 / (2 * Dd)   if Dd and Dd > 0 else np.nan   # Length of overland flow
    C  = 1 / Dd          if Dd and Dd > 0 else np.nan   # Constant of channel maintenance

    AREAL.append({
        'basin_id'              : bid,
        'Area_km2'              : round(A_km2, 4),
        'Perimeter_km'          : round(P_km, 4),
        'Basin_Length_km'       : round(Lb_km, 4),
        'Total_Stream_Length_km': round(L_km, 4),
        'Stream_Count'          : Nu_total,
        'Drainage_Density_Dd'   : round(Dd, 4) if not np.isnan(Dd) else np.nan,
        'Stream_Frequency_Fs'   : round(Fs, 4) if not np.isnan(Fs) else np.nan,
        'Texture_Ratio_T'       : round(T,  4) if not np.isnan(T)  else np.nan,
        'Form_Factor_Ff'        : round(Ff, 4) if not np.isnan(Ff) else np.nan,
        'Elongation_Ratio_Re'   : round(Re, 4) if not np.isnan(Re) else np.nan,
        'Circularity_Ratio_Rc'  : round(Rc, 4) if not np.isnan(Rc) else np.nan,
        'Compactness_Cc'        : round(Cc, 4) if not np.isnan(Cc) else np.nan,
        'LengthOverlandFlow_Lg' : round(Lg, 4) if not np.isnan(Lg) else np.nan,
        'ChannelMaintenance_C'  : round(C,  4) if not np.isnan(C)  else np.nan,
    })

    print(f"  {bid}: A={A_km2:.2f} kmÃ‚Â² | Dd={Dd:.3f} km/kmÃ‚Â² | "
          f"Re={Re:.3f} | Rc={Rc:.3f} | Ff={Ff:.3f}")

df_areal = pd.DataFrame(AREAL).set_index('basin_id')

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. RELIEF ASPECTS  (DEM zonal statistics)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[C] Computing Relief Aspects...")

def hypsometric_integral(dem_clipped):
    """
    Compute hypsometric integral (HI) = (mean_elev - min_elev) / (max_elev - min_elev)
    Also returns arrays for hypsometric curve: (relative_area, relative_elevation)
    """
    vals = dem_clipped[~np.isnan(dem_clipped)].flatten()
    if len(vals) < 10:
        return np.nan, None, None
    mn, mx, mu = vals.min(), vals.max(), vals.mean()
    rng = mx - mn
    if rng == 0:
        return np.nan, None, None
    HI = (mu - mn) / rng
    # Curve: relative elevation h/H vs relative area a/A
    thresholds   = np.percentile(vals, np.linspace(0, 100, 101))
    rel_elev     = (thresholds - mn) / rng          # h/H  (0Ã¢â€ â€™1)
    rel_area     = 1 - np.linspace(0, 1, 101)       # a/A  (1Ã¢â€ â€™0)
    return HI, rel_area, rel_elev


def terrain_ruggedness_index(dem_arr):
    """
    TRI (Riley et al., 1999): mean absolute difference from center cell
    to 8 neighbours.
    """
    from scipy.ndimage import generic_filter
    def _tri_kernel(x):
        centre = x[4]
        if np.isnan(centre):
            return np.nan
        diffs = x - centre
        diffs[4] = 0
        valid = diffs[~np.isnan(diffs)]
        return np.sqrt(np.sum(valid**2)) if len(valid) > 0 else np.nan
    tri = generic_filter(dem_arr.astype(float), _tri_kernel, size=3, mode='reflect')
    tri[np.isnan(dem_arr)] = np.nan
    return tri


def melton_ruggedness(h_m, a_km2):
    """Melton (1965) ruggedness index MRN = H / sqrt(A)."""
    return h_m / np.sqrt(a_km2) if a_km2 > 0 else np.nan


# Compute TRI once for full DEM
print("  Computing TRI (this may take 30Ã¢â‚¬â€œ60 sec on large DEMs)...")
TRI_ARR = terrain_ruggedness_index(DEM_ARR)
save_raster(TRI_ARR, os.path.join(OUT_DIR, "tri.tif"), RASTERS['dem'])

RELIEF   = []
HYPS     = {}   # basin_id Ã¢â€ â€™ (rel_area, rel_elev)

for _, row in gdf_sub.iterrows():
    bid  = row['basin_id']
    geom = [row.geometry.__geo_interface__]

    # Mask DEM to subbasin (STRICT)
    with rasterio.open(RASTERS['dem']) as src:
        geom_dem = [mapping(gdf_sub[gdf_sub['basin_id'] == bid].to_crs(src.crs).geometry.iloc[0])]
        try:
            # Use native nodata for the mask operation itself
            arr_masked, _ = rio_mask(src, geom_dem, crop=True, nodata=src.nodata)
            dem_clip = arr_masked[0].astype(np.float32)
            if src.nodata is not None:
                dem_clip[dem_clip == src.nodata] = np.nan
        except Exception as e:
            print(f"  [Error] Clipping DEM for {bid}: {e}")
            dem_clip = np.array([np.nan])

    # Mask slope to subbasin (STRICT)
    with rasterio.open(RASTERS['slope']) as src:
        geom_slope = [mapping(gdf_sub[gdf_sub['basin_id'] == bid].to_crs(src.crs).geometry.iloc[0])]
        try:
            s_masked, _ = rio_mask(src, geom_slope, crop=True, nodata=-9999)
            slope_clip = s_masked[0].astype(np.float32)
            slope_clip[slope_clip == -9999.0] = np.nan
        except Exception as e:
            print(f"  [Error] Clipping Slope for {bid}: {e}")
            slope_clip = np.array([np.nan])

    # Mask TRI
    with rasterio.open(os.path.join(OUT_DIR, "tri.tif")) as src:
        try:
            t_masked, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            tri_clip = t_masked[0].astype(np.float32)
            tri_clip[tri_clip == -9999.0] = np.nan
        except Exception:
            tri_clip = TRI_ARR.copy()

    valid_dem   = dem_clip[~np.isnan(dem_clip)]
    valid_slope = slope_clip[~np.isnan(slope_clip)]
    valid_tri   = tri_clip[~np.isnan(tri_clip)]

    if len(valid_dem) == 0:
        print(f"  Ã¢Å¡Â Ã¯Â¸Â  {bid}: no valid DEM cells")
        continue

    elev_min  = float(valid_dem.min())
    elev_max  = float(valid_dem.max())
    elev_mean = float(valid_dem.mean())
    H         = elev_max - elev_min              # Basin relief (m)
    A_km2     = df_areal.loc[bid, 'Area_km2']
    Lb_km     = df_areal.loc[bid, 'Basin_Length_km']
    P_km      = df_areal.loc[bid, 'Perimeter_km']

    Rh  = H / (Lb_km * 1000) if Lb_km > 0 else np.nan   # Relief ratio
    Rr = (H / 1000.0) / P_km  if P_km > 0 else np.nan   # Relative relief (dimensionless)
    Dd  = df_areal.loc[bid, 'Drainage_Density_Dd']
    Rn  = H * Dd / 1000       if not np.isnan(Dd) else np.nan  # Ruggedness number
    MRN = melton_ruggedness(H, A_km2)                           # Melton ruggedness

    # Hypsometric integral
    HI, rel_area, rel_elev = hypsometric_integral(dem_clip)
    if rel_area is not None:
        HYPS[bid] = (rel_area, rel_elev)

    # Slope statistics
    slope_mean = float(np.nanmean(valid_slope))
    slope_std  = float(np.nanstd(valid_slope))
    slope_skew = float(stats.skew(valid_slope))

    # TRI stats
    tri_mean = float(np.nanmean(valid_tri))

    RELIEF.append({
        'basin_id'         : bid,
        'Elev_Min_m'       : round(elev_min,  2),
        'Elev_Max_m'       : round(elev_max,  2),
        'Elev_Mean_m'      : round(elev_mean, 2),
        'Basin_Relief_H_m' : round(H,         2),
        'Relief_Ratio_Rh'  : round(Rh,        6) if not np.isnan(Rh) else np.nan,
        'Relative_Relief'  : round(Rr,        4) if not np.isnan(Rr) else np.nan,
        'Ruggedness_Rn'    : round(Rn,        4) if not np.isnan(Rn) else np.nan,
        'Melton_MRN'       : round(MRN,       4) if not np.isnan(MRN) else np.nan,
        'Hypsometric_HI'   : round(HI,        4) if not np.isnan(HI) else np.nan,
        'Slope_Mean_deg'   : round(slope_mean, 3),
        'Slope_Std_deg'    : round(slope_std,  3),
        'Slope_Skewness'   : round(slope_skew, 4),
        'TRI_Mean'         : round(tri_mean,   3),
    })

    print(f"  {bid}: H={H:.0f}m | Rh={Rh:.5f} | HI={HI:.3f} | "
          f"Rn={Rn:.3f} | Slope_mean={slope_mean:.2f}Ã‚Â°")

df_relief = pd.DataFrame(RELIEF).set_index('basin_id')

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. MASTER MORPHOMETRIC TABLE
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Assembling master morphometric table...")

df_master = df_areal.join(df_relief, how='left')
df_master = df_master.join(df_linear_summary, how='left')

# Add stream order per-basin summary
for bid in gdf_sub['basin_id']:
    if bid in LINEAR_PER_ORDER:
        df_lin = LINEAR_PER_ORDER[bid]
        for _, r in df_lin.iterrows():
            col = f"Nu_order{int(r['order'])}"
            df_master.loc[bid, col] = r['Nu']
            col = f"Lu_order{int(r['order'])}_km"
            df_master.loc[bid, col] = round(r['Lu'] / 1000, 4)

# Ã¢â€â‚¬Ã¢â€â‚¬ Interpretation flags Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def interpret_elongation(Re):
    if pd.isna(Re):       return "Unknown"
    if Re >= 0.9:         return "Circular"
    if Re >= 0.8:         return "Oval"
    if Re >= 0.7:         return "Less Elongated"
    if Re >= 0.5:         return "Elongated"
    return "More Elongated"

def interpret_circularity(Rc):
    if pd.isna(Rc):      return "Unknown"
    if Rc >= 0.75:       return "Circular/Young"
    if Rc >= 0.50:       return "Intermediate"
    return "Elongated/Old"

def interpret_HI(HI):
    if pd.isna(HI):      return "Unknown"
    if HI > 0.60:        return "Monadnock (Young/Convex)"
    if HI > 0.35:        return "Mature (Equilibrium)"
    return "Peneplain (Old/Concave)"

df_master['Shape_Class']    = df_master['Elongation_Ratio_Re'].apply(interpret_elongation)
df_master['Circ_Class']     = df_master['Circularity_Ratio_Rc'].apply(interpret_circularity)
df_master['Hyps_Class']     = df_master['Hypsometric_HI'].apply(interpret_HI)

# Save
csv_path = os.path.join(TABLES_DIR, "morphometric_master_table.csv")
df_master.to_csv(csv_path)
print(f"  Ã¢Å“â€¦ Master table saved: {csv_path}")

print("\n" + "Ã¢â€â‚¬"*60)
print("  MASTER MORPHOMETRIC TABLE (first 10 rows/all params):")
print("Ã¢â€â‚¬"*60)
print(df_master.to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬ Hypsometric Curves Ã¢â‚¬â€ all sub-basins Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
if 'HYPS' in globals() and HYPS:
    fig_h, ax_h = plt.subplots(figsize=(7, 6))
    colors_h = plt.cm.tab10(np.linspace(0, 1, len(HYPS)))
    for (bid_h, (rel_area, rel_elev)), col in zip(HYPS.items(), colors_h):
        ax_h.plot(rel_area, rel_elev, lw=2, label=bid_h, color=col)
    ax_h.set_xlabel("Relative Area (a/A)", fontsize=12)
    ax_h.set_ylabel("Relative Elevation (h/H)", fontsize=12)
    ax_h.set_title("Hypsometric Curves Ã¢â‚¬â€ Pravara Sub-basins", fontsize=13,
                 fontweight='bold')
    ax_h.legend(fontsize=10)
    ax_h.set_xlim(0, 1); ax_h.set_ylim(0, 1)
    ax_h.grid(True, linestyle='--', alpha=0.5)
    # Annotate HI values
    for bid_h in HYPS:
        if bid_h in df_master.index and 'Hypsometric_HI' in df_master.columns:
            hi = df_master.loc[bid_h, 'Hypsometric_HI']
            ax_h.annotate(f"{bid_h}: HI={hi:.3f}",
                        xy=(0.05, 0.05 + list(HYPS.keys()).index(bid_h) * 0.08),
                        xycoords='axes fraction', fontsize=9)
    plt.tight_layout()
    fig_h.savefig(os.path.join(PLOTS_DIR, "hypsometric_curves.png"),
                dpi=180, bbox_inches='tight')
    plt.close(fig_h)
    print("  Ã¢Å“â€¦ Hypsometric curve plot saved.")


# Ã¢â€¢â€Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢â€”
# Ã¢â€¢â€˜  MAP FRAMEWORK Ã¢â‚¬â€ 70:30 layout Ã‚Â· ESRI basemap Ã‚Â· GIS scale bar          Ã¢â€¢â€˜
# Ã¢â€¢â€˜  DESIGN-01 Ã‚Â· DESIGN-02 Ã‚Â· DESIGN-03 Ã‚Â· DESIGN-04 Ã‚Â· DESIGN-05 Ã‚Â· 07     Ã¢â€¢â€˜
# Ã¢â€¢Å¡Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â

import subprocess, sys
try:
    import contextily as cx
    print("  contextily already installed")
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'contextily', '-q'])
    import contextily as cx
    print("  contextily installed")

import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from rasterio.features import geometry_mask
from shapely.ops import unary_union

# Ã¢â€â‚¬Ã¢â€â‚¬ Basemap sources Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
BASEMAP_TOPO      = cx.providers.Esri.WorldTopoMap
BASEMAP_HILLSHADE = cx.providers.Esri.WorldShadedRelief
COMPASS_PNG_PATH  = os.path.join(OUT_DIR, "assets", "compass_rose.png")
os.makedirs(os.path.join(OUT_DIR, "assets"), exist_ok=True)
PANEL_BG = '#F4F3EF'

# Ã¢â€â‚¬Ã¢â€â‚¬ DESIGN-05: Mask raster to basin boundary Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def mask_raster_to_basin(arr, dem_transform, gdf_sub_utm):
    """Set pixels outside combined basin polygon to NaN."""
    union_geom = unary_union(gdf_sub_utm.geometry)
    mask = geometry_mask(
        [union_geom.__geo_interface__],
        transform=dem_transform, invert=True, out_shape=arr.shape,
    )
    out = arr.copy().astype(np.float32)
    out[~mask] = np.nan
    return out

print("  Pre-masking rasters to basin boundary...")
DEM_ARR_MASKED    = mask_raster_to_basin(DEM_ARR,    DEM_TRANSFORM, gdf_sub)
SLOPE_ARR_MASKED  = mask_raster_to_basin(SLOPE_ARR,  DEM_TRANSFORM, gdf_sub)
ASPECT_ARR_MASKED = mask_raster_to_basin(ASPECT_ARR, DEM_TRANSFORM, gdf_sub)
FACC_ARR_MASKED   = mask_raster_to_basin(FACC_ARR,   DEM_TRANSFORM, gdf_sub)
FDIR_ARR_MASKED   = mask_raster_to_basin(FDIR_ARR,   DEM_TRANSFORM, gdf_sub)
HILLSHADE_MASKED  = mask_raster_to_basin(HILLSHADE,  DEM_TRANSFORM, gdf_sub)
print("  Raster masking done.")

# Ã¢â€â‚¬Ã¢â€â‚¬ Basin extent with padding Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def basin_extent_padded(pad_frac=0.025):
    """(xmin, xmax, ymin, ymax) + padding."""
    b  = gdf_sub.total_bounds
    px = (b[2] - b[0]) * pad_frac
    py = (b[3] - b[1]) * pad_frac
    return (b[0]-px, b[2]+px, b[1]-py, b[3]+py)

def compute_utm_extent():
    b = DEM_BOUNDS
    return b.left, b.right, b.bottom, b.top

def raster_extent():
    b = DEM_BOUNDS
    return [b.left, b.right, b.bottom, b.top]

# Ã¢â€â‚¬Ã¢â€â‚¬ DESIGN-01: Standard GIS Unified Layout Figure Factory Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def make_map_figure(title, figsize=(16, 11)):
    """Creates a professional GIS layout using a unified 16x11 frame."""
    fig, ax_map = plt.subplots(figsize=figsize, facecolor='white', dpi=150)
    fig.subplots_adjust(left=0.08, right=0.92, bottom=0.08, top=0.88)
    
    # Transparent shim for backward compat
    ax_panel = fig.add_axes([0, 0, 1, 1], facecolor='none')
    ax_panel.axis('off')
    
    # Boxed Title overlay
    title_box = FancyBboxPatch((0.15, 0.90), 0.70, 0.08, transform=fig.transFigure,
                             facecolor='white', alpha=0.92, edgecolor='#111111', 
                             linewidth=1.5, boxstyle="round,pad=0.01", zorder=100)
    fig.patches.append(title_box)
    
    fig.text(0.5, 0.945, 'PRAVARA RIVER BASIN', transform=fig.transFigure,
             ha='center', va='center', fontsize=12, fontweight='bold', color='#333333')
    fig.text(0.5, 0.920, title.upper(), transform=fig.transFigure,
             ha='center', va='center', fontsize=15, fontweight='black', color='black')

    for sp in ax_map.spines.values():
        sp.set_edgecolor('#111111'); sp.set_linewidth(2.0)
    ax_map.set_facecolor('#F0F8FF') 
    return fig, ax_map, ax_panel

def add_esri_basemap(ax, source=None, alpha=0.55):
    """ESRI World Topo Map integration with optimal transparency."""
    if source is None: source = ctx.providers.Esri.WorldTopoMap
    try:
        ctx.add_basemap(ax, crs=str(gdf_sub.crs), source=source,
                       zoom='auto', alpha=alpha, attribution=False, zorder=0)
    except Exception:
        ax.imshow(HILLSHADE_MASKED, extent=raster_extent(), origin='upper',
                  cmap='Greys_r', alpha=0.45, zorder=0)

def add_compass_rose_panel(ax_panel, cx_pos=0.08, cy_pos=0.15, r=0.06):
    """Professional 8-point compass rose overlay."""
    ax_panel.add_patch(plt.Circle((cx_pos, cy_pos), r*1.15, transform=ax_panel.transAxes,
                                  facecolor='white', alpha=0.9, edgecolor='#333333', lw=0.6, zorder=30))
    for angle_deg in range(0, 360, 45):
        angle = np.radians(angle_deg)
        length = r if angle_deg % 90 == 0 else r * 0.6
        pts_r = [ (cx_pos, cy_pos),
                  (cx_pos + np.cos(angle)*length, cy_pos + np.sin(angle)*length),
                  (cx_pos + np.cos(angle-0.12)*length*0.2, cy_pos + np.sin(angle-0.12)*length*0.2) ]
        ax_panel.add_patch(plt.Polygon(pts_r, transform=ax_panel.transAxes, 
                                       facecolor='#111111', edgecolor='none', zorder=31))
        pts_l = [ (cx_pos, cy_pos),
                  (cx_pos + np.cos(angle)*length, cy_pos + np.sin(angle)*length),
                  (cx_pos + np.cos(angle+0.12)*length*0.2, cy_pos + np.sin(angle+0.12)*length*0.2) ]
        ax_panel.add_patch(plt.Polygon(pts_l, transform=ax_panel.transAxes, 
                                       facecolor='white', edgecolor='#111111', lw=0.4, zorder=31))
    ax_panel.text(cx_pos, cy_pos + r*1.35, 'N', transform=ax_panel.transAxes,
                  ha='center', va='bottom', fontsize=10, fontweight='black', color='black', zorder=35)

def add_scale_bar_panel(ax_panel, utm_extent=None, y_top=0.32, x_left=0.03, bar_w=0.15):
    """Modular GIS staggered scale bar overlay."""
    if utm_extent is None: utm_extent = compute_utm_extent()
    dist_km = (utm_extent[1] - utm_extent[0]) / 1000.0
    bar_km = next((n for n in [5,10,20,50,100] if n >= dist_km*0.15), 10)
    bar_h = 0.02; bar_y = y_top - bar_h
    x_steps = np.linspace(x_left, x_left + bar_w, 5)
    ax_panel.add_patch(Rectangle((x_left-0.01, y_top-0.08), bar_w+0.02, 0.12, transform=ax_panel.transAxes,
                                 facecolor='white', alpha=0.85, edgecolor='none', zorder=20))
    for i in range(4):
        fc = '#111111' if i % 2 == 0 else 'white'
        ax_panel.add_patch(Rectangle((x_steps[i], bar_y), x_steps[i+1]-x_steps[i], bar_h,
                                     transform=ax_panel.transAxes, facecolor=fc, 
                                     edgecolor='#111111', lw=0.8, zorder=25))
    lkw = dict(transform=ax_panel.transAxes, ha='center', va='bottom', fontsize=7, color='black', fontweight='bold')
    ax_panel.text(x_steps[0], bar_y+bar_h+0.005, '0', **lkw)
    ax_panel.text(x_steps[4], bar_y+bar_h+0.005, f'{bar_km} km', **lkw)
    ax_panel.text(x_left + bar_w/2, bar_y - 0.015, "PLANIMETRIC SCALE", 
                  transform=ax_panel.transAxes, ha='center', va='top', 
                  fontsize=6, color='#444444', style='italic', zorder=26)

def add_classified_legend_panel(ax_panel, colours, labels, title='Legend', y_top=0.42, x_left=0.74):
    """Categorical legend in an inset box."""
    n = len(labels)
    box_w, box_h = 0.24, 0.05 + (n * 0.045)
    ax_panel.add_patch(FancyBboxPatch((x_left, y_top-box_h), box_w, box_h, 
                                     boxstyle='round,pad=0.01', transform=ax_panel.transAxes,
                                     facecolor='white', alpha=0.92, edgecolor='#111111', lw=1.2, zorder=100))
    ax_panel.text(x_left + box_w/2, y_top - 0.03, title, transform=ax_panel.transAxes,
                  ha='center', va='top', fontsize=10, fontweight='bold', color='black', zorder=101)
    for i, (col, lbl) in enumerate(zip(colours, labels)):
        y = y_top - 0.05 - (i * 0.04)
        ax_panel.add_patch(Rectangle((x_left+0.02, y-0.02), 0.04, 0.03, transform=ax_panel.transAxes,
                                     facecolor=col, edgecolor='#333333', lw=0.5, zorder=102))
        ax_panel.text(x_left+0.07, y-0.005, lbl, transform=ax_panel.transAxes,
                      ha='left', va='center', fontsize=8, color='black', zorder=102)

def add_continuous_legend_panel(ax_panel, arr_masked, cmap_name, label, y_top=0.38, y_bot=0.08, x_left=0.78):
    """Continuous colorbar in a professional boxed inset."""
    from matplotlib.colorbar import ColorbarBase
    from matplotlib.colors import Normalize
    box_w, box_h = 0.20, (y_top - y_bot) + 0.10
    ax_panel.add_patch(FancyBboxPatch((x_left, y_bot-0.02), box_w, box_h, 
                                     boxstyle='round,pad=0.01', transform=ax_panel.transAxes,
                                     facecolor='white', alpha=0.92, edgecolor='#111111', lw=1.2, zorder=100))
    ax_panel.text(x_left + box_w/2, y_top + 0.02, 'Legend', transform=ax_panel.transAxes,
                  ha='center', va='bottom', fontsize=9, fontweight='bold', color='black', zorder=101)
    cb_ax = ax_panel.inset_axes([x_left+0.06, y_bot+0.02, 0.05, y_top-y_bot])
    valid = arr_masked[~np.isnan(arr_masked)]; vmin = float(np.nanmin(valid)); vmax = float(np.nanmax(valid))
    cb = ColorbarBase(cb_ax, cmap=plt.get_cmap(cmap_name), norm=Normalize(vmin=vmin, vmax=vmax), orientation='vertical')
    cb.set_label(label, fontsize=7.5, labelpad=4, fontweight='bold')
    cb.ax.tick_params(labelsize=7); cb_ax.yaxis.set_label_position('right'); cb_ax.yaxis.tick_right()

def apply_dms_grid(ax, utm_extent, n_ticks=4):
    """Grid with de-cluttering: high padding and corner avoidance."""
    x_ticks, x_labels, y_ticks, y_labels = get_dms_ticks(utm_extent, n=n_ticks)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, fontsize=7.5, color='#333333', fontweight='medium')
    ax.tick_params(axis='x', which='both', length=6, direction='in', pad=10, 
                   bottom=True, top=True, labelbottom=True, labeltop=True)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels, rotation=90, va='center', fontsize=7.5, color='#333333', fontweight='medium')
    ax.tick_params(axis='y', which='both', length=6, direction='in', pad=10, 
                   left=True, right=True, labelleft=True, labelright=True)
    ax.grid(True, linestyle=(0, (5, 8)), color='#999999', alpha=0.35, zorder=1)

def finalize_map(fig, ax_map, ax_panel, filename, add_panel_elements=True, source=None):
    """Finalize the map with grid, basemap, neatline, and furniture."""
    ext = basin_extent_padded()
    ax_map.set_xlim(ext[0], ext[1]); ax_map.set_ylim(ext[2], ext[3])
    apply_dms_grid(ax_map, ext)
    for spine in ax_map.spines.values():
        spine.set_linewidth(1.8); spine.set_edgecolor('#1a1a1a')
    if add_panel_elements:
        add_compass_rose_panel(ax_panel)
        add_scale_bar_panel(ax_panel, compute_utm_extent())
    fig.savefig(os.path.join(MAPS_DIR, filename), dpi=220, bbox_inches='tight', facecolor='white')
    plt.close(fig); print(f"  Saved: {filename}")

def finalize_and_save(fig, ax, utm_extent, filename, n_ticks=4):
    """Backward-compat shim updated for the Unified Frame."""
    ax_panel = getattr(fig, '_panel_ax', None)
    if ax_panel: finalize_map(fig, ax, ax_panel, filename)
    else: 
        apply_dms_grid(ax, utm_extent, n_ticks)
        add_compass_rose_panel(ax, cx_pos=0.08, cy_pos=0.15, r=0.05)
        add_scale_bar_panel(ax, utm_extent)
        fig.savefig(os.path.join(MAPS_DIR, filename), dpi=220, bbox_inches='tight')
        plt.close(fig); print(f"  Saved: {filename}")


def safe_normalise(arr, lo_pct=2, hi_pct=98):
    lo = np.nanpercentile(arr, lo_pct)
    hi = np.nanpercentile(arr, hi_pct)
    out = (arr - lo) / (hi - lo + 1e-12)
    out = np.clip(out, 0.0, 1.0)
    out[np.isnan(arr)] = np.nan
    return out


def base_axes(title, figsize=(16, 11)):
    """Unified Frame shim: returns (fig, ax_map, utm_extent)."""
    fig, ax_map, ax_panel = make_map_figure(title, figsize=figsize)
    fig._panel_ax = ax_panel 
    add_esri_basemap(ax_map)
    utm_ext = compute_utm_extent()
    return fig, ax_map, utm_ext

print("Map framework loaded — DESIGN-01 through DESIGN-07 active.")


print("=" * 60)
