# -*- coding: utf-8 -*-
"""
=============================================================================
 SECTIONS 14–18 — ADVANCED HYDROLOGICAL & SOIL-WATER CONSERVATION ANALYSIS
 Pravara River Basin, Maharashtra, India
=============================================================================

 Addon to: adv_v2_morphometry_pravra3basin.py
 Run AFTER Sections 0–13 so the following variables are in memory:
   gdf_sub, gdf_so, gdf_streams, df_master, df_areal, df_relief
   DEM_ARR, FACC_ARR, FDIR_ARR, SLOPE_ARR, HILLSHADE
   DEM_TRANSFORM, DEM_BOUNDS, DEM_RES, DEM_CRS
   UTM_EPSG, ORDER_COL, RASTERS, OUT_DIR, MAPS_DIR,
   PLOTS_DIR, TABLES_DIR, HTML_DIR, SHAPES_DIR
   base_axes, overlay_boundaries, finalize_and_save,
   raster_extent, compute_utm_extent, save_raster,
   save_fig (Plotly helper)

 NEW SECTIONS:
   14 — Runoff Estimation       : SCS-CN, Time of Concentration, Peak Discharge
   15 — RUSLE Soil Erosion Model: R·K·LS·C·P, SDR, Annual Sediment Yield
   16 — Treatment Planning      : Check dam, Percolation tank, Contour trench
   17 — Synthetic Unit Hydrograph: Snyder's & SCS methods
   18 — Stream Channel Hydraulics: Stream power, Shear stress, Stability index

 Regional context:
   Basin  : Pravara River (Godavari sub-basin), Ahmednagar Dist., Maharashtra
   Lat/Lon: ~19.5°N, ~73.8°E  |  CRS: UTM Zone 43N (EPSG:32643)
   Climate: Semi-arid monsoonal — mean annual rainfall ~750 mm (Jun-Sep)
   Geology: Basaltic Deccan Traps — shallow, fine-textured Vertisol/Inceptisol

 References:
   USDA-SCS (1985). Hydrology. National Engineering Handbook, Section 4.
   Wischmeier & Smith (1978). Predicting Rainfall Erosion Losses. USDA-AH537.
   Moore et al. (1991). Digital Terrain Modelling. Hydrol. Processes 5, 3-30.
   Snyder (1938). Synthetic Unit Hydrographs. Trans. AGU 19, 447-454.
   Singh (1988). Hydrologic Systems Vol. I. Prentice-Hall.
   Kirpich (1940). Time of Concentration. Civil Engineering 10(6), 362.
   Mitasova et al. (1996). Modelling topographic potential for erosion.
   Bagnold (1966). An Approach to the Sediment Transport Problem.
   Leopold & Maddock (1953). Hydraulic Geometry. USGS Prof. Paper 252.
=============================================================================
"""

# ── Standard imports (all should already be in memory from Sections 0–13) ────
import os
import warnings
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.mask import mask as rio_mask
from rasterio.transform import rowcol, xy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize, LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import stats
from scipy.ndimage import gaussian_filter, uniform_filter, label as ndlabel
from shapely.geometry import Point, LineString, Polygon
from shapely.ops import linemerge
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

warnings.filterwarnings("ignore")

# ── Output sub-directories ──────────────────────────────────────────────────
HYD_DIR   = os.path.join(OUT_DIR, "hydrology/")
SWC_DIR   = os.path.join(OUT_DIR, "conservation/")
UHG_DIR   = os.path.join(OUT_DIR, "unit_hydrograph/")
HYD_MAPS  = os.path.join(MAPS_DIR, "hydrology/")
SWC_MAPS  = os.path.join(MAPS_DIR, "conservation/")

for d in [HYD_DIR, SWC_DIR, UHG_DIR, HYD_MAPS, SWC_MAPS]:
    os.makedirs(d, exist_ok=True)

print("✅ Output directories created.")

# ─────────────────────────────────────────────────────────────────────────────
# ██████████████████████████████████████████████████████████████████████████
# SECTION 14 — RUNOFF ESTIMATION: SCS-CN, TIME OF CONCENTRATION, PEAK FLOW
# ██████████████████████████████████████████████████████████████████████████
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SECTION 14 — RUNOFF ESTIMATION (SCS-CN + RATIONAL METHOD)")
print("=" * 70)

# ─────────────────────────────────────────────────────────────────────────────
#  A. RAINFALL FREQUENCY ANALYSIS — Gumbel Extreme Value Type-I (EV-I)
# ─────────────────────────────────────────────────────────────────────────────
# Pravara basin (Ahmednagar dist., Maharashtra) historical rainfall statistics
# Source: IMD data / regional studies for Upper Godavari sub-basin
# Mean annual rainfall: 750 mm | Std dev: 187 mm | CV ≈ 0.25

print("\n[14-A] Rainfall Frequency Analysis (Gumbel EV-I)...")

RAIN_MEAN_MM = 750.0   # Mean annual rainfall (mm)
RAIN_STD_MM  = 187.0   # Standard deviation (mm)

# Gumbel EV-I parameters
alpha_g = RAIN_STD_MM * np.sqrt(6) / np.pi          # scale
u_g     = RAIN_MEAN_MM - 0.5772 * alpha_g           # location (mode)

# Return period rainfall (1-day max derived as fraction of annual)
# Ratio of 1-day max to annual: ~0.20-0.25 for semi-arid India
DAILY_FRACTION = 0.22

RETURN_PERIODS = [2, 5, 10, 25, 50, 100]
RAINFALL_RT    = {}   # P24hr [mm] for each return period

gumbel_rows = []
for T in RETURN_PERIODS:
    y_T  = -np.log(-np.log(1 - 1/T))               # Gumbel reduced variate
    P_T  = (u_g + alpha_g * y_T) * DAILY_FRACTION  # 24-hr max rainfall
    P_T  = max(P_T, 10.0)                           # floor at 10 mm
    RAINFALL_RT[T] = round(P_T, 1)
    gumbel_rows.append({'Return_Period_yr': T,
                        'Annual_Rainfall_mm': round(u_g + alpha_g * y_T, 1),
                        'P24hr_mm': round(P_T, 1)})
    print(f"  T={T:4d}-yr: Annual = {u_g + alpha_g * y_T:.0f} mm | "
          f"P24hr = {P_T:.1f} mm")

df_rainfall_freq = pd.DataFrame(gumbel_rows)
df_rainfall_freq.to_csv(os.path.join(HYD_DIR, "rainfall_frequency.csv"), index=False)

# ─────────────────────────────────────────────────────────────────────────────
#  B. CURVE NUMBER MAP — SLOPE-BASED PROXY (no land-use raster available)
# ─────────────────────────────────────────────────────────────────────────────
# CN assigned per pixel using SLOPE class as proxy:
#   Flat  (<  3°): Poorly drained, compacted — CN=85 (soil group C/D)
#   Gentle( 3–8°): Mixed cultivated/fallow   — CN=79 (soil group B/C)
#   Moderate(8–20°): Degraded hill slope     — CN=75 (soil group B)
#   Steep (>20°):  Rock/shallow soil         — CN=70 (soil group A/B)
# These represent typical Deccan Trap basalt conditions under AMC-II.

print("\n[14-B] Computing Curve Number raster...")

CN_ARR = np.full(DEM_ARR.shape, np.nan, dtype=np.float32)
slope_safe = np.where(np.isnan(SLOPE_ARR), 0, SLOPE_ARR)

CN_ARR = np.where(slope_safe <  3,   85.0,
         np.where(slope_safe <  8,   79.0,
         np.where(slope_safe < 20,   75.0,
                                     70.0)))
CN_ARR[np.isnan(DEM_ARR)] = np.nan

# Save CN raster
save_raster(CN_ARR, os.path.join(OUT_DIR, "CN.tif"), RASTERS["dem"])
RASTERS["CN"] = os.path.join(OUT_DIR, "CN.tif")
print(f"  CN range: {np.nanmin(CN_ARR):.0f}–{np.nanmax(CN_ARR):.0f} | "
      f"Mean: {np.nanmean(CN_ARR):.1f}")

# ─────────────────────────────────────────────────────────────────────────────
#  C. SCS-CN DIRECT RUNOFF & PER-BASIN RUNOFF STATISTICS
# ─────────────────────────────────────────────────────────────────────────────

print("\n[14-C] SCS-CN Direct Runoff calculation...")

def scscn_runoff(P_mm, CN):
    """
    SCS-CN direct runoff (Q) for rainfall P [mm] and Curve Number CN.
    Q = (P - 0.2·S)² / (P + 0.8·S)  if P > 0.2·S  else Q = 0
    S = 25400/CN - 254  (potential max retention, mm)
    """
    S = 25400.0 / CN - 254.0          # potential max retention [mm]
    I_a = 0.2 * S                      # initial abstraction [mm]
    valid = P_mm > I_a
    Q = np.where(valid, (P_mm - I_a)**2 / (P_mm + 0.8*S), 0.0)
    return np.maximum(Q, 0.0)

def runoff_coeff(P_mm, CN):
    """Runoff coefficient C = Q/P."""
    Q = scscn_runoff(P_mm, CN)
    return np.where(P_mm > 0, Q / P_mm, 0.0)

# Per-basin: compute CN_mean, S_mean, Q for each return period, runoff volume
RUNOFF_ROWS = []

for _, row in gdf_sub.iterrows():
    bid  = row["basin_id"]
    geom = [row.geometry.__geo_interface__]
    A_km2 = df_areal.loc[bid, "Area_km2"]
    A_m2  = A_km2 * 1e6

    # Clip CN to basin
    with rasterio.open(RASTERS["CN"]) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            cn_clip  = arr_m[0].astype(np.float32)
            cn_clip[cn_clip == -9999.0] = np.nan
        except Exception:
            cn_clip = CN_ARR.copy()

    CN_mean = float(np.nanmean(cn_clip))
    CN_std  = float(np.nanstd(cn_clip))
    S_mean  = 25400.0 / CN_mean - 254.0     # [mm]
    Ia_mean = 0.2 * S_mean                  # initial abstraction [mm]

    r_row = {"basin_id": bid, "CN_mean": round(CN_mean, 2),
             "CN_std": round(CN_std, 2), "S_mm": round(S_mean, 2),
             "Ia_mm": round(Ia_mean, 2), "Area_km2": round(A_km2, 3)}

    for T in RETURN_PERIODS:
        P = RAINFALL_RT[T]
        Q = float(scscn_runoff(P, CN_mean))
        C = float(runoff_coeff(P, CN_mean))
        Vol_Mm3 = Q * 1e-3 * A_m2 / 1e6   # Million cubic metres
        r_row[f"P_{T}yr_mm"]    = P
        r_row[f"Q_{T}yr_mm"]    = round(Q, 2)
        r_row[f"C_{T}yr"]       = round(C, 3)
        r_row[f"Vol_{T}yr_Mm3"] = round(Vol_Mm3, 4)

    RUNOFF_ROWS.append(r_row)
    print(f"  {bid}: CN={CN_mean:.1f} | S={S_mean:.1f} mm | "
          f"Q(25yr)={r_row['Q_25yr_mm']:.1f} mm | "
          f"Vol(25yr)={r_row['Vol_25yr_Mm3']:.4f} Mm³")

df_runoff = pd.DataFrame(RUNOFF_ROWS).set_index("basin_id")
df_runoff.to_csv(os.path.join(HYD_DIR, "runoff_scscn.csv"))

# ─────────────────────────────────────────────────────────────────────────────
#  D. TIME OF CONCENTRATION — KIRPICH, SCS LAG, OVERLAND FLOW
# ─────────────────────────────────────────────────────────────────────────────

print("\n[14-D] Time of Concentration (Tc) calculations...")

def tc_kirpich(L_m, H_m):
    """
    Kirpich (1940): Tc = 0.0195 × L^0.77 × S^-0.385
    L = channel length (m), H = head difference (m)
    S = H/L (dimensionless slope)
    Returns Tc in minutes.
    """
    S = H_m / L_m if L_m > 0 else 0.001
    S = max(S, 0.0001)
    Tc = 0.0195 * (L_m ** 0.77) * (S ** -0.385)
    return Tc  # minutes

