# -*- coding: utf-8 -*-
"""
=============================================================================
 SECTION 06 — WATERSHED PRIORITIZATION FRAMEWORK
 Pravara River Basin Morphometric Analysis
=============================================================================
 Purpose  : Compound value method; rank subbasins by treatment urgency; generate priority map.
 Source   : adv_v2_morphometry_pravra3basin.py :: SECTION 6
 Depends  : Sections 00–05 must be run first (variables must be in memory).
 Usage    :   %run scripts/section_06_prioritization.py
           OR exec(open("scripts/section_06_prioritization.py").read())
=============================================================================
"""

# ─── How to use this file ────────────────────────────────────────────────────
#
# This script is a standalone module for Section 06 of the pipeline.
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
# SECTION 06 CODE — copied from adv_v2_morphometry_pravra3basin.py :: SECTION 6
# ─────────────────────────────────────────────────────────────────────────────
#
# [PASTE THE SECTION 06 CODE BLOCK HERE]
#
# To extract the code:
#   1. Open adv_v2_morphometry_pravra3basin.py
#   2. Find the header: "SECTION 06 — WATERSHED PRIORITIZATION FRAMEWORK"
#   3. Copy everything until the next SECTION header
#   4. Paste it here, replacing this comment block
# ─────────────────────────────────────────────────────────────────────────────
