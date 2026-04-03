<div align="center">

# 🌊 Pravara River Basin
### Advanced Morphometric & Hydrological Analysis Pipeline

*Godavari Sub-basin · Ahmednagar District · Maharashtra · India*

<br>

<!-- Tech Stack -->
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Colab](https://img.shields.io/badge/Google%20Colab-Ready-F9AB00?style=flat-square&logo=google-colab&logoColor=black)](https://colab.research.google.com/github/Satwik-1234/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis/blob/main/notebooks/Adv_v2__Final_morphometry_pravrabasin.ipynb)
[![geopandas](https://img.shields.io/badge/geopandas-0.13%2B-139C5A?style=flat-square)](https://geopandas.org)
[![rasterio](https://img.shields.io/badge/rasterio-1.3%2B-4CABD8?style=flat-square)](https://rasterio.readthedocs.io)
[![plotly](https://img.shields.io/badge/Plotly-5.14%2B-3F4F75?style=flat-square&logo=plotly)](https://plotly.com)

<!-- Project Stats -->
[![CI](https://img.shields.io/github/actions/workflow/status/Satwik-1234/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis/ci.yml?style=flat-square&label=CI&logo=github-actions)](https://github.com/Satwik-1234/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis/actions)
[![Pipeline Sections](https://img.shields.io/badge/Pipeline%20Sections-18-8b5cf6?style=flat-square)](docs/)
[![Parameters](https://img.shields.io/badge/Parameters%20Computed-60%2B-0ea5e9?style=flat-square)](docs/PARAMETERS_REFERENCE.md)
[![Maps](https://img.shields.io/badge/Maps%20Generated-26-22c55e?style=flat-square)](outputs/maps/)
[![Charts](https://img.shields.io/badge/Interactive%20Charts-27-f59e0b?style=flat-square)](outputs/html/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)

<br>

[**🗺️ Maps Gallery**](outputs/maps/README.md) &nbsp;·&nbsp;
[**📊 Interactive Charts**](outputs/html/README.md) &nbsp;·&nbsp;
[**📐 Parameters Reference**](docs/PARAMETERS_REFERENCE.md) &nbsp;·&nbsp;
[**📂 Data Guide**](docs/DATA_REQUIREMENTS.md) &nbsp;·&nbsp;
[**📖 Methodology**](docs/)

</div>

---

## 🌍 What Is This?

A **production-ready, end-to-end watershed analysis pipeline** for the **Pravara River Basin** — a Godavari sub-basin in Maharashtra, India. Built entirely in Python and designed to run on Google Colab with a single zip file upload.

The pipeline covers **18 sequential sections** across three thematic modules:

| Module | Sections | What It Does |
|--------|----------|-------------|
| 🔵 **Core Morphometry** | 0 – 9 | 62+ basin shape, drainage, relief parameters, maps, PCA |
| 🟠 **Geomorphic & Tectonic** | 10 – 13 | Tectonic activity indices, SL gradient, TWI/SPI rasters, flood hazard composite |
| 🟢 **Hydrology & SWC** | 14 – 18 | SCS-CN runoff, RUSLE erosion, conservation planning, unit hydrographs, channel hydraulics |

---

## 📍 Study Area

<table>
<tr>
<td>

| | |
|--|--|
| 🌊 **River** | Pravara (Godavari sub-basin) |
| 📍 **District** | Ahmednagar, Maharashtra |
| 📐 **Total Area** | **312.15 km²** |
| 🏔️ **Elevation Range** | 584 – 1 537 m (relief 953 m) |
| 🌧️ **Mean Rainfall** | ~750 mm/yr (semi-arid) |
| 🪨 **Geology** | Basaltic Deccan Traps |
| 🗺️ **CRS** | UTM Zone 43N (EPSG:32643) |
| 📡 **DEM** | SRTM 30 m |

</td>
<td>

| Subbasin | Area | Max Order | Priority |
|:---:|---:|:---:|:---:|
| **SB1** | 116.99 km² | 6 | 🔴 1st |
| **SB2** | 45.19 km² | 5 | 🟡 2nd |
| **SB3** | 149.97 km² | 6 | 🟢 3rd |
| **3 610** stream segments | | | |

</td>
</tr>
</table>

---

## 🔑 Three Headline Findings

<table>
<tr>
<td align="center" width="33%">

### ⚠️ Severe Erosion Basin-wide

All 3 subbasins classified **Severe** under USDA RUSLE.

**168 t/ha/yr** mean soil loss — **33×** India's tolerable limit (5 t/ha/yr). **1.21 Mt/yr** leaves the catchment.

→ [Full RUSLE results](docs/RESULTS_INTERPRETATION.md)

</td>
<td align="center" width="33%">

### 🔴 Highly Unstable Channels

Stream shear and power far exceed critical thresholds.

τ₀ = **2 400–3 125 Pa** (τ_c = 10 Pa). W/D ratio 20–22 → active widening.

→ [Full hydraulics results](docs/RESULTS_INTERPRETATION.md)

</td>
<td align="center" width="33%">

### 💡 High Conservation Potential

Significant opportunity for water harvesting.

**21.76 Mm³** WHP at 25-yr event. **73.8%** of stream network Suitable+ for check dams.

→ [SWC planning results](docs/RESULTS_INTERPRETATION.md)

</td>
</tr>
</table>

---

## 🗺️ Map Highlights

> **26 maps generated at 300 DPI** · Full gallery → [`outputs/maps/README.md`](outputs/maps/README.md)

<table>
<tr>
<td align="center" width="25%">

**Stream Order Network**

![Stream Order](outputs/maps/06_stream_order.png)

Orders 1–6 · 3 610 segments · *Section 4*

</td>
<td align="center" width="25%">

**RUSLE Soil Loss**

![RUSLE Soil Loss](outputs/maps/15b_RUSLE_soil_loss.png)

Mean **168 t/ha/yr** · Severe class · *Section 15*

</td>
<td align="center" width="25%">

**Check Dam Suitability**

![Check Dam](outputs/maps/16a_checkdam_suitability.png)

73.8% network Suitable+ · *Section 16*

</td>
<td align="center" width="25%">

**Channel Stability**

![Channel Stability](outputs/maps/18b_channel_stability.png)

All basins Highly Unstable · *Section 18*

</td>
</tr>
<tr>
<td align="center">

**Flood Hazard Composite**

![Flood Hazard](outputs/maps/13e_flood_hazard_composite_map.png)

FFPI + TWI + morphometry · *Section 13*

</td>
<td align="center">

**Curve Number Map**

![CN Map](outputs/maps/14a_CN_map.png)

CN 70–85 · Mean 76.2 · *Section 14*

</td>
<td align="center">

**TWI — Wetness Index**

![TWI](outputs/maps/13a_TWI_map.png)

Mean 6.8–7.7 · Max 24.8 · *Section 13*

</td>
<td align="center">

**SWC Treatment Zones**

![SWC Zones](outputs/maps/16b_SWC_treatment_zones.png)

Percolation · Trenches · Check dams · *Section 16*

</td>
</tr>
</table>

*➡️ [View all 26 maps →](outputs/maps/README.md)*

---

## 📊 Interactive Charts

> **27 Plotly HTML charts** — open locally in any browser · Full index → [`outputs/html/README.md`](outputs/html/README.md)

| Chart | Key Finding |
|-------|-------------|
| [`14c_flood_frequency_curves.html`](outputs/html/14c_flood_frequency_curves.html) | Qp₂₅ reaches **1 736 m³/s** (SB3) |
| [`17b_synthetic_unit_hydrographs.html`](outputs/html/17b_synthetic_unit_hydrographs.html) | W₅₀ = 6.6–9.7 hr · tp = 5.1–7.3 hr |
| [`18c_stream_power_hydraulics.html`](outputs/html/18c_stream_power_hydraulics.html) | ω by order: 11.8 → **189 W/m²** |
| [`15c_RUSLE_erosion_bars.html`](outputs/html/15c_RUSLE_erosion_bars.html) | Total: **1.21 million t/yr** |
| [`02_radar_morphometric.html`](outputs/html/02_radar_morphometric.html) | SB1 clearly most degraded |
| [`09_parallel_coordinates.html`](outputs/html/09_parallel_coordinates.html) | All 21 parameters across basins, interactive |

*➡️ [View all 27 charts →](outputs/html/README.md)*

---

## 🏗️ Pipeline Architecture

```mermaid
graph TD
    classDef input fill:#1e293b,stroke:#e2e8f0,stroke-width:2px,color:#fff
    classDef core fill:#2563eb,stroke:#60a5fa,stroke-width:2px,color:#fff
    classDef geomorph fill:#ea580c,stroke:#fdba74,stroke-width:2px,color:#fff
    classDef hydro fill:#16a34a,stroke:#86efac,stroke-width:2px,color:#fff
    classDef output fill:#475569,stroke:#cbd5e1,stroke-width:2px,color:#fff

    subgraph "Raw Spatial Inputs"
        A1[Filled DEM]:::input
        A2[Flow Direction]:::input
        A3[Flow Accumulation]:::input
        A4[Stream Order Vectors]:::input
        A5[Basin Polygons]:::input
    end

    A1 & A2 & A3 & A4 & A5 -->|GeoPandas & Rasterio| B1

    subgraph "Automated Orchestrator (make pipeline)"
        B1("Core Morphometry<br>(Sec 00-09)"):::core
        B2("Geomorphic & Tectonic<br>(Sec 10-13)"):::geomorph
        B3("Hydrology & SWC<br>(Sec 14-18)"):::hydro
        B1 -->|Base Parameters & Geometries| B2
        B2 -->|Tectonic Indices & Anomaly Grids| B3
    end

    subgraph "Generated Artifacts"
        C1[26 PNG Maps @ 300 DPI]:::output
        C2[27 Interactive HTML Charts]:::output
        C3[18 CSV Result Tables]:::output
        C4[15 Derived GeoTIFF Rasters]:::output
    end

    B1 & B2 & B3 --> C1 & C2 & C3 & C4
```

---

## ⚡ Quick Start

### Google Colab (Recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Satwik-1234/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis/blob/main/notebooks/Adv_v2__Final_morphometry_pravrabasin.ipynb)

```python
# 1. Clone
!git clone https://github.com/Satwik-1234/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis.git
%cd Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis

# 2. Install
!pip install -r requirements.txt --quiet

# 3. Upload your zip to Colab /content/ then run sections 00 → 18
%run scripts/section_00_zip_extraction.py
# ... continue section_01 through section_18
```

### Local Python (Automated Pipeline)

```bash
git clone https://github.com/Satwik-1234/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis.git
cd Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis

make install        # install dependencies
make pipeline       # run all 18 sections
make test           # run unit tests
make lint           # check formatting
```

### Input Files Required

| File | Type | Description |
|------|------|-------------|
| `Filled DEM.tif` | Raster | Hydrologically filled SRTM 30 m DEM |
| `Flow Direction.tif` | Raster | D8 flow direction |
| `FlowAccumilation.tif` | Raster | D8 flow accumulation |
| `SteamOrder.shp` | Vector | Stream network (field: `grid_code`) |
| `Pourpoints_3.shp` | Vector | 3 pour-point outlets |
| `Pravrabasin.shp` | Vector | Subbasin polygons |

→ [Full data guide](docs/DATA_REQUIREMENTS.md)

---

## 📂 Repository Structure

```
Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis/
│
├── scripts/
│   ├── adv_v2_morphometry_pravra3basin.py   ← Sections 0–13 (4 367 lines)
│   ├── sections_14_18_hydrology_swc.py      ← Sections 14–18 (1 770 lines)
│   ├── run_pipeline.py                      ← Master orchestrator
│   └── section_00_zip_extraction.py … section_18_hydraulics.py
│
├── notebooks/
│   └── Adv_v2__Final_morphometry_pravrabasin.ipynb
│
├── data/
│   ├── Morphomtery_layers-Final.zip         ← GIS inputs
│   └── README.md
│
├── outputs/
│   ├── maps/          ← 26 PNG maps @ 300 DPI
│   ├── html/          ← 27 interactive Plotly charts
│   ├── tables/        ← 18 CSV result tables
│   ├── hydrology/     ← Sections 14–18 CSVs
│   ├── conservation/  ← SWC planning outputs
│   ├── unit_hydrograph/
│   ├── shapefiles/    ← 5 GIS exports
│   └── *.tif          ← 15 derived GeoTIFF rasters
│
├── docs/
│   ├── PARAMETERS_REFERENCE.md
│   ├── DATA_REQUIREMENTS.md
│   ├── RESULTS_INTERPRETATION.md
│   └── methodology/   ← RUSLE · SCS-CN · Snyder UH
│
├── tests/
│   └── test_morphometry.py
│
├── .github/workflows/ci.yml
├── Makefile
├── requirements.txt
└── requirements-dev.txt
```

---

## 🧰 Tech Stack

| Category | Libraries |
|----------|-----------|
| **GIS & Raster** | `geopandas`, `rasterio`, `shapely`, `pyproj`, `fiona` |
| **Analysis** | `numpy`, `scipy`, `pandas`, `scikit-learn`, `statsmodels` |
| **Visualisation** | `matplotlib`, `plotly`, `seaborn`, `kaleido` |
| **Reports** | `reportlab`, `jinja2`, `Pillow` |
| **Dev** | `pytest`, `black`, `isort`, `flake8` |

---

## 🧪 Running Tests

```bash
# Unit tests only (no GDAL needed)
pytest tests/ -v

# With coverage
pytest tests/ -v --cov=. --cov-report=term-missing
```

---

## 📚 References

Horton (1945) · Strahler (1952, 1964) · Schumm (1956) · Miller (1953) · Moore et al. (1991) · USDA-SCS (1985) · Wischmeier & Smith (1978) · Snyder (1938) · Kirpich (1940) · Leopold & Maddock (1953) · Bagnold (1966) · El Hamdouni et al. (2008) · Renfro (1975)

→ [Full bibliography](docs/README.md)

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Run `make lint` and `make test` before opening a pull request.

---

<div align="center">

*Made with 🐍 Python · 🗺️ GDAL · 📊 Plotly*

*Pravara River Basin · Maharashtra · India · 312 km²*

**[⬆ back to top](#-pravara-river-basin)**

</div>
