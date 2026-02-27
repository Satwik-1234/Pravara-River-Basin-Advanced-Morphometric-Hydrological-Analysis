# SCS-CN Runoff Methodology

## Overview

The **Soil Conservation Service Curve Number (SCS-CN)** method estimates direct runoff from a rainfall event. It is the standard method in Indian watershed hydrology and accepted by NABARD and MWSSB for watershed scheme design.

---

## Rainfall Frequency Analysis — Gumbel EV-I

Before computing runoff, extreme rainfall values for different return periods are derived using **Gumbel Extreme Value Type-I (EV-I)** distribution:

```
P(T) = u + α × yT
```

Where:
- `α = σ × √6 / π` — scale parameter
- `u = μ − 0.5772 × α` — location parameter (mode)
- `yT = −ln(−ln(1 − 1/T))` — Gumbel reduced variate

For Pravara basin (Ahmednagar):
- Mean annual rainfall μ = 750 mm
- Std deviation σ = 187 mm
- CV ≈ 0.25

24-hour maximum rainfall = 22% of annual total (semi-arid India empirical ratio).

---

## SCS-CN Direct Runoff

```
S = 25400/CN − 254     [potential max retention, mm]
Ia = 0.2 × S           [initial abstraction, mm]
Q = (P − Ia)² / (P + 0.8S)   if P > Ia, else Q = 0
```

**Curve Number Assignment (slope-based proxy):**

| Slope | CN | Soil/Cover Type (Deccan Trap) |
|-------|-----|------------------------------|
| < 3° | 85 | Deep Vertisol, flat cultivated (AMC-II) |
| 3–8° | 79 | Vertic Inceptisol, mixed agriculture |
| 8–20° | 75 | Shallow Alfisol, degraded hillslope |
| > 20° | 70 | Lithic/rocky, sparse cover |

**AMC-II** (Average Moisture Condition) is the standard design condition.

---

## Time of Concentration

Two methods are computed and averaged:

### 1. Kirpich (1940)
```
Tc = 0.0195 × L^0.77 × S^(-0.385)   [minutes]
```
Where L = channel length (m), S = H/L = channel slope.

### 2. SCS Lag Method
```
tL = (L_ft^0.8 × (S_val + 1)^0.7) / (1900 × Y^0.5)   [hours]
Tc = tL / 0.6
```
Where L = hydraulic length (feet), S_val = 1000/CN − 10, Y = average slope (%).

---

## Rainfall Intensity at Tc (IMD Empirical IDF)

```
i_Tc = (P24hr / 24) × (24 / Tc_hr)^(2/3)   [mm/hr]
```

This follows the Chen (1983) / Indian standard approach for converting 24-hr rainfall to sub-daily intensities.

---

## Peak Discharge — Rational Method

```
Qp = C × i_Tc × A / 3.6   [m³/s]
```

Where:
- C = runoff coefficient = Q_SCS / P (dimensionless)
- i_Tc = rainfall intensity at Tc (mm/hr)
- A = basin area (km²)

---

## Design Return Periods

| Return Period | Use Case |
|---------------|---------|
| 2-year | Drainage design (roads, field bunds) |
| 5-year | Agricultural drainage |
| 10-year | Check dam spillway (minor structures) |
| 25-year | Check dam spillway (major structures) |
| 50-year | Percolation tank spillway |
| 100-year | Large reservoir, bridge design |

As per Indian Bureau of Standards IS:5477 and CWC guidelines:
- **Minor check dams (< 3m height):** Design for Q_25yr
- **Medium structures (3–7.5m):** Design for Q_50yr + routing
- **Major dams:** Full PMF analysis required
