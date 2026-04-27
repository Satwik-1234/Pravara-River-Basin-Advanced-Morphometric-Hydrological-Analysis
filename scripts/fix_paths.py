path = r'e:\Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main\Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main\scripts\pravra_pipeline_patched.py'

with open(path, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

BASE = "E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data"

for i, line in enumerate(lines):
    # Fix line 197 (0-indexed 196): broken comma after comment
    if '"stream_order_shp"' in line and 'SteamOrder' in line:
        lines[i] = f'    "stream_order_shp" : r"{BASE}/SteamOrder.shp",\n'
        print(f'  Fixed line {i+1}: stream_order_shp -> SteamOrder.shp')
    # Ensure streams also points to SteamOrder.shp (not _Fixed)
    if '"streams"' in line and 'SteamOrder_Fixed' in line:
        lines[i] = f'    "streams"          : r"{BASE}/SteamOrder.shp",\n'
        print(f'  Fixed line {i+1}: streams -> SteamOrder.shp')

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done.')
