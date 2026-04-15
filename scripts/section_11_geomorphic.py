print("SECTION 11 Ã¢â‚¬â€ GEOMORPHIC INDICES: SL, SPI, TWI")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  HELPER FUNCTIONS (for SL, SPI, TWI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

def calculate_sl_index(stream_gdf, dem_arr, dem_transform, k=10):
    """
    Calculate Stream Length-gradient (SL) index for each stream segment.
    SL = (dH/dL) * L.
    dH/dL is local gradient, L is total channel length upstream (approximated).
    The local gradient is calculated over a window of k cells.
    """
    sl_indices = []
    for idx, row in stream_gdf.iterrows():
        geom = row.geometry
        if geom.geom_type == 'MultiLineString':
            geom = max(geom.geoms, key=lambda g: g.length)
        if geom.geom_type != 'LineString' or geom.length == 0:
            sl_indices.append(np.nan)
            continue

        coords = list(geom.coords)
        if len(coords) < 2:
            sl_indices.append(np.nan)
            continue

        # Sample elevation along the stream
        elevations = []
        for p in coords:
            row_idx, col_idx = rasterio.transform.rowcol(dem_transform, p[0], p[1])
            if 0 <= row_idx < dem_arr.shape[0] and 0 <= col_idx < dem_arr.shape[1]:
                elevations.append(dem_arr[row_idx, col_idx])
            else:
                elevations.append(np.nan)
        elevations = np.array(elevations)

        # Remove NaNs and corresponding coordinates
        valid_indices = ~np.isnan(elevations)
        elevations_valid = elevations[valid_indices]
        coords_valid     = np.array(coords)[valid_indices]

        if len(elevations_valid) < 2:
            sl_indices.append(np.nan)
            continue

        # Calculate local gradient (dH/dL) over a window of k points
        gradients = []
        for i in range(len(elevations_valid) - k):
            p1 = coords_valid[i]
            p2 = coords_valid[i+k]
            dist = np.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
            if dist > 0:
                grad = (elevations_valid[i] - elevations_valid[i+k]) / dist
                gradients.append(grad)

        if not gradients:
            sl_indices.append(np.nan)
            continue

        local_gradient = np.nanmean(gradients) # Average gradient over segment

        # Approximate upstream length as the total length of the segment
        # A more rigorous approach would trace upstream from the pour point
        L_upstream = geom.length # Approximation

        sl_index = local_gradient * L_upstream
        sl_indices.append(sl_index)
    return sl_indices

def calculate_spi(stream_gdf, flow_acc_arr, slope_arr, dem_res, dem_transform=None, threshold=1e-6):
    if dem_transform is None:
        dem_transform = DEM_TRANSFORM
    """
    Calculate Stream Power Index (SPI) for each stream segment.
    SPI = As * tan(beta), where As is contributing area, beta is slope.
    Approximates As with flow accumulation * cell_area.
    """
    spi_values = []
    for idx, row in stream_gdf.iterrows():
        geom = row.geometry
        if geom.geom_type == 'MultiLineString':
            geom = max(geom.geoms, key=lambda g: g.length)
        if geom.geom_type != 'LineString' or geom.length == 0:
            spi_values.append(np.nan)
            continue

        coords = list(geom.coords)
        fa_values = []
        slope_values = []

        for p in coords:
            row_idx, col_idx = rasterio.transform.rowcol(dem_transform, p[0], p[1])
            if 0 <= row_idx < flow_acc_arr.shape[0] and 0 <= col_idx < flow_acc_arr.shape[1]:
                fa_values.append(flow_acc_arr[row_idx, col_idx])
                slope_values.append(slope_arr[row_idx, col_idx])
            else:
                fa_values.append(np.nan)
                slope_values.append(np.nan)

        fa_values = np.array(fa_values)
        slope_values = np.array(slope_values)

        valid_indices = ~np.isnan(fa_values) & ~np.isnan(slope_values)
        if not np.any(valid_indices):
            spi_values.append(np.nan)
            continue

        # Use mean flow accumulation and slope for the segment
        mean_fa    = np.nanmean(fa_values[valid_indices])
        mean_slope = np.nanmean(slope_values[valid_indices]) # in degrees

        # Convert slope to radians for tan function
        mean_slope_rad = np.radians(mean_slope)

        # As (contributing area) = flow_accumulation * cell_area
        cell_area = dem_res * dem_res # m^2
        As = mean_fa * cell_area

        # Avoid division by zero or tan(90 deg)
        tan_beta = np.tan(mean_slope_rad)
        if tan_beta < threshold: # Set a small threshold for very flat areas
            tan_beta = threshold

        spi = As * tan_beta
        spi_values.append(spi)

    return spi_values

def calculate_sti(stream_gdf, flow_acc_arr, slope_arr, dem_res, dem_transform=None, threshold=1e-6):
    if dem_transform is None:
        dem_transform = DEM_TRANSFORM
    """
    Calculate Sediment Transport Index (STI) for each stream segment.
    STI = (As * sin(beta)). Simplified version for segments.
    Approximates As with flow accumulation * cell_area.
    """
    sti_values = []
    for idx, row in stream_gdf.iterrows():
        geom = row.geometry
        if geom.geom_type == 'MultiLineString':
            geom = max(geom.geoms, key=lambda g: g.length)
        if geom.geom_type != 'LineString' or geom.length == 0:
            sti_values.append(np.nan)
            continue

        coords = list(geom.coords)
        fa_values = []
        slope_values = []

        for p in coords:
            row_idx, col_idx = rasterio.transform.rowcol(dem_transform, p[0], p[1])
            if 0 <= row_idx < flow_acc_arr.shape[0] and 0 <= col_idx < flow_acc_arr.shape[1]:
                fa_values.append(flow_acc_arr[row_idx, col_idx])
                slope_values.append(slope_arr[row_idx, col_idx])
            else:
                fa_values.append(np.nan)
                slope_values.append(np.nan)

        fa_values = np.array(fa_values)
        slope_values = np.array(slope_values)

        valid_indices = ~np.isnan(fa_values) & ~np.isnan(slope_values)
        if not np.any(valid_indices):
            sti_values.append(np.nan)
            continue

        mean_fa = np.nanmean(fa_values[valid_indices])
        mean_slope = np.nanmean(slope_values[valid_indices]) # in degrees

        mean_slope_rad = np.radians(mean_slope)
        As = mean_fa * dem_res # Specific catchment area (m) for unit contour length (simplified)

        # Ã¢â€â‚¬Ã¢â€â‚¬ Correct STI per Moore & Burch (1986) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
        # STI = (As/22.13)^0.6 Ãƒâ€” (sin ÃŽÂ² / 0.0896)^1.3
        cell_area = dem_res * dem_res                   # mÃ‚Â²
        As_seg    = mean_fa * dem_res                   # specific catchment area m
        sin_beta  = max(np.sin(mean_slope_rad), threshold)

        sti = ((As_seg / 22.13) ** 0.6) * ((sin_beta / 0.0896) ** 1.3)
        sti_values.append(float(sti))

    return sti_values

def calculate_twi(dem_arr, dem_res):
    """
    Calculate Topographic Wetness Index (TWI) raster using a simple approach.
    TWI = ln(As / tan(beta))
    As is specific catchment area (approximated by flow accumulation * cell size)
    tan(beta) is local slope.
    This is a simplified TWI calculation for demonstration. For precise TWI,
    a dedicated hydrological model (e.g., WhiteboxTools, pysheds) is needed.
    """
    # Use existing flow accumulation and slope arrays
    flow_acc_arr = FACC_ARR.copy()
    slope_arr    = SLOPE_ARR.copy() # already in degrees

    # Convert slope to radians
    slope_rad_arr = np.radians(slope_arr)

    # Calculate specific catchment area (As) - approximation
    # Assuming flow_acc_arr represents number of upstream cells
    As_arr = flow_acc_arr * dem_res  # Specific catchment area (m^2/m)

    # Avoid division by zero or tan(0)
    tan_beta_arr = np.tan(slope_rad_arr)
    # Set a minimum slope to avoid log of zero/negative and very high TWI values
    min_slope_rad = np.radians(0.01) # 0.01 degrees minimum slope
    tan_beta_arr[tan_beta_arr < np.tan(min_slope_rad)] = np.tan(min_slope_rad)

    # Ã¢â€â‚¬Ã¢â€â‚¬ Compute TWI only where As > 0 and slope > 0 Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    valid_mask = (As_arr > 0) & (~np.isnan(dem_arr)) & (tan_beta_arr > np.tan(min_slope_rad))
    twi_arr    = np.full(dem_arr.shape, np.nan, dtype=np.float32)
    twi_arr[valid_mask] = np.log(As_arr[valid_mask] / tan_beta_arr[valid_mask])
    # Clamp to physically reasonable range
    twi_arr = np.clip(twi_arr, -5.0, 25.0)
    twi_arr[~valid_mask] = np.nan

    return twi_arr.astype(np.float32)

def rasterize_segment_attribute(gdf, attribute_col, dem_arr_shape, dem_transform, nodata_val=-9999.0):
    """
    Rasterize a GeoDataFrame's attribute (from line segments) onto a raster grid.
    Values are burned along the line's path, taking the max value if multiple lines cross.
    """
    raster = np.full(dem_arr_shape, np.nan, dtype=np.float32)

    for _, row in gdf[gdf[attribute_col].notna()].iterrows():
        geom = row.geometry
        val  = row[attribute_col]
        if geom.geom_type == 'MultiLineString':
            for single_line in geom.geoms:
                for x, y in single_line.coords:
                    r_idx, c_idx = rasterio.transform.rowcol(dem_transform, x, y)
                    if 0 <= r_idx < dem_arr_shape[0] and 0 <= c_idx < dem_arr_shape[1]:
                        if np.isnan(raster[r_idx, c_idx]):
                            raster[r_idx, c_idx] = val
                        else:
                            raster[r_idx, c_idx] = max(raster[r_idx, c_idx], val)
        elif geom.geom_type == 'LineString':
            for x, y in geom.coords:
                r_idx, c_idx = rasterio.transform.rowcol(dem_transform, x, y)
                if 0 <= r_idx < dem_arr_shape[0] and 0 <= c_idx < dem_arr_shape[1]:
                    if np.isnan(raster[r_idx, c_idx]):
                        raster[r_idx, c_idx] = val
                    else:
                        raster[r_idx, c_idx] = max(raster[r_idx, c_idx], val)

    # Fill remaining NaNs with nodata_val for rasterio compatibility
    raster[np.isnan(raster)] = nodata_val
    return raster.astype(np.float32)


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. STREAM LENGTH-GRADIENT (SL) INDEX
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[A] Computing Stream Length-gradient (SL) Index...")

# Join stream segments to subbasins for basin_id access
gdf_so_with_basin_id = gpd.sjoin(
    gdf_so.copy(), gdf_sub[['basin_id', 'geometry']], how='left', predicate='intersects'
).drop(columns=['index_right']).dropna(subset=['basin_id'])

# Ensure basin_id is set correctly for all segments
if 'basin_id' not in gdf_so_with_basin_id.columns:
    # Fallback if sjoin fails to assign basin_id consistently
    gdf_so_with_basin_id['basin_id'] = None
    for bid in gdf_sub['basin_id'].unique():
        basin_geom = gdf_sub[gdf_sub['basin_id'] == bid].geometry.iloc[0]
        # Find streams within this basin
        streams_in_basin = gdf_so_with_basin_id.geometry.apply(lambda x: x.intersects(basin_geom))
        gdf_so_with_basin_id.loc[streams_in_basin, 'basin_id'] = bid

# Calculate SL index for each segment
# Using gdf_so (stream order segments) as the base for SL calculations
gdf_SL = gdf_so_with_basin_id.copy()
gdf_SL['SL_index'] = calculate_sl_index(gdf_SL, DEM_ARR, DEM_TRANSFORM)

# Calculate SL anomaly (deviation from mean for its order)
mean_sl_per_order = gdf_SL.groupby(ORDER_COL)['SL_index'].mean()
std_sl_per_order  = gdf_SL.groupby(ORDER_COL)['SL_index'].std()

gdf_SL['mean_SL_order'] = gdf_SL[ORDER_COL].map(mean_sl_per_order)
gdf_SL['std_SL_order']  = gdf_SL[ORDER_COL].map(std_sl_per_order)

# SL anomaly is deviation from mean SL for its order, normalized by std dev
gdf_SL['SL_anomaly'] = (gdf_SL['SL_index'] - gdf_SL['mean_SL_order']) / gdf_SL['std_SL_order']

# Replace inf/-inf with nan for anomaly calculation
gdf_SL['SL_anomaly'] = gdf_SL['SL_anomaly'].replace([np.inf, -np.inf], np.nan)

# Store max SL anomaly per basin for plotting/summary later
SL_per_basin = gdf_SL.groupby('basin_id')['SL_anomaly'].agg(
    SL_anomaly_mean='mean', SL_anomaly_max='max', SL_anomaly_std='std'
).round(4)

print("  SL Anomaly per basin (mean/max):")
print(SL_per_basin.to_string())
SL_per_basin.to_csv(os.path.join(TABLES_DIR, "sl_anomaly_per_basin.csv"))
gdf_SL.to_file(os.path.join(SHAPES_DIR, "streams_sl_anomaly.shp"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. STREAM POWER INDEX (SPI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[B] Computing Stream Power Index (SPI)...")

gdf_SL['SPI'] = calculate_spi(gdf_SL, FACC_ARR, SLOPE_ARR, DEM_RES, dem_transform=DEM_TRANSFORM)

SPI_per_basin = gdf_SL.groupby('basin_id')['SPI'].agg(
    SPI_mean='mean', SPI_max='max', SPI_std='std'
).round(4)
print("  SPI per basin (mean/max):")
print(SPI_per_basin.to_string())
SPI_per_basin.to_csv(os.path.join(TABLES_DIR, "spi_per_basin.csv"))

# Rasterize SPI
SPI_ARR = rasterize_segment_attribute(gdf_SL, 'SPI', DEM_ARR.shape, DEM_TRANSFORM)
save_raster(SPI_ARR, os.path.join(OUT_DIR, "spi.tif"), RASTERS['dem'])
RASTERS['spi'] = os.path.join(OUT_DIR, "spi.tif")
print(f"  SPI raster range: {np.nanmin(SPI_ARR):.3f} Ã¢â‚¬â€œ {np.nanmax(SPI_ARR):.3f}")


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. SEDIMENT TRANSPORT INDEX (STI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[C] Computing Sediment Transport Index (STI)...")

gdf_SL['STI'] = calculate_sti(gdf_SL, FACC_ARR, SLOPE_ARR, DEM_RES, dem_transform=DEM_TRANSFORM)

STI_per_basin = gdf_SL.groupby('basin_id')['STI'].agg(
    STI_mean='mean', STI_max='max', STI_std='std'
).round(4)
print("  STI per basin (mean/max):")
print(STI_per_basin.to_string())
STI_per_basin.to_csv(os.path.join(TABLES_DIR, "sti_per_basin.csv"))

# Rasterize STI
STI_ARR = rasterize_segment_attribute(gdf_SL, 'STI', DEM_ARR.shape, DEM_TRANSFORM)
save_raster(STI_ARR, os.path.join(OUT_DIR, "sti.tif"), RASTERS['dem'])
RASTERS['sti'] = os.path.join(OUT_DIR, "sti.tif")
print(f"  STI raster range: {np.nanmin(STI_ARR):.3f} Ã¢â‚¬â€œ {np.nanmax(STI_ARR):.3f}")


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. TOPOGRAPHIC WETNESS INDEX (TWI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Computing Topographic Wetness Index (TWI)...")

TWI_ARR = calculate_twi(DEM_ARR, DEM_RES)
# MAP-05: clamp TWI and mask flat-area artifacts (slope < 0.05 deg)
TWI_ARR = np.clip(TWI_ARR, 0.0, 18.0)
SLOPE_SAFE_DEG = np.where(np.isnan(SLOPE_ARR), 90.0, SLOPE_ARR)
TWI_ARR[SLOPE_SAFE_DEG < 0.05] = np.nan
save_raster(TWI_ARR, os.path.join(OUT_DIR, "twi.tif"), RASTERS['dem'])
RASTERS['twi'] = os.path.join(OUT_DIR, "twi.tif")
print(f"  TWI range: {np.nanmin(TWI_ARR):.3f} Ã¢â‚¬â€œ {np.nanmax(TWI_ARR):.3f}")

# Per-basin TWI statistics
TWI_basin = []
for _, row in gdf_sub.iterrows():
    geom = [row.geometry.__geo_interface__]
    with rasterio.open(os.path.join(OUT_DIR, "twi.tif")) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            twi_clip  = arr_m[0]
            twi_clip[twi_clip == -9999] = np.nan
        except:
            twi_clip  = TWI_ARR.copy()
    TWI_basin.append({
        'basin_id': row['basin_id'],
        'TWI_mean': round(float(np.nanmean(twi_clip)), 4),
        'TWI_max' : round(float(np.nanmax(twi_clip)), 4),
        'TWI_std': round(float(np.nanstd(twi_clip)), 4),
    })
df_TWI_basin = pd.DataFrame(TWI_basin).set_index('basin_id')
print("  Per-basin TWI:")
print(df_TWI_basin.to_string())
df_TWI_basin.to_csv(os.path.join(TABLES_DIR, "twi_per_basin.csv"))

print("\nÃ¢Å“â€¦ SECTION 11 complete.")

print("=" * 60)
