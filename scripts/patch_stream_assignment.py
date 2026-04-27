"""
Patch script: replaces the scrambled stream-order detection + assignment block
in pravra_pipeline_patched.py with clean, correctly-ordered code.
"""

path = (
    r"e:\Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main"
    r"\Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main"
    r"\scripts\pravra_pipeline_patched.py"
)

with open(path, "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

# ── Markers that bracket the broken block ───────────────────────────────────
AFTER  = "gdf_so = gdf_so.to_crs(UTM_EPSG)\n"
BEFORE = "# Pour points (optional but important for snapping)"

start_pos = content.find(AFTER)
end_pos   = content.find(BEFORE)

if start_pos == -1 or end_pos == -1:
    raise RuntimeError(f"Markers not found: start={start_pos}  end={end_pos}")

# ── Replacement block (ORDER_COL detection FIRST, then assignment loop) ─────
NEW_BLOCK = r"""gdf_so = gdf_so.to_crs(UTM_EPSG)

# ── Detect Strahler order column ─────────────────────────────────────────────
ORDER_COL_CANDIDATES = [
    'grid_code', 'GRIDCODE', 'Grid_Code', 'GRID_CODE',
    'strahler',  'Strahler',  'order',    'ORDER',
    'StreamOrde','str_order',
]
ORDER_COL = None
for _cand in ORDER_COL_CANDIDATES:
    if _cand in gdf_so.columns:
        ORDER_COL = _cand
        print(f"  Stream order column detected: '{ORDER_COL}'")
        break

if ORDER_COL is None:
    raise ValueError(
        f"Cannot detect stream order column. "
        f"Available: {gdf_so.columns.tolist()}"
    )

gdf_so[ORDER_COL] = gdf_so[ORDER_COL].astype(int)
MAX_ORDER          = int(gdf_so[ORDER_COL].max())
print(f"  Orders in global layer: {sorted(gdf_so[ORDER_COL].unique())}")

# ── Robust stream-to-subbasin assignment ─────────────────────────────────────
#
# gpd.clip() drops order-5 streams that lie on or near subbasin boundaries
# (they get clipped to zero-length stubs and vanish).
#
# Three-tier fix:
#   1. intersects check       — find every basin a stream touches
#   2. midpoint containment   — assign each boundary segment to the basin
#                               whose interior contains the segment midpoint
#   3. largest-overlap rule   — fallback when midpoint is exactly on the edge
#   4. 100 m buffer fallback  — catches streams just outside the polygon
#
print("\n  Assigning streams to subbasins (robust intersect + midpoint method)...")

_basin_geoms     = {r["basin_id"]: r.geometry for _, r in gdf_sub.iterrows()}
_basin_geoms_buf = {bid: geom.buffer(100) for bid, geom in _basin_geoms.items()}
_bid_list        = list(_basin_geoms.keys())

clipped_parts = []

for _, _seg in gdf_so[[ORDER_COL, "geometry"]].iterrows():
    _geom  = _seg.geometry
    _order = int(_seg[ORDER_COL])

    if _geom is None or _geom.is_empty:
        continue

    # Tier 1: intersects
    _cands = [b for b, bg in _basin_geoms.items() if _geom.intersects(bg)]

    # Tier 4: 100 m buffer fallback
    if not _cands:
        _cands = [b for b, bg in _basin_geoms_buf.items() if _geom.intersects(bg)]

    if not _cands:
        continue   # truly outside all basins

    if len(_cands) == 1:
        _assigned = _cands[0]
        try:
            _cgeom = _geom.intersection(_basin_geoms[_assigned])
        except Exception:
            _cgeom = _geom
    else:
        # Tier 2: midpoint containment
        try:
            _midpt = _geom.interpolate(0.5, normalized=True)
        except Exception:
            _midpt = _geom.centroid

        _assigned = None
        for _b in _cands:
            if _basin_geoms[_b].contains(_midpt):
                _assigned = _b
                break

        # Tier 3: largest overlap
        if _assigned is None:
            _best = -1.0
            for _b in _cands:
                try:
                    _ln = _geom.intersection(_basin_geoms[_b]).length
                except Exception:
                    _ln = 0.0
                if _ln > _best:
                    _best     = _ln
                    _assigned = _b

        try:
            _cgeom = _geom.intersection(_basin_geoms[_assigned])
        except Exception:
            _cgeom = _geom

    # Keep original geometry if intersection collapsed to a point
    if _cgeom is None or _cgeom.is_empty:
        _cgeom = _geom

    clipped_parts.append({ORDER_COL: _order,
                           "geometry": _cgeom,
                           "basin_id": _assigned})

if clipped_parts:
    gdf_so_sub = gpd.GeoDataFrame(clipped_parts, crs=gdf_so.crs)
    for _b in _bid_list:
        _ords = sorted(gdf_so_sub[gdf_so_sub["basin_id"] == _b][ORDER_COL].unique())
        print(f"  {_b}: Strahler orders present after assignment: {_ords}")
else:
    print("  WARNING: robust assignment yielded nothing -- falling back to sjoin")
    gdf_so_sub = gpd.sjoin(
        gdf_so[[ORDER_COL, "geometry"]],
        gdf_sub[["basin_id", "geometry"]],
        how="left", predicate="intersects",
    ).dropna(subset=["basin_id"])

"""

# ── Splice into file ─────────────────────────────────────────────────────────
# Remove everything between (and including) AFTER up to (not including) BEFORE
insert_at = start_pos                     # keep AFTER in NEW_BLOCK already
remove_to = end_pos

new_content = content[:insert_at] + NEW_BLOCK + content[remove_to:]

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Patch applied successfully.")
lines_before = content[:remove_to].count("\n")
lines_after  = content[:insert_at].count("\n")
print(f"  Replaced lines ~{lines_after+1} to ~{lines_before+1}")
print(f"  New total lines: {new_content.count(chr(10))+1}")
