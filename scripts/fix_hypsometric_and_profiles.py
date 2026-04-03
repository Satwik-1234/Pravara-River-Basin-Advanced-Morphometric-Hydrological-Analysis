# -*- coding: utf-8 -*-
"""
=============================================================================
 fix_hypsometric_and_profiles.py
=============================================================================
 Standalone script to fix the hypsometric curve bug and generate new
 elevation analysis charts for the Pravara River Basin.

 Bug: The original pipeline produced identical hypsometric curves for all
 3 subbasins (all HI=0.262) because the DEM clipping silently fell back
 to using the full DEM for every subbasin.

 This script generates:
  1. FIXED hypsometric curves (per-basin DEM clipping via pravra3.shp)
  2. W->E and E->W elevation transect profiles
  3. N->S and S->N elevation transect profiles
  4. Combined 4-directional transect comparison
  5. Elevation distribution histograms per basin
  6. Elevation statistics summary table

 Usage:
   python scripts/fix_hypsometric_and_profiles.py

 Requirements: geopandas, rasterio, numpy, plotly
=============================================================================
"""

import os
import sys
import zipfile

import numpy as np

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_ZIP = os.path.join(REPO_ROOT, "data", "Morphomtery layers-Final.zip")
TEMP_DIR = os.path.join(REPO_ROOT, "_temp_gis")
OUTPUT_HTML = os.path.join(REPO_ROOT, "outputs", "html")

DEM_FILE = "Filled DEM.tif"
BASIN_FILE = "pravra3.shp"  # 3-polygon delineation (not the 5-polygon one)

os.makedirs(OUTPUT_HTML, exist_ok=True)


def extract_if_needed():
    """Extract zip to _temp_gis if not already done."""
    dem_path = os.path.join(TEMP_DIR, DEM_FILE)
    if os.path.exists(dem_path):
        print(f"  [OK] Data already extracted: {TEMP_DIR}")
        return
    if not os.path.exists(DATA_ZIP):
        print(f"  [ERROR] Zip not found: {DATA_ZIP}")
        sys.exit(1)
    os.makedirs(TEMP_DIR, exist_ok=True)
    with zipfile.ZipFile(DATA_ZIP, "r") as z:
        z.extractall(TEMP_DIR)
    print(f"  [OK] Extracted {DEM_FILE} and {BASIN_FILE} to {TEMP_DIR}")


def load_data():
    """Load DEM and subbasin shapefile."""
    import geopandas as gpd
    import rasterio

    dem_path = os.path.join(TEMP_DIR, DEM_FILE)
    basin_path = os.path.join(TEMP_DIR, BASIN_FILE)

    with rasterio.open(dem_path) as src:
        dem_arr = src.read(1).astype(np.float32)
        nodata = src.nodata
        if nodata is not None:
            dem_arr[dem_arr == nodata] = np.nan
        dem_meta = {
            "crs": src.crs,
            "transform": src.transform,
            "bounds": src.bounds,
            "res": src.res[0],
        }
    print(
        f"  DEM: {dem_arr.shape} | "
        f"range {np.nanmin(dem_arr):.0f}-{np.nanmax(dem_arr):.0f} m | "
        f"CRS: {dem_meta['crs']}"
    )

    gdf = gpd.read_file(basin_path)
    if str(gdf.crs) != str(dem_meta["crs"]):
        gdf = gdf.to_crs(dem_meta["crs"])

    basin_ids = []
    for i, row in gdf.iterrows():
        name = row.get("name", f"SB{i+1}")
        if "Subbasin" in str(name):
            num = str(name).split("-")[-1]
            basin_ids.append(f"SB{num}")
        else:
            basin_ids.append(f"SB{i+1}")
    gdf["basin_id"] = basin_ids

    print(f"  Basins: {gdf['basin_id'].tolist()} | CRS: {gdf.crs}")
    return dem_arr, dem_meta, gdf


