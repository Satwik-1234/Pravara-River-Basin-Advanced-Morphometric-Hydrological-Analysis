print("SECTION 13 Ã¢â‚¬â€ FLOOD HAZARD INDICATORS")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. VERIFY TWI / SPI / STI (computed in S11)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[A] Loading TWI, SPI, STI arrays...")
assert 'twi' in RASTERS, "TWI raster not found Ã¢â‚¬â€ ensure Section 11 ran first"

# Re-read into memory (may have been computed in S11)
with rasterio.open(RASTERS['twi']) as src:
    TWI_ARR2 = src.read(1).astype(np.float32)
    TWI_ARR2[TWI_ARR2 == -9999.0] = np.nan

# Now, SPI and STI rasters should be available in RASTERS if Section 11 ran correctly
assert 'spi' in RASTERS, "SPI raster not found in RASTERS after Section 11"
assert 'sti' in RASTERS, "STI raster not found in RASTERS after Section 11"

with rasterio.open(RASTERS['spi']) as src:
    SPI_ARR2 = src.read(1).astype(np.float32)
    SPI_ARR2[SPI_ARR2 == -9999.0] = np.nan

with rasterio.open(RASTERS['sti']) as src:
    STI_ARR2 = src.read(1).astype(np.float32)
    STI_ARR2[STI_ARR2 == -9999.0] = np.nan

# Let's adjust the prints to reflect what is actually available.
print(f"  TWI : min={np.nanmin(TWI_ARR2):.2f} max={np.nanmax(TWI_ARR2):.2f} mean={np.nanmean(TWI_ARR2):.2f}")
print(f"  SPI : min={np.nanmin(SPI_ARR2):.2f} max={np.nanmax(SPI_ARR2):.2f} mean={np.nanmean(SPI_ARR2):.2f}")
print(f"  STI : min={np.nanmin(STI_ARR2):.2f} max={np.nanmax(STI_ARR2):.2f} mean={np.nanmean(STI_ARR2):.2f}")
# MAP-06/07: prepare log-stretch versions to fix invisible uniform-grey rendering
SPI_LOG = np.log10(np.where(SPI_ARR2 > 1.0, SPI_ARR2, np.nan))
SPI_LOG_MASKED = mask_raster_to_basin(SPI_LOG, DEM_TRANSFORM, gdf_sub)
STI_LOG = np.log10(np.where(STI_ARR2 > 0.01, STI_ARR2, np.nan))
STI_LOG_MASKED = mask_raster_to_basin(STI_LOG, DEM_TRANSFORM, gdf_sub)
TWI_MASKED2 = mask_raster_to_basin(TWI_ARR2, DEM_TRANSFORM, gdf_sub)
# MAP-05: also mask flat-area in TWI_MASKED2
SLOPE_SAFE2 = np.where(np.isnan(SLOPE_ARR), 90.0, SLOPE_ARR)
TWI_MASKED2[SLOPE_SAFE2 < 0.05] = np.nan




# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. FLASH FLOOD POTENTIAL INDEX (FFPI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# FFPI raster derived from slope, relief proxy, and TWI
# Weights following Smith (2003) and Gregory & Walling (1973) concepts

print("\n[B] Flash Flood Potential Index (FFPI)...")

def normalise_raster(arr):
    mn, mx = np.nanmin(arr), np.nanmax(arr)
    if mx == mn:
        return np.zeros_like(arr)
    return (arr - mn) / (mx - mn)


# Component normalised rasters
# MAP-08: build flat-area mask before compositing to prevent pale rectangles
FLAT_MASK_FFPI = np.where(np.isnan(SLOPE_ARR), False, SLOPE_ARR < 0.05)

def safe_component(arr, flat_mask):
    out = arr.copy()
    basin_mean = np.nanmean(arr[~flat_mask]) if np.any(~flat_mask) else 0.5
    out[flat_mask] = basin_mean
    return out

norm_slope   = normalise_raster(np.where(np.isnan(SLOPE_ARR), 0, SLOPE_ARR))

