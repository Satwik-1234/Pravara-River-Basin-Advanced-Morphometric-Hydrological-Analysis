# 📊 Results Interpretation Guide

How to read and act on the outputs from each section of the analysis.

---

## Section 3 — Morphometric Results (`outputs/tables/`)

### `morphometry_master.csv`
The master table with all parameters for all subbasins. Start here.

**Red flags to look for:**
- **High Rb (> 4.5):** Geological control on drainage; subbasin may exhibit flashy floods
- **High Dd (> 4 km/km²):** Impermeable soils, thin vegetation cover, high runoff
- **Low Re (< 0.5):** Strongly elongated — high peak discharge, short response time
- **Low Rc (< 0.4):** Elongated basin — flood wave elongated in time, but concentrated in space
- **High Rn (> 0.5):** Rugged, highly erodible terrain

---

## Section 6 — Watershed Prioritization

### Priority Rank Map + Table (`outputs/maps/06_priority_map.png`)

- **Priority 1 (Highest):** This subbasin is most degraded and needs immediate treatment. Typically has: high drainage density, high stream frequency, low form factor, high relief
- **Priority 2:** Moderate degradation. Plan treatment within 3–5 years
- **Priority 3 (Lowest):** Relatively stable. Maintain existing land use

> Action: Allocate NABARD/MGNREGS watershed treatment funds in priority order

---

## Section 10 — Tectonic Activity

### Tectonic Class Map (`outputs/maps/10_tectonic_class.png`)

| Class | Meaning for SWC |
|-------|----------------|
| Very High (1) | Active tectonic uplift — avoid large dams; use small distributed structures |
| High (2) | Moderate tectonic activity — slope failures are a risk; stabilise gullies first |
| Moderate (3) | Normal geomorphic processes dominate |
| Low (4) | Stable landscape — large check dams and percolation tanks are safe |

**Af (Asymmetry Factor):**
- 50% = perfectly symmetric drainage
- > 60% or < 40% = tilting (tectonic or lithological)
- Indicates which side of the basin is more erosion-prone

---

## Section 11 — TWI & SPI

### TWI Map (`outputs/maps/11_TWI.png`)
- **High TWI zones (> 8):** Flat, low areas where runoff converges → ideal for percolation ponds
- **Low TWI zones (< 4):** Ridges and steep slopes → runoff source areas → target for contour trenches

### SPI Map (`outputs/maps/11_SPI.png`)
- **High SPI:** Indicates high erosive power of the stream at this location → prioritise check dams here

---

## Section 13 — Flood Hazard

### Flood Hazard Map (`outputs/maps/13_flood_hazard.png`)

Composite score from:
- High drainage density
- Low form factor (elongated)
- High bifurcation ratio
- High relief ratio
- High ruggedness

> **High hazard zones** should be incorporated into local disaster risk reduction plans. These are the first subbasins to treat in flash flood contexts.

---

## Section 14 — Runoff Results

### Key CSV: `outputs/hydrology/runoff_scscn.csv`

| Column | Meaning |
|--------|---------|
| `CN_mean` | Average curve number — higher = more runoff, less infiltration |
| `Q_25yr_mm` | Direct runoff depth in mm from a 25-year return period storm |
| `Vol_25yr_Mm3` | Total runoff volume (million cubic metres) from same event |
| `C_25yr` | Runoff coefficient — fraction of rainfall becoming runoff |

### Key CSV: `outputs/hydrology/time_of_concentration_peak_discharge.csv`

| Column | Meaning |
|--------|---------|
| `Tc_Avg_min` | Time of concentration — how quickly runoff peaks after rainfall |
| `Qp_25yr_m3s` | Peak discharge (m³/s) for 25-year event |

> **Design guideline:** For check dam spillway design, use Qp from the 25-yr event. For road culverts, use Qp from the 50-yr event.

---

## Section 15 — RUSLE Erosion Results

### Key CSV: `outputs/hydrology/RUSLE_soil_erosion.csv`

