# 🗺️ Map Gallery: Ultimate Publication Suite (v15.0)

This directory contains the **definitive cartographic products** for the Pravara River Basin analysis. All maps are exported at institutional research standards for high-resolution publication and academic presentation.

## 📏 Technical Standards
- **Resolution**: High-Fidelity 600 DPI
- **Grid System**: Symmetric 3'/4' DMS Grids (Black Hairline)
- **Typography**: Times New Roman (Institutional Academic Standard)
- **Features**: Vertical labeling, Compass Rose, Scale Bar, and Regional Branding.

---

## 📂 Master Inventory (24 Thematic Layers)

### 🔵 Core Terrain & Morphometry
| ID | Map Title | Analytical Target |
|:--:|-----------|-------------------|
| 01 | Digital Elevation Model | Absolute relief and terrain configuration |
| 02 | Slope Distribution | Surface steepness for hydrological response |
| 03 | Aspect Map | Topographic orientation and exposure |
| 23 | Stream Order Map | Strahler network classification (Orders 1-6) |
| 24 | Drainage Density Map | Surface impermeability and runoff potential |

### 🟠 Advanced Geomorphic Indices
| ID | Map Title | Analytical Target |
|:--:|-----------|-------------------|
| 04 | Topographic Wetness Index | Surface saturation and runoff convergence |
| 05 | Stream Power Index | Erosive capacity of the drainage network |
| 06 | Sediment Transport Index | Catchment erosional and depositional logic |
| 07 | Ruggedness Index | Terrain complexity and dissection stage |
| 13 | Geomorphic Anomaly Index | Neotectonic and lithological disruptions |

### 🟢 Hydrology & Hazard
| ID | Map Title | Analytical Target |
|:--:|-----------|-------------------|
| 09 | Flow Direction | D8-modelled gravitational drainage pathway |
| 10 | Flow Accumulation | Contributing area and stream initialization |
| 11 | Curve Number (CN) Map | SCS-based infiltration and runoff potential |
| 12 | Flash Flood Potential | Composite index (FFPI) for disaster planning |

### 🟤 RUSLE Soil Erosion Suite
| ID | Map Title | Analytical Target |
|:--:|-----------|-------------------|
| 17 | Potential Soil Loss (A) | Mean annual soil loss (tonnes/ha/year) |
| 18 | C-Factor (Cover) | Land cover and crop management influence |
| 19 | K-Factor (Erodibility) | Soil resistance to detachment and transport |
| 20 | LS-Factor (Slope) | Combined length and steepness influence |
| 22 | R-Factor (Rainfall) | Erosivity from Gumbel-transformed frequency |

### 🛰️ SWC & Conservation Planning
| ID | Map Title | Analytical Target |
|:--:|-----------|-------------------|
| 15 | Percolation Potential | Identification of infiltration-friendly zones |
| 16 | Contour Trench Suitability | Slope-calibrated trench planning (3-30°) |
| 08 | Tectonic Lineament Density | Structural control on watershed treatment |

---

## 🧪 Scientific Disclaimer
Indices such as **SPI (05)** and **STI (06)** have been rendered using **Log-Normal Scaling (`LogNorm`)** to ensure maximum visibility of drainage pathways across high-dynamic range terrain. The audited Hypsometric Integrals (HI) for SB1 (0.222), SB2 (0.267), and SB3 (0.249) were used to validate the geomorphic maturity of these specific layers.

> [!TIP]
> Use the [scripts/ultimate_publication_renderer.py](../../scripts/ultimate_publication_renderer.py) to re-generate this suite at 300, 600, or 1200 DPI as required for your publication.
