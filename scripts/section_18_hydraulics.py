# SECTION 18 Ã¢â‚¬â€ STREAM CHANNEL HYDRAULICS & STABILITY ANALYSIS
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n" + "=" * 70)
print("SECTION 18 Ã¢â‚¬â€ STREAM CHANNEL HYDRAULICS & STABILITY")
print("(Bankfull Discharge, Shear Stress, Stream Power, Stability Index)")
print("=" * 70)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. HYDRAULIC GEOMETRY Ã¢â‚¬â€ Leopold & Maddock (1953) Regional Curves
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# For Indian semi-arid Deccan rivers, regional hydraulic geometry:
#   w = a Ãƒâ€” Q^b     (bankfull width, b Ã¢â€°Ë† 0.50)
#   d = c Ãƒâ€” Q^f     (bankfull depth, f Ã¢â€°Ë† 0.40)
#   v = k Ãƒâ€” Q^m     (mean velocity, m Ã¢â€°Ë† 0.10)
# Calibrated coefficients for Deccan Trap basalt basins:
#   a=3.2, b=0.50; c=0.28, f=0.40; k=1.12, m=0.10
# Q_bankfull estimated as Q(1.5-yr) Ã¢â‚¬â€ typical recurrence for bankfull stage

print("\n[18-A] Bankfull Discharge & Hydraulic Geometry...")

# Bankfull discharge: Q(1.5-yr) via Gumbel interpolation
T_bf = 1.5
y_bf = -np.log(-np.log(1 - 1/T_bf))
P_bf_annual = u_g + alpha_g * y_bf          # annual rainfall
P_bf_24hr   = P_bf_annual * DAILY_FRACTION

HG_ROWS = []

