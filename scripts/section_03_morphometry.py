# -*- coding: utf-8 -*-
"""
=============================================================================
 SECTION 03 — MORPHOMETRIC PARAMETER CALCULATION
 Pravara River Basin Morphometric Analysis
=============================================================================
 Purpose  : Compute 60+ parameters: Linear (Nu, Rb, RL, Lsm), Areal (Dd, Fs, Re, Rc, Ff), Relief (H, Rh, Rn, HI).
 Source   : adv_v2_morphometry_pravra3basin.py :: SECTION 3
 Depends  : Sections 00–02 must be run first (variables must be in memory).
 Usage    :   %run scripts/section_03_morphometry.py
           OR exec(open("scripts/section_03_morphometry.py").read())
=============================================================================
"""

# ─── How to use this file ────────────────────────────────────────────────────
#
# This script is a standalone module for Section 03 of the pipeline.
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
# SECTION 03 CODE — copied from adv_v2_morphometry_pravra3basin.py :: SECTION 3
# ─────────────────────────────────────────────────────────────────────────────
#
# [PASTE THE SECTION 03 CODE BLOCK HERE]
#
# To extract the code:
#   1. Open adv_v2_morphometry_pravra3basin.py
#   2. Find the header: "SECTION 03 — MORPHOMETRIC PARAMETER CALCULATION"
#   3. Copy everything until the next SECTION header
#   4. Paste it here, replacing this comment block
# ─────────────────────────────────────────────────────────────────────────────