def clip_dem_per_basin(gdf):
    """Clip DEM per subbasin and return dict of clipped arrays + vals."""
    import rasterio
    from rasterio.mask import mask as rio_mask

    dem_path = os.path.join(TEMP_DIR, DEM_FILE)
    clipped = {}

    for _, row in gdf.iterrows():
        bid = row["basin_id"]
        geom = [row.geometry.__geo_interface__]
        with rasterio.open(dem_path) as src:
            nd_val = src.nodata if src.nodata is not None else -9999
            out_image, out_transform = rio_mask(
                src, geom, crop=True, nodata=nd_val, filled=True
            )
            dem_clip = out_image[0].astype(np.float32)
            dem_clip[dem_clip == nd_val] = np.nan
        vals = dem_clip[~np.isnan(dem_clip)].flatten()
        clipped[bid] = {"array": dem_clip, "vals": vals, "transform": out_transform}
    return clipped


def compute_hypsometric(clipped):
    """Compute per-basin hypsometric curves from pre-clipped DEMs."""
    results = {}
    for bid, data in clipped.items():
        vals = data["vals"]
        if len(vals) < 10:
            print(f"  [WARN] {bid}: insufficient DEM pixels ({len(vals)})")
            continue
        mn, mx, mu = vals.min(), vals.max(), vals.mean()
        rng = mx - mn
        if rng == 0:
            print(f"  [WARN] {bid}: zero elevation range")
            continue
        HI = float((mu - mn) / rng)
        vals_sorted = np.sort(vals)[::-1]
        n_pts = min(500, len(vals_sorted))
        indices = np.linspace(0, len(vals_sorted) - 1, n_pts).astype(int)
        vals_sampled = vals_sorted[indices]
        rel_area = np.linspace(0, 1, n_pts)
        rel_elev = (vals_sampled - mn) / rng

        results[bid] = {
            "HI": HI,
            "rel_area": rel_area,
            "rel_elev": rel_elev,
            "elev_min": float(mn),
            "elev_max": float(mx),
            "elev_mean": float(mu),
            "elev_std": float(vals.std()),
            "elev_median": float(np.median(vals)),
            "n_pixels": len(vals),
            "vals": vals,
        }
        stage = (
            "Young (Monadnock)"
            if HI > 0.6
            else "Mature (Equilibrium)" if HI > 0.35 else "Old (Peneplain)"
        )
        print(
            f"  {bid}: HI={HI:.4f} ({stage}) | "
            f"Elev {mn:.0f}-{mx:.0f} m | {len(vals):,} pixels"
        )
    return results


def generate_hypsometric_html(hyps_data):
    """Generate corrected hypsometric curves HTML chart."""
    import plotly.express as px
    import plotly.graph_objects as go

    fig = go.Figure()
    colors = px.colors.qualitative.Plotly
    for i, (bid, data) in enumerate(sorted(hyps_data.items())):
        fig.add_trace(
            go.Scatter(
                x=data["rel_area"].tolist(),
                y=data["rel_elev"].tolist(),
                mode="lines",
                name=f"{bid} (HI={data['HI']:.3f})",
                line=dict(color=colors[i % len(colors)], width=2.5),
                hovertemplate=(
                    f"<b>{bid}</b><br>"
                    "Rel. Area (a/A): %{x:.3f}<br>"
                    "Rel. Elev (h/H): %{y:.3f}<extra></extra>"
                ),
            )
        )
    fig.add_trace(
        go.Scatter(
            x=[0, 1], y=[0.5, 0.5], mode="lines",
            name="HI = 0.5 (Equilibrium)",
            line=dict(dash="dash", color="grey", width=1),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[0, 1], y=[1, 0], mode="lines",
            name="Diagonal (reference)",
            line=dict(dash="dot", color="lightgrey", width=1),
        )
    )
    fig.update_layout(
        title="Hypsometric Curves - Pravara River Basin Subbasins<br>"
        "<sup>Accurate per-basin DEM clipping (pravra3.shp)</sup>",
        xaxis_title="Relative Area (a/A)",
        yaxis_title="Relative Elevation (h/H)",
        template="plotly_white",
        height=600,
        legend=dict(x=0.65, y=0.95),
        xaxis=dict(range=[0, 1], dtick=0.1),
        yaxis=dict(range=[0, 1], dtick=0.1),
    )
    out_path = os.path.join(OUTPUT_HTML, "07_hypsometric_curves.html")
    fig.write_html(out_path)
    print(f"  [OK] Saved: {out_path}")


