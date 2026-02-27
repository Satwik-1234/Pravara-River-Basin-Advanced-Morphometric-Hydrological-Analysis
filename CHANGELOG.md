# Changelog

All notable changes to this project are documented here.

---

## [v2.0.0] — 2024 (Current — adv_v2_morphometry_pravra3basin.py)

### Added
- **Sections 14–18** — Full hydrology & soil-water conservation module:
  - Section 14: SCS-CN runoff estimation with Gumbel EV-I rainfall frequency
  - Section 15: RUSLE soil erosion model (R·K·LS·C·P) with pixel-level rasters
  - Section 16: Watershed treatment planning (check dams, percolation ponds, contour trenches)
  - Section 17: Synthetic Unit Hydrograph (Snyder's method, Deccan calibration)
  - Section 18: Stream channel hydraulics (bankfull geometry, shear stress, stream power, stability)
- **Sections 10–13** — Tectonic & geomorphic indices:
  - Section 10: Tectonic activity indices (Bs, Af, Vf, Smf, HI)
  - Section 11: Geomorphic indices (SL, SPI, TWI rasters)
  - Section 12: Geomorphic anomaly & lineament analysis
  - Section 13: Flood hazard indicators
- Dynamic N_SUBBASINS auto-detection (no hard assertion crash)
- Smart basin ID extraction from attribute table
- Check dam suitability index (CDSI) with 5-factor weighting
- Water Harvesting Potential (WHP) per subbasin
- Sediment Delivery Ratio (SDR) and annual sediment yield

### Fixed
- **CRITICAL:** Broken stream path `/content/streams.shp` → `SteamOrder.shp`
- **CRITICAL:** `ChannelOverlandFlow_C` → `ChannelMaintenance_C` (correct column name)
- Zip filename updated: `Morphomtery_layers.zip` → `Morphomtery_layers-Final.zip`
- Pour points path updated: `Pourpoints-Pravrabasin.shp` → `Pourpoints_3.shp`
- DEM resolution check changed from hard assertion to soft warning
- ORDER_COL confirmed as `grid_code` (verified from SteamOrder.dbf)

### Changed
- N_SUBBASINS: Hardcoded `5` → auto-detected from shapefile
- N_SUBBASINS mismatch: Hard crash → graceful warning + auto-correction

---

## [v1.0.0] — 2024 (adv_v1_morphometry_pravarabasin.py)

### Features
- Sections 0–13 complete morphometric analysis pipeline
- 5-subbasin configuration (Pravrabasin.shp with 5 polygons)
- All linear, areal, and relief parameters
- Publication-grade matplotlib maps (Section 4)
- Statistical analysis with PCA and clustering (Section 5)
- Watershed prioritization compound value method (Section 6)
- Interactive Plotly charts (Section 7)
- Automated PDF/HTML report (Section 9)
- Tectonic activity indices (Section 10)
- Geomorphic indices — SL, SPI, TWI (Section 11)
- Geomorphic anomaly & lineaments (Section 12)
- Flood hazard indicators (Section 13)

---

## Planned (v3.0.0)

- [ ] True 3-polygon subbasin shapefile (`pravra3.shp`) integration
- [ ] SWAT model integration for calibrated rainfall-runoff
- [ ] IMD gridded rainfall data for spatially distributed R-factor
- [ ] Sentinel-2 NDVI-based LULC → C-factor refinement
- [ ] NBSS&LUP soil map → K-factor refinement
- [ ] Ground-truth validation of check dam suitability with field data
- [ ] Web dashboard (Streamlit) for interactive results exploration
- [ ] Batch processing for multiple basins in the Pravara catchment
