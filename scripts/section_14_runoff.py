# SECTION 14 Ã¢â‚¬â€ RUNOFF ESTIMATION: SCS-CN, TIME OF CONCENTRATION, PEAK FLOW
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n" + "=" * 70)
print("SECTION 14 Ã¢â‚¬â€ RUNOFF ESTIMATION (SCS-CN + RATIONAL METHOD)")
print("=" * 70)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. RAINFALL FREQUENCY ANALYSIS Ã¢â‚¬â€ Gumbel Extreme Value Type-I (EV-I)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Pravara basin (Ahmednagar dist., Maharashtra) historical rainfall statistics
# Source: IMD data / regional studies for Upper Godavari sub-basin
# Mean annual rainfall: 750 mm | Std dev: 187 mm | CV Ã¢â€°Ë† 0.25

print("\n[14-A] Rainfall Frequency Analysis (Gumbel EV-I)...")

RAIN_MEAN_MM = 750.0   # Mean annual rainfall (mm)
RAIN_STD_MM  = 187.0   # Standard deviation (mm)

# Gumbel EV-I parameters
alpha_g = RAIN_STD_MM * np.sqrt(6) / np.pi          # scale
u_g     = RAIN_MEAN_MM - 0.5772 * alpha_g           # location (mode)

# Return period rainfall (1-day max derived as fraction of annual)
# Ratio of 1-day max to annual: ~0.20-0.25 for semi-arid India
DAILY_FRACTION = 0.22

RETURN_PERIODS = [2, 5, 10, 25, 50, 100]
RAINFALL_RT    = {}   # P24hr [mm] for each return period

gumbel_rows = []
for T in RETURN_PERIODS:
    y_T  = -np.log(-np.log(1 - 1/T))               # Gumbel reduced variate
    P_T  = (u_g + alpha_g * y_T) * DAILY_FRACTION  # 24-hr max rainfall
    P_T  = max(P_T, 10.0)                           # floor at 10 mm
    RAINFALL_RT[T] = round(P_T, 1)
    gumbel_rows.append({'Return_Period_yr': T,
                        'Annual_Rainfall_mm': round(u_g + alpha_g * y_T, 1),
                        'P24hr_mm': round(P_T, 1)})
    print(f"  T={T:4d}-yr: Annual = {u_g + alpha_g * y_T:.0f} mm | "
          f"P24hr = {P_T:.1f} mm")

df_rainfall_freq = pd.DataFrame(gumbel_rows)
df_rainfall_freq.to_csv(os.path.join(HYD_DIR, "rainfall_frequency.csv"), index=False)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. CURVE NUMBER MAP Ã¢â‚¬â€ SLOPE-BASED PROXY (no land-use raster available)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# CN assigned per pixel using SLOPE class as proxy:
#   Flat  (<  3Ã‚Â°): Poorly drained, compacted Ã¢â‚¬â€ CN=85 (soil group C/D)
#   Gentle( 3Ã¢â‚¬â€œ8Ã‚Â°): Mixed cultivated/fallow   Ã¢â‚¬â€ CN=79 (soil group B/C)
#   Moderate(8Ã¢â‚¬â€œ20Ã‚Â°): Degraded hill slope     Ã¢â‚¬â€ CN=75 (soil group B)
#   Steep (>20Ã‚Â°):  Rock/shallow soil         Ã¢â‚¬â€ CN=70 (soil group A/B)
# These represent typical Deccan Trap basalt conditions under AMC-II.

print("\n[14-B] Computing Curve Number raster...")

CN_ARR = np.full(DEM_ARR.shape, np.nan, dtype=np.float32)
# Ã¢â€â‚¬Ã¢â€â‚¬ BUG-09: defensive guard if section reruns independently Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
if 'slope_safe' not in dir():
    slope_safe = np.where(np.isnan(SLOPE_ARR), 0.0, SLOPE_ARR)
    print("  slope_safe re-initialised.")
else:
    slope_safe = np.where(np.isnan(SLOPE_ARR), 0.0, SLOPE_ARR)

CN_ARR = np.where(slope_safe <  3,   85.0,
         np.where(slope_safe <  8,   79.0,
         np.where(slope_safe < 20,   75.0,
                                     70.0)))
CN_ARR[np.isnan(DEM_ARR)] = np.nan