for _, row in gdf_sub.iterrows():
    bid   = row["basin_id"]
    A_km2 = df_areal.loc[bid, "Area_km2"]
    L_km  = df_areal.loc[bid, "Basin_Length_km"]
    CN    = df_runoff.loc[bid, "CN_mean"] if bid in df_runoff.index else 78.0
    Tc_hr = df_tc.loc[bid, "Tc_hr"] if bid in df_tc.index else 2.0

    # Bankfull Q (1.5-yr)
    Q_bf_mm = float(scscn_runoff(P_bf_24hr, CN))
    C_bf    = float(runoff_coeff(P_bf_24hr, CN))
    i_bf    = (P_bf_24hr / 24.0) * (24.0 / Tc_hr) ** (2.0/3.0)
    Q_bf    = C_bf * i_bf * A_km2 / 3.6   # mÃ‚Â³/s

    # Hydraulic geometry (Leopold-Maddock regional coefficients Ã¢â‚¬â€ Deccan)
    a_w, b_w = 3.20, 0.50   # width
    a_d, b_d = 0.28, 0.40   # depth
    a_v, b_v = 1.12, 0.10   # velocity

    W_bf = a_w * (Q_bf ** b_w)   # bankfull width [m]
    D_bf = a_d * (Q_bf ** b_d)   # bankfull depth [m]
    V_bf = a_v * (Q_bf ** b_v)   # bankfull velocity [m/s]

    # Cross-sectional area and hydraulic radius
    A_cs = W_bf * D_bf * 0.80   # assuming trapezoidal Ãƒâ€” efficiency factor
    R_hyd = A_cs / (W_bf + 2*D_bf)  # hydraulic radius [m]

    # Channel bed slope from DEM relief and basin length
    H_m    = df_relief.loc[bid, "Basin_Relief_H_m"] if bid in df_relief.index else 100.0
    S_ch   = H_m / (L_km * 1000.0)   # dimensionless

    # Manning's n (estimated for Deccan basalt-lined channels)
    # Rocky channels: n Ã¢â€°Ë† 0.035Ã¢â‚¬â€œ0.050; alluvial gravel: n Ã¢â€°Ë† 0.025Ã¢â‚¬â€œ0.035
    n_mann = 0.038 + 0.002 * (1 - min(S_ch / 0.01, 1))  # slightly rougher on steeper slopes

    # Manning's Q (check)
    Q_mann = (1.0 / n_mann) * A_cs * (R_hyd ** (2/3)) * (S_ch ** 0.5)

    # Ã¢â€â‚¬Ã¢â€â‚¬ Shear stress Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    # Ãâ€žÃ¢â€šâ‚¬ = ÃÂ Ãƒâ€” g Ãƒâ€” R Ãƒâ€” S  [N/mÃ‚Â² = Pa]
    rho_water = 1000.0   # kg/mÃ‚Â³
    g         = 9.81     # m/sÃ‚Â²
    tau0      = rho_water * g * R_hyd * S_ch   # bed shear stress [Pa]

    # Critical shear stress Ã¢â‚¬â€ Shields (D50 Ã¢â€°Ë† 15mm for basalt gravel)
    # Ãâ€ž_c = ÃŽÂ¸_c Ãƒâ€” (ÃÂ_s - ÃÂ) Ãƒâ€” g Ãƒâ€” D50
    D50_m    = 0.015    # median grain size [m] Ã¢â‚¬â€ basaltic gravel
    rho_s    = 2650.0   # sediment density [kg/mÃ‚Â³]
    theta_c  = 0.047    # Shields parameter for D50 >10mm
    tau_c    = theta_c * (rho_s - rho_water) * g * D50_m   # critical shear [Pa]

    excess_shear = tau0 - tau_c   # positive = bed mobility

    # Ã¢â€â‚¬Ã¢â€â‚¬ Stream power Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    # ÃŽÂ© = ÃÂ Ãƒâ€” g Ãƒâ€” Q Ãƒâ€” S   [W/m]   total stream power
    # Ãâ€° = ÃŽÂ© / w            [W/mÃ‚Â²]  specific (unit width) stream power
    Omega_total   = rho_water * g * Q_bf * S_ch
    omega_spec    = Omega_total / W_bf   # W/mÃ‚Â²

    # Critical specific stream power (Bagnold 1966):
    # Ãâ€°_c Ã¢â€°Ë† 35.0 W/mÃ‚Â² for coarse sandÃ¢â‚¬â€œgravel in semi-arid rivers
    omega_c = 35.0
    omega_excess = omega_spec - omega_c

    # Ã¢â€â‚¬Ã¢â€â‚¬ Channel stability index Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    # Regime theory: stable channel has W/D (aspect ratio) within bounds
    # For Deccan semi-arid channels: W/D < 15 = stable; 15Ã¢â‚¬â€œ30 = marginally stable
    WD_ratio = W_bf / max(D_bf, 0.01)

    def channel_stability(WD, excess_shear_val, omega_exc):
        """Combined channel stability assessment."""
        score = 0
        if WD < 12:          score += 3   # narrow deep = stable
        elif WD < 20:        score += 2
        elif WD < 30:        score += 1
        if excess_shear_val < 0:  score += 3  # sub-critical shear = stable
        elif excess_shear_val < 5: score += 2
        elif excess_shear_val < 15: score += 1
        if omega_exc < 0:    score += 3   # sub-critical stream power
        elif omega_exc < 20: score += 2
        elif omega_exc < 50: score += 1
        if score >= 7:  return "Stable"
        if score >= 5:  return "Marginally Stable"
        if score >= 3:  return "Unstable"
        return "Highly Unstable"

    stab_class = channel_stability(WD_ratio, excess_shear, omega_excess)

    # Ã¢â€â‚¬Ã¢â€â‚¬ Sediment transport capacity (Einstein-Brown simplified) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    # Using unit stream power approach: Qs Ã¢Ë†Â Ãâ€°_excessÃ‚Â² for Ãâ€° > Ãâ€°_c
    if omega_excess > 0:
        Qs_relative = (omega_excess / omega_c) ** 2.0  # relative transport capacity
    else:
        Qs_relative = 0.0

    HG_ROWS.append({
        "basin_id"              : bid,
        "Q_bankfull_m3s"        : round(Q_bf, 3),
        "W_bankfull_m"          : round(W_bf, 2),
        "D_bankfull_m"          : round(D_bf, 2),
        "V_bankfull_ms"         : round(V_bf, 3),
        "WD_ratio"              : round(WD_ratio, 2),
        "R_hydraulic_m"         : round(R_hyd, 3),
        "Channel_Slope_S"       : round(S_ch, 6),
        "Manning_n"             : round(n_mann, 4),
        "Q_Manning_m3s"         : round(Q_mann, 3),
        "Shear_Stress_Pa"       : round(tau0, 3),
        "Critical_Shear_Pa"     : round(tau_c, 3),
        "Excess_Shear_Pa"       : round(excess_shear, 3),
        "Stream_Power_total_Wm" : round(Omega_total, 2),
        "Stream_Power_spec_Wm2" : round(omega_spec, 3),
        "Excess_Sp_Power_Wm2"   : round(omega_excess, 3),
        "Transport_Capacity_rel": round(Qs_relative, 3),
        "Channel_Stability"     : stab_class,
    })
    print(f"  {bid}: Q_bf={Q_bf:.2f} mÃ‚Â³/s | W={W_bf:.1f}m | D={D_bf:.2f}m | "
          f"Ãâ€ž={tau0:.1f}Pa | Ãâ€°={omega_spec:.1f} W/mÃ‚Â² | {stab_class}")