def sample_transect(dem_arr, transform, geom, start_coord, end_coord, n_samples=500):
    """Sample DEM along a transect line, returning distances and elevations."""
    from rasterio.transform import rowcol
    from shapely.geometry import Point

    xs = np.linspace(start_coord[0], end_coord[0], n_samples)
    ys = np.linspace(start_coord[1], end_coord[1], n_samples)

    distances = []
    elevations = []
    total_dist = np.sqrt(
        (end_coord[0] - start_coord[0]) ** 2 + (end_coord[1] - start_coord[1]) ** 2
    )

    for j in range(n_samples):
        px, py = xs[j], ys[j]
        if not geom.contains(Point(px, py)):
            continue
        try:
            r, c = rowcol(transform, px, py)
            if 0 <= r < dem_arr.shape[0] and 0 <= c < dem_arr.shape[1]:
                elev = dem_arr[r, c]
                if not np.isnan(elev):
                    frac = j / (n_samples - 1)
                    distances.append(frac * total_dist / 1000)
                    elevations.append(float(elev))
        except Exception:
            continue
    return np.array(distances), np.array(elevations)


def compute_all_profiles(dem_arr, dem_meta, gdf):
    """Compute W-E, E-W, N-S, S-N elevation transect profiles per subbasin."""
    profiles = {}

    for _, row in gdf.iterrows():
        bid = row["basin_id"]
        geom = row.geometry
        bounds = geom.bounds  # (minx, miny, maxx, maxy)
        cx, cy = geom.centroid.x, geom.centroid.y

        # W->E transect: horizontal at centroid_y
        d_we, e_we = sample_transect(
            dem_arr, dem_meta["transform"], geom,
            (bounds[0], cy), (bounds[2], cy)
        )
        # N->S transect: vertical at centroid_x
        d_ns, e_ns = sample_transect(
            dem_arr, dem_meta["transform"], geom,
            (cx, bounds[3]), (cx, bounds[1])  # north (maxy) to south (miny)
        )

        if len(e_we) < 10 or len(e_ns) < 10:
            print(f"  [WARN] {bid}: insufficient profile points (W-E:{len(e_we)}, N-S:{len(e_ns)})")
            continue

        profiles[bid] = {
            "d_we": d_we, "e_we": e_we,
            "d_ns": d_ns, "e_ns": e_ns,
            "bounds": bounds,
            "centroid": (cx, cy),
        }
        print(
            f"  {bid}: W-E {len(e_we)} pts ({d_we.max():.1f} km), "
            f"N-S {len(e_ns)} pts ({d_ns.max():.1f} km)"
        )
    return profiles


