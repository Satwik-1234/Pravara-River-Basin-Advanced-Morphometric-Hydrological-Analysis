# 📐 Complete Morphometric Parameters Reference

All parameters computed across Sections 3, 10, 11, 12, 13, 14, 15, 16, 17, and 18.

---

## Group 1 — Linear Parameters (Section 3)

> Describe the geometry and branching of the stream network

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Stream Order | u | Strahler (1952) hierarchical method | — | Strahler 1952 |
| Stream Number | Nu | Count of segments per order | — | Horton 1945 |
| Bifurcation Ratio | Rb | Nu / Nu+1 | — | Schumm 1956 |
| Mean Bifurcation Ratio | Rbm | Weighted mean of all Rb values | — | Strahler 1957 |
| Stream Length | Lu | Sum of segment lengths per order | km | Horton 1945 |
| Mean Stream Length | Lsm | Lu / Nu | km | Strahler 1964 |
| Stream Length Ratio | RL | Lsm(u) / Lsm(u-1) | — | Horton 1945 |
| Fineness Ratio | — | Lb / P | — | Smith 1950 |

**Interpretation:**
- **Rb**: Ranges 2–5 in natural basins. Low Rb (2–3) = low structural control; high Rb (4–5+) = strong geological control or elongated basin
- **Rbm**: > 4.0 suggests high flood peaks due to rapid concentration of runoff

---

## Group 2 — Areal Parameters (Section 3)

> Describe the shape and drainage characteristics of each subbasin

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Basin Area | A | Polygon area | km² | — |
| Basin Perimeter | P | Polygon perimeter | km | — |
| Basin Length | Lb | Longest dimension along main stream | km | Schumm 1956 |
| Basin Width | Wb | A / Lb | km | — |
| Drainage Density | Dd | ΣL / A | km/km² | Horton 1932 |
| Stream Frequency | Fs | N / A | streams/km² | Horton 1932 |
| Drainage Intensity | Di | Fs / Dd | — | Faniran 1968 |
| Elongation Ratio | Re | 2√(A/π) / Lb | — | Schumm 1956 |
| Circularity Ratio | Rc | 4πA / P² | — | Miller 1953 |
| Form Factor | Ff | A / Lb² | — | Horton 1932 |
| Compactness Coefficient | Cc | 0.2821 × P / √A | — | Gravelius 1914 |
| Infiltration Number | If | Dd × Fs | — | Faniran 1968 |
| Drainage Texture | T | Nu / P | streams/km | Smith 1950 |
| Lemniscate Ratio | k | Lb² / (4A/π) | — | Chorley et al. 1957 |
| RHO Coefficient | RHO | RL / Rb | — | Horton 1945 |
| Channel Maintenance | C | 1 / Dd | km²/km | Schumm 1956 |
| Overland Flow Length | Lg | 1 / (2 × Dd) | km | Horton 1945 |

**Interpretation:**
- **Re** (Elongation Ratio): 0.6–0.8 = elongated (good drainage); 0.8–1.0 = circular (more flood prone)
- **Rc** (Circularity): < 0.5 = elongated; 0.5–0.7 = oval; > 0.7 = circular
- **Dd** (Drainage Density): < 2 = coarse/permeable; 2–4 = moderate; > 4 = fine/impermeable/steep
- **Ff** (Form Factor): > 0.54 = circular (high peak, short response time); < 0.54 = elongated (lower flood peak)

---

## Group 3 — Relief Parameters (Section 3)

> Describe the vertical dimension and energy of the landscape

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Maximum Elevation | Hmax | Max DEM value in basin | m | — |
| Minimum Elevation | Hmin | Min DEM value (at outlet) | m | — |
| Basin Relief | H | Hmax − Hmin | m | Hadley & Schumm 1961 |
| Relief Ratio | Rh | H / Lb | m/km | Schumm 1956 |
| Gradient Ratio | Rg | (Hmax − Hmin) / Lb | — | Sreedevi et al. 2013 |
| Ruggedness Number | Rn | H × Dd | — | Strahler 1958 |
| Melton Ruggedness | MR | H / √A | m/km | Melton 1965 |
| Hypsometric Integral | HI | (Hmean − Hmin) / (Hmax − Hmin) | — | Strahler 1952 |
| Dissection Index | Di | H / Hmax | — | Singh & Dubey 1994 |
| Mean Slope | S̄ | Mean of slope raster (degrees) | ° | DEM-derived |
| Slope Std Dev | σs | Std dev of slope raster | ° | DEM-derived |