| Column | Meaning |
|--------|---------|
| `A_mean_t_ha_yr` | Mean annual soil loss (tonnes/hectare/year) |
| `A_p95_t_ha_yr` | 95th percentile — the most erosive areas |
| `Gross_Erosion_t_yr` | Total gross erosion from the entire subbasin |
| `SDR` | Sediment Delivery Ratio — fraction of eroded soil reaching the stream |
| `Sed_Yield_t_yr` | Actual sediment reaching the outlet per year |
| `Loss_Class_Mode` | Most common erosion class in the basin |

### Soil Loss Map (`outputs/maps/15b_RUSLE_soil_loss.png`)

Interpret the 5 colour zones:
- 🟢 **Green (< 5 t/ha/yr):** Tolerable — maintain current land use
- 🟡 **Yellow (5–15 t/ha/yr):** Moderate — introduce contour bunding, check dams on higher-order streams
- 🟠 **Orange (15–30 t/ha/yr):** High — dense contour trenching, 1st–2nd order check dams urgent
- 🔴 **Red (30–60 t/ha/yr):** Very High — gully plugs + afforestation immediately
- ⬛ **Dark Red (> 60 t/ha/yr):** Severe — full watershed treatment; possible badland reclamation

---

## Section 16 — Conservation Planning

### Check Dam Suitability Map (`outputs/maps/16a_checkdam_suitability.png`)

- **Green segments (Very Suitable / CDSI ≥ 7.5):** Build check dams here first
- **Yellow segments (Suitable / CDSI 5.5–7.5):** Second priority
- **Orange / Grey:** Not economically viable for check dams; consider contour trenches instead

### Treatment Zone Map (`outputs/maps/16b_SWC_treatment_zones.png`)

| Colour | Treatment |
|--------|-----------|
| Blue shading | Percolation pond / farm pond location zone |
| Orange shading | Contour trench zone (slope 3–30°) |
| Green lines | Recommended check dam reaches |

### Key CSV: `outputs/conservation/conservation_potential.csv`

| Column | Meaning |
|--------|---------|
| `WHP_25yr_Mm3` | Water harvesting potential in million m³ from a 25-yr event |
| `Potential_CheckDams_N` | Estimated number of viable check dam sites |
| `SWC_Priority` | High / Moderate / Low — based on erosion severity |

---

## Section 17 — Unit Hydrograph

### Hydrograph Plot (`outputs/unit_hydrograph/17_unit_hydrographs.png`)

- **X-axis:** Time in hours after storm begins
- **Y-axis:** Discharge in m³/s
- **Shaded band:** 50% and 75% of peak discharge — used to shape spillway design hydrographs
- **Qp (diamond marker):** Peak discharge — the critical design value
- **tp:** Time to peak — for short tp, the basin is flashy; design must accommodate rapid filling

> **W50/W75 widths** are used to construct the full design hydrograph for dam spillway sizing per IS:5477 and Bureau of Indian Standards guidelines.

---

## Section 18 — Channel Hydraulics

### Stability Map (`outputs/maps/18b_channel_stability.png`)

| Colour | Class | Meaning |
|--------|-------|---------|
| Green | Stable | Channel in equilibrium with current flows |
| Orange | Marginally Stable | Monitor; avoid disturbance (construction, mining) |
| Red | Unstable | Active bed incision or bank erosion; needs bioengineering |
| Dark Red | Highly Unstable | Dangerous; avoid encroachment; gully control urgent |

### Stream Power Chart (`outputs/html/18c_stream_power_hydraulics.html`)

- Points **above** the ω_c = 35 W/m² threshold line → active sediment transport
- Points **below** → sediment deposition zones → good sites for percolation structures

### Hydraulic Geometry Plots (`outputs/html/18d_hydraulic_geometry_loglog.html`)

Points lying **above the dashed line** (regional curve) → channel is wider/deeper than expected → possible bank erosion or flow concentration.

---

## Overall Basin Assessment Summary

After running all sections, read:

```
outputs/tables/hydrology_SWC_consolidated.csv
```

This is the **one-stop summary table** with all key results per subbasin. Compare subbasins on:
1. Which has highest soil loss?
2. Which has highest peak flood discharge?
3. Which is most unstable hydraulically?
4. Which has the most check dam potential?
5. Which needs highest SWC investment?

The **SWC Priority** column directly answers question 5 for treatment planning purposes.
