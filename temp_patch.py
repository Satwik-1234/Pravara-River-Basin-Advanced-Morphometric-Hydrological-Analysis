import re

with open('E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/scripts/pravra_pipeline_patched.py', 'r', encoding='utf-8') as f:
    text = f.read()

rep3_before = '''    if 'name' in gdf_sub.columns and gdf_sub['name'].notna().all():
        # Extract subbasin name from the 'AreaSqkm' column which has "Subbasin-X"
        # Try AreaSqkm field first (Pravrabasin.shp stores subbasin names there)
        if 'AreaSqkm' in gdf_sub.columns:
            names = gdf_sub['AreaSqkm'].astype(str).str.extract(r'(Subbasin-\d+)')[0]
            if names.notna().sum() == len(gdf_sub):
                gdf_sub['basin_id'] = names
            else:
                gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]
        else:
            gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]
    else:
        gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]'''

rep3_after = '''    if 'name' in gdf_sub.columns and gdf_sub['name'].notna().all():
        gdf_sub['basin_id'] = gdf_sub['name'].astype(str).str.replace("Subbasin-", "SB", regex=False)
    else:
        gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]'''

text = text.replace(rep3_before, rep3_after)

rep4_before = '''    for u in orders:
        segs = gdf_streams_clipped[gdf_streams_clipped[order_col] == u]
        nu   = len(segs)
        lu   = segs.geometry.length.sum()'''

rep4_after = '''    for u in orders:
        segs = gdf_streams_clipped[gdf_streams_clipped[order_col] == u]
        if len(segs) > 0:
            dissolved = segs.dissolve()
            exploded = dissolved.explode(index_parts=False)
            nu = len(exploded)
        else:
            nu = 0
        lu   = segs.geometry.length.sum()'''

text = text.replace(rep4_before, rep4_after)

with open('E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/scripts/pravra_pipeline_patched.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Patched successfully part 2!')