def tc_scs_lag(L_m, CN, S_avg_pct):
    """
    SCS Lag method: tL = (L^0.8 × (S+1)^0.7) / (1900 × Y^0.5)
    L = hydraulic length (feet), S = (1000/CN)-10, Y = average watershed slope (%)
    Returns lag time tL in hours; Tc = tL / 0.6
    """
    L_ft = L_m * 3.28084
    S_val = 1000.0 / CN - 10.0
    Y = max(S_avg_pct, 0.1)
    tL = (L_ft**0.8 * (S_val + 1)**0.7) / (1900.0 * Y**0.5)  # hours
    Tc = tL / 0.6
    return Tc * 60  # minutes

def tc_overland(L_m, n_mann, slope_frac, P_mm):
    """
    NRCS Overland Flow Tc (sheet flow):
    Tt = 0.007 × (n×L)^0.8 / (P²^0.5 × S^0.4)
    n = Manning roughness, P2 = 2-year 24-hr rainfall (mm→in)
    Returns Tt in hours; usually only for first 100m of flow.
    """
    P2_in = P_mm * 0.0394
    L_use = min(L_m, 100.0)   # max 100m for sheet flow
    S     = max(slope_frac, 0.001)
    Tt    = 0.007 * ((n_mann * L_use)**0.8) / ((P2_in**0.5) * (S**0.4))
    return Tt * 60  # minutes

TC_ROWS = []

for _, row in gdf_sub.iterrows():
    bid    = row["basin_id"]
    A_km2  = df_areal.loc[bid, "Area_km2"]
    Lb_km  = df_areal.loc[bid, "Basin_Length_km"]
    L_m    = Lb_km * 1000.0
    H_m    = df_relief.loc[bid, "Basin_Relief_H_m"] if bid in df_relief.index else 100.0
    slope_deg = df_relief.loc[bid, "Slope_Mean_deg"] if bid in df_relief.index else 5.0
    slope_pct = np.tan(np.radians(slope_deg)) * 100.0
    slope_frac = slope_pct / 100.0
    CN_mean   = df_runoff.loc[bid, "CN_mean"]
    P2_mm     = RAINFALL_RT[2]   # 2-yr 24-hr rainfall

    Tc_k   = tc_kirpich(L_m, H_m)
    Tc_scs = tc_scs_lag(L_m, CN_mean, slope_pct)
    Tc_ov  = tc_overland(min(L_m, 100), 0.15, slope_frac, P2_mm)
    Tc_avg = np.mean([Tc_k, Tc_scs])   # practical average

    # Rational method peak discharge: Qp = C × i × A / 360
    # i = rainfall intensity at Tc [mm/hr] using Tc in minutes
    # Using Dickens formula common for India: i = a / (Tc + b)
    # Or convert P24hr to intensity using Chen (1983) or Indian standard IDF
    # Indian IMD empirical: i_Tc = P24hr × (24/Tc_hr)^(2/3) / 24  [mm/hr]
    Q_PEAK = {}
    C_rational = {}
    for T in RETURN_PERIODS:
        P24 = RAINFALL_RT[T]
        Tc_hr = Tc_avg / 60.0
        i_Tc  = (P24 / 24.0) * (24.0 / Tc_hr) ** (2.0/3.0)  # mm/hr
        # C (runoff coeff from SCS Q/P for this storm)
        C_val = float(runoff_coeff(P24, CN_mean))
        # Qp [m³/s] = C × i [mm/hr] × A [km²] / 3.6
        Qp = C_val * i_Tc * A_km2 / 3.6
        Q_PEAK[T] = round(Qp, 3)
        C_rational[T] = round(C_val, 3)

    r_tc = {
        "basin_id"     : bid,
        "L_km"         : round(Lb_km, 3),
        "H_m"          : round(H_m, 1),
        "Slope_pct"    : round(slope_pct, 2),
        "Tc_Kirpich_min": round(Tc_k, 1),
        "Tc_SCS_min"   : round(Tc_scs, 1),
        "Tc_Avg_min"   : round(Tc_avg, 1),
        "Tc_hr"        : round(Tc_avg / 60.0, 3),
    }
    for T in RETURN_PERIODS:
        r_tc[f"Qp_{T}yr_m3s"]  = Q_PEAK[T]
        r_tc[f"C_{T}yr"]       = C_rational[T]

    TC_ROWS.append(r_tc)
    print(f"  {bid}: Tc_Kirpich={Tc_k:.1f} min | Tc_SCS={Tc_scs:.1f} min | "
          f"Qp(25yr)={Q_PEAK[25]:.2f} m³/s")

df_tc = pd.DataFrame(TC_ROWS).set_index("basin_id")
df_tc.to_csv(os.path.join(HYD_DIR, "time_of_concentration_peak_discharge.csv"))

# ─────────────────────────────────────────────────────────────────────────────
#  E. RUNOFF MAPS & PLOTLY CHARTS
# ─────────────────────────────────────────────────────────────────────────────

print("\n[14-E] Generating runoff maps...")

# CN map
fig, ax, utm_ext = base_axes("Curve Number (CN) Map — SCS-CN, AMC-II\n"
                              "(Slope-based proxy, Deccan Trap basalt)")
im = ax.imshow(CN_ARR, extent=raster_extent(), origin="upper",
               cmap="RdYlGn_r", alpha=0.80, zorder=1, vmin=68, vmax=88)
overlay_boundaries(ax)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.07)
cb  = plt.colorbar(im, cax=cax)
cb.set_label("Curve Number (CN)", fontsize=10)
# Annotate each basin with CN mean
for _, r in gdf_sub.iterrows():
    bid = r["basin_id"]
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    cn_val = df_runoff.loc[bid, "CN_mean"] if bid in df_runoff.index else np.nan
    ax.text(cx, cy, f"{bid}\nCN={cn_val:.1f}", ha="center", va="center",
            fontsize=8, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
finalize_and_save(fig, ax, utm_ext, "14a_CN_map.png")

# Runoff volume map for 25-yr event
fig, ax, utm_ext = base_axes("Direct Runoff Volume Map — 25-year Return Period Event\n"
                              "(SCS-CN method, per subbasin)")
gdf_rv = gdf_sub.merge(
    df_runoff[["Q_25yr_mm", "Vol_25yr_Mm3", "CN_mean"]].reset_index(),
    on="basin_id", how="left"
)
gdf_rv.plot(column="Vol_25yr_Mm3", ax=ax, cmap="Blues", legend=True, alpha=0.80,
            zorder=2, edgecolor="black", linewidth=1.2,
            legend_kwds={"label": "Runoff Volume (Mm³)", "shrink": 0.75})
for _, r in gdf_rv.iterrows():
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    ax.text(cx, cy,
            f"{r['basin_id']}\nQ={r['Q_25yr_mm']:.0f} mm\n{r['Vol_25yr_Mm3']:.3f} Mm³",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.7, alpha=0.5, zorder=5)
finalize_and_save(fig, ax, utm_ext, "14b_runoff_volume_25yr.png")

# Plotly: multi-return-period peak discharge comparison
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Peak Discharge by Return Period (m³/s)",
                                    "Runoff Depth by Return Period (mm)"])
colors_rt = px.colors.qualitative.Set1
for i, bid in enumerate(df_tc.index):
    qp_vals = [df_tc.loc[bid, f"Qp_{T}yr_m3s"] for T in RETURN_PERIODS]
    q_vals  = [df_runoff.loc[bid, f"Q_{T}yr_mm"] for T in RETURN_PERIODS]
    fig.add_trace(go.Scatter(
        x=RETURN_PERIODS, y=qp_vals, mode="lines+markers",
        name=bid, line=dict(color=colors_rt[i % 9], width=2),
        marker=dict(size=8), legendgroup=bid,
        hovertemplate=f"{bid}<br>T=%{{x}} yr<br>Qp=%{{y:.2f}} m³/s",
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=RETURN_PERIODS, y=q_vals, mode="lines+markers",
        name=bid, line=dict(color=colors_rt[i % 9], dash="dot", width=2),
        marker=dict(size=8), legendgroup=bid, showlegend=False,
        hovertemplate=f"{bid}<br>T=%{{x}} yr<br>Q=%{{y:.2f}} mm",
    ), row=1, col=2)

fig.update_xaxes(type="log", title_text="Return Period (yr)", row=1, col=1)
fig.update_xaxes(type="log", title_text="Return Period (yr)", row=1, col=2)
fig.update_yaxes(title_text="Peak Discharge (m³/s)", row=1, col=1)
fig.update_yaxes(title_text="Runoff Depth Q (mm)", row=1, col=2)
fig.update_layout(title="Flood Frequency Curves — Pravara Subbasins",
                  template="plotly_white", height=500)
save_fig(fig, "14c_flood_frequency_curves")
print("\n✅ SECTION 14 complete.")

# ─────────────────────────────────────────────────────────────────────────────
# ██████████████████████████████████████████████████████████████████████████
# SECTION 15 — RUSLE SOIL EROSION MODEL
# ██████████████████████████████████████████████████████████████████████████
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SECTION 15 — RUSLE SOIL EROSION ESTIMATION")
print("=" * 70)

# RUSLE:  A = R × K × LS × C × P
# A  = Annual average soil loss (t/ha/yr)
# R  = Rainfall-runoff erosivity factor (MJ·mm/ha·hr·yr)
# K  = Soil erodibility factor (t·ha·hr/ha·MJ·mm)
# LS = Slope length-gradient factor (dimensionless)
# C  = Cover-management factor (dimensionless, 0–1)
# P  = Support practice factor (dimensionless, 0–1)

# ─────────────────────────────────────────────────────────────────────────────
#  A. R-FACTOR — Erosivity
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-A] R-Factor (Rainfall Erosivity)...")
# Maharashtra Deccan Trap region: R ≈ 550–800 MJ·mm/(ha·hr·yr)
# Pravara catchment (Ahmednagar): R ≈ 650 MJ·mm/(ha·hr·yr)
# Spatial variation modelled as: R = R0 × (1 + 0.05 × (elev - elev_mean)/elev_std)
# (higher elevations get slightly higher R due to orographic rainfall)

R0       = 650.0
elev_mean = np.nanmean(DEM_ARR)
elev_std  = np.nanstd(DEM_ARR)

R_ARR = R0 * (1.0 + 0.05 * (DEM_ARR - elev_mean) / (elev_std + 1e-6))
R_ARR = np.clip(R_ARR, 400.0, 1000.0)
R_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(R_ARR.astype(np.float32), os.path.join(OUT_DIR, "RUSLE_R.tif"), RASTERS["dem"])
RASTERS["RUSLE_R"] = os.path.join(OUT_DIR, "RUSLE_R.tif")
print(f"  R-factor range: {np.nanmin(R_ARR):.0f}–{np.nanmax(R_ARR):.0f} "
      f"MJ·mm/(ha·hr·yr) | Mean: {np.nanmean(R_ARR):.0f}")

# ─────────────────────────────────────────────────────────────────────────────
#  B. K-FACTOR — Soil Erodibility
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-B] K-Factor (Soil Erodibility)...")
# Deccan Trap basalt → Vertisols + Inceptisols
# K ranges: Vertisol (clay-rich) 0.10–0.20; Shallow rocky 0.05–0.10
# Proxy using slope: steeper slopes → shallower soil → lower K (rocky)
# Flat/gentle → deep Vertisol → higher K

K_ARR = np.where(slope_safe <  3,  0.25,   # Deep Vertisol (fine clay, flat)
         np.where(slope_safe <  8,  0.20,   # Vertic Inceptisol
         np.where(slope_safe < 15,  0.15,   # Shallow Alfisol
         np.where(slope_safe < 25,  0.10,   # Lithic Inceptisol (stony)
                                   0.05)))).astype(np.float32)  # Rock/talus
K_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(K_ARR, os.path.join(OUT_DIR, "RUSLE_K.tif"), RASTERS["dem"])
RASTERS["RUSLE_K"] = os.path.join(OUT_DIR, "RUSLE_K.tif")
print(f"  K-factor range: {np.nanmin(K_ARR):.2f}–{np.nanmax(K_ARR):.2f} "
      f"t·ha·hr/(ha·MJ·mm) | Mean: {np.nanmean(K_ARR):.3f}")

