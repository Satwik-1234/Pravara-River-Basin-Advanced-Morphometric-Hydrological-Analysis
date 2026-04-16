# === SECTION 6: WATERSHED PRIORITIZATION (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# --- PARAMETER DEFINITIONS ---
DIRECT_PARAMS = {'Drainage_Density_Dd':'Dd','Stream_Frequency_Fs':'Fs','Rbm':'Rb','Ruggedness_Rn':'Rn','Relief_Ratio_Rh':'Rh','Hypsometric_HI':'HI'}
INVERSE_PARAMS = {'Elongation_Ratio_Re':'Re','Circularity_Ratio_Rc':'Rc','Form_Factor_Ff':'Ff'}
ALL_PRIORITY_COLS = list(DIRECT_PARAMS.keys()) + list(INVERSE_PARAMS.keys())
df_pri = df_master[ALL_PRIORITY_COLS].copy().fillna(df_master[ALL_PRIORITY_COLS].median())

# --- METHOD 1: COMPOUND RANKING ---
df_rank = pd.DataFrame(index=df_pri.index)
for col in DIRECT_PARAMS: df_rank[col] = df_pri[col].rank(ascending=False, method='min')
for col in INVERSE_PARAMS: df_rank[col] = df_pri[col].rank(ascending=True, method='min')
df_rank['CF_M1'] = df_rank.mean(axis=1)
df_rank['Rank_M1'] = df_rank['CF_M1'].rank(ascending=True, method='min').astype(int)
t1 = np.percentile(df_rank['CF_M1'], [33, 66])
df_rank['Priority_M1'] = df_rank['CF_M1'].apply(lambda x: 'High' if x <= t1[0] else ('Moderate' if x <= t1[1] else 'Low'))

# --- METHOD 2: ENTROPY WEIGHT ---
def entropy_weight_score(df, d_cols, i_cols):
    df_n = pd.DataFrame(index=df.index)
    for c in d_cols: df_n[c] = (df[c]-df[c].min())/(df[c].max()-df[c].min()+1e-12)
    for c in i_cols: df_n[c] = 1 - (df[c]-df[c].min())/(df[c].max()-df[c].min()+1e-12)
    n, m = df_n.shape
    weights = []
    for c in df_n.columns:
        p = df_n[c]/(df_n[c].sum()+1e-12); p = p.clip(lower=1e-12)
        e = -np.sum(p*np.log(p))/np.log(n+1e-12); weights.append(1-e)
    weights = np.array(weights); weights /= (weights.sum()+1e-12)
    return (df_n.values * weights).sum(axis=1), dict(zip(df_n.columns, weights))

score_m2, ew_w = entropy_weight_score(df_pri, list(DIRECT_PARAMS.keys()), list(INVERSE_PARAMS.keys()))
df_rank['Score_M2'] = score_m2
df_rank['Rank_M2'] = pd.Series(score_m2, index=df_pri.index).rank(ascending=False, method='min').astype(int)
t2 = np.percentile(score_m2, [66, 33])
df_rank['Priority_M2'] = df_rank['Score_M2'].apply(lambda x: 'High' if x >= t2[0] else ('Moderate' if x >= t2[1] else 'Low'))

# --- AGREEMENT: KENDALL TAU ---
tau, p_val = stats.kendalltau(df_rank['Rank_M1'], df_rank['Rank_M2'])
print(f"✅ Prioritization Complete. Kendall Tau Agreement: {tau:.3f} (p={p_val:.4f})")
df_rank.to_csv(os.path.join(TABLES_DIR, "prioritization_ranking.csv"))
print("✅ Section 06 Verbatim Restoral Complete.")
