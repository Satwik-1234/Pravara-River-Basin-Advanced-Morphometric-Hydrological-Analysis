#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║   PRAVARA RIVER BASIN — Ultimate Publication Renderer (V15.0)              ║
║   Scope: All 24 Thematic Layers · 600 DPI · Vivid Shading · Times NR       ║
║   Template: Institutional Blueprint · Landscape A4 · Matched Legend        ║
║   Symmetry: X=3-Min / Y=4-Min Symmetric Grids · INTERNAL SCALE & NORTH     ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import warnings
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap
import matplotlib.ticker as mticker
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch
from mpl_toolkits.axes_grid1 import make_axes_locatable

import geopandas as gpd
import rasterio
from rasterio.mask import mask as rio_mask
import contextily as ctx
from pyproj import Transformer
from shapely.geometry import mapping

warnings.filterwarnings('ignore')

# ── GLOBAL CARTOGRAPHIC CONFIG ───────────────────────────────────────────────
DPI = 600
A4_LANDSCAPE = (11.69, 8.27)
FNT_MAIN = 'Times New Roman'
plt.rcParams['font.family'] = FNT_MAIN
plt.rcParams['axes.linewidth'] = 2.0

ESRI_WORLD_TOPO = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}'
transformer_to_wgs = Transformer.from_crs('EPSG:32643', 'EPSG:4326', always_xy=True)
transformer_to_utm = Transformer.from_crs('EPSG:4326', 'EPSG:32643', always_xy=True)

# ── THE ULTIMATE REGISTRY (All 25 Maps) ──────────────────────────────────────
ULTIMATE_REGISTRY = [
    {"id": "01", "name": "Digital Elevation Model", "path": "data/watershed_data/Filled DEM.tif", "cmap": "terrain", "label": "Elevation (m)"},
    {"id": "02", "name": "Slope Distribution", "path": "outputs/thematic_rasters/slope.tif", "cmap": "magma", "label": "Slope (Degrees)"},
    {"id": "03", "name": "Aspect Map", "path": "outputs/thematic_rasters/aspect.tif", "cmap": "twilight", "label": "Aspect (Degrees)"},
    {"id": "04", "name": "Topographic Wetness Index", "path": "outputs/thematic_rasters/twi.tif", "cmap": "GnBu", "label": "TWI Value"},
    {"id": "05", "name": "Stream Power Index", "path": "outputs/thematic_rasters/spi.tif", "cmap": "magma", "label": "SPI Value (Log)", "norm": "log"},
    {"id": "06", "name": "Sediment Transport Index", "path": "outputs/thematic_rasters/sti.tif", "cmap": "YlOrRd", "label": "STI Value (Log)", "norm": "log"},
    {"id": "07", "name": "Topographic Ruggedness Index", "path": "outputs/thematic_rasters/tri.tif", "cmap": "magma", "label": "TRI Value"},
    {"id": "08", "name": "Tectonic Lineament Density", "path": "outputs/thematic_rasters/lineament_proxy.tif", "cmap": "Reds", "label": "Density (km/km2)"},
    {"id": "09", "name": "Flow Direction", "path": "data/watershed_data/Flow Direction.tif", "cmap": "tab20", "label": "Direction Code"},
    {"id": "10", "name": "Flow Accumulation", "path": "data/watershed_data/FlowAccumilation.tif", "cmap": "Blues", "label": "Cell Count"},
    {"id": "11", "name": "Curve Number CN Map", "path": "outputs/thematic_rasters/CN.tif", "cmap": "YlGn", "label": "CN Value"},
    {"id": "12", "name": "Flash Flood Potential Index", "path": "outputs/thematic_rasters/FFPI.tif", "cmap": "OrRd", "label": "FFPI Value"},
    {"id": "13", "name": "Geomorphic Anomaly Index", "path": "outputs/thematic_rasters/GAI.tif", "cmap": "coolwarm", "label": "GAI Value"},
    {"id": "14", "name": "HI High Anomaly Areas", "path": "outputs/thematic_rasters/GAI_high_anomaly.tif", "cmap": "Reds", "label": "Anomaly Severity"},
    {"id": "15", "name": "Percolation Potential", "path": "outputs/thematic_rasters/percolation_potential.tif", "cmap": "Greens", "label": "Suitability Class"},
    {"id": "16", "name": "Contour Trench Suitability", "path": "outputs/thematic_rasters/contour_trench_suitability.tif", "cmap": "Purples", "label": "Suitability Class"},
    {"id": "17", "name": "RUSLE Potential Soil Loss", "path": "outputs/thematic_rasters/RUSLE_A.tif", "cmap": "YlOrBr", "label": "Loss (t/ha/yr)"},
    {"id": "18", "name": "RUSLE C-Factor Land Cover", "path": "outputs/thematic_rasters/RUSLE_C.tif", "cmap": "PiYG", "label": "C-Factor"},
    {"id": "19", "name": "RUSLE K-Factor Erodibility", "path": "outputs/thematic_rasters/RUSLE_K.tif", "cmap": "copper", "label": "K-Factor"},
    {"id": "20", "name": "RUSLE LS-Factor Topography", "path": "outputs/thematic_rasters/RUSLE_LS.tif", "cmap": "inferno", "label": "LS-Factor"},
    {"id": "21", "name": "RUSLE P-Factor Conservation", "path": "outputs/thematic_rasters/RUSLE_P.tif", "cmap": "summer", "label": "P-Factor"},
    {"id": "22", "name": "RUSLE R-Factor Rainfall", "path": "outputs/thematic_rasters/RUSLE_R.tif", "cmap": "YlGnBu", "label": "R-Factor"},
    {"id": "23", "name": "Stream Order Map", "path": "data/watershed_data/SteamOrder.shp", "categorical": True, "legend_type": "lines"},
    {"id": "24", "name": "Drainage Density Map", "path": "data/watershed_data/Flowthreshould.tif", "cmap": "jet", "label": "Density Class"},
    {"id": "25", "name": "Topographic Contour Map", "path": "data/watershed_data/Filled DEM.tif", "categorical": True, "legend_type": "lines"}
]