# ─────────────────────────────────────────────────────────────────────────────
#  C. LS-FACTOR — Slope Length-Gradient
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-C] LS-Factor (Slope-Length Gradient, Moore et al. 1991)...")
# Moore et al. (1991) LS from flow accumulation (As) and slope:
#   LS = (As/22.13)^m × (sin(β)/0.0896)^n
# where As = specific catchment area (m²/m) = flow_acc × cell_size
# m = 0.6 (rill erosion, semi-arid), n = 1.3
# This formulation handles divergent/convergent flow better than Wischmeier's L.

cell_area_m2 = DEM_RES * DEM_RES
fa_safe  = np.where(np.isnan(FACC_ARR), 0, np.maximum(FACC_ARR, 1))
As_arr   = fa_safe * DEM_RES                # specific catchment area m²/m
slope_rad = np.radians(np.where(np.isnan(SLOPE_ARR), 0.01, SLOPE_ARR))
slope_rad = np.maximum(slope_rad, np.radians(0.01))  # min 0.01° to avoid log issues

m_exp = 0.6
n_exp = 1.3
LS_ARR = ((As_arr / 22.13) ** m_exp) * ((np.sin(slope_rad) / 0.0896) ** n_exp)
LS_ARR = np.clip(LS_ARR, 0.0, 50.0)       # cap to avoid extreme values on cliffs
LS_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(LS_ARR.astype(np.float32), os.path.join(OUT_DIR, "RUSLE_LS.tif"), RASTERS["dem"])
RASTERS["RUSLE_LS"] = os.path.join(OUT_DIR, "RUSLE_LS.tif")
print(f"  LS-factor range: {np.nanmin(LS_ARR):.2f}–{np.nanmax(LS_ARR):.2f} | "
      f"Mean: {np.nanmean(LS_ARR):.2f}")

# ─────────────────────────────────────────────────────────────────────────────
#  D. C-FACTOR — Cover-Management
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-D] C-Factor (Cover-Management)...")
# No land-use raster: use slope + elevation proxy for cover quality
# Flat lowlands (cultivated, Rabi/Kharif crops): C = 0.15–0.25
# Moderate slopes (degraded dryland agriculture): C = 0.25–0.40
# Steep slopes (sparse scrub/bare basalt): C = 0.40–0.60
# Very steep / ridges (bare rock): C = 0.10–0.20 (less soil to erode)

C_ARR = np.where(slope_safe <  3,  0.20,   # Irrigated/Rabi crops in flat areas
         np.where(slope_safe <  8,  0.30,   # Rainfed Kharif crops
         np.where(slope_safe < 15,  0.45,   # Degraded rangeland/scrub
         np.where(slope_safe < 25,  0.55,   # Sparse vegetation / bare patches
                                   0.15)))).astype(np.float32)  # Rocky ridge (low erosion)
C_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(C_ARR, os.path.join(OUT_DIR, "RUSLE_C.tif"), RASTERS["dem"])
RASTERS["RUSLE_C"] = os.path.join(OUT_DIR, "RUSLE_C.tif")
print(f"  C-factor range: {np.nanmin(C_ARR):.2f}–{np.nanmax(C_ARR):.2f} | "
      f"Mean: {np.nanmean(C_ARR):.3f}")

# ─────────────────────────────────────────────────────────────────────────────
#  E. P-FACTOR — Support Practice
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-E] P-Factor (Support Practice)...")
# Maharashtra farmers on steep slopes use traditional bunding (terracing)
# Flat (<3°) : cultivated flat fields, no terracing needed → P = 1.0
# Gentle–Moderate (3–20°): traditional tied ridges / broad-based bunds → P = 0.6
# Steep (>20°): bench terracing or no practice → P = 0.8
# Very steep (>30°): grassland / no effective practice → P = 1.0

P_ARR = np.where(slope_safe <  3,  1.00,
         np.where(slope_safe <  8,  0.55,   # Contour cultivation + bunding
         np.where(slope_safe < 15,  0.65,   # Graded bunding
         np.where(slope_safe < 25,  0.80,   # Bench terrace
                                   1.00)))).astype(np.float32)
P_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(P_ARR, os.path.join(OUT_DIR, "RUSLE_P.tif"), RASTERS["dem"])
RASTERS["RUSLE_P"] = os.path.join(OUT_DIR, "RUSLE_P.tif")
print(f"  P-factor range: {np.nanmin(P_ARR):.2f}–{np.nanmax(P_ARR):.2f} | "
      f"Mean: {np.nanmean(P_ARR):.3f}")

# ─────────────────────────────────────────────────────────────────────────────
#  F. ANNUAL SOIL LOSS (A) — RUSLE
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-F] Computing Annual Soil Loss raster A = R·K·LS·C·P ...")

A_ARR = R_ARR * K_ARR * LS_ARR * C_ARR * P_ARR     # t/ha/yr
A_ARR = np.clip(A_ARR, 0.0, 500.0)                 # cap extreme values
A_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(A_ARR.astype(np.float32), os.path.join(OUT_DIR, "RUSLE_A.tif"), RASTERS["dem"])
RASTERS["RUSLE_A"] = os.path.join(OUT_DIR, "RUSLE_A.tif")
print(f"  Annual soil loss range: {np.nanmin(A_ARR):.1f}–{np.nanmax(A_ARR):.0f} t/ha/yr")
print(f"  Basin-wide mean: {np.nanmean(A_ARR):.1f} t/ha/yr")

# ── USDA soil loss class thresholds (t/ha/yr) ────────────────────────────────
# Slight <5 | Moderate 5-15 | High 15-30 | Very High 30-60 | Severe >60
SOIL_LOSS_CLASSES = [
    (0,   5,  "Slight (<5)",        "#1a9641"),
    (5,  15,  "Moderate (5-15)",    "#a6d96a"),
    (15, 30,  "High (15-30)",       "#fdae61"),
    (30, 60,  "Very High (30-60)",  "#d7191c"),
    (60, 999, "Severe (>60)",       "#7f0000"),
]

def classify_soil_loss(val):
    for lo, hi, name, _ in SOIL_LOSS_CLASSES:
        if lo <= val < hi:
            return name
    return "Severe (>60)"

# ─────────────────────────────────────────────────────────────────────────────
#  G. SEDIMENT DELIVERY RATIO (SDR) & ANNUAL SEDIMENT YIELD
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-G] Sediment Delivery Ratio & Annual Sediment Yield...")

# SDR = 0.417 × A^(-0.3) (Vanoni, 1975 — area in km²)
# Also: SDR = exp(-1.58 + 0.46 × ln(slope%) - 0.19 × ln(A_km²))
# We use Renfro (1975) formula: SDR = 0.42 × A_km2^(-0.125)

RUSLE_ROWS = []

for _, row in gdf_sub.iterrows():
    bid  = row["basin_id"]
    geom = [row.geometry.__geo_interface__]
    A_km2 = df_areal.loc[bid, "Area_km2"]

    # Clip A raster
    with rasterio.open(RASTERS["RUSLE_A"]) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            a_clip   = arr_m[0].astype(np.float32)
            a_clip[a_clip == -9999.0] = np.nan
        except Exception:
            a_clip   = A_ARR.copy()

    valid_a = a_clip[~np.isnan(a_clip)]
    if len(valid_a) == 0:
        continue

    A_mean = float(np.nanmean(valid_a))    # t/ha/yr
    A_max  = float(np.nanpercentile(valid_a, 95))

    # Total gross erosion (t/yr): A_mean [t/ha/yr] × Area [ha]
    A_ha   = A_km2 * 100.0
    Gross_erosion_t_yr = A_mean * A_ha

    # SDR
    SDR = 0.42 * (A_km2 ** -0.125)
    SDR = min(SDR, 0.80)

    # Annual sediment yield
    Sed_yield_t_yr   = Gross_erosion_t_yr * SDR
    Sed_yield_Mm3_yr = Sed_yield_t_yr / (1300 * 1000)  # assuming bulk density 1.3 t/m³

    # Area fraction per soil loss class
    class_fracs = {}
    for lo, hi, name, _ in SOIL_LOSS_CLASSES:
        frac = float(np.sum((valid_a >= lo) & (valid_a < hi))) / len(valid_a)
        class_fracs[name] = round(frac * 100, 1)

    RUSLE_ROWS.append({
        "basin_id"              : bid,
        "A_mean_t_ha_yr"        : round(A_mean, 2),
        "A_p95_t_ha_yr"         : round(A_max, 2),
        "Area_ha"               : round(A_ha, 1),
        "Gross_Erosion_t_yr"    : round(Gross_erosion_t_yr, 0),
        "SDR"                   : round(SDR, 3),
        "Sed_Yield_t_yr"        : round(Sed_yield_t_yr, 0),
        "Sed_Yield_Mm3_yr"      : round(Sed_yield_Mm3_yr, 6),
        "Loss_Class_Mode"       : classify_soil_loss(A_mean),
        **{f"Pct_{k}": v for k, v in class_fracs.items()},
    })
    print(f"  {bid}: A_mean={A_mean:.1f} t/ha/yr | SDR={SDR:.3f} | "
          f"Sed.Yield={Sed_yield_t_yr:.0f} t/yr | Class: {classify_soil_loss(A_mean)}")

df_rusle = pd.DataFrame(RUSLE_ROWS).set_index("basin_id")
df_rusle.to_csv(os.path.join(HYD_DIR, "RUSLE_soil_erosion.csv"))

# ─────────────────────────────────────────────────────────────────────────────
#  H. RUSLE MAPS
# ─────────────────────────────────────────────────────────────────────────────

print("\n[15-H] Generating RUSLE maps...")

# LS-factor map
fig, ax, utm_ext = base_axes("RUSLE LS-Factor Map\n(Moore et al. 1991: "
                              "Slope-Length × Gradient combined)")
im = ax.imshow(LS_ARR, extent=raster_extent(), origin="upper",
               cmap="YlOrRd", alpha=0.80, zorder=1,
               vmin=0, vmax=np.nanpercentile(LS_ARR, 97))
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.2, zorder=10)
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.6, alpha=0.5, zorder=8)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.07)
cb  = plt.colorbar(im, cax=cax)
cb.set_label("LS Factor (dimensionless)", fontsize=10)
finalize_and_save(fig, ax, utm_ext, "15a_LS_factor.png")

# Annual soil loss map
fig, ax, utm_ext = base_axes("Annual Soil Loss Map (RUSLE: A = R·K·LS·C·P)\n"
                              "(tonnes/ha/year)")
# Custom classified colormap
boundaries_sl = [0, 5, 15, 30, 60, 500]
colors_sl     = ["#1a9641", "#a6d96a", "#fdae61", "#d7191c", "#7f0000"]
cmap_sl       = mcolors.BoundaryNorm(boundaries_sl, len(colors_sl))
cmap_sl_obj   = LinearSegmentedColormap.from_list("sl", colors_sl, N=len(colors_sl))
norm_sl       = mcolors.BoundaryNorm(boundaries_sl, cmap_sl_obj.N)

im = ax.imshow(A_ARR, extent=raster_extent(), origin="upper",
               cmap=cmap_sl_obj, norm=norm_sl, alpha=0.80, zorder=1)
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.2, zorder=10)
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.6, alpha=0.5, zorder=8)
patches_sl = [mpatches.Patch(color=c, label=n)
              for _, _, n, c in SOIL_LOSS_CLASSES]
ax.legend(handles=patches_sl, loc="lower left", fontsize=8,
          title="Soil Loss Class (t/ha/yr)", title_fontsize=9, framealpha=0.9)
# Annotate basins
for _, r in gdf_sub.iterrows():
    bid = r["basin_id"]
    if bid in df_rusle.index:
        cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
        ax.text(cx, cy,
                f"{bid}\n{df_rusle.loc[bid,'A_mean_t_ha_yr']:.1f} t/ha/yr\n"
                f"{df_rusle.loc[bid,'Loss_Class_Mode']}",
                ha="center", va="center", fontsize=7, fontweight="bold",
                path_effects=[pe.withStroke(linewidth=2, foreground="white")])
