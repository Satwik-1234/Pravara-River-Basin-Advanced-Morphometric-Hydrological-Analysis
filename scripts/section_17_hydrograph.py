# === SECTION 17: SYNTHETIC UNIT HYDROGRAPH (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd

print("\n" + "=" * 70)
print("SECTION 17 — SYNTHETIC UNIT HYDROGRAPH")
print("=" * 70)

# SNYDER'S PARAMETERS (Indian Deccan calibration)
Ct = 1.8; Cp = 0.6
SUH_ROWS = []
for _, row in gdf_sub.iterrows():
    bid   = row["basin_id"]
    A_km2 = df_areal.loc[bid, "Area_km2"]
    L_km  = df_areal.loc[bid, "Basin_Length_km"]
    Lca_km = 0.6 * L_km
    tL_hr  = Ct * (L_km * Lca_km) ** 0.3
    Qp_unit = 2.75 * Cp * A_km2 / tL_hr
    SUH_ROWS.append({'basin_id': bid, 'tp_hr': tL_hr, 'Qp_unit': Qp_unit})

df_suh = pd.DataFrame(SUH_ROWS).set_index("basin_id")
df_suh.to_csv(os.path.join(TABLES_DIR, "unit_hydrograph_params.csv"))

print("✅ Section 17 Verbatim Restoral Complete.")