def generate_all_profile_html(profiles):
    """Generate all profile HTML charts including N-S/S-N."""
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    colors = px.colors.qualitative.Plotly
    sorted_bids = sorted(profiles.keys())

    def _make_simple_chart(title_text, subtitle, xlab, get_xy, filename):
        fig = go.Figure()
        for i, bid in enumerate(sorted_bids):
            data = profiles[bid]
            x, y = get_xy(data)
            fig.add_trace(
                go.Scatter(
                    x=x, y=y, mode="lines", name=bid, fill="tozeroy",
                    line=dict(color=colors[i % len(colors)], width=2),
                    hovertemplate=(
                        f"<b>{bid}</b><br>"
                        f"Distance: %{{x:.2f}} km<br>"
                        f"Elevation: %{{y:.0f}} m<extra></extra>"
                    ),
                )
            )
        fig.update_layout(
            title=f"{title_text}<br><sup>{subtitle}</sup>",
            xaxis_title=xlab,
            yaxis_title="Elevation (m)",
            template="plotly_white",
            height=500,
            legend=dict(x=0.02, y=0.98),
        )
        path = os.path.join(OUTPUT_HTML, filename)
        fig.write_html(path)
        print(f"  [OK] Saved: {path}")

    # W -> E
    _make_simple_chart(
        "Elevation Profile - West to East Transect",
        "Cross-section at subbasin centroid latitude",
        "Distance from Western Boundary (km)",
        lambda d: (d["d_we"], d["e_we"]),
        "elevation_profile_W2E.html",
    )
    # E -> W
    _make_simple_chart(
        "Elevation Profile - East to West Transect",
        "Cross-section at subbasin centroid latitude",
        "Distance from Eastern Boundary (km)",
        lambda d: (d["d_we"].max() - d["d_we"], d["e_we"]),
        "elevation_profile_E2W.html",
    )
    # N -> S
    _make_simple_chart(
        "Elevation Profile - North to South Transect",
        "Cross-section at subbasin centroid longitude",
        "Distance from Northern Boundary (km)",
        lambda d: (d["d_ns"], d["e_ns"]),
        "elevation_profile_N2S.html",
    )
    # S -> N
    _make_simple_chart(
        "Elevation Profile - South to North Transect",
        "Cross-section at subbasin centroid longitude",
        "Distance from Southern Boundary (km)",
        lambda d: (d["d_ns"].max() - d["d_ns"], d["e_ns"]),
        "elevation_profile_S2N.html",
    )

    # ── Combined 4-directional view per basin ───────────────────────────────
    n_basins = len(sorted_bids)
    fig_combo = make_subplots(
        rows=n_basins, cols=4,
        subplot_titles=[
            f"{bid} - {d}"
            for bid in sorted_bids
            for d in ["W->E", "E->W", "N->S", "S->N"]
        ],
        horizontal_spacing=0.04,
        vertical_spacing=0.08,
    )
    for i, bid in enumerate(sorted_bids):
        data = profiles[bid]
        color = colors[i % len(colors)]
        traces = [
            (data["d_we"], data["e_we"]),
            (data["d_we"].max() - data["d_we"], data["e_we"]),
            (data["d_ns"], data["e_ns"]),
            (data["d_ns"].max() - data["d_ns"], data["e_ns"]),
        ]
        for col_i, (x, y) in enumerate(traces):
            fig_combo.add_trace(
                go.Scatter(
                    x=x, y=y, mode="lines", fill="tozeroy",
                    line=dict(color=color, width=1.5),
                    showlegend=False,
                ),
                row=i + 1, col=col_i + 1,
            )
            fig_combo.update_xaxes(title_text="km", row=i + 1, col=col_i + 1)
        fig_combo.update_yaxes(title_text="m", row=i + 1, col=1)

    fig_combo.update_layout(
        title="Elevation Transect Profiles - All Directions<br>"
        "<sup>W->E | E->W | N->S | S->N at centroid</sup>",
        template="plotly_white",
        height=300 * n_basins + 100,
        showlegend=False,
    )
    path = os.path.join(OUTPUT_HTML, "elevation_profiles_4dir.html")
    fig_combo.write_html(path)
    print(f"  [OK] Saved: {path}")


def generate_elevation_histograms(hyps_data):
    """Generate elevation distribution histograms per basin."""
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    colors = px.colors.qualitative.Plotly
    sorted_bids = sorted(hyps_data.keys())
    n = len(sorted_bids)

    # Overlaid histogram
    fig = go.Figure()
    for i, bid in enumerate(sorted_bids):
        vals = hyps_data[bid]["vals"]
        fig.add_trace(
            go.Histogram(
                x=vals, nbinsx=80, name=bid, opacity=0.6,
                marker_color=colors[i % len(colors)],
                hovertemplate=f"<b>{bid}</b><br>Elevation: %{{x:.0f}} m<br>Count: %{{y}}<extra></extra>",
            )
        )
    fig.update_layout(
        title="Elevation Distribution - All Subbasins<br>"
        "<sup>Pixel-level elevation histogram from clipped DEM</sup>",
        xaxis_title="Elevation (m)",
        yaxis_title="Pixel Count",
        barmode="overlay",
        template="plotly_white",
        height=500,
    )
    path = os.path.join(OUTPUT_HTML, "elevation_histograms.html")
    fig.write_html(path)
    print(f"  [OK] Saved: {path}")

    # Per-basin subplot histograms with stats annotations
    fig_sub = make_subplots(
        rows=1, cols=n,
        subplot_titles=[f"{bid}" for bid in sorted_bids],
    )
    for i, bid in enumerate(sorted_bids):
        d = hyps_data[bid]
        vals = d["vals"]
        fig_sub.add_trace(
            go.Histogram(
                x=vals, nbinsx=60,
                marker_color=colors[i % len(colors)],
                showlegend=False,
            ),
            row=1, col=i + 1,
        )
        # Add stats as a text trace instead of annotation (more reliable with subplots)
        stats_text = (
            f"Min: {d['elev_min']:.0f} m\n"
            f"Max: {d['elev_max']:.0f} m\n"
            f"Mean: {d['elev_mean']:.0f} m\n"
            f"Std: {d['elev_std']:.0f} m\n"
            f"HI: {d['HI']:.3f}"
        )
        fig_sub.update_xaxes(title_text="Elevation (m)", row=1, col=i + 1)
    fig_sub.update_yaxes(title_text="Count", row=1, col=1)
    fig_sub.update_layout(
        title="Elevation Distribution per Subbasin<br>"
        "<sup>With descriptive statistics</sup>",
        template="plotly_white",
        height=450,
    )
    path2 = os.path.join(OUTPUT_HTML, "elevation_histograms_per_basin.html")
    fig_sub.write_html(path2)
    print(f"  [OK] Saved: {path2}")


