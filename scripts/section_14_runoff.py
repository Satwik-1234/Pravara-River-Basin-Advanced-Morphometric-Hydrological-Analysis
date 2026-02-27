# -*- coding: utf-8 -*-
"""
=============================================================================
 SECTION 14 — RUNOFF ESTIMATION: SCS-CN
 Pravara River Basin Morphometric Analysis
=============================================================================
 Purpose  : Gumbel EV-I rainfall frequency, CN raster, direct runoff Q, volume, Tc, peak discharge Qp (Rational Method).
 Source   : sections_14_18_hydrology_swc.py :: SECTION 14
 Depends  : Sections 00–13 must be run first (variables must be in memory).
 Usage    :   %run scripts/section_14_runoff.py
           OR exec(open("scripts/section_14_runoff.py").read())
=============================================================================
"""

# ─── How to use this file ────────────────────────────────────────────────────
#
# This script is a standalone module for Section 14 of the pipeline.
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
# SECTION 14 CODE — copied from sections_14_18_hydrology_swc.py :: SECTION 14
# ─────────────────────────────────────────────────────────────────────────────
#
# [PASTE THE SECTION 14 CODE BLOCK HERE]
#
# To extract the code:
#   1. Open sections_14_18_hydrology_swc.py
#   2. Find the header: "SECTION 14 — RUNOFF ESTIMATION: SCS-CN"
#   3. Copy everything until the next SECTION header
#   4. Paste it here, replacing this comment block
# ─────────────────────────────────────────────────────────────────────────────
