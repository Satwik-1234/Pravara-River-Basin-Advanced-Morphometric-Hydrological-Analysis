#!/usr/bin/env python3
"""
Pravara River Basin — Production Atlas Cartography Engine (300 DPI).
Preserves the exact production layout, styling, typography, and cartographic symbology
from the institutional atlas standard (Lohara/Tuljapur reference):
 - Clean white sheet framing with delicate neatline and DMS graticule ticks
 - Shaded 3D relief blending (LightSource azimuth 315 deg, altitude 45 deg)
 - Basin & Sub-basin cadastral boundaries (crimson outer #c1121f, slate dashed inner)
 - Subbasin centroids and area labels with white halo text
 - Times New Roman three-line institutional header (Category, BASIN, District/State)
 - Alternating black/white segmented scale bar and feathered North Arrow
 - Dynamic corner placement of transparent legends and compact horizontal colorbars
 - Bottom-left projection metadata and bottom-right scientific data attribution
"""

import os
import sys
import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.path import Path as MPath
import geopandas as gpd
import numpy as np
import pyproj
import rasterio
from rasterio.mask import mask
from shapely.geometry import box
import contextily as ctx

try:
    from adjustText import adjust_text
except ImportError:
    adjust_text = None

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------- directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "watershed_data"
RASTERS_DIR = BASE_DIR / "outputs" / "thematic_rasters"
OUTPUT_DIR = BASE_DIR / "outputs" / "ultimate_publication_suite"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- typography & style
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "Liberation Serif", "DejaVu Serif", "serif"]
plt.rcParams["axes.linewidth"] = 0.9

RED = "#c1121f"
INK = "#1a1a1a"
GREY = "#6b7280"
DOT = "#262626"
HALO = [pe.withStroke(linewidth=2.4, foreground="white")]
SUBTITLE = "Ahmednagar District, Maharashtra"
BASIN_TITLE = "PRAVARA RIVER BASIN"

# sheet geometry (inches) & resolution
DPI = 600
MAP_MAX_W, MAP_MAX_H, MAP_MIN_W = 9.0, 11.0, 6.5
M_LEFT, M_RIGHT, M_TOP, M_BOTTOM = 0.65, 0.65, 1.60, 0.60
PAD_FRAC = 0.08

# ---------------------------------------------------------------- CRS Transformers
TO_UTM = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32643", always_xy=True)
TO_WGS = pyproj.Transformer.from_crs("EPSG:32643", "EPSG:4326", always_xy=True)

# ---------------------------------------------------------------- Geometry Helpers
def geom_to_path(geom):
    verts, codes = [], []
    for poly in getattr(geom, "geoms", [geom]):
        for ring in [poly.exterior, *poly.interiors]:
            xy = np.asarray(ring.coords)
            verts.extend(xy)
            codes.extend([MPath.MOVETO] + [MPath.LINETO] * (len(xy) - 2) + [MPath.CLOSEPOLY])
    return MPath(verts, codes)

def clip_to_geom(artist, ax, geom):
    patch = mpatches.PathPatch(geom_to_path(geom), transform=ax.transData, fc="none", ec="none")
    try:
        artist.set_clip_path(patch)
    except AttributeError:
        for c in artist.collections:
            c.set_clip_path(patch)

def clipped(path, geom, nodata=None, band=0, buffer=0):
    with rasterio.open(path) as src:
        g = geom.buffer(buffer) if buffer else geom
        nd = src.nodata if nodata is None else nodata
        kw = {} if nd is None else {"nodata": nd}
        try:
            out_img, out_tr = mask(src, [g], crop=True, **kw)
        except Exception:
            out_img, out_tr = mask(src, [g], crop=True)
            nd = src.nodata
        arr = out_img[band].astype("float32")
        if nd is not None:
            arr[arr == nd] = np.nan
        extent = (out_tr[2], out_tr[2] + out_tr[0] * arr.shape[1],
                  out_tr[5] + out_tr[4] * arr.shape[0], out_tr[5])
        return arr, extent