df_hg = pd.DataFrame(HG_ROWS).set_index("basin_id")
df_hg.to_csv(os.path.join(HYD_DIR, "channel_hydraulics.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. STREAM POWER INDEX PER ORDER Ã¢â‚¬â€ GEOMORPHIC WORK BY ORDER
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[18-B] Stream power analysis per Strahler order...")

# For each order, compute mean gradient, estimated Q, and stream power
ORDER_POWER_ROWS = []
orders_all = sorted(gdf_so[ORDER_COL].unique())

for o in orders_all:
    segs = gdf_so[gdf_so[ORDER_COL] == o]
    n_segs  = len(segs)
    L_total_m = segs.geometry.length.sum()
    L_mean_m  = segs.geometry.length.mean()

    # Sample slope at each segment
    seg_slopes = []
    for _, seg in segs.iterrows():
        s = sample_slope_at_segment(seg.geometry, SLOPE_ARR, DEM_TRANSFORM)
        if s is not None and not np.isnan(s):
            seg_slopes.append(s)
    mean_slope_deg = float(np.nanmean(seg_slopes)) if seg_slopes else 5.0
    S_order = np.tan(np.radians(max(mean_slope_deg, 0.1)))

    # Estimate Q for this order using Hack's (1957) scaling:
    # Q_order Ã¢â€°Ë† Q_max_basin Ãƒâ€” (Dd_order / Dd_total)
    # Simpler: Q scales with segment length proxy
    Q_order_proxy = 0.02 * (o ** 2.5) * np.mean(
        [df_runoff.loc[bid, "Q_25yr_mm"] if bid in df_runoff.index else 25
         for bid in gdf_sub["basin_id"]]) * 1e-3  # rough proxy

    omega_order = rho_water * g * Q_order_proxy * S_order / max(
        3.2 * (Q_order_proxy ** 0.5), 0.5)  # W/mÃ‚Â²

    ORDER_POWER_ROWS.append({
        "Strahler_Order"     : o,
        "N_segments"         : n_segs,
        "Total_Length_km"    : round(L_total_m / 1000, 2),
        "Mean_Seg_Length_m"  : round(L_mean_m, 1),
        "Mean_Slope_deg"     : round(mean_slope_deg, 2),
        "Mean_Slope_frac"    : round(S_order, 5),
        "Qproxy_m3s"         : round(Q_order_proxy, 4),
        "StreamPower_Wm2"    : round(omega_order, 2),
    })
    print(f"  Order {o}: N={n_segs:4d} | L_tot={L_total_m/1000:.1f} km | "
          f"S_mean={mean_slope_deg:.2f}Ã‚Â° | Ãâ€°Ã¢â€°Ë†{omega_order:.2f} W/mÃ‚Â²")

df_order_power = pd.DataFrame(ORDER_POWER_ROWS)
df_order_power.to_csv(os.path.join(HYD_DIR, "stream_order_power.csv"), index=False)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. COMPREHENSIVE MAPS & PLOTLY CHARTS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[18-C] Generating hydraulics maps and charts...")

# Bankfull width map (choropleth per basin)
fig, ax, utm_ext = base_axes("Bankfull Channel Width & Hydraulic Geometry\n"
                              "Leopold-Maddock Regional Curves (Deccan Trap)")
gdf_hg = gdf_sub.merge(df_hg.reset_index(), on="basin_id", how="left")
gdf_hg.plot(column="W_bankfull_m", ax=ax, cmap="YlOrRd", legend=True,
            alpha=0.75, zorder=2, edgecolor="black", linewidth=1.2,
            legend_kwds={"label":"Bankfull Width (m)","shrink":0.75})
for _, r in gdf_hg.iterrows():
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    ax.text(cx, cy,
            f"{r['basin_id']}\nW={r['W_bankfull_m']:.1f}m\nD={r['D_bankfull_m']:.2f}m",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
# Stream network coloured by order
for o in orders_all:
    segs = gdf_so[gdf_so[ORDER_COL] == o]
    lw   = 0.4 + o * 0.6
    segs.plot(ax=ax, linewidth=lw, color=plt.cm.Blues(0.3 + o * 0.15), zorder=5, alpha=0.9)
finalize_and_save(fig, ax, utm_ext, "18a_bankfull_hydraulics.png")

# Channel stability map
stab_colors = {"Stable": "#1a9641", "Marginally Stable": "#fdae61",
               "Unstable": "#d73027", "Highly Unstable": "#7f0000"}
fig, ax, utm_ext = base_axes("Channel Stability Classification Map\n"
                              "(Shear Stress, Stream Power, W/D Ratio)")
for _, r in gdf_hg.iterrows():
    col = stab_colors.get(r["Channel_Stability"], "grey")
    gpd.GeoDataFrame([r], geometry="geometry", crs=gdf_sub.crs).plot(
        ax=ax, color=col, edgecolor="black", linewidth=1.2, alpha=0.80, zorder=3)
    cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
    ax.text(cx, cy, f"{r['basin_id']}\n{r['Channel_Stability']}\nÃâ€ž={r['Shear_Stress_Pa']:.1f}Pa",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")])
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.7, alpha=0.5, zorder=8)
patches_st = [mpatches.Patch(color=v, label=k) for k, v in stab_colors.items()]
ax.legend(handles=patches_st, loc="lower left", fontsize=8,
          title="Channel Stability", title_fontsize=9, framealpha=0.9)
finalize_and_save(fig, ax, utm_ext, "18b_channel_stability.png")

# Plotly: stream power vs shear stress bubble
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Stream Power vs Shear Stress per Basin",
                                    "Stream Power by Strahler Order"])
stab_c_map = {"Stable":"#1a9641","Marginally Stable":"#fdae61",
              "Unstable":"#d73027","Highly Unstable":"#7f0000"}
for i, (bid, r) in enumerate(df_hg.iterrows()):
    c = stab_c_map.get(r["Channel_Stability"], "grey")
    fig.add_trace(go.Scatter(
        x=[r["Shear_Stress_Pa"]], y=[r["Stream_Power_spec_Wm2"]],
        mode="markers+text", text=[bid], textposition="top center",
        marker=dict(size=r["W_bankfull_m"] * 2.5, color=c, opacity=0.85,
                    line=dict(width=1, color="black")),
        name=bid,
        hovertemplate=(f"<b>{bid}</b><br>"
                       f"Ãâ€ž = {r['Shear_Stress_Pa']:.2f} Pa<br>"
                       f"Ãâ€° = {r['Stream_Power_spec_Wm2']:.2f} W/mÃ‚Â²<br>"
                       f"Q_bf = {r['Q_bankfull_m3s']:.2f} mÃ‚Â³/s<br>"
                       f"Stability: {r['Channel_Stability']}"),
    ), row=1, col=1)

# Order power bar
fig.add_trace(go.Bar(
    x=df_order_power["Strahler_Order"].tolist(),
    y=df_order_power["StreamPower_Wm2"].tolist(),
    marker_color=px.colors.sequential.Blues[2:],
    text=[f"{v:.2f}" for v in df_order_power["StreamPower_Wm2"]],
    textposition="outside",
    hovertemplate="Order %{x}<br>Ãâ€°=%{y:.2f} W/mÃ‚Â²",
    name="Stream Power",
), row=1, col=2)

# Critical stream power line
fig.add_hline(y=35, line_dash="dash", line_color="red",
              annotation_text="Ãâ€°_c = 35 W/mÃ‚Â² (critical)", row=1, col=1)
fig.add_hline(y=35, line_dash="dash", line_color="red", row=1, col=2)

fig.update_xaxes(title_text="Bed Shear Stress Ãâ€žÃ¢â€šâ‚¬ (Pa)", row=1, col=1)
fig.update_yaxes(title_text="Specific Stream Power Ãâ€° (W/mÃ‚Â²)", row=1, col=1)
fig.update_xaxes(title_text="Strahler Order", row=1, col=2)
fig.update_yaxes(title_text="Ãâ€° (W/mÃ‚Â²)", row=1, col=2)
fig.update_layout(title="Stream Channel Hydraulics Ã¢â‚¬â€ Pravara River Basin",
                  template="plotly_white", height=520)
save_fig(fig, "18c_stream_power_hydraulics")

# Plotly: Hydraulic geometry log-log plots
fig = make_subplots(rows=1, cols=3,
                    subplot_titles=["Bankfull Width (W-Q)", "Bankfull Depth (D-Q)",
                                    "Bankfull Velocity (V-Q)"])
for i, (bid, r) in enumerate(df_hg.iterrows()):
    c = px.colors.qualitative.Set1[i % 9]
    fig.add_trace(go.Scatter(
        x=[r["Q_bankfull_m3s"]], y=[r["W_bankfull_m"]],
        mode="markers+text", text=[bid], textposition="top center",
        marker=dict(size=12, color=c), name=bid, legendgroup=bid,
        hovertemplate=f"{bid}<br>Q={r['Q_bankfull_m3s']:.2f} mÃ‚Â³/s<br>W={r['W_bankfull_m']:.2f} m",
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=[r["Q_bankfull_m3s"]], y=[r["D_bankfull_m"]],
        mode="markers", marker=dict(size=12, color=c), name=bid,
        legendgroup=bid, showlegend=False,
        hovertemplate=f"{bid}<br>Q={r['Q_bankfull_m3s']:.2f} mÃ‚Â³/s<br>D={r['D_bankfull_m']:.2f} m",
    ), row=1, col=2)
    fig.add_trace(go.Scatter(
        x=[r["Q_bankfull_m3s"]], y=[r["V_bankfull_ms"]],
        mode="markers", marker=dict(size=12, color=c), name=bid,
        legendgroup=bid, showlegend=False,
        hovertemplate=f"{bid}<br>Q={r['Q_bankfull_m3s']:.2f} mÃ‚Â³/s<br>V={r['V_bankfull_ms']:.3f} m/s",
    ), row=1, col=3)

# Leopold-Maddock regional curves (dashed lines)
Q_range = np.logspace(-1, 2, 50)
fig.add_trace(go.Scatter(x=Q_range.tolist(), y=(3.20*Q_range**0.50).tolist(),
    mode="lines", line=dict(dash="dash",color="grey",width=1.5), name="W=3.2Q^0.5",
    hoverinfo="skip"), row=1, col=1)
fig.add_trace(go.Scatter(x=Q_range.tolist(), y=(0.28*Q_range**0.40).tolist(),
    mode="lines", line=dict(dash="dash",color="grey",width=1.5), name="D=0.28Q^0.4",
    showlegend=False, hoverinfo="skip"), row=1, col=2)
fig.add_trace(go.Scatter(x=Q_range.tolist(), y=(1.12*Q_range**0.10).tolist(),
    mode="lines", line=dict(dash="dash",color="grey",width=1.5), name="V=1.12Q^0.1",
    showlegend=False, hoverinfo="skip"), row=1, col=3)

for col_i, ylabel in [(1,"Width W (m)"), (2,"Depth D (m)"), (3,"Velocity V (m/s)")]:
    fig.update_xaxes(type="log", title_text="Bankfull Q (mÃ‚Â³/s)", row=1, col=col_i)
    fig.update_yaxes(type="log", title_text=ylabel, row=1, col=col_i)

fig.update_layout(title="Hydraulic Geometry Ã¢â‚¬â€ At-a-Station Relationships (log-log)<br>"
                        "<sup>Leopold-Maddock (1953) regional curves for Deccan Trap basalt</sup>",
                  template="plotly_white", height=500)
save_fig(fig, "18d_hydraulic_geometry_loglog")

print("\nÃ¢Å“â€¦ SECTION 18 complete.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  FINAL CONSOLIDATED OUTPUT TABLE (Sections 14Ã¢â‚¬â€œ18)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n" + "=" * 70)
print("CONSOLIDATED HYDROLOGY & SWC RESULTS TABLE")
print("=" * 70)

df_consolidated = pd.concat([
    df_runoff[["CN_mean","Q_10yr_mm","Q_25yr_mm","Q_100yr_mm",
               "Vol_25yr_Mm3"]],
    df_tc[["Tc_Avg_min","Tc_hr","Qp_10yr_m3s","Qp_25yr_m3s","Qp_100yr_m3s"]],
    df_rusle[["A_mean_t_ha_yr","SDR","Sed_Yield_t_yr","Loss_Class_Mode"]],
    df_whp[["WHP_25yr_Mm3","Potential_CheckDams_N","SWC_Priority"]],
    df_suh[["tp_hr","Qp_1mm_m3s","W50_hr","W75_hr","tb_hr"]],
    df_hg[["Q_bankfull_m3s","W_bankfull_m","D_bankfull_m",
           "Shear_Stress_Pa","Stream_Power_spec_Wm2","Channel_Stability"]],
], axis=1)

df_consolidated.to_csv(os.path.join(TABLES_DIR, "hydrology_SWC_consolidated.csv"))

print("\nCONSOLIDATED RESULTS:")
print(df_consolidated.to_string())

# Print to output summary
print("\n" + "Ã¢â€â‚¬"*70)
print("SUMMARY OF KEY SOIL & WATER CONSERVATION METRICS")
print("Ã¢â€â‚¬"*70)
for bid in df_consolidated.index:
    r = df_consolidated.loc[bid]
    print(f"\n  Ã¢â€Å’Ã¢â€â‚¬ {bid} {'Ã¢â€â‚¬'*40}")
    print(f"  Ã¢â€â€š  CN={r['CN_mean']:.1f} | Tc={r['Tc_Avg_min']:.1f} min | "
          f"Q25yr={r['Q_25yr_mm']:.1f}mm | Qp25={r['Qp_25yr_m3s']:.2f}mÃ‚Â³/s")
    print(f"  Ã¢â€â€š  Soil loss={r['A_mean_t_ha_yr']:.1f} t/ha/yr ({r['Loss_Class_Mode']}) | "
          f"Sed.Yield={r['Sed_Yield_t_yr']:.0f} t/yr")
    print(f"  Ã¢â€â€š  WHP={r['WHP_25yr_Mm3']:.4f}MmÃ‚Â³ | ~{r['Potential_CheckDams_N']} check dams | "
          f"SWC priority: {r['SWC_Priority']}")
    print(f"  Ã¢â€â€š  Bankfull Q={r['Q_bankfull_m3s']:.2f}mÃ‚Â³/s | "
          f"Ãâ€ž={r['Shear_Stress_Pa']:.1f}Pa | Ãâ€°={r['Stream_Power_spec_Wm2']:.1f}W/mÃ‚Â² | "
          f"Stability: {r['Channel_Stability']}")
    print(f"  Ã¢â€â€Ã¢â€â‚¬ UH: tp={r['tp_hr']:.2f}hr | Qp(1mm)={r['Qp_1mm_m3s']:.4f}mÃ‚Â³/s | "
          f"W50={r['W50_hr']:.2f}hr | tb={r['tb_hr']:.2f}hr")

print("\n" + "=" * 70)
print("ALL SECTIONS 14Ã¢â‚¬â€œ18 COMPLETE")
print("=" * 70)
print(f"\n  Output files:")
all_new_files = (
    [(HYD_DIR,  f) for f in os.listdir(HYD_DIR)] +
    [(SWC_DIR,  f) for f in os.listdir(SWC_DIR)] +
    [(UHG_DIR,  f) for f in os.listdir(UHG_DIR)] +
    [(HYD_MAPS, f) for f in os.listdir(HYD_MAPS) if os.path.exists(HYD_MAPS)] +
    [(SWC_MAPS, f) for f in os.listdir(SWC_MAPS) if os.path.exists(SWC_MAPS)]
)
for d, f in sorted(all_new_files):
    fpath = os.path.join(d, f)
    size  = os.path.getsize(fpath) / 1024 if os.path.exists(fpath) else 0
    print(f"    {fpath.replace(OUT_DIR,''):<60s}  {size:>8.1f} KB")

print(f"\n  Total new maps   : 9 (14a, 14b, 15a, 15b, 16a, 16b, 18a, 18b)")
print(f"  Total new CSVs   : 9")
print(f"  Plotly HTML      : 12 interactive charts")
print(f"  Shapefile        : checkdam_suitability.shp")

import os, zipfile
from datetime import datetime

OUT_DIR     = "E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/outputs/"
EXPORT_NAME = f"morphometric_outputs_{datetime.now().strftime('%Y%m%d_%H%M')}.zip"
EXPORT_PATH = f"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/outputs/{EXPORT_NAME}"

print("Ã°Å¸â€œÂ¦ Zipping all outputs...")
with zipfile.ZipFile(EXPORT_PATH, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, fnames in os.walk(OUT_DIR):
        for fname in fnames:
            full_path = os.path.join(root, fname)
            arc_name  = os.path.relpath(full_path, "E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/outputs/")
            zf.write(full_path, arc_name)

size_mb = os.path.getsize(EXPORT_PATH) / 1e6
print(f"Ã¢Å“â€¦ Zipped: {EXPORT_NAME}  ({size_mb:.1f} MB)")

# Print contents summary
print("\nÃ°Å¸â€œâ€š Contents:")
with zipfile.ZipFile(EXPORT_PATH, 'r') as zf:
    for name in sorted(zf.namelist()):
        info = zf.getinfo(name)
        print(f"  {name:<70s}  {info.file_size/1024:>8.1f} KB")

print("\nÃ¢Â¬â€¡Ã¯Â¸Â  Starting download...")
files.download(EXPORT_PATH)

