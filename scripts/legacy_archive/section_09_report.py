# === SECTION 9: SCIENTIFIC REPORT GENERATION (VERBATIM) ===
import os, sys
import numpy as np
import pandas as pd

def format_val(val, decimals=3):
    try: return f"{float(val):.{decimals}f}"
    except: return "N/A"

def build_report():
    basin_ids = gdf_sub['basin_id'].tolist()
    bounds = gdf_sub.to_crs("EPSG:4326").total_bounds
    total_area = df_master['Area_km2'].sum()
    elev_min = df_master['Elev_Min_m'].min()
    elev_max = df_master['Elev_Max_m'].max()
    
    lines = []
    lines.append("="*80)
    lines.append("MORPHOMETRIC ANALYSIS OF PRAVARA RIVER BASIN")
    lines.append("Institutional Analytical Report - Verbatim Extraction")
    lines.append("="*80)
    
    lines.append(f"\n1. STUDY AREA: {len(basin_ids)} Subbasins. Total Area: {total_area:.2f} km2.")
    lines.append(f"Elevation Range: {elev_min:.0f}m to {elev_max:.0f}m.")
    
    lines.append("\n2. MORPHOMETRIC RESULTS SUMMARY")
    for bid in basin_ids:
        if bid in df_master.index:
            row = df_master.loc[bid]
            lines.append(f"  {bid}: Area={format_val(row.get('Area_km2'))}, Dd={format_val(row.get('Drainage_Density_Dd'))}, Re={format_val(row.get('Elongation_Ratio_Re'))}")

    lines.append("\n3. WATERSHED PRIORITIZATION (M1)")
    high_pri = df_rank[df_rank['Priority_M1'] == 'High'].index.tolist()
    lines.append(f"  HIGH Priority: {', '.join(high_pri)}")
    
    lines.append("\n4. CONCLUSION")
    lines.append("This analysis follows Horton (1945), Strahler (1952), and Schumm (1956) methodologies.")
    return "\n".join(lines)

report_text = build_report()
with open(os.path.join(REPORT_DIR, "morphometric_analysis_report.txt"), 'w', encoding='utf-8') as f:
    f.write(report_text)
print("✅ Section 09 Verbatim Restoral Complete.")