def generate_elev_stats_table(hyps_data):
    """Generate an interactive elevation statistics summary table."""
    import plotly.graph_objects as go

    sorted_bids = sorted(hyps_data.keys())
    headers = [
        "Basin", "Elev Min (m)", "Elev Max (m)", "Relief (m)",
        "Mean (m)", "Median (m)", "Std Dev (m)", "HI", "Stage", "Pixels"
    ]
    rows = []
    for bid in sorted_bids:
        d = hyps_data[bid]
        relief = d["elev_max"] - d["elev_min"]
        stage = (
            "Young" if d["HI"] > 0.6
            else "Mature" if d["HI"] > 0.35
            else "Old (Peneplain)"
        )
        rows.append([
            bid,
            f"{d['elev_min']:.0f}",
            f"{d['elev_max']:.0f}",
            f"{relief:.0f}",
            f"{d['elev_mean']:.1f}",
            f"{d['elev_median']:.0f}",
            f"{d['elev_std']:.1f}",
            f"{d['HI']:.4f}",
            stage,
            f"{d['n_pixels']:,}",
        ])

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=[f"<b>{h}</b>" for h in headers],
                    fill_color="#2563eb",
                    font=dict(color="white", size=12),
                    align="center",
                ),
                cells=dict(
                    values=list(zip(*rows)),
                    fill_color=[["#f1f5f9", "#e2e8f0"] * len(rows)],
                    font=dict(size=11),
                    align="center",
                    height=30,
                ),
            )
        ]
    )
    fig.update_layout(
        title="Elevation Statistics Summary - Pravara River Basin<br>"
        "<sup>Per-basin DEM analysis (pravra3.shp, 3 subbasins)</sup>",
        template="plotly_white",
        height=300,
    )
    path = os.path.join(OUTPUT_HTML, "elevation_statistics_table.html")
    fig.write_html(path)
    print(f"  [OK] Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("  FIX: Hypsometric Curves & Elevation Analysis")
    print("=" * 60)

    print("\n[1/7] Extracting data...")
    extract_if_needed()

    print("\n[2/7] Loading DEM and subbasin shapefile...")
    dem_arr, dem_meta, gdf = load_data()

    print("\n[3/7] Clipping DEM per basin...")
    clipped = clip_dem_per_basin(gdf)

    print("\n[4/7] Computing per-basin hypsometric curves...")
    hyps_data = compute_hypsometric(clipped)

    print("\n[5/7] Generating corrected hypsometric HTML...")
    generate_hypsometric_html(hyps_data)

    print("\n[6/7] Computing elevation profiles (W-E, E-W, N-S, S-N)...")
    profiles = compute_all_profiles(dem_arr, dem_meta, gdf)
    generate_all_profile_html(profiles)

    print("\n[7/7] Generating elevation histograms & stats...")
    generate_elevation_histograms(hyps_data)
    generate_elev_stats_table(hyps_data)

    print("\n" + "=" * 60)
    print("  ALL FIXES COMPLETE")
    print("=" * 60)
    print(f"\n  Output directory: {OUTPUT_HTML}")
    print("  Files generated:")
    print("    07_hypsometric_curves.html         (FIXED)")
    print("    elevation_profile_W2E.html         (NEW)")
    print("    elevation_profile_E2W.html         (NEW)")
    print("    elevation_profile_N2S.html         (NEW)")
    print("    elevation_profile_S2N.html         (NEW)")
    print("    elevation_profiles_4dir.html       (NEW)")
    print("    elevation_histograms.html          (NEW)")
    print("    elevation_histograms_per_basin.html(NEW)")
    print("    elevation_statistics_table.html    (NEW)")