def get_hillshade_array(geom, vert_exag=3.5):
    dem_path = DATA_DIR / "Filled DEM.tif"
    if not dem_path.exists():
        return None, None, None
    arr, ext = clipped(dem_path, geom, nodata=-9999)
    dem = arr.astype("float32")
    bad = ~np.isfinite(dem) | (dem < -500)
    if np.all(bad):
        return None, None, None
    dem[bad] = np.nanmin(dem[~bad])
    hs = mcolors.LightSource(azdeg=315, altdeg=45).hillshade(dem, vert_exag=vert_exag)
    return hs, ext, bad

def hillshade(ax, geom, alpha=0.45, vert_exag=3.5, zorder=1):
    hs, ext, bad = get_hillshade_array(geom, vert_exag=vert_exag)
    if hs is None:
        return
    rgba = plt.cm.gray(0.20 + 0.80 * hs)
    rgba[..., 3] = np.where(bad, 0.0, alpha)
    im = ax.imshow(rgba, extent=ext, zorder=zorder, interpolation="bilinear")
    clip_to_geom(im, ax, geom)

# ---------------------------------------------------------------- Subbasin overlays
def overlay_subbasins(ax, subbasins_gdf):
    if subbasins_gdf is None or subbasins_gdf.empty:
        return
    subbasins_gdf.boundary.plot(ax=ax, color="#475569", linewidth=0.6, linestyle="--", alpha=0.85, zorder=6)
    pts = []
    for _, r in subbasins_gdf.iterrows():
        pt = r.geometry.representative_point()
        name = str(r.get("name", "Subbasin")).strip()
        pts.append((pt.x, pt.y, name))
        ax.scatter([pt.x], [pt.y], s=12, color=DOT, edgecolors="white", linewidths=0.6, zorder=11)
    
    texts = [ax.text(x, y + 250, s, fontsize=7.2, fontweight="bold", ha="center", va="center",
                     color=INK, path_effects=HALO, zorder=12) for x, y, s in pts]
    if adjust_text and texts:
        try:
            adjust_text(texts, ax=ax)
        except Exception:
            pass

# ---------------------------------------------------------------- Legend entry builders
def line(label, color, lw=1.5, ls="-"):
    return ("line", dict(color=color, lw=lw, ls=ls), label)

def patch(label, fc, ec="none"):
    return ("patch", dict(fc=fc, ec=ec), label)

def dot(label, color=DOT):
    return ("point", dict(color=color), label)

# ---------------------------------------------------------------- Map Furniture
def legend_el(title, entries, fs=8.0):
    rh, pad, sw, th = 0.18, 0.12, 0.32, 0.26
    w = max(pad * 2 + sw + 0.10 + max(len(e[2]) for e in entries) * 0.065, pad * 2 + len(title) * 0.085)
    h = pad + th + rh * len(entries) + pad * 0.5

    def draw(ia, w, h):
        ia.patch.set_alpha(0.0)
        ia.patch.set_facecolor("none")
        ia.text(pad, h - pad - 0.06, title, fontsize=fs + 1.2, fontweight="bold", va="center", ha="left", color=INK, path_effects=HALO, zorder=2)
        for i, (kind, st, label) in enumerate(entries):
            y = h - pad - th - rh * (i + 0.5)
            if kind == "line":
                ia.plot([pad, pad + sw], [y, y], color=st["color"], lw=st["lw"], ls=st["ls"], solid_capstyle="butt", zorder=2)
            elif kind == "patch":
                ia.add_patch(mpatches.Rectangle((pad, y - 0.05), sw, 0.10, fc=st["fc"], ec=st["ec"], lw=0.5, zorder=2))
            else:
                ia.plot([pad + sw / 2], [y], "o", color=st["color"], ms=4.0, mec="white", mew=0.6, zorder=2)
            ia.text(pad + sw + 0.10, y, label, fontsize=fs, va="center_baseline", ha="left", color=INK, path_effects=HALO, zorder=2)
    return w, h, draw