finalize_and_save(fig, ax, utm_ext, "15b_RUSLE_soil_loss.png")

# Sediment yield bar chart (Plotly)
df_rusle_reset = df_rusle.reset_index()
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Annual Soil Loss (t/ha/yr) per Basin",
                                    "Sediment Yield (t/yr) per Basin"])
colors_b = ["#d73027", "#fdae61", "#1a9641", "#4575b4", "#762a83"]
for i, row_ in df_rusle_reset.iterrows():
    fig.add_trace(go.Bar(
        x=[row_["basin_id"]], y=[row_["A_mean_t_ha_yr"]],
        marker_color=colors_b[i % 5],
        text=f"{row_['A_mean_t_ha_yr']:.1f}", textposition="outside",
        name=row_["basin_id"],
        hovertemplate=(f"{row_['basin_id']}<br>"
                       f"Mean Loss: {row_['A_mean_t_ha_yr']:.1f} t/ha/yr<br>"
                       f"Class: {row_['Loss_Class_Mode']}"),
    ), row=1, col=1)
    fig.add_trace(go.Bar(
        x=[row_["basin_id"]], y=[row_["Sed_Yield_t_yr"]],
        marker_color=colors_b[i % 5],
        text=f"{row_['Sed_Yield_t_yr']:.0f}", textposition="outside",
        name=row_["basin_id"], showlegend=False,
        hovertemplate=(f"{row_['basin_id']}<br>"
                       f"Sediment Yield: {row_['Sed_Yield_t_yr']:.0f} t/yr<br>"
                       f"SDR: {row_['SDR']:.3f}"),
    ), row=1, col=2)

# USDA threshold lines
for T_val, label in [(5, "Slight/Moderate"), (15, "Moderate/High"),
                      (30, "High/Very High"), (60, "Very High/Severe")]:
    fig.add_hline(y=T_val, line_dash="dash", line_color="grey",
                  annotation_text=label, annotation_position="right",
                  annotation_font_size=9, row=1, col=1)

fig.update_yaxes(title_text="Mean Annual Soil Loss (t/ha/yr)", row=1, col=1)
fig.update_yaxes(title_text="Annual Sediment Yield (t/yr)", row=1, col=2)
fig.update_layout(title="RUSLE Erosion Results — Pravara Subbasins",
                  template="plotly_white", height=500, showlegend=False)
save_fig(fig, "15c_RUSLE_erosion_bars")

# RUSLE factor comparison radar (Plotly)
factor_cols_r = ["A_mean_t_ha_yr", "SDR", "Gross_Erosion_t_yr"]
fig_r = go.Figure()
for i, (bid, row_) in enumerate(df_rusle.iterrows()):
    val_r = [df_rusle.loc[bid, c] for c in factor_cols_r]
    val_r_n = [(v - df_rusle[c].min()) / (df_rusle[c].max() - df_rusle[c].min() + 1e-9)
               for v, c in zip(val_r, factor_cols_r)]
    val_r_n += [val_r_n[0]]
    cats = ["Soil Loss", "SDR", "Gross Erosion", "Soil Loss"]
    fig_r.add_trace(go.Scatterpolar(
        r=val_r_n, theta=cats, fill="toself", name=bid, opacity=0.7,
        line_color=px.colors.qualitative.Set1[i % 9]))

fig_r.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                    title="RUSLE Erosion Signature — Normalised per Subbasin",
                    template="plotly_white", height=500)
save_fig(fig_r, "15d_RUSLE_radar")
print("\n✅ SECTION 15 complete.")

# ─────────────────────────────────────────────────────────────────────────────
# ██████████████████████████████████████████████████████████████████████████
# SECTION 16 — WATERSHED TREATMENT PLANNING (SOIL & WATER CONSERVATION)
# ██████████████████████████████████████████████████████████████████████████
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SECTION 16 — WATERSHED TREATMENT PLANNING")
print("(Check Dams, Percolation Tanks, Contour Trenches, Priority Zones)")
print("=" * 70)

# ─────────────────────────────────────────────────────────────────────────────
#  A. CHECK DAM SUITABILITY INDEX (CDSI)
# ─────────────────────────────────────────────────────────────────────────────
# Check dam (naala bund / gully plug) suitability criteria:
#  1. Stream order: 1st–2nd order preferred (scores: ord1=10, ord2=8, ord3=5, ord4+=2)
#  2. Upstream catchment area: 0.5–10 km² optimal (score 10), beyond that less suitable
#  3. Valley cross-section (Vf): 0.3–1.5 ideal (narrow V-shape; score inversely with Vf)
#  4. Channel slope: 1–5% optimal for sediment trapping (too flat = silts up; too steep = washout)
#  5. RUSLE A-index: High erosion upstream = high benefit (score ~A/Amax)

print("\n[16-A] Computing Check Dam Suitability Index...")

def score_stream_order(order):
    """Score stream order 1–6 for check dam suitability (1st order = best)."""
    return max(0, 10 - (order - 1) * 2.5)   # 10, 7.5, 5.0, 2.5, 0...

def score_catchment_area(A_km2):
    """0.5–10 km² is optimal for check dams."""
    if   0.1 <= A_km2 <= 0.5:  return 6
    elif 0.5 <  A_km2 <= 5.0:  return 10
    elif 5.0 <  A_km2 <= 15.0: return 7
    elif A_km2 > 15.0:          return 3
    return 4

def score_channel_slope(slope_pct):
    """1–5% channel slope is optimal."""
    if   slope_pct < 0.5:  return 3   # Too flat → rapid silting
    elif slope_pct < 1.0:  return 6
    elif slope_pct < 5.0:  return 10  # Optimal
    elif slope_pct < 10.0: return 7
    elif slope_pct < 20.0: return 4
    return 2                           # Too steep → unstable

def score_valley_vf(Vf):
    """Vf 0.3–1.5 ideal (narrow V = easy to block; very wide = costly)."""
    if np.isnan(Vf):        return 5
    if   Vf < 0.3:          return 6   # Very narrow — ok but hard to construct
    elif Vf < 1.5:          return 10  # Ideal
    elif Vf < 3.0:          return 7
    elif Vf < 6.0:          return 4
    return 2                            # Very wide valley — not suitable

# For each stream segment, compute CDSI
gdf_cd = gdf_so.copy()
gdf_cd["stream_length_m"] = gdf_cd.geometry.length

# Upstream catchment area from flow accumulation at segment midpoint
def sample_facc_at_midpoint(geom, facc_arr, transform):
    """Sample flow accumulation at segment midpoint."""
    try:
        mid_pt = geom.interpolate(0.5, normalized=True)
        r_i, c_i = rowcol(transform, mid_pt.x, mid_pt.y)
        if 0 <= r_i < facc_arr.shape[0] and 0 <= c_i < facc_arr.shape[1]:
            return float(facc_arr[r_i, c_i])
    except Exception:
        pass
    return np.nan

def sample_slope_at_segment(geom, slope_arr, transform):
    """Mean slope along segment."""
    try:
        pts = [geom.interpolate(f, normalized=True) for f in np.linspace(0.1, 0.9, 7)]
        slopes = []
        for pt in pts:
            r_i, c_i = rowcol(transform, pt.x, pt.y)
            if 0 <= r_i < slope_arr.shape[0] and 0 <= c_i < slope_arr.shape[1]:
                s = slope_arr[r_i, c_i]
                if not np.isnan(s):
                    slopes.append(s)
        return float(np.nanmean(slopes)) if slopes else np.nan
    except Exception:
        return np.nan

# Sample FAcc and slope for each segment
print("  Sampling flow accumulation and slope at stream segments...")
fa_vals    = []
slope_segs = []
for _, seg in gdf_cd.iterrows():
    geom = seg.geometry
    if geom.geom_type == "MultiLineString":
        geom = max(geom.geoms, key=lambda g: g.length)
    fa_vals.append(sample_facc_at_midpoint(geom, FACC_ARR, DEM_TRANSFORM))
    slope_segs.append(sample_slope_at_segment(geom, SLOPE_ARR, DEM_TRANSFORM))

gdf_cd["FA_cells"]    = fa_vals
gdf_cd["seg_slope_deg"] = slope_segs
gdf_cd["A_upstream_km2"] = (gdf_cd["FA_cells"] * DEM_RES * DEM_RES / 1e6).clip(lower=0)
gdf_cd["seg_slope_pct"]  = np.tan(np.radians(gdf_cd["seg_slope_deg"].fillna(5))) * 100

# RUSLE A-score: mean soil loss in 2km upstream buffer of segment
def sample_rusle_upstream(geom, a_arr, transform, buffer_m=1000):
    """Mean RUSLE A in buffer around segment endpoints."""
    try:
        start_pt = Point(geom.coords[0])
        buffered = start_pt.buffer(buffer_m)
        geom_list = [buffered.__geo_interface__]
        with rasterio.open(RASTERS["RUSLE_A"]) as src:
            arr_m, _ = rio_mask(src, geom_list, crop=True, nodata=np.nan)
            vals = arr_m[0][arr_m[0] > 0]
            return float(np.nanmean(vals)) if len(vals) > 0 else np.nan
    except Exception:
        return np.nan

# Compute RUSLE score per segment (sample a subset for speed)
A_max_basin = float(np.nanpercentile(A_ARR, 95))
gdf_cd["A_upstream_mean"] = np.nan
for idx in gdf_cd.index:
    geom = gdf_cd.loc[idx, "geometry"]
    if geom.geom_type == "MultiLineString":
        geom = max(geom.geoms, key=lambda g: g.length)
    val = sample_rusle_upstream(geom, A_ARR, DEM_TRANSFORM, buffer_m=500)
    gdf_cd.at[idx, "A_upstream_mean"] = val

# Score each component
gdf_cd["S_order"]    = gdf_cd[ORDER_COL].apply(score_stream_order)
gdf_cd["S_area"]     = gdf_cd["A_upstream_km2"].apply(score_catchment_area)
gdf_cd["S_slope"]    = gdf_cd["seg_slope_pct"].apply(score_channel_slope)
gdf_cd["S_erosion"]  = (gdf_cd["A_upstream_mean"].fillna(A_max_basin/2) /
                         (A_max_basin + 1e-6) * 10).clip(0, 10)

# Get Vf from df_Vf if available, else use default
try:
    gdf_cd_sub = gpd.sjoin(gdf_cd, gdf_sub[["basin_id","geometry"]],
                            how="left", predicate="intersects")
    gdf_cd_sub = gdf_cd_sub.drop_duplicates(subset=gdf_cd_sub.index.name or gdf_cd.index.name)
    if "basin_id" not in gdf_cd_sub.columns:
        gdf_cd["S_vf"] = 5.0
    else:
        def get_vf_for_basin(bid):
            if bid in df_Vf.index:
                return score_valley_vf(df_Vf.loc[bid, "Vf"])
            return 5.0
        gdf_cd["S_vf"] = gdf_cd_sub["basin_id"].apply(
            lambda b: get_vf_for_basin(b) if pd.notna(b) else 5.0).values
except Exception:
    gdf_cd["S_vf"] = 5.0

# Weighted CDSI (weights reflect relative importance for check dam selection)
W = {"order": 0.30, "area": 0.25, "slope": 0.20, "erosion": 0.15, "vf": 0.10}
gdf_cd["CDSI"] = (W["order"]   * gdf_cd["S_order"]   +
                   W["area"]    * gdf_cd["S_area"]    +
                   W["slope"]   * gdf_cd["S_slope"]   +
                   W["erosion"] * gdf_cd["S_erosion"] +
                   W["vf"]      * gdf_cd["S_vf"])
gdf_cd["CDSI"] = gdf_cd["CDSI"].clip(0, 10)

# Classification
def cdsi_class(v):
    if v >= 7.5: return "Very Suitable"
    if v >= 5.5: return "Suitable"
    if v >= 3.5: return "Moderately Suitable"
    return "Poorly Suitable"

gdf_cd["CDSI_class"] = gdf_cd["CDSI"].apply(cdsi_class)

print("  CDSI distribution:")
print(gdf_cd["CDSI_class"].value_counts().to_string())
gdf_cd[["CDSI","CDSI_class","A_upstream_km2","seg_slope_pct",
         ORDER_COL]].to_csv(os.path.join(SWC_DIR, "checkdam_suitability.csv"))