**Interpretation:**
- **HI** (Hypsometric Integral): > 0.60 = monadnock phase (youthful); 0.35–0.60 = equilibrium (mature); < 0.35 = peneplain (old)
- **Rn** (Ruggedness Number): High = high relief AND high drainage density = very susceptible to erosion
- **MR** (Melton): > 0.6 suggests debris flow potential

---

## Group 4 — Tectonic Activity Indices (Section 10)

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Basin Shape Index | Bs | Bl / Bw (at midpoint) | — | Bull & McFadden 1977 |
| Asymmetry Factor | Af | 100 × (Ar / At) | % | Hare & Gardner 1985 |
| Valley Floor Width-Height Ratio | Vf | 2Vfw / (Eld + Erd − 2Esc) | — | Bull & McFadden 1977 |
| Mountain Front Sinuosity | Smf | Lmf / Ls | — | Bull & McFadden 1977 |
| Hypsometric Integral | HI | (see above) | — | Strahler 1952 |

**Tectonic Activity Classification (El Hamdouni et al. 2008):**

| Class | Relative Tectonic Activity | Index Value |
|-------|--------------------------|-------------|
| 1 | Very High | < 1.5 |
| 2 | High | 1.5–2.5 |
| 3 | Moderate | 2.5–3.5 |
| 4 | Low | > 3.5 |

---

## Group 5 — Geomorphic Indices (Section 11)

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Stream Length Gradient Index | SL | (ΔH/ΔL) × L | m | Hack 1973 |
| Stream Power Index | SPI | As × tan(β) | — | Moore et al. 1991 |
| Topographic Wetness Index | TWI | ln(As / tan(β)) | — | Beven & Kirkby 1979 |
| SL Anomaly Index | k | SL / SL_average | — | Hack 1973 |

---

## Group 6 — Hydrological Parameters (Sections 14–18)

### Runoff Parameters (Section 14)

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Curve Number | CN | Slope-based proxy (70–85) | — | USDA-SCS 1985 |
| Potential Max Retention | S | 25400/CN − 254 | mm | USDA-SCS 1985 |
| Initial Abstraction | Ia | 0.2 × S | mm | USDA-SCS 1985 |
| Direct Runoff | Q | (P − Ia)² / (P + 0.8S) | mm | USDA-SCS 1985 |
| Time of Concentration (Kirpich) | Tc | 0.0195 × L^0.77 × S^−0.385 | min | Kirpich 1940 |
| Time of Concentration (SCS Lag) | Tc | tL / 0.6 | min | USDA-SCS 1985 |
| Peak Discharge (Rational) | Qp | C × i × A / 3.6 | m³/s | Lloyd-Davies 1906 |
| Rainfall Intensity | i_Tc | (P24/24) × (24/Tc_hr)^(2/3) | mm/hr | IMD IDF empirical |

### RUSLE Parameters (Section 15)

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Rainfall Erosivity | R | 650 × f(elevation) | MJ·mm/(ha·hr·yr) | Wischmeier & Smith 1978 |
| Soil Erodibility | K | Slope-based proxy (0.05–0.25) | t·ha·hr/(ha·MJ·mm) | Wischmeier & Smith 1978 |
| Slope-Length Gradient | LS | (As/22.13)^0.6 × (sinβ/0.0896)^1.3 | — | Moore et al. 1991 |
| Cover-Management | C | Slope-based proxy (0.15–0.55) | — | Wischmeier & Smith 1978 |
| Support Practice | P | Slope-based bunding proxy (0.55–1.0) | — | Wischmeier & Smith 1978 |
| Annual Soil Loss | A | R × K × LS × C × P | t/ha/yr | RUSLE |
| Sediment Delivery Ratio | SDR | 0.42 × A_km2^(−0.125) | — | Renfro 1975 |
| Annual Sediment Yield | Sy | A_gross × SDR | t/yr | — |

**USDA Soil Loss Classes:**