# Save CN raster
save_raster(CN_ARR, os.path.join(OUT_DIR, "CN.tif"), RASTERS["dem"])
RASTERS["CN"] = os.path.join(OUT_DIR, "CN.tif")
print(f"  CN range: {np.nanmin(CN_ARR):.0f}Ã¢â‚¬â€œ{np.nanmax(CN_ARR):.0f} | "
      f"Mean: {np.nanmean(CN_ARR):.1f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. SCS-CN DIRECT RUNOFF & PER-BASIN RUNOFF STATISTICS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[14-C] SCS-CN Direct Runoff calculation...")

def scscn_runoff(P_mm, CN):
    """
    SCS-CN direct runoff (Q) for rainfall P [mm] and Curve Number CN.
    Q = (P - 0.2Ã‚Â·S)Ã‚Â² / (P + 0.8Ã‚Â·S)  if P > 0.2Ã‚Â·S  else Q = 0
    S = 25400/CN - 254  (potential max retention, mm)
    """
    S = 25400.0 / CN - 254.0          # potential max retention [mm]
    I_a = 0.2 * S                      # initial abstraction [mm]
    valid = P_mm > I_a
    Q = np.where(valid, (P_mm - I_a)**2 / (P_mm + 0.8*S), 0.0)
    return np.maximum(Q, 0.0)

def runoff_coeff(P_mm, CN):
    """Runoff coefficient C = Q/P."""
    Q = scscn_runoff(P_mm, CN)
    return np.where(P_mm > 0, Q / P_mm, 0.0)

# Per-basin: compute CN_mean, S_mean, Q for each return period, runoff volume
RUNOFF_ROWS = []

for _, row in gdf_sub.iterrows():
    bid  = row["basin_id"]
    geom = [row.geometry.__geo_interface__]
    A_km2 = df_areal.loc[bid, "Area_km2"]
    A_m2  = A_km2 * 1e6

    # Clip CN to basin
    with rasterio.open(RASTERS["CN"]) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            cn_clip  = arr_m[0].astype(np.float32)
            cn_clip[cn_clip == -9999.0] = np.nan
        except Exception:
            cn_clip = CN_ARR.copy()

    CN_mean = float(np.nanmean(cn_clip))
    CN_std  = float(np.nanstd(cn_clip))
    S_mean  = 25400.0 / CN_mean - 254.0     # [mm]
    Ia_mean = 0.2 * S_mean                  # initial abstraction [mm]

    r_row = {"basin_id": bid, "CN_mean": round(CN_mean, 2),
             "CN_std": round(CN_std, 2), "S_mm": round(S_mean, 2),
             "Ia_mm": round(Ia_mean, 2), "Area_km2": round(A_km2, 3)}

    for T in RETURN_PERIODS:
        P = RAINFALL_RT[T]
        Q = float(scscn_runoff(P, CN_mean))
        C = float(runoff_coeff(P, CN_mean))
        Vol_Mm3 = Q * 1e-3 * A_m2 / 1e6   # Million cubic metres
        r_row[f"P_{T}yr_mm"]    = P
        r_row[f"Q_{T}yr_mm"]    = round(Q, 2)
        r_row[f"C_{T}yr"]       = round(C, 3)
        r_row[f"Vol_{T}yr_Mm3"] = round(Vol_Mm3, 4)

    RUNOFF_ROWS.append(r_row)
    print(f"  {bid}: CN={CN_mean:.1f} | S={S_mean:.1f} mm | "
          f"Q(25yr)={r_row['Q_25yr_mm']:.1f} mm | "
          f"Vol(25yr)={r_row['Vol_25yr_Mm3']:.4f} MmÃ‚Â³")

