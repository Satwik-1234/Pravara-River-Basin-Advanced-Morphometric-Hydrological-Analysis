# Synthetic Unit Hydrograph Methodology

## Overview

A **Unit Hydrograph (UH)** is the direct-runoff hydrograph from 1 mm of uniformly distributed rainfall over the basin in a given storm duration. Once the UH is derived, peak floods for any return period can be estimated by convolving the UH with the design storm rainfall.

For ungauged basins like the Pravara subbasins, the UH is derived synthetically using empirical formulae calibrated to regional basin characteristics.

---

## Snyder's Synthetic UH (1938)

### Parameters

**Lag Time:**
```
tL = Ct × (L × Lca)^0.3   [hours]
```
- L = main channel length from outlet to basin divide (km)
- Lca = distance from outlet to centroid along main channel (≈ 0.6L)
- Ct = 1.8 (lag coefficient, calibrated for Deccan Trap semi-arid basins)

**Standard Storm Duration:**
```
tr = tL / 5.5   [hours]
```

**Time to Peak:**
```
tp = tL + tr / 2   [hours]
```

**Peak Discharge (per mm of rainfall):**
```
Qp = 2.75 × Cp × A / tL   [m³/s]
```
- A = basin area (km²)
- Cp = 0.6 (peak coefficient, Deccan Trap calibration)

**Unit Area Peak:**
```
qp = Qp / A   [m³/s/km² per mm]
```

**Hydrograph Widths:**
```
W50 = 2.14 / qp^1.08   [hours at 50% of Qp]
W75 = 1.22 / qp^1.08   [hours at 75% of Qp]
```
Standard USBR (1960) empirical — 1/3 of width is on the rising limb, 2/3 on recession.

**Base Time:**
```
tb ≈ 5 × tp   [hours]
```

---

## SCS Dimensionless UH Shape

The dimensionless UH (t/tp vs Q/Qp) follows the tabulated SCS curve:

| t/tp | Q/Qp | t/tp | Q/Qp |
|------|------|------|------|
| 0.0 | 0.000 | 1.1 | 0.990 |
| 0.5 | 0.470 | 1.4 | 0.780 |
| 1.0 | 1.000 | 2.0 | 0.280 |
| — | — | 5.0 | 0.000 |

This shape is applied with Snyder's tp and Qp to produce the full hydrograph for each storm.

---

## Calibration Constants — Deccan Trap

The standard Snyder constants (Ct=2.0, Cp=0.65) are for the eastern USA. For the Pravara basin:

| Constant | This Study | Typical Range (India) | Basis |
|----------|-----------|----------------------|-------|
| Ct | 1.8 | 1.5–2.2 | Semi-arid Deccan basalt; moderate channel density |
| Cp | 0.6 | 0.55–0.75 | Moderate peak attenuation; some floodplain |

These are consistent with CWC guidelines for Godavari sub-basin tributaries.

---

## Return Period Flood Hydrographs

For each return period T, the flood hydrograph is:

```
Q(t, T) = Qp_unit × Q_T(mm) × UH_shape(t/tp)
```

Where Q_T(mm) is the direct runoff depth from SCS-CN for the T-year 24-hr rainfall.

---

## Design Applications

| Structure | Design Flow | Notes |
|-----------|------------|-------|
| Naala bund / check dam < 3m | Q₂₅ | IS:11200 minor irrigation |
| Check dam > 3m | Q₅₀ | Full routing required |
| Percolation tank | Q₅₀ with freeboard | GSDA Maharashtra guidelines |
| Road culvert | Q₁₀–Q₂₅ | Based on road class |
| Flood plains (land use) | Q₅₀–Q₁₀₀ | Revenue map demarcation |
