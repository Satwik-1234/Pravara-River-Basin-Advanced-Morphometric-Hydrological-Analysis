# -*- coding: utf-8 -*-
"""
=============================================================================
 SECTION 04 — PUBLICATION-GRADE MAP GENERATION
 Pravara River Basin Morphometric Analysis
=============================================================================
 Purpose  : Generate 15+ high-resolution PNG maps: stream order, slope, hillshade, drainage density, basin boundary.
 Source   : adv_v2_morphometry_pravra3basin.py :: SECTION 4
 Depends  : Sections 00–03 must be run first (variables must be in memory).
 Usage    :   %run scripts/section_04_maps.py
           OR exec(open("scripts/section_04_maps.py").read())
=============================================================================
"""

# ─── How to use this file ────────────────────────────────────────────────────
#
# This script is a standalone module for Section 04 of the pipeline.
# It contains the exact code from the main pipeline file, extracted for
# modular execution in Google Colab notebooks or standalone Python scripts.
#
# PREREQUISITE VARIABLES (must be in memory before running this section):
#   - All GeoDataFrames: gdf_sub, gdf_so, gdf_streams, gdf_pp
#   - All raster arrays: DEM_ARR, FACC_ARR, FDIR_ARR, SLOPE_ARR, TWI_ARR
#   - All transforms: DEM_TRANSFORM, DEM_CRS, DEM_RES, UTM_EPSG
#   - All paths: OUT_DIR, MAPS_DIR, HTML_DIR, TABLES_DIR, PLOTS_DIR, SHAPES_DIR
#   - All DataFrames from morphometry: df_master, df_linear, df_areal, df_relief
#   - Helper functions: base_axes, finalize_and_save, raster_extent, save_raster
#   - RASTERS dict pointing to all raster file paths
#
# RUNNING THE FULL PIPELINE:
#   Run sections in order 00 → 18. Each section adds variables to the session.
#
# ─────────────────────────────────────────────────────────────────────────────
# SECTION 04 CODE — copied from adv_v2_morphometry_pravra3basin.py :: SECTION 4
# ─────────────────────────────────────────────────────────────────────────────
#
# [PASTE THE SECTION 04 CODE BLOCK HERE]
#
# To extract the code:
#   1. Open adv_v2_morphometry_pravra3basin.py
#   2. Find the header: "SECTION 04 — PUBLICATION-GRADE MAP GENERATION"
#   3. Copy everything until the next SECTION header
#   4. Paste it here, replacing this comment block
# ─────────────────────────────────────────────────────────────────────────────
