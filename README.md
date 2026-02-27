<div align="center">

# Pravara River Basin
## Advanced Morphometric & Hydrological Analysis

*A complete 18-section geospatial pipeline — watershed characterisation · RUSLE soil erosion · soil–water conservation planning*
*Ahmednagar District, Maharashtra, India*

<br>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Colab](https://img.shields.io/badge/Google%20Colab-Ready-F9AB00?style=for-the-badge&logo=google-colab&logoColor=black)](https://colab.research.google.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Sections](https://img.shields.io/badge/Pipeline%20Sections-18-8b5cf6?style=for-the-badge)](#pipeline-architecture)
[![Parameters](https://img.shields.io/badge/Morphometric%20Parameters-60%2B-0ea5e9?style=for-the-badge)](#complete-morphometric-results)

<br>

[**Quick Start**](#quick-start) · [**Architecture**](#pipeline-architecture) · [**Morphometry**](#complete-morphometric-results) · [**Hydrology**](#hydrology--flood-analysis) · [**RUSLE**](#rusle-soil-erosion-results) · [**Conservation**](#soil--water-conservation-planning) · [**UH**](#synthetic-unit-hydrograph) · [**Hydraulics**](#stream-channel-hydraulics) · [**Maps**](#maps-gallery)

</div>

---

## 📍 Study Area

<table>
<tr>
<td width="55%">

```
Basin         :  Pravara River (Godavari sub-basin)
District      :  Ahmednagar, Maharashtra, India
Coordinates   :  19.47°N–19.65°N  |  73.64°E–73.91°E
CRS           :  UTM Zone 43N (EPSG:32643)
DEM Source    :  SRTM 30 m (NASA/USGS)
Geology       :  Basaltic Deccan Traps
Climate       :  Semi-arid monsoonal (~750 mm/yr)
Total Area    :  312.15 km²  |  3 subbasins
Elevation     :  584 m – 1 537 m  (relief = 953 m)
Stream Segs   :  3 610  |  Strahler Orders 1–6
```

</td>
<td width="45%">

| Subbasin | Area (km²) | Perimeter (km) | Max Order |
|:---:|---:|---:|:---:|
| **SB1** | 116.99 | 51.86 | 6 |
| **SB2** | 45.19 | 42.75 | 5 |
| **SB3** | 149.97 | 55.71 | 6 |
| **Total** | **312.15** | — | 6 |

</td>
</tr>
</table>

---

## ⚡ Quick Start

```bash
git clone https://github.com/<your-username>/pravara-basin-morphometry.git
cd pravara-basin-morphometry
pip install -r requirements.txt
```

**Google Colab** — upload `Morphomtery_layers-Final.zip` → `/content/`, then run sections 00 → 18 in order:

```python
%run scripts/section_00_zip_extraction.py
%run scripts/section_01_environment.py
# ... continue through section_18_hydraulics.py
```

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-username>/pravara-basin-morphometry/blob/main/notebooks/full_pipeline.ipynb)

---

## 🏗️ Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PRAVARA BASIN ANALYSIS PIPELINE                       │
├─────────────────────────────────────────────────────────────────────────┤
│  SEC 00  ▸  Zip Extraction & File Auto-Discovery                         │
│  SEC 01  ▸  Environment Setup  (GDAL · geopandas · rasterio)            │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌── CORE MORPHOMETRY ─────────────────────────────────────────────┐    │
│  │  02  Data Loading & DEM Preprocessing                           │    │
│  │  03  60+ Morphometric Parameters (Linear · Areal · Relief)      │    │
│  │  04  Publication Maps  (15 PNG @ 300 DPI)                       │    │
│  │  05  Statistical Analysis  (PCA · Correlation · Clustering)     │    │
│  │  06  Watershed Prioritization  (3 independent methods)          │    │
│  │  07  Interactive Plotly Suite  (12 HTML charts)                 │    │
│  │  08  Export  (CSV · Excel · Shapefiles)                         │    │
│  └── 09  Automated Report Generation                               │    │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌── GEOMORPHIC & TECTONIC ────────────────────────────────────────┐    │
│  │  10  Tectonic Activity Indices  (Bs · Af · Vf · Smf · IAT)      │    │
│  │  11  Geomorphic Indices  (SL · SPI · STI · TWI)                 │    │
│  │  12  Geomorphic Anomaly & Channel Sinuosity                      │    │
│  └── 13  Flood Hazard Composite Score                              │    │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌── HYDROLOGY & SOIL–WATER CONSERVATION ─────────────────────────┐    │
│  │  14  SCS-CN Runoff · Gumbel Freq · Time of Conc · Peak Qp       │    │
│  │  15  RUSLE  (R · K · LS · C · P · SDR · Sediment Yield)         │    │
│  │  16  Conservation Planning  (CDSI · Percolation · WHP)          │    │
│  │  17  Synthetic Unit Hydrograph  (Snyder · SCS Dimensionless)    │    │
│  └── 18  Stream Channel Hydraulics  (τ₀ · ω · Stability)          │    │
└─────────────────────────────────────────────────────────────────────────┘
```

<details>
<summary><b>📂 Repository Structure</b></summary>

```
pravara-basin-morphometry/
│
├── 📄 README.md                                ← This file
├── 📄 requirements.txt
├── 📄 .gitignore  ·  LICENSE  ·  CHANGELOG.md  ·  CONTRIBUTING.md
│
├── 📂 scripts/                                 ← 19 Python modules
│   ├── adv_v2_morphometry_pravra3basin.py      ← Sections 0–13  (4 367 lines)
│   ├── sections_14_18_hydrology_swc.py         ← Sections 14–18 (1 770 lines)
│   └── section_00_zip_extraction.py … section_18_hydraulics.py
│
├── 📂 notebooks/                               ← Colab-ready .ipynb files
├── 📂 data/                                    ← GIS inputs (Git-ignored)
├── 📂 outputs/                                 ← Generated results (Git-ignored)
│   ├── maps/             ← 15+ maps @ 300 DPI
│   ├── html/             ← 12 Plotly interactive charts
│   ├── tables/           ← CSV / Excel workbooks
│   ├── hydrology/        ← Sections 14–18 CSVs
│   ├── conservation/     ← SWC planning outputs
│   ├── unit_hydrograph/  ← UH plots & parameter table
│   └── shapefiles/       ← GIS exports
│
├── 📂 docs/
│   ├── DATA_REQUIREMENTS.md
│   ├── PARAMETERS_REFERENCE.md
│   ├── RESULTS_INTERPRETATION.md
│   └── methodology/
│       ├── 06_rusle.md
│       ├── 07_scs_cn_runoff.md
│       └── 08_synthetic_uh.md
│
└── 📂 tests/                                   ← pytest unit tests
```

</details>

---

## 📊 Complete Morphometric Results

### Section 3 · Stream Order Statistics

<details open>
<summary><b>Strahler Stream Order Hierarchy (all subbasins)</b></summary>

**SB1** — 1 453 streams · max order 6 · **Rbm = 2.520**

| Order | Nu | Lu (km) | Lsm (km) | Rb | RL |
|:---:|---:|---:|---:|---:|---:|
| 1 | 726 | 205.26 | 0.283 | 2.039 | — |
| 2 | 356 | 90.10 | 0.253 | 2.082 | 0.895 |
| 3 | 171 | 46.39 | 0.271 | 1.188 | 1.072 |
| 4 | 144 | 29.37 | 0.204 | 3.200 | 0.752 |
| 5 | 45 | 7.70 | 0.171 | 4.091 | 0.839 |
| 6 | 11 | 2.57 | 0.234 | — | 1.367 |

**SB2** — 528 streams · max order 5 · **Rbm = 1.796**

| Order | Nu | Lu (km) | Lsm (km) | Rb | RL |
|:---:|---:|---:|---:|---:|---:|
| 1 | 269 | 68.13 | 0.253 | 2.242 | — |
| 2 | 120 | 31.29 | 0.261 | 1.690 | 1.030 |
| 3 | 71 | 18.23 | 0.257 | 1.732 | 0.985 |
| 4 | 41 | 11.34 | 0.277 | 1.519 | 1.078 |
| 5 | 27 | 8.30 | 0.307 | — | 1.111 |

**SB3** — 1 618 streams · max order 6 · **Rbm = 1.763**

| Order | Nu | Lu (km) | Lsm (km) | Rb | RL |
|:---:|---:|---:|---:|---:|---:|
| 1 | 827 | 234.90 | 0.284 | 2.499 | — |
| 2 | 331 | 96.70 | 0.292 | 1.505 | 1.029 |
| 3 | 220 | 53.37 | 0.243 | 2.178 | 0.830 |
| 4 | 101 | 24.49 | 0.243 | 2.104 | 1.000 |
| 5 | 48 | 12.16 | 0.253 | 0.528 | 1.045 |
| 6 | 91 | 25.18 | 0.277 | — | 1.092 |

</details>

### Section 3 · Areal & Relief Parameters — Master Table

| Parameter | SB1 | SB2 | SB3 | Basin Mean |
|-----------|---:|---:|---:|---:|
| Area (km²) | 116.99 | 45.19 | 149.97 | **104.05** |
| Perimeter (km) | 51.86 | 42.75 | 55.71 | 50.11 |
| Basin Length Lb (km) | 10.19 | 6.33 | 11.52 | 9.35 |
| Drainage Density Dd (km/km²) | 3.260 | 3.038 | 2.979 | **3.093** |
| Stream Frequency Fs (str/km²) | 12.42 | 11.68 | 10.79 | 11.63 |
| Texture Ratio T | 21.87 | 12.35 | 19.76 | 17.99 |
| Form Factor Ff | 1.128 | 1.128 | 1.128 | **1.128** |
| Elongation Ratio Re | 1.198 | 1.198 | 1.198 | **1.198** |
| Circularity Ratio Rc | 0.274 | 0.310 | 0.304 | 0.296 |
| Compactness Cc | 1.792 | 1.794 | 1.820 | 1.802 |
| Length Overland Flow Lg (km) | 0.153 | 0.165 | 0.168 | 0.162 |
| Channel Maintenance C (km²/km) | 0.307 | 0.329 | 0.336 | 0.324 |
| Max Elevation (m) | 1 537 | 1 537 | 1 537 | 1 537 |
| Min Elevation (m) | 584 | 584 | 584 | 584 |
| **Basin Relief H (m)** | **953** | **953** | **953** | **953** |
| Relief Ratio Rh | 0.0936 | 0.1506 | 0.0827 | 0.1089 |
| Ruggedness Number Rn | 3.107 | 2.895 | 2.839 | **2.947** |
| Melton Ruggedness MRN | 88.09 | 141.77 | 77.87 | 102.56 |
| **Hypsometric Integral HI** | **0.262** | **0.262** | **0.262** | **0.262** |
| Mean Slope (°) | 13.85 | 13.93 | 12.13 | 13.30 |
| **Mean Bifurcation Ratio Rbm** | **2.520** | **1.796** | **1.763** | **2.026** |

> **Key Findings:** HI = 0.262 → **Peneplain stage** (mature-to-old landscape). Rn > 2.8 → high erosion susceptibility across all basins. Rc < 0.35 → strongly elongated basins, moderate flood risk. Re = 1.198 → near-circular form factor (high peak discharge potential).

---

### Section 6 · Watershed Prioritization — Three Independent Methods

| Subbasin | Compound CF | Entropy Score | PCA Score | **Consensus** |
|:---:|:---:|:---:|:---:|:---:|
| **SB1** | 1.200 (Rank 1) | 0.608 (Rank 1) | +2.153 (Rank 1) | 🔴 **Priority 1 — HIGH** |
| **SB2** | 1.600 (Rank 2) | 0.336 (Rank 2) | −0.511 (Rank 2) | 🟡 **Priority 2 — MODERATE** |
| **SB3** | 2.300 (Rank 3) | 0.022 (Rank 3) | −1.642 (Rank 3) | 🟢 **Priority 3 — LOW** |

> All three methods show **perfect agreement** (Kendall's τ = 1.000, p = 0.333). **SB1 requires immediate watershed treatment investment.**

---

### Section 10 · Tectonic Activity Indices

| Index | SB1 | SB2 | SB3 |
|-------|---:|---:|---:|
| Mountain Front Sinuosity Smf | 6.78 | 6.78 | 6.78 |
| Asymmetry Factor AF proxy | 0.094 | 0.151 | 0.083 |
| Valley Floor Ratio Vf proxy | 13.85° | 13.93° | 12.13° |
| **IAT (Index Active Tectonics)** | **2.00** | **1.25** | **2.75** |
| **Tectonic Class** | Class 2 — High | **Class 1 — Very High** | Class 4 — Low |

> ⚠️ SB2 = **Class 1 Very High tectonic activity** — avoid large dam structures; design distributed small check dams only.

---

### Section 11 · Geomorphic Indices

| Index | SB1 | SB2 | SB3 |
|-------|---:|---:|---:|
| SL Anomaly (mean) | −0.198 | **+0.303** | −0.003 |
| SL Anomaly (max) | 1.152 | 1.247 | 0.867 |
| **SPI mean** | 252 497 | 274 669 | **2 295 745** |
| **STI mean** | 8 324 | 9 099 | **75 686** |
| **TWI mean** | **7.685** | 6.822 | 6.878 |
| TWI max | 23.84 | 22.60 | **24.82** |

> SB3 has dramatically elevated SPI (9× SB1) and STI (9× SB1) → very high erosive energy. SB1 has the highest mean TWI → best groundwater recharge potential → site percolation ponds here.

---

## 💧 Hydrology & Flood Analysis

### Section 14 · Rainfall Frequency Analysis (Gumbel EV-I)

*μ = 750 mm · σ = 187 mm · CV = 0.25 — IMD Ahmednagar station*

| Return Period | Annual P (mm) | P₂₄ₕᵣ (mm) |
|:---:|---:|---:|
| 2-yr | 719 | 158.2 |
| 5-yr | 885 | 194.6 |
| 10-yr | 994 | 218.7 |
| **25-yr** | **1 132** | **249.1** |
| 50-yr | 1 235 | 271.6 |
| 100-yr | 1 337 | 294.0 |

### Section 14 · SCS-CN Direct Runoff & Peak Discharge

| Parameter | SB1 | SB2 | SB3 |
|-----------|---:|---:|---:|
| **Curve Number CN** | 76.57 | 75.82 | 76.19 |
| Potential Retention S (mm) | 77.7 | 81.0 | 79.4 |
| Q₁₀ (mm) | 146.94 | 144.64 | 145.77 |
| **Q₂₅ (mm)** | **175.24** | **172.80** | **174.00** |
| Q₁₀₀ (mm) | 217.70 | 215.08 | 216.37 |
| **Vol₂₅ (Mm³)** | **20.50** | **7.81** | **26.10** |
| Tc Kirpich (min) | 59.2 | 34.2 | 68.3 |
| Tc SCS Lag (min) | 117.6 | 81.9 | 140.7 |
| **Tc Average (min)** | **88.4** | **58.1** | **104.5** |
| Qp₁₀ (m³/s) | 1 278.6 | 643.5 | 1 454.5 |
| **Qp₂₅ (m³/s)** | **1 524.9** | **768.8** | **1 736.1** |
| Qp₁₀₀ (m³/s) | 1 894.3 | 956.9 | 2 158.8 |

> 🌊 **SB3 generates the highest peak discharge — 1 736 m³/s at 25-yr return period.** Design all major check dam spillways in SB3 for this flow. SB2, with the shortest Tc (58 min), produces the flashiest response.

📊 [Interactive Flood Frequency Curves →](outputs/html/14c_flood_frequency_curves.html)

---

## 🌱 RUSLE Soil Erosion Results

### Section 15 · Factor Values

| Factor | Range | Basin Mean | Basis |
|--------|-------|:---:|-------|
| **R** — Rainfall Erosivity | 594–807 MJ·mm/(ha·hr·yr) | **650** | IMD Maharashtra + elevation gradient |
| **K** — Soil Erodibility | 0.05–0.25 t·ha·hr/(ha·MJ·mm) | **0.153** | Slope-based Deccan Trap proxy |
| **LS** — Slope-Length Gradient | 0.00–50.00 | **10.87** | Moore et al. (1991): As-based |
| **C** — Cover-Management | 0.15–0.55 | **0.356** | Slope-class LULC proxy |
| **P** — Support Practice | 0.55–1.00 | **0.737** | Maharashtra bunding practices |

### Section 15 · Annual Soil Loss — A = R · K · LS · C · P

| Metric | SB1 | SB2 | SB3 | **Total** |
|--------|---:|---:|---:|---:|
| Mean Soil Loss A (t/ha/yr) | 159.66 | 175.09 | 169.77 | **168.2** |
| Basin Area (ha) | 11 699 | 4 519 | 14 997 | **31 215** |
| Gross Erosion (t/yr) | ~1 868 000 | ~791 000 | ~2 547 000 | **~5 206 000** |
| SDR | 0.232 | 0.261 | 0.225 | — |
| **Sediment Yield (t/yr)** | **432 585** | **206 386** | **571 624** | **1 210 595** |
| Erosion Class | 🔴 Severe | 🔴 Severe | 🔴 Severe | 🔴 **Severe** |

> ⚠️ **Critical Finding:** The basin-wide mean of **168 t/ha/yr is 33× the tolerable limit** (5 t/ha/yr for India). Total annual sediment yield of **1.21 million tonnes** is transported out of the Pravara catchment. Immediate large-scale watershed intervention is hydrologically and economically justified.

📊 [RUSLE Erosion Charts →](outputs/html/15c_RUSLE_erosion_bars.html) · [RUSLE Radar →](outputs/html/15d_RUSLE_radar.html)

---

## 🛡️ Soil & Water Conservation Planning

### Section 16 · Check Dam Suitability (CDSI)

*CDSI = 0.30×Order + 0.25×Area + 0.20×Slope + 0.15×Erosion + 0.10×Vf*

| CDSI Class | Segments | % Network | Action |
|:---:|:---:|:---:|---|
| 🟢 Very Suitable (≥7.5) | 52 | 1.4% | Build immediately |
| 🔵 Suitable (5.5–7.5) | **2 666** | **73.8%** | Primary check dam network |
| 🟡 Moderately Suitable (3.5–5.5) | 669 | 18.5% | Secondary network |
| 🔴 Poorly Suitable (<3.5) | 223 | 6.2% | Use contour trenches instead |

### Section 16 · Water Harvesting & Conservation Potential

| Parameter | SB1 | SB2 | SB3 | **Combined** |
|-----------|---:|---:|---:|---:|
| Contour Trench Area (%) | 37.2% | **46.3%** | **53.6%** | — |
| **Water Harvesting Potential₂₅ (Mm³)** | **8.20** | **3.12** | **10.44** | **21.76** |
| Estimated Check Dam Sites | ~1 078 | ~1 078 | ~1 078 | **~3 234** |
| Percolation Zone | High TWI | Moderate | Moderate | SB1 priority |
| **SWC Priority** | 🔴 HIGH | 🔴 HIGH | 🔴 HIGH | — |

> 💡 Combined WHP = **21.76 Mm³** (25-yr event) — equivalent to **~21 760 farm ponds**. Prioritise SB3 for large percolation tanks (10.4 Mm³); SB2 for dense check dam network (compact basin, highest erosion, Class 1 tectonic).

📊 [SWC Planning Charts →](outputs/html/16c_SWC_potential_bars.html)

---

## 📈 Synthetic Unit Hydrograph

### Section 17 · Snyder's Method — Calibration: Ct = 1.8, Cp = 0.6 (Deccan Trap)

| Parameter | SB1 | SB2 | SB3 |
|-----------|---:|---:|---:|
| Channel Length L (km) | 10.19 | 6.33 | 11.52 |
| Lag Time tL (hr) | 6.22 | 4.67 | 6.70 |
| Standard Duration tr (hr) | 1.13 | 0.85 | 1.22 |
| **Time to Peak tp (hr)** | **6.78** | **5.10** | **7.30** |
| **Unit Peak Qp (m³/s/mm)** | **31.056** | **15.959** | **36.954** |
| **Width W50 (hr)** | **8.963** | **6.586** | **9.715** |
| Width W75 (hr) | 5.110 | 3.755 | 5.538 |
| **Base Time tb (hr)** | **33.90** | **25.49** | **36.53** |

**Return Period Peak Discharges from Synthetic UH**

| T | Qp SB1 (m³/s) | Qp SB2 (m³/s) | Qp SB3 (m³/s) |
|:---:|---:|---:|---:|
| 10-yr | 1 278.6 | 643.5 | 1 454.5 |
| **25-yr** | **1 524.9** | **768.8** | **1 736.1** |
| 100-yr | 1 894.3 | 956.9 | 2 158.8 |

> 🏔️ For check dam spillway design per **IS:11200** (MWSSB Maharashtra): use **Q₂₅ = 1 736 m³/s** for SB3, **Q₂₅ = 1 525 m³/s** for SB1, and **Q₂₅ = 769 m³/s** for SB2. Route through the hydrograph to determine required spillway capacity.

📊 [Synthetic Unit Hydrographs →](outputs/html/17b_synthetic_unit_hydrographs.html) · [Parameter Table →](outputs/html/17c_UH_parameter_table.html)

---

## 🌊 Stream Channel Hydraulics

### Section 18 · Bankfull Geometry & Stability

*Leopold-Maddock regional curves: W = 3.2Q⁰·⁵, D = 0.28Q⁰·⁴, V = 1.12Q⁰·¹ — Deccan Trap calibration*

| Parameter | SB1 | SB2 | SB3 |
|-----------|---:|---:|---:|
| **Bankfull Q_bf (m³/s)** | 692.5 | 345.9 | 785.0 |
| Bankfull Width W (m) | 84.2 | 59.5 | 89.7 |
| Bankfull Depth D (m) | 3.83 | 2.90 | 4.03 |
| W/D Ratio | 22.0 | 20.5 | 22.3 |
| **Bed Shear Stress τ₀ (Pa)** | **2 578.9** | **3 124.5** | **2 397.3** |
| Critical Shields τc (Pa) | 10.3 | 10.3 | 10.3 |
| Excess Shear τ₀−τc (Pa) | 2 568.6 | 3 114.2 | 2 387.0 |
| **Specific Stream Power ω (W/m²)** | **7 549.2** | **8 584.0** | **7 098.8** |
| Critical ωc (W/m²) | 35.0 | 35.0 | 35.0 |
| **Channel Stability** | 🔴 Highly Unstable | 🔴 Highly Unstable | 🔴 Highly Unstable |

### Section 18 · Stream Power by Strahler Order

| Order | N | Length (km) | Mean Slope (°) | ω (W/m²) | Status |
|:---:|---:|---:|:---:|---:|:---:|
| 1 | 1 828 | 510.6 | 9.83 | 11.83 | ✅ Sub-critical |
| 2 | 809 | 218.4 | 7.13 | **48.35** | ⚠️ Active transport |
| 3 | 462 | 118.0 | 4.31 | **53.86** | ⚠️ Active transport |
| 4 | 286 | 65.2 | 2.89 | **51.63** | ⚠️ Active transport |
| 5 | 120 | 28.2 | 3.36 | **79.44** | 🔴 High erosive power |
| **6** | **105** | **28.5** | **6.36** | **189.30** | 🔴 **Very high power** |

> ⚠️ **Critical Hydraulic Result:** Shear stress is **250× above Shields threshold**; stream power is **216× above critical ωc**. This independently validates the RUSLE Severe classification. Before installing any check dam infrastructure, **gully plug + bioengineering bank stabilisation** must precede structure construction — otherwise structures will be undermined.

📊 [Stream Power & Hydraulics →](outputs/html/18c_stream_power_hydraulics.html) · [Hydraulic Geometry (log-log) →](outputs/html/18d_hydraulic_geometry_loglog.html)

---

## 🔬 Final Consolidated Results

> Full machine-readable table: [`outputs/tables/hydrology_SWC_consolidated.csv`](outputs/tables/hydrology_SWC_consolidated.csv)

| Metric | SB1 | SB2 | SB3 |
|--------|---:|---:|---:|
| CN mean | 76.57 | 75.82 | 76.19 |
| Tc avg (min) | 88.4 | 58.1 | 104.5 |
| Q₂₅ (mm) | 175.24 | 172.80 | 174.00 |
| Vol₂₅ (Mm³) | 20.50 | 7.81 | 26.10 |
| Qp₂₅ (m³/s) | 1 524.9 | 768.8 | 1 736.1 |
| Qp₁₀₀ (m³/s) | 1 894.3 | 956.9 | 2 158.8 |
| RUSLE A̅ (t/ha/yr) | 159.66 | 175.09 | 169.77 |
| SDR | 0.232 | 0.261 | 0.225 |
| Sediment Yield (t/yr) | 432 585 | 206 386 | 571 624 |
| Erosion Class | 🔴 Severe | 🔴 Severe | 🔴 Severe |
| WHP₂₅ (Mm³) | 8.20 | 3.12 | 10.44 |
| Est. Check Dams | ~1 078 | ~1 078 | ~1 078 |
| SWC Priority | 🔴 HIGH | 🔴 HIGH | 🔴 HIGH |
| UH tp (hr) | 6.78 | 5.10 | 7.30 |
| UH Qp/mm (m³/s) | 31.056 | 15.959 | 36.954 |
| W50 (hr) | 8.963 | 6.586 | 9.715 |
| tb (hr) | 33.90 | 25.49 | 36.53 |
| Q_bankfull (m³/s) | 692.5 | 345.9 | 785.0 |
| τ₀ (Pa) | 2 578.9 | 3 124.5 | 2 397.3 |
| ω (W/m²) | 7 549.2 | 8 584.0 | 7 098.8 |
| Channel Stability | 🔴 Highly Unstable | 🔴 Highly Unstable | 🔴 Highly Unstable |

---

## 🗺️ Maps Gallery

| Map | Section | Key Finding |
|-----|:---:|---|
| `maps/04a_basin_boundary.png` | 4 | Basin + stream network on hillshade |
| `maps/04b_stream_order.png` | 4 | Strahler 1–6 colour-coded |
| `maps/04c_slope_map.png` | 4 | 0°–88.4° continuous |
| `maps/10a_tectonic_IAT_map.png` | 10 | SB2 = Class 1 Very High activity |
| `maps/14a_CN_map.png` | 14 | CN 70–85, mean 76.2 |
| `maps/14b_runoff_volume_25yr.png` | 14 | Vol 7.8–26.1 Mm³ (25-yr) |
| `maps/15a_LS_factor.png` | 15 | LS mean 10.87, max 50 |
| `maps/15b_RUSLE_soil_loss.png` | 15 | **All pixels: Severe class** |
| `maps/16a_checkdam_suitability.png` | 16 | 73.8% of network Suitable+ |
| `maps/16b_SWC_treatment_zones.png` | 16 | Percolation · Trench · Check dam |
| `maps/18a_bankfull_hydraulics.png` | 18 | W = 59–90 m bankfull |
| `maps/18b_channel_stability.png` | 18 | All basins Highly Unstable |

---

## 📊 Interactive Visualization Index

| Chart | File | Section | Insight |
|-------|------|:---:|--------|
| Horton's Laws — SB1 | `html/01_hortons_law_SB1.html` | 7 | Rbm = 2.520 |
| Horton's Laws — SB2 | `html/01_hortons_law_SB2.html` | 7 | Rbm = 1.796 |
| Horton's Laws — SB3 | `html/01_hortons_law_SB3.html` | 7 | Rbm = 1.763 |
| Radar — Morphometric | `html/02_radar_morphometric.html` | 7 | SB1 most degraded |
| Scatter Matrix | `html/03_scatter_matrix.html` | 7 | Dd–Fs strong positive |
| 3D Parameter Scatter | `html/04_3d_scatter.html` | 7 | Relief–Dd–Area space |
| Hypsometric Curves | `html/07_hypsometric_curves.html` | 7 | HI = 0.262 peneplain |
| Correlation Heatmap | `html/08_correlation_heatmap.html` | 7 | Full r-matrix |
| Parallel Coordinates | `html/09_parallel_coordinates.html` | 7 | Full parameter space |
| Tectonic Radar | `html/10b_tectonic_radar.html` | 10 | SB2 Class 1 outlier |
| **Flood Frequency Curves** | `html/14c_flood_frequency_curves.html` | **14** | **Qp₂₅ = 1 736 m³/s** |
| RUSLE Erosion Bars | `html/15c_RUSLE_erosion_bars.html` | 15 | 1.21 Mt/yr total |
| RUSLE Radar | `html/15d_RUSLE_radar.html` | 15 | Factor signatures |
| SWC Potential Bars | `html/16c_SWC_potential_bars.html` | 16 | WHP = 21.76 Mm³ |
| **Synthetic Unit Hydrographs** | `html/17b_synthetic_unit_hydrographs.html` | **17** | **tp = 5–7 hr** |
| UH Parameter Table | `html/17c_UH_parameter_table.html` | 17 | All UH parameters |
| **Stream Power & Shear** | `html/18c_stream_power_hydraulics.html` | **18** | **ω = 189 W/m² (order 6)** |
| Hydraulic Geometry (log-log) | `html/18d_hydraulic_geometry_loglog.html` | 18 | W-Q, D-Q, V-Q |

---

## 📦 Output File Index

| File | Size | Section |
|------|-----:|:---:|
| `hydrology/rainfall_frequency.csv` | 0.1 KB | 14 |
| `hydrology/runoff_scscn.csv` | 0.8 KB | 14 |
| `hydrology/time_of_concentration_peak_discharge.csv` | 0.6 KB | 14 |
| `hydrology/RUSLE_soil_erosion.csv` | 0.5 KB | 15 |
| `hydrology/stream_order_power.csv` | 0.4 KB | 18 |
| `hydrology/channel_hydraulics.csv` | 0.7 KB | 18 |
| `conservation/checkdam_suitability.csv` | 215.5 KB | 16 |
| `conservation/conservation_potential.csv` | 0.3 KB | 16 |
| `unit_hydrograph/snyder_unit_hydrograph_params.csv` | 0.5 KB | 17 |
| `unit_hydrograph/17_unit_hydrographs.png` | **439.1 KB** | 17 |
| `tables/hydrology_SWC_consolidated.csv` | — | All |
| `tables/morphometric_master_table.csv` | — | 3 |
| `tables/tectonic_activity_indices.csv` | — | 10 |
| `shapefiles/checkdam_suitability.shp` | — | 16 |
| **`morphometric_outputs_20260225.zip`** | **67.5 MB** | All |

---

## 📖 Documentation

| Doc | Description |
|-----|-------------|
| [`docs/DATA_REQUIREMENTS.md`](docs/DATA_REQUIREMENTS.md) | Required files, field names, preprocessing, zip structure |
| [`docs/PARAMETERS_REFERENCE.md`](docs/PARAMETERS_REFERENCE.md) | All 60+ parameters: formula, unit, interpretation |
| [`docs/RESULTS_INTERPRETATION.md`](docs/RESULTS_INTERPRETATION.md) | How to read each map, CSV, chart and what action to take |
| [`docs/methodology/06_rusle.md`](docs/methodology/06_rusle.md) | RUSLE factor derivation, Deccan assumptions, improvement path |
| [`docs/methodology/07_scs_cn_runoff.md`](docs/methodology/07_scs_cn_runoff.md) | SCS-CN + Gumbel + IDF + design return periods |
| [`docs/methodology/08_synthetic_uh.md`](docs/methodology/08_synthetic_uh.md) | Snyder's calibration for Deccan Trap basalt |
| [`CHANGELOG.md`](CHANGELOG.md) | v1.0 → v2.0 changes, all bug fixes |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Code style, PR workflow, priority improvements |

---

## 📚 References

1. Horton R.E. (1945). Erosional development of streams. *Bulletin GSA*, 56, 275–370
2. Strahler A.N. (1952, 1964). Quantitative geomorphology. *Handbook of Applied Hydrology*
3. Schumm S.A. (1956). Evolution of drainage systems. *Bulletin GSA*, 67, 597–646
4. Moore I.D., Grayson R.B., Ladson A.R. (1991). Digital terrain modelling. *Hydrol. Processes*, 5, 3–30
5. USDA-SCS (1985). *National Engineering Handbook, Section 4: Hydrology*
6. Wischmeier W.H. & Smith D.D. (1978). *Predicting Rainfall Erosion Losses*. USDA-AH537
7. Snyder F.F. (1938). Synthetic unit-graphs. *Trans. AGU*, 19, 447–454
8. Kirpich Z.P. (1940). Time of concentration. *Civil Engineering*, 10(6), 362
9. Leopold L.B. & Maddock T. (1953). *Hydraulic geometry*. USGS Prof. Paper 252
10. Bagnold R.A. (1966). *Sediment transport*. USGS Prof. Paper 422-I
11. El Hamdouni R. et al. (2008). Active tectonics assessment. *Geomorphology*, 96, 150–173
12. Renfro G.W. (1975). Sediment delivery ratios. *USDA-ARS Pub.*

---

## 🤝 Contributing & License

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines · MIT License — [`LICENSE`](LICENSE)

---

<div align="center">

*Pravara River Basin · Ahmednagar District · Maharashtra · India*
*18-section pipeline · 312 km² · 3 610 stream segments · 60+ morphometric parameters*

**[⬆ Back to top](#pravara-river-basin)**

</div>