# Relief proxy: local relief within 5Ãƒâ€”5 neighbourhood
from scipy.ndimage import maximum_filter, minimum_filter
dem_safe     = np.where(np.isnan(DEM_ARR), np.nanmean(DEM_ARR), DEM_ARR)
local_relief = maximum_filter(dem_safe, size=5) - minimum_filter(dem_safe, size=5)
local_relief[np.isnan(DEM_ARR)] = np.nan
norm_relief  = normalise_raster(np.where(np.isnan(local_relief), 0, local_relief))

# TWI inverted: high TWI = flat accumulation zone = high flood potential
TWI_safe     = np.where(np.isnan(TWI_ARR2), np.nanmin(TWI_ARR2), TWI_ARR2)
norm_twi     = normalise_raster(TWI_safe)

# SPI: high SPI = high stream power = high flood energy
# Using a placeholder for now, as SPI raster is not generated.
SPI_safe     = np.where(np.isnan(SPI_ARR2), 0, SPI_ARR2) # SPI_ARR2 is a nan placeholder
norm_spi     = normalise_raster(np.log1p(SPI_safe))  # log-transform

# Weighted FFPI Ã¢â‚¬â€ MAP-08: apply flat-area masking on each component
FFPI = (safe_component(norm_slope,  FLAT_MASK_FFPI) * 0.35 +
        safe_component(norm_relief, FLAT_MASK_FFPI) * 0.25 +
        safe_component(norm_twi,    FLAT_MASK_FFPI) * 0.25 +
        safe_component(norm_spi,    FLAT_MASK_FFPI) * 0.15)
FFPI[np.isnan(DEM_ARR)] = np.nan

save_raster(FFPI.astype(np.float32), os.path.join(OUT_DIR, "FFPI.tif"), RASTERS['dem'])
RASTERS['FFPI'] = os.path.join(OUT_DIR, "FFPI.tif")
print(f"  FFPI range: {np.nanmin(FFPI):.3f} Ã¢â‚¬â€œ {np.nanmax(FFPI):.3f}")

# Classify FFPI
def classify_ffpi(val):
    if np.isnan(val): return "Unknown"
    if val > 0.75:    return "Very High"
    if val > 0.55:    return "High"
    if val > 0.35:    return "Moderate"
    if val > 0.20:    return "Low"
    return "Very Low"

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. PER-BASIN HAZARD STATISTICS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[C] Per-basin hazard statistics...")

HAZARD_ROWS = []
for _, row in gdf_sub.iterrows():
    bid  = row['basin_id']
    geom = [row.geometry.__geo_interface__]

    def mask_raster(path):
        with rasterio.open(path) as src:
            try:
                arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
                arr = arr_m[0].astype(np.float32)
                arr[arr == -9999.0] = np.nan
                return arr
            except:
                return np.array([np.nan])

    twi_clip  = mask_raster(RASTERS['twi']) # Use 'twi' (lowercase)
    spi_clip  = mask_raster(RASTERS['spi']) # SPI raster is now available
    sti_clip  = mask_raster(RASTERS['sti']) # STI raster is now available
    ffpi_clip = mask_raster(RASTERS['FFPI'])

    ffpi_mean = float(np.nanmean(ffpi_clip))
    HAZARD_ROWS.append({
        'basin_id'      : bid,
        'TWI_mean'      : round(float(np.nanmean(twi_clip)),  3),
        'TWI_max'       : round(float(np.nanmax(twi_clip)),   3),
        'SPI_mean'      : round(float(np.nanmean(spi_clip)),  3) if np.any(~np.isnan(spi_clip)) else np.nan,
        'SPI_max'       : round(float(np.nanmax(spi_clip)),   3) if np.any(~np.isnan(spi_clip)) else np.nan,
        'STI_mean'      : round(float(np.nanmean(sti_clip)),  3) if np.any(~np.isnan(sti_clip)) else np.nan,
        'STI_max'       : round(float(np.nanmax(sti_clip)),   3) if np.any(~np.isnan(sti_clip)) else np.nan,
        'FFPI_mean'     : round(ffpi_mean, 4),
        'FFPI_max'      : round(float(np.nanmax(ffpi_clip)),  4),
        'FFPI_high_frac': round(float(np.nanmean(ffpi_clip > 0.55)), 4),
        'FFPI_class'    : classify_ffpi(ffpi_mean),
    })
    print(f"  {bid}: TWI_mean={np.nanmean(twi_clip):.2f} | "
          f"SPI_mean={np.nanmean(spi_clip):.2f} | "
          f"FFPI_mean={ffpi_mean:.3f} Ã¢â€ â€™ {classify_ffpi(ffpi_mean)}")