def scalebar_el(ax):
    fig, pos = ax.figure, ax.get_position()
    aw = pos.width * fig.get_figwidth()
    x0, x1 = ax.get_xlim()
    mpi = (x1 - x0) / aw
    target = 2.4 * mpi
    km = max([k for k in (2, 4, 5, 8, 10, 15, 20) if k * 1000 <= target] or [5])
    bar = km * 1000 / mpi
    ox = 0.12
    w = ox + bar + 0.45
    h = 1.30

    def draw(ia, w, h):
        ia.patch.set_alpha(0.0)
        ia.patch.set_facecolor("none")
        sb_y = h - 0.28
        seg = bar / 4
        for i in range(4):
            ia.add_patch(mpatches.Rectangle((ox + i * seg, sb_y), seg, 0.08,
                                            fc="black" if i % 2 == 0 else "white", ec="black", lw=0.7, zorder=2))
        for frac, lab in ((0, "0"), (0.5, f"{km / 2:.1f}".rstrip('0').rstrip('.')), (1, f"{km} km")):
            ia.text(ox + frac * bar, sb_y + 0.12, lab, fontsize=7.5, ha="center", va="bottom", color=INK, path_effects=HALO, zorder=2)

        # North arrow directly below scale bar
        c = ox + bar / 2
        arrow_top = sb_y - 0.22
        arrow_bot = arrow_top - 0.48
        arrow_mid = arrow_top - 0.36
        dx = 0.11
        ia.add_patch(mpatches.Polygon([(c, arrow_top), (c - dx, arrow_bot), (c, arrow_mid)], fc="black", ec="black", lw=0.7, zorder=2))
        ia.add_patch(mpatches.Polygon([(c, arrow_top), (c + dx, arrow_bot), (c, arrow_mid)], fc="white", ec="black", lw=0.7, zorder=2))
        ia.text(c, arrow_top + 0.03, "N", fontsize=11, fontweight="bold", ha="center", va="bottom", color=INK, path_effects=HALO, zorder=2)
    return w, h, draw

def cbar_el(vmin, vmax, cmap, title, unit=""):
    w, h = 2.4, 0.62

    def draw(ia, w, h):
        ia.patch.set_alpha(0.0)
        ia.patch.set_facecolor("none")
        hdr = f"{title} ({unit})" if unit else title
        ia.text(0.13, h - 0.14, hdr, fontsize=8.5, fontweight="bold", va="center", ha="left", color=INK, path_effects=HALO, zorder=2)
        gradient = np.linspace(0, 1, 256)[None, :]
        ia.imshow(gradient, extent=(0.13, w - 0.13, 0.22, 0.34), cmap=cmap, aspect="auto", zorder=2)
        ia.add_patch(mpatches.Rectangle((0.13, 0.22), w - 0.26, 0.12, fc="none", ec="#475569", lw=0.6, zorder=3))
        ia.set_xlim(0, w); ia.set_ylim(0, h); ia.axis("off")
        for f in (0, 0.5, 1):
            val = vmin + f * (vmax - vmin)
            lab = f"{val:.1f}" if abs(val) < 100 and val != int(val) else f"{val:.0f}"
            ia.text(0.13 + f * (w - 0.26), 0.17, lab, fontsize=7.2, ha="center", va="top", color=INK, path_effects=HALO, zorder=2)
    return w, h, draw