gdf_cd.to_file(os.path.join(SHAPES_DIR, "checkdam_suitability.shp"))

# ─────────────────────────────────────────────────────────────────────────────
#  B. PERCOLATION POND / RECHARGE ZONE SUITABILITY
# ─────────────────────────────────────────────────────────────────────────────

print("\n[16-B] Percolation Pond & Groundwater Recharge Zones...")
# Criteria: high TWI (water accumulates), low slope (<5°),
#           moderate FA (not first-order headwaters, not mainstem)
#           away from steep erosive zones

TWI_safe2  = np.where(np.isnan(TWI_ARR), np.nanmin(TWI_ARR), TWI_ARR)
FA_norm    = np.log1p(np.where(np.isnan(FACC_ARR), 0, FACC_ARR))
FA_norm    = FA_norm / (np.nanmax(FA_norm) + 1e-9)
slope_n2   = 1.0 - (slope_safe / (np.nanmax(slope_safe) + 1e-9))  # inverted — flat preferred

# TWI normalised
TWI_n      = (TWI_safe2 - np.nanmin(TWI_safe2)) / (np.nanmax(TWI_safe2) - np.nanmin(TWI_safe2) + 1e-9)

# Filter to gentle slopes
mask_flat  = (slope_safe < 5.0).astype(float)
mask_flat[np.isnan(DEM_ARR)] = np.nan

PERC_ARR   = (TWI_n * 0.50 + FA_norm * 0.30 + slope_n2 * 0.20) * mask_flat
PERC_ARR[np.isnan(DEM_ARR)] = np.nan
PERC_ARR   = np.clip(PERC_ARR, 0, 1)

save_raster(PERC_ARR.astype(np.float32), os.path.join(OUT_DIR, "percolation_potential.tif"), RASTERS["dem"])
RASTERS["percolation"] = os.path.join(OUT_DIR, "percolation_potential.tif")
print(f"  Percolation potential range: {np.nanmin(PERC_ARR):.3f}–{np.nanmax(PERC_ARR):.3f}")

# ─────────────────────────────────────────────────────────────────────────────
#  C. CONTOUR TRENCH SUITABILITY
# ─────────────────────────────────────────────────────────────────────────────

print("\n[16-C] Contour Trench Suitability...")
# Contour trenches (staggered trenches across slope) work best where:
#  • Slope: 3–30° (too flat = no runoff to harvest; too steep = unstable)
#  • High RUSLE A (high erosion = high benefit from trenches)
#  • Not on stream channels (avoid blocking channels)
#  • Moderate soil depth (not rocky)

slope_ok    = ((slope_safe >= 3) & (slope_safe < 30)).astype(float)
A_norm_c    = np.clip(A_ARR / (A_max_basin + 1e-9), 0, 1)
A_norm_c    = np.where(np.isnan(A_norm_c), 0, A_norm_c)

# Penalise cells on channels (high flow accumulation)
FA_threshold = 500  # cells — anything above is a channel
not_channel = (FACC_ARR < FA_threshold).astype(float)
not_channel[np.isnan(FACC_ARR)] = 1.0

CT_ARR = (slope_ok * 0.40 + A_norm_c * 0.40 + not_channel * 0.20)
CT_ARR[np.isnan(DEM_ARR)] = np.nan
CT_ARR = np.clip(CT_ARR, 0, 1)

save_raster(CT_ARR.astype(np.float32), os.path.join(OUT_DIR, "contour_trench_suitability.tif"), RASTERS["dem"])
RASTERS["contour_trench"] = os.path.join(OUT_DIR, "contour_trench_suitability.tif")
print(f"  Contour trench suitability range: {np.nanmin(CT_ARR):.3f}–{np.nanmax(CT_ARR):.3f}")

# ─────────────────────────────────────────────────────────────────────────────
#  D. PER-BASIN CONSERVATION SUMMARY & WATER HARVESTING POTENTIAL (WHP)
# ─────────────────────────────────────────────────────────────────────────────

print("\n[16-D] Per-basin conservation statistics & Water Harvesting Potential...")

WHP_ROWS = []

for _, row in gdf_sub.iterrows():
    bid  = row["basin_id"]
    geom = [row.geometry.__geo_interface__]
    A_km2 = df_areal.loc[bid, "Area_km2"]

    def clip_and_stats(raster_path):
        with rasterio.open(raster_path) as src:
            try:
                arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
                arr = arr_m[0].astype(np.float32)
                arr[arr == -9999.0] = np.nan
                return arr
            except Exception:
                return np.array([np.nan])

    perc_clip = clip_and_stats(RASTERS["percolation"])
    ct_clip   = clip_and_stats(RASTERS["contour_trench"])
    cn_clip   = clip_and_stats(RASTERS["CN"])
    q_25yr_mm = df_runoff.loc[bid, "Q_25yr_mm"] if bid in df_runoff.index else np.nan

    # WHP = potential runoff harvestable volume (25-yr event, m³)
    # Adjusting for realistic harvesting fraction (0.4 = 40% captured)
    harvest_frac = 0.40
    WHP_m3       = float(q_25yr_mm) * 1e-3 * A_km2 * 1e6 * harvest_frac

    # Check dam count potential: every 500–1000m on 1st–2nd order streams
    n_suitable = int((gdf_cd[gdf_cd["CDSI_class"].isin(["Very Suitable", "Suitable"])]
                       .geometry.length.sum() / 700.0))

    WHP_ROWS.append({
        "basin_id"              : bid,
        "Perc_Potential_mean"   : round(float(np.nanmean(perc_clip)), 3),
        "Perc_Potential_p75"    : round(float(np.nanpercentile(perc_clip[~np.isnan(perc_clip)], 75)
                                              if np.any(~np.isnan(perc_clip)) else np.nan), 3),
        "ContourTrench_mean"    : round(float(np.nanmean(ct_clip)), 3),
        "Pct_CT_suitable"       : round(float(np.nanmean(ct_clip > 0.5)) * 100, 1),
        "WHP_25yr_Mm3"          : round(WHP_m3 / 1e6, 4),
        "Potential_CheckDams_N" : n_suitable,
        "CN_mean"               : round(float(np.nanmean(cn_clip)), 2),
        "SWC_Priority"          : ("High"     if df_rusle.loc[bid, "A_mean_t_ha_yr"] > 15 else
                                   "Moderate" if df_rusle.loc[bid, "A_mean_t_ha_yr"] > 5  else
                                   "Low") if bid in df_rusle.index else "Unknown"
    })
    print(f"  {bid}: WHP={WHP_m3/1e6:.4f} Mm³ | CT_suit%={round(float(np.nanmean(ct_clip > 0.5))*100,1)}% "
          f"| Est. check dams={n_suitable}")

df_whp = pd.DataFrame(WHP_ROWS).set_index("basin_id")
df_whp.to_csv(os.path.join(SWC_DIR, "conservation_potential.csv"))

# ─────────────────────────────────────────────────────────────────────────────
#  E. SWC MAPS
# ─────────────────────────────────────────────────────────────────────────────

print("\n[16-E] Generating conservation maps...")

# Check dam suitability map
cdsi_colors = {"Very Suitable": "#1a9641", "Suitable": "#a6d96a",
               "Moderately Suitable": "#fdae61", "Poorly Suitable": "#d73027"}
fig, ax, utm_ext = base_axes("Check Dam (Naala Bund) Suitability Map\n"
                              "CDSI = f(Order, Catchment Area, Slope, Erosion, Valley Width)")
for cls, color in cdsi_colors.items():
    segs = gdf_cd[gdf_cd["CDSI_class"] == cls]
    if len(segs) > 0:
        segs.plot(ax=ax, color=color, linewidth=1.5+gdf_cd[gdf_cd["CDSI_class"]==cls][ORDER_COL].mean()*0.3,
                  alpha=0.9, zorder=5, label=cls)
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.5, zorder=15)
# Mark pour points as potential check dam sites
if "gdf_pp" in dir() and gdf_pp is not None:
    gdf_pp.plot(ax=ax, color="red", markersize=80, marker="v",
                zorder=20, label="Pour points (outlets)", edgecolor="white", linewidth=0.8)
patches_cd = [mpatches.Patch(color=v, label=k) for k, v in cdsi_colors.items()]
ax.legend(handles=patches_cd, loc="lower left", fontsize=8,
          title="Check Dam Suitability", title_fontsize=9, framealpha=0.9)
finalize_and_save(fig, ax, utm_ext, "16a_checkdam_suitability.png")

# Composite SWC treatment map
fig, ax, utm_ext = base_axes("Soil & Water Conservation Treatment Zone Map\n"
                              "(Contour Trenches + Percolation Potential)")
# Percolation zones (background)
im1 = ax.imshow(PERC_ARR, extent=raster_extent(), origin="upper",
                cmap="Blues", alpha=0.55, zorder=1, vmin=0, vmax=1)
# Contour trench suitability (overlay)
im2 = ax.imshow(np.ma.masked_where(CT_ARR < 0.5, CT_ARR),
                extent=raster_extent(), origin="upper",
                cmap="Oranges", alpha=0.60, zorder=2, vmin=0.5, vmax=1)
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.2, zorder=10)
# Suitable check dam stream reaches
gdf_cd[gdf_cd["CDSI"] >= 5.5].plot(ax=ax, color="darkgreen", linewidth=1.5, zorder=8, alpha=0.85)
gdf_cd[gdf_cd["CDSI"] < 5.5].plot(ax=ax, color="lightgrey",  linewidth=0.5, zorder=6, alpha=0.4)

legend_items = [
    mpatches.Patch(color="#3182bd", alpha=0.55, label="Percolation / Recharge Zone"),
    mpatches.Patch(color="#e6550d", alpha=0.60, label="Contour Trench Zone (slope 3–30°)"),
    mpatches.Patch(color="darkgreen",            label="Check Dam Sites (CDSI ≥ 5.5)"),
]
ax.legend(handles=legend_items, loc="lower left", fontsize=8,
          title="Treatment Zones", title_fontsize=9, framealpha=0.9)
finalize_and_save(fig, ax, utm_ext, "16b_SWC_treatment_zones.png")

# Plotly: WHP bar chart + SWC priority
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Water Harvesting Potential (Mm³/25-yr event)",
                                    "SWC Priority & Estimated Check Dam Count"])
swc_pmap = {"High": "#d73027", "Moderate": "#fdae61", "Low": "#4575b4"}
for i, (bid, row_) in enumerate(df_whp.iterrows()):
    c = swc_pmap.get(row_["SWC_Priority"], "grey")
    fig.add_trace(go.Bar(
        x=[bid], y=[row_["WHP_25yr_Mm3"]], marker_color=c, name=bid,
        text=f"{row_['WHP_25yr_Mm3']:.4f}", textposition="outside",
        hovertemplate=f"{bid}<br>WHP={row_['WHP_25yr_Mm3']:.4f} Mm³<br>Priority={row_['SWC_Priority']}",
    ), row=1, col=1)
    fig.add_trace(go.Bar(
        x=[bid], y=[row_["Potential_CheckDams_N"]], marker_color=c, name=bid,
        showlegend=False, text=str(row_["Potential_CheckDams_N"]), textposition="outside",
        hovertemplate=f"{bid}<br>Est. check dams={row_['Potential_CheckDams_N']}",
    ), row=1, col=2)

fig.update_yaxes(title_text="Water Harvesting Potential (Mm³)", row=1, col=1)
fig.update_yaxes(title_text="Estimated Check Dam Count", row=1, col=2)
fig.update_layout(title="Soil & Water Conservation Potential — Pravara Subbasins",
                  template="plotly_white", height=480, showlegend=False)
save_fig(fig, "16c_SWC_potential_bars")
print("\n✅ SECTION 16 complete.")