| Class | Range (t/ha/yr) | SWC Recommendation |
|-------|-----------------|-------------------|
| Slight | < 5 | No immediate action needed |
| Moderate | 5–15 | Conservation measures advisable |
| High | 15–30 | Check dams + contour trenches |
| Very High | 30–60 | Intensive treatment required |
| Severe | > 60 | Gully plugging + afforestation urgently |

### SWC Planning Parameters (Section 16)

| Parameter | Symbol | Description | Range |
|-----------|--------|-------------|-------|
| Check Dam Suitability Index | CDSI | Weighted score: order(30%) + area(25%) + slope(20%) + erosion(15%) + Vf(10%) | 0–10 |
| Water Harvesting Potential | WHP | Runoff volume × 0.4 harvest fraction | Mm³ |
| Contour Trench Suitability | CT | Slope-class × erosion × not-channel score | 0–1 |
| Percolation Potential | PP | TWI × FA × (1−slope) on flat terrain | 0–1 |

**CDSI Classes:**

| Score | Class |
|-------|-------|
| ≥ 7.5 | Very Suitable |
| 5.5–7.5 | Suitable |
| 3.5–5.5 | Moderately Suitable |
| < 3.5 | Poorly Suitable |

### Unit Hydrograph Parameters (Section 17)

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Lag Time | tL | Ct × (L × Lca)^0.3 | hr | Snyder 1938 |
| Storm Duration | tr | tL / 5.5 | hr | Snyder 1938 |
| Time to Peak | tp | tL + tr/2 | hr | Snyder 1938 |
| Peak Discharge (1mm) | Qp | 2.75 × Cp × A / tL | m³/s | Snyder 1938 |
| W50 | W50 | 2.14 / (Qp/A)^1.08 | hr | USBR 1960 |
| W75 | W75 | 1.22 / (Qp/A)^1.08 | hr | USBR 1960 |
| Base Time | tb | 5 × tp | hr | Linsley et al. |

**Calibration constants for Deccan Trap (this study):**
- Ct = 1.8 (lag coefficient)
- Cp = 0.6 (peak coefficient)

### Channel Hydraulics Parameters (Section 18)

| Parameter | Symbol | Formula | Unit | Reference |
|-----------|--------|---------|------|-----------|
| Bankfull Discharge | Q_bf | Q(1.5-yr return period) | m³/s | Wolman & Leopold 1957 |
| Bankfull Width | W_bf | 3.2 × Q^0.50 | m | Leopold & Maddock 1953 |
| Bankfull Depth | D_bf | 0.28 × Q^0.40 | m | Leopold & Maddock 1953 |
| Mean Velocity | V_bf | 1.12 × Q^0.10 | m/s | Leopold & Maddock 1953 |
| W/D Ratio | WD | W_bf / D_bf | — | — |
| Hydraulic Radius | R | A_cs / (W + 2D) | m | — |
| Bed Shear Stress | τ₀ | ρ × g × R × S | Pa | Du Boys 1879 |
| Critical Shear (Shields) | τ_c | θ_c × (ρ_s−ρ) × g × D50 | Pa | Shields 1936 |
| Total Stream Power | Ω | ρ × g × Q × S | W/m | Bagnold 1966 |
| Specific Stream Power | ω | Ω / W | W/m² | Bagnold 1966 |

**Channel Stability Classes:**

| Class | Criteria |
|-------|---------|
| Stable | WD < 12, τ₀ < τ_c, ω < ω_c (35 W/m²) |
| Marginally Stable | WD 12–20, slight excess shear/power |
| Unstable | WD 20–30, moderate excess shear/power |
| Highly Unstable | WD > 30, significant excess shear/power |

---

## Watershed Prioritization (Section 6)

### Compound Value Method

Parameters are classified into:
- **Category A** (high value = good drainage, low erosion): Rb, Dd, Fs, T, Di
- **Category B** (high value = problematic, more degradation): Re, Rc, Ff, Bs, HI

Priority rank:
1. Compute mean value for each category per subbasin
2. Compound value = (mean_A + mean_B) / 2
3. Lowest compound value → Highest priority (needs most treatment)

| Priority | Compound Value | Treatment Urgency |
|----------|---------------|------------------|
| High | Lowest | Immediate intervention |
| Medium | Moderate | Medium-term planning |
| Low | Highest | Maintenance/monitoring |
