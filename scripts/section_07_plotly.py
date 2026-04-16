# === SECTION 7: PLOTLY INTERACTIVE VISUALIZATION (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from scipy import stats

HTML_DIR = os.path.join(PLOTS_DIR, "html/")
os.makedirs(HTML_DIR, exist_ok=True)

def save_plotly(fig, name):
    path = os.path.join(HTML_DIR, f"{name}.html")
    fig.write_html(path, include_plotlyjs=True)
    return path

# 01. Horton's Laws
print("🎨 Generating Horton's Law Interactive Plots...")
for bid, df_lin in LINEAR_PER_ORDER.items():
    if df_lin.empty or len(df_lin) < 2: continue
    fig = make_subplots(rows=1, cols=2, subplot_titles=[f"Stream Number Law - {bid}", f"Stream Length Law - {bid}"])
    fig.add_trace(go.Scatter(x=df_lin['order'], y=df_lin['Nu'], mode='markers+lines', name='Nu'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_lin['order'], y=df_lin['Lu']/1000, mode='markers+lines', name='Lu (km)'), row=1, col=2)
    fig.update_xaxes(type='log'); fig.update_yaxes(type='log')
    save_plotly(fig, f"01_hortons_law_{bid}")

# 02. Radar Charts
print("🎨 Generating Morphometric Radar Signatures...")
radar_cols = ['Drainage_Density_Dd', 'Stream_Frequency_Fs', 'Form_Factor_Ff', 'Elongation_Ratio_Re', 'Circularity_Ratio_Rc', 'Ruggedness_Rn']
df_radar = df_master[radar_cols].copy()
df_radar_n = (df_radar - df_radar.min()) / (df_radar.max() - df_radar.min() + 1e-12)
fig = go.Figure()
for bid, row in df_radar_n.iterrows():
    fig.add_trace(go.Scatterpolar(r=row.tolist()+[row.tolist()[0]], theta=radar_cols+[radar_cols[0]], fill='toself', name=bid))
save_plotly(fig, "02_radar_morphometric")

# 11. Priority Map (Interactive)
print("🎨 Rendering Interactive Priority Map...")
fig = go.Figure()
priority_colors = {'High': '#d73027', 'Moderate': '#fee090', 'Low': '#4575b4'}
for _, row in gdf_priority.iterrows():
    bid = row['basin_id']; pri = row.get('Priority_M1', 'Unknown')
    for g in ([row.geometry] if row.geometry.geom_type == 'Polygon' else list(row.geometry.geoms)):
        coords = np.array(g.exterior.coords)
        fig.add_trace(go.Scatter(x=coords[:,0], y=coords[:,1], fill='toself', fillcolor=priority_colors.get(pri, 'grey'), 
                                 line=dict(color='black'), name=f"{bid} ({pri})"))
fig.update_layout(template='plotly_white', title="Interactive Watershed Priority Map")
save_plotly(fig, "11_priority_map")

print("✅ Section 07 Verbatim Restoral Complete.")