# ─────────────────────────────────────────────────────────────────────────────
# ██████████████████████████████████████████████████████████████████████████
# SECTION 17 — SYNTHETIC UNIT HYDROGRAPH
# ██████████████████████████████████████████████████████████████████████████
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SECTION 17 — SYNTHETIC UNIT HYDROGRAPH (Snyder's & SCS Methods)")
print("=" * 70)

# ─────────────────────────────────────────────────────────────────────────────
#  A. SNYDER'S SYNTHETIC UNIT HYDROGRAPH
# ─────────────────────────────────────────────────────────────────────────────

print("\n[17-A] Snyder's Synthetic Unit Hydrograph parameters...")

# Snyder (1938) — calibrated for Indian semi-arid basins:
# Ct = 1.8 (lag coefficient, typical for Deccan Trap with moderate relief)
# Cp = 0.6 (peaking coefficient)
# tL = Ct × (L × Lca)^0.3      [L = basin length km, Lca = L to centroid km]
# Qp = 2.75 × Cp × A / tL      [Qp in m³/s for 1mm/hr rainfall, A in km²]
# tp = tL + tr/2                [tp = time to peak; tr = storm duration = tL/5.5]
# W50 = 2.14 / (Qp/A)^1.08     [width at 50% Qp, hrs]
# W75 = 1.22 / (Qp/A)^1.08     [width at 75% Qp, hrs]
# tb  = 5 × (tp + tr/2) / 24   [base time, hrs]  — approximate

Ct = 1.8    # lag coefficient (Indian semi-arid, Deccan Trap)
Cp = 0.6    # peak coefficient

SUH_ROWS = []

for _, row in gdf_sub.iterrows():
    bid   = row["basin_id"]
    geom  = row.geometry
    A_km2 = df_areal.loc[bid, "Area_km2"]
    L_km  = df_areal.loc[bid, "Basin_Length_km"]

    # Lca: distance from outlet to centroid along main channel
    # Approximate as 0.6 × L for natural basins (standard assumption)
    Lca_km = 0.6 * L_km

    # Snyder lag time
    tL_hr  = Ct * (L_km * Lca_km) ** 0.3      # hours

    # Standard storm duration
    tr_hr  = tL_hr / 5.5

    # Time to peak
    tp_hr  = tL_hr + tr_hr / 2.0

    # Peak discharge (m³/s per mm of rainfall over basin)
    Qp     = 2.75 * Cp * A_km2 / tL_hr

    # Unit area peak
    qp     = Qp / A_km2   # m³/s/km² per mm

    # Hydrograph widths
    W50    = 2.14 / (qp ** 1.08)   # hrs
    W75    = 1.22 / (qp ** 1.08)   # hrs

    # Base time
    tb_hr  = 5.0 * tp_hr / 1.0     # approximate (Linsley et al. rule)
    tb_hr  = max(tb_hr, 2.0 * tp_hr)  # at least 2×tp

    # Time of rise and recession
    tr_rise = tp_hr
    tr_recs = tb_hr - tp_hr

    # Return-period peak discharge (m³/s)
    QP_RT = {}
    for T in RETURN_PERIODS:
        P24  = RAINFALL_RT[T]
        Q_mm = float(scscn_runoff(P24, df_runoff.loc[bid,"CN_mean"] if bid in df_runoff.index else 78))
        QP_RT[T] = round(Qp * Q_mm, 2)   # Qp [m³/s] = unit Qp × Q [mm]

    r_suh = {
        "basin_id"    : bid,
        "L_km"        : round(L_km, 3),
        "Lca_km"      : round(Lca_km, 3),
        "A_km2"       : round(A_km2, 3),
        "tL_hr"       : round(tL_hr, 3),
        "tr_hr"       : round(tr_hr, 3),
        "tp_hr"       : round(tp_hr, 3),
        "Qp_1mm_m3s"  : round(Qp, 4),
        "qp_m3s_km2"  : round(qp, 5),
        "W50_hr"      : round(W50, 3),
        "W75_hr"      : round(W75, 3),
        "tb_hr"       : round(tb_hr, 3),
    }
    for T in RETURN_PERIODS:
        r_suh[f"Qp_{T}yr_m3s"] = QP_RT[T]

    SUH_ROWS.append(r_suh)
    print(f"  {bid}: tL={tL_hr:.2f}hr | tp={tp_hr:.2f}hr | "
          f"Qp(1mm)={Qp:.3f} m³/s | W50={W50:.2f}hr | W75={W75:.2f}hr")

df_suh = pd.DataFrame(SUH_ROWS).set_index("basin_id")
df_suh.to_csv(os.path.join(UHG_DIR, "snyder_unit_hydrograph_params.csv"))

# ─────────────────────────────────────────────────────────────────────────────
#  B. SCS DIMENSIONLESS UNIT HYDROGRAPH
# ─────────────────────────────────────────────────────────────────────────────

print("\n[17-B] SCS Dimensionless Unit Hydrograph...")

# SCS dimensionless ratios (t/tp vs Q/Qp)
SCS_DIM = np.array([
    [0.0, 0.000], [0.1, 0.030], [0.2, 0.100], [0.3, 0.190], [0.4, 0.310],
    [0.5, 0.470], [0.6, 0.660], [0.7, 0.820], [0.8, 0.930], [0.9, 0.990],
    [1.0, 1.000], [1.1, 0.990], [1.2, 0.930], [1.3, 0.860], [1.4, 0.780],
    [1.5, 0.680], [1.6, 0.560], [1.7, 0.460], [1.8, 0.390], [1.9, 0.330],
    [2.0, 0.280], [2.2, 0.207], [2.4, 0.147], [2.6, 0.107], [2.8, 0.077],
    [3.0, 0.055], [3.5, 0.025], [4.0, 0.011], [4.5, 0.005], [5.0, 0.000],
])
t_ratio = SCS_DIM[:, 0]
q_ratio = SCS_DIM[:, 1]

# ─────────────────────────────────────────────────────────────────────────────
#  C. HYDROGRAPH PLOTS
# ─────────────────────────────────────────────────────────────────────────────

print("\n[17-C] Generating unit hydrograph plots...")

# Matplotlib: all basins on one figure
fig, axes = plt.subplots(len(df_suh), 1,
                         figsize=(12, 4 * len(df_suh)),
                         sharex=False)
if len(df_suh) == 1:
    axes = [axes]

colors_suh = plt.cm.Set1(np.linspace(0, 1, max(len(df_suh), 2)))

for ax_i, (bid, suh) in enumerate(df_suh.iterrows()):
    ax = axes[ax_i]
    tp = suh["tp_hr"]
    tb = suh["tb_hr"]

    # SCS-based hydrograph for 25-yr storm
    Q25_mm = (float(df_runoff.loc[bid, "Q_25yr_mm"])
               if bid in df_runoff.index else 25.0)
    Qp_25  = suh["Qp_1mm_m3s"] * Q25_mm

    t_abs  = t_ratio * tp
    t_full = np.linspace(0, tb * 1.05, 500)
    from scipy.interpolate import interp1d
    q_interp = interp1d(t_ratio * tp, q_ratio * Qp_25,
                         kind="linear", fill_value=0.0, bounds_error=False)
    q_full   = q_interp(t_full)

    ax.fill_between(t_full, 0, q_full, alpha=0.25, color=colors_suh[ax_i])
    ax.plot(t_full, q_full, color=colors_suh[ax_i], linewidth=2.2,
            label=f"{bid} — 25-yr (Q={Q25_mm:.0f}mm)")

    # Also plot 10-yr and 50-yr for comparison
    for T_comp, ls, alpha_c in [(10, "--", 0.6), (50, "-.", 0.6)]:
        Qmm_c = float(df_runoff.loc[bid, f"Q_{T_comp}yr_mm"]
                       if bid in df_runoff.index else 20.0)
        Qp_c  = suh["Qp_1mm_m3s"] * Qmm_c
        ax.plot(t_full, q_interp(t_full) * (Qp_c / (Qp_25 + 1e-9)),
                color=colors_suh[ax_i], linestyle=ls, linewidth=1.5, alpha=alpha_c,
                label=f"{T_comp}-yr")

    # Annotate Qp and tp
    ax.axvline(tp, color="grey", linestyle=":", linewidth=1.2)
    ax.axhline(Qp_25, color="grey", linestyle=":", linewidth=0.8)
    ax.annotate(f"Qp={Qp_25:.1f} m³/s\ntp={tp:.2f} hr",
                xy=(tp, Qp_25), xytext=(tp + 0.5, Qp_25 * 0.75),
                fontsize=9, arrowprops=dict(arrowstyle="->", color="black"))

    # W50 and W75 hatching
    w50_half = suh["W50_hr"] / 2.0
    w75_half = suh["W75_hr"] / 2.0
    ax.axvspan(tp - w50_half, tp + w50_half, alpha=0.08, color="blue", label="W50")
    ax.axvspan(tp - w75_half, tp + w75_half, alpha=0.08, color="red",  label="W75")

    ax.set_title(f"Synthetic Unit Hydrograph — {bid}  "
                 f"(A={suh['A_km2']:.1f} km², L={suh['L_km']:.2f} km)",
                 fontweight="bold", fontsize=11)
    ax.set_xlabel("Time (hours)", fontsize=9)
    ax.set_ylabel("Discharge (m³/s)", fontsize=9)
    ax.legend(fontsize=8, loc="upper right", framealpha=0.85)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_xlim(0, tb * 1.05)
    ax.set_ylim(bottom=0)

plt.suptitle("Synthetic Unit Hydrographs — Pravara Subbasins\n"
             "Snyder's Method with SCS Dimensionless UH Shape | Ct=1.8, Cp=0.6",
             fontsize=13, fontweight="bold", y=1.01)
plt.tight_layout()
fig.savefig(os.path.join(UHG_DIR, "17_unit_hydrographs.png"), dpi=180, bbox_inches="tight")
plt.close(fig)
print(f"  ✅ Hydrograph plot saved")

# Plotly: interactive multi-basin hydrograph
fig_hy = go.Figure()
for i, (bid, suh) in enumerate(df_suh.iterrows()):
    tp = suh["tp_hr"]
    tb = suh["tb_hr"]
    Q25_mm = float(df_runoff.loc[bid, "Q_25yr_mm"] if bid in df_runoff.index else 25.0)
    Qp_25  = suh["Qp_1mm_m3s"] * Q25_mm
    t_full = np.linspace(0, tb * 1.05, 300)
    q_interp = interp1d(t_ratio * tp, q_ratio * Qp_25,
                         kind="linear", fill_value=0.0, bounds_error=False)
    q_full = q_interp(t_full)

    fig_hy.add_trace(go.Scatter(
        x=t_full.tolist(), y=q_full.tolist(),
        mode="lines", name=f"{bid} (25-yr)",
        fill="tozeroy",
        line=dict(color=px.colors.qualitative.Set1[i % 9], width=2.5),
        hovertemplate=f"{bid}<br>t=%{{x:.2f}} hr<br>Q=%{{y:.2f}} m³/s",
    ))
    # Mark Qp
    fig_hy.add_trace(go.Scatter(
        x=[tp], y=[Qp_25], mode="markers+text",
        text=[f"Qp={Qp_25:.1f}"], textposition="top center",
        marker=dict(size=10, color=px.colors.qualitative.Set1[i % 9], symbol="diamond"),
        name=f"{bid} peak", showlegend=False,
    ))

fig_hy.update_layout(
    title="Synthetic Unit Hydrographs — 25-year Return Period Event<br>"
          "<sup>Snyder's Method, Deccan Trap basalt calibration: Ct=1.8, Cp=0.6</sup>",
    xaxis_title="Time (hours)",
    yaxis_title="Discharge Q (m³/s)",
    template="plotly_white", height=550,
)
save_fig(fig_hy, "17b_synthetic_unit_hydrographs")

# Summary table plot
cols_suh = ["tp_hr", "Qp_1mm_m3s", "W50_hr", "W75_hr", "tb_hr",
             "Qp_25yr_m3s", "Qp_100yr_m3s"]
fig_tbl = go.Figure(go.Table(
    header=dict(
        values=["Basin", "tp (hr)", "Qp_unit (m³/s)", "W50 (hr)", "W75 (hr)",
                "tb (hr)", "Qp 25-yr", "Qp 100-yr"],
        fill_color="#2c5f8c", font_color="white",
        align="center", line_color="white",
    ),
    cells=dict(
        values=[
            df_suh.index.tolist(),
            df_suh["tp_hr"].round(2).tolist(),
            df_suh["Qp_1mm_m3s"].round(4).tolist(),
            df_suh["W50_hr"].round(2).tolist(),
            df_suh["W75_hr"].round(2).tolist(),
            df_suh["tb_hr"].round(2).tolist(),
            df_suh["Qp_25yr_m3s"].tolist(),
            df_suh["Qp_100yr_m3s"].tolist(),
        ],
        fill_color=[["#f0f4ff", "#dce8ff"] * len(df_suh)],
        align="center",
    )
))
fig_tbl.update_layout(title="Snyder's UH Parameter Summary Table",
                       template="plotly_white", height=300)
save_fig(fig_tbl, "17c_UH_parameter_table")
print("\n✅ SECTION 17 complete.")

# ─────────────────────────────────────────────────────────────────────────────
# ██████████████████████████████████████████████████████████████████████████
# SECTION 18 — STREAM CHANNEL HYDRAULICS & STABILITY ANALYSIS
# ██████████████████████████████████████████████████████████████████████████
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("SECTION 18 — STREAM CHANNEL HYDRAULICS & STABILITY")
print("(Bankfull Discharge, Shear Stress, Stream Power, Stability Index)")
print("=" * 70)

# ─────────────────────────────────────────────────────────────────────────────
#  A. HYDRAULIC GEOMETRY — Leopold & Maddock (1953) Regional Curves
# ─────────────────────────────────────────────────────────────────────────────
# For Indian semi-arid Deccan rivers, regional hydraulic geometry:
#   w = a × Q^b     (bankfull width, b ≈ 0.50)
#   d = c × Q^f     (bankfull depth, f ≈ 0.40)
#   v = k × Q^m     (mean velocity, m ≈ 0.10)
# Calibrated coefficients for Deccan Trap basalt basins:
#   a=3.2, b=0.50; c=0.28, f=0.40; k=1.12, m=0.10
# Q_bankfull estimated as Q(1.5-yr) — typical recurrence for bankfull stage

print("\n[18-A] Bankfull Discharge & Hydraulic Geometry...")

# Bankfull discharge: Q(1.5-yr) via Gumbel interpolation
T_bf = 1.5
y_bf = -np.log(-np.log(1 - 1/T_bf))
P_bf_annual = u_g + alpha_g * y_bf          # annual rainfall
P_bf_24hr   = P_bf_annual * DAILY_FRACTION

HG_ROWS = []

for _, row in gdf_sub.iterrows():
    bid   = row["basin_id"]
    A_km2 = df_areal.loc[bid, "Area_km2"]
    L_km  = df_areal.loc[bid, "Basin_Length_km"]
    CN    = df_runoff.loc[bid, "CN_mean"] if bid in df_runoff.index else 78.0
    Tc_hr = df_tc.loc[bid, "Tc_hr"] if bid in df_tc.index else 2.0

    # Bankfull Q (1.5-yr)
    Q_bf_mm = float(scscn_runoff(P_bf_24hr, CN))
    C_bf    = float(runoff_coeff(P_bf_24hr, CN))
    i_bf    = (P_bf_24hr / 24.0) * (24.0 / Tc_hr) ** (2.0/3.0)
    Q_bf    = C_bf * i_bf * A_km2 / 3.6   # m³/s

    # Hydraulic geometry (Leopold-Maddock regional coefficients — Deccan)
    a_w, b_w = 3.20, 0.50   # width
    a_d, b_d = 0.28, 0.40   # depth
    a_v, b_v = 1.12, 0.10   # velocity

    W_bf = a_w * (Q_bf ** b_w)   # bankfull width [m]
    D_bf = a_d * (Q_bf ** b_d)   # bankfull depth [m]
    V_bf = a_v * (Q_bf ** b_v)   # bankfull velocity [m/s]

    # Cross-sectional area and hydraulic radius
    A_cs = W_bf * D_bf * 0.80   # assuming trapezoidal × efficiency factor
    R_hyd = A_cs / (W_bf + 2*D_bf)  # hydraulic radius [m]

    # Channel bed slope from DEM relief and basin length
    H_m    = df_relief.loc[bid, "Basin_Relief_H_m"] if bid in df_relief.index else 100.0
    S_ch   = H_m / (L_km * 1000.0)   # dimensionless

    # Manning's n (estimated for Deccan basalt-lined channels)
    # Rocky channels: n ≈ 0.035–0.050; alluvial gravel: n ≈ 0.025–0.035
    n_mann = 0.038 + 0.002 * (1 - min(S_ch / 0.01, 1))  # slightly rougher on steeper slopes

    # Manning's Q (check)
    Q_mann = (1.0 / n_mann) * A_cs * (R_hyd ** (2/3)) * (S_ch ** 0.5)

    # ── Shear stress ──────────────────────────────────────────────────────────
    # τ₀ = ρ × g × R × S  [N/m² = Pa]
    rho_water = 1000.0   # kg/m³
    g         = 9.81     # m/s²
    tau0      = rho_water * g * R_hyd * S_ch   # bed shear stress [Pa]

    # Critical shear stress — Shields (D50 ≈ 15mm for basalt gravel)
    # τ_c = θ_c × (ρ_s - ρ) × g × D50
    D50_m    = 0.015    # median grain size [m] — basaltic gravel
    rho_s    = 2650.0   # sediment density [kg/m³]
    theta_c  = 0.047    # Shields parameter for D50 >10mm
    tau_c    = theta_c * (rho_s - rho_water) * g * D50_m   # critical shear [Pa]

    excess_shear = tau0 - tau_c   # positive = bed mobility

    # ── Stream power ──────────────────────────────────────────────────────────
    # Ω = ρ × g × Q × S   [W/m]   total stream power
    # ω = Ω / w            [W/m²]  specific (unit width) stream power
    Omega_total   = rho_water * g * Q_bf * S_ch
    omega_spec    = Omega_total / W_bf   # W/m²

    # Critical specific stream power (Bagnold 1966):
    # ω_c ≈ 35.0 W/m² for coarse sand–gravel in semi-arid rivers
    omega_c = 35.0
    omega_excess = omega_spec - omega_c

    # ── Channel stability index ────────────────────────────────────────────
    # Regime theory: stable channel has W/D (aspect ratio) within bounds
    # For Deccan semi-arid channels: W/D < 15 = stable; 15–30 = marginally stable
    WD_ratio = W_bf / max(D_bf, 0.01)

    def channel_stability(WD, excess_shear_val, omega_exc):
        """Combined channel stability assessment."""
        score = 0
        if WD < 12:          score += 3   # narrow deep = stable
        elif WD < 20:        score += 2
        elif WD < 30:        score += 1
        if excess_shear_val < 0:  score += 3  # sub-critical shear = stable
        elif excess_shear_val < 5: score += 2
        elif excess_shear_val < 15: score += 1
        if omega_exc < 0:    score += 3   # sub-critical stream power
        elif omega_exc < 20: score += 2
        elif omega_exc < 50: score += 1
        if score >= 7:  return "Stable"
        if score >= 5:  return "Marginally Stable"
        if score >= 3:  return "Unstable"
        return "Highly Unstable"

    stab_class = channel_stability(WD_ratio, excess_shear, omega_excess)

    # ── Sediment transport capacity (Einstein-Brown simplified) ───────────────
    # Using unit stream power approach: Qs ∝ ω_excess² for ω > ω_c
    if omega_excess > 0:
        Qs_relative = (omega_excess / omega_c) ** 2.0  # relative transport capacity
    else:
        Qs_relative = 0.0

    HG_ROWS.append({
        "basin_id"              : bid,
        "Q_bankfull_m3s"        : round(Q_bf, 3),
        "W_bankfull_m"          : round(W_bf, 2),
        "D_bankfull_m"          : round(D_bf, 2),
        "V_bankfull_ms"         : round(V_bf, 3),
        "WD_ratio"              : round(WD_ratio, 2),
        "R_hydraulic_m"         : round(R_hyd, 3),
        "Channel_Slope_S"       : round(S_ch, 6),
        "Manning_n"             : round(n_mann, 4),
        "Q_Manning_m3s"         : round(Q_mann, 3),
        "Shear_Stress_Pa"       : round(tau0, 3),
        "Critical_Shear_Pa"     : round(tau_c, 3),
        "Excess_Shear_Pa"       : round(excess_shear, 3),
        "Stream_Power_total_Wm" : round(Omega_total, 2),
        "Stream_Power_spec_Wm2" : round(omega_spec, 3),
        "Excess_Sp_Power_Wm2"   : round(omega_excess, 3),
        "Transport_Capacity_rel": round(Qs_relative, 3),
        "Channel_Stability"     : stab_class,
    })
    print(f"  {bid}: Q_bf={Q_bf:.2f} m³/s | W={W_bf:.1f}m | D={D_bf:.2f}m | "
          f"τ={tau0:.1f}Pa | ω={omega_spec:.1f} W/m² | {stab_class}")

df_hg = pd.DataFrame(HG_ROWS).set_index("basin_id")
df_hg.to_csv(os.path.join(HYD_DIR, "channel_hydraulics.csv"))

# ─────────────────────────────────────────────────────────────────────────────
#  B. STREAM POWER INDEX PER ORDER — GEOMORPHIC WORK BY ORDER
# ─────────────────────────────────────────────────────────────────────────────

print("\n[18-B] Stream power analysis per Strahler order...")

# For each order, compute mean gradient, estimated Q, and stream power
ORDER_POWER_ROWS = []
orders_all = sorted(gdf_so[ORDER_COL].unique())

for o in orders_all:
    segs = gdf_so[gdf_so[ORDER_COL] == o]
    n_segs  = len(segs)
    L_total_m = segs.geometry.length.sum()
    L_mean_m  = segs.geometry.length.mean()

    # Sample slope at each segment
    seg_slopes = []
    for _, seg in segs.iterrows():
        s = sample_slope_at_segment(seg.geometry, SLOPE_ARR, DEM_TRANSFORM)
        if s is not None and not np.isnan(s):
            seg_slopes.append(s)
    mean_slope_deg = float(np.nanmean(seg_slopes)) if seg_slopes else 5.0
    S_order = np.tan(np.radians(max(mean_slope_deg, 0.1)))

    # Estimate Q for this order using Hack's (1957) scaling:
    # Q_order ≈ Q_max_basin × (Dd_order / Dd_total)
    # Simpler: Q scales with segment length proxy
    Q_order_proxy = 0.02 * (o ** 2.5) * np.mean(
        [df_runoff.loc[bid, "Q_25yr_mm"] if bid in df_runoff.index else 25
         for bid in gdf_sub["basin_id"]]) * 1e-3  # rough proxy

    omega_order = rho_water * g * Q_order_proxy * S_order / max(
        3.2 * (Q_order_proxy ** 0.5), 0.5)  # W/m²

    ORDER_POWER_ROWS.append({
        "Strahler_Order"     : o,
        "N_segments"         : n_segs,
        "Total_Length_km"    : round(L_total_m / 1000, 2),
        "Mean_Seg_Length_m"  : round(L_mean_m, 1),
        "Mean_Slope_deg"     : round(mean_slope_deg, 2),
        "Mean_Slope_frac"    : round(S_order, 5),
        "Qproxy_m3s"         : round(Q_order_proxy, 4),
        "StreamPower_Wm2"    : round(omega_order, 2),
    })
    print(f"  Order {o}: N={n_segs:4d} | L_tot={L_total_m/1000:.1f} km | "
          f"S_mean={mean_slope_deg:.2f}° | ω≈{omega_order:.2f} W/m²")

df_order_power = pd.DataFrame(ORDER_POWER_ROWS)
df_order_power.to_csv(os.path.join(HYD_DIR, "stream_order_power.csv"), index=False)

# ─────────────────────────────────────────────────────────────────────────────
#  C. COMPREHENSIVE MAPS & PLOTLY CHARTS
# ─────────────────────────────────────────────────────────────────────────────

print("\n[18-C] Generating hydraulics maps and charts...")

# Bankfull width map (choropleth per basin)
fig, ax, utm_ext = base_axes("Bankfull Channel Width & Hydraulic Geometry\n"
                              "Leopold-Maddock Regional Curves (Deccan Trap)")
gdf_hg = gdf_sub.merge(df_hg.reset_index(), on="basin_id", how="left")
gdf_hg.plot(column="W_bankfull_m", ax=ax, cmap="YlOrRd", legend=True,
            alpha=0.75, zorder=2, edgecolor="black", linewidth=1.2,
            legend_kwds={"label":"Bankfull Width (m)","shrink":0.75})
for _, r in gdf_hg.iterrows():
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    ax.text(cx, cy,
            f"{r['basin_id']}\nW={r['W_bankfull_m']:.1f}m\nD={r['D_bankfull_m']:.2f}m",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
# Stream network coloured by order
for o in orders_all:
    segs = gdf_so[gdf_so[ORDER_COL] == o]
    lw   = 0.4 + o * 0.6
    segs.plot(ax=ax, linewidth=lw, color=plt.cm.Blues(0.3 + o * 0.15), zorder=5, alpha=0.9)
finalize_and_save(fig, ax, utm_ext, "18a_bankfull_hydraulics.png")

# Channel stability map
stab_colors = {"Stable": "#1a9641", "Marginally Stable": "#fdae61",
               "Unstable": "#d73027", "Highly Unstable": "#7f0000"}
fig, ax, utm_ext = base_axes("Channel Stability Classification Map\n"
                              "(Shear Stress, Stream Power, W/D Ratio)")
for _, r in gdf_hg.iterrows():
    col = stab_colors.get(r["Channel_Stability"], "grey")
    gpd.GeoDataFrame([r], geometry="geometry", crs=gdf_sub.crs).plot(
        ax=ax, color=col, edgecolor="black", linewidth=1.2, alpha=0.80, zorder=3)
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    ax.text(cx, cy, f"{r['basin_id']}\n{r['Channel_Stability']}\nτ={r['Shear_Stress_Pa']:.1f}Pa",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.7, alpha=0.5, zorder=8)
patches_st = [mpatches.Patch(color=v, label=k) for k, v in stab_colors.items()]
ax.legend(handles=patches_st, loc="lower left", fontsize=8,
          title="Channel Stability", title_fontsize=9, framealpha=0.9)
finalize_and_save(fig, ax, utm_ext, "18b_channel_stability.png")

# Plotly: stream power vs shear stress bubble
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Stream Power vs Shear Stress per Basin",
                                    "Stream Power by Strahler Order"])
