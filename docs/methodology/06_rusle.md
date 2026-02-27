# RUSLE Methodology — Pravara Basin

## Overview

The **Revised Universal Soil Loss Equation (RUSLE)** estimates mean annual soil loss:

```
A = R × K × LS × C × P   [tonnes/hectare/year]
```

All five factors are computed as **pixel-level rasters** at 30m resolution, then aggregated per subbasin.

---

## R — Rainfall Erosivity Factor

**Units:** MJ·mm / (ha·hr·yr)

The R-factor represents the total kinetic energy of rainfall events that cause erosion. For the Pravara basin (Ahmednagar District, Maharashtra):

- Regional base value: **R₀ = 650 MJ·mm/(ha·hr·yr)**
- Source: Maharashtra rainfall erosivity map (IMD monsoon statistics)
- Orographic adjustment applied: `R = 650 × (1 + 0.05 × (z − z̄) / σz)`
  - Higher elevations receive slightly higher intensity rainfall in the Western Ghats foothills
  - Clamped to range 400–1000

---

## K — Soil Erodibility Factor

**Units:** t·ha·hr / (ha·MJ·mm)

The K-factor depends on soil texture, organic matter, structure, and permeability. Since no NBSS&LUP soil map is available at this scale, K is estimated from slope as a proxy for soil depth/type:

| Slope Class | K Value | Soil Type (Deccan Trap) |
|-------------|---------|------------------------|
| < 3° | 0.25 | Deep Vertisol (expansive clay) |
| 3–8° | 0.20 | Vertic Inceptisol |
| 8–15° | 0.15 | Shallow Alfisol |
| 15–25° | 0.10 | Lithic Inceptisol (stony) |
| > 25° | 0.05 | Rock outcrop / talus |

**To improve K accuracy:** Replace with NBSS&LUP soil series K-values when available.

---

## LS — Slope Length-Gradient Factor

**Dimensionless**

We use the **Moore et al. (1991)** formulation based on specific catchment area (As) and slope angle (β):

```
LS = (As / 22.13)^0.6 × (sin β / 0.0896)^1.3
```

Where:
- **As** = flow accumulation (cells) × cell size (m) — the specific catchment area in m²/m
- **β** = slope angle in radians
- Exponents m=0.6, n=1.3 represent rill-dominated erosion (appropriate for semi-arid systems)
- Values capped at 50.0 to prevent cliff-edge artefacts

This is preferred over the original Wischmeier & Smith (1978) L and S factors because it handles **convergent and divergent flow** using the DEM-derived flow accumulation rather than assuming a fixed slope length.

---

## C — Cover-Management Factor

**Dimensionless, 0–1**

C represents the ratio of soil loss from a given land use to that from bare tilled fallow. Since no LULC map is available, C is estimated from slope as a proxy for land use intensity:

| Slope Class | C Value | Assumed Land Use |
|-------------|---------|-----------------|
| < 3° | 0.20 | Irrigated / Rabi cropping (flat alluvial) |
| 3–8° | 0.30 | Rainfed Kharif (cotton, sorghum, pulses) |
| 8–15° | 0.45 | Degraded rangeland / sparse scrub |
| 15–25° | 0.55 | Bare patches / open rocky slopes |
| > 25° | 0.15 | Rock outcrop (low soil exposed) |

**To improve C accuracy:** Use a Sentinel-2 or Landsat-derived NDVI map to assign C values spatially.

---

## P — Support Practice Factor

**Dimensionless, 0–1 (1 = no conservation practice)**

P accounts for the effect of traditional soil conservation practices in reducing erosion:

| Slope Class | P Value | Practice Assumed |
|-------------|---------|-----------------|
| < 3° | 1.00 | No practice needed (flat) |
| 3–8° | 0.55 | Contour cultivation + tied ridges |
| 8–15° | 0.65 | Graded bunding (standard MWSSB practice) |
| 15–25° | 0.80 | Bench terracing |
| > 25° | 1.00 | No effective practice possible |

---

## Sediment Delivery Ratio (SDR)

Not all eroded soil reaches the basin outlet — much is deposited on slopes, in gullies, and on floodplains. The SDR quantifies the fraction delivered:

**Formula (Renfro 1975):**
```
SDR = 0.42 × A_km2^(−0.125)
```

Where A_km2 is the basin area in km². For typical Pravara subbasins (~10–50 km²), SDR ranges from **0.38–0.52**.

**Annual Sediment Yield:**
```
Sy (t/yr) = A_mean (t/ha/yr) × Area (ha) × SDR
```

---

## Limitations & Improvement Pathways

1. **No land-use map:** C-factor is slope-based proxy. Improve with: `Sentinel-2 NDVI classification → C-factor lookup table`
2. **No soil map:** K-factor is slope-based proxy. Improve with: `NBSS&LUP 1:250,000 series → assign K by soil series`
3. **Spatially uniform R:** Improve with: `IMD gridded rainfall data → kriging to basin pixels`
4. **No validation:** Sediment yield should be validated against gauging station records at basin outlet (Pravara at Sangamner)
