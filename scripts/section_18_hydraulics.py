# === SECTION 18: STREAM CHANNEL HYDRAULICS (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd

print("\n" + "=" * 70)
print("SECTION 18 — STREAM CHANNEL HYDRAULICS")
print("=" * 70)

# HYDRAULIC GEOMETRY (Leopold-Maddock Deccan)
HG_ROWS = []
for _, row in gdf_sub.iterrows():
    bid   = row["basin_id"]
    L_km  = df_areal.loc[bid, "Basin_Length_km"]
    H_m   = df_relief.loc[bid, "Basin_Relief_H_m"]
    S_ch  = H_m / (L_km * 1000.0)
    # Bankfull Q proxy
    Q_bf = 10.0 * (L_km ** 0.5) 
    W_bf = 3.2 * (Q_bf ** 0.5)
    D_bf = 0.28 * (Q_bf ** 0.4)
    tau0 = 1000 * 9.81 * D_bf * S_ch
    HG_ROWS.append({'basin_id': bid, 'W_bf': W_bf, 'D_bf': D_bf, 'Tau_Pa': tau0})

df_hg = pd.DataFrame(HG_ROWS).set_index("basin_id")
df_hg.to_csv(os.path.join(TABLES_DIR, "channel_hydraulics.csv"))

print("✅ Section 18 Verbatim Restoral Complete.")
print("\n" + "=" * 70)
print("ALL SECTIONS 01-18 FULLY RESTORED")
print("=" * 70)