stab_c_map = {"Stable":"#1a9641","Marginally Stable":"#fdae61",
              "Unstable":"#d73027","Highly Unstable":"#7f0000"}
for i, (bid, r) in enumerate(df_hg.iterrows()):
    c = stab_c_map.get(r["Channel_Stability"], "grey")
    fig.add_trace(go.Scatter(
        x=[r["Shear_Stress_Pa"]], y=[r["Stream_Power_spec_Wm2"]],
        mode="markers+text", text=[bid], textposition="top center",
        marker=dict(size=r["W_bankfull_m"] * 2.5, color=c, opacity=0.85,
                    line=dict(width=1, color="black")),
        name=bid,
        hovertemplate=(f"<b>{bid}</b><br>"
                       f"τ = {r['Shear_Stress_Pa']:.2f} Pa<br>"
                       f"ω = {r['Stream_Power_spec_Wm2']:.2f} W/m²<br>"
                       f"Q_bf = {r['Q_bankfull_m3s']:.2f} m³/s<br>"
                       f"Stability: {r['Channel_Stability']}"),
    ), row=1, col=1)

# Order power bar
fig.add_trace(go.Bar(
    x=df_order_power["Strahler_Order"].tolist(),
    y=df_order_power["StreamPower_Wm2"].tolist(),
    marker_color=px.colors.sequential.Blues[2:],
    text=[f"{v:.2f}" for v in df_order_power["StreamPower_Wm2"]],
    textposition="outside",
    hovertemplate="Order %{x}<br>ω=%{y:.2f} W/m²",
    name="Stream Power",
), row=1, col=2)