# ---------------------------------------------------------------- Element placement
def place_elements(ax, geom, elements):
    fig, pos = ax.figure, ax.get_position()
    aw, ah = pos.width * fig.get_figwidth(), pos.height * fig.get_figheight()
    (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
    sx, sy = (x1 - x0) / aw, (y1 - y0) / ah
    m, pad = 0.12, 0.10
    free = ["ul", "ll", "lr", "ur"]
    for w, h, draw in elements:
        best = None
        for c in free:
            xa = m if c[1] == "l" else aw - m - w
            ya = m if c[0] == "l" else ah - m - h
            bx = box(x0 + (xa - pad) * sx, y0 + (ya - pad) * sy, x0 + (xa + w + pad) * sx, y0 + (ya + h + pad) * sy)
            ov = geom.intersection(bx).area
            if best is None or ov < best[0] - 1e-9:
                best = (ov, c, xa, ya)
        _, c, xa, ya = best
        free.remove(c)
        ia = ax.inset_axes([xa / aw, ya / ah, w / aw, h / ah])
        ia.patch.set_alpha(0.0)
        ia.patch.set_facecolor("none")
        ia.set_xlim(0, w); ia.set_ylim(0, h); ia.axis("off"); ia.set_zorder(30)
        draw(ia, w, h)
        ia.set_xlim(0, w); ia.set_ylim(0, h); ia.axis("off"); ia.set_zorder(30)
        draw(ia, w, h)

# ---------------------------------------------------------------- DMS Ticks
def dms_ticks(ax):
    (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
    cs = [TO_WGS.transform(x, y) for x in (x0, x1) for y in (y0, y1)]
    lons, lats = [c[0] for c in cs], [c[1] for c in cs]
    lo0, lo1, la0, la1 = min(lons), max(lons), min(lats), max(lats)
    span = max(lo1 - lo0, la1 - la0) * 60
    step = next((s for s in (1, 2, 3, 5, 10, 15) if span / s <= 8), 5)
    xt, xl, yt, yl = [], [], [], []
    for m in range(int(np.ceil(lo0 * 60 / step)) * step, int(np.floor(lo1 * 60 / step)) * step + 1, step):
        x = TO_UTM.transform(m / 60, (la0 + la1) / 2)[0]
        if x0 <= x <= x1:
            xt.append(x); xl.append(f"{m // 60}°{m % 60:02d}′E")
    for m in range(int(np.ceil(la0 * 60 / step)) * step, int(np.floor(la1 * 60 / step)) * step + 1, step):
        y = TO_UTM.transform((lo0 + lo1) / 2, m / 60)[1]
        if y0 <= y <= y1:
            yt.append(y); yl.append(f"{m // 60}°{m % 60:02d}′N")
    ax.set_xticks(xt); ax.set_xticklabels(xl, fontsize=7.5, color=INK)
    ax.set_yticks(yt); ax.set_yticklabels(yl, fontsize=7.5, color=INK)
    ax.tick_params(axis="both", direction="out", length=4, width=0.8, pad=3, colors=INK,
                   top=True, bottom=True, left=True, right=True,
                   labeltop=True, labelbottom=True, labelleft=True, labelright=True)
    for t in ax.yaxis.get_major_ticks():
        t.label1.set_rotation(90); t.label1.set_va("center")
        t.label2.set_rotation(270); t.label2.set_va("center")
    ax.grid(True, linestyle=":", linewidth=0.55, color="#94a3b8", alpha=0.65, zorder=8)

# ---------------------------------------------------------------- Sheet Initializer
def new_sheet(gdf_boundary, title):
    bounds = gdf_boundary.total_bounds
    bw, bh = bounds[2] - bounds[0], bounds[3] - bounds[1]
    pad_x, pad_y = bw * PAD_FRAC, bh * PAD_FRAC
    xlim = (bounds[0] - pad_x, bounds[2] + pad_x)
    ylim = (bounds[1] - pad_y, bounds[3] + pad_y)
    ar = (xlim[1] - xlim[0]) / (ylim[1] - ylim[0])

    if ar >= 1.0:
        map_w = MAP_MAX_W
        map_h = max(map_w / ar, 4.5)
    else:
        map_h = MAP_MAX_H
        map_w = max(map_h * ar, MAP_MIN_W)

    fw = map_w + M_LEFT + M_RIGHT
    fh = map_h + M_TOP + M_BOTTOM

    fig = plt.figure(figsize=(fw, fh), dpi=DPI, facecolor="white")
    ax = fig.add_axes([M_LEFT / fw, M_BOTTOM / fh, map_w / fw, map_h / fh])
    ax.set_xlim(xlim); ax.set_ylim(ylim); ax.set_aspect("equal", adjustable="box")
    ax.sheet_lim = (xlim, ylim)

    geom_union = gdf_boundary.geometry.union_all() if hasattr(gdf_boundary.geometry, "union_all") else gdf_boundary.geometry.unary_union

    # 1. Continuous Esri World Topographic Basemap
    try:
        ctx.add_basemap(ax, crs='EPSG:32643', source=ctx.providers.Esri.WorldTopoMap, attribution=False, zorder=0)
    except Exception as e:
        print(f"Basemap warning: {e}")

    # 2. Ambient Dimming Mask Outside Basin (35% white veil)
    try:
        outer_box = box(xlim[0] - 100000, ylim[0] - 100000, xlim[1] + 100000, ylim[1] + 100000)
        exterior_mask = outer_box.difference(geom_union)
        mask_patch = mpatches.PathPatch(geom_to_path(exterior_mask), transform=ax.transData, fc="white", alpha=0.35, ec="none", zorder=1)
        ax.add_patch(mask_patch)
    except Exception as e:
        print(f"Ambient mask warning: {e}")

    fig.text(0.5, 1 - 0.30 / fh, title.upper(), fontsize=11.5, ha="center", va="center", color="#374151")
    fig.text(0.5, 1 - 0.68 / fh, BASIN_TITLE, fontsize=24, fontweight="bold", ha="center", va="center", color=INK)
    fig.text(0.5, 1 - 0.98 / fh, SUBTITLE, fontsize=9, style="italic", ha="center", va="center", color=GREY)
    fig.text(M_LEFT / fw, 0.13 / fh, "Projection: UTM Zone 43N  |  Datum: WGS 84", fontsize=7, color=GREY, ha="left", va="center")
    return fig, ax, geom_union

def finish(fig, ax, gdf_boundary, subbasins_gdf, geom, out_path, legend_title, entries, extra=(), bnd=RED, source=""):
    ax.set_xlim(ax.sheet_lim[0]); ax.set_ylim(ax.sheet_lim[1])
    overlay_subbasins(ax, subbasins_gdf)
    gdf_boundary.boundary.plot(ax=ax, color=bnd, linewidth=1.8, zorder=10)
    ax.set_xlim(ax.sheet_lim[0]); ax.set_ylim(ax.sheet_lim[1])
    dms_ticks(ax)
    
    entries = [*entries, line("Sub-basin boundary", "#475569", 0.8, "--"), dot("Sub-basin centroid")]
    place_elements(ax, geom, [*extra, legend_el(legend_title, entries), scalebar_el(ax)])
    if source:
        fig.text(1 - M_RIGHT / fig.get_figwidth(), 0.13 / fig.get_figheight(), source, fontsize=7,
                 color=GREY, ha="right", va="center", style="italic")
    fig.savefig(out_path, dpi=DPI, facecolor="white")
    plt.close(fig)
    plt.close('all')
    import gc
    gc.collect()
    print(f"Saved: {Path(out_path).name}")

# ---------------------------------------------------------------- RENDERERS
def render_dem(gdf_bound, gdf_sub, out_path):
    fig, ax, geom = new_sheet(gdf_bound, "Digital Elevation Model (DEM) of")
    arr, ext = clipped(DATA_DIR / "Filled DEM.tif", geom, nodata=-9999)
    dem = arr.astype("float32")
    bad = ~np.isfinite(dem) | (dem < -500)
    vmin, vmax = float(dem[~bad].min()), float(dem[~bad].max())
    dem[bad] = vmin
    cmap = plt.get_cmap("terrain")
    rgb = mcolors.LightSource(azdeg=315, altdeg=45).shade(dem, cmap=cmap, blend_mode="overlay",
                                                         vert_exag=3.5, vmin=vmin, vmax=vmax)
    rgb[bad, 3] = 0
    im = ax.imshow(rgb, extent=ext, zorder=2, interpolation="bilinear")
    clip_to_geom(im, ax, geom)
    finish(fig, ax, gdf_bound, gdf_sub, geom, out_path, "Legend",
           [line("Basin boundary", RED, 2)],
           extra=[cbar_el(round(vmin), round(vmax), cmap, "Elevation", "m a.s.l.")],
           source="Copernicus DEM GLO-30 (ESA / Airbus Defence & Space)")

def render_contours(gdf_bound, gdf_sub, out_path):
    fig, ax, geom = new_sheet(gdf_bound, "High-Resolution Contour (25 m) Map of")
    hillshade(ax, geom, 0.45)
    arr, ext = clipped(DATA_DIR / "Filled DEM.tif", geom, nodata=-9999)
    dem = arr.astype("float32")
    bad = ~np.isfinite(dem) | (dem < -500)
    dem[bad] = np.nan
    x = np.linspace(ext[0], ext[1], dem.shape[1])
    y = np.linspace(ext[3], ext[2], dem.shape[0])
    
    # 25m interval contours, 100m index
    levels_all = np.arange(np.floor(np.nanmin(dem) / 25) * 25, np.nanmax(dem) + 25, 25)
    levels_idx = [l for l in levels_all if l % 100 == 0]
    levels_int = [l for l in levels_all if l % 100 != 0]
    
    c_int = ax.contour(x, y, dem, levels=levels_int, colors="#854d0e", linewidths=0.45, alpha=0.75, zorder=4)
    clip_to_geom(c_int, ax, geom)
    c_idx = ax.contour(x, y, dem, levels=levels_idx, colors="#713f12", linewidths=0.95, alpha=0.95, zorder=5)
    clip_to_geom(c_idx, ax, geom)
    
    # Labels on index contours
    clip_patch = mpatches.PathPatch(geom_to_path(geom), transform=ax.transData, fc="none", ec="none")
    ax.add_patch(clip_patch)
    for t in ax.clabel(c_idx, inline=True, fmt="%d", fontsize=7.0, colors="#713f12"):
        t.set_path_effects(HALO)
        t.set_clip_path(clip_patch)
        
    finish(fig, ax, gdf_bound, gdf_sub, geom, out_path, "Legend",
           [line("Basin boundary", RED, 2),
            line("Index contour (100 m)", "#713f12", 1.2),
            line("Contour (25 m)", "#854d0e", 0.6)],
           source="Derived from Copernicus GLO-30 DEM (ESA/Airbus)")

def render_stream_orders(gdf_bound, gdf_sub, out_path):
    fig, ax, geom = new_sheet(gdf_bound, "Strahler Stream Order & Drainage Map of")
    hillshade(ax, geom, 0.45, vert_exag=4.0)
    gdf_so = gpd.read_file(DATA_DIR / "SteamOrder.shp")
    if gdf_so.crs != "EPSG:32643":
        gdf_so = gdf_so.to_crs("EPSG:32643")
    sc = gpd.clip(gdf_so, geom)
    order_style = {
        1: ("#7dd3fc", 0.6, "1st Order Stream"),
        2: ("#38bdf8", 1.0, "2nd Order Stream"),
        3: ("#0284c7", 1.6, "3rd Order Stream"),
        4: ("#1d4ed8", 2.2, "4th Order Stream"),
        5: ("#1e3a8a", 2.8, "5th Order Stream"),
        6: ("#0f172a", 3.6, "6th Order Trunk (Pravara)"),
    }
    entries = [line("Basin boundary", RED, 2)]
    order_col = "grid_code" if "grid_code" in sc.columns else "order"
    for order in sorted(sc[order_col].unique()):
        col, lw, lab = order_style.get(int(order), ("#0f172a", 2.0, f"Order {int(order)}"))
        sc[sc[order_col] == order].plot(ax=ax, color=col, linewidth=lw, zorder=3 + int(order))
        entries.append(line(lab, col, lw))
    finish(fig, ax, gdf_bound, gdf_sub, geom, out_path, "Legend", entries,
           source="Derived from Copernicus GLO-30 DEM (D8 Flow Routing, Strahler Hierarchy)")

def render_generic_raster(gdf_bound, gdf_sub, raster_path, out_path, title, label, cmap_name, unit="", vmin=None, vmax=None, log_scale=False, source="Pravara Hydrological Analysis Suite"):
    fig, ax, geom = new_sheet(gdf_bound, f"{title} of")
    hillshade(ax, geom, 0.40, vert_exag=3.5)
    arr, ext = clipped(raster_path, geom)
    arr = arr.astype("float32")
    valid = np.isfinite(arr) & (arr > -9000)
    if not np.any(valid):
        print(f"Skipping empty: {title}")
        plt.close(fig)
        return
    if vmin is None:
        vmin = float(np.nanpercentile(arr[valid], 1))
    if vmax is None:
        vmax = float(np.nanpercentile(arr[valid], 99))
    if vmin >= vmax:
        vmax = vmin + 1.0

    cmap = plt.get_cmap(cmap_name)
    if log_scale:
        from matplotlib.colors import LogNorm
        arr_pos = np.where(arr <= 0, 1e-4, arr)
        norm = LogNorm(vmin=max(1e-4, vmin), vmax=vmax)
        im = ax.imshow(arr_pos, extent=ext, cmap=cmap, norm=norm, alpha=0.72, zorder=2, interpolation="bilinear")
    else:
        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
        im = ax.imshow(arr, extent=ext, cmap=cmap, norm=norm, alpha=0.72, zorder=2, interpolation="bilinear")
    clip_to_geom(im, ax, geom)

    # Top Hillshade Relief Blend (Preserves 3D topography and ridge illumination across every map)
    hillshade(ax, geom, alpha=0.35, vert_exag=4.5, zorder=4)
    finish(fig, ax, gdf_bound, gdf_sub, geom, out_path, "Legend",
           [line("Basin boundary", RED, 2)],
           extra=[cbar_el(vmin, vmax, cmap, label, unit)],
           source=source)

# ---------------------------------------------------------------- BATCH RUNNER
ALL_LAYERS = [
    {"id": "01", "name": "Digital Elevation Model", "type": "dem"},
    {"id": "02", "name": "Slope Distribution", "path": RASTERS_DIR / "slope.tif", "cmap": "magma", "label": "Slope", "unit": "deg"},
    {"id": "03", "name": "Aspect Map", "path": RASTERS_DIR / "aspect.tif", "cmap": "twilight", "label": "Aspect", "unit": "deg"},
    {"id": "04", "name": "Topographic Wetness Index", "path": RASTERS_DIR / "twi.tif", "cmap": "GnBu", "label": "TWI", "unit": ""},
    {"id": "05", "name": "Stream Power Index", "path": RASTERS_DIR / "spi.tif", "cmap": "magma", "label": "SPI", "unit": "log", "log": True},
    {"id": "06", "name": "Sediment Transport Index", "path": RASTERS_DIR / "sti.tif", "cmap": "YlOrRd", "label": "STI", "unit": "log", "log": True},
    {"id": "07", "name": "Topographic Ruggedness Index", "path": RASTERS_DIR / "tri.tif", "cmap": "magma", "label": "TRI", "unit": "m"},
    {"id": "08", "name": "Tectonic Lineament Density", "path": RASTERS_DIR / "lineament_proxy.tif", "cmap": "Reds", "label": "Density", "unit": "km/km²"},
    {"id": "09", "name": "Flow Direction", "path": DATA_DIR / "Flow Direction.tif", "cmap": "tab20", "label": "Flow Dir", "unit": "Code"},
    {"id": "10", "name": "Flow Accumulation", "path": DATA_DIR / "FlowAccumilation.tif", "cmap": "Blues", "label": "Flow Acc", "unit": "Cells", "log": True},
    {"id": "11", "name": "Curve Number CN Map", "path": RASTERS_DIR / "CN.tif", "cmap": "YlGn", "label": "Curve Number", "unit": "CN"},
    {"id": "12", "name": "Flash Flood Potential Index", "path": RASTERS_DIR / "FFPI.tif", "cmap": "OrRd", "label": "FFPI", "unit": "Index"},
    {"id": "13", "name": "Geomorphic Anomaly Index", "path": RASTERS_DIR / "GAI.tif", "cmap": "coolwarm", "label": "GAI", "unit": "Index"},
    {"id": "14", "name": "HI High Anomaly Areas", "path": RASTERS_DIR / "GAI_high_anomaly.tif", "cmap": "Reds", "label": "HI Anomaly", "unit": "Severity"},
    {"id": "15", "name": "Percolation Potential", "path": RASTERS_DIR / "percolation_potential.tif", "cmap": "Greens", "label": "Percolation", "unit": "Score"},
    {"id": "16", "name": "Contour Trench Suitability", "path": RASTERS_DIR / "contour_trench_suitability.tif", "cmap": "Purples", "label": "Trench Suitability", "unit": "Class"},
    {"id": "17", "name": "RUSLE Potential Soil Loss", "path": RASTERS_DIR / "RUSLE_A.tif", "cmap": "YlOrBr", "label": "Soil Loss", "unit": "t/ha/yr"},
    {"id": "18", "name": "RUSLE C-Factor Land Cover", "path": RASTERS_DIR / "RUSLE_C.tif", "cmap": "PiYG", "label": "C-Factor", "unit": ""},
    {"id": "19", "name": "RUSLE K-Factor Erodibility", "path": RASTERS_DIR / "RUSLE_K.tif", "cmap": "copper", "label": "K-Factor", "unit": "t·ha·h/ha·MJ·mm"},
    {"id": "20", "name": "RUSLE LS-Factor Topography", "path": RASTERS_DIR / "RUSLE_LS.tif", "cmap": "inferno", "label": "LS-Factor", "unit": ""},
    {"id": "21", "name": "RUSLE P-Factor Conservation", "path": RASTERS_DIR / "RUSLE_P.tif", "cmap": "summer", "label": "P-Factor", "unit": ""},
    {"id": "22", "name": "RUSLE R-Factor Rainfall", "path": RASTERS_DIR / "RUSLE_R.tif", "cmap": "YlGnBu", "label": "R-Factor", "unit": "MJ·mm/ha·h·yr"},
    {"id": "23", "name": "Stream Order Map", "type": "stream_order"},
    {"id": "24", "name": "Drainage Density Map", "path": RASTERS_DIR / "drainage_density_kde.tif", "cmap": "YlGnBu", "label": "Drainage Density", "unit": "km/km²", "vmin": 0.0, "vmax": 5.0},
    {"id": "25", "name": "Topographic Contour Map", "type": "contours"}
]

def main():
    gdf_bound = gpd.read_file(DATA_DIR / "pravra3.shp").dissolve()
    gdf_sub = gpd.read_file(DATA_DIR / "pravra3.shp")

    print(f"Loaded boundary. Total area = {gdf_bound.area.sum() / 1e6:.2f} km2")
    for layer in ALL_LAYERS:
        l_id = layer["id"]
        l_name = layer["name"].replace(" ", "_")
        out_file = OUTPUT_DIR / f"{l_id}_{l_name}.png"
        l_type = layer.get("type")
        if l_type == "dem":
            render_dem(gdf_bound, gdf_sub, out_file)
        elif l_type == "contours":
            render_contours(gdf_bound, gdf_sub, out_file)
        elif l_type == "stream_order":
            render_stream_orders(gdf_bound, gdf_sub, out_file)
        else:
            p = layer.get("path")
            if p and Path(p).exists():
                render_generic_raster(
                    gdf_bound, gdf_sub, p, out_file,
                    layer["name"], layer["label"], layer["cmap"],
                    unit=layer.get("unit", ""),
                    log_scale=layer.get("log", False)
                )
            else:
                print(f"Skipping missing raster: {layer['name']} ({p})")

if __name__ == "__main__":
    main()
