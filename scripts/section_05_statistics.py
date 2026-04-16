# === SECTION 5: MULTIVARIATE STATISTICAL ANALYSIS ===
import os, sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

# --- PARAMETER SELECTION ---
STAT_COLS = [
    'Area_km2', 'Drainage_Density_Dd', 'Stream_Frequency_Fs', 'Texture_Ratio_T',
    'Form_Factor_Ff', 'Elongation_Ratio_Re', 'Circularity_Ratio_Rc',
    'Basin_Relief_H_m', 'Hypsometric_HI', 'Rbm'
]
STAT_COLS = [c for c in STAT_COLS if c in df_master.columns]
df_stat = df_master[STAT_COLS].copy().astype(float).dropna(axis=1, how='all')

# --- DESCRIPTIVE STATS ---
print("📊 Computing Verbatim Descriptive Stats...")
desc = df_stat.describe()
desc.loc['cv_pct'] = (df_stat.std()/df_stat.mean()*100)
desc.loc['skewness'] = df_stat.apply(lambda x: stats.skew(x.dropna()))
desc.to_csv(os.path.join(TABLES_DIR, "descriptive_statistics.csv"))

# --- CORRELATIONS ---
print("📈 Generating Verbatim Correlation Heatmaps...")
corr_p = df_stat.corr(method='pearson')
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(corr_p, annot=True, cmap='RdYlBu_r', center=0, fmt='.2f', ax=ax)
fig.savefig(os.path.join(PLOTS_DIR, "correlation_heatmap.png"), dpi=180)
plt.close(fig)

# --- VIF ANALYSIS ---
print("📉 Executing VIF Collinearity Audit...")
if len(df_stat) > len(df_stat.columns):
    X = sm.add_constant(df_stat.fillna(df_stat.median()))
    vif = pd.DataFrame({'Feature': df_stat.columns, 'VIF': [variance_inflation_factor(X.values, i+1) for i in range(len(df_stat.columns))]})
    vif.to_csv(os.path.join(TABLES_DIR, "vif.csv"), index=False)

# --- PCA DECOMPOSITION ---
print("🧬 Running Principal Component Analysis...")
scaler = StandardScaler()
X_sc = scaler.fit_transform(df_stat.fillna(df_stat.median()))
pca = PCA(); scores = pca.fit_transform(X_sc)
exp_var = pca.explained_variance_ratio_ * 100
cum_var = np.cumsum(exp_var)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.bar(range(1, len(exp_var)+1), exp_var, label='Individual')
ax1.plot(range(1, len(exp_var)+1), cum_var, 'ro-', label='Cumulative')
ax1.set_title("Scree Plot"); ax1.legend()

# Biplot snippet
ax2.scatter(scores[:,0], scores[:,1], c='darkorange', s=100); ax2.set_title("PCA Biplot")
fig.savefig(os.path.join(PLOTS_DIR, "pca_scree_biplot.png"), dpi=180)
plt.close(fig)

pd.DataFrame(pca.components_.T, index=df_stat.columns, columns=[f"PC{i+1}" for i in range(len(exp_var))]).to_csv(os.path.join(TABLES_DIR, "pca_loadings.csv"))
print("✅ Section 05 Verbatim Restoral Complete.")
