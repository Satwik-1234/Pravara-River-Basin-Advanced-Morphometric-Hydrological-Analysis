import os

path = r"e:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/scripts/pravra_pipeline_patched.py"

with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

new_lines = []
found = False
for line in lines:
    if 'Map framework loaded' in line and not found:
        new_lines.append('\ndef base_axes(title, figsize=(16, 11)):\n')
        new_lines.append('    """Unified Frame shim: returns (fig, ax_map, utm_extent)."""\n')
        new_lines.append('    fig, ax_map, ax_panel = make_map_figure(title, figsize=figsize)\n')
        new_lines.append('    fig._panel_ax = ax_panel \n')
        new_lines.append('    add_esri_basemap(ax_map)\n')
        new_lines.append('    utm_ext = compute_utm_extent()\n')
        new_lines.append('    return fig, ax_map, utm_ext\n\n')
        new_lines.append('print("Map framework loaded — DESIGN-01 through DESIGN-07 active.")\n')
        found = True
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully injected base_axes shim.")