# Critical stream power line
fig.add_hline(y=35, line_dash="dash", line_color="red",
              annotation_text="ω_c = 35 W/m² (critical)", row=1, col=1)
fig.add_hline(y=35, line_dash="dash", line_color="red", row=1, col=2)

fig.update_xaxes(title_text="Bed Shear Stress τ₀ (Pa)", row=1, col=1)
fig.update_yaxes(title_text="Specific Stream Power ω (W/m²)", row=1, col=1)
fig.update_xaxes(title_text="Strahler Order", row=1, col=2)
fig.update_yaxes(title_text="ω (W/m²)", row=1, col=2)
fig.update_layout(title="Stream Channel Hydraulics — Pravara River Basin",
                  template="plotly_white", height=520)
save_fig(fig, "18c_stream_power_hydraulics")

# Plotly: Hydraulic geometry log-log plots
fig = make_subplots(rows=1, cols=3,
                    subplot_titles=["Bankfull Width (W-Q)", "Bankfull Depth (D-Q)",
                                    "Bankfull Velocity (V-Q)"])
for i, (bid, r) in enumerate(df_hg.iterrows()):
    c = px.colors.qualitative.Set1[i % 9]
    fig.add_trace(go.Scatter(
        x=[r["Q_bankfull_m3s"]], y=[r["W_bankfull_m"]],
        mode="markers+text", text=[bid], textposition="top center",
        marker=dict(size=12, color=c), name=bid, legendgroup=bid,
        hovertemplate=f"{bid}<br>Q={r['Q_bankfull_m3s']:.2f} m³/s<br>W={r['W_bankfull_m']:.2f} m",
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=[r["Q_bankfull_m3s"]], y=[r["D_bankfull_m"]],
        mode="markers", marker=dict(size=12, color=c), name=bid,
        legendgroup=bid, showlegend=False,
        hovertemplate=f"{bid}<br>Q={r['Q_bankfull_m3s']:.2f} m³/s<br>D={r['D_bankfull_m']:.2f} m",
    ), row=1, col=2)
    fig.add_trace(go.Scatter(
        x=[r["Q_bankfull_m3s"]], y=[r["V_bankfull_ms"]],
        mode="markers", marker=dict(size=12, color=c), name=bid,
        legendgroup=bid, showlegend=False,
        hovertemplate=f"{bid}<br>Q={r['Q_bankfull_m3s']:.2f} m³/s<br>V={r['V_bankfull_ms']:.3f} m/s",
    ), row=1, col=3)

# Leopold-Maddock regional curves (dashed lines)
Q_range = np.logspace(-1, 2, 50)
fig.add_trace(go.Scatter(x=Q_range.tolist(), y=(3.20*Q_range**0.50).tolist(),
    mode="lines", line=dict(dash="dash",color="grey",width=1.5), name="W=3.2Q^0.5",
    hoverinfo="skip"), row=1, col=1)
fig.add_trace(go.Scatter(x=Q_range.tolist(), y=(0.28*Q_range**0.40).tolist(),
    mode="lines", line=dict(dash="dash",color="grey",width=1.5), name="D=0.28Q^0.4",
    showlegend=False, hoverinfo="skip"), row=1, col=2)
fig.add_trace(go.Scatter(x=Q_range.tolist(), y=(1.12*Q_range**0.10).tolist(),
    mode="lines", line=dict(dash="dash",color="grey",width=1.5), name="V=1.12Q^0.1",
    showlegend=False, hoverinfo="skip"), row=1, col=3)

for col_i, ylabel in [(1,"Width W (m)"), (2,"Depth D (m)"), (3,"Velocity V (m/s)")]:
    fig.update_xaxes(type="log", title_text="Bankfull Q (m³/s)", row=1, col=col_i)
    fig.update_yaxes(type="log", title_text=ylabel, row=1, col=col_i)

fig.update_layout(title="Hydraulic Geometry — At-a-Station Relationships (log-log)<br>"
                        "<sup>Leopold-Maddock (1953) regional curves for Deccan Trap basalt</sup>",
                  template="plotly_white", height=500)
save_fig(fig, "18d_hydraulic_geometry_loglog")

print("\n✅ SECTION 18 complete.")

# ─────────────────────────────────────────────────────────────────────────────
#  FINAL CONSOLIDATED OUTPUT TABLE (Sections 14–18)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("CONSOLIDATED HYDROLOGY & SWC RESULTS TABLE")
print("=" * 70)

df_consolidated = pd.concat([
    df_runoff[["CN_mean","Q_10yr_mm","Q_25yr_mm","Q_100yr_mm",
               "Vol_25yr_Mm3"]],
    df_tc[["Tc_Avg_min","Tc_hr","Qp_10yr_m3s","Qp_25yr_m3s","Qp_100yr_m3s"]],
    df_rusle[["A_mean_t_ha_yr","SDR","Sed_Yield_t_yr","Loss_Class_Mode"]],
    df_whp[["WHP_25yr_Mm3","Potential_CheckDams_N","SWC_Priority"]],
    df_suh[["tp_hr","Qp_1mm_m3s","W50_hr","W75_hr","tb_hr"]],
    df_hg[["Q_bankfull_m3s","W_bankfull_m","D_bankfull_m",
           "Shear_Stress_Pa","Stream_Power_spec_Wm2","Channel_Stability"]],
], axis=1)

df_consolidated.to_csv(os.path.join(TABLES_DIR, "hydrology_SWC_consolidated.csv"))

print("\nCONSOLIDATED RESULTS:")
print(df_consolidated.to_string())

# Print to output summary
print("\n" + "─"*70)
print("SUMMARY OF KEY SOIL & WATER CONSERVATION METRICS")
print("─"*70)
for bid in df_consolidated.index:
    r = df_consolidated.loc[bid]
    print(f"\n  ┌─ {bid} {'─'*40}")
    print(f"  │  CN={r['CN_mean']:.1f} | Tc={r['Tc_Avg_min']:.1f} min | "
          f"Q25yr={r['Q_25yr_mm']:.1f}mm | Qp25={r['Qp_25yr_m3s']:.2f}m³/s")
    print(f"  │  Soil loss={r['A_mean_t_ha_yr']:.1f} t/ha/yr ({r['Loss_Class_Mode']}) | "
          f"Sed.Yield={r['Sed_Yield_t_yr']:.0f} t/yr")
    print(f"  │  WHP={r['WHP_25yr_Mm3']:.4f}Mm³ | ~{r['Potential_CheckDams_N']} check dams | "
          f"SWC priority: {r['SWC_Priority']}")
    print(f"  │  Bankfull Q={r['Q_bankfull_m3s']:.2f}m³/s | "
          f"τ={r['Shear_Stress_Pa']:.1f}Pa | ω={r['Stream_Power_spec_Wm2']:.1f}W/m² | "
          f"Stability: {r['Channel_Stability']}")
    print(f"  └─ UH: tp={r['tp_hr']:.2f}hr | Qp(1mm)={r['Qp_1mm_m3s']:.4f}m³/s | "
          f"W50={r['W50_hr']:.2f}hr | tb={r['tb_hr']:.2f}hr")

print("\n" + "=" * 70)
print("ALL SECTIONS 14–18 COMPLETE")
print("=" * 70)
print(f"\n  Output files:")
all_new_files = (
    [(HYD_DIR,  f) for f in os.listdir(HYD_DIR)] +
    [(SWC_DIR,  f) for f in os.listdir(SWC_DIR)] +
    [(UHG_DIR,  f) for f in os.listdir(UHG_DIR)] +
    [(HYD_MAPS, f) for f in os.listdir(HYD_MAPS) if os.path.exists(HYD_MAPS)] +
    [(SWC_MAPS, f) for f in os.listdir(SWC_MAPS) if os.path.exists(SWC_MAPS)]
)
for d, f in sorted(all_new_files):
    fpath = os.path.join(d, f)
    size  = os.path.getsize(fpath) / 1024 if os.path.exists(fpath) else 0
    print(f"    {fpath.replace(OUT_DIR,''):<60s}  {size:>8.1f} KB")

print(f"\n  Total new maps   : 9 (14a, 14b, 15a, 15b, 16a, 16b, 18a, 18b)")
print(f"  Total new CSVs   : 9")
print(f"  Plotly HTML      : 12 interactive charts")
print(f"  Shapefile        : checkdam_suitability.shp")