# ── LOGIC UTILITIES ──────────────────────────────────────────────────────────

def to_dms_label(val, is_lon):
    lon, lat = transformer_to_wgs.transform(val, 2160000) if is_lon else transformer_to_wgs.transform(370000, val)
    deg = lon if is_lon else lat
    d = int(deg); frac = abs(deg - d); m = int(round(frac * 60))
    if m == 60: d += 1; m = 0
    return f"{d}º{m:02d}'{('E' if deg >=0 else 'W') if is_lon else ('N' if deg >=0 else 'S')}"

def get_clip_patch(ax, shp_path):
    gdf = gpd.read_file(shp_path)
    poly = gdf.geometry.unary_union
    if poly.geom_type == 'Polygon': polys = [poly]
    else: polys = list(poly.geoms)
    patches = []
    for p in polys:
        verts = np.array(p.exterior.coords)
        codes = [MPath.MOVETO] + [MPath.LINETO]*(len(verts)-2) + [MPath.CLOSEPOLY]
        patches.append(MPath(verts, codes))
    return PathPatch(MPath.make_compound_path(*patches), transform=ax.transData)

def add_line_legend_panel(ax, colors, labels, title='Legend', internal=False):
    if internal:
        # Bottom-Right Inside Grid (Tucked deeper into corner)
        ax_p = ax.inset_axes([0.72, 0.01, 0.27, 0.25], transform=ax.transAxes)
    else:
        # Standard Outside Right
        ax_p = ax.inset_axes([1.05, 0.2, 0.25, 0.6], transform=ax.transAxes)
    
    ax_p.axis('off')
    # Add a subtle semi-transparent white background for internal legends
    if internal:
        ax_p.patch.set_facecolor('white')
        ax_p.patch.set_alpha(0.7)
        
    ax_p.text(0, 1.0, title, fontweight='bold', fontsize=12, transform=ax_p.transAxes)
    for i, (col, lbl) in enumerate(zip(colors, labels)):
        y = 0.85 - (i * 0.12) if internal else 0.9 - (i * 0.08)
        ax_p.plot([0, 0.15], [y, y], color=col, lw=3.0, transform=ax_p.transAxes)
        ax_p.text(0.20, y, lbl, va='center', fontsize=11 if internal else 10, transform=ax_p.transAxes)

# ── CORE RENDERER ─────────────────────────────────────────────────────────────

