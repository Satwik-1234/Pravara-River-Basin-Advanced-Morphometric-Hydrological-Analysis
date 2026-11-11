# === SECTION 10: TECTONIC ACTIVITY INDICES (IAT) ===
import os, sys
import numpy as np
import pandas as pd
import geopandas as gpd

# --- IAT ENGINE ---
df_IAT = df_master[['Area_km2', 'Perimeter_km', 'Basin_Length_km', 'Drainage_Density_Dd', 'Relief_Ratio_Rh', 'Slope_Mean_deg']].copy()

# A. Mountain Front Sinuosity (Smf proxy)
df_IAT['Smf'] = df_IAT['Perimeter_km'] / df_IAT['Basin_Length_km']

# B. Asymmetry Factor (AF proxy from Relief)
df_IAT['AF'] = df_IAT['Relief_Ratio_Rh']

# C. Transverse Topographic Symmetry (T proxy from Dd)
df_IAT['T'] = df_IAT['Drainage_Density_Dd']

# D. Valley Floor Width-to-Height (Vf proxy from Slope)
df_IAT['Vf'] = df_IAT['Slope_Mean_deg']

# --- CLASSIFICATION (El Hamdouni et al., 2008) ---
def classify_iat(iat_score):
    if iat_score <= 1.5: return 'Class 1 - Very High'
    if iat_score <= 2.5: return 'Class 2 - High'
    if iat_score <= 3.5: return 'Class 3 - Moderate'
    return 'Class 4 - Low'

df_IAT['Class_Smf'] = df_IAT['Smf'].apply(lambda x: 1 if x<1.6 else (2 if x<3.0 else (3 if x<5.0 else 4)))
df_IAT['Class_AF']  = df_IAT['AF'].apply(lambda x: 1 if x>0.10 else (2 if x>0.05 else (3 if x>0.02 else 4)))
df_IAT['Class_T']   = df_IAT['T'].apply(lambda x: 1 if x>3.0 else (2 if x>2.0 else (3 if x>1.0 else 4)))
df_IAT['Class_Vf']  = df_IAT['Vf'].apply(lambda x: 1 if x>15 else (2 if x>8 else (3 if x>3 else 4)))

df_IAT['IAT'] = df_IAT[['Class_Smf', 'Class_AF', 'Class_T', 'Class_Vf']].mean(axis=1)
df_IAT['IAT_class'] = df_IAT['IAT'].apply(classify_iat)

df_IAT.to_csv(os.path.join(TABLES_DIR, "tectonic_activity_indices.csv"))
print("✅ Section 10 Verbatim Restoral Complete.")
