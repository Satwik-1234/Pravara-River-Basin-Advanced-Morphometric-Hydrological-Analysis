# === SECTION 2: DATA PATHS & PREPROCESSING ===
import os, sys
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.mask import mask as rio_mask
from rasterio.features import geometry_mask
from shapely.geometry import Point, mapping
from pyproj import CRS
from matplotlib.colors import LightSource

# --- OUTPUT DIRECTORIES ---
OUT_DIR      = "E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/outputs/"
MAPS_DIR     = os.path.join(OUT_DIR, "maps/")
PLOTS_DIR    = os.path.join(OUT_DIR, "plots/")
TABLES_DIR   = os.path.join(OUT_DIR, "tables/")
SHAPES_DIR   = os.path.join(OUT_DIR, "shapefiles/")
REPORT_DIR   = os.path.join(OUT_DIR, "report/")

for d in [OUT_DIR, MAPS_DIR, PLOTS_DIR, TABLES_DIR, SHAPES_DIR, REPORT_DIR]:
    os.makedirs(d, exist_ok=True)

# --- DATA PATHS ---
DATA_PATHS = {
    "dem"              : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/Filled DEM.tif",
    "subbasins"        : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/pravra3.shp",
    "streams"          : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/SteamOrder.shp",
    "stream_order_shp" : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/SteamOrder.shp",
    "flow_dir"         : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/Flow Direction.tif",
    "flow_acc"         : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/FlowAccumilation.tif",
    "pour_points"      : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/Pourpoints_3.shp",
}

RASTERS = {'dem': DATA_PATHS['dem'], 'flow_dir': DATA_PATHS['flow_dir'], 'flow_acc': DATA_PATHS['flow_acc']}

def detect_utm_epsg(lon, lat):
    zone = int((lon + 180) / 6) + 1
    return f"EPSG:326{zone:02d}" if lat >= 0 else f"EPSG:327{zone:02d}"

def get_raster_info(path):
    with rasterio.open(path) as src:
        return {"crs": src.crs, "res": src.res, "nodata": src.nodata, "bounds": src.bounds, "transform": src.transform, "shape": src.shape}

def reproject_raster(src_path, dst_path, target_crs):
    with rasterio.open(src_path) as src:
        transform, width, height = calculate_default_transform(src.crs, target_crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({'crs': target_crs, 'transform': transform, 'width': width, 'height': height})
        with rasterio.open(dst_path, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(source=rasterio.band(src, i), destination=rasterio.band(dst, i),
                          src_transform=src.transform, src_crs=src.crs,
                          dst_transform=transform, dst_crs=target_crs, resampling=Resampling.bilinear)
    return dst_path

def fix_geometries(gdf, layer_name="layer"):
    gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.notna()].copy()
    gdf['geometry'] = gdf['geometry'].apply(lambda g: g.buffer(0) if not g.is_valid else g)
    return gdf[gdf.geometry.is_valid].reset_index(drop=True)

def snap_pour_points(pour_pts_gdf, flow_acc_path, snap_distance_m=300):
    with rasterio.open(flow_acc_path) as src:
        fa_data = src.read(1).astype(float); transform = src.transform; res = src.res[0]
        fa_data[fa_data == (src.nodata or -9999)] = np.nan
    snap_cells = int(snap_distance_m / res); snapped_pts = []
    for idx, row in pour_pts_gdf.iterrows():
        px_c, px_r = ~transform * (row.geometry.x, row.geometry.y)
        px_c, px_r = int(px_c), int(px_r)
        r0, r1 = max(0, px_r-snap_cells), min(fa_data.shape[0], px_r+snap_cells+1)
        c0, c1 = max(0, px_c-snap_cells), min(fa_data.shape[1], px_c+snap_cells+1)
        window = fa_data[r0:r1, c0:c1]
        if np.all(np.isnan(window)): snapped_pts.append(row.geometry); continue
        local_max = np.nanargmax(window); lr, lc = np.unravel_index(local_max, window.shape)
        sx, sy = rasterio.transform.xy(transform, r0+lr, c0+lc)
        snapped_pts.append(Point(sx, sy))
    result = pour_pts_gdf.copy(); result['geometry'] = snapped_pts
    return result

# --- INITIALIZATION ---
dem_info = get_raster_info(DATA_PATHS['dem'])
UTM_EPSG = str(dem_info['crs']) if not CRS.from_user_input(dem_info['crs']).is_geographic else detect_utm_epsg((dem_info['bounds'].left+dem_info['bounds'].right)/2, (dem_info['bounds'].bottom+dem_info['bounds'].top)/2)

gdf_sub = fix_geometries(gpd.read_file(DATA_PATHS['subbasins']).to_crs(UTM_EPSG), "subbasins")
gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]
gdf_streams = fix_geometries(gpd.read_file(DATA_PATHS['streams']).to_crs(UTM_EPSG), "streams")
gdf_so = fix_geometries(gpd.read_file(DATA_PATHS['stream_order_shp']).to_crs(UTM_EPSG), "stream_order")
ORDER_COL = next((c for c in ['grid_code', 'GRIDCODE', 'StreamOrde'] if c in gdf_so.columns), 'grid_code')

with rasterio.open(RASTERS['dem']) as src:
    DEM_ARR = src.read(1).astype(np.float32); DEM_TRANSFORM = src.transform; DEM_CRS = src.crs; DEM_RES = src.res[0]
    DEM_ARR[DEM_ARR == (src.nodata or -9999)] = np.nan
    DEM_BOUNDS = src.bounds

ls = LightSource(azdeg=315, altdeg=45)
HILLSHADE = ls.hillshade(np.where(np.isnan(DEM_ARR), np.nanmean(DEM_ARR), DEM_ARR), vert_exag=1.5, dx=DEM_RES, dy=DEM_RES)
print("✅ Section 02 Verbatim Restoral Complete.")
