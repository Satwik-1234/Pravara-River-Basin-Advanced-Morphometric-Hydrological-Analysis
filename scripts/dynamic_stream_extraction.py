import numpy as np
if not hasattr(np, "in1d"):
    np.in1d = np.isin
import pandas as pd
import geopandas as gpd
import rasterio
import rasterio.features
from rasterio.mask import mask as rio_mask
from rasterio.transform import from_bounds
import matplotlib.pyplot as plt
import networkx as nx
from pysheds.grid import Grid
from shapely.geometry import LineString, mapping, Point
from scipy import stats
import warnings
import os
import sys

warnings.filterwarnings("ignore")

CONFIG = {
    # ── Input files ──────────────────────────────────────────────────────────
    "dem_path":       r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/Filled DEM.tif",
    "basin_shp":      r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/pravra3.shp",
    "basin_id_col":   "name",

    # ── Stream Extraction ─────────────────────────────────────────────────────
    "acc_threshold":  200,               # Global threshold to increase density

    # ── Output ────────────────────────────────────────────────────────────────
    "output_csv":     "stream_order_summary_fixed.csv",
    "output_dir":     r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/outputs/tables",
    "output_shp":     r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/SteamOrder_Fixed.shp",
}

os.makedirs(CONFIG["output_dir"], exist_ok=True)

def assign_strahler_order(stream_network_gdf):
    print("[Assigning Strahler] Building topological graph...")
    G = nx.DiGraph()
    # Use rounded coordinates to ensure connectivity
    def rnd(coords): return tuple(np.round(coords, 3))

    for idx, row in stream_network_gdf.iterrows():
        coords = list(row.geometry.coords)
        for i in range(len(coords) - 1):
            G.add_edge(rnd(coords[i]), rnd(coords[i + 1]))

    print("[Assigning Strahler] Computing orders...")
    order_map = {}
    for node in nx.topological_sort(G):
        preds = list(G.predecessors(node))
        if not preds:
            order_map[node] = 1
        else:
            pred_orders = [order_map.get(p, 1) for p in preds]
            max_order   = max(pred_orders)
            count_max   = pred_orders.count(max_order)
            order_map[node] = max_order + 1 if count_max >= 2 else max_order

    segment_orders = []
    for idx, row in stream_network_gdf.iterrows():
        coords     = list(row.geometry.coords)
        # Use midpoint or endpoint to determine segment order
        mid_node   = rnd(coords[len(coords) // 2])
        seg_order  = order_map.get(mid_node, 1)
        segment_orders.append(seg_order)

    stream_network_gdf = stream_network_gdf.copy()
    stream_network_gdf["strahler_order"] = segment_orders
    return stream_network_gdf

def run_pipeline():
    print("\n" + "="*70)
    print("  GLOBAL TOPOLOGY STREAM EXTRACTION PIPELINE")
    print("  Fixing SB3 boundary anomaly and threshold rills")
    print("="*70)

    # 1. Load data
    grid = Grid.from_raster(CONFIG["dem_path"])
    dem  = grid.read_raster(CONFIG["dem_path"])
    basins_gdf = gpd.read_file(CONFIG["basin_shp"])
    basins_gdf = basins_gdf.to_crs(epsg=32643)

    # 2. Condition DEM
    print("\n[STEP 1] Conditioning Full DEM...")
    pit_filled = grid.fill_pits(dem)
    flooded    = grid.fill_depressions(pit_filled)
    inflated   = grid.resolve_flats(flooded)

    # 3. Flow Direction & Accumulation
    print("[STEP 2] Computing Flow Direction & Accumulation...")
    fdir = grid.flowdir(inflated)
    acc  = grid.accumulation(fdir)

    # 4. Global Stream Extraction
    thresh = CONFIG["acc_threshold"]
    print(f"[STEP 3] Extracting Global Network (Threshold={thresh})...")
    streams = acc > thresh
    stream_network = grid.extract_river_network(fdir, streams)
    
    global_stream_gdf = gpd.GeoDataFrame(
        stream_network["features"],
        geometry=[LineString(f["geometry"]["coordinates"]) for f in stream_network["features"]],
        crs=basins_gdf.crs
    )

    # 5. Global Strahler Ordering
    print("[STEP 4] Performing Global Strahler Ordering...")
    global_stream_gdf = assign_strahler_order(global_stream_gdf)

    # 6. Clip and Analyze per Basin
    print("\n[STEP 5] Clipping and Analyzing per Basin...")
    all_results = []
    all_clipped_streams = []

    for _, basin_row in basins_gdf.iterrows():
        bid = str(basin_row[CONFIG["basin_id_col"]]).replace("Subbasin-", "SB")
        print(f"  Processing {bid}...")
        
        basin_geom = basin_row.geometry
        # Clip streams to basin
        clipped = global_stream_gdf[global_stream_gdf.intersects(basin_geom)].copy()
        
        # Clip geometries to exact basin boundary
        clipped.geometry = clipped.geometry.intersection(basin_geom)
        # Remove empty or non-line geometries (e.g. points at boundary)
        clipped = clipped[clipped.geometry.type.isin(['LineString', 'MultiLineString'])]
        clipped = clipped[~clipped.geometry.is_empty]

        if len(clipped) == 0:
            print(f"    [!] No streams found in {bid}")
            continue

        # Count streams (Nu) correctly by dissolving contiguous segments of same order
        orders = sorted(clipped["strahler_order"].unique())
        Nu_by_order = {}
        
        for o in orders:
            segs = clipped[clipped["strahler_order"] == o]
            # Dissolve contiguous segments
            try:
                # Use a larger buffer (50m) for higher orders to bridge fragmentation
                buf = 50.0 if o >= 4 else 5.0
                dissolved = segs.copy()
                dissolved.geometry = dissolved.geometry.buffer(buf)
                dissolved = dissolved.dissolve()
                exploded = dissolved.explode(index_parts=False)
                Nu_by_order[o] = len(exploded)
            except:
                Nu_by_order[o] = len(segs)

        # Compute Rb
        rb_vals = []
        for o in orders[:-1]:
            n = Nu_by_order.get(o, 0)
            n1 = Nu_by_order.get(o+1, 0)
            if n1 > 0:
                rb_vals.append(n / n1)
        
        rbm = np.mean(rb_vals) if rb_vals else np.nan
        
        print(f"    -> Max Order: {max(orders)} | Rbm: {rbm:.4f} | Counts: {Nu_by_order}")
        
        res = {"basin_id": bid, "max_order": max(orders), "Rbm": round(rbm, 4)}
        for o in range(1, max(orders)+1):
            res[f"Nu_order{o}"] = Nu_by_order.get(o, 0)
        all_results.append(res)
        
        clipped["basin_id"] = bid
        all_clipped_streams.append(clipped)

    # 7. Save Outputs
    df = pd.DataFrame(all_results)
    out_csv = os.path.join(CONFIG["output_dir"], CONFIG["output_csv"])
    df.to_csv(out_csv, index=False)
    
    final_gdf = pd.concat(all_clipped_streams, ignore_index=True)
    final_gdf = final_gdf.rename(columns={"strahler_order": "GRID_CODE"})
    final_gdf.to_file(CONFIG["output_shp"])

    print("\n" + "="*70)
    print(f"[OK] SUCCESS! Results saved to {out_csv}")
    print(f"[OK] Vector Streams saved to {CONFIG['output_shp']}")
    print("="*70 + "\n")

if __name__ == "__main__":
    run_pipeline()