df_runoff = pd.DataFrame(RUNOFF_ROWS).set_index("basin_id")
df_runoff.to_csv(os.path.join(HYD_DIR, "runoff_scscn.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. TIME OF CONCENTRATION Ã¢â‚¬â€ KIRPICH, SCS LAG, OVERLAND FLOW
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[14-D] Time of Concentration (Tc) calculations...")

def tc_kirpich(L_m, H_m):
    """
    Kirpich (1940): Tc = 0.0195 Ãƒâ€” L^0.77 Ãƒâ€” S^-0.385
    L = channel length (m), H = head difference (m)
    S = H/L (dimensionless slope)
    Returns Tc in minutes.
    """
    S = H_m / L_m if L_m > 0 else 0.001
    S = max(S, 0.0001)
    Tc = 0.0195 * (L_m ** 0.77) * (S ** -0.385)
    return Tc  # minutes

def tc_scs_lag(L_m, CN, S_avg_pct):
    """
    SCS Lag method: tL = (L^0.8 Ãƒâ€” (S+1)^0.7) / (1900 Ãƒâ€” Y^0.5)
    L = hydraulic length (feet), S = (1000/CN)-10, Y = average watershed slope (%)
    Returns lag time tL in hours; Tc = tL / 0.6
    """
    L_ft = L_m * 3.28084
    S_val = 1000.0 / CN - 10.0
    Y = max(S_avg_pct, 0.1)
    tL = (L_ft**0.8 * (S_val + 1)**0.7) / (1900.0 * Y**0.5)  # hours
    Tc = tL / 0.6
    return Tc * 60  # minutes

def tc_overland(L_m, n_mann, slope_frac, P_mm):
    """
    NRCS Overland Flow Tc (sheet flow):
    Tt = 0.007 Ãƒâ€” (nÃƒâ€”L)^0.8 / (PÃ‚Â²^0.5 Ãƒâ€” S^0.4)
    n = Manning roughness, P2 = 2-year 24-hr rainfall (mmÃ¢â€ â€™in)
    Returns Tt in hours; usually only for first 100m of flow.
    """
    P2_in = P_mm * 0.0394
    L_use = min(L_m, 100.0)   # max 100m for sheet flow
    S     = max(slope_frac, 0.001)
    Tt    = 0.007 * ((n_mann * L_use)**0.8) / ((P2_in**0.5) * (S**0.4))
    return Tt * 60  # minutes

TC_ROWS = []

for _, row in gdf_sub.iterrows():
    bid    = row["basin_id"]
    A_km2  = df_areal.loc[bid, "Area_km2"]
    Lb_km  = df_areal.loc[bid, "Basin_Length_km"]
    L_m    = Lb_km * 1000.0
    H_m    = df_relief.loc[bid, "Basin_Relief_H_m"] if bid in df_relief.index else 100.0
    slope_deg = df_relief.loc[bid, "Slope_Mean_deg"] if bid in df_relief.index else 5.0
    slope_pct = np.tan(np.radians(slope_deg)) * 100.0
    slope_frac = slope_pct / 100.0
    CN_mean   = df_runoff.loc[bid, "CN_mean"]
    P2_mm     = RAINFALL_RT[2]   # 2-yr 24-hr rainfall

    Tc_k   = tc_kirpich(L_m, H_m)
    Tc_scs = tc_scs_lag(L_m, CN_mean, slope_pct)
    Tc_ov  = tc_overland(min(L_m, 100), 0.15, slope_frac, P2_mm)
    Tc_avg = np.mean([Tc_k, Tc_scs])   # practical average

    # Rational method peak discharge: Qp = C Ãƒâ€” i Ãƒâ€” A / 360
    # i = rainfall intensity at Tc [mm/hr] using Tc in minutes
    # Using Dickens formula common for India: i = a / (Tc + b)
    # Or convert P24hr to intensity using Chen (1983) or Indian standard IDF
    # Indian IMD empirical: i_Tc = P24hr Ãƒâ€” (24/Tc_hr)^(2/3) / 24  [mm/hr]
    Q_PEAK = {}
    C_rational = {}
    for T in RETURN_PERIODS:
        P24 = RAINFALL_RT[T]
        Tc_hr = Tc_avg / 60.0
        i_Tc  = (P24 / 24.0) * (24.0 / Tc_hr) ** (2.0/3.0)  # mm/hr
        # C (runoff coeff from SCS Q/P for this storm)
        C_val = float(runoff_coeff(P24, CN_mean))
        # Qp [mÃ‚Â³/s] = C Ãƒâ€” i [mm/hr] Ãƒâ€” A [kmÃ‚Â²] / 3.6
        Qp = C_val * i_Tc * A_km2 / 3.6
        Q_PEAK[T] = round(Qp, 3)
        C_rational[T] = round(C_val, 3)

    r_tc = {
        "basin_id"     : bid,
        "L_km"         : round(Lb_km, 3),
        "H_m"          : round(H_m, 1),
        "Slope_pct"    : round(slope_pct, 2),
        "Tc_Kirpich_min": round(Tc_k, 1),
        "Tc_SCS_min"   : round(Tc_scs, 1),
        "Tc_Avg_min"   : round(Tc_avg, 1),
        "Tc_hr"        : round(Tc_avg / 60.0, 3),
    }
    for T in RETURN_PERIODS:
        r_tc[f"Qp_{T}yr_m3s"]  = Q_PEAK[T]
        r_tc[f"C_{T}yr"]       = C_rational[T]

    TC_ROWS.append(r_tc)
    print(f"  {bid}: Tc_Kirpich={Tc_k:.1f} min | Tc_SCS={Tc_scs:.1f} min | "
          f"Qp(25yr)={Q_PEAK[25]:.2f} mÃ‚Â³/s")

df_tc = pd.DataFrame(TC_ROWS).set_index("basin_id")
df_tc.to_csv(os.path.join(HYD_DIR, "time_of_concentration_peak_discharge.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. RUNOFF MAPS & PLOTLY CHARTS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[14-E] Generating runoff maps...")

# CN map
fig, ax, utm_ext = base_axes("Curve Number (CN) Map Ã¢â‚¬â€ SCS-CN, AMC-II\n"
                              "(Slope-based proxy, Deccan Trap basalt)")
im = ax.imshow(CN_ARR, extent=raster_extent(), origin="upper",
               cmap="RdYlGn_r", alpha=0.80, zorder=1, vmin=68, vmax=88)
overlay_boundaries(ax)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.07)
cb  = plt.colorbar(im, cax=cax)
cb.set_label("Curve Number (CN)", fontsize=10)
# Annotate each basin with CN mean
for _, r in gdf_sub.iterrows():
    bid = r["basin_id"]
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    cn_val = df_runoff.loc[bid, "CN_mean"] if bid in df_runoff.index else np.nan
    ax.text(cx, cy, f"{bid}\nCN={cn_val:.1f}", ha="center", va="center",
            fontsize=8, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
finalize_and_save(fig, ax, utm_ext, "14a_CN_map.png")

# Runoff volume map for 25-yr event
fig, ax, utm_ext = base_axes("Direct Runoff Volume Map Ã¢â‚¬â€ 25-year Return Period Event\n"
                              "(SCS-CN method, per subbasin)")
gdf_rv = gdf_sub.merge(
    df_runoff[["Q_25yr_mm", "Vol_25yr_Mm3", "CN_mean"]].reset_index(),
    on="basin_id", how="left"
)
gdf_rv.plot(column="Vol_25yr_Mm3", ax=ax, cmap="Blues", legend=True, alpha=0.80,
            zorder=2, edgecolor="black", linewidth=1.2,
            legend_kwds={"label": "Runoff Volume (MmÃ‚Â³)", "shrink": 0.75})
for _, r in gdf_rv.iterrows():
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    ax.text(cx, cy,
            f"{r['basin_id']}\nQ={r['Q_25yr_mm']:.0f} mm\n{r['Vol_25yr_Mm3']:.3f} MmÃ‚Â³",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.7, alpha=0.5, zorder=5)
finalize_and_save(fig, ax, utm_ext, "14b_runoff_volume_25yr.png")

# Plotly: multi-return-period peak discharge comparison
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Peak Discharge by Return Period (mÃ‚Â³/s)",
                                    "Runoff Depth by Return Period (mm)"])
colors_rt = px.colors.qualitative.Set1
for i, bid in enumerate(df_tc.index):
    qp_vals = [df_tc.loc[bid, f"Qp_{T}yr_m3s"] for T in RETURN_PERIODS]
    q_vals  = [df_runoff.loc[bid, f"Q_{T}yr_mm"] for T in RETURN_PERIODS]
    fig.add_trace(go.Scatter(
        x=RETURN_PERIODS, y=qp_vals, mode="lines+markers",
        name=bid, line=dict(color=colors_rt[i % 9], width=2),
        marker=dict(size=8), legendgroup=bid,
        hovertemplate=f"{bid}<br>T=%{{x}} yr<br>Qp=%{{y:.2f}} mÃ‚Â³/s",
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=RETURN_PERIODS, y=q_vals, mode="lines+markers",
        name=bid, line=dict(color=colors_rt[i % 9], dash="dot", width=2),
        marker=dict(size=8), legendgroup=bid, showlegend=False,
        hovertemplate=f"{bid}<br>T=%{{x}} yr<br>Q=%{{y:.2f}} mm",
    ), row=1, col=2)

fig.update_xaxes(type="log", title_text="Return Period (yr)", row=1, col=1)
fig.update_xaxes(type="log", title_text="Return Period (yr)", row=1, col=2)
fig.update_yaxes(title_text="Peak Discharge (mÃ‚Â³/s)", row=1, col=1)
fig.update_yaxes(title_text="Runoff Depth Q (mm)", row=1, col=2)
fig.update_layout(title="Flood Frequency Curves Ã¢â‚¬â€ Pravara Subbasins",
                  template="plotly_white", height=500)
save_fig(fig, "14c_flood_frequency_curves")
print("\nÃ¢Å“â€¦ SECTION 14 complete.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