def render_ultimate_map(m_cfg, boundary_path):
    print(f"Rendering {m_cfg['id']}: {m_cfg['name']}...")
    fig = plt.figure(figsize=A4_LANDSCAPE, dpi=DPI, facecolor='white')
    ax = fig.add_axes([0.14, 0.15, 0.60, 0.70])
    
    gdf_bound = gpd.read_file(boundary_path).dissolve()
    
    # Basemap (Always ESRI World Topo)
    ctx.add_basemap(ax, crs='EPSG:32643', source=ESRI_WORLD_TOPO, alpha=0.8, attribution=False, zorder=0, zoom=10)
    
    # Clip Boundary
    patch = get_clip_patch(ax, boundary_path)
    ax.set_clip_path(patch)

    # ── MAP CORE CONTENT ──────────────────────────────────────────────────────
    data_path = m_cfg['path']
    if not os.path.exists(data_path):
        print(f"Warning: Path {data_path} not found.")
        return

    # Draw Study Area Boundary (Always, on top)
    gdf_bound.plot(ax=ax, facecolor='none', edgecolor='black', linewidth=2.0, zorder=100)

    if m_cfg.get('legend_type') == 'lines':
        if m_cfg['id'] == '23': # Stream Order (Vector)
            gdf_so = gpd.read_file(data_path)
            # Use 'grid_code' for order (lowercase as per file metadata)
            order_col = 'grid_code' if 'grid_code' in gdf_so.columns else None
            if order_col:
                orders = sorted(gdf_so[order_col].unique())
                cmap = plt.get_cmap('plasma_r', len(orders))
                colors = [cmap(i) for i in range(len(orders))]
                for i, order in enumerate(orders):
                    gdf_so[gdf_so[order_col] == order].plot(ax=ax, color=colors[i], lw=0.4 + order*0.7, zorder=10)
                add_line_legend_panel(ax, colors, [f"Order {int(ord)}" for ord in orders], title='Stream Order', internal=True)
            else:
                gdf_so.plot(ax=ax, color='blue', lw=1.0, zorder=10)
                add_line_legend_panel(ax, ['blue'], ['Stream Network'], title='Streams')
        
        elif m_cfg['id'] == '25': # Contour Map (from DEM)
            with rasterio.open(data_path) as src:
                out_image, out_transform = rio_mask(src, gdf_bound.geometry, crop=False)
                arr = out_image[0].astype(float); arr[arr == src.nodata] = np.nan
                b = src.bounds
                x = np.linspace(b.left, b.right, arr.shape[1])
                y = np.linspace(b.bottom, b.top, arr.shape[0])[::-1]
                XX, YY = np.meshgrid(x, y)
                
                # Single 25m interval as requested
                levels = np.arange(np.floor(np.nanmin(arr)/25)*25, np.nanmax(arr)+25, 25)
                
                # No labels as requested to avoid crowding
                ax.contour(XX, YY, arr, levels=levels, colors='#5D2906', linewidths=0.8, alpha=0.8, zorder=9)
                
                add_line_legend_panel(ax, ['#5D2906'], ['Contour Interval - 25 mtr'], title='Topography', internal=True)
        
    
    else: # Default Raster Rendering
        with rasterio.open(data_path) as src:
            out_image, out_transform = rio_mask(src, gdf_bound.geometry, crop=False)
            data = out_image[0].astype(float); data[data == src.nodata] = np.nan
            ext = [src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top]
            
            if m_cfg.get('norm') == 'log':
                from matplotlib.colors import LogNorm
                d_safe = np.where(data <= 0, np.nanmin(data[data > 0]) if np.any(data > 0) else 1e-6, data)
                norm = LogNorm(vmin=np.nanmin(d_safe), vmax=np.nanmax(d_safe))
                im = ax.imshow(d_safe, extent=ext, cmap=m_cfg['cmap'], alpha=1.0, zorder=5, norm=norm)
            else:
                norm = mcolors.Normalize(vmin=np.nanmin(data), vmax=np.nanmax(data))
                im = ax.imshow(data, extent=ext, cmap=m_cfg['cmap'], alpha=1.0, zorder=5, norm=norm)
            
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="3%", pad=0.7)
            sm = plt.cm.ScalarMappable(cmap=plt.get_cmap(m_cfg['cmap']), norm=norm)
            cb = plt.colorbar(sm, cax=cax, orientation='vertical')
            cb.ax.tick_params(labelsize=10)
            cb.set_label(m_cfg['label'], fontsize=12, fontweight='bold', labelpad=15)
            cb.outline.set_linewidth(1.8)

    # Grids (X=3', Y=4')
    deg_x_steps = np.arange(73.5, 74.0, 0.050) # 3-min
    x_ticks_utm = [transformer_to_utm.transform(d, 19.5)[0] for d in deg_x_steps]
    ax.xaxis.set_major_locator(mticker.FixedLocator(x_ticks_utm))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: to_dms_label(v, True)))
    
    deg_y_steps = np.arange(19.4, 19.8, 0.0666) # 4-min
    y_ticks_utm = [transformer_to_utm.transform(73.7, d)[1] for d in deg_y_steps]
    ax.yaxis.set_major_locator(mticker.FixedLocator(y_ticks_utm))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: to_dms_label(v, False)))
    
    ax.tick_params(top=True, labeltop=True, right=True, labelright=True)
    ax.tick_params(axis='y', which='major', labelsize=11, labelrotation=90)
    ax.tick_params(axis='x', which='major', labelsize=11)
    ax.grid(True, linestyle=(0, (1, 15)), color='black', alpha=0.3, zorder=0)

    # Standard buffer plus extra room on right and bottom for internal Legend (IDs 23, 25)
    xl, yl, xr, yr = gdf_bound.total_bounds
    width, height = xr-xl, yr-yl
    # Asymmetrical padding: basin shifted slightly Top-Left to clear Bottom-Right corner
    ax.set_xlim(xl - 5000, xr + width * 0.28)
    ax.set_ylim(yl - height * 0.22, yr + 5000)

    # Internal Furniture (Small & Cornered)
    ax.text(0.02, 0.97, m_cfg['name'].upper(), ha='left', va='top', fontweight='bold', fontsize=18, transform=ax.transAxes, zorder=300)
    # Subtitle removed globally
    
    nax = ax.inset_axes([0.94, 0.90, 0.04, 0.07], transform=ax.transAxes, zorder=305)
    nax.axis('off')
    nax.annotate('', xy=(0.5, 0.92), xytext=(0.5, 0.08), arrowprops=dict(arrowstyle='simple', facecolor='black', lw=0.8))
    nax.text(0.5, 0.98, 'N', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    # Scale Bar (Internal)
    draw_block_scale_final(ax, 0.02, 0.04)
    
    # Frame
    for s in ax.spines.values(): s.set_linewidth(2.5)
    
    out_dir = 'outputs/ultimate_publication_suite'
    os.makedirs(out_dir, exist_ok=True)
    out_path = f"{out_dir}/{m_cfg['id']}_{m_cfg['name'].replace(' ', '_')}.png"
    fig.savefig(out_path, dpi=DPI, facecolor='white')
    plt.close(fig)

def draw_block_scale_final(ax, x_f, y_f):
    xl, xr = ax.get_xlim(); yr_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    map_w = xr - xl; nice = map_w * 0.14
    mag = 10**np.floor(np.log10(nice)); nice = min([1, 2, 5, 10], key=lambda c: abs(c*mag - nice)) * mag
    seg_w = nice / 2
    x0, y0 = xl + map_w * x_f, ax.get_ylim()[0] + yr_range * y_f
    bh = yr_range * 0.022
    for i in range(2):
        ax.add_patch(mpatches.Rectangle((x0 + i*seg_w, y0), seg_w, bh, facecolor='black' if i%2==0 else 'white', edgecolor='black', lw=2.0, zorder=310))
    ax.text(x0, y0+bh+yr_range*0.012, '0', ha='center', fontsize=11, zorder=315)
    ax.text(x0+nice, y0+bh+yr_range*0.012, f'{int(nice/1000)} km', ha='center', fontsize=11, zorder=315)

if __name__ == '__main__':
    bound_shp = 'data/watershed_data/pravra3.shp'
    for m in ULTIMATE_REGISTRY:
        try:
            render_ultimate_map(m, bound_shp)
        except Exception as e:
            print(f"Skipping {m['name']}: {e}")