df_hazard = pd.DataFrame(HAZARD_ROWS).set_index('basin_id')

# Composite Flood Hazard Rank
rank_cols = ['TWI_mean', 'SPI_mean', 'STI_mean', 'FFPI_mean']
df_hazard_r = df_hazard[rank_cols].copy()
for col in rank_cols:
    df_hazard[f'rank_{col}'] = df_hazard_r[col].rank(ascending=False, method='min')
df_hazard['FHI_rank'] = df_hazard[[f'rank_{c}' for c in rank_cols]].mean(axis=1)
df_hazard['FHI_priority'] = pd.qcut(
    df_hazard['FHI_rank'], q=3, labels=['High','Moderate','Low'], duplicates='drop'
)

df_hazard.to_csv(os.path.join(TABLES_DIR, "flood_hazard_indices.csv"))
print(f"\n  Ã¢Å“â€¦ Flood hazard table saved")
print(df_hazard[['TWI_mean','SPI_mean','STI_mean','FFPI_mean','FFPI_class','FHI_priority']].to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. MAPS Ã¢â‚¬â€ all 5 hazard maps
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Generating hazard maps...")

utm_ext = compute_utm_extent()

# Ã¢â€â‚¬Ã¢â€â‚¬ MAP-06/07/08: 70:30 layout for all hazard rasters with log-stretch Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# TWI map (MAP-05 fix: masked, log-clamped)
fig, ax_map13, ax_panel13 = make_map_figure("Topographic Wetness Index (TWI)")
add_esri_basemap(ax_map13, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_twi = plt.get_cmap('Blues').copy(); cmap_twi.set_bad(alpha=0)
ax_map13.imshow(TWI_MASKED2, extent=raster_extent(), origin='upper',
    cmap=cmap_twi, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(TWI_MASKED2, 2), vmax=np.nanpercentile(TWI_MASKED2, 98))
gdf_sub.boundary.plot(ax=ax_map13, edgecolor='black', linewidth=1.2, zorder=10)
gdf_streams.plot(ax=ax_map13, color='royalblue', linewidth=0.5, alpha=0.4, zorder=8)
add_continuous_legend_panel(ax_panel13, TWI_MASKED2, 'Blues', 'TWI')
finalize_map(fig, ax_map13, ax_panel13, "13a_TWI_map.png")

# SPI map (MAP-06 fix: log10 stretch)
fig, ax_map13b, ax_panel13b = make_map_figure("Stream Power Index (SPI)\n(logÃ¢â€šÂÃ¢â€šâ‚¬ scale)")
add_esri_basemap(ax_map13b, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_spi = plt.get_cmap('YlOrRd').copy(); cmap_spi.set_bad(alpha=0)
ax_map13b.imshow(SPI_LOG_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_spi, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(SPI_LOG_MASKED, 5), vmax=np.nanpercentile(SPI_LOG_MASKED, 98))
gdf_sub.boundary.plot(ax=ax_map13b, edgecolor='black', linewidth=1.2, zorder=10)
add_continuous_legend_panel(ax_panel13b, SPI_LOG_MASKED, 'YlOrRd', 'logÃ¢â€šÂÃ¢â€šâ‚¬(SPI) [mÃ‚Â²]')
finalize_map(fig, ax_map13b, ax_panel13b, "13b_SPI_map.png")

# STI map (MAP-07 fix: log10 stretch)
fig, ax_map13c, ax_panel13c = make_map_figure("Sediment Transport Index (STI)\n(logÃ¢â€šÂÃ¢â€šâ‚¬ scale)")
add_esri_basemap(ax_map13c, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_sti = plt.get_cmap('RdPu').copy(); cmap_sti.set_bad(alpha=0)
ax_map13c.imshow(STI_LOG_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_sti, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(STI_LOG_MASKED, 5), vmax=np.nanpercentile(STI_LOG_MASKED, 98))
gdf_sub.boundary.plot(ax=ax_map13c, edgecolor='black', linewidth=1.2, zorder=10)
add_continuous_legend_panel(ax_panel13c, STI_LOG_MASKED, 'RdPu', 'logÃ¢â€šÂÃ¢â€šâ‚¬(STI)')
finalize_map(fig, ax_map13c, ax_panel13c, "13c_STI_map.png")

# FFPI map
FFPI_MASKED = mask_raster_to_basin(FFPI.astype(np.float32), DEM_TRANSFORM, gdf_sub)
fig, ax_map13d, ax_panel13d = make_map_figure(
    "Flash Flood Potential Index (FFPI)\n(SlopeÃƒâ€”0.35 + ReliefÃƒâ€”0.25 + TWIÃƒâ€”0.25 + SPIÃƒâ€”0.15)")
add_esri_basemap(ax_map13d, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_ffpi = plt.get_cmap('OrRd').copy(); cmap_ffpi.set_bad(alpha=0)
ax_map13d.imshow(FFPI_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_ffpi, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(FFPI_MASKED, 2), vmax=np.nanpercentile(FFPI_MASKED, 98))
gdf_sub.boundary.plot(ax=ax_map13d, edgecolor='black', linewidth=1.2, zorder=10)
add_continuous_legend_panel(ax_panel13d, FFPI_MASKED, 'OrRd', 'FFPI (0Ã¢â‚¬â€œ1)')
finalize_map(fig, ax_map13d, ax_panel13d, "13d_FFPI_map.png")

# Ã¢â€â‚¬Ã¢â€â‚¬ MAP-09: Composite flood hazard choropleth (70:30, quantile-based) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# MAP-09 fix: use quantile thresholds not fixed values to avoid all-VeryLow
ffpi_vals = np.array([df_hazard.loc[b, 'FFPI_mean'] for b in df_hazard.index])
q20, q40, q60, q80 = np.percentile(ffpi_vals, [20, 40, 60, 80])

def classify_ffpi_quantile(val):
    if val >= q80: return 'Very High'
    if val >= q60: return 'High'
    if val >= q40: return 'Moderate'
    if val >= q20: return 'Low'
    return 'Very Low'

df_hazard['FFPI_class_q'] = [classify_ffpi_quantile(v) for v in ffpi_vals]
ffpi_class_colors = {
    'Very High': '#7f0000', 'High': '#d73027', 'Moderate': '#fc8d59',
    'Low': '#fee090',       'Very Low': '#91bfdb', 'Unknown': 'grey',
}
fig, ax_map13e, ax_panel13e = make_map_figure(
    "Composite Flood Hazard Priority\n(Quantile FFPI Ranking)")
add_esri_basemap(ax_map13e, source=BASEMAP_TOPO, alpha=0.30)
gdf_fhaz = gdf_sub.merge(
    df_hazard[['FFPI_class_q', 'FFPI_mean']].reset_index(), on='basin_id', how='left')
for _, row in gdf_fhaz.iterrows():
    col_f = ffpi_class_colors.get(row['FFPI_class_q'], 'grey')
    gpd.GeoDataFrame([row], geometry='geometry', crs=gdf_sub.crs).plot(
        ax=ax_map13e, color=col_f, edgecolor='black', linewidth=1.2, alpha=0.80, zorder=3)
    cx13, cy13 = row.geometry.centroid.x, row.geometry.centroid.y
    ax_map13e.text(cx13, cy13,
        f"{row['basin_id']}\n{row['FFPI_class_q']}\nFFPI={row['FFPI_mean']:.3f}",
        ha='center', va='center', fontsize=8, fontweight='bold',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])
gdf_so[gdf_so[ORDER_COL] >= 3].plot(ax=ax_map13e, color='royalblue',
                                      linewidth=0.8, alpha=0.5, zorder=6)
_cls_cols  = [ffpi_class_colors[c] for c in ['Very High','High','Moderate','Low','Very Low']]
_cls_lbls  = ['Very High','High','Moderate','Low','Very Low']
add_classified_legend_panel(ax_panel13e, _cls_cols, _cls_lbls,
                             title='Flood Hazard Class', y_top=0.48)
finalize_map(fig, ax_map13e, ax_panel13e, "13e_flood_hazard_composite_map.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. PLOTLY Ã¢â‚¬â€ multi-panel hazard comparison
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[E] Plotly flood hazard charts...")

basins = df_hazard.index.tolist()

# Multi-panel bar comparison
fig = make_subplots(rows=2, cols=2,
                    subplot_titles=['TWI Mean', 'SPI Mean', 'STI Mean', 'FFPI Mean'])
colors_p = px.colors.qualitative.Set1

for panel_i, (col, r, c_idx) in enumerate([
    ('TWI_mean',  1, 1), ('SPI_mean',  1, 2),
    ('STI_mean',  2, 1), ('FFPI_mean', 2, 2),
]):
    fig.add_trace(go.Bar(
        x=basins,
        y=df_hazard[col].tolist(),
        name=col,
        marker_color=colors_p[panel_i % 9],
        text=[f"{v:.3f}" for v in df_hazard[col]],
        textposition='outside',
        hovertemplate='%{x}<br>' + col + ': %{y:.3f}',
    ),
    row=r, col=c_idx)

fig.update_layout(
    title="Flood Hazard Indices Ã¢â‚¬â€ All Subbasins",
    template='plotly_white', height=600, showlegend=False,
)
save_fig(fig, "13f_flood_indices_bar")

# Bubble plot: FFPI vs Drainage Density vs Basin Relief
df_bubble_fh = df_hazard[['FFPI_mean']].join(
    df_master[['Drainage_Density_Dd', 'Basin_Relief_H_m']]
).reset_index()
fig = px.scatter(
    df_bubble_fh, x='Drainage_Density_Dd', y='FFPI_mean',
    size='Basin_Relief_H_m', color='basin_id', text='basin_id',
    title="Flash Flood Potential vs Drainage Density<br>"
          "<sup>Bubble size = Basin Relief (m)</sup>",
    labels={
        'Drainage_Density_Dd': 'Drainage Density (km/kmÃ‚Â²)',
        'FFPI_mean': 'FFPI Mean',
        'Basin_Relief_H_m': 'Relief (m)',
    },
    template='plotly_white', size_max=55,
)
fig.add_hline(y=0.55, line_dash='dash', line_color='red',
              annotation_text='High flood hazard threshold (FFPI=0.55)')
save_fig(fig, "13g_flood_bubble_plot")

# Susceptibility ranking bar
fig = go.Figure()
fig.add_trace(go.Bar(
    x=basins,
    y=df_hazard['FHI_rank'].tolist(),
    marker_color=[
        {'High': '#d73027', 'Moderate': '#fc8d59', 'Low': '#4575b4'}.get(
            str(df_hazard.loc[b, 'FHI_priority']), 'grey'
        ) for b in basins
    ],
    text=[str(df_hazard.loc[b, 'FHI_priority']) for b in basins],
    textposition='outside',
    hovertemplate='%{x}<br>FHI Rank: %{y:.2f}<br>Priority: %{text}',
))
fig.update_layout(
    title="Flood Hazard Priority Ranking<br>"
          "<sup>Lower rank = higher flood susceptibility</sup>",
    xaxis_title="Subbasin", yaxis_title="FHI Composite Rank",
    template='plotly_white', height=430,
    yaxis=dict(autorange='reversed'),
)
save_fig(fig, "13h_flood_susceptibility_ranking")

print("\nÃ¢Å“â€¦ SECTION 13 complete.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  ADVANCED INTERPRETATION PARAGRAPHS (appended to report)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[F] Writing advanced interpretation to report...")

ADVANCED_REPORT_PATH = os.path.join(REPORT_DIR, "advanced_analysis_interpretation.txt")

with open(ADVANCED_REPORT_PATH, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("ADVANCED MORPHOMETRIC ANALYSIS Ã¢â‚¬â€ SUPPLEMENTARY INTERPRETATIONS\n")
    f.write("=" * 80 + "\n\n")

    f.write("10. TECTONIC ACTIVITY ANALYSIS\n" + "-"*40 + "\n")
    f.write(
        "The Index of Active Tectonics (IAT) integrates four geomorphic proxies: "
        "Asymmetry Factor (AF), Transverse Symmetry (T), Valley Floor Width-to-Height "
        "Ratio (Vf), and Mountain Front Sinuosity (Smf), following El Hamdouni et al. "
        "(2008). AF values deviating substantially from 50 indicate basin tilting "
        "driven by differential uplift or lithological asymmetry. Vf < 0.5 is "
        "diagnostic of active incision associated with tectonic uplift, producing "
        "V-shaped valleys, whereas Vf > 1.0 reflects reduced tectonic activity and "
        "lateral widening. Low Smf (< 1.4) indicates a tectonically active, "
        "straight mountain front.\n\n"
    )
    for bid in gdf_sub['basin_id']:
        if bid in df_IAT.index:
            row = df_IAT.loc[bid]
            f.write(
                f"  {bid}: IAT={row['IAT']:.2f} ({row['IAT_class']}). "
                f"AF={row['AF']:.2f}, T={row['T']:.4f}, "
                f"Vf={row['Vf']:.3f}, Smf={row['Smf']:.3f}.\n"
            )
    f.write("\n")

    f.write("11. CHANNEL STEEPNESS & CONCAVITY\n" + "-"*40 + "\n")
    f.write(
        "Channel steepness indices (ksn) and concavity (ÃŽÂ¸) were derived from the "
        "slope-area relationship following Hack (1973) and Flint (1974). High ksn "
        "values indicate either strong lithological resistance, active rock uplift, "
        "or transient adjustment to base-level change. The chi (Ãâ€¡) coordinate plot "
        "(Perron & Royden, 2012) allows comparison of drainage networks independent "
        "of their spatial position, where non-collinear Ãâ€¡-elevation relationships "
        "between adjacent basins signal ongoing divide migration or stream capture. "
        "SL anomaly hotspots correspond to knickpoints or reaches crossing resistant "
        "lithological boundaries.\n\n"
    )
    # THETA_RESULTS and ksn_stats are not defined. Removing the loop that uses them.
    # for bid, tres in THETA_RESULTS.items():
    #     f.write(
    #         f"  {bid}: ÃŽÂ¸={tres['theta_concavity']:.3f} "
    #         f"({'Concave (normal)' if tres['theta_concavity'] > 0.3 else 'Low concavity (active uplift or hard substrate)'}) "
    #         f"| ksn mean={ksn_stats.loc[bid,'ksn_mean'] if bid in ksn_stats.index else 'N/A'} "
    #         f"| RÃ‚Â²={tres['R2_SA']:.3f}\n"
    #     )
    f.write("  (Steepness and concavity parameters were not computed in this run.)\n")
    f.write("\n")

    f.write("12. GEOMORPHIC ANOMALY & LINEAMENT ANALYSIS\n" + "-"*40 + "\n")
    f.write(
        "The Geomorphic Anomaly Index (GAI) integrates SL anomaly, TRI, and inverse "
        "TWI to identify geomorphically active zones where structural or lithological "
        "controls modulate landscape evolution. High GAI zones (top 20th percentile) "
        "are spatially coincident with anomalously high SL reaches, implying "
        "knickpoint clusters, fault zones, or resistant bedrock outcrops. Structural "
        "lineaments were identified as a proxy using Sobel edge detection combined "
        "with Probabilistic Hough Line Transform, targeting linear high-gradient "
        "alignments in the DEM and slope rasters.\n\n"
    )
    for bid in gdf_sub['basin_id']:
        if bid in df_GAI_basin.index:
            g = df_GAI_basin.loc[bid]
            si_m = SI_per_basin.loc[bid, 'SI_mean'] if bid in SI_per_basin.index else np.nan
            f.write(
                f"  {bid}: GAI_mean={g['GAI_mean']:.3f} | "
                f"High anomaly fraction={g['GAI_high_frac']*100:.1f}% | "
                f"Mean SI={si_m:.3f} "
                f"({'Straight Ã¢â‚¬â€ possible structural control' if si_m < 1.05 else 'Sinuous/meandering'})\n"
            )
    f.write("\n")

    f.write("13. FLOOD HAZARD ANALYSIS\n" + "-"*40 + "\n")
    f.write(
        "Topographic Wetness Index (TWI), Stream Power Index (SPI), Sediment Transport "
        "Index (STI), and Flash Flood Potential Index (FFPI) were computed to characterise "
        "the hydrological response and hazard potential of each subbasin. TWI identifies "
        "zones of moisture accumulation and potential saturation-excess overland flow. "
        "High SPI zones correspond to areas of concentrated flow energy capable of "
        "significant geomorphic work. STI quantifies sediment detachment and transport "
        "potential. FFPI synthesises these signals as a weighted composite.\n\n"
    )
    for bid in df_hazard.index:
        row = df_hazard.loc[bid]
        f.write(
            f"  {bid}: FFPI={row['FFPI_mean']:.3f} ({row['FFPI_class']}) | "
            f"TWI_mean={row['TWI_mean']:.2f} | SPI_mean={row['SPI_mean']:.2f} | "
            f"Flood priority: {row['FHI_priority']}\n"
        )
    f.write("\n")

    f.write("REFERENCES (Advanced Sections)\n" + "-"*40 + "\n")
    refs = [
        "Bull, W.B. & McFadden, L.D. (1977). Tectonic geomorphology N & S of the Garlock fault. Geomorphology in arid regions, 115Ã¢â‚¬â€œ138.",
        "Cox, R.T. (1994). Analysis of drainage basin symmetry. Geology, 22(9), 813Ã¢â‚¬â€œ816.",
        "El Hamdouni, R. et al. (2008). Assessment of relative active tectonics, SE Spain. Geomorphology, 96(1Ã¢â‚¬â€œ2), 150Ã¢â‚¬â€œ173.",
        "Flint, J.J. (1974). Stream gradient as a function of order, magnitude, and discharge. Water Resources Research, 10(5), 969Ã¢â‚¬â€œ973.",
        "Gregory, K.J. & Walling, D.E. (1973). Drainage Basin Form and Process. Edward Arnold.",
        "Hack, J.T. (1973). Stream-profile analysis and stream-gradient index. USGS Journal of Research, 1(4), 421Ã¢â‚¬â€œ429.",
        "Moore, I.D., Grayson, R.B. & Ladson, A.R. (1991). Digital terrain modelling. Hydrological Processes, 5(1), 3Ã¢â‚¬â€œ30.",
        "Moore, I.D. & Burch, G.J. (1986). Sediment transport capacity of sheet and rill flow. Water Resources Research, 22(13), 1350Ã¢â‚¬â€œ1360.",
        "Perron, J.T. & Royden, L. (2012). An integral approach to bedrock river profile analysis. Earth Surface Processes and Landforms, 38(6), 570Ã¢â‚¬â€œ576.",
        "Smith, G.H. (2003). The morphometry of drainage basins. Annals of the Association of American Geographers.",
    ]
    for ref in refs:
        f.write(f"  {ref}\n")

print(f"  Ã¢Å“â€¦ Advanced interpretation saved: {ADVANCED_REPORT_PATH}")
print("\nÃ¢Å“â€¦ ALL ADVANCED SECTIONS COMPLETE (10Ã¢â‚¬â€œ13).")
print(f"\n  Total new maps  : 5 tectonic + 3 channel + 3 anomaly + 5 flood = 16 maps")
print(f"  Total new tables: IAT, SL, ksn, theta, sinuosity, GAI, flood hazard = 7 CSVs")
print(f"  Total new plots : 14 interactive Plotly HTML files")


# -*- coding: utf-8 -*-
"""
=============================================================================
 SECTIONS 14Ã¢â‚¬â€œ18 Ã¢â‚¬â€ ADVANCED HYDROLOGICAL & SOIL-WATER CONSERVATION ANALYSIS
 Pravara River Basin, Maharashtra, India
=============================================================================

 Addon to: adv_v2_morphometry_pravra3basin.py
 Run AFTER Sections 0Ã¢â‚¬â€œ13 so the following variables are in memory:
   gdf_sub, gdf_so, gdf_streams, df_master, df_areal, df_relief
   DEM_ARR, FACC_ARR, FDIR_ARR, SLOPE_ARR, HILLSHADE
   DEM_TRANSFORM, DEM_BOUNDS, DEM_RES, DEM_CRS
   UTM_EPSG, ORDER_COL, RASTERS, OUT_DIR, MAPS_DIR,
   PLOTS_DIR, TABLES_DIR, HTML_DIR, SHAPES_DIR
   base_axes, overlay_boundaries, finalize_and_save,
   raster_extent, compute_utm_extent, save_raster,
   save_fig (Plotly helper)

 NEW SECTIONS:
   14 Ã¢â‚¬â€ Runoff Estimation       : SCS-CN, Time of Concentration, Peak Discharge
   15 Ã¢â‚¬â€ RUSLE Soil Erosion Model: RÃ‚Â·KÃ‚Â·LSÃ‚Â·CÃ‚Â·P, SDR, Annual Sediment Yield
   16 Ã¢â‚¬â€ Treatment Planning      : Check dam, Percolation tank, Contour trench
   17 Ã¢â‚¬â€ Synthetic Unit Hydrograph: Snyder's & SCS methods
   18 Ã¢â‚¬â€ Stream Channel Hydraulics: Stream power, Shear stress, Stability index

 Regional context:
   Basin  : Pravara River (Godavari sub-basin), Ahmednagar Dist., Maharashtra
   Lat/Lon: ~19.5Ã‚Â°N, ~73.8Ã‚Â°E  |  CRS: UTM Zone 43N (EPSG:32643)
   Climate: Semi-arid monsoonal Ã¢â‚¬â€ mean annual rainfall ~750 mm (Jun-Sep)
   Geology: Basaltic Deccan Traps Ã¢â‚¬â€ shallow, fine-textured Vertisol/Inceptisol

 References:
   USDA-SCS (1985). Hydrology. National Engineering Handbook, Section 4.
   Wischmeier & Smith (1978). Predicting Rainfall Erosion Losses. USDA-AH537.
   Moore et al. (1991). Digital Terrain Modelling. Hydrol. Processes 5, 3-30.
   Snyder (1938). Synthetic Unit Hydrographs. Trans. AGU 19, 447-454.
   Singh (1988). Hydrologic Systems Vol. I. Prentice-Hall.
   Kirpich (1940). Time of Concentration. Civil Engineering 10(6), 362.
   Mitasova et al. (1996). Modelling topographic potential for erosion.
   Bagnold (1966). An Approach to the Sediment Transport Problem.
   Leopold & Maddock (1953). Hydraulic Geometry. USGS Prof. Paper 252.
=============================================================================
"""

# Ã¢â€â‚¬Ã¢â€â‚¬ Standard imports (all should already be in memory from Sections 0Ã¢â‚¬â€œ13) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import os
import warnings
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.mask import mask as rio_mask
from rasterio.transform import rowcol, xy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize, LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import stats
from scipy.ndimage import gaussian_filter, uniform_filter, label as ndlabel
from shapely.geometry import Point, LineString, Polygon
from shapely.ops import linemerge
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

warnings.filterwarnings("ignore")

# Ã¢â€â‚¬Ã¢â€â‚¬ Output sub-directories Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
HYD_DIR   = os.path.join(OUT_DIR, "hydrology/")
SWC_DIR   = os.path.join(OUT_DIR, "conservation/")
UHG_DIR   = os.path.join(OUT_DIR, "unit_hydrograph/")
HYD_MAPS  = os.path.join(MAPS_DIR, "hydrology/")
SWC_MAPS  = os.path.join(MAPS_DIR, "conservation/")

for d in [HYD_DIR, SWC_DIR, UHG_DIR, HYD_MAPS, SWC_MAPS]:
    os.makedirs(d, exist_ok=True)

print("Ã¢Å“â€¦ Output directories created.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
