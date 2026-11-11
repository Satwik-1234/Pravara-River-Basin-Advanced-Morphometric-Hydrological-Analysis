# === SECTION 8: OUTPUT EXPORT SUITE (VERBATIM) ===
import os, sys
import pandas as pd
import geopandas as gpd

# 1. Master Csv Export
master_csv = os.path.join(TABLES_DIR, "morphometric_master_table.csv")
df_master.to_csv(master_csv)
print(f"📊 Global Table Exported: {master_csv}")

# 2. Priority Shapefile Export
priority_shp = os.path.join(SHAPES_DIR, "subbasins_priority.shp")
gdf_priority.to_file(priority_shp)
print(f"🗺️ Priority Shapefile Exported: {priority_shp}")

# 3. Stream Order Summary
all_order_data = []
for bid, df_lin in LINEAR_PER_ORDER.items():
    df_c = df_lin.copy(); df_c['basin_id'] = bid
    all_order_data.append(df_c)
if all_order_data:
    pd.concat(all_order_data).to_csv(os.path.join(TABLES_DIR, "stream_order_summary.csv"), index=False)

# 4. Inventory of Generated Products
print("\n--- OUTPUT INVENTORY ---")
for root, _, files in os.walk(OUT_DIR):
    for f in sorted(files):
        print(f" - {os.path.relpath(os.path.join(root, f), OUT_DIR)}")

print("✅ Section 08 Verbatim Restoral Complete.")
