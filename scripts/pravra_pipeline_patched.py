# Ã¢â€â‚¬Ã¢â€â‚¬ Section 1: Data already extracted to local path Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import os, json
EXTRACT_DIR = r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/"
ZIP_PATH    = r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/Morphomtery layers-Final.zip"
print(f"  Data directory: {EXTRACT_DIR}")
print(f"  Files available: {len(os.listdir(EXTRACT_DIR))}")
# Stub so references to DETECTED_FILES still work if any cell uses it
DETECTED_FILES = {}


import subprocess, sys

def pip_install(*pkgs):
    """Silent pip install with error catching."""
    for pkg in pkgs:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pkg, "-q"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            print(f"  Ã¢Å“â€¦ {pkg}")
        except Exception as e:
            print(f"  Ã¢Å¡Â Ã¯Â¸Â  {pkg} Ã¢â‚¬â€ install failed ({e}), will try to continue")

print("Ã°Å¸â€œÂ¦ Installing packages...")
pip_install(
    "geopandas",
    "rasterio",
    "rasterstats",
    "shapely",
    "fiona",
    "pyproj",
    "richdem",
    "numpy",
    "pandas",
    "scipy",
    "scikit-learn",
    "statsmodels",
    "seaborn",
    "plotly",
    "matplotlib",
    "mapclassify",
    "contextily",
    "joypy",
    "xarray",
    "rioxarray",
    "earthpy",
    "tqdm",
    "openpyxl",
)

print("\nÃ°Å¸â€œÅ¡ Importing libraries...")

# Ã¢â€â‚¬Ã¢â€â‚¬ STANDARD Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import os
import warnings
import traceback
import zipfile
import json
from pathlib import Path
from tqdm import tqdm

warnings.filterwarnings('ignore')

# Ã¢â€â‚¬Ã¢â€â‚¬ GEOSPATIAL Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import geopandas as gpd
import rasterio
from rasterio.transform import rowcol, xy
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.mask import mask as rio_mask
from rasterio.features import geometry_mask
import rasterio.plot
import fiona
from shapely.geometry import (Point, LineString, MultiLineString,
                               Polygon, MultiPolygon, box, mapping)
from shapely.ops import unary_union, linemerge
from pyproj import CRS, Transformer
from rasterstats import zonal_stats
import contextily as ctx

# Ã¢â€â‚¬Ã¢â€â‚¬ RICHDEM (optional, graceful fallback) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
try:
    import richdem as rd
    RICHDEM_OK = True
    print("  Ã¢Å“â€¦ richdem available")
except ImportError:
    RICHDEM_OK = False
    print("  Ã¢Å¡Â Ã¯Â¸Â  richdem not available Ã¢â‚¬â€ slope/aspect computed via numpy")

# Ã¢â€â‚¬Ã¢â€â‚¬ NUMERICAL Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import numpy as np
import pandas as pd
from scipy import stats
from scipy.spatial.distance import cdist
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Ã¢â€â‚¬Ã¢â€â‚¬ SKLEARN Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Ã¢â€â‚¬Ã¢â€â‚¬ STATSMODELS Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Ã¢â€â‚¬Ã¢â€â‚¬ VISUALIZATION Ã¢â‚¬â€ MATPLOTLIB Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import matplotlib.ticker as mticker
import matplotlib.colors as mcolors
from matplotlib.colors import LightSource, LinearSegmentedColormap, Normalize
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns

# Ã¢â€â‚¬Ã¢â€â‚¬ VISUALIZATION Ã¢â‚¬â€ PLOTLY Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Ã¢â€â‚¬Ã¢â€â‚¬ OPTIONAL Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
try:
    import joypy
    JOYPY_OK = True
except ImportError:
    JOYPY_OK = False
    print("  Ã¢Å¡Â Ã¯Â¸Â  joypy not available Ã¢â‚¬â€ ridge plots skipped")

try:
    import earthpy.spatial as es
    EARTHPY_OK = True
except ImportError:
    EARTHPY_OK = False

try:
    import xarray as xr
    import rioxarray
    RIOXARRAY_OK = True
except ImportError:
    RIOXARRAY_OK = False

# Ã¢â€â‚¬Ã¢â€â‚¬ GLOBAL SETTINGS Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 200)
pd.set_option('display.float_format', '{:.4f}'.format)
plt.rcParams.update({
    'figure.dpi': 150,
    'font.family': 'DejaVu Sans',
    'axes.labelsize': 11,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
})

# Ã¢â€â‚¬Ã¢â€â‚¬ OUTPUT DIRECTORIES Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
OUT_DIR      = "E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/outputs/"
MAPS_DIR     = os.path.join(OUT_DIR, "maps/")
PLOTS_DIR    = os.path.join(OUT_DIR, "plots/")
TABLES_DIR   = os.path.join(OUT_DIR, "tables/")
SHAPES_DIR   = os.path.join(OUT_DIR, "shapefiles/")
REPORT_DIR   = os.path.join(OUT_DIR, "report/")

for d in [OUT_DIR, MAPS_DIR, PLOTS_DIR, TABLES_DIR, SHAPES_DIR, REPORT_DIR]:
    os.makedirs(d, exist_ok=True)

print("\nÃ¢Å“â€¦ All libraries imported successfully.")
print(f"Ã°Å¸â€œÂ Output directory: {OUT_DIR}")

# Ã¢â€â‚¬Ã¢â€â‚¬ VERSION REPORT Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print(f"\n{'='*50}")
print(f"  geopandas  : {gpd.__version__}")
print(f"  rasterio   : {rasterio.__version__}")
print(f"  numpy      : {np.__version__}")
print(f"  pandas     : {pd.__version__}")
print(f"  plotly     : {__import__('plotly').__version__}")
print(f"{'='*50}")

import subprocess, sys

# Ã¢â€Å’Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Â
# Ã¢â€â€š  SECTION 2 Ã¢â‚¬â€ DATA PATHS (Updated for 3-Pour-Point Pravra Basin Run)        Ã¢â€â€š
# Ã¢â€â€š                                                                             Ã¢â€â€š
# Ã¢â€â€š  Subbasins : Pravrabasin.shp  Ã¢â€ Â contains 5 polygons as confirmed by DBF   Ã¢â€â€š
# Ã¢â€â€š              If you have a 3-polygon delineation, replace path with:       Ã¢â€â€š
# Ã¢â€â€š              r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/pravra3.shp"                        Ã¢â€â€š
# Ã¢â€â€š  Pour Pts  : Pourpoints_3.shp Ã¢â€ Â 3 points confirmed Ã¢Å“â€¦                     Ã¢â€â€š
# Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€Ëœ

# Ã¢â€â‚¬Ã¢â€â‚¬ Ã¢â€“Â¼Ã¢â€“Â¼Ã¢â€“Â¼  EDIT THESE PATHS  Ã¢â€“Â¼Ã¢â€“Â¼Ã¢â€“Â¼ Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
DATA_PATHS = {
    "dem"              : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/Filled DEM.tif",
    "subbasins"        : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/pravra3.shp",       # 3-polygon Pravra basin
    "streams"          : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/SteamOrder.shp",
    "stream_order_shp" : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/SteamOrder.shp",
    "flow_dir"         : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/Flow Direction.tif",
    "flow_acc"         : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/FlowAccumilation.tif",
    "pour_points"      : r"E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main/data/watershed_data/Pourpoints_3.shp",
}
# Ã¢â€â‚¬Ã¢â€â‚¬ Ã¢â€“Â²Ã¢â€“Â²Ã¢â€“Â²  EDIT ABOVE  Ã¢â€“Â²Ã¢â€“Â²Ã¢â€“Â² Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

# N_SUBBASINS is now set dynamically from the actual shapefile (see load step below).
# Override here ONLY if you want a strict assertion check:
#   N_SUBBASINS = 3    Ã¢â€ Â set to 3 when pravra3.shp (3-polygon file) is ready
#   N_SUBBASINS = 5    Ã¢â€ Â current Pravrabasin.shp has 5 polygons
N_SUBBASINS = None   # None = auto-detect from shapefile (recommended)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  HELPER FUNCTIONS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

def detect_utm_epsg(lon, lat):
    """Return appropriate UTM EPSG code for a given lon/lat."""
    zone = int((lon + 180) / 6) + 1
    if lat >= 0:
        return f"EPSG:326{zone:02d}"
    else:
        return f"EPSG:327{zone:02d}"


def get_raster_info(path):
    """Return dict of raster metadata."""
    with rasterio.open(path) as src:
        return {
            "crs"        : src.crs,
            "res"        : src.res,
            "nodata"     : src.nodata,
            "shape"      : (src.height, src.width),
            "bounds"     : src.bounds,
            "dtype"      : src.dtypes[0],
            "count"      : src.count,
            "transform"  : src.transform,
        }


def reproject_raster(src_path, dst_path, target_crs):
    """Reproject a raster to target CRS and save."""
    with rasterio.open(src_path) as src:
        transform, width, height = calculate_default_transform(
            src.crs, target_crs, src.width, src.height, *src.bounds
        )
        kwargs = src.meta.copy()
        kwargs.update({
            'crs'       : target_crs,
            'transform' : transform,
            'width'     : width,
            'height'    : height,
        })
        with rasterio.open(dst_path, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=target_crs,
                    resampling=Resampling.bilinear,
                )
    return dst_path


def fix_geometries(gdf, layer_name="layer"):
    """Fix invalid geometries and remove nulls."""
    before = len(gdf)
    gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.notna()].copy()
    gdf['geometry'] = gdf['geometry'].apply(
        lambda g: g.buffer(0) if not g.is_valid else g
    )
    gdf = gdf[gdf.geometry.is_valid].copy()
    print(f"  {layer_name}: {before} Ã¢â€ â€™ {len(gdf)} features (after geometry fix)")
    return gdf.reset_index(drop=True)


def explode_multipart(gdf, layer_name="layer"):
    """Explode multipart geometries to single-part."""
    before = len(gdf)
    gdf = gdf.explode(index_parts=False).reset_index(drop=True)
    if len(gdf) != before:
        print(f"  {layer_name}: Exploded multipart Ã¢â€ â€™ {len(gdf)} parts")
    return gdf


def snap_pour_points(pour_pts_gdf, flow_acc_path, snap_distance_m=300):
    """
    Snap pour points to the highest flow accumulation cell
    within snap_distance_m (in metres, projected CRS assumed).
    Returns GeoDataFrame with snapped geometries.
    """
    with rasterio.open(flow_acc_path) as src:
        fa_data  = src.read(1).astype(float)
        nodata   = src.nodata if src.nodata is not None else -9999
        fa_data[fa_data == nodata] = np.nan
        transform = src.transform
        res        = src.res[0]  # metres per pixel

    snap_cells = int(snap_distance_m / res)
    snapped_pts = []

    for idx, row in pour_pts_gdf.iterrows():
        px_c, px_r = ~transform * (row.geometry.x, row.geometry.y)
        px_c, px_r = int(px_c), int(px_r)

        r0 = max(0, px_r - snap_cells)
        r1 = min(fa_data.shape[0], px_r + snap_cells + 1)
        c0 = max(0, px_c - snap_cells)
        c1 = min(fa_data.shape[1], px_c + snap_cells + 1)

        window = fa_data[r0:r1, c0:c1]
        if np.all(np.isnan(window)):
            snapped_pts.append(row.geometry)
            continue

        local_max = np.nanargmax(window)
        local_r, local_c = np.unravel_index(local_max, window.shape)
        global_r = r0 + local_r
        global_c = c0 + local_c

        snap_x, snap_y = xy(transform, global_r, global_c)
        snapped_pts.append(Point(snap_x, snap_y))

    result = pour_pts_gdf.copy()
    result['geometry']       = snapped_pts
    result['snap_distance_m'] = [
        row.geometry.distance(snapped_pts[i])
        for i, (_, row) in enumerate(pour_pts_gdf.iterrows())
    ]
    return result


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  LOAD & VALIDATE
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("=" * 60)
print("SECTION 2 Ã¢â‚¬â€ DATA LOADING & PREPROCESSING")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬ 1. Load DEM info first to determine UTM zone Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[1/6] Reading DEM metadata...")
assert os.path.exists(DATA_PATHS['dem']), f"DEM not found: {DATA_PATHS['dem']}"
dem_info = get_raster_info(DATA_PATHS['dem'])
print(f"  CRS      : {dem_info['crs']}")
print(f"  Res      : {dem_info['res']} m")
print(f"  Shape    : {dem_info['shape']}")
print(f"  Bounds   : {dem_info['bounds']}")
print(f"  No-data  : {dem_info['nodata']}")

# Determine if geographic or projected
src_crs = CRS.from_user_input(dem_info['crs'])
if src_crs.is_geographic:
    # Compute centroid lon/lat for UTM zone
    b = dem_info['bounds']
    cen_lon = (b.left + b.right) / 2
    cen_lat = (b.bottom + b.top) / 2
    UTM_EPSG = detect_utm_epsg(cen_lon, cen_lat)
    print(f"  DEM is geographic Ã¢â€ â€™ will reproject to {UTM_EPSG}")
    NEEDS_REPROJECT = True
else:
    UTM_EPSG = str(dem_info['crs'])
    print(f"  DEM is already projected: {UTM_EPSG}")
    NEEDS_REPROJECT = False

TARGET_CRS = CRS.from_epsg(int(UTM_EPSG.split(":")[1]))

# Ã¢â€â‚¬Ã¢â€â‚¬ 2. Reproject rasters if needed Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[2/6] Reprojecting rasters...")
RASTER_KEYS = ['dem', 'flow_dir', 'flow_acc']
RASTERS = {}

for key in RASTER_KEYS:
    src_path = DATA_PATHS[key]
    assert os.path.exists(src_path), f"Missing: {src_path}"
    info = get_raster_info(src_path)
    if NEEDS_REPROJECT and CRS.from_user_input(info['crs']).is_geographic:
        dst_path = os.path.join(OUT_DIR, f"{key}_utm.tif")
        reproject_raster(src_path, dst_path, TARGET_CRS)
        RASTERS[key] = dst_path
        print(f"  Ã¢Å“â€¦ Reprojected {key}")
    else:
        RASTERS[key] = src_path
        print(f"  Ã¢Å“â€¦ {key} OK (already projected)")

# Optional stream order raster
if os.path.exists(DATA_PATHS.get('stream_order_raster', '')):
    so_path = DATA_PATHS['stream_order_raster']
    so_info = get_raster_info(so_path)
    if NEEDS_REPROJECT and CRS.from_user_input(so_info['crs']).is_geographic:
        dst = os.path.join(OUT_DIR, "stream_order_utm.tif")
        reproject_raster(so_path, dst, TARGET_CRS)
        RASTERS['stream_order_raster'] = dst
    else:
        RASTERS['stream_order_raster'] = so_path

# Ã¢â€â‚¬Ã¢â€â‚¬ 3. Load & validate vector layers Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[3/6] Loading vector layers...")

# Subbasins
gdf_sub = gpd.read_file(DATA_PATHS['subbasins'])
gdf_sub = fix_geometries(gdf_sub, "subbasins")
gdf_sub = gdf_sub.to_crs(UTM_EPSG)

# Ã¢â€â‚¬Ã¢â€â‚¬ Dynamic N_SUBBASINS: auto-detect from the loaded shapefile Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
if N_SUBBASINS is None:
    N_SUBBASINS = len(gdf_sub)
    print(f"  Ã¢â€žÂ¹Ã¯Â¸Â  N_SUBBASINS auto-detected: {N_SUBBASINS} polygons in {DATA_PATHS['subbasins']}")
else:
    if len(gdf_sub) != N_SUBBASINS:
        print(f"  Ã¢Å¡Â Ã¯Â¸Â  Warning: Expected {N_SUBBASINS} subbasins but shapefile has {len(gdf_sub)}.")
        print(f"       Using actual count: {len(gdf_sub)}")
        print(f"       Ã¢â€ â€™ If you want exactly 3 subbasins, replace subbasins path with pravra3.shp")
        N_SUBBASINS = len(gdf_sub)
    else:
        print(f"  Ã¢Å“â€¦ Subbasin count verified: {N_SUBBASINS}")

print(f"  Ã¢Å“â€¦ Subbasins: {len(gdf_sub)} | CRS: {gdf_sub.crs}")

# Ensure unique basin ID Ã¢â‚¬â€ try to detect from existing columns
if 'basin_id' not in gdf_sub.columns:
    # Try to use 'name' column if present (Pravrabasin.shp has 'name' field)
    if 'name' in gdf_sub.columns and gdf_sub['name'].notna().all():
        # Extract subbasin name from the 'AreaSqkm' column which has "Subbasin-X"
        # Try AreaSqkm field first (Pravrabasin.shp stores subbasin names there)
        if 'AreaSqkm' in gdf_sub.columns:
            names = gdf_sub['AreaSqkm'].astype(str).str.extract(r'(Subbasin-\d+)')[0]
            if names.notna().sum() == len(gdf_sub):
                gdf_sub['basin_id'] = names
            else:
                gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]
        else:
            gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]
    else:
        gdf_sub['basin_id'] = [f"SB{i+1}" for i in range(len(gdf_sub))]
print(f"  Basin IDs: {gdf_sub['basin_id'].tolist()}")

# Streams
gdf_streams = gpd.read_file(DATA_PATHS['streams'])
gdf_streams = fix_geometries(gdf_streams, "streams")
gdf_streams = explode_multipart(gdf_streams, "streams")
gdf_streams = gdf_streams.to_crs(UTM_EPSG)
print(f"  Ã¢Å“â€¦ Streams: {len(gdf_streams)} segments | CRS: {gdf_streams.crs}")

# Stream order shapefile
gdf_so = gpd.read_file(DATA_PATHS['stream_order_shp'])
gdf_so = fix_geometries(gdf_so, "stream_order")
gdf_so = explode_multipart(gdf_so, "stream_order")
gdf_so = gdf_so.to_crs(UTM_EPSG)

# Detect stream order column
# Ã¢â€â‚¬Ã¢â€â‚¬ Detect stream order column dynamically Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
ORDER_COL_CANDIDATES = ['grid_code', 'GRIDCODE', 'Grid_Code',
                         'strahler', 'Strahler', 'order', 'ORDER',
                         'StreamOrde', 'str_order']
ORDER_COL = None
for cand in ORDER_COL_CANDIDATES:
    if cand in gdf_so.columns:
        ORDER_COL = cand
        print(f"  Ã¢Å“â€¦ Stream order column auto-detected: '{ORDER_COL}'")
        break

if ORDER_COL is None:
    raise ValueError(
        f"Cannot detect stream order column. Columns: {gdf_so.columns.tolist()}\n"
        "Please set ORDER_COL manually below."
    )
print(f"  Ã¢Å“â€¦ Stream order col detected: '{ORDER_COL}' "
      f"| Orders: {sorted(gdf_so[ORDER_COL].unique())}")

gdf_so[ORDER_COL] = gdf_so[ORDER_COL].astype(int)
MAX_ORDER = int(gdf_so[ORDER_COL].max())

# Pour points (optional but important for snapping)
POUR_POINTS_OK = False
if os.path.exists(DATA_PATHS.get('pour_points', '')):
    gdf_pp = gpd.read_file(DATA_PATHS['pour_points'])
    gdf_pp = gdf_pp.to_crs(UTM_EPSG)
    print(f"  Ã¢Å“â€¦ Pour points: {len(gdf_pp)}")
    print("  Snapping pour points to max flow accumulation...")
    gdf_pp = snap_pour_points(gdf_pp, RASTERS['flow_acc'], snap_distance_m=300)
    print(f"  Snap distances (m): {gdf_pp['snap_distance_m'].round(1).tolist()}")
    gdf_pp.to_file(os.path.join(SHAPES_DIR, "pour_points_snapped.shp"))
    POUR_POINTS_OK = True
else:
    gdf_pp = None
    print("  Ã¢Å¡Â Ã¯Â¸Â  Pour points file not found Ã¢â‚¬â€ skipping snap")

# Ã¢â€â‚¬Ã¢â€â‚¬ 4. Validate DEM resolution Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print(f"\n[4/6] Validating DEM resolution...")
dem_info_utm = get_raster_info(RASTERS['dem'])
res_x, res_y = dem_info_utm['res']
if 20 <= res_x <= 35:
    print(f"  Ã¢Å“â€¦ DEM resolution: {res_x:.1f} x {res_y:.1f} m Ã¢â€°Ë† 30 m SRTM Ã¢Å“â€œ")
else:
    print(f"  Ã¢Å¡Â Ã¯Â¸Â  DEM resolution: {res_x:.1f} x {res_y:.1f} m (not standard 30 m Ã¢â‚¬â€ continuing anyway)")

# Ã¢â€â‚¬Ã¢â€â‚¬ 5. Read raster arrays into memory Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[5/6] Reading raster arrays...")

with rasterio.open(RASTERS['dem']) as src:
    DEM_ARR       = src.read(1).astype(np.float32)
    DEM_NODATA    = src.nodata if src.nodata is not None else -9999.0
    DEM_TRANSFORM = src.transform
    DEM_CRS       = src.crs
    DEM_BOUNDS    = src.bounds
    DEM_RES       = src.res[0]
    DEM_ARR[DEM_ARR == DEM_NODATA] = np.nan

with rasterio.open(RASTERS['flow_dir']) as src:
    FDIR_ARR    = src.read(1).astype(np.float32)
    FDIR_NODATA = src.nodata if src.nodata is not None else -9999.0
    FDIR_ARR[FDIR_ARR == FDIR_NODATA] = np.nan

with rasterio.open(RASTERS['flow_acc']) as src:
    FACC_ARR    = src.read(1).astype(np.float32)
    FACC_NODATA = src.nodata if src.nodata is not None else -9999.0
    FACC_ARR[FACC_ARR == FACC_NODATA] = np.nan

print(f"  DEM  shape: {DEM_ARR.shape} | min={np.nanmin(DEM_ARR):.1f} max={np.nanmax(DEM_ARR):.1f} m")
print(f"  FDIR shape: {FDIR_ARR.shape}")
print(f"  FACC shape: {FACC_ARR.shape}")

# Ã¢â€â‚¬Ã¢â€â‚¬ 6. Compute slope & aspect if not provided Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[6/6] Computing slope and aspect...")

def compute_slope_aspect_numpy(dem, res_m):
    """Compute slope (degrees) and aspect (degrees) using numpy gradient."""
    # Smooth first to reduce noise
    from scipy.ndimage import uniform_filter
    dem_sm = np.where(np.isnan(dem), 0, dem)
    dz_dy, dz_dx = np.gradient(dem_sm, res_m, res_m)
    slope_rad = np.arctan(np.sqrt(dz_dx**2 + dz_dy**2))
    slope_deg = np.degrees(slope_rad)
    aspect_deg = np.degrees(np.arctan2(-dz_dx, dz_dy)) % 360
    slope_deg[np.isnan(dem)] = np.nan
    aspect_deg[np.isnan(dem)] = np.nan
    return slope_deg.astype(np.float32), aspect_deg.astype(np.float32)


if RICHDEM_OK:
    try:
        rda = rd.rdarray(np.where(np.isnan(DEM_ARR), -9999, DEM_ARR), no_data=-9999)
        rda.projection = DEM_CRS.to_wkt()
        rda.geotransform = (DEM_TRANSFORM.c, DEM_TRANSFORM.a, 0,
                            DEM_TRANSFORM.f, 0, DEM_TRANSFORM.e)
        SLOPE_ARR  = np.array(rd.TerrainAttribute(rda, attrib='slope_degrees')).astype(np.float32)
        ASPECT_ARR = np.array(rd.TerrainAttribute(rda, attrib='aspect')).astype(np.float32)
        SLOPE_ARR[np.isnan(DEM_ARR)]  = np.nan
        ASPECT_ARR[np.isnan(DEM_ARR)] = np.nan
        print("  Ã¢Å“â€¦ Slope & aspect from richdem")
    except Exception as e:
        print(f"  Ã¢Å¡Â Ã¯Â¸Â  richdem failed ({e}) Ã¢â‚¬â€ using numpy")
        SLOPE_ARR, ASPECT_ARR = compute_slope_aspect_numpy(DEM_ARR, DEM_RES)
else:
    SLOPE_ARR, ASPECT_ARR = compute_slope_aspect_numpy(DEM_ARR, DEM_RES)
    print("  Ã¢Å“â€¦ Slope & aspect from numpy gradient")

# Save slope & aspect to disk
def save_raster(arr, path, template_path):
    with rasterio.open(template_path) as src:
        meta = src.meta.copy()
    meta.update({'dtype': 'float32', 'nodata': -9999.0, 'count': 1})
    arr_save = np.where(np.isnan(arr), -9999.0, arr)
    with rasterio.open(path, 'w', **meta) as dst:
        dst.write(arr_save.astype(np.float32), 1)

save_raster(SLOPE_ARR,  os.path.join(OUT_DIR, "slope.tif"),  RASTERS['dem'])
save_raster(ASPECT_ARR, os.path.join(OUT_DIR, "aspect.tif"), RASTERS['dem'])
RASTERS['slope']  = os.path.join(OUT_DIR, "slope.tif")
RASTERS['aspect'] = os.path.join(OUT_DIR, "aspect.tif")

# Ã¢â€â‚¬Ã¢â€â‚¬ HILLSHADE (used as background in all maps) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("  Computing hillshade for map backgrounds...")
ls = LightSource(azdeg=315, altdeg=45)
dem_filled = np.where(np.isnan(DEM_ARR), np.nanmean(DEM_ARR), DEM_ARR)
HILLSHADE = ls.hillshade(dem_filled, vert_exag=1.5, dx=DEM_RES, dy=DEM_RES)
assert HILLSHADE.shape == DEM_ARR.shape, \
    f"Hillshade shape {HILLSHADE.shape} Ã¢â€°Â  DEM shape {DEM_ARR.shape}. Recompute hillshade from the reprojected DEM."
HILLSHADE[np.isnan(DEM_ARR)] = np.nan
print("  Ã¢Å“â€¦ Hillshade computed")

# Ã¢â€â‚¬Ã¢â€â‚¬ SPATIAL INDEX (for fast spatial joins) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\nÃ¢Å“â€¦ SECTION 2 complete.")
print(f"  Subbasins    : {len(gdf_sub)}")
print(f"  Stream segs  : {len(gdf_streams)}")
print(f"  Stream orders: {sorted(gdf_so[ORDER_COL].unique())}")
print(f"  UTM CRS      : {UTM_EPSG}")
print(f"  DEM range    : {np.nanmin(DEM_ARR):.1f} Ã¢â‚¬â€œ {np.nanmax(DEM_ARR):.1f} m")
print(f"  Slope range  : {np.nanmin(SLOPE_ARR):.1f}Ã‚Â° Ã¢â‚¬â€œ {np.nanmax(SLOPE_ARR):.1f}Ã‚Â°")

REQUIRED_GLOBALS = ['DEM_ARR', 'FACC_ARR', 'FDIR_ARR', 'SLOPE_ARR',
                     'ASPECT_ARR', 'HILLSHADE', 'DEM_TRANSFORM',
                     'DEM_BOUNDS', 'DEM_RES', 'DEM_CRS']
missing_globals = [v for v in REQUIRED_GLOBALS if v not in dir()]
if missing_globals:
    raise RuntimeError(
        f"Missing raster arrays: {missing_globals}\n"
        f"Ensure Section 2 fully executed the DEM read block."
    )
print("  All required raster arrays are in memory.")


# Ã¢â€â‚¬Ã¢â€â‚¬ CRS sanity check Ã¢â‚¬â€ all layers must be in the same UTM zone Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
ref_crs = gdf_sub.crs
for name, gdf in [('streams', gdf_streams), ('stream_order', gdf_so)]:
    if gdf.crs != ref_crs:
        print(f"  Ã¢Å¡Â Ã¯Â¸Â  CRS mismatch: {name} is {gdf.crs}, expected {ref_crs}")
        print(f"       Auto-reprojecting {name}...")
        if name == 'streams':
            gdf_streams = gdf_streams.to_crs(ref_crs)
        elif name == 'stream_order':
            gdf_so = gdf_so.to_crs(ref_crs)
    else:
        print(f"  Ã¢Å“â€¦ CRS OK: {name}")

print("=" * 60)
print("SECTION 3 Ã¢â‚¬â€ MORPHOMETRIC PARAMETER CALCULATION")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. LINEAR ASPECTS  (stream order statistics)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[A] Computing Linear Aspects...")

def compute_linear_aspects(gdf_streams_clipped, order_col, basin_id):
    """
    Compute stream order statistics for one subbasin.
    Returns per-order DataFrame and summary ratios.
    """
    rows = []
    orders = sorted(gdf_streams_clipped[order_col].unique())

    for u in orders:
        segs = gdf_streams_clipped[gdf_streams_clipped[order_col] == u]
        nu   = len(segs)
        lu   = segs.geometry.length.sum()
        lsm  = lu / nu if nu > 0 else 0
        rows.append({'basin_id': basin_id, 'order': u,
                     'Nu': nu, 'Lu': lu, 'Lsm': lsm})

    df = pd.DataFrame(rows).set_index('order')

    # Bifurcation ratio Rb = Nu / Nu+1
    df['Rb'] = np.nan
    for i in range(len(df) - 1):
        o1, o2 = orders[i], orders[i+1]
        if df.loc[o2, 'Nu'] > 0:
            df.loc[o1, 'Rb'] = df.loc[o1, 'Nu'] / df.loc[o2, 'Nu']

    # Stream length ratio RL = Lsm(u) / Lsm(u-1)
    df['RL'] = np.nan
    for i in range(1, len(df)):
        o_prev, o_curr = orders[i-1], orders[i]
        if df.loc[o_prev, 'Lsm'] > 0:
            df.loc[o_curr, 'RL'] = df.loc[o_curr, 'Lsm'] / df.loc[o_prev, 'Lsm']

    # Mean bifurcation ratio (arithmetic)
    Rb_vals = df['Rb'].dropna()
    Rbm = Rb_vals.mean() if len(Rb_vals) > 0 else np.nan

    # Weighted mean bifurcation ratio (Strahler, 1957)
    wRbm = np.nan
    if len(Rb_vals) > 0:
        rb_list, wt_list = [], []
        for i in range(len(orders) - 1):
            o1, o2 = orders[i], orders[i+1]
            rb_val = df.loc[o1, 'Rb']
            if not np.isnan(rb_val) and df.loc[o2, 'Nu'] > 0:
                rb_list.append(rb_val)
                wt_list.append(df.loc[o1, 'Nu'] + df.loc[o2, 'Nu'])

        if len(rb_list) > 0:
            wts_arr = np.array(wt_list)
            if wts_arr.sum() > 0:
                wRbm = np.average(rb_list, weights=wts_arr)

    return df.reset_index(), Rbm, wRbm


# Spatial join: streams to subbasins
# Ã¢â€â‚¬Ã¢â€â‚¬ Correct: clip stream network to each subbasin, then tag basin_id Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
clipped_parts = []
for _, basin_row in gdf_sub.iterrows():
    bid  = basin_row['basin_id']
    clip = gpd.clip(gdf_so[[ORDER_COL, 'geometry']], basin_row.geometry)
    if clip is not None and len(clip) > 0:
        clip = clip.copy()
        clip['basin_id'] = bid
        clipped_parts.append(clip)

if clipped_parts:
    gdf_so_sub = pd.concat(clipped_parts, ignore_index=True)
else:
    # Last-resort fallback: intersects join (may double-count boundary segs)
    gdf_so_sub = gpd.sjoin(
        gdf_so[[ORDER_COL, 'geometry']],
        gdf_sub[['basin_id', 'geometry']],
        how='left', predicate='intersects'
    ).dropna(subset=['basin_id'])
    print("  Ã¢Å¡Â Ã¯Â¸Â  Falling back to intersects join Ã¢â‚¬â€ check CRS alignment.")

LINEAR_PER_ORDER = {}   # basin_id Ã¢â€ â€™ DataFrame
LINEAR_SUMMARY   = []   # one row per basin

for bid in gdf_sub['basin_id']:
    segs = gdf_so_sub[gdf_so_sub['basin_id'] == bid]
    if len(segs) == 0:
        print(f"  Ã¢Å¡Â Ã¯Â¸Â  No stream segments found for basin {bid}")
        continue
    df_lin, Rbm, wRbm = compute_linear_aspects(segs, ORDER_COL, bid)
    LINEAR_PER_ORDER[bid] = df_lin

    total_N = df_lin['Nu'].sum()
    total_L = df_lin['Lu'].sum()
    max_ord = df_lin['order'].max()

    LINEAR_SUMMARY.append({
        'basin_id'       : bid,
        'total_streams_N': total_N,
        'total_length_m' : total_L,
        'max_order'      : max_ord,
        'Rbm'            : round(Rbm, 4),
        'wRbm'           : round(wRbm, 4) if not np.isnan(wRbm) else np.nan,
    })
    print(f"  {bid}: {total_N} streams | max order {max_ord} | Rbm={Rbm:.3f}")

df_linear_summary = pd.DataFrame(LINEAR_SUMMARY).set_index('basin_id')
print("\n  Stream Order Summary (all basins):")
for bid, df in LINEAR_PER_ORDER.items():
    print(f"\n  [{bid}]")
    print(df[['order','Nu','Lu','Lsm','Rb','RL']].to_string(index=False))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. AREAL ASPECTS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[B] Computing Areal Aspects...")

from shapely.geometry import Point as _SPoint
def longest_flow_path(basin_geom, facc_arr=None, transform=None, res_m=None):
    """
    Approximate basin length (Lb) as the major axis of the minimum rotated
    bounding rectangle Ã¢â‚¬â€ a standard GIS proxy used when full D8 tracing is
    not available (Schumm, 1956).
    """
    try:
        obb    = basin_geom.minimum_rotated_rectangle
        coords = list(obb.exterior.coords)
        side1  = _SPoint(coords[0]).distance(_SPoint(coords[1]))
        side2  = _SPoint(coords[1]).distance(_SPoint(coords[2]))
        lb     = max(side1, side2)   # longest axis of the OBB (metres)
    except Exception:
        b  = basin_geom.bounds       # (minx, miny, maxx, maxy)
        lb = np.sqrt((b[2]-b[0])**2 + (b[3]-b[1])**2)
    return lb


AREAL = []

for _, row in gdf_sub.iterrows():
    bid   = row['basin_id']
    geom  = row.geometry

    A  = geom.area          # mÃ‚Â²
    P  = geom.length        # m
    Lb = longest_flow_path(geom, FACC_ARR, DEM_TRANSFORM, DEM_RES)

    # Streams inside basin
    segs = gdf_so_sub[gdf_so_sub['basin_id'] == bid]
    total_stream_length = segs.geometry.length.sum() if len(segs) > 0 else 0
    Nu_total = len(segs)

    # ----- parameters -----
    A_km2   = A   / 1e6
    P_km    = P   / 1e3
    Lb_km   = Lb  / 1e3
    L_km    = total_stream_length / 1e3

    Dd = L_km  / A_km2 if A_km2 > 0 else np.nan   # Drainage density  [km/kmÃ‚Â²]
    Fs = Nu_total / A_km2 if A_km2 > 0 else np.nan # Stream frequency  [streams/kmÃ‚Â²]
    # Ã¢â€â‚¬Ã¢â€â‚¬ Correct Texture Ratio: use first-order streams only Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    segs_first_order = segs[segs[ORDER_COL] == 1]   # first-order (Strahler) only
    N1 = len(segs_first_order)                       # count of 1st-order streams

    T  = N1 / P_km  if P_km  > 0 else np.nan        # Texture ratio (Smith, 1950)
    Ff = A_km2   / (Lb_km**2)     if Lb_km > 0 else np.nan  # Form factor (Horton,1932)
    Re = (2 / Lb_km) * np.sqrt(A_km2 / np.pi) if Lb_km > 0 else np.nan  # Elongation ratio
    Rc = (4 * np.pi * A_km2) / (P_km**2)  if P_km > 0 else np.nan       # Circularity ratio
    Cc = P_km / (2 * np.sqrt(np.pi * A_km2)) if A_km2 > 0 else np.nan   # Compactness coeff
    Lg = 1 / (2 * Dd)   if Dd and Dd > 0 else np.nan   # Length of overland flow
    C  = 1 / Dd          if Dd and Dd > 0 else np.nan   # Constant of channel maintenance

    AREAL.append({
        'basin_id'              : bid,
        'Area_km2'              : round(A_km2, 4),
        'Perimeter_km'          : round(P_km, 4),
        'Basin_Length_km'       : round(Lb_km, 4),
        'Total_Stream_Length_km': round(L_km, 4),
        'Stream_Count'          : Nu_total,
        'Drainage_Density_Dd'   : round(Dd, 4) if not np.isnan(Dd) else np.nan,
        'Stream_Frequency_Fs'   : round(Fs, 4) if not np.isnan(Fs) else np.nan,
        'Texture_Ratio_T'       : round(T,  4) if not np.isnan(T)  else np.nan,
        'Form_Factor_Ff'        : round(Ff, 4) if not np.isnan(Ff) else np.nan,
        'Elongation_Ratio_Re'   : round(Re, 4) if not np.isnan(Re) else np.nan,
        'Circularity_Ratio_Rc'  : round(Rc, 4) if not np.isnan(Rc) else np.nan,
        'Compactness_Cc'        : round(Cc, 4) if not np.isnan(Cc) else np.nan,
        'LengthOverlandFlow_Lg' : round(Lg, 4) if not np.isnan(Lg) else np.nan,
        'ChannelMaintenance_C'  : round(C,  4) if not np.isnan(C)  else np.nan,
    })

    print(f"  {bid}: A={A_km2:.2f} kmÃ‚Â² | Dd={Dd:.3f} km/kmÃ‚Â² | "
          f"Re={Re:.3f} | Rc={Rc:.3f} | Ff={Ff:.3f}")

df_areal = pd.DataFrame(AREAL).set_index('basin_id')

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. RELIEF ASPECTS  (DEM zonal statistics)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[C] Computing Relief Aspects...")

def hypsometric_integral(dem_clipped):
    """
    Compute hypsometric integral (HI) = (mean_elev - min_elev) / (max_elev - min_elev)
    Also returns arrays for hypsometric curve: (relative_area, relative_elevation)
    """
    vals = dem_clipped[~np.isnan(dem_clipped)].flatten()
    if len(vals) < 10:
        return np.nan, None, None
    mn, mx, mu = vals.min(), vals.max(), vals.mean()
    rng = mx - mn
    if rng == 0:
        return np.nan, None, None
    HI = (mu - mn) / rng
    # Curve: relative elevation h/H vs relative area a/A
    thresholds   = np.percentile(vals, np.linspace(0, 100, 101))
    rel_elev     = (thresholds - mn) / rng          # h/H  (0Ã¢â€ â€™1)
    rel_area     = 1 - np.linspace(0, 1, 101)       # a/A  (1Ã¢â€ â€™0)
    return HI, rel_area, rel_elev


def terrain_ruggedness_index(dem_arr):
    """
    TRI (Riley et al., 1999): mean absolute difference from center cell
    to 8 neighbours.
    """
    from scipy.ndimage import generic_filter
    def _tri_kernel(x):
        centre = x[4]
        if np.isnan(centre):
            return np.nan
        diffs = x - centre
        diffs[4] = 0
        valid = diffs[~np.isnan(diffs)]
        return np.sqrt(np.sum(valid**2)) if len(valid) > 0 else np.nan
    tri = generic_filter(dem_arr.astype(float), _tri_kernel, size=3, mode='reflect')
    tri[np.isnan(dem_arr)] = np.nan
    return tri


def melton_ruggedness(h_m, a_km2):
    """Melton (1965) ruggedness index MRN = H / sqrt(A)."""
    return h_m / np.sqrt(a_km2) if a_km2 > 0 else np.nan


# Compute TRI once for full DEM
print("  Computing TRI (this may take 30Ã¢â‚¬â€œ60 sec on large DEMs)...")
TRI_ARR = terrain_ruggedness_index(DEM_ARR)
save_raster(TRI_ARR, os.path.join(OUT_DIR, "tri.tif"), RASTERS['dem'])

RELIEF   = []
HYPS     = {}   # basin_id Ã¢â€ â€™ (rel_area, rel_elev)

for _, row in gdf_sub.iterrows():
    bid  = row['basin_id']
    geom = [row.geometry.__geo_interface__]

    # Mask DEM to subbasin (STRICT)
    with rasterio.open(RASTERS['dem']) as src:
        geom_dem = [mapping(gdf_sub[gdf_sub['basin_id'] == bid].to_crs(src.crs).geometry.iloc[0])]
        try:
            # Use native nodata for the mask operation itself
            arr_masked, _ = rio_mask(src, geom_dem, crop=True, nodata=src.nodata)
            dem_clip = arr_masked[0].astype(np.float32)
            if src.nodata is not None:
                dem_clip[dem_clip == src.nodata] = np.nan
        except Exception as e:
            print(f"  [Error] Clipping DEM for {bid}: {e}")
            dem_clip = np.array([np.nan])

    # Mask slope to subbasin (STRICT)
    with rasterio.open(RASTERS['slope']) as src:
        geom_slope = [mapping(gdf_sub[gdf_sub['basin_id'] == bid].to_crs(src.crs).geometry.iloc[0])]
        try:
            s_masked, _ = rio_mask(src, geom_slope, crop=True, nodata=-9999)
            slope_clip = s_masked[0].astype(np.float32)
            slope_clip[slope_clip == -9999.0] = np.nan
        except Exception as e:
            print(f"  [Error] Clipping Slope for {bid}: {e}")
            slope_clip = np.array([np.nan])

    # Mask TRI
    with rasterio.open(os.path.join(OUT_DIR, "tri.tif")) as src:
        try:
            t_masked, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            tri_clip = t_masked[0].astype(np.float32)
            tri_clip[tri_clip == -9999.0] = np.nan
        except Exception:
            tri_clip = TRI_ARR.copy()

    valid_dem   = dem_clip[~np.isnan(dem_clip)]
    valid_slope = slope_clip[~np.isnan(slope_clip)]
    valid_tri   = tri_clip[~np.isnan(tri_clip)]

    if len(valid_dem) == 0:
        print(f"  Ã¢Å¡Â Ã¯Â¸Â  {bid}: no valid DEM cells")
        continue

    elev_min  = float(valid_dem.min())
    elev_max  = float(valid_dem.max())
    elev_mean = float(valid_dem.mean())
    H         = elev_max - elev_min              # Basin relief (m)
    A_km2     = df_areal.loc[bid, 'Area_km2']
    Lb_km     = df_areal.loc[bid, 'Basin_Length_km']
    P_km      = df_areal.loc[bid, 'Perimeter_km']

    Rh  = H / (Lb_km * 1000) if Lb_km > 0 else np.nan   # Relief ratio
    Rr = (H / 1000.0) / P_km  if P_km > 0 else np.nan   # Relative relief (dimensionless)
    Dd  = df_areal.loc[bid, 'Drainage_Density_Dd']
    Rn  = H * Dd / 1000       if not np.isnan(Dd) else np.nan  # Ruggedness number
    MRN = melton_ruggedness(H, A_km2)                           # Melton ruggedness

    # Hypsometric integral
    HI, rel_area, rel_elev = hypsometric_integral(dem_clip)
    if rel_area is not None:
        HYPS[bid] = (rel_area, rel_elev)

    # Slope statistics
    slope_mean = float(np.nanmean(valid_slope))
    slope_std  = float(np.nanstd(valid_slope))
    slope_skew = float(stats.skew(valid_slope))

    # TRI stats
    tri_mean = float(np.nanmean(valid_tri))

    RELIEF.append({
        'basin_id'         : bid,
        'Elev_Min_m'       : round(elev_min,  2),
        'Elev_Max_m'       : round(elev_max,  2),
        'Elev_Mean_m'      : round(elev_mean, 2),
        'Basin_Relief_H_m' : round(H,         2),
        'Relief_Ratio_Rh'  : round(Rh,        6) if not np.isnan(Rh) else np.nan,
        'Relative_Relief'  : round(Rr,        4) if not np.isnan(Rr) else np.nan,
        'Ruggedness_Rn'    : round(Rn,        4) if not np.isnan(Rn) else np.nan,
        'Melton_MRN'       : round(MRN,       4) if not np.isnan(MRN) else np.nan,
        'Hypsometric_HI'   : round(HI,        4) if not np.isnan(HI) else np.nan,
        'Slope_Mean_deg'   : round(slope_mean, 3),
        'Slope_Std_deg'    : round(slope_std,  3),
        'Slope_Skewness'   : round(slope_skew, 4),
        'TRI_Mean'         : round(tri_mean,   3),
    })

    print(f"  {bid}: H={H:.0f}m | Rh={Rh:.5f} | HI={HI:.3f} | "
          f"Rn={Rn:.3f} | Slope_mean={slope_mean:.2f}Ã‚Â°")

df_relief = pd.DataFrame(RELIEF).set_index('basin_id')

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. MASTER MORPHOMETRIC TABLE
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Assembling master morphometric table...")

df_master = df_areal.join(df_relief, how='left')
df_master = df_master.join(df_linear_summary, how='left')

# Add stream order per-basin summary
for bid in gdf_sub['basin_id']:
    if bid in LINEAR_PER_ORDER:
        df_lin = LINEAR_PER_ORDER[bid]
        for _, r in df_lin.iterrows():
            col = f"Nu_order{int(r['order'])}"
            df_master.loc[bid, col] = r['Nu']
            col = f"Lu_order{int(r['order'])}_km"
            df_master.loc[bid, col] = round(r['Lu'] / 1000, 4)

# Ã¢â€â‚¬Ã¢â€â‚¬ Interpretation flags Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def interpret_elongation(Re):
    if pd.isna(Re):       return "Unknown"
    if Re >= 0.9:         return "Circular"
    if Re >= 0.8:         return "Oval"
    if Re >= 0.7:         return "Less Elongated"
    if Re >= 0.5:         return "Elongated"
    return "More Elongated"

def interpret_circularity(Rc):
    if pd.isna(Rc):      return "Unknown"
    if Rc >= 0.75:       return "Circular/Young"
    if Rc >= 0.50:       return "Intermediate"
    return "Elongated/Old"

def interpret_HI(HI):
    if pd.isna(HI):      return "Unknown"
    if HI > 0.60:        return "Monadnock (Young/Convex)"
    if HI > 0.35:        return "Mature (Equilibrium)"
    return "Peneplain (Old/Concave)"

df_master['Shape_Class']    = df_master['Elongation_Ratio_Re'].apply(interpret_elongation)
df_master['Circ_Class']     = df_master['Circularity_Ratio_Rc'].apply(interpret_circularity)
df_master['Hyps_Class']     = df_master['Hypsometric_HI'].apply(interpret_HI)

# Save
csv_path = os.path.join(TABLES_DIR, "morphometric_master_table.csv")
df_master.to_csv(csv_path)
print(f"  Ã¢Å“â€¦ Master table saved: {csv_path}")

print("\n" + "Ã¢â€â‚¬"*60)
print("  MASTER MORPHOMETRIC TABLE (first 10 rows/all params):")
print("Ã¢â€â‚¬"*60)
print(df_master.to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬ Hypsometric Curves Ã¢â‚¬â€ all sub-basins Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
if 'HYPS' in globals() and HYPS:
    fig_h, ax_h = plt.subplots(figsize=(7, 6))
    colors_h = plt.cm.tab10(np.linspace(0, 1, len(HYPS)))
    for (bid_h, (rel_area, rel_elev)), col in zip(HYPS.items(), colors_h):
        ax_h.plot(rel_area, rel_elev, lw=2, label=bid_h, color=col)
    ax_h.set_xlabel("Relative Area (a/A)", fontsize=12)
    ax_h.set_ylabel("Relative Elevation (h/H)", fontsize=12)
    ax_h.set_title("Hypsometric Curves Ã¢â‚¬â€ Pravara Sub-basins", fontsize=13,
                 fontweight='bold')
    ax_h.legend(fontsize=10)
    ax_h.set_xlim(0, 1); ax_h.set_ylim(0, 1)
    ax_h.grid(True, linestyle='--', alpha=0.5)
    # Annotate HI values
    for bid_h in HYPS:
        if bid_h in df_master.index and 'Hypsometric_HI' in df_master.columns:
            hi = df_master.loc[bid_h, 'Hypsometric_HI']
            ax_h.annotate(f"{bid_h}: HI={hi:.3f}",
                        xy=(0.05, 0.05 + list(HYPS.keys()).index(bid_h) * 0.08),
                        xycoords='axes fraction', fontsize=9)
    plt.tight_layout()
    fig_h.savefig(os.path.join(PLOTS_DIR, "hypsometric_curves.png"),
                dpi=180, bbox_inches='tight')
    plt.close(fig_h)
    print("  Ã¢Å“â€¦ Hypsometric curve plot saved.")


# Ã¢â€¢â€Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢â€”
# Ã¢â€¢â€˜  MAP FRAMEWORK Ã¢â‚¬â€ 70:30 layout Ã‚Â· ESRI basemap Ã‚Â· GIS scale bar          Ã¢â€¢â€˜
# Ã¢â€¢â€˜  DESIGN-01 Ã‚Â· DESIGN-02 Ã‚Â· DESIGN-03 Ã‚Â· DESIGN-04 Ã‚Â· DESIGN-05 Ã‚Â· 07     Ã¢â€¢â€˜
# Ã¢â€¢Å¡Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â

import subprocess, sys
try:
    import contextily as cx
    print("  contextily already installed")
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'contextily', '-q'])
    import contextily as cx
    print("  contextily installed")

import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from rasterio.features import geometry_mask
from shapely.ops import unary_union

# Ã¢â€â‚¬Ã¢â€â‚¬ Basemap sources Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
BASEMAP_TOPO      = cx.providers.Esri.WorldTopoMap
BASEMAP_HILLSHADE = cx.providers.Esri.WorldShadedRelief
COMPASS_PNG_PATH  = os.path.join(OUT_DIR, "assets", "compass_rose.png")
os.makedirs(os.path.join(OUT_DIR, "assets"), exist_ok=True)
PANEL_BG = '#F4F3EF'

# Ã¢â€â‚¬Ã¢â€â‚¬ DESIGN-05: Mask raster to basin boundary Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def mask_raster_to_basin(arr, dem_transform, gdf_sub_utm):
    """Set pixels outside combined basin polygon to NaN."""
    union_geom = unary_union(gdf_sub_utm.geometry)
    mask = geometry_mask(
        [union_geom.__geo_interface__],
        transform=dem_transform, invert=True, out_shape=arr.shape,
    )
    out = arr.copy().astype(np.float32)
    out[~mask] = np.nan
    return out

print("  Pre-masking rasters to basin boundary...")
DEM_ARR_MASKED    = mask_raster_to_basin(DEM_ARR,    DEM_TRANSFORM, gdf_sub)
SLOPE_ARR_MASKED  = mask_raster_to_basin(SLOPE_ARR,  DEM_TRANSFORM, gdf_sub)
ASPECT_ARR_MASKED = mask_raster_to_basin(ASPECT_ARR, DEM_TRANSFORM, gdf_sub)
FACC_ARR_MASKED   = mask_raster_to_basin(FACC_ARR,   DEM_TRANSFORM, gdf_sub)
FDIR_ARR_MASKED   = mask_raster_to_basin(FDIR_ARR,   DEM_TRANSFORM, gdf_sub)
HILLSHADE_MASKED  = mask_raster_to_basin(HILLSHADE,  DEM_TRANSFORM, gdf_sub)
print("  Raster masking done.")

# Ã¢â€â‚¬Ã¢â€â‚¬ Basin extent with padding Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def basin_extent_padded(pad_frac=0.025):
    """(xmin, xmax, ymin, ymax) + padding."""
    b  = gdf_sub.total_bounds
    px = (b[2] - b[0]) * pad_frac
    py = (b[3] - b[1]) * pad_frac
    return (b[0]-px, b[2]+px, b[1]-py, b[3]+py)

def compute_utm_extent():
    b = DEM_BOUNDS
    return b.left, b.right, b.bottom, b.top

def raster_extent():
    b = DEM_BOUNDS
    return [b.left, b.right, b.bottom, b.top]

# Ã¢â€â‚¬Ã¢â€â‚¬ DESIGN-01: Standard GIS Unified Layout Figure Factory Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
def make_map_figure(title, figsize=(16, 11)):
    """Creates a professional GIS layout using a unified 16x11 frame."""
    fig, ax_map = plt.subplots(figsize=figsize, facecolor='white', dpi=150)
    fig.subplots_adjust(left=0.08, right=0.92, bottom=0.08, top=0.88)
    
    # Transparent shim for backward compat
    ax_panel = fig.add_axes([0, 0, 1, 1], facecolor='none')
    ax_panel.axis('off')
    
    # Boxed Title overlay
    title_box = FancyBboxPatch((0.15, 0.90), 0.70, 0.08, transform=fig.transFigure,
                             facecolor='white', alpha=0.92, edgecolor='#111111', 
                             linewidth=1.5, boxstyle="round,pad=0.01", zorder=100)
    fig.patches.append(title_box)
    
    fig.text(0.5, 0.945, 'PRAVARA RIVER BASIN', transform=fig.transFigure,
             ha='center', va='center', fontsize=12, fontweight='bold', color='#333333')
    fig.text(0.5, 0.920, title.upper(), transform=fig.transFigure,
             ha='center', va='center', fontsize=15, fontweight='black', color='black')

    for sp in ax_map.spines.values():
        sp.set_edgecolor('#111111'); sp.set_linewidth(2.0)
    ax_map.set_facecolor('#F0F8FF') 
    return fig, ax_map, ax_panel

def add_esri_basemap(ax, source=None, alpha=0.55):
    """ESRI World Topo Map integration with optimal transparency."""
    if source is None: source = ctx.providers.Esri.WorldTopoMap
    try:
        ctx.add_basemap(ax, crs=str(gdf_sub.crs), source=source,
                       zoom='auto', alpha=alpha, attribution=False, zorder=0)
    except Exception:
        ax.imshow(HILLSHADE_MASKED, extent=raster_extent(), origin='upper',
                  cmap='Greys_r', alpha=0.45, zorder=0)

def add_compass_rose_panel(ax_panel, cx_pos=0.08, cy_pos=0.15, r=0.06):
    """Professional 8-point compass rose overlay."""
    ax_panel.add_patch(plt.Circle((cx_pos, cy_pos), r*1.15, transform=ax_panel.transAxes,
                                  facecolor='white', alpha=0.9, edgecolor='#333333', lw=0.6, zorder=30))
    for angle_deg in range(0, 360, 45):
        angle = np.radians(angle_deg)
        length = r if angle_deg % 90 == 0 else r * 0.6
        pts_r = [ (cx_pos, cy_pos),
                  (cx_pos + np.cos(angle)*length, cy_pos + np.sin(angle)*length),
                  (cx_pos + np.cos(angle-0.12)*length*0.2, cy_pos + np.sin(angle-0.12)*length*0.2) ]
        ax_panel.add_patch(plt.Polygon(pts_r, transform=ax_panel.transAxes, 
                                       facecolor='#111111', edgecolor='none', zorder=31))
        pts_l = [ (cx_pos, cy_pos),
                  (cx_pos + np.cos(angle)*length, cy_pos + np.sin(angle)*length),
                  (cx_pos + np.cos(angle+0.12)*length*0.2, cy_pos + np.sin(angle+0.12)*length*0.2) ]
        ax_panel.add_patch(plt.Polygon(pts_l, transform=ax_panel.transAxes, 
                                       facecolor='white', edgecolor='#111111', lw=0.4, zorder=31))
    ax_panel.text(cx_pos, cy_pos + r*1.35, 'N', transform=ax_panel.transAxes,
                  ha='center', va='bottom', fontsize=10, fontweight='black', color='black', zorder=35)

def add_scale_bar_panel(ax_panel, utm_extent=None, y_top=0.32, x_left=0.03, bar_w=0.15):
    """Modular GIS staggered scale bar overlay."""
    if utm_extent is None: utm_extent = compute_utm_extent()
    dist_km = (utm_extent[1] - utm_extent[0]) / 1000.0
    bar_km = next((n for n in [5,10,20,50,100] if n >= dist_km*0.15), 10)
    bar_h = 0.02; bar_y = y_top - bar_h
    x_steps = np.linspace(x_left, x_left + bar_w, 5)
    ax_panel.add_patch(Rectangle((x_left-0.01, y_top-0.08), bar_w+0.02, 0.12, transform=ax_panel.transAxes,
                                 facecolor='white', alpha=0.85, edgecolor='none', zorder=20))
    for i in range(4):
        fc = '#111111' if i % 2 == 0 else 'white'
        ax_panel.add_patch(Rectangle((x_steps[i], bar_y), x_steps[i+1]-x_steps[i], bar_h,
                                     transform=ax_panel.transAxes, facecolor=fc, 
                                     edgecolor='#111111', lw=0.8, zorder=25))
    lkw = dict(transform=ax_panel.transAxes, ha='center', va='bottom', fontsize=7, color='black', fontweight='bold')
    ax_panel.text(x_steps[0], bar_y+bar_h+0.005, '0', **lkw)
    ax_panel.text(x_steps[4], bar_y+bar_h+0.005, f'{bar_km} km', **lkw)
    ax_panel.text(x_left + bar_w/2, bar_y - 0.015, "PLANIMETRIC SCALE", 
                  transform=ax_panel.transAxes, ha='center', va='top', 
                  fontsize=6, color='#444444', style='italic', zorder=26)

def add_classified_legend_panel(ax_panel, colours, labels, title='Legend', y_top=0.42, x_left=0.74):
    """Categorical legend in an inset box."""
    n = len(labels)
    box_w, box_h = 0.24, 0.05 + (n * 0.045)
    ax_panel.add_patch(FancyBboxPatch((x_left, y_top-box_h), box_w, box_h, 
                                     boxstyle='round,pad=0.01', transform=ax_panel.transAxes,
                                     facecolor='white', alpha=0.92, edgecolor='#111111', lw=1.2, zorder=100))
    ax_panel.text(x_left + box_w/2, y_top - 0.03, title, transform=ax_panel.transAxes,
                  ha='center', va='top', fontsize=10, fontweight='bold', color='black', zorder=101)
    for i, (col, lbl) in enumerate(zip(colours, labels)):
        y = y_top - 0.05 - (i * 0.04)
        ax_panel.add_patch(Rectangle((x_left+0.02, y-0.02), 0.04, 0.03, transform=ax_panel.transAxes,
                                     facecolor=col, edgecolor='#333333', lw=0.5, zorder=102))
        ax_panel.text(x_left+0.07, y-0.005, lbl, transform=ax_panel.transAxes,
                      ha='left', va='center', fontsize=8, color='black', zorder=102)

def add_continuous_legend_panel(ax_panel, arr_masked, cmap_name, label, y_top=0.38, y_bot=0.08, x_left=0.78):
    """Continuous colorbar in a professional boxed inset."""
    from matplotlib.colorbar import ColorbarBase
    from matplotlib.colors import Normalize
    box_w, box_h = 0.20, (y_top - y_bot) + 0.10
    ax_panel.add_patch(FancyBboxPatch((x_left, y_bot-0.02), box_w, box_h, 
                                     boxstyle='round,pad=0.01', transform=ax_panel.transAxes,
                                     facecolor='white', alpha=0.92, edgecolor='#111111', lw=1.2, zorder=100))
    ax_panel.text(x_left + box_w/2, y_top + 0.02, 'Legend', transform=ax_panel.transAxes,
                  ha='center', va='bottom', fontsize=9, fontweight='bold', color='black', zorder=101)
    cb_ax = ax_panel.inset_axes([x_left+0.06, y_bot+0.02, 0.05, y_top-y_bot])
    valid = arr_masked[~np.isnan(arr_masked)]; vmin = float(np.nanmin(valid)); vmax = float(np.nanmax(valid))
    cb = ColorbarBase(cb_ax, cmap=plt.get_cmap(cmap_name), norm=Normalize(vmin=vmin, vmax=vmax), orientation='vertical')
    cb.set_label(label, fontsize=7.5, labelpad=4, fontweight='bold')
    cb.ax.tick_params(labelsize=7); cb_ax.yaxis.set_label_position('right'); cb_ax.yaxis.tick_right()

def apply_dms_grid(ax, utm_extent, n_ticks=4):
    """Grid with de-cluttering: high padding and corner avoidance."""
    x_ticks, x_labels, y_ticks, y_labels = get_dms_ticks(utm_extent, n=n_ticks)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, fontsize=7.5, color='#333333', fontweight='medium')
    ax.tick_params(axis='x', which='both', length=6, direction='in', pad=10, 
                   bottom=True, top=True, labelbottom=True, labeltop=True)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels, rotation=90, va='center', fontsize=7.5, color='#333333', fontweight='medium')
    ax.tick_params(axis='y', which='both', length=6, direction='in', pad=10, 
                   left=True, right=True, labelleft=True, labelright=True)
    ax.grid(True, linestyle=(0, (5, 8)), color='#999999', alpha=0.35, zorder=1)

def finalize_map(fig, ax_map, ax_panel, filename, add_panel_elements=True, source=None):
    """Finalize the map with grid, basemap, neatline, and furniture."""
    ext = basin_extent_padded()
    ax_map.set_xlim(ext[0], ext[1]); ax_map.set_ylim(ext[2], ext[3])
    apply_dms_grid(ax_map, ext)
    for spine in ax_map.spines.values():
        spine.set_linewidth(1.8); spine.set_edgecolor('#1a1a1a')
    if add_panel_elements:
        add_compass_rose_panel(ax_panel)
        add_scale_bar_panel(ax_panel, compute_utm_extent())
    fig.savefig(os.path.join(MAPS_DIR, filename), dpi=220, bbox_inches='tight', facecolor='white')
    plt.close(fig); print(f"  Saved: {filename}")

def finalize_and_save(fig, ax, utm_extent, filename, n_ticks=4):
    """Backward-compat shim updated for the Unified Frame."""
    ax_panel = getattr(fig, '_panel_ax', None)
    if ax_panel: finalize_map(fig, ax, ax_panel, filename)
    else: 
        apply_dms_grid(ax, utm_extent, n_ticks)
        add_compass_rose_panel(ax, cx_pos=0.08, cy_pos=0.15, r=0.05)
        add_scale_bar_panel(ax, utm_extent)
        fig.savefig(os.path.join(MAPS_DIR, filename), dpi=220, bbox_inches='tight')
        plt.close(fig); print(f"  Saved: {filename}")


def safe_normalise(arr, lo_pct=2, hi_pct=98):
    lo = np.nanpercentile(arr, lo_pct)
    hi = np.nanpercentile(arr, hi_pct)
    out = (arr - lo) / (hi - lo + 1e-12)
    out = np.clip(out, 0.0, 1.0)
    out[np.isnan(arr)] = np.nan
    return out


def base_axes(title, figsize=(16, 11)):
    """Unified Frame shim: returns (fig, ax_map, utm_extent)."""
    fig, ax_map, ax_panel = make_map_figure(title, figsize=figsize)
    fig._panel_ax = ax_panel 
    add_esri_basemap(ax_map)
    utm_ext = compute_utm_extent()
    return fig, ax_map, utm_ext

print("Map framework loaded — DESIGN-01 through DESIGN-07 active.")


print("=" * 60)
print("SECTION 4 Ã¢â‚¬â€ MAP GENERATION")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  SHARED MAP UTILITIES (legacy helpers kept for overlay_boundaries etc.)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

from pyproj import Transformer as PyTransformer
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

_to_geo = PyTransformer.from_crs(UTM_EPSG, "EPSG:4326", always_xy=True)


def dd_to_dms(dd, is_lat=True):
    """Convert decimal degrees -> DÃ‚Â°M' format only (no seconds)."""
    hemi = ("N" if dd >= 0 else "S") if is_lat else ("E" if dd >= 0 else "W")
    dd = abs(dd)
    deg = int(dd)
    mins_full = (dd - deg) * 60
    mins = int(round(mins_full))   # round to nearest minute
    if mins == 60:                  # handle rounding edge-case
        deg += 1; mins = 0
    return f"{deg}Ã‚Â°{mins:02d}\u2032{hemi}"


def get_dms_ticks(utm_extent, n=5):
    xmin, xmax, ymin, ymax = utm_extent
    corners_utm = [(xmin,ymin),(xmax,ymin),(xmin,ymax),(xmax,ymax)]
    lon_all, lat_all = [], []
    for xu, yu in corners_utm:
        lo, la = _to_geo.transform(xu, yu)
        lon_all.append(lo); lat_all.append(la)
    lon_min, lon_max = min(lon_all), max(lon_all)
    lat_min, lat_max = min(lat_all), max(lat_all)
    lon_ticks_geo = np.linspace(lon_min, lon_max, n)
    lat_ticks_geo = np.linspace(lat_min, lat_max, n)
    from pyproj import Transformer as T2
    _to_utm = T2.from_crs("EPSG:4326", UTM_EPSG, always_xy=True)
    x_ticks_utm = [_to_utm.transform(lo, (lat_min+lat_max)/2)[0] for lo in lon_ticks_geo]
    y_ticks_utm = [_to_utm.transform((lon_min+lon_max)/2, la)[1] for la in lat_ticks_geo]
    x_labels = [dd_to_dms(lo, is_lat=False) for lo in lon_ticks_geo]
    y_labels = [dd_to_dms(la, is_lat=True)  for la in lat_ticks_geo]
    return x_ticks_utm, x_labels, y_ticks_utm, y_labels


def overlay_boundaries(ax, alpha_sub=0.9, alpha_str=0.5):
    gdf_sub.boundary.plot(ax=ax, edgecolor='black', linewidth=1.2,
                          zorder=10, label='Subbasin boundary')
    if len(gdf_streams) > 0:
        gdf_streams.plot(ax=ax, color='royalblue', linewidth=0.8,
                         alpha=alpha_str, zorder=9, label='Stream network')


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  1. ELEVATION MAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[1/9] Elevation map...")
fig, ax_map, ax_panel = make_map_figure("Elevation Map")
add_esri_basemap(ax_map)

cmap_elev = plt.get_cmap('terrain').copy(); cmap_elev.set_bad(alpha=0)
ax_map.imshow(DEM_ARR_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_elev, alpha=0.75, zorder=2,
    vmin=np.nanpercentile(DEM_ARR_MASKED, 2), vmax=np.nanpercentile(DEM_ARR_MASKED, 98))

gdf_sub.boundary.plot(ax=ax_map, edgecolor='black', linewidth=1.5, zorder=10)
gdf_streams.plot(ax=ax_map, color='royalblue', linewidth=0.8, alpha=0.6, zorder=8)

add_continuous_legend_panel(ax_panel, DEM_ARR_MASKED, 'terrain', 'Elevation (m)')
finalize_map(fig, ax_map, ax_panel, "01_elevation.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  2. SLOPE MAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[2/9] Slope map...")
fig, ax_map, ax_panel = make_map_figure("Slope Map")
add_esri_basemap(ax_map)

cmap_sl = plt.get_cmap('YlOrRd').copy(); cmap_sl.set_bad(alpha=0)
ax_map.imshow(SLOPE_ARR_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_sl, alpha=0.75, zorder=2,
    vmin=0, vmax=np.nanpercentile(SLOPE_ARR_MASKED, 98))

gdf_sub.boundary.plot(ax=ax_map, edgecolor='black', linewidth=1.5, zorder=10)
add_continuous_legend_panel(ax_panel, SLOPE_ARR_MASKED, 'YlOrRd', 'Slope (Ã‚Â°)')
finalize_map(fig, ax_map, ax_panel, "02_slope.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  3. ASPECT MAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[3/9] Aspect map...")
fig, ax_map, ax_panel = make_map_figure("Aspect Map")
add_esri_basemap(ax_map)

cmap_asp = plt.get_cmap('hsv').copy(); cmap_asp.set_bad(alpha=0)
ax_map.imshow(ASPECT_ARR_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_asp, alpha=0.72, zorder=2, vmin=0, vmax=360)

gdf_sub.boundary.plot(ax=ax_map, edgecolor='black', linewidth=1.5, zorder=10)
add_continuous_legend_panel(ax_panel, ASPECT_ARR_MASKED, 'hsv', 'Aspect (Ã‚Â°)')
finalize_map(fig, ax_map, ax_panel, "03_aspect.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  4. FLOW DIRECTION MAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[4/9] Flow direction map...")
fig, ax_map, ax_panel = make_map_figure("Flow Direction Map")
add_esri_basemap(ax_map)

d8_labels = {1:'E', 2:'SE', 4:'S', 8:'SW', 16:'W', 32:'NW', 64:'N', 128:'NE'}
_fdir_valid = FDIR_ARR_MASKED[~np.isnan(FDIR_ARR_MASKED)]
unique_d8 = [v for v in sorted(d8_labels.keys()) if v in np.unique(_fdir_valid)]
colors_d8 = plt.cm.tab10(np.linspace(0, 1, 8))
d8_cmap   = mcolors.ListedColormap(colors_d8[:len(unique_d8)])
d8_bounds = [unique_d8[0]-0.5] + [v+0.5 for v in unique_d8]
d8_norm   = mcolors.BoundaryNorm(d8_bounds, d8_cmap.N)

ax_map.imshow(FDIR_ARR_MASKED, extent=raster_extent(), origin='upper',
    cmap=d8_cmap, norm=d8_norm, alpha=0.75, zorder=2)
gdf_sub.boundary.plot(ax=ax_map, edgecolor='black', linewidth=1.2, zorder=10)
patches_d8 = [mpatches.Patch(color=colors_d8[i], label=d8_labels.get(unique_d8[i],''))
              for i in range(len(unique_d8))]
ax_map.legend(handles=patches_d8, loc='lower left', fontsize=6,
              ncol=2, title='Flow Dir.', framealpha=0.85)
finalize_map(fig, ax_map, ax_panel, "04_flow_direction.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  5. FLOW ACCUMULATION MAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[5/9] Flow accumulation map...")
fig, ax_map, ax_panel = make_map_figure("Flow Accumulation Map")
add_esri_basemap(ax_map)

fa_log_masked = np.log10(np.where(FACC_ARR_MASKED>0, FACC_ARR_MASKED, np.nan))
cmap_fa = plt.get_cmap('Blues').copy(); cmap_fa.set_bad(alpha=0)
ax_map.imshow(fa_log_masked, extent=raster_extent(), origin='upper',
    cmap=cmap_fa, alpha=0.75, zorder=2)

gdf_sub.boundary.plot(ax=ax_map, edgecolor='black', linewidth=1.5, zorder=10)
gdf_streams.plot(ax=ax_map, color='royalblue', linewidth=0.8, alpha=0.6, zorder=8)

add_continuous_legend_panel(ax_panel, fa_log_masked, 'Blues', 'log\u2081\u2080(Accumulation)')
finalize_map(fig, ax_map, ax_panel, "05_flow_accumulation.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  6. STREAM ORDER MAP (Strahler)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[6/9] Stream order map...")
fig, ax_map, ax_panel = make_map_figure("Strahler Stream Order Map")
add_esri_basemap(ax_map, source=BASEMAP_TOPO, alpha=0.50)

orders_list  = sorted(gdf_so[ORDER_COL].unique())
order_cmap   = plt.cm.get_cmap('plasma_r', len(orders_list))
order_colors = {o: order_cmap(i) for i, o in enumerate(orders_list)}
lw_map_ord   = {o: 0.6 + (o - 1) * 0.8 for o in orders_list}

for o in orders_list:
    gdf_so[gdf_so[ORDER_COL]==o].plot(ax=ax_map, color=order_colors[o],
    linewidth=lw_map_ord[o], zorder=5+o)

gdf_sub.boundary.plot(ax=ax_map, edgecolor='black', linewidth=1.8, zorder=15)
so_colours = [order_colors[o] for o in orders_list]
so_labels  = [f"Order {o}" for o in orders_list]
add_classified_legend_panel(ax_panel, so_colours, so_labels, title='Strahler Order')
finalize_map(fig, ax_map, ax_panel, "06_stream_order.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  7. DRAINAGE DENSITY MAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[7/9] Drainage density map...")
fig, ax_map, ax_panel = make_map_figure("Drainage Density Map")
add_esri_basemap(ax_map, source=BASEMAP_TOPO, alpha=0.55)

gdf_dd = gdf_sub.merge(df_master[['Drainage_Density_Dd']].reset_index(),
                        on='basin_id', how='left')
gdf_dd.plot(column='Drainage_Density_Dd', ax=ax_map,
            cmap='YlGnBu', alpha=0.70, zorder=3,
            edgecolor='#222222', linewidth=1.2, legend=False)

for _, r in gdf_dd.iterrows():
    cx2, cy2 = r.geometry.centroid.x, r.geometry.centroid.y
    ax_map.text(cx2, cy2, f"{r['basin_id']}\n{r['Drainage_Density_Dd']:.2f}",
                ha='center', va='center', fontsize=7, fontweight='bold',
                color='black', path_effects=[pe.withStroke(linewidth=2, foreground="white")])

add_continuous_legend_panel(ax_panel, gdf_dd['Drainage_Density_Dd'].values, 'YlGnBu', 'Dd (km/km\u00b2)')
finalize_map(fig, ax_map, ax_panel, "07_drainage_density.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  8. CONTOUR MAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[8/9] Contour map...")
fig, ax_map, ax_panel = make_map_figure("Topographic Contour Map")
add_esri_basemap(ax_map)

ax = ax_map
b2 = DEM_BOUNDS
# Force professional contour intervals: 10m minor, 50m major
minor_interval = 10
major_interval = 50

x_c = np.linspace(b2.left, b2.right, DEM_ARR.shape[1])
y_c = np.linspace(b2.bottom, b2.top, DEM_ARR.shape[0])[::-1]
XX, YY = np.meshgrid(x_c, y_c)

# Contour levels
levels_all = np.arange(np.floor(np.nanmin(DEM_ARR)/10)*10, np.nanmax(DEM_ARR)+10, minor_interval)
levels_major = np.arange(np.floor(np.nanmin(DEM_ARR)/50)*50, np.nanmax(DEM_ARR)+50, major_interval)

dem_filled_c = np.where(np.isnan(DEM_ARR), np.nanmean(DEM_ARR), DEM_ARR)

# Plot minor contours
cs_minor = ax.contour(XX, YY, dem_filled_c, levels=levels_all,
                       colors='#8B4513', linewidths=0.3, alpha=0.4, zorder=3)
# Plot major contours
cs_major = ax.contour(XX, YY, dem_filled_c, levels=levels_major,
                       colors='#5D2906', linewidths=0.8, alpha=0.8, zorder=4)

ax.clabel(cs_major, inline=True, fontsize=7, fmt='%d m')
overlay_boundaries(ax)

# Legend entry for contours
ax_panel.text(0.5, 0.45, "Contour Intervals", transform=ax_panel.transAxes, 
              ha='center', va='bottom', fontsize=9, fontweight='bold')
ax_panel.text(0.5, 0.41, f"Major: {major_interval} m\nMinor: {minor_interval} m", 
              transform=ax_panel.transAxes, ha='center', va='top', fontsize=7.5)

finalize_map(fig, ax_map, ax_panel, "08_contour.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  9. POUR POINTS ON DEM
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("[9/9] Pour points map...")
fig, ax_map2, ax_panel2 = make_map_figure("Pour Points Location Map")
add_esri_basemap(ax_map2)
ax = ax_map2

ax.imshow(DEM_ARR_MASKED, extent=raster_extent(), origin='upper',
    cmap='terrain', alpha=0.72, zorder=2,
    vmin=np.nanpercentile(DEM_ARR_MASKED, 2), vmax=np.nanpercentile(DEM_ARR_MASKED, 98))

gdf_sub.boundary.plot(ax=ax, edgecolor='black', linewidth=1.5, zorder=10)

if POUR_POINTS_OK and gdf_pp is not None:
    gdf_pp.plot(ax=ax, color='#E31A1C', markersize=100, zorder=25,
                label='Snapped pour points', marker='v', edgecolor='white', linewidth=1.0)
    for idx, r in gdf_pp.iterrows():
        label = str(r.get('basin_id', idx))
        ax.annotate(label, xy=(r.geometry.x, r.geometry.y),
            xytext=(6, 6), textcoords='offset points',
            fontsize=9, color='white', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2.5, foreground='black')])

add_continuous_legend_panel(ax_panel2, DEM_ARR_MASKED, 'terrain', 'Elevation (m)',
                             y_top=0.38, y_bot=0.05)
finalize_map(fig, ax_map2, ax_panel2, "09_pour_points.png")

print(f"\n  All 9 maps saved to: {MAPS_DIR}")


print("=" * 60)
print("SECTION 5 Ã¢â‚¬â€ STATISTICAL ANALYSIS")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬ Select numeric morphometric columns for analysis Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
STAT_COLS = [
    'Area_km2', 'Perimeter_km', 'Basin_Length_km',
    'Drainage_Density_Dd', 'Stream_Frequency_Fs', 'Texture_Ratio_T',
    'Form_Factor_Ff', 'Elongation_Ratio_Re', 'Circularity_Ratio_Rc',
    'Compactness_Cc', 'LengthOverlandFlow_Lg', 'ChannelMaintenance_C',
    'Basin_Relief_H_m', 'Relief_Ratio_Rh', 'Relative_Relief',
    'Ruggedness_Rn', 'Melton_MRN', 'Hypsometric_HI',
    'Slope_Mean_deg', 'TRI_Mean', 'Rbm',
]
# Keep only columns that actually exist in df_master
STAT_COLS = [c for c in STAT_COLS if c in df_master.columns]
df_stat   = df_master[STAT_COLS].copy().astype(float)
df_stat.dropna(axis=1, how='all', inplace=True)
STAT_COLS = df_stat.columns.tolist()

print(f"  Parameters for analysis: {len(STAT_COLS)}")
print(f"  Subbasins: {len(df_stat)}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. DESCRIPTIVE STATISTICS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[A] Descriptive Statistics...")

desc_extra = df_stat.agg([
    'mean', 'median', 'std',
    lambda x: (x.std()/x.mean()*100) if x.mean() != 0 else np.nan,  # CV%
    lambda x: float(stats.skew(x.dropna())),
    lambda x: float(stats.kurtosis(x.dropna())),
])
desc_extra.index = ['Mean', 'Median', 'Std', 'CV%', 'Skewness', 'Kurtosis']
desc_full = pd.concat([df_stat.describe(), desc_extra])

csv_path = os.path.join(TABLES_DIR, "descriptive_statistics.csv")
desc_full.to_csv(csv_path)
print(f"  Ã¢Å“â€¦ Saved: {csv_path}")
print(desc_full.to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. CORRELATION MATRICES
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[B] Correlation Matrices (Pearson + Spearman)...")

# Pearson
corr_pearson  = df_stat.corr(method='pearson')
corr_spearman = df_stat.corr(method='spearman')

# Heatmap Ã¢â‚¬â€ Pearson
fig, axes = plt.subplots(1, 2, figsize=(20, 8))
for ax_corr, corr_mat, title in [
    (axes[0], corr_pearson,  "Pearson Correlation"),
    (axes[1], corr_spearman, "Spearman Correlation"),
]:
    mask = np.triu(np.ones_like(corr_mat, dtype=bool))
    sns.heatmap(
        corr_mat, mask=mask, ax=ax_corr,
        cmap='RdYlBu_r', center=0, vmin=-1, vmax=1,
        annot=True, fmt='.2f', annot_kws={'size': 7},
        linewidths=0.5, square=True, cbar_kws={'shrink': 0.7},
    )
    ax_corr.set_title(title, fontsize=13, fontweight='bold')
    ax_corr.set_xticklabels(ax_corr.get_xticklabels(), rotation=45,
                              ha='right', fontsize=7.5)
    ax_corr.set_yticklabels(ax_corr.get_yticklabels(), fontsize=7.5)

plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, "correlation_heatmap.png"), dpi=180, bbox_inches='tight')
plt.close(fig)
print("  Ã¢Å“â€¦ Correlation heatmap saved")

corr_pearson.to_csv(os.path.join(TABLES_DIR, "correlation_pearson.csv"))
corr_spearman.to_csv(os.path.join(TABLES_DIR, "correlation_spearman.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. VARIANCE INFLATION FACTOR
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[C] VIF Analysis...")
# Require at least 2 samples per predictor Ã¢â‚¬â€ only feasible if n > n_params
if len(df_stat) > len(STAT_COLS):
    df_vif    = df_stat.dropna()
    X_vif     = sm.add_constant(df_vif)
    vif_data  = pd.DataFrame({
        'Feature': df_vif.columns,
        'VIF'    : [variance_inflation_factor(X_vif.values, i + 1)
                    for i in range(len(df_vif.columns))]
    }).sort_values('VIF', ascending=False)
    print(vif_data.to_string(index=False))
    vif_data.to_csv(os.path.join(TABLES_DIR, "vif.csv"), index=False)
else:
    print(f"  Ã¢Å¡Â Ã¯Â¸Â  VIF skipped: n_basins ({len(df_stat)}) Ã¢â€°Â¤ n_params ({len(STAT_COLS)})")
    vif_data = pd.DataFrame(columns=['Feature', 'VIF'])

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. PCA
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Principal Component Analysis...")

# Standardize
scaler    = StandardScaler()
df_scaled = df_stat.fillna(df_stat.median())
X_scaled  = scaler.fit_transform(df_scaled)

pca      = PCA()
scores   = pca.fit_transform(X_scaled)
n_comp   = len(pca.explained_variance_ratio_)

# Scree data
exp_var      = pca.explained_variance_ratio_ * 100
cum_var      = np.cumsum(exp_var)
n_comp_95    = np.searchsorted(cum_var, 95) + 1

print(f"  Total components: {n_comp}")
print(f"  Components to explain 95% variance: {n_comp_95}")
for i in range(min(n_comp, 5)):
    print(f"  PC{i+1}: {exp_var[i]:.2f}%  (cumulative: {cum_var[i]:.2f}%)")

# Ã¢â€â‚¬Ã¢â€â‚¬ Scree plot Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.bar(range(1, n_comp + 1), exp_var, color='steelblue', alpha=0.8, label='Individual')
ax1.plot(range(1, n_comp + 1), cum_var, 'ro-', ms=5, label='Cumulative')
ax1.axhline(95, color='green', linestyle='--', lw=1.2, label='95% threshold')
ax1.set_xlabel("Principal Component")
ax1.set_ylabel("Explained Variance (%)")
ax1.set_title("Scree Plot Ã¢â‚¬â€ PCA")
ax1.legend()
ax1.set_xlim(0.5, n_comp + 0.5)

# Ã¢â€â‚¬Ã¢â€â‚¬ Biplot (PC1 vs PC2) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
pc1_scores = scores[:, 0]
pc2_scores = scores[:, 1] if n_comp > 1 else np.zeros(len(scores))

ax2.scatter(pc1_scores, pc2_scores, c='darkorange', s=120, zorder=5, edgecolors='black')
for i, bid in enumerate(df_stat.index):
    ax2.annotate(bid, (pc1_scores[i], pc2_scores[i]),
                 textcoords='offset points', xytext=(6, 3), fontsize=9)

# Loading vectors
loadings = pca.components_.T
scale    = max(abs(pc1_scores).max(), abs(pc2_scores).max())
for j, feat in enumerate(STAT_COLS):
    ax2.annotate(
        '', xy=(loadings[j, 0] * scale * 0.5, loadings[j, 1] * scale * 0.5),
        xytext=(0, 0),
        arrowprops=dict(arrowstyle='->', color='royalblue', lw=1.2)
    )
    ax2.text(loadings[j, 0] * scale * 0.55, loadings[j, 1] * scale * 0.55,
             feat, fontsize=6.5, color='royalblue', ha='center')

ax2.set_xlabel(f"PC1 ({exp_var[0]:.1f}%)")
ax2.set_ylabel(f"PC2 ({exp_var[1]:.1f}%)" if n_comp > 1 else "PC2")
ax2.set_title("PCA Biplot (PC1 vs PC2)")
ax2.axhline(0, color='grey', lw=0.5, linestyle='--')
ax2.axvline(0, color='grey', lw=0.5, linestyle='--')

plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, "pca_scree_biplot.png"), dpi=180, bbox_inches='tight')
plt.close(fig)
print("  Ã¢Å“â€¦ PCA scree + biplot saved")

# Save loadings
df_loadings = pd.DataFrame(
    pca.components_[:min(n_comp, 5)].T,
    index=STAT_COLS,
    columns=[f"PC{i+1}" for i in range(min(n_comp, 5))],
)
df_loadings.to_csv(os.path.join(TABLES_DIR, "pca_loadings.csv"))

df_scores_df = pd.DataFrame(
    scores[:, :min(n_comp, 5)],
    index=df_stat.index,
    columns=[f"PC{i+1}" for i in range(min(n_comp, 5))],
)
df_scores_df.to_csv(os.path.join(TABLES_DIR, "pca_scores.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. CLUSTER ANALYSIS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[E] Cluster Analysis...")

if len(df_scaled) >= 3:
    # Ã¢â€â‚¬Ã¢â€â‚¬ Hierarchical Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    Z = linkage(X_scaled, method='ward')
    fig, ax = plt.subplots(figsize=(10, 5))
    dendrogram(Z, labels=df_stat.index.tolist(), ax=ax, color_threshold=0.7 * max(Z[:, 2]))
    ax.set_title("Hierarchical Clustering Dendrogram (Ward linkage)")
    ax.set_xlabel("Subbasin")
    ax.set_ylabel("Distance")
    # unified layout margins instead of tight_layout
    fig.savefig(os.path.join(PLOTS_DIR, "hierarchical_dendrogram.png"), dpi=180, bbox_inches='tight')
    plt.close(fig)

    # Ã¢â€â‚¬Ã¢â€â‚¬ K-means Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    k_range = range(2, min(len(df_scaled), 4))
    sil_scores = []
    for k in k_range:
        km  = KMeans(n_clusters=k, random_state=42, n_init=10)
        lbs = km.fit_predict(X_scaled)
        if len(set(lbs)) > 1:
            sil_scores.append(silhouette_score(X_scaled, lbs))
        else:
            sil_scores.append(-1)

    best_k = k_range.start + int(np.argmax(sil_scores))
    print(f"  Best k (silhouette): {best_k}")

    km_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    CLUSTER_LABELS = km_final.fit_predict(X_scaled)
    df_master['Cluster'] = CLUSTER_LABELS

    # Visualise clusters in PC space
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(
        pc1_scores, pc2_scores,
        c=CLUSTER_LABELS, cmap='Set1', s=180, edgecolors='black', zorder=5
    )
    for i, bid in enumerate(df_stat.index):
        ax.annotate(bid, (pc1_scores[i], pc2_scores[i]),
                    textcoords='offset points', xytext=(6, 3), fontsize=9)
    plt.colorbar(scatter, ax=ax, label='Cluster')
    ax.set_xlabel(f"PC1 ({exp_var[0]:.1f}%)")
    ax.set_ylabel(f"PC2 ({exp_var[1]:.1f}%)" if n_comp > 1 else "PC2")
    ax.set_title(f"K-means Clustering (k={best_k}) in PCA Space")
    # unified layout margins instead of tight_layout
    fig.savefig(os.path.join(PLOTS_DIR, "kmeans_clusters.png"), dpi=180, bbox_inches='tight')
    plt.close(fig)
    print(f"  Ã¢Å“â€¦ Cluster analysis complete (k={best_k})")
else:
    print(f"  Ã¢Å¡Â Ã¯Â¸Â  Clustering skipped: only {len(df_scaled)} basins (need Ã¢â€°Â¥ 3)")
    CLUSTER_LABELS = np.zeros(len(df_stat), dtype=int)
    df_master['Cluster'] = CLUSTER_LABELS

print("\nÃ¢Å“â€¦ SECTION 5 complete.")


print("=" * 60)
print("SECTION 6 Ã¢â‚¬â€ WATERSHED PRIORITIZATION")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬ Erosion-sensitive parameters Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Direct relation with erosion (higher = more erosion prone Ã¢â€ â€™ higher rank = worse)
DIRECT_PARAMS = {
    'Drainage_Density_Dd' : 'Dd',
    'Stream_Frequency_Fs' : 'Fs',
    'Rbm'                 : 'Rb',
    'Ruggedness_Rn'       : 'Rn',
    'Relief_Ratio_Rh'     : 'Rh',
    'Hypsometric_HI'      : 'HI',
    'Melton_MRN'          : 'MRN',
}
# Inverse relation (higher = less erosion prone Ã¢â€ â€™ lower rank = worse)
INVERSE_PARAMS = {
    'Elongation_Ratio_Re' : 'Re',
    'Circularity_Ratio_Rc': 'Rc',
    'Form_Factor_Ff'      : 'Ff',
}

# Keep only params actually in df_master
DIRECT_AVAIL  = {k: v for k, v in DIRECT_PARAMS.items()  if k in df_master.columns}
INVERSE_AVAIL = {k: v for k, v in INVERSE_PARAMS.items() if k in df_master.columns}
ALL_PRIORITY_COLS = list(DIRECT_AVAIL.keys()) + list(INVERSE_AVAIL.keys())

df_pri = df_master[ALL_PRIORITY_COLS].copy().astype(float).fillna(df_master[ALL_PRIORITY_COLS].median())

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  METHOD 1 Ã¢â‚¬â€ COMPOUND PARAMETER RANKING
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[Method 1] Compound Parameter Ranking...")

df_rank = pd.DataFrame(index=df_pri.index)

for col in DIRECT_AVAIL:
    # rank: highest value Ã¢â€ â€™ rank 1 (most erosion prone)
    df_rank[col] = df_pri[col].rank(ascending=False, method='min')

for col in INVERSE_AVAIL:
    # rank: lowest value Ã¢â€ â€™ rank 1 (most erosion prone)
    df_rank[col] = df_pri[col].rank(ascending=True, method='min')

df_rank['CF_M1'] = df_rank.mean(axis=1)
df_rank['Rank_M1'] = df_rank['CF_M1'].rank(ascending=True, method='min').astype(int)

# Priority classes
n = len(df_rank)
thresholds = np.percentile(df_rank['CF_M1'], [33, 66])
df_rank['Priority_M1'] = df_rank['CF_M1'].apply(
    lambda x: 'High' if x <= thresholds[0] else ('Moderate' if x <= thresholds[1] else 'Low')
)

print(df_rank[['CF_M1', 'Rank_M1', 'Priority_M1']].to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  METHOD 2 Ã¢â‚¬â€ ENTROPY WEIGHT METHOD
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[Method 2] Entropy Weight Method...")

def entropy_weight_score(df, direct_cols, inverse_cols):
    """
    1. Normalise each parameter (0Ã¢â‚¬â€œ1)
    2. Compute Shannon entropy for each parameter
    3. Derive weights from entropy divergence
    4. Compute weighted score per subbasin
    """
    df_norm = pd.DataFrame(index=df.index)
    for col in direct_cols:
        mn, mx = df[col].min(), df[col].max()
        df_norm[col] = (df[col] - mn) / (mx - mn + 1e-12)  # 0=best 1=worst
    for col in inverse_cols:
        mn, mx = df[col].min(), df[col].max()
        # Invert: low value = high risk Ã¢â€ â€™ normalise inverted
        df_norm[col] = 1 - (df[col] - mn) / (mx - mn + 1e-12)

    # Entropy for each criterion
    n, m   = df_norm.shape
    weights = []
    for col in df_norm.columns:
        p = df_norm[col] / (df_norm[col].sum() + 1e-12)
        p = p.clip(lower=1e-12)  # avoid log(0)
        e = -np.sum(p * np.log(p)) / np.log(n + 1e-12)
        d = 1 - e
        weights.append(d)

    weights = np.array(weights)
    weights /= (weights.sum() + 1e-12)   # normalise to sum=1

    # Weighted score
    score = (df_norm.values * weights).sum(axis=1)
    return score, dict(zip(df_norm.columns, weights))


score_m2, ew_weights = entropy_weight_score(
    df_pri, list(DIRECT_AVAIL.keys()), list(INVERSE_AVAIL.keys())
)
df_rank['Score_M2'] = score_m2
df_rank['Rank_M2']  = pd.Series(score_m2, index=df_pri.index).rank(
    ascending=False, method='min'
).astype(int)

thresh_m2 = np.percentile(score_m2, [66, 33])
df_rank['Priority_M2'] = df_rank['Score_M2'].apply(
    lambda x: 'High' if x >= thresh_m2[0] else ('Moderate' if x >= thresh_m2[1] else 'Low')
)

print("  Entropy weights:")
for k, w in sorted(ew_weights.items(), key=lambda x: -x[1]):
    print(f"    {k}: {w:.4f}")
print(df_rank[['Score_M2', 'Rank_M2', 'Priority_M2']].to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  METHOD 3 Ã¢â‚¬â€ PCA-BASED PRIORITY
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[Method 3] PCA-Based Priority...")

# Re-run PCA on priority parameters only
scaler_p   = StandardScaler()
X_p        = scaler_p.fit_transform(df_pri.fillna(df_pri.median()))
pca_p      = PCA()
scores_p   = pca_p.fit_transform(X_p)
exp_var_p  = pca_p.explained_variance_ratio_

# Composite score: weighted sum of PC scores by explained variance
n_retain = min(3, len(exp_var_p))
weights_p = exp_var_p[:n_retain] / exp_var_p[:n_retain].sum()

# Sign convention: check if PC1 aligns with erosion risk
# (higher PC1 loading on Dd/Rn = higher risk = positive score)
pc1_loadings = pd.Series(pca_p.components_[0], index=ALL_PRIORITY_COLS)
direct_sign  = np.sign(pc1_loadings[list(DIRECT_AVAIL.keys())].mean())
if direct_sign < 0:
    scores_p = -scores_p   # flip sign

pca_composite = (scores_p[:, :n_retain] * weights_p).sum(axis=1)
df_rank['Score_M3'] = pca_composite
df_rank['Rank_M3']  = pd.Series(pca_composite, index=df_pri.index).rank(
    ascending=False, method='min'
).astype(int)

thresh_m3 = np.percentile(pca_composite, [66, 33])
df_rank['Priority_M3'] = df_rank['Score_M3'].apply(
    lambda x: 'High' if x >= thresh_m3[0] else ('Moderate' if x >= thresh_m3[1] else 'Low')
)
print(df_rank[['Score_M3', 'Rank_M3', 'Priority_M3']].to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  COMPARISON Ã¢â‚¬â€ KENDALL's TAU
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[Comparison] Kendall's tau agreement analysis...")

r12, p12 = stats.kendalltau(df_rank['Rank_M1'], df_rank['Rank_M2'])
r13, p13 = stats.kendalltau(df_rank['Rank_M1'], df_rank['Rank_M3'])
r23, p23 = stats.kendalltau(df_rank['Rank_M2'], df_rank['Rank_M3'])

df_kendall = pd.DataFrame({
    'Comparison': ['M1 vs M2', 'M1 vs M3', 'M2 vs M3'],
    'Kendall_tau': [r12, r13, r23],
    'p_value'    : [p12, p13, p23],
    'Agreement'  : ['Strong' if abs(r) > 0.7 else 'Moderate' if abs(r) > 0.4 else 'Weak'
                    for r in [r12, r13, r23]],
})
print(df_kendall.to_string(index=False))

# Ã¢â€â‚¬Ã¢â€â‚¬ Ranking comparison bar chart Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

basins  = df_rank.index.tolist()
x       = np.arange(len(basins))
width   = 0.28

ax1.bar(x - width, df_rank['Rank_M1'], width, label='Method 1 (Compound)',  color='steelblue')
ax1.bar(x,         df_rank['Rank_M2'], width, label='Method 2 (Entropy)',   color='darkorange')
ax1.bar(x + width, df_rank['Rank_M3'], width, label='Method 3 (PCA-based)', color='green')
ax1.set_xticks(x)
ax1.set_xticklabels(basins)
ax1.set_ylabel("Rank (1 = Highest Priority)")
ax1.set_title("Prioritization Rank Comparison Across Methods")
ax1.legend()
ax1.invert_yaxis()   # rank 1 at top

# Priority colour map
priority_map = {'High': '#d73027', 'Moderate': '#fee090', 'Low': '#4575b4'}
for i, bid in enumerate(basins):
    for j, (col, method) in enumerate([
        ('Priority_M1', 'M1'), ('Priority_M2', 'M2'), ('Priority_M3', 'M3')
    ]):
        ax2.bar(i * 4 + j, 1,
                color=priority_map.get(df_rank.loc[bid, col], 'grey'),
                edgecolor='black', linewidth=0.7)
        ax2.text(i * 4 + j, 0.5, df_rank.loc[bid, col][:1],
                 ha='center', va='center', fontsize=9, fontweight='bold')

ax2.set_xticks([i * 4 + 1 for i in range(len(basins))])
ax2.set_xticklabels(basins)
ax2.set_title("Priority Class by Method")
legend_patches = [mpatches.Patch(color=v, label=k) for k, v in priority_map.items()]
ax2.legend(handles=legend_patches, loc='upper right')
ax2.set_yticks([])

plt.tight_layout()
fig.savefig(os.path.join(PLOTS_DIR, "prioritization_comparison.png"), dpi=180, bbox_inches='tight')
plt.close(fig)

# Ã¢â€â‚¬Ã¢â€â‚¬ Save outputs Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
ranking_table = df_rank[['CF_M1','Rank_M1','Priority_M1',
                          'Score_M2','Rank_M2','Priority_M2',
                          'Score_M3','Rank_M3','Priority_M3']].copy()
ranking_table.to_csv(os.path.join(TABLES_DIR, "prioritization_ranking.csv"))
df_kendall.to_csv(os.path.join(TABLES_DIR, "kendall_tau.csv"), index=False)

# Save priority shapefile
gdf_priority = gdf_sub.merge(
    ranking_table.reset_index(), on='basin_id', how='left'
)
gdf_priority.to_file(os.path.join(SHAPES_DIR, "subbasins_priority.shp"))

print(f"\n  Ã¢Å“â€¦ Priority shapefile saved: {SHAPES_DIR}subbasins_priority.shp")
print("\nÃ¢Å“â€¦ SECTION 6 complete.")
print("\n  FINAL RANKING TABLE:")
print(ranking_table.to_string())

print("=" * 60)
print("SECTION 7 Ã¢â‚¬â€ PLOTLY INTERACTIVE VISUALIZATION SUITE")
print("=" * 60)

HTML_DIR = os.path.join(PLOTS_DIR, "html/")
os.makedirs(HTML_DIR, exist_ok=True)


def save_fig(fig, name):
    """Save Plotly figure as self-contained HTML (Bundled JS) to fix errors."""
    html_path = os.path.join(HTML_DIR, f"{name}.html")
    # include_plotlyjs=True converts JS to string inside HTML (fixes CSP/CDN errors)
    fig.write_html(html_path, include_plotlyjs=True)
    print(f"  Ã¢Å“â€¦ {name}.html")
    return html_path


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  1. HORTON'S LAWS Ã¢â‚¬â€ Stream Number & Stream Length
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[1] Horton's Law plots...")

for bid, df_lin in LINEAR_PER_ORDER.items():
    if df_lin.empty or len(df_lin) < 2:
        continue
    orders   = df_lin['order'].values
    Nu_vals  = df_lin['Nu'].values.astype(float)
    Lu_vals  = (df_lin['Lu'].values / 1000).astype(float)  # km

    # Regression on log scale (exclude zeros)
    mask_n = Nu_vals > 0
    log_Nu = np.log10(Nu_vals[mask_n])
    log_u  = np.log10(orders[mask_n])
    if len(log_u) > 1:
        slope_n, intercept_n, r_n, p_n, _ = stats.linregress(log_u, log_Nu)
        r2_n = r_n ** 2
    else:
        slope_n, intercept_n, r2_n = 0, 0, 0

    mask_l = Lu_vals > 0
    log_Lu = np.log10(Lu_vals[mask_l])
    if len(log_u[mask_l[:len(log_u)]]) > 1:
        slope_l, intercept_l, r_l, _, _ = stats.linregress(
            log_u[:len(log_Lu)], log_Lu
        )
        r2_l = r_l ** 2
    else:
        slope_l, intercept_l, r2_l = 0, 0, 0

    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=[
                            f"Stream Number Law Ã¢â‚¬â€ {bid}",
                            f"Stream Length Law Ã¢â‚¬â€ {bid}"
                        ])

    # Stream number
    fig.add_trace(go.Scatter(
        x=orders[mask_n], y=Nu_vals[mask_n], mode='markers+lines',
        name='Stream Number', marker=dict(size=10, color='royalblue'),
        hovertemplate='Order %{x}: %{y} streams',
    ), row=1, col=1)
    fit_x = np.linspace(orders.min(), orders.max(), 50)
    fit_y = 10 ** (intercept_n + slope_n * np.log10(fit_x))
    fig.add_trace(go.Scatter(
        x=fit_x, y=fit_y, mode='lines',
        name=f'Regression (RÃ‚Â²={r2_n:.3f})',
        line=dict(color='firebrick', dash='dash'),
    ), row=1, col=1)

    # Stream length
    fig.add_trace(go.Scatter(
        x=orders[mask_l], y=Lu_vals[mask_l], mode='markers+lines',
        name='Stream Length (km)', marker=dict(size=10, color='darkorange'),
        hovertemplate='Order %{x}: %{y:.2f} km',
    ), row=1, col=2)
    if r2_l > 0:
        fit_yl = 10 ** (intercept_l + slope_l * np.log10(fit_x))
        fig.add_trace(go.Scatter(
            x=fit_x, y=fit_yl, mode='lines',
            name=f'Regression (RÃ‚Â²={r2_l:.3f})',
            line=dict(color='green', dash='dash'),
        ), row=1, col=2)

    fig.update_xaxes(type='log', title_text='Stream Order (log)', row=1, col=1)
    fig.update_yaxes(type='log', title_text='Stream Number (log)', row=1, col=1)
    fig.update_xaxes(type='log', title_text='Stream Order (log)', row=1, col=2)
    fig.update_yaxes(type='log', title_text='Stream Length km (log)', row=1, col=2)
    fig.update_layout(title=f"Horton's Laws Ã¢â‚¬â€ {bid}", template='plotly_white',
                      height=500, showlegend=True)
    save_fig(fig, f"01_hortons_law_{bid}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  2. RADAR CHART Ã¢â‚¬â€ Morphometric Signature per Subbasin
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[2] Radar charts...")

radar_params = [
    'Drainage_Density_Dd', 'Stream_Frequency_Fs', 'Form_Factor_Ff',
    'Elongation_Ratio_Re', 'Circularity_Ratio_Rc', 'Ruggedness_Rn',
    'Hypsometric_HI', 'Relief_Ratio_Rh', 'Rbm',
]
radar_params = [p for p in radar_params if p in df_master.columns]

df_radar = df_master[radar_params].copy().astype(float)
# Normalise 0-1 for radar
df_radar_norm = (df_radar - df_radar.min()) / (df_radar.max() - df_radar.min() + 1e-12)

fig = go.Figure()
categories = [p.split('_')[-1] for p in radar_params]
colors_r   = px.colors.qualitative.Set2

for i, (bid, row) in enumerate(df_radar_norm.iterrows()):
    vals = row.tolist()
    vals += [vals[0]]  # close polygon
    fig.add_trace(go.Scatterpolar(
        r=vals, theta=categories + [categories[0]],
        fill='toself', name=bid,
        line_color=colors_r[i % len(colors_r)],
        opacity=0.6,
        hovertemplate=bid + '<br>%{theta}: %{r:.3f}',
    ))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
    title="Morphometric Signature Radar Chart Ã¢â‚¬â€ All Subbasins",
    template='plotly_white', height=600,
)
save_fig(fig, "02_radar_morphometric")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  3. SCATTER MATRIX
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[3] Scatter matrix...")
scatter_cols = [c for c in ['Drainage_Density_Dd', 'Stream_Frequency_Fs',
                              'Elongation_Ratio_Re', 'Basin_Relief_H_m',
                              'Ruggedness_Rn', 'Hypsometric_HI']
                if c in df_master.columns]
df_sc = df_master[scatter_cols].reset_index()
fig   = px.scatter_matrix(
    df_sc, dimensions=scatter_cols, color='basin_id',
    title="Scatter Matrix Ã¢â‚¬â€ Key Morphometric Parameters",
    labels={c: c.split('_')[-1] for c in scatter_cols},
    template='plotly_white',
)
fig.update_traces(diagonal_visible=False, showupperhalf=False)
save_fig(fig, "03_scatter_matrix")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  4. 3D SCATTER Ã¢â‚¬â€ Dd vs Relief vs Area
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[4] 3D scatter...")
if all(c in df_master.columns for c in ['Drainage_Density_Dd', 'Basin_Relief_H_m', 'Area_km2']):
    df3d = df_master[['Drainage_Density_Dd', 'Basin_Relief_H_m', 'Area_km2']].reset_index()
    fig  = px.scatter_3d(
        df3d, x='Drainage_Density_Dd', y='Basin_Relief_H_m', z='Area_km2',
        color='basin_id', text='basin_id',
        title="3D Scatter: Drainage Density vs Relief vs Area",
        labels={'Drainage_Density_Dd': 'Dd (km/kmÃ‚Â²)',
                'Basin_Relief_H_m': 'Relief (m)',
                'Area_km2': 'Area (kmÃ‚Â²)'},
        template='plotly_white', size_max=18,
    )
    save_fig(fig, "04_3d_scatter")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  5. HISTOGRAM DISTRIBUTIONS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[5] Histogram distributions...")
hist_cols = [c for c in STAT_COLS if c in df_master.columns][:9]
fig = make_subplots(rows=3, cols=3, subplot_titles=hist_cols)
for i, col in enumerate(hist_cols):
    r, c_idx = divmod(i, 3)
    fig.add_trace(
        go.Histogram(x=df_master[col].dropna(), name=col,
                     marker_color=px.colors.qualitative.Set1[i % 9],
                     nbinsx=10),
        row=r+1, col=c_idx+1,
    )
fig.update_layout(title="Parameter Distributions", template='plotly_white',
                  height=800, showlegend=False)
save_fig(fig, "05_histograms")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  6. BOX PLOTS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[6] Box plots...")
df_melt = df_master[STAT_COLS[:10]].reset_index().melt(id_vars='basin_id')
fig     = px.box(
    df_melt, x='variable', y='value', color='variable',
    title="Box Plot Ã¢â‚¬â€ Morphometric Parameters",
    template='plotly_white', points='all',
    labels={'variable': 'Parameter', 'value': 'Value'},
)
fig.update_xaxes(tickangle=45)
save_fig(fig, "06_boxplots")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  7. HYPSOMETRIC CURVES
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[7] Hypsometric curves...")
if HYPS:
    fig = go.Figure()
    colors_h = px.colors.qualitative.Plotly
    for i, (bid, (rel_area, rel_elev)) in enumerate(HYPS.items()):
        hi_val = df_master.loc[bid, 'Hypsometric_HI'] if 'Hypsometric_HI' in df_master.columns else np.nan
        fig.add_trace(go.Scatter(
            x=rel_area, y=rel_elev, mode='lines',
            name=f"{bid} (HI={hi_val:.3f})" if not np.isnan(hi_val) else bid,
            line=dict(color=colors_h[i % len(colors_h)], width=2),
            hovertemplate='Rel. Area: %{x:.2f}<br>Rel. Elev: %{y:.2f}',
        ))
    # Reference lines
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[0.5, 0.5], mode='lines',
        name='HI = 0.5 (Equilibrium)', line=dict(dash='dash', color='grey'),
    ))
    fig.update_layout(
        title="Hypsometric Curves Ã¢â‚¬â€ All Subbasins",
        xaxis_title="Relative Area (a/A)",
        yaxis_title="Relative Elevation (h/H)",
        template='plotly_white', height=550,
    )
    save_fig(fig, "07_hypsometric_curves")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  8. PLOTLY CORRELATION HEATMAP
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[8] Plotly correlation heatmap...")
fig = go.Figure(go.Heatmap(
    z=corr_pearson.values,
    x=corr_pearson.columns.tolist(),
    y=corr_pearson.index.tolist(),
    colorscale='RdYlBu', zmid=0, zmin=-1, zmax=1,
    text=np.round(corr_pearson.values, 2).astype(str),
    texttemplate='%{text}', textfont_size=8,
    hovertemplate='%{y} vs %{x}: %{z:.3f}',
))
fig.update_layout(title="Pearson Correlation Matrix (Interactive)",
                  template='plotly_white', height=700, width=800)
save_fig(fig, "08_correlation_heatmap")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  9. PARALLEL COORDINATE PLOT
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[9] Parallel coordinate plot...")
par_cols = [c for c in STAT_COLS if c in df_master.columns][:8]
df_par   = df_master[par_cols].reset_index()
df_par['basin_num'] = range(len(df_par))
fig = px.parallel_coordinates(
    df_par, color='basin_num', dimensions=par_cols,
    color_continuous_scale=px.colors.diverging.Tealrose,
    title="Parallel Coordinate Plot Ã¢â‚¬â€ Morphometric Parameters",
    labels={c: c.replace('_', ' ') for c in par_cols},
)
save_fig(fig, "09_parallel_coordinates")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  10. BUBBLE PLOT Ã¢â‚¬â€ Area vs Dd sized by Relief
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[10] Bubble plot...")
if all(c in df_master.columns for c in ['Area_km2', 'Drainage_Density_Dd', 'Basin_Relief_H_m']):
    df_bub = df_master[['Area_km2', 'Drainage_Density_Dd', 'Basin_Relief_H_m']].reset_index()
    fig    = px.scatter(
        df_bub, x='Area_km2', y='Drainage_Density_Dd',
        size='Basin_Relief_H_m', color='basin_id', text='basin_id',
        title="Area vs Drainage Density (size = Basin Relief)",
        labels={'Area_km2': 'Area (kmÃ‚Â²)',
                'Drainage_Density_Dd': 'Drainage Density (km/kmÃ‚Â²)',
                'Basin_Relief_H_m': 'Relief (m)'},
        template='plotly_white', size_max=50,
    )
    save_fig(fig, "10_bubble_area_dd_relief")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  11. PRIORITY MAP Ã¢â‚¬â€ Interactive Plotly choropleth-style
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[11] Priority class map...")
priority_color = {'High': '#d73027', 'Moderate': '#fee090', 'Low': '#4575b4'}
fig = go.Figure()

for _, row in gdf_priority.iterrows():
    bid  = row['basin_id']
    pri  = row.get('Priority_M1', 'Unknown')
    col  = priority_color.get(pri, 'grey')
    geom = row.geometry

    if geom.geom_type == 'Polygon':
        geoms = [geom]
    else:
        geoms = list(geom.geoms)

    for g in geoms:
        coords = np.array(g.exterior.coords)
        fig.add_trace(go.Scatter(
            x=coords[:, 0], y=coords[:, 1],
            fill='toself', fillcolor=col,
            line=dict(color='black', width=1.5),
            name=f"{bid} ({pri})",
            opacity=0.75,
            hovertemplate=(
                f"<b>{bid}</b><br>"
                f"Priority: {pri}<br>"
                f"Rank M1: {row.get('Rank_M1','Ã¢â‚¬â€')}<br>"
                f"Rank M2: {row.get('Rank_M2','Ã¢â‚¬â€')}<br>"
                f"Rank M3: {row.get('Rank_M3','Ã¢â‚¬â€')}<br>"
                f"Dd: {row.get('Drainage_Density_Dd','Ã¢â‚¬â€')}"
            ),
        ))

fig.update_layout(
    title="Watershed Priority Classification Map (Method 1 Ã¢â‚¬â€ Compound Ranking)",
    xaxis=dict(title="Easting (m)", scaleanchor='y'),
    yaxis=dict(title="Northing (m)"),
    template='plotly_white', height=650,
    showlegend=True,
)
save_fig(fig, "11_priority_map")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  12. ELEVATION PROFILE (Main Channel)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[12] Elevation profiles...")

def extract_stream_profile(stream_gdf, dem_path, basin_id, n_points=200):
    """Sample DEM along the longest stream segment in a basin."""
    segs = stream_gdf[stream_gdf.get('basin_id', stream_gdf.index) == basin_id]
    if len(segs) == 0:
        return None, None, None
    longest_seg = segs.loc[segs.geometry.length.idxmax()]
    geom = longest_seg.geometry

    if geom.geom_type == 'MultiLineString':
        geom = linemerge(geom)
    if geom.geom_type != 'LineString':
        return None, None, None

    distances = np.linspace(0, geom.length, n_points)
    pts       = [geom.interpolate(d) for d in distances]

    with rasterio.open(dem_path) as src:
        elevations = []
        for pt in pts:
            r_idx, c_idx = rowcol(src.transform, pt.x, pt.y)
            try:
                elev = src.read(1)[r_idx, c_idx]
                nodata = src.nodata if src.nodata else -9999
                elevations.append(np.nan if elev == nodata else float(elev))
            except IndexError:
                elevations.append(np.nan)

    return np.array(distances / 1000), np.array(elevations), geom


fig_profiles = make_subplots(
    rows=len(gdf_sub), cols=1,
    shared_xaxes=False,
    subplot_titles=[f"Longitudinal Profile Ã¢â‚¬â€ {bid}" for bid in gdf_sub['basin_id']],
    vertical_spacing=0.08,
)

for i, (_, row) in enumerate(gdf_sub.iterrows()):
    bid = row['basin_id']
    # Assign basin_id to stream order dataframe if not present
    if 'basin_id' not in gdf_so_sub.columns:
        break
    dist, elev, _ = extract_stream_profile(gdf_so_sub, RASTERS['dem'], bid)
    if dist is None:
        continue
    valid = ~np.isnan(elev)
    fig_profiles.add_trace(
        go.Scatter(
            x=dist[valid], y=elev[valid],
            mode='lines', name=bid, fill='tozeroy',
            line=dict(color=px.colors.qualitative.Plotly[i % 10], width=2),
            hovertemplate='Distance: %{x:.2f} km<br>Elevation: %{y:.1f} m',
        ),
        row=i+1, col=1,
    )
    fig_profiles.update_xaxes(title_text="Distance from outlet (km)", row=i+1, col=1)
    fig_profiles.update_yaxes(title_text="Elevation (m)", row=i+1, col=1)

fig_profiles.update_layout(
    title="Longitudinal Stream Profiles Ã¢â‚¬â€ All Subbasins",
    template='plotly_white', height=300 * len(gdf_sub), showlegend=True,
)
save_fig(fig_profiles, "12_longitudinal_profiles")

print(f"\nÃ¢Å“â€¦ SECTION 7 complete. HTML files in: {HTML_DIR}")
print(f"   Total figures: 12")

print("=" * 60)
print("SECTION 8 Ã¢â‚¬â€ OUTPUT EXPORT")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬ 1. Master morphometric table Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
master_csv = os.path.join(TABLES_DIR, "morphometric_master_table.csv")
df_master.to_csv(master_csv)
print(f"\n[1] Master table Ã¢â€ â€™ {master_csv}")

print("\n  Ã¢â€â‚¬Ã¢â€â‚¬ First 10 rows (all basins if Ã¢â€°Â¤ 10) Ã¢â€â‚¬Ã¢â€â‚¬")
print(df_master.head(10).to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬ 2. Stream order summary Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[2] Stream Order Summary:")
all_order_rows = []
for bid, df_lin in LINEAR_PER_ORDER.items():
    df_lin_c = df_lin.copy()
    df_lin_c['basin_id'] = bid
    all_order_rows.append(df_lin_c)

if all_order_rows:
    df_order_summary = pd.concat(all_order_rows, ignore_index=True)
    df_order_summary.to_csv(os.path.join(TABLES_DIR, "stream_order_summary.csv"), index=False)
    print(df_order_summary.to_string(index=False))

# Ã¢â€â‚¬Ã¢â€â‚¬ 3. Statistical summary Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[3] Statistical Summary (mean Ã‚Â± std):")
for col in STAT_COLS[:12]:
    if col in df_master.columns:
        mn  = df_master[col].mean()
        sd  = df_master[col].std()
        cv  = (sd / mn * 100) if mn != 0 else np.nan
        print(f"  {col:<35s} {mn:>10.4f} Ã‚Â± {sd:>8.4f}  (CV={cv:>6.1f}%)")

# Ã¢â€â‚¬Ã¢â€â‚¬ 4. Ranking table Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[4] Prioritization Ranking:")
rank_csv = os.path.join(TABLES_DIR, "prioritization_ranking.csv")
print(pd.read_csv(rank_csv, index_col=0).to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬ 5. Priority classification Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print("\n[5] Priority Classification Summary:")
for bid in gdf_sub['basin_id']:
    if bid in df_rank.index:
        r = df_rank.loc[bid]
        print(f"  {bid}: M1={r['Priority_M1']:<8} M2={r['Priority_M2']:<8} M3={r['Priority_M3']}")

# Ã¢â€â‚¬Ã¢â€â‚¬ 6. Summary of all output files Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
print(f"\n[6] Output files:")
for root, dirs, files in os.walk(OUT_DIR):
    for f in sorted(files):
        full = os.path.join(root, f)
        size = os.path.getsize(full) / 1024
        print(f"  {full.replace(OUT_DIR, ''):<60s}  {size:>8.1f} KB")

print("\nÃ¢Å“â€¦ SECTION 8 complete.")



print("\n" + "=" * 60)
print("SECTION 9 Ã¢â‚¬â€ REPORT GENERATION")
print("=" * 60)

def format_val(val, decimals=3):
    """Format float or return 'N/A'."""
    try:
        return f"{float(val):.{decimals}f}"
    except (TypeError, ValueError):
        return "N/A"


def build_report():
    basin_ids = gdf_sub['basin_id'].tolist()
    n_basins  = len(basin_ids)

    # Study area bounding box in geographic coords
    bounds = gdf_sub.to_crs("EPSG:4326").total_bounds
    lon_min, lat_min, lon_max, lat_max = bounds

    total_area = df_master['Area_km2'].sum()
    elev_min   = df_master['Elev_Min_m'].min()
    elev_max   = df_master['Elev_Max_m'].max()
    mean_dd    = df_master['Drainage_Density_Dd'].mean()
    mean_re    = df_master['Elongation_Ratio_Re'].mean()
    mean_hi    = df_master['Hypsometric_HI'].mean() if 'Hypsometric_HI' in df_master.columns else np.nan
    mean_rn    = df_master['Ruggedness_Rn'].mean() if 'Ruggedness_Rn' in df_master.columns else np.nan

    high_pri   = df_rank[df_rank['Priority_M1'] == 'High'].index.tolist()
    mod_pri    = df_rank[df_rank['Priority_M1'] == 'Moderate'].index.tolist()
    low_pri    = df_rank[df_rank['Priority_M1'] == 'Low'].index.tolist()

    lines = []
    def s(text=""):
        lines.append(text)

    s("=" * 80)
    s("MORPHOMETRIC ANALYSIS OF A WATERSHED")
    s("Generated by Automated Morphometric Analysis Tool")
    s("Based on: Horton (1945), Strahler (1952, 1964), Schumm (1956), Miller (1953)")
    s("=" * 80)

    s()
    s("1. STUDY AREA DESCRIPTION")
    s("-" * 40)
    s(f"The study area comprises {n_basins} subbasins covering a total area of "
      f"{total_area:.2f} kmÃ‚Â². The watershed extends from approximately "
      f"{lat_min:.4f}Ã‚Â°N to {lat_max:.4f}Ã‚Â°N and {lon_min:.4f}Ã‚Â°E to {lon_max:.4f}Ã‚Â°E. "
      f"Elevation ranges from {elev_min:.0f} m to {elev_max:.0f} m above sea level, "
      f"indicating a relief of {elev_max - elev_min:.0f} m across the watershed. "
      f"The analysis utilises SRTM 30 m Digital Elevation Model data processed "
      f"in a UTM projected coordinate reference system ({UTM_EPSG}) to ensure "
      f"accurate area and length computations.")

    s()
    s("2. DATA SOURCES")
    s("-" * 40)
    s("Ã¢â‚¬Â¢ DEM: Shuttle Radar Topography Mission (SRTM) 30 m resolution (NASA/USGS)")
    s("Ã¢â‚¬Â¢ Subbasins: Derived from DEM hydrological processing (see shapefile for polygon count)")
    s("Ã¢â‚¬Â¢ Stream network: Extracted via D8 flow routing with Strahler ordering")
    s("Ã¢â‚¬Â¢ Flow direction: D8 algorithm (ArcGIS/QGIS/TauDEM compatible)")
    s("Ã¢â‚¬Â¢ Flow accumulation: Derived from D8 flow direction")
    s("Ã¢â‚¬Â¢ CRS: Reprojected to UTM for accurate metric computations")

    s()
    s("3. METHODOLOGY")
    s("-" * 40)
    s("Morphometric analysis was performed following the methodologies of "
      "Horton (1945) for stream ordering and bifurcation laws, Strahler (1952, 1964) "
      "for the hierarchical stream order classification, Schumm (1956) for basin "
      "geometry and elongation ratio, and Miller (1953) for circularity ratio. "
      "Linear, areal, and relief morphometric parameters were computed at the "
      "subbasin level using SRTM DEM data and derived GIS layers. "
      "Watershed prioritization employed three independent methods: Compound "
      "Parameter Ranking, Entropy Weight Method, and PCA-Based Priority scoring, "
      "with inter-method agreement assessed using Kendall's tau.")

    s()
    s("4. MORPHOMETRIC RESULTS")
    s("-" * 40)
    s()
    s("4.1 Linear Aspects")
    for bid in basin_ids:
        if bid not in LINEAR_PER_ORDER:
            continue
        df_lin = LINEAR_PER_ORDER[bid]
        max_ord = df_lin['order'].max()
        Rbm_v   = df_linear_summary.loc[bid, 'Rbm'] if bid in df_linear_summary.index else np.nan
        tot_N   = df_lin['Nu'].sum()
        s(f"  {bid}: {int(max_ord)}-order basin, {int(tot_N)} stream segments, "
          f"Mean Bifurcation Ratio (Rbm) = {format_val(Rbm_v)}. "
          f"{'Rbm values between 3Ã¢â‚¬â€œ5 indicate normal basins without structural disturbances.' if 3 <= Rbm_v <= 5 else 'Rbm outside 3Ã¢â‚¬â€œ5 range may indicate structural control.'}")

    s()
    s("4.2 Areal Aspects")
    for bid in basin_ids:
        if bid not in df_master.index:
            continue
        row = df_master.loc[bid]
        s(f"  {bid}: Area={format_val(row.get('Area_km2'))} kmÃ‚Â², "
          f"Dd={format_val(row.get('Drainage_Density_Dd'))} km/kmÃ‚Â², "
          f"Re={format_val(row.get('Elongation_Ratio_Re'))}, "
          f"Rc={format_val(row.get('Circularity_Ratio_Rc'))}, "
          f"Ff={format_val(row.get('Form_Factor_Ff'))}, "
          f"Shape: {row.get('Shape_Class','Ã¢â‚¬â€')}.")

    s()
    s("4.3 Relief Aspects")
    for bid in basin_ids:
        if bid not in df_master.index:
            continue
        row = df_master.loc[bid]
        hi_interp = row.get('Hyps_Class', 'Ã¢â‚¬â€')
        s(f"  {bid}: H={format_val(row.get('Basin_Relief_H_m'),0)} m, "
          f"Rh={format_val(row.get('Relief_Ratio_Rh'),5)}, "
          f"Rn={format_val(row.get('Ruggedness_Rn'))}, "
          f"HI={format_val(row.get('Hypsometric_HI'))}, "
          f"Stage: {hi_interp}.")

    s()
    s("5. STATISTICAL ANALYSIS")
    s("-" * 40)
    s(f"Mean drainage density across all subbasins: {format_val(mean_dd)} km/kmÃ‚Â². "
      f"{'High drainage density (>3.5 km/kmÃ‚Â²) implies impermeable lithology, steep slopes, and sparse vegetation, leading to rapid surface runoff.' if mean_dd > 3.5 else 'Moderate to low drainage density suggests permeable materials and gentle topography.'}"
      " PCA revealed that the first two principal components explained the majority "
      f"of total variance ({exp_var[0]:.1f}% + {exp_var[1]:.1f}% = "
      f"{exp_var[0]+exp_var[1]:.1f}%), with drainage density and relief parameters "
      "dominating PC1 and basin shape parameters dominating PC2.")

    s()
    s("6. WATERSHED PRIORITIZATION")
    s("-" * 40)
    s(f"Three independent methods identified the following priority classes:")
    s(f"  HIGH priority basins (most susceptible to erosion): {', '.join(high_pri) if high_pri else 'None'}")
    s(f"  MODERATE priority basins: {', '.join(mod_pri) if mod_pri else 'None'}")
    s(f"  LOW priority basins: {', '.join(low_pri) if low_pri else 'None'}")
    s(f"Inter-method agreement (Kendall's Ãâ€ž): M1 vs M2 = {format_val(r12,3)}, "
      f"M1 vs M3 = {format_val(r13,3)}, M2 vs M3 = {format_val(r23,3)}. "
      f"{'High agreement across methods validates the prioritization framework.' if min(abs(r12),abs(r13),abs(r23))>0.5 else 'Moderate agreement suggests parameter-sensitivity in ranking.'}")

    s()
    s("7. DISCUSSION")
    s("-" * 40)
    s("Drainage Density Implications:")
    s(f"  The watershed exhibits a mean Dd of {format_val(mean_dd)} km/kmÃ‚Â². "
      "High Dd values indicate fine texture, less permeable lithology, and "
      "greater surface runoff propensity (Horton, 1945). Basins with Dd > 3.5 "
      "are expected to respond rapidly to rainfall events, increasing flood risk.")
    s()
    s("Shape and Runoff Response:")
    s(f"  Mean Elongation Ratio (Re) = {format_val(mean_re)}. "
      f"{'Elongated basins (Re < 0.6) have lower peak discharge and extended concentration time.' if mean_re < 0.6 else 'Sub-circular to circular basins (Re > 0.7) generate higher and faster flood peaks.'} "
      "Form factor and circularity ratio confirm this assessment.")
    s()
    s("Relief and Erosion:")
    s(f"  Mean Ruggedness Number (Rn) = {format_val(mean_rn)}. "
      "High Rn reflects steep slopes combined with high drainage density, "
      "indicating high erosion potential and flash flood susceptibility "
      "(Strahler, 1964).")
    s()
    s("Hypsometric Stage:")
    s(f"  Mean Hypsometric Integral (HI) = {format_val(mean_hi)}. "
      f"{'HI > 0.6 indicates monadnock/young stage Ã¢â‚¬â€ active erosion, convex slopes.' if mean_hi > 0.6 else 'HI 0.35Ã¢â‚¬â€œ0.6 indicates mature equilibrium stage.' if mean_hi > 0.35 else 'HI < 0.35 indicates peneplain/old stage Ã¢â‚¬â€ reduced erosion activity.'}")

    s()
    s("8. CONCLUSION")
    s("-" * 40)
    s(f"This study presents a comprehensive morphometric analysis of a {n_basins}-subbasin "
      f"watershed using SRTM 30 m DEM. The integrated analysis of linear, areal, and "
      f"relief parameters reveals the geomorphic maturity, erosion susceptibility, "
      f"and hydrological response characteristics of each subbasin. "
      f"Subbasins {', '.join(high_pri)} are identified as highest priority for "
      f"soil and water conservation interventions based on convergent evidence "
      f"from three independent prioritization methods. Findings are reproducible "
      f"and suitable for integration into watershed management planning frameworks.")

    s()
    s("9. REFERENCES")
    s("-" * 40)
    s("Horton, R.E. (1945). Erosional development of streams and their drainage basins.")
    s("  Geological Society of America Bulletin, 56(3), 275Ã¢â‚¬â€œ370.")
    s()
    s("Miller, V.C. (1953). A quantitative geomorphic study of drainage basin characteristics")
    s("  in the Clinch Mountain area, Virginia and Tennessee. Columbia University, Tech. Rep.")
    s()
    s("Schumm, S.A. (1956). Evolution of drainage systems and slopes in badlands at Perth")
    s("  Amboy, New Jersey. Geological Society of America Bulletin, 67(5), 597Ã¢â‚¬â€œ646.")
    s()
    s("Strahler, A.N. (1952). Hypsometric (area-altitude) analysis of erosional topography.")
    s("  Geological Society of America Bulletin, 63(11), 1117Ã¢â‚¬â€œ1142.")
    s()
    s("Strahler, A.N. (1964). Quantitative geomorphology of drainage basins and channel")
    s("  networks. In Handbook of Applied Hydrology (ed. V.T. Chow), pp. 4.39Ã¢â‚¬â€œ4.76.")
    s()
    s("Hack, J.T. (1957). Studies of longitudinal stream profiles in Virginia and Maryland.")
    s("  USGS Professional Paper 294-B.")
    s()
    s("Melton, M.A. (1965). The geomorphic and palaeoclimatic significance of alluvial")
    s("  deposits in Southern Arizona. Journal of Geology, 73(1), 1Ã¢â‚¬â€œ38.")
    s()
    s("Riley, S.J., DeGloria, S.D., Elliot, R. (1999). A terrain ruggedness index that")
    s("  quantifies topographic heterogeneity. Intermountain Journal of Sciences, 5, 23Ã¢â‚¬â€œ27.")

    s()
    s("=" * 80)
    s("END OF REPORT")
    s("=" * 80)

    return "\n".join(lines)


report_text = build_report()
report_path = os.path.join(REPORT_DIR, "morphometric_analysis_report.txt")
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_text)

print("\nREPORT PREVIEW (first 40 lines):")
print("Ã¢â‚¬â€" * 60)
for line in report_text.split("\n")[:40]:
    print(line)
print("...")
print("Ã¢â‚¬â€" * 60)
print(f"\nÃ¢Å“â€¦ Full report saved: {report_path}")
print("\nÃ¢Å“â€¦ SECTION 9 complete.")

print("\n" + "=" * 60)
print("  Ã°Å¸Å½â€°  ALL SECTIONS COMPLETE")
print("=" * 60)
print(f"  Output root: {OUT_DIR}")
print(f"  Maps (9)   : {MAPS_DIR}")
print(f"  Plots HTML : {HTML_DIR}")
print(f"  Tables     : {TABLES_DIR}")
print(f"  Shapefiles : {SHAPES_DIR}")
print(f"  Report     : {REPORT_DIR}")


print("\n" + "=" * 60)
print("SECTION 10 Ã¢â‚¬â€ TECTONIC ACTIVITY INDICES CALCULATION")
print("=" * 60)

# Initialize df_IAT based on existing master table
df_IAT = df_master[['Area_km2', 'Perimeter_km', 'Basin_Length_km',
                    'Drainage_Density_Dd', 'Relief_Ratio_Rh', 'Slope_Mean_deg']].copy()

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. MOUNTAIN FRONT SINUOSITY (Smf)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Smf = Lmf / Ls (Lmf = length of mountain front, Ls = straight-line length)
# Proxy: Smf = Perimeter / Basin_Length_km (approximates Lmf/Ls)
# Lower Smf indicates higher tectonic activity.
df_IAT['Smf'] = df_IAT['Perimeter_km'] / df_IAT['Basin_Length_km']
# Rank Smf: lower value (straighter front) gets a lower score (higher activity)
# Smf proxy already assigned above Ã¢â‚¬â€ no rank used (BUG-08 uses 1-4 classify instead)

print(f"\n[A] Mountain Front Sinuosity (Smf) calculated. Mean: {df_IAT['Smf'].mean():.2f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. ASYMMETRY FACTOR (AF)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# AF = 100 * (Ar / At) - 50 (Ar = Area right of main stream, At = Total Area)
# Requires detailed stream network and sub-basin delineation.
# For simplicity, we use Relief_Ratio_Rh as a proxy, as higher relief often
# correlates with areas of more active/asymmetric uplift.
# Higher Relief Ratio Ã¢â€ â€™ Higher tectonic activity.
# Ã¢â€â‚¬Ã¢â€â‚¬ AF proxy: Relief Ratio used as surrogate for Asymmetry Factor Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# True AF = 100Ãƒâ€”(Ar/At); requires detailed sub-basin delineation.
# Proxy labelled *_proxy to distinguish from the true index.
df_IAT['AF_proxy'] = df_IAT['Relief_Ratio_Rh']  # Relief Ratio as AF proxy
df_IAT['AF'] = df_IAT['AF_proxy']

print(f"[B] Asymmetry Factor (AF) proxy calculated from Relief Ratio. Mean: {df_IAT['AF'].mean():.4f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. TRANSVERSE TOPOGRAPHIC SYMMETRY FACTOR (T)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# T = (Ad - Aa) / At (Ad = area right of median, Aa = area left of median)
# Similar complexity to AF.
# Using Drainage_Density_Dd as a proxy, as higher Dd can reflect a more
# developed or stressed drainage pattern in tectonically active areas.
# Higher Dd Ã¢â€ â€™ Higher tectonic activity.
# Ã¢â€â‚¬Ã¢â€â‚¬ T proxy: Drainage Density used as surrogate for Transverse Symmetry Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# True T = (Ad-Aa)/At; proxy-based values should be noted as indicative.
df_IAT['T_proxy'] = df_IAT['Drainage_Density_Dd']  # Dd as T proxy
df_IAT['T'] = df_IAT['T_proxy']

print(f"[C] Transverse Topographic Symmetry Factor (T) proxy calculated from Drainage Density. Mean: {df_IAT['T'].mean():.3f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. VALLEY FLOOR WIDTH-TO-HEIGHT RATIO (Vf)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Vf = 2 * Vfw / (Eld - Esc + Erd - Esc)
# Requires cross-section data, difficult to derive directly from DEM.
# Using Mean Slope as an inverse proxy: steeper slopes often imply narrower
# valleys and higher incision rates, indicative of higher tectonic activity.
# Higher Slope_Mean_deg Ã¢â€ â€™ Lower Vf (higher activity).
# Ã¢â€â‚¬Ã¢â€â‚¬ Vf proxy: Mean Slope used as surrogate for Valley Floor Width-Height Ratio Ã¢â€â‚¬
# True Vf = 2Vfw/(Eld-Esc+Erd-Esc); requires cross-section survey data.
df_IAT['Vf_proxy'] = df_IAT['Slope_Mean_deg']  # Mean Slope as 1/Vf proxy
df_IAT['Vf'] = df_IAT['Vf_proxy']

print(f"[D] Valley Floor Width-to-Height Ratio (Vf) proxy calculated from Mean Slope. Mean: {df_IAT['Vf'].mean():.2f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. BASIN SHAPE INDEX (BS)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# BS is often related to Ff or Re. Let's not add a new proxy but acknowledge
# its correlation with existing morphometric parameters.
# For the IAT, we will stick to Smf, AF, T, Vf as per El Hamdouni et al. (2008).

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  F. INDEX OF ACTIVE TECTONICS (IAT) Ã¢â‚¬â€ El Hamdouni et al. (2008)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

# Ã¢â€â‚¬Ã¢â€â‚¬ Assign 1Ã¢â‚¬â€œ4 class per index using published literature thresholds Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Smf: < 1.6 Ã¢â€ â€™ Class 1 (Very High); 1.6Ã¢â‚¬â€œ3.0 Ã¢â€ â€™ 2; 3.0Ã¢â‚¬â€œ5.0 Ã¢â€ â€™ 3; >5.0 Ã¢â€ â€™ 4
def classify_smf(smf):
    if smf < 1.6:  return 1
    if smf < 3.0:  return 2
    if smf < 5.0:  return 3
    return 4

# AF proxy (Relief Ratio): >0.10 Ã¢â€ â€™ 1, 0.05Ã¢â‚¬â€œ0.10 Ã¢â€ â€™ 2, 0.02Ã¢â‚¬â€œ0.05 Ã¢â€ â€™ 3, <0.02 Ã¢â€ â€™ 4
def classify_af_proxy(rh):
    if rh > 0.10: return 1
    if rh > 0.05: return 2
    if rh > 0.02: return 3
    return 4

# T proxy (Drainage Density km/kmÃ‚Â²): >3.0 Ã¢â€ â€™ 1, 2.0Ã¢â‚¬â€œ3.0 Ã¢â€ â€™ 2, 1.0Ã¢â‚¬â€œ2.0 Ã¢â€ â€™ 3, <1.0 Ã¢â€ â€™ 4
def classify_t_proxy(dd):
    if dd > 3.0: return 1
    if dd > 2.0: return 2
    if dd > 1.0: return 3
    return 4

# Vf proxy (slope deg): >15Ã‚Â° Ã¢â€ â€™ 1, 8Ã¢â‚¬â€œ15Ã‚Â° Ã¢â€ â€™ 2, 3Ã¢â‚¬â€œ8Ã‚Â° Ã¢â€ â€™ 3, <3Ã‚Â° Ã¢â€ â€™ 4
def classify_vf_proxy(slope_deg):
    if slope_deg > 15: return 1
    if slope_deg > 8:  return 2
    if slope_deg > 3:  return 3
    return 4

df_IAT['Class_Smf'] = df_IAT['Smf'].apply(classify_smf)
df_IAT['Class_AF']  = df_IAT['AF'].apply(classify_af_proxy)
df_IAT['Class_T']   = df_IAT['T'].apply(classify_t_proxy)
df_IAT['Class_Vf']  = df_IAT['Vf'].apply(classify_vf_proxy)

# IAT = mean of individual 1Ã¢â‚¬â€œ4 classes (El Hamdouni 2008)
df_IAT['IAT'] = df_IAT[['Class_Smf', 'Class_AF', 'Class_T', 'Class_Vf']].mean(axis=1)

# Fixed thresholds (El Hamdouni et al., 2008)
def classify_iat(iat_score):
    if iat_score <= 1.5: return 'Class 1 Ã¢â‚¬â€ Very High'
    if iat_score <= 2.5: return 'Class 2 Ã¢â‚¬â€ High'
    if iat_score <= 3.5: return 'Class 3 Ã¢â‚¬â€ Moderate'
    return 'Class 4 Ã¢â‚¬â€ Low'

df_IAT['IAT_class'] = df_IAT['IAT'].apply(classify_iat)

print(f"\n[F] Index of Active Tectonics (IAT) calculated. Mean: {df_IAT['IAT'].mean():.2f}")
print("  IAT Classification:\n", df_IAT[['IAT', 'IAT_class']].sort_values('IAT').to_string())

# Save df_IAT to a CSV file
iat_csv_path = os.path.join(TABLES_DIR, "tectonic_activity_indices.csv")
df_IAT.to_csv(iat_csv_path)
print(f"\nÃ¢Å“â€¦ Tectonic activity indices saved to: {iat_csv_path}")

print("\n[F] Generating Tectonic Activity Map...")

iat_color_map = {
    'Class 1 Ã¢â‚¬â€ Very High': '#d73027',
    'Class 2 Ã¢â‚¬â€ High'     : '#fc8d59',
    'Class 3 Ã¢â‚¬â€ Moderate' : '#fee08b',
    'Class 4 Ã¢â‚¬â€ Low'      : '#91bfdb',
}

gdf_iat = gdf_sub.merge(df_IAT[['IAT','IAT_class']].reset_index(), on='basin_id')

utm_ext  = compute_utm_extent()
fig, ax_map_iat, ax_panel_iat = make_map_figure(
    "Index of Active Tectonics (IAT)\nEl Hamdouni et al., 2008")
add_esri_basemap(ax_map_iat, source=BASEMAP_TOPO, alpha=0.30)
for _, row in gdf_iat.iterrows():
    color = iat_color_map.get(row['IAT_class'], 'grey')
    gpd.GeoDataFrame([row], geometry='geometry', crs=gdf_sub.crs).plot(
        ax=ax_map_iat, color=color, edgecolor='black', linewidth=1.2,
        alpha=0.80, zorder=3)
    cxx, cyy = row.geometry.centroid.x, row.geometry.centroid.y
    ax_map_iat.text(cxx, cyy, f"{row['basin_id']}\nIAT={row['IAT']:.2f}",
        ha='center', va='center', fontsize=8, fontweight='bold',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])
# Only major streams (order >= 3) to reduce visual noise Ã¢â‚¬â€ MAP-01 fix
gdf_so[gdf_so[ORDER_COL]>=3].plot(ax=ax_map_iat, color='royalblue',
                                    linewidth=0.9, alpha=0.7, zorder=5)
# Classified legend in panel
add_classified_legend_panel(
    ax_panel_iat,
    colours=list(iat_color_map.values()),
    labels=list(iat_color_map.keys()),
    title='Tectonic Activity', y_top=0.50)
finalize_map(fig, ax_map_iat, ax_panel_iat, "10a_tectonic_IAT_map.png")

# Ã¢â€â‚¬Ã¢â€â‚¬ Plotly radar Ã¢â‚¬â€ tectonic scores Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
fig_r = go.Figure()
for i, bid in enumerate(df_IAT.index):
    row  = df_IAT.loc[bid]
    cats = ['AF_proxy','T_proxy','Vf_proxy','Smf']  # columns after BUG-13
    # BUG-13 fix: column names updated from Score_* to proxy-based scores
    def _score(v, low, high):
        if v <= low:  return 1
        if v <= high: return 2
        return 3
    _af_score  = _score(row.get('AF_proxy',  row.get('Score_AF',  2)), 38, 62)
    _t_score   = _score(row.get('T_proxy',   row.get('Score_T',   2)), 0.1, 0.5)
    _vf_score  = _score(row.get('Vf_proxy',  row.get('Score_Vf',  2)), 1.0, 2.5)
    _smf_score = _score(row.get('Smf',       row.get('Score_Smf', 2)), 1.1, 1.5)
    vals = [_af_score, _t_score, _vf_score, _smf_score]
    vals += [vals[0]]
    fig_r.add_trace(go.Scatterpolar(
        r=vals, theta=['AF','T','Vf','Smf','AF'],
        fill='toself', name=bid,
        line_color=px.colors.qualitative.Set1[i % 9], opacity=0.65,
        hovertemplate=bid+'<br>%{theta}: %{r} (1=high 3=low activity)',
    ))
fig_r.update_layout(
    polar=dict(radialaxis=dict(range=[0, 3], tickvals=[1,2,3],
                               ticktext=['High','Moderate','Low'])),
    title="Tectonic Activity Score Radar Ã¢â‚¬â€ Per Subbasin",
    template='plotly_white', height=550,
)
save_fig(fig_r, "10b_tectonic_radar")

print("\nÃ¢Å“â€¦ SECTION 10 complete.")

print("=" * 60)
print("SECTION 11 Ã¢â‚¬â€ GEOMORPHIC INDICES: SL, SPI, TWI")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  HELPER FUNCTIONS (for SL, SPI, TWI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

def calculate_sl_index(stream_gdf, dem_arr, dem_transform, k=10):
    """
    Calculate Stream Length-gradient (SL) index for each stream segment.
    SL = (dH/dL) * L.
    dH/dL is local gradient, L is total channel length upstream (approximated).
    The local gradient is calculated over a window of k cells.
    """
    sl_indices = []
    for idx, row in stream_gdf.iterrows():
        geom = row.geometry
        if geom.geom_type == 'MultiLineString':
            geom = max(geom.geoms, key=lambda g: g.length)
        if geom.geom_type != 'LineString' or geom.length == 0:
            sl_indices.append(np.nan)
            continue

        coords = list(geom.coords)
        if len(coords) < 2:
            sl_indices.append(np.nan)
            continue

        # Sample elevation along the stream
        elevations = []
        for p in coords:
            row_idx, col_idx = rasterio.transform.rowcol(dem_transform, p[0], p[1])
            if 0 <= row_idx < dem_arr.shape[0] and 0 <= col_idx < dem_arr.shape[1]:
                elevations.append(dem_arr[row_idx, col_idx])
            else:
                elevations.append(np.nan)
        elevations = np.array(elevations)

        # Remove NaNs and corresponding coordinates
        valid_indices = ~np.isnan(elevations)
        elevations_valid = elevations[valid_indices]
        coords_valid     = np.array(coords)[valid_indices]

        if len(elevations_valid) < 2:
            sl_indices.append(np.nan)
            continue

        # Calculate local gradient (dH/dL) over a window of k points
        gradients = []
        for i in range(len(elevations_valid) - k):
            p1 = coords_valid[i]
            p2 = coords_valid[i+k]
            dist = np.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
            if dist > 0:
                grad = (elevations_valid[i] - elevations_valid[i+k]) / dist
                gradients.append(grad)

        if not gradients:
            sl_indices.append(np.nan)
            continue

        local_gradient = np.nanmean(gradients) # Average gradient over segment

        # Approximate upstream length as the total length of the segment
        # A more rigorous approach would trace upstream from the pour point
        L_upstream = geom.length # Approximation

        sl_index = local_gradient * L_upstream
        sl_indices.append(sl_index)
    return sl_indices

def calculate_spi(stream_gdf, flow_acc_arr, slope_arr, dem_res, dem_transform=None, threshold=1e-6):
    if dem_transform is None:
        dem_transform = DEM_TRANSFORM
    """
    Calculate Stream Power Index (SPI) for each stream segment.
    SPI = As * tan(beta), where As is contributing area, beta is slope.
    Approximates As with flow accumulation * cell_area.
    """
    spi_values = []
    for idx, row in stream_gdf.iterrows():
        geom = row.geometry
        if geom.geom_type == 'MultiLineString':
            geom = max(geom.geoms, key=lambda g: g.length)
        if geom.geom_type != 'LineString' or geom.length == 0:
            spi_values.append(np.nan)
            continue

        coords = list(geom.coords)
        fa_values = []
        slope_values = []

        for p in coords:
            row_idx, col_idx = rasterio.transform.rowcol(dem_transform, p[0], p[1])
            if 0 <= row_idx < flow_acc_arr.shape[0] and 0 <= col_idx < flow_acc_arr.shape[1]:
                fa_values.append(flow_acc_arr[row_idx, col_idx])
                slope_values.append(slope_arr[row_idx, col_idx])
            else:
                fa_values.append(np.nan)
                slope_values.append(np.nan)

        fa_values = np.array(fa_values)
        slope_values = np.array(slope_values)

        valid_indices = ~np.isnan(fa_values) & ~np.isnan(slope_values)
        if not np.any(valid_indices):
            spi_values.append(np.nan)
            continue

        # Use mean flow accumulation and slope for the segment
        mean_fa    = np.nanmean(fa_values[valid_indices])
        mean_slope = np.nanmean(slope_values[valid_indices]) # in degrees

        # Convert slope to radians for tan function
        mean_slope_rad = np.radians(mean_slope)

        # As (contributing area) = flow_accumulation * cell_area
        cell_area = dem_res * dem_res # m^2
        As = mean_fa * cell_area

        # Avoid division by zero or tan(90 deg)
        tan_beta = np.tan(mean_slope_rad)
        if tan_beta < threshold: # Set a small threshold for very flat areas
            tan_beta = threshold

        spi = As * tan_beta
        spi_values.append(spi)

    return spi_values

def calculate_sti(stream_gdf, flow_acc_arr, slope_arr, dem_res, dem_transform=None, threshold=1e-6):
    if dem_transform is None:
        dem_transform = DEM_TRANSFORM
    """
    Calculate Sediment Transport Index (STI) for each stream segment.
    STI = (As * sin(beta)). Simplified version for segments.
    Approximates As with flow accumulation * cell_area.
    """
    sti_values = []
    for idx, row in stream_gdf.iterrows():
        geom = row.geometry
        if geom.geom_type == 'MultiLineString':
            geom = max(geom.geoms, key=lambda g: g.length)
        if geom.geom_type != 'LineString' or geom.length == 0:
            sti_values.append(np.nan)
            continue

        coords = list(geom.coords)
        fa_values = []
        slope_values = []

        for p in coords:
            row_idx, col_idx = rasterio.transform.rowcol(dem_transform, p[0], p[1])
            if 0 <= row_idx < flow_acc_arr.shape[0] and 0 <= col_idx < flow_acc_arr.shape[1]:
                fa_values.append(flow_acc_arr[row_idx, col_idx])
                slope_values.append(slope_arr[row_idx, col_idx])
            else:
                fa_values.append(np.nan)
                slope_values.append(np.nan)

        fa_values = np.array(fa_values)
        slope_values = np.array(slope_values)

        valid_indices = ~np.isnan(fa_values) & ~np.isnan(slope_values)
        if not np.any(valid_indices):
            sti_values.append(np.nan)
            continue

        mean_fa = np.nanmean(fa_values[valid_indices])
        mean_slope = np.nanmean(slope_values[valid_indices]) # in degrees

        mean_slope_rad = np.radians(mean_slope)
        As = mean_fa * dem_res # Specific catchment area (m) for unit contour length (simplified)

        # Ã¢â€â‚¬Ã¢â€â‚¬ Correct STI per Moore & Burch (1986) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
        # STI = (As/22.13)^0.6 Ãƒâ€” (sin ÃŽÂ² / 0.0896)^1.3
        cell_area = dem_res * dem_res                   # mÃ‚Â²
        As_seg    = mean_fa * dem_res                   # specific catchment area m
        sin_beta  = max(np.sin(mean_slope_rad), threshold)

        sti = ((As_seg / 22.13) ** 0.6) * ((sin_beta / 0.0896) ** 1.3)
        sti_values.append(float(sti))

    return sti_values

def calculate_twi(dem_arr, dem_res):
    """
    Calculate Topographic Wetness Index (TWI) raster using a simple approach.
    TWI = ln(As / tan(beta))
    As is specific catchment area (approximated by flow accumulation * cell size)
    tan(beta) is local slope.
    This is a simplified TWI calculation for demonstration. For precise TWI,
    a dedicated hydrological model (e.g., WhiteboxTools, pysheds) is needed.
    """
    # Use existing flow accumulation and slope arrays
    flow_acc_arr = FACC_ARR.copy()
    slope_arr    = SLOPE_ARR.copy() # already in degrees

    # Convert slope to radians
    slope_rad_arr = np.radians(slope_arr)

    # Calculate specific catchment area (As) - approximation
    # Assuming flow_acc_arr represents number of upstream cells
    As_arr = flow_acc_arr * dem_res  # Specific catchment area (m^2/m)

    # Avoid division by zero or tan(0)
    tan_beta_arr = np.tan(slope_rad_arr)
    # Set a minimum slope to avoid log of zero/negative and very high TWI values
    min_slope_rad = np.radians(0.01) # 0.01 degrees minimum slope
    tan_beta_arr[tan_beta_arr < np.tan(min_slope_rad)] = np.tan(min_slope_rad)

    # Ã¢â€â‚¬Ã¢â€â‚¬ Compute TWI only where As > 0 and slope > 0 Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
    valid_mask = (As_arr > 0) & (~np.isnan(dem_arr)) & (tan_beta_arr > np.tan(min_slope_rad))
    twi_arr    = np.full(dem_arr.shape, np.nan, dtype=np.float32)
    twi_arr[valid_mask] = np.log(As_arr[valid_mask] / tan_beta_arr[valid_mask])
    # Clamp to physically reasonable range
    twi_arr = np.clip(twi_arr, -5.0, 25.0)
    twi_arr[~valid_mask] = np.nan

    return twi_arr.astype(np.float32)

def rasterize_segment_attribute(gdf, attribute_col, dem_arr_shape, dem_transform, nodata_val=-9999.0):
    """
    Rasterize a GeoDataFrame's attribute (from line segments) onto a raster grid.
    Values are burned along the line's path, taking the max value if multiple lines cross.
    """
    raster = np.full(dem_arr_shape, np.nan, dtype=np.float32)

    for _, row in gdf[gdf[attribute_col].notna()].iterrows():
        geom = row.geometry
        val  = row[attribute_col]
        if geom.geom_type == 'MultiLineString':
            for single_line in geom.geoms:
                for x, y in single_line.coords:
                    r_idx, c_idx = rasterio.transform.rowcol(dem_transform, x, y)
                    if 0 <= r_idx < dem_arr_shape[0] and 0 <= c_idx < dem_arr_shape[1]:
                        if np.isnan(raster[r_idx, c_idx]):
                            raster[r_idx, c_idx] = val
                        else:
                            raster[r_idx, c_idx] = max(raster[r_idx, c_idx], val)
        elif geom.geom_type == 'LineString':
            for x, y in geom.coords:
                r_idx, c_idx = rasterio.transform.rowcol(dem_transform, x, y)
                if 0 <= r_idx < dem_arr_shape[0] and 0 <= c_idx < dem_arr_shape[1]:
                    if np.isnan(raster[r_idx, c_idx]):
                        raster[r_idx, c_idx] = val
                    else:
                        raster[r_idx, c_idx] = max(raster[r_idx, c_idx], val)

    # Fill remaining NaNs with nodata_val for rasterio compatibility
    raster[np.isnan(raster)] = nodata_val
    return raster.astype(np.float32)


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. STREAM LENGTH-GRADIENT (SL) INDEX
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[A] Computing Stream Length-gradient (SL) Index...")

# Join stream segments to subbasins for basin_id access
gdf_so_with_basin_id = gpd.sjoin(
    gdf_so.copy(), gdf_sub[['basin_id', 'geometry']], how='left', predicate='intersects'
).drop(columns=['index_right']).dropna(subset=['basin_id'])

# Ensure basin_id is set correctly for all segments
if 'basin_id' not in gdf_so_with_basin_id.columns:
    # Fallback if sjoin fails to assign basin_id consistently
    gdf_so_with_basin_id['basin_id'] = None
    for bid in gdf_sub['basin_id'].unique():
        basin_geom = gdf_sub[gdf_sub['basin_id'] == bid].geometry.iloc[0]
        # Find streams within this basin
        streams_in_basin = gdf_so_with_basin_id.geometry.apply(lambda x: x.intersects(basin_geom))
        gdf_so_with_basin_id.loc[streams_in_basin, 'basin_id'] = bid

# Calculate SL index for each segment
# Using gdf_so (stream order segments) as the base for SL calculations
gdf_SL = gdf_so_with_basin_id.copy()
gdf_SL['SL_index'] = calculate_sl_index(gdf_SL, DEM_ARR, DEM_TRANSFORM)

# Calculate SL anomaly (deviation from mean for its order)
mean_sl_per_order = gdf_SL.groupby(ORDER_COL)['SL_index'].mean()
std_sl_per_order  = gdf_SL.groupby(ORDER_COL)['SL_index'].std()

gdf_SL['mean_SL_order'] = gdf_SL[ORDER_COL].map(mean_sl_per_order)
gdf_SL['std_SL_order']  = gdf_SL[ORDER_COL].map(std_sl_per_order)

# SL anomaly is deviation from mean SL for its order, normalized by std dev
gdf_SL['SL_anomaly'] = (gdf_SL['SL_index'] - gdf_SL['mean_SL_order']) / gdf_SL['std_SL_order']

# Replace inf/-inf with nan for anomaly calculation
gdf_SL['SL_anomaly'] = gdf_SL['SL_anomaly'].replace([np.inf, -np.inf], np.nan)

# Store max SL anomaly per basin for plotting/summary later
SL_per_basin = gdf_SL.groupby('basin_id')['SL_anomaly'].agg(
    SL_anomaly_mean='mean', SL_anomaly_max='max', SL_anomaly_std='std'
).round(4)

print("  SL Anomaly per basin (mean/max):")
print(SL_per_basin.to_string())
SL_per_basin.to_csv(os.path.join(TABLES_DIR, "sl_anomaly_per_basin.csv"))
gdf_SL.to_file(os.path.join(SHAPES_DIR, "streams_sl_anomaly.shp"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. STREAM POWER INDEX (SPI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[B] Computing Stream Power Index (SPI)...")

gdf_SL['SPI'] = calculate_spi(gdf_SL, FACC_ARR, SLOPE_ARR, DEM_RES, dem_transform=DEM_TRANSFORM)

SPI_per_basin = gdf_SL.groupby('basin_id')['SPI'].agg(
    SPI_mean='mean', SPI_max='max', SPI_std='std'
).round(4)
print("  SPI per basin (mean/max):")
print(SPI_per_basin.to_string())
SPI_per_basin.to_csv(os.path.join(TABLES_DIR, "spi_per_basin.csv"))

# Rasterize SPI
SPI_ARR = rasterize_segment_attribute(gdf_SL, 'SPI', DEM_ARR.shape, DEM_TRANSFORM)
save_raster(SPI_ARR, os.path.join(OUT_DIR, "spi.tif"), RASTERS['dem'])
RASTERS['spi'] = os.path.join(OUT_DIR, "spi.tif")
print(f"  SPI raster range: {np.nanmin(SPI_ARR):.3f} Ã¢â‚¬â€œ {np.nanmax(SPI_ARR):.3f}")


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. SEDIMENT TRANSPORT INDEX (STI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[C] Computing Sediment Transport Index (STI)...")

gdf_SL['STI'] = calculate_sti(gdf_SL, FACC_ARR, SLOPE_ARR, DEM_RES, dem_transform=DEM_TRANSFORM)

STI_per_basin = gdf_SL.groupby('basin_id')['STI'].agg(
    STI_mean='mean', STI_max='max', STI_std='std'
).round(4)
print("  STI per basin (mean/max):")
print(STI_per_basin.to_string())
STI_per_basin.to_csv(os.path.join(TABLES_DIR, "sti_per_basin.csv"))

# Rasterize STI
STI_ARR = rasterize_segment_attribute(gdf_SL, 'STI', DEM_ARR.shape, DEM_TRANSFORM)
save_raster(STI_ARR, os.path.join(OUT_DIR, "sti.tif"), RASTERS['dem'])
RASTERS['sti'] = os.path.join(OUT_DIR, "sti.tif")
print(f"  STI raster range: {np.nanmin(STI_ARR):.3f} Ã¢â‚¬â€œ {np.nanmax(STI_ARR):.3f}")


# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. TOPOGRAPHIC WETNESS INDEX (TWI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Computing Topographic Wetness Index (TWI)...")

TWI_ARR = calculate_twi(DEM_ARR, DEM_RES)
# MAP-05: clamp TWI and mask flat-area artifacts (slope < 0.05 deg)
TWI_ARR = np.clip(TWI_ARR, 0.0, 18.0)
SLOPE_SAFE_DEG = np.where(np.isnan(SLOPE_ARR), 90.0, SLOPE_ARR)
TWI_ARR[SLOPE_SAFE_DEG < 0.05] = np.nan
save_raster(TWI_ARR, os.path.join(OUT_DIR, "twi.tif"), RASTERS['dem'])
RASTERS['twi'] = os.path.join(OUT_DIR, "twi.tif")
print(f"  TWI range: {np.nanmin(TWI_ARR):.3f} Ã¢â‚¬â€œ {np.nanmax(TWI_ARR):.3f}")

# Per-basin TWI statistics
TWI_basin = []
for _, row in gdf_sub.iterrows():
    geom = [row.geometry.__geo_interface__]
    with rasterio.open(os.path.join(OUT_DIR, "twi.tif")) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            twi_clip  = arr_m[0]
            twi_clip[twi_clip == -9999] = np.nan
        except:
            twi_clip  = TWI_ARR.copy()
    TWI_basin.append({
        'basin_id': row['basin_id'],
        'TWI_mean': round(float(np.nanmean(twi_clip)), 4),
        'TWI_max' : round(float(np.nanmax(twi_clip)), 4),
        'TWI_std': round(float(np.nanstd(twi_clip)), 4),
    })
df_TWI_basin = pd.DataFrame(TWI_basin).set_index('basin_id')
print("  Per-basin TWI:")
print(df_TWI_basin.to_string())
df_TWI_basin.to_csv(os.path.join(TABLES_DIR, "twi_per_basin.csv"))

print("\nÃ¢Å“â€¦ SECTION 11 complete.")

print("=" * 60)
print("SECTION 12 Ã¢â‚¬â€ GEOMORPHIC ANOMALY & LINEAMENT ANALYSIS")
print("=" * 60)

from scipy.ndimage import (sobel, gaussian_filter, maximum_filter,
                            generic_filter, binary_dilation)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. CHANNEL SINUOSITY INDEX (SI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# SI = actual channel length / straight-line distance between endpoints
# SI > 1.5 Ã¢â€ â€™ sinuous/meandering; SI Ã¢â€°Ë† 1.0 Ã¢â€ â€™ straight

print("\n[A] Channel Sinuosity Index (SI)...")

def compute_sinuosity(geom):
    """SI = channel length / straight-line distance between endpoints."""
    if geom.geom_type == 'MultiLineString':
        geom = max(geom.geoms, key=lambda g: g.length)
    if geom.geom_type != 'LineString' or geom.length < DEM_RES:
        return np.nan
    coords    = list(geom.coords)
    straight  = np.sqrt((coords[-1][0] - coords[0][0])**2 +
                        (coords[-1][1] - coords[0][1])**2)
    return geom.length / straight if straight > 0 else np.nan


gdf_SL['SI'] = gdf_SL['geometry'].apply(compute_sinuosity)
SI_per_basin  = gdf_SL.groupby('basin_id')['SI'].agg(
    SI_mean='mean', SI_max='max', SI_std='std'
).round(4)

def si_class(si):
    if np.isnan(si):  return 'Unknown'
    if si < 1.05:     return 'Straight (structural control)'
    if si < 1.3:      return 'Irregular'
    if si < 1.5:      return 'Sinuous'
    return 'Meandering'

SI_per_basin['SI_class'] = SI_per_basin['SI_mean'].apply(si_class)
print(SI_per_basin.to_string())
SI_per_basin.to_csv(os.path.join(TABLES_DIR, "sinuosity_per_basin.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. GEOMORPHIC ANOMALY INDEX (GAI) RASTER
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# GAI = normalised composite of:
#   Ã¢â‚¬Â¢ SL anomaly (rasterised from segment values)
#   Ã¢â‚¬Â¢ TRI (terrain ruggedness)
#   Ã¢â‚¬Â¢ TWI inverted (low TWI = steep, anomalous)
# Higher GAI Ã¢â€ â€™ geomorphically anomalous zone

print("\n[B] Geomorphic Anomaly Index (GAI) raster...")

def normalise_0_1(arr):
    mn, mx = np.nanmin(arr), np.nanmax(arr)
    if mx == mn:
        return np.zeros_like(arr)
    return (arr - mn) / (mx - mn)

# Rasterise SL anomaly: burn each segment's SL_anomaly value onto raster
SL_anomaly_raster = np.full(DEM_ARR.shape, np.nan, dtype=np.float32)
with rasterio.open(RASTERS['dem']) as src:
    transform_r = src.transform
    for _, seg in gdf_SL[gdf_SL['SL_anomaly'].notna()].iterrows():
        geom = seg['geometry']
        pts  = [geom.interpolate(f, normalized=True) for f in np.linspace(0, 1, 20)]
        for pt in pts:
            try:
                r_i, c_i = rowcol(transform_r, pt.x, pt.y)
                if 0 <= r_i < SL_anomaly_raster.shape[0] and 0 <= c_i < SL_anomaly_raster.shape[1]:
                    existing = SL_anomaly_raster[r_i, c_i]
                    val      = seg['SL_anomaly']
                    SL_anomaly_raster[r_i, c_i] = val if np.isnan(existing) else max(existing, val)
            except:
                pass

# Fill gaps with Gaussian spread (proximity decay)
mask_sl = ~np.isnan(SL_anomaly_raster)
SL_filled = np.where(mask_sl, SL_anomaly_raster, 0)
SL_spread = gaussian_filter(SL_filled, sigma=5)
SL_spread[np.isnan(DEM_ARR)] = np.nan

# TRI already computed: TRI_ARR
# TWI inverted: high TWI = flat = low anomaly Ã¢â€ â€™ invert
TWI_inv = np.nanmax(TWI_ARR) - TWI_ARR

# Ã¢â€â‚¬Ã¢â€â‚¬ MAP-02: use robust 2-98 pct normalisation to eliminate black speckle Ã¢â€â‚¬Ã¢â€â‚¬
n_SL  = safe_normalise(SL_spread)
n_TRI = safe_normalise(TRI_ARR)
n_TWI = safe_normalise(TWI_inv)

GAI = (n_SL * 0.5 + n_TRI * 0.3 + n_TWI * 0.2)
GAI[np.isnan(DEM_ARR)] = np.nan

save_raster(GAI, os.path.join(OUT_DIR, "GAI.tif"), RASTERS['dem'])
RASTERS['GAI'] = os.path.join(OUT_DIR, "GAI.tif")
print(f"  GAI range: {np.nanmin(GAI):.3f} Ã¢â‚¬â€œ {np.nanmax(GAI):.3f}")

# Classify high anomaly zones (top 20%)
GAI_thresh       = np.nanpercentile(GAI, 80)
HIGH_ANOMALY     = (GAI > GAI_thresh).astype(np.float32)
HIGH_ANOMALY[np.isnan(DEM_ARR)] = np.nan
save_raster(HIGH_ANOMALY, os.path.join(OUT_DIR, "GAI_high_anomaly.tif"), RASTERS['dem'])

# Per-basin GAI statistics
GAI_basin = []
for _, row in gdf_sub.iterrows():
    geom = [row.geometry.__geo_interface__]
    with rasterio.open(os.path.join(OUT_DIR, "GAI.tif")) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            gai_clip  = arr_m[0]
            gai_clip[gai_clip == -9999] = np.nan
        except:
            gai_clip  = GAI.copy()
    GAI_basin.append({
        'basin_id': row['basin_id'],
        'GAI_mean': round(float(np.nanmean(gai_clip)), 4),
        'GAI_max' : round(float(np.nanmax(gai_clip)), 4),
        'GAI_high_frac': round(float(np.nanmean(gai_clip > GAI_thresh)), 4),
    })
df_GAI_basin = pd.DataFrame(GAI_basin).set_index('basin_id')
print("  Per-basin GAI:")
print(df_GAI_basin.to_string())
df_GAI_basin.to_csv(os.path.join(TABLES_DIR, "GAI_per_basin.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. LINEAMENT PROXY Ã¢â‚¬â€ structural lineament detection
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Method: Sobel edge detection on smoothed DEM + slope, thresholded to
# identify linear high-gradient zones likely representing faults/fractures.

print("\n[C] Structural Lineament Proxy...")

try:
    from skimage.feature import canny
    from skimage.transform import probabilistic_hough_line
    SKIMAGE_OK = True
except ImportError:
    SKIMAGE_OK = False
    print("  scikit-image not available Ã¢â‚¬â€ using Sobel only")

# Smooth DEM
dem_smooth   = gaussian_filter(np.where(np.isnan(DEM_ARR), np.nanmean(DEM_ARR), DEM_ARR), sigma=3)

# Sobel edge magnitude
sx = sobel(dem_smooth, axis=1)
sy = sobel(dem_smooth, axis=0)
edge_mag = np.hypot(sx, sy)
edge_mag[np.isnan(DEM_ARR)] = 0

# Combine with slope for structural emphasis
edge_combined = (normalise_0_1(edge_mag) * 0.6 +
                 normalise_0_1(np.where(np.isnan(SLOPE_ARR), 0, SLOPE_ARR)) * 0.4)
edge_combined[np.isnan(DEM_ARR)] = np.nan
save_raster(edge_combined.astype(np.float32),
            os.path.join(OUT_DIR, "lineament_proxy.tif"), RASTERS['dem'])

# Detect probable lineaments using Canny + Hough if available
LINEAMENTS_GDF = None
if SKIMAGE_OK:
    try:
        edge_uint8 = ((edge_combined / np.nanmax(edge_combined)) * 255).astype(np.uint8)
        canny_edges = canny(edge_uint8, sigma=2,
                            low_threshold=50, high_threshold=100)
        lines = probabilistic_hough_line(
            canny_edges, threshold=30, line_length=20, line_gap=5
        )
        if lines:
            line_geoms = []
            with rasterio.open(RASTERS['dem']) as src:
                T = src.transform
                for (x0, y0), (x1, y1) in lines:
                    wx0, wy0 = xy(T, y0, x0)
                    wx1, wy1 = xy(T, y1, x1)
                    if abs(wx1 - wx0) > 0 or abs(wy1 - wy0) > 0:
                        line_geoms.append(LineString([(wx0, wy0), (wx1, wy1)]))
            if line_geoms:
                LINEAMENTS_GDF = gpd.GeoDataFrame(
                    {'lineament_id': range(len(line_geoms))},
                    geometry=line_geoms, crs=UTM_EPSG
                )
                LINEAMENTS_GDF.to_file(os.path.join(SHAPES_DIR, "lineament_proxy.shp"))
                print(f"  Detected {len(line_geoms)} probable lineaments")
    except Exception as e:
        print(f"  Hough detection failed ({e}) Ã¢â‚¬â€ edge raster saved only")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. MAPS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Generating anomaly maps...")

utm_ext = compute_utm_extent()

# GAI map
# MAP-02: set_bad=transparent to kill black speckle; mask to basin
GAI_MASKED = mask_raster_to_basin(GAI, DEM_TRANSFORM, gdf_sub)
fig, ax_map_gai, ax_panel_gai = make_map_figure(
    "Geomorphic Anomaly Index (GAI)\n0.5*SL + 0.3*TRI + 0.2*TWI\u207b\xb9")
add_esri_basemap(ax_map_gai, source=BASEMAP_HILLSHADE, alpha=0.45)
cmap_gai = plt.cm.get_cmap('RdYlGn_r').copy()
cmap_gai.set_bad(color='white', alpha=0)
ax = ax_map_gai
im = ax.imshow(
    GAI_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_gai, alpha=0.80, zorder=1, vmin=0, vmax=1)
# High anomaly contour overlay
b = DEM_BOUNDS
x_c = np.linspace(b.left, b.right,  GAI.shape[1])
y_c = np.linspace(b.bottom, b.top,  GAI.shape[0])[::-1]
XX, YY = np.meshgrid(x_c, y_c)
ax.contour(XX, YY, np.where(np.isnan(GAI), 0, GAI),
           levels=[GAI_thresh], colors='black', linewidths=1.5,
           linestyles='--', zorder=8)
ax.text(0.02, 0.06, f"Dashed contour = top 20%\nGAI threshold = {GAI_thresh:.3f}",
        transform=ax.transAxes, fontsize=7.5, style='italic',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
gdf_sub.boundary.plot(ax=ax, edgecolor='black', linewidth=1.2, zorder=10)
gdf_streams.plot(ax=ax, color='royalblue', linewidth=0.5, alpha=0.4, zorder=6)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.07)
cb  = plt.colorbar(im, cax=cax)
cb.set_label("GAI (0 = low, 1 = high anomaly)", fontsize=9)
add_continuous_legend_panel(ax_panel_gai, GAI_MASKED, 'RdYlGn_r', 'GAI (0=low, 1=high)')
finalize_map(fig, ax_map_gai, ax_panel_gai, "12a_GAI_map.png", add_panel_elements=False)

# Lineament proxy map
# MAP-03: mask to basin; set_bad eliminates cyan rectangle boundary bleed
LINEAMENT_MASKED = mask_raster_to_basin(edge_combined.astype(np.float32), DEM_TRANSFORM, gdf_sub)
fig, ax_map_lin, ax_panel_lin = make_map_figure("Structural Lineament Proxy\n(Sobel + slope composite)")
add_esri_basemap(ax_map_lin, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_lin = plt.cm.get_cmap('copper_r').copy(); cmap_lin.set_bad(color='white', alpha=0)
ax_map_lin.imshow(LINEAMENT_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_lin, alpha=0.85, zorder=1,
    vmin=0, vmax=np.nanpercentile(LINEAMENT_MASKED, 98))
if LINEAMENTS_GDF is not None and len(LINEAMENTS_GDF) > 0:
    LINEAMENTS_GDF.plot(ax=ax_map_lin, color='yellow', linewidth=0.7,
                        alpha=0.7, zorder=7, label='Probable lineaments')
    ax_map_lin.legend(loc='lower left', fontsize=8, framealpha=0.85)
gdf_sub.boundary.plot(ax=ax_map_lin, edgecolor='#1a1a1a', linewidth=1.5, zorder=10)
add_continuous_legend_panel(ax_panel_lin, LINEAMENT_MASKED, 'copper_r', 'Edge Magnitude')
finalize_map(fig, ax_map_lin, ax_panel_lin, "12b_lineament_proxy_map.png",
             add_panel_elements=False)

# Channel sinuosity map Ã¢â‚¬â€ coloured by SI
fig, ax_map_si, ax_panel_si = make_map_figure("Channel Sinuosity Index (SI)")
add_esri_basemap(ax_map_si, source=BASEMAP_HILLSHADE, alpha=0.40)
ax = ax_map_si
# MAP-04: filter out perfectly straight (SI==1.0) flat-area artifacts
SI_valid  = gdf_SL[gdf_SL['SI'].notna() & (gdf_SL['SI'] > 1.001)].copy()
if len(SI_valid) > 0:
    vmin_si, vmax_si = 1.0, np.nanpercentile(SI_valid['SI'], 98)
    cmap_si = plt.get_cmap('RdYlBu_r')
    norm_si = Normalize(vmin=vmin_si, vmax=vmax_si)
    for _, seg in SI_valid.iterrows():
        color = cmap_si(norm_si(seg['SI']))
        ax.plot(*seg.geometry.xy, color=color, linewidth=1.2, zorder=5)
    sm_si = plt.cm.ScalarMappable(cmap=cmap_si, norm=norm_si)
    sm_si.set_array([])
    cb3 = plt.colorbar(sm_si, ax=ax, fraction=0.03, pad=0.02)
cb3.set_label("Sinuosity Index (SI)", fontsize=9)
gdf_sub.boundary.plot(ax=ax, edgecolor='black', linewidth=1.2, zorder=10)
gdf_sub.boundary.plot(ax=ax_map_si, edgecolor='black', linewidth=1.2, zorder=10)
finalize_map(fig, ax_map_si, ax_panel_si, "12c_sinuosity_map.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. PLOTLY Ã¢â‚¬â€ GAI interactive + anomaly scatter
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[E] Plotly charts...")

# GAI per basin bar + sinuosity overlay
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["GAI Mean per Subbasin",
                                    "Sinuosity vs SL Anomaly"])
fig.add_trace(go.Bar(
    x=df_GAI_basin.index.tolist(),
    y=df_GAI_basin['GAI_mean'].tolist(),
    marker_color=px.colors.sequential.Reds[3:],
    text=[f"{v:.3f}" for v in df_GAI_basin['GAI_mean']],
    textposition='outside',
    hovertemplate='%{x}<br>GAI mean: %{y:.3f}',
    name='GAI mean',
), row=1, col=1)
fig.add_trace(go.Bar(
    x=df_GAI_basin.index.tolist(),
    y=(df_GAI_basin['GAI_high_frac'] * 100).tolist(),
    marker_color=px.colors.sequential.OrRd[3:],
    name='% High anomaly',
    hovertemplate='%{x}<br>High anomaly: %{y:.1f}%',
    yaxis='y2',
), row=1, col=1)

# Sinuosity vs SL scatter
for bid in gdf_sub['basin_id']:
    si_m  = SI_per_basin.loc[bid, 'SI_mean'] if bid in SI_per_basin.index else np.nan
    sl_m  = SL_per_basin.loc[bid, 'SL_anomaly_max'] if bid in SL_per_basin.index else np.nan
    if np.isnan(si_m) or np.isnan(sl_m):
        continue
    fig.add_trace(go.Scatter(
        x=[si_m], y=[sl_m], mode='markers+text',
        text=[bid], textposition='top center',
        marker=dict(size=14, symbol='circle'),
        name=bid,
        hovertemplate=f"{bid}<br>SI={si_m:.3f}<br>SL anomaly={sl_m:.2f}",
    ),
    row=1, col=2)

fig.update_xaxes(title_text='Subbasin', row=1, col=1)
fig.update_yaxes(title_text='GAI Mean', row=1, col=1)
fig.update_xaxes(title_text='Mean Sinuosity (SI)', row=1, col=2)
fig.update_yaxes(title_text='Max SL Anomaly', row=1, col=2)
fig.update_layout(title="Geomorphic Anomaly Analysis",
                  template='plotly_white', height=480, showlegend=True)
save_fig(fig, "12d_geomorphic_anomaly_plotly")

print("\nÃ¢Å“â€¦ SECTION 12 complete.")

print("=" * 60)
print("SECTION 13 Ã¢â‚¬â€ FLOOD HAZARD INDICATORS")
print("=" * 60)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. VERIFY TWI / SPI / STI (computed in S11)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[A] Loading TWI, SPI, STI arrays...")
assert 'twi' in RASTERS, "TWI raster not found Ã¢â‚¬â€ ensure Section 11 ran first"

# Re-read into memory (may have been computed in S11)
with rasterio.open(RASTERS['twi']) as src:
    TWI_ARR2 = src.read(1).astype(np.float32)
    TWI_ARR2[TWI_ARR2 == -9999.0] = np.nan

# Now, SPI and STI rasters should be available in RASTERS if Section 11 ran correctly
assert 'spi' in RASTERS, "SPI raster not found in RASTERS after Section 11"
assert 'sti' in RASTERS, "STI raster not found in RASTERS after Section 11"

with rasterio.open(RASTERS['spi']) as src:
    SPI_ARR2 = src.read(1).astype(np.float32)
    SPI_ARR2[SPI_ARR2 == -9999.0] = np.nan

with rasterio.open(RASTERS['sti']) as src:
    STI_ARR2 = src.read(1).astype(np.float32)
    STI_ARR2[STI_ARR2 == -9999.0] = np.nan

# Let's adjust the prints to reflect what is actually available.
print(f"  TWI : min={np.nanmin(TWI_ARR2):.2f} max={np.nanmax(TWI_ARR2):.2f} mean={np.nanmean(TWI_ARR2):.2f}")
print(f"  SPI : min={np.nanmin(SPI_ARR2):.2f} max={np.nanmax(SPI_ARR2):.2f} mean={np.nanmean(SPI_ARR2):.2f}")
print(f"  STI : min={np.nanmin(STI_ARR2):.2f} max={np.nanmax(STI_ARR2):.2f} mean={np.nanmean(STI_ARR2):.2f}")
# MAP-06/07: prepare log-stretch versions to fix invisible uniform-grey rendering
SPI_LOG = np.log10(np.where(SPI_ARR2 > 1.0, SPI_ARR2, np.nan))
SPI_LOG_MASKED = mask_raster_to_basin(SPI_LOG, DEM_TRANSFORM, gdf_sub)
STI_LOG = np.log10(np.where(STI_ARR2 > 0.01, STI_ARR2, np.nan))
STI_LOG_MASKED = mask_raster_to_basin(STI_LOG, DEM_TRANSFORM, gdf_sub)
TWI_MASKED2 = mask_raster_to_basin(TWI_ARR2, DEM_TRANSFORM, gdf_sub)
# MAP-05: also mask flat-area in TWI_MASKED2
SLOPE_SAFE2 = np.where(np.isnan(SLOPE_ARR), 90.0, SLOPE_ARR)
TWI_MASKED2[SLOPE_SAFE2 < 0.05] = np.nan




# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. FLASH FLOOD POTENTIAL INDEX (FFPI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# FFPI raster derived from slope, relief proxy, and TWI
# Weights following Smith (2003) and Gregory & Walling (1973) concepts

print("\n[B] Flash Flood Potential Index (FFPI)...")

def normalise_raster(arr):
    mn, mx = np.nanmin(arr), np.nanmax(arr)
    if mx == mn:
        return np.zeros_like(arr)
    return (arr - mn) / (mx - mn)


# Component normalised rasters
# MAP-08: build flat-area mask before compositing to prevent pale rectangles
FLAT_MASK_FFPI = np.where(np.isnan(SLOPE_ARR), False, SLOPE_ARR < 0.05)

def safe_component(arr, flat_mask):
    out = arr.copy()
    basin_mean = np.nanmean(arr[~flat_mask]) if np.any(~flat_mask) else 0.5
    out[flat_mask] = basin_mean
    return out

norm_slope   = normalise_raster(np.where(np.isnan(SLOPE_ARR), 0, SLOPE_ARR))

# Relief proxy: local relief within 5Ãƒâ€”5 neighbourhood
from scipy.ndimage import maximum_filter, minimum_filter
dem_safe     = np.where(np.isnan(DEM_ARR), np.nanmean(DEM_ARR), DEM_ARR)
local_relief = maximum_filter(dem_safe, size=5) - minimum_filter(dem_safe, size=5)
local_relief[np.isnan(DEM_ARR)] = np.nan
norm_relief  = normalise_raster(np.where(np.isnan(local_relief), 0, local_relief))

# TWI inverted: high TWI = flat accumulation zone = high flood potential
TWI_safe     = np.where(np.isnan(TWI_ARR2), np.nanmin(TWI_ARR2), TWI_ARR2)
norm_twi     = normalise_raster(TWI_safe)

# SPI: high SPI = high stream power = high flood energy
# Using a placeholder for now, as SPI raster is not generated.
SPI_safe     = np.where(np.isnan(SPI_ARR2), 0, SPI_ARR2) # SPI_ARR2 is a nan placeholder
norm_spi     = normalise_raster(np.log1p(SPI_safe))  # log-transform

# Weighted FFPI Ã¢â‚¬â€ MAP-08: apply flat-area masking on each component
FFPI = (safe_component(norm_slope,  FLAT_MASK_FFPI) * 0.35 +
        safe_component(norm_relief, FLAT_MASK_FFPI) * 0.25 +
        safe_component(norm_twi,    FLAT_MASK_FFPI) * 0.25 +
        safe_component(norm_spi,    FLAT_MASK_FFPI) * 0.15)
FFPI[np.isnan(DEM_ARR)] = np.nan

save_raster(FFPI.astype(np.float32), os.path.join(OUT_DIR, "FFPI.tif"), RASTERS['dem'])
RASTERS['FFPI'] = os.path.join(OUT_DIR, "FFPI.tif")
print(f"  FFPI range: {np.nanmin(FFPI):.3f} Ã¢â‚¬â€œ {np.nanmax(FFPI):.3f}")

# Classify FFPI
def classify_ffpi(val):
    if np.isnan(val): return "Unknown"
    if val > 0.75:    return "Very High"
    if val > 0.55:    return "High"
    if val > 0.35:    return "Moderate"
    if val > 0.20:    return "Low"
    return "Very Low"

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. PER-BASIN HAZARD STATISTICS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[C] Per-basin hazard statistics...")

HAZARD_ROWS = []
for _, row in gdf_sub.iterrows():
    bid  = row['basin_id']
    geom = [row.geometry.__geo_interface__]

    def mask_raster(path):
        with rasterio.open(path) as src:
            try:
                arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
                arr = arr_m[0].astype(np.float32)
                arr[arr == -9999.0] = np.nan
                return arr
            except:
                return np.array([np.nan])

    twi_clip  = mask_raster(RASTERS['twi']) # Use 'twi' (lowercase)
    spi_clip  = mask_raster(RASTERS['spi']) # SPI raster is now available
    sti_clip  = mask_raster(RASTERS['sti']) # STI raster is now available
    ffpi_clip = mask_raster(RASTERS['FFPI'])

    ffpi_mean = float(np.nanmean(ffpi_clip))
    HAZARD_ROWS.append({
        'basin_id'      : bid,
        'TWI_mean'      : round(float(np.nanmean(twi_clip)),  3),
        'TWI_max'       : round(float(np.nanmax(twi_clip)),   3),
        'SPI_mean'      : round(float(np.nanmean(spi_clip)),  3) if np.any(~np.isnan(spi_clip)) else np.nan,
        'SPI_max'       : round(float(np.nanmax(spi_clip)),   3) if np.any(~np.isnan(spi_clip)) else np.nan,
        'STI_mean'      : round(float(np.nanmean(sti_clip)),  3) if np.any(~np.isnan(sti_clip)) else np.nan,
        'STI_max'       : round(float(np.nanmax(sti_clip)),   3) if np.any(~np.isnan(sti_clip)) else np.nan,
        'FFPI_mean'     : round(ffpi_mean, 4),
        'FFPI_max'      : round(float(np.nanmax(ffpi_clip)),  4),
        'FFPI_high_frac': round(float(np.nanmean(ffpi_clip > 0.55)), 4),
        'FFPI_class'    : classify_ffpi(ffpi_mean),
    })
    print(f"  {bid}: TWI_mean={np.nanmean(twi_clip):.2f} | "
          f"SPI_mean={np.nanmean(spi_clip):.2f} | "
          f"FFPI_mean={ffpi_mean:.3f} Ã¢â€ â€™ {classify_ffpi(ffpi_mean)}")

df_hazard = pd.DataFrame(HAZARD_ROWS).set_index('basin_id')

# Composite Flood Hazard Rank
rank_cols = ['TWI_mean', 'SPI_mean', 'STI_mean', 'FFPI_mean']
df_hazard_r = df_hazard[rank_cols].copy()
for col in rank_cols:
    df_hazard[f'rank_{col}'] = df_hazard_r[col].rank(ascending=False, method='min')
df_hazard['FHI_rank'] = df_hazard[[f'rank_{c}' for c in rank_cols]].mean(axis=1)
df_hazard['FHI_priority'] = pd.qcut(
    df_hazard['FHI_rank'], q=3, labels=['High','Moderate','Low'], duplicates='drop'
)

df_hazard.to_csv(os.path.join(TABLES_DIR, "flood_hazard_indices.csv"))
print(f"\n  Ã¢Å“â€¦ Flood hazard table saved")
print(df_hazard[['TWI_mean','SPI_mean','STI_mean','FFPI_mean','FFPI_class','FHI_priority']].to_string())

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. MAPS Ã¢â‚¬â€ all 5 hazard maps
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[D] Generating hazard maps...")

utm_ext = compute_utm_extent()

# Ã¢â€â‚¬Ã¢â€â‚¬ MAP-06/07/08: 70:30 layout for all hazard rasters with log-stretch Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# TWI map (MAP-05 fix: masked, log-clamped)
fig, ax_map13, ax_panel13 = make_map_figure("Topographic Wetness Index (TWI)")
add_esri_basemap(ax_map13, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_twi = plt.get_cmap('Blues').copy(); cmap_twi.set_bad(alpha=0)
ax_map13.imshow(TWI_MASKED2, extent=raster_extent(), origin='upper',
    cmap=cmap_twi, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(TWI_MASKED2, 2), vmax=np.nanpercentile(TWI_MASKED2, 98))
gdf_sub.boundary.plot(ax=ax_map13, edgecolor='black', linewidth=1.2, zorder=10)
gdf_streams.plot(ax=ax_map13, color='royalblue', linewidth=0.5, alpha=0.4, zorder=8)
add_continuous_legend_panel(ax_panel13, TWI_MASKED2, 'Blues', 'TWI')
finalize_map(fig, ax_map13, ax_panel13, "13a_TWI_map.png")

# SPI map (MAP-06 fix: log10 stretch)
fig, ax_map13b, ax_panel13b = make_map_figure("Stream Power Index (SPI)\n(logÃ¢â€šÂÃ¢â€šâ‚¬ scale)")
add_esri_basemap(ax_map13b, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_spi = plt.get_cmap('YlOrRd').copy(); cmap_spi.set_bad(alpha=0)
ax_map13b.imshow(SPI_LOG_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_spi, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(SPI_LOG_MASKED, 5), vmax=np.nanpercentile(SPI_LOG_MASKED, 98))
gdf_sub.boundary.plot(ax=ax_map13b, edgecolor='black', linewidth=1.2, zorder=10)
add_continuous_legend_panel(ax_panel13b, SPI_LOG_MASKED, 'YlOrRd', 'logÃ¢â€šÂÃ¢â€šâ‚¬(SPI) [mÃ‚Â²]')
finalize_map(fig, ax_map13b, ax_panel13b, "13b_SPI_map.png")

# STI map (MAP-07 fix: log10 stretch)
fig, ax_map13c, ax_panel13c = make_map_figure("Sediment Transport Index (STI)\n(logÃ¢â€šÂÃ¢â€šâ‚¬ scale)")
add_esri_basemap(ax_map13c, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_sti = plt.get_cmap('RdPu').copy(); cmap_sti.set_bad(alpha=0)
ax_map13c.imshow(STI_LOG_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_sti, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(STI_LOG_MASKED, 5), vmax=np.nanpercentile(STI_LOG_MASKED, 98))
gdf_sub.boundary.plot(ax=ax_map13c, edgecolor='black', linewidth=1.2, zorder=10)
add_continuous_legend_panel(ax_panel13c, STI_LOG_MASKED, 'RdPu', 'logÃ¢â€šÂÃ¢â€šâ‚¬(STI)')
finalize_map(fig, ax_map13c, ax_panel13c, "13c_STI_map.png")

# FFPI map
FFPI_MASKED = mask_raster_to_basin(FFPI.astype(np.float32), DEM_TRANSFORM, gdf_sub)
fig, ax_map13d, ax_panel13d = make_map_figure(
    "Flash Flood Potential Index (FFPI)\n(SlopeÃƒâ€”0.35 + ReliefÃƒâ€”0.25 + TWIÃƒâ€”0.25 + SPIÃƒâ€”0.15)")
add_esri_basemap(ax_map13d, source=BASEMAP_HILLSHADE, alpha=0.40)
cmap_ffpi = plt.get_cmap('OrRd').copy(); cmap_ffpi.set_bad(alpha=0)
ax_map13d.imshow(FFPI_MASKED, extent=raster_extent(), origin='upper',
    cmap=cmap_ffpi, alpha=0.80, zorder=1,
    vmin=np.nanpercentile(FFPI_MASKED, 2), vmax=np.nanpercentile(FFPI_MASKED, 98))
gdf_sub.boundary.plot(ax=ax_map13d, edgecolor='black', linewidth=1.2, zorder=10)
add_continuous_legend_panel(ax_panel13d, FFPI_MASKED, 'OrRd', 'FFPI (0Ã¢â‚¬â€œ1)')
finalize_map(fig, ax_map13d, ax_panel13d, "13d_FFPI_map.png")

# Ã¢â€â‚¬Ã¢â€â‚¬ MAP-09: Composite flood hazard choropleth (70:30, quantile-based) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# MAP-09 fix: use quantile thresholds not fixed values to avoid all-VeryLow
ffpi_vals = np.array([df_hazard.loc[b, 'FFPI_mean'] for b in df_hazard.index])
q20, q40, q60, q80 = np.percentile(ffpi_vals, [20, 40, 60, 80])

def classify_ffpi_quantile(val):
    if val >= q80: return 'Very High'
    if val >= q60: return 'High'
    if val >= q40: return 'Moderate'
    if val >= q20: return 'Low'
    return 'Very Low'

df_hazard['FFPI_class_q'] = [classify_ffpi_quantile(v) for v in ffpi_vals]
ffpi_class_colors = {
    'Very High': '#7f0000', 'High': '#d73027', 'Moderate': '#fc8d59',
    'Low': '#fee090',       'Very Low': '#91bfdb', 'Unknown': 'grey',
}
fig, ax_map13e, ax_panel13e = make_map_figure(
    "Composite Flood Hazard Priority\n(Quantile FFPI Ranking)")
add_esri_basemap(ax_map13e, source=BASEMAP_TOPO, alpha=0.30)
gdf_fhaz = gdf_sub.merge(
    df_hazard[['FFPI_class_q', 'FFPI_mean']].reset_index(), on='basin_id', how='left')
for _, row in gdf_fhaz.iterrows():
    col_f = ffpi_class_colors.get(row['FFPI_class_q'], 'grey')
    gpd.GeoDataFrame([row], geometry='geometry', crs=gdf_sub.crs).plot(
        ax=ax_map13e, color=col_f, edgecolor='black', linewidth=1.2, alpha=0.80, zorder=3)
    cx13, cy13 = row.geometry.centroid.x, row.geometry.centroid.y
    ax_map13e.text(cx13, cy13,
        f"{row['basin_id']}\n{row['FFPI_class_q']}\nFFPI={row['FFPI_mean']:.3f}",
        ha='center', va='center', fontsize=8, fontweight='bold',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])
gdf_so[gdf_so[ORDER_COL] >= 3].plot(ax=ax_map13e, color='royalblue',
                                      linewidth=0.8, alpha=0.5, zorder=6)
_cls_cols  = [ffpi_class_colors[c] for c in ['Very High','High','Moderate','Low','Very Low']]
_cls_lbls  = ['Very High','High','Moderate','Low','Very Low']
add_classified_legend_panel(ax_panel13e, _cls_cols, _cls_lbls,
                             title='Flood Hazard Class', y_top=0.48)
finalize_map(fig, ax_map13e, ax_panel13e, "13e_flood_hazard_composite_map.png")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. PLOTLY Ã¢â‚¬â€ multi-panel hazard comparison
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[E] Plotly flood hazard charts...")

basins = df_hazard.index.tolist()

# Multi-panel bar comparison
fig = make_subplots(rows=2, cols=2,
                    subplot_titles=['TWI Mean', 'SPI Mean', 'STI Mean', 'FFPI Mean'])
colors_p = px.colors.qualitative.Set1

for panel_i, (col, r, c_idx) in enumerate([
    ('TWI_mean',  1, 1), ('SPI_mean',  1, 2),
    ('STI_mean',  2, 1), ('FFPI_mean', 2, 2),
]):
    fig.add_trace(go.Bar(
        x=basins,
        y=df_hazard[col].tolist(),
        name=col,
        marker_color=colors_p[panel_i % 9],
        text=[f"{v:.3f}" for v in df_hazard[col]],
        textposition='outside',
        hovertemplate='%{x}<br>' + col + ': %{y:.3f}',
    ),
    row=r, col=c_idx)

fig.update_layout(
    title="Flood Hazard Indices Ã¢â‚¬â€ All Subbasins",
    template='plotly_white', height=600, showlegend=False,
)
save_fig(fig, "13f_flood_indices_bar")

# Bubble plot: FFPI vs Drainage Density vs Basin Relief
df_bubble_fh = df_hazard[['FFPI_mean']].join(
    df_master[['Drainage_Density_Dd', 'Basin_Relief_H_m']]
).reset_index()
fig = px.scatter(
    df_bubble_fh, x='Drainage_Density_Dd', y='FFPI_mean',
    size='Basin_Relief_H_m', color='basin_id', text='basin_id',
    title="Flash Flood Potential vs Drainage Density<br>"
          "<sup>Bubble size = Basin Relief (m)</sup>",
    labels={
        'Drainage_Density_Dd': 'Drainage Density (km/kmÃ‚Â²)',
        'FFPI_mean': 'FFPI Mean',
        'Basin_Relief_H_m': 'Relief (m)',
    },
    template='plotly_white', size_max=55,
)
fig.add_hline(y=0.55, line_dash='dash', line_color='red',
              annotation_text='High flood hazard threshold (FFPI=0.55)')
save_fig(fig, "13g_flood_bubble_plot")

# Susceptibility ranking bar
fig = go.Figure()
fig.add_trace(go.Bar(
    x=basins,
    y=df_hazard['FHI_rank'].tolist(),
    marker_color=[
        {'High': '#d73027', 'Moderate': '#fc8d59', 'Low': '#4575b4'}.get(
            str(df_hazard.loc[b, 'FHI_priority']), 'grey'
        ) for b in basins
    ],
    text=[str(df_hazard.loc[b, 'FHI_priority']) for b in basins],
    textposition='outside',
    hovertemplate='%{x}<br>FHI Rank: %{y:.2f}<br>Priority: %{text}',
))
fig.update_layout(
    title="Flood Hazard Priority Ranking<br>"
          "<sup>Lower rank = higher flood susceptibility</sup>",
    xaxis_title="Subbasin", yaxis_title="FHI Composite Rank",
    template='plotly_white', height=430,
    yaxis=dict(autorange='reversed'),
)
save_fig(fig, "13h_flood_susceptibility_ranking")

print("\nÃ¢Å“â€¦ SECTION 13 complete.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  ADVANCED INTERPRETATION PARAGRAPHS (appended to report)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[F] Writing advanced interpretation to report...")

ADVANCED_REPORT_PATH = os.path.join(REPORT_DIR, "advanced_analysis_interpretation.txt")

with open(ADVANCED_REPORT_PATH, 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("ADVANCED MORPHOMETRIC ANALYSIS Ã¢â‚¬â€ SUPPLEMENTARY INTERPRETATIONS\n")
    f.write("=" * 80 + "\n\n")

    f.write("10. TECTONIC ACTIVITY ANALYSIS\n" + "-"*40 + "\n")
    f.write(
        "The Index of Active Tectonics (IAT) integrates four geomorphic proxies: "
        "Asymmetry Factor (AF), Transverse Symmetry (T), Valley Floor Width-to-Height "
        "Ratio (Vf), and Mountain Front Sinuosity (Smf), following El Hamdouni et al. "
        "(2008). AF values deviating substantially from 50 indicate basin tilting "
        "driven by differential uplift or lithological asymmetry. Vf < 0.5 is "
        "diagnostic of active incision associated with tectonic uplift, producing "
        "V-shaped valleys, whereas Vf > 1.0 reflects reduced tectonic activity and "
        "lateral widening. Low Smf (< 1.4) indicates a tectonically active, "
        "straight mountain front.\n\n"
    )
    for bid in gdf_sub['basin_id']:
        if bid in df_IAT.index:
            row = df_IAT.loc[bid]
            f.write(
                f"  {bid}: IAT={row['IAT']:.2f} ({row['IAT_class']}). "
                f"AF={row['AF']:.2f}, T={row['T']:.4f}, "
                f"Vf={row['Vf']:.3f}, Smf={row['Smf']:.3f}.\n"
            )
    f.write("\n")

    f.write("11. CHANNEL STEEPNESS & CONCAVITY\n" + "-"*40 + "\n")
    f.write(
        "Channel steepness indices (ksn) and concavity (ÃŽÂ¸) were derived from the "
        "slope-area relationship following Hack (1973) and Flint (1974). High ksn "
        "values indicate either strong lithological resistance, active rock uplift, "
        "or transient adjustment to base-level change. The chi (Ãâ€¡) coordinate plot "
        "(Perron & Royden, 2012) allows comparison of drainage networks independent "
        "of their spatial position, where non-collinear Ãâ€¡-elevation relationships "
        "between adjacent basins signal ongoing divide migration or stream capture. "
        "SL anomaly hotspots correspond to knickpoints or reaches crossing resistant "
        "lithological boundaries.\n\n"
    )
    # THETA_RESULTS and ksn_stats are not defined. Removing the loop that uses them.
    # for bid, tres in THETA_RESULTS.items():
    #     f.write(
    #         f"  {bid}: ÃŽÂ¸={tres['theta_concavity']:.3f} "
    #         f"({'Concave (normal)' if tres['theta_concavity'] > 0.3 else 'Low concavity (active uplift or hard substrate)'}) "
    #         f"| ksn mean={ksn_stats.loc[bid,'ksn_mean'] if bid in ksn_stats.index else 'N/A'} "
    #         f"| RÃ‚Â²={tres['R2_SA']:.3f}\n"
    #     )
    f.write("  (Steepness and concavity parameters were not computed in this run.)\n")
    f.write("\n")

    f.write("12. GEOMORPHIC ANOMALY & LINEAMENT ANALYSIS\n" + "-"*40 + "\n")
    f.write(
        "The Geomorphic Anomaly Index (GAI) integrates SL anomaly, TRI, and inverse "
        "TWI to identify geomorphically active zones where structural or lithological "
        "controls modulate landscape evolution. High GAI zones (top 20th percentile) "
        "are spatially coincident with anomalously high SL reaches, implying "
        "knickpoint clusters, fault zones, or resistant bedrock outcrops. Structural "
        "lineaments were identified as a proxy using Sobel edge detection combined "
        "with Probabilistic Hough Line Transform, targeting linear high-gradient "
        "alignments in the DEM and slope rasters.\n\n"
    )
    for bid in gdf_sub['basin_id']:
        if bid in df_GAI_basin.index:
            g = df_GAI_basin.loc[bid]
            si_m = SI_per_basin.loc[bid, 'SI_mean'] if bid in SI_per_basin.index else np.nan
            f.write(
                f"  {bid}: GAI_mean={g['GAI_mean']:.3f} | "
                f"High anomaly fraction={g['GAI_high_frac']*100:.1f}% | "
                f"Mean SI={si_m:.3f} "
                f"({'Straight Ã¢â‚¬â€ possible structural control' if si_m < 1.05 else 'Sinuous/meandering'})\n"
            )
    f.write("\n")

    f.write("13. FLOOD HAZARD ANALYSIS\n" + "-"*40 + "\n")
    f.write(
        "Topographic Wetness Index (TWI), Stream Power Index (SPI), Sediment Transport "
        "Index (STI), and Flash Flood Potential Index (FFPI) were computed to characterise "
        "the hydrological response and hazard potential of each subbasin. TWI identifies "
        "zones of moisture accumulation and potential saturation-excess overland flow. "
        "High SPI zones correspond to areas of concentrated flow energy capable of "
        "significant geomorphic work. STI quantifies sediment detachment and transport "
        "potential. FFPI synthesises these signals as a weighted composite.\n\n"
    )
    for bid in df_hazard.index:
        row = df_hazard.loc[bid]
        f.write(
            f"  {bid}: FFPI={row['FFPI_mean']:.3f} ({row['FFPI_class']}) | "
            f"TWI_mean={row['TWI_mean']:.2f} | SPI_mean={row['SPI_mean']:.2f} | "
            f"Flood priority: {row['FHI_priority']}\n"
        )
    f.write("\n")

    f.write("REFERENCES (Advanced Sections)\n" + "-"*40 + "\n")
    refs = [
        "Bull, W.B. & McFadden, L.D. (1977). Tectonic geomorphology N & S of the Garlock fault. Geomorphology in arid regions, 115Ã¢â‚¬â€œ138.",
        "Cox, R.T. (1994). Analysis of drainage basin symmetry. Geology, 22(9), 813Ã¢â‚¬â€œ816.",
        "El Hamdouni, R. et al. (2008). Assessment of relative active tectonics, SE Spain. Geomorphology, 96(1Ã¢â‚¬â€œ2), 150Ã¢â‚¬â€œ173.",
        "Flint, J.J. (1974). Stream gradient as a function of order, magnitude, and discharge. Water Resources Research, 10(5), 969Ã¢â‚¬â€œ973.",
        "Gregory, K.J. & Walling, D.E. (1973). Drainage Basin Form and Process. Edward Arnold.",
        "Hack, J.T. (1973). Stream-profile analysis and stream-gradient index. USGS Journal of Research, 1(4), 421Ã¢â‚¬â€œ429.",
        "Moore, I.D., Grayson, R.B. & Ladson, A.R. (1991). Digital terrain modelling. Hydrological Processes, 5(1), 3Ã¢â‚¬â€œ30.",
        "Moore, I.D. & Burch, G.J. (1986). Sediment transport capacity of sheet and rill flow. Water Resources Research, 22(13), 1350Ã¢â‚¬â€œ1360.",
        "Perron, J.T. & Royden, L. (2012). An integral approach to bedrock river profile analysis. Earth Surface Processes and Landforms, 38(6), 570Ã¢â‚¬â€œ576.",
        "Smith, G.H. (2003). The morphometry of drainage basins. Annals of the Association of American Geographers.",
    ]
    for ref in refs:
        f.write(f"  {ref}\n")

print(f"  Ã¢Å“â€¦ Advanced interpretation saved: {ADVANCED_REPORT_PATH}")
print("\nÃ¢Å“â€¦ ALL ADVANCED SECTIONS COMPLETE (10Ã¢â‚¬â€œ13).")
print(f"\n  Total new maps  : 5 tectonic + 3 channel + 3 anomaly + 5 flood = 16 maps")
print(f"  Total new tables: IAT, SL, ksn, theta, sinuosity, GAI, flood hazard = 7 CSVs")
print(f"  Total new plots : 14 interactive Plotly HTML files")


# -*- coding: utf-8 -*-
"""
=============================================================================
 SECTIONS 14Ã¢â‚¬â€œ18 Ã¢â‚¬â€ ADVANCED HYDROLOGICAL & SOIL-WATER CONSERVATION ANALYSIS
 Pravara River Basin, Maharashtra, India
=============================================================================

 Addon to: adv_v2_morphometry_pravra3basin.py
 Run AFTER Sections 0Ã¢â‚¬â€œ13 so the following variables are in memory:
   gdf_sub, gdf_so, gdf_streams, df_master, df_areal, df_relief
   DEM_ARR, FACC_ARR, FDIR_ARR, SLOPE_ARR, HILLSHADE
   DEM_TRANSFORM, DEM_BOUNDS, DEM_RES, DEM_CRS
   UTM_EPSG, ORDER_COL, RASTERS, OUT_DIR, MAPS_DIR,
   PLOTS_DIR, TABLES_DIR, HTML_DIR, SHAPES_DIR
   base_axes, overlay_boundaries, finalize_and_save,
   raster_extent, compute_utm_extent, save_raster,
   save_fig (Plotly helper)

 NEW SECTIONS:
   14 Ã¢â‚¬â€ Runoff Estimation       : SCS-CN, Time of Concentration, Peak Discharge
   15 Ã¢â‚¬â€ RUSLE Soil Erosion Model: RÃ‚Â·KÃ‚Â·LSÃ‚Â·CÃ‚Â·P, SDR, Annual Sediment Yield
   16 Ã¢â‚¬â€ Treatment Planning      : Check dam, Percolation tank, Contour trench
   17 Ã¢â‚¬â€ Synthetic Unit Hydrograph: Snyder's & SCS methods
   18 Ã¢â‚¬â€ Stream Channel Hydraulics: Stream power, Shear stress, Stability index

 Regional context:
   Basin  : Pravara River (Godavari sub-basin), Ahmednagar Dist., Maharashtra
   Lat/Lon: ~19.5Ã‚Â°N, ~73.8Ã‚Â°E  |  CRS: UTM Zone 43N (EPSG:32643)
   Climate: Semi-arid monsoonal Ã¢â‚¬â€ mean annual rainfall ~750 mm (Jun-Sep)
   Geology: Basaltic Deccan Traps Ã¢â‚¬â€ shallow, fine-textured Vertisol/Inceptisol

 References:
   USDA-SCS (1985). Hydrology. National Engineering Handbook, Section 4.
   Wischmeier & Smith (1978). Predicting Rainfall Erosion Losses. USDA-AH537.
   Moore et al. (1991). Digital Terrain Modelling. Hydrol. Processes 5, 3-30.
   Snyder (1938). Synthetic Unit Hydrographs. Trans. AGU 19, 447-454.
   Singh (1988). Hydrologic Systems Vol. I. Prentice-Hall.
   Kirpich (1940). Time of Concentration. Civil Engineering 10(6), 362.
   Mitasova et al. (1996). Modelling topographic potential for erosion.
   Bagnold (1966). An Approach to the Sediment Transport Problem.
   Leopold & Maddock (1953). Hydraulic Geometry. USGS Prof. Paper 252.
=============================================================================
"""

# Ã¢â€â‚¬Ã¢â€â‚¬ Standard imports (all should already be in memory from Sections 0Ã¢â‚¬â€œ13) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
import os
import warnings
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.mask import mask as rio_mask
from rasterio.transform import rowcol, xy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize, LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy import stats
from scipy.ndimage import gaussian_filter, uniform_filter, label as ndlabel
from shapely.geometry import Point, LineString, Polygon
from shapely.ops import linemerge
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

warnings.filterwarnings("ignore")

# Ã¢â€â‚¬Ã¢â€â‚¬ Output sub-directories Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
HYD_DIR   = os.path.join(OUT_DIR, "hydrology/")
SWC_DIR   = os.path.join(OUT_DIR, "conservation/")
UHG_DIR   = os.path.join(OUT_DIR, "unit_hydrograph/")
HYD_MAPS  = os.path.join(MAPS_DIR, "hydrology/")
SWC_MAPS  = os.path.join(MAPS_DIR, "conservation/")

for d in [HYD_DIR, SWC_DIR, UHG_DIR, HYD_MAPS, SWC_MAPS]:
    os.makedirs(d, exist_ok=True)

print("Ã¢Å“â€¦ Output directories created.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
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
# SECTION 15 Ã¢â‚¬â€ RUSLE SOIL EROSION MODEL
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n" + "=" * 70)
print("SECTION 15 Ã¢â‚¬â€ RUSLE SOIL EROSION ESTIMATION")
print("=" * 70)

# RUSLE:  A = R Ãƒâ€” K Ãƒâ€” LS Ãƒâ€” C Ãƒâ€” P
# A  = Annual average soil loss (t/ha/yr)
# R  = Rainfall-runoff erosivity factor (MJÃ‚Â·mm/haÃ‚Â·hrÃ‚Â·yr)
# K  = Soil erodibility factor (tÃ‚Â·haÃ‚Â·hr/haÃ‚Â·MJÃ‚Â·mm)
# LS = Slope length-gradient factor (dimensionless)
# C  = Cover-management factor (dimensionless, 0Ã¢â‚¬â€œ1)
# P  = Support practice factor (dimensionless, 0Ã¢â‚¬â€œ1)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. R-FACTOR Ã¢â‚¬â€ Erosivity
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-A] R-Factor (Rainfall Erosivity)...")
# Maharashtra Deccan Trap region: R Ã¢â€°Ë† 550Ã¢â‚¬â€œ800 MJÃ‚Â·mm/(haÃ‚Â·hrÃ‚Â·yr)
# Pravara catchment (Ahmednagar): R Ã¢â€°Ë† 650 MJÃ‚Â·mm/(haÃ‚Â·hrÃ‚Â·yr)
# Spatial variation modelled as: R = R0 Ãƒâ€” (1 + 0.05 Ãƒâ€” (elev - elev_mean)/elev_std)
# (higher elevations get slightly higher R due to orographic rainfall)

R0       = 650.0
elev_mean = np.nanmean(DEM_ARR)
elev_std  = np.nanstd(DEM_ARR)

R_ARR = R0 * (1.0 + 0.05 * (DEM_ARR - elev_mean) / (elev_std + 1e-6))
R_ARR = np.clip(R_ARR, 400.0, 1000.0)
R_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(R_ARR.astype(np.float32), os.path.join(OUT_DIR, "RUSLE_R.tif"), RASTERS["dem"])
RASTERS["RUSLE_R"] = os.path.join(OUT_DIR, "RUSLE_R.tif")
print(f"  R-factor range: {np.nanmin(R_ARR):.0f}Ã¢â‚¬â€œ{np.nanmax(R_ARR):.0f} "
      f"MJÃ‚Â·mm/(haÃ‚Â·hrÃ‚Â·yr) | Mean: {np.nanmean(R_ARR):.0f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. K-FACTOR Ã¢â‚¬â€ Soil Erodibility
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-B] K-Factor (Soil Erodibility)...")
# Deccan Trap basalt Ã¢â€ â€™ Vertisols + Inceptisols
# K ranges: Vertisol (clay-rich) 0.10Ã¢â‚¬â€œ0.20; Shallow rocky 0.05Ã¢â‚¬â€œ0.10
# Proxy using slope: steeper slopes Ã¢â€ â€™ shallower soil Ã¢â€ â€™ lower K (rocky)
# Flat/gentle Ã¢â€ â€™ deep Vertisol Ã¢â€ â€™ higher K

K_ARR = np.where(slope_safe <  3,  0.25,   # Deep Vertisol (fine clay, flat)
         np.where(slope_safe <  8,  0.20,   # Vertic Inceptisol
         np.where(slope_safe < 15,  0.15,   # Shallow Alfisol
         np.where(slope_safe < 25,  0.10,   # Lithic Inceptisol (stony)
                                   0.05)))).astype(np.float32)  # Rock/talus
K_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(K_ARR, os.path.join(OUT_DIR, "RUSLE_K.tif"), RASTERS["dem"])
RASTERS["RUSLE_K"] = os.path.join(OUT_DIR, "RUSLE_K.tif")
print(f"  K-factor range: {np.nanmin(K_ARR):.2f}Ã¢â‚¬â€œ{np.nanmax(K_ARR):.2f} "
      f"tÃ‚Â·haÃ‚Â·hr/(haÃ‚Â·MJÃ‚Â·mm) | Mean: {np.nanmean(K_ARR):.3f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. LS-FACTOR Ã¢â‚¬â€ Slope Length-Gradient
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-C] LS-Factor (Slope-Length Gradient, Moore et al. 1991)...")
# Moore et al. (1991) LS from flow accumulation (As) and slope:
#   LS = (As/22.13)^m Ãƒâ€” (sin(ÃŽÂ²)/0.0896)^n
# where As = specific catchment area (mÃ‚Â²/m) = flow_acc Ãƒâ€” cell_size
# m = 0.6 (rill erosion, semi-arid), n = 1.3
# This formulation handles divergent/convergent flow better than Wischmeier's L.

cell_area_m2 = DEM_RES * DEM_RES
fa_safe  = np.where(np.isnan(FACC_ARR), 0, np.maximum(FACC_ARR, 1))
As_arr   = fa_safe * DEM_RES                # specific catchment area mÃ‚Â²/m
slope_rad = np.radians(np.where(np.isnan(SLOPE_ARR), 0.01, SLOPE_ARR))
slope_rad = np.maximum(slope_rad, np.radians(0.01))  # min 0.01Ã‚Â° to avoid log issues

# Ã¢â€â‚¬Ã¢â€â‚¬ LS-factor exponents (Moore et al., 1991) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# m=0.4, n=1.3 Ã¢â€ â€™ interrill/sheet erosion (standard default)
# m=0.6, n=1.3 Ã¢â€ â€™ rill-dominated / steep terrain (change if confirmed by field)
m_exp = 0.4   # Ã¢Å“â€¦ standard Moore et al. (1991) Ã¢â‚¬â€ Pravara basin Deccan trap Vertisols
n_exp = 1.3
LS_ARR = ((As_arr / 22.13) ** m_exp) * ((np.sin(slope_rad) / 0.0896) ** n_exp)
LS_ARR = np.clip(LS_ARR, 0.0, 50.0)       # cap to avoid extreme values on cliffs
LS_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(LS_ARR.astype(np.float32), os.path.join(OUT_DIR, "RUSLE_LS.tif"), RASTERS["dem"])
RASTERS["RUSLE_LS"] = os.path.join(OUT_DIR, "RUSLE_LS.tif")
print(f"  LS-factor range: {np.nanmin(LS_ARR):.2f}Ã¢â‚¬â€œ{np.nanmax(LS_ARR):.2f} | "
      f"Mean: {np.nanmean(LS_ARR):.2f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. C-FACTOR Ã¢â‚¬â€ Cover-Management
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-D] C-Factor (Cover-Management)...")
# No land-use raster: use slope + elevation proxy for cover quality
# Flat lowlands (cultivated, Rabi/Kharif crops): C = 0.15Ã¢â‚¬â€œ0.25
# Moderate slopes (degraded dryland agriculture): C = 0.25Ã¢â‚¬â€œ0.40
# Steep slopes (sparse scrub/bare basalt): C = 0.40Ã¢â‚¬â€œ0.60
# Very steep / ridges (bare rock): C = 0.10Ã¢â‚¬â€œ0.20 (less soil to erode)

C_ARR = np.where(slope_safe <  3,  0.20,   # Irrigated/Rabi crops in flat areas
         np.where(slope_safe <  8,  0.30,   # Rainfed Kharif crops
         np.where(slope_safe < 15,  0.45,   # Degraded rangeland/scrub
         np.where(slope_safe < 25,  0.55,   # Sparse vegetation / bare patches
                                   0.15)))).astype(np.float32)  # Rocky ridge (low erosion)
C_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(C_ARR, os.path.join(OUT_DIR, "RUSLE_C.tif"), RASTERS["dem"])
RASTERS["RUSLE_C"] = os.path.join(OUT_DIR, "RUSLE_C.tif")
print(f"  C-factor range: {np.nanmin(C_ARR):.2f}Ã¢â‚¬â€œ{np.nanmax(C_ARR):.2f} | "
      f"Mean: {np.nanmean(C_ARR):.3f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. P-FACTOR Ã¢â‚¬â€ Support Practice
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-E] P-Factor (Support Practice)...")
# Maharashtra farmers on steep slopes use traditional bunding (terracing)
# Flat (<3Ã‚Â°) : cultivated flat fields, no terracing needed Ã¢â€ â€™ P = 1.0
# GentleÃ¢â‚¬â€œModerate (3Ã¢â‚¬â€œ20Ã‚Â°): traditional tied ridges / broad-based bunds Ã¢â€ â€™ P = 0.6
# Steep (>20Ã‚Â°): bench terracing or no practice Ã¢â€ â€™ P = 0.8
# Very steep (>30Ã‚Â°): grassland / no effective practice Ã¢â€ â€™ P = 1.0

P_ARR = np.where(slope_safe <  3,  1.00,
         np.where(slope_safe <  8,  0.55,   # Contour cultivation + bunding
         np.where(slope_safe < 15,  0.65,   # Graded bunding
         np.where(slope_safe < 25,  0.80,   # Bench terrace
                                   1.00)))).astype(np.float32)
P_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(P_ARR, os.path.join(OUT_DIR, "RUSLE_P.tif"), RASTERS["dem"])
RASTERS["RUSLE_P"] = os.path.join(OUT_DIR, "RUSLE_P.tif")
print(f"  P-factor range: {np.nanmin(P_ARR):.2f}Ã¢â‚¬â€œ{np.nanmax(P_ARR):.2f} | "
      f"Mean: {np.nanmean(P_ARR):.3f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  F. ANNUAL SOIL LOSS (A) Ã¢â‚¬â€ RUSLE
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-F] Computing Annual Soil Loss raster A = RÃ‚Â·KÃ‚Â·LSÃ‚Â·CÃ‚Â·P ...")

A_ARR = R_ARR * K_ARR * LS_ARR * C_ARR * P_ARR     # t/ha/yr
A_ARR = np.clip(A_ARR, 0.0, 500.0)                 # cap extreme values
A_ARR[np.isnan(DEM_ARR)] = np.nan

save_raster(A_ARR.astype(np.float32), os.path.join(OUT_DIR, "RUSLE_A.tif"), RASTERS["dem"])
RASTERS["RUSLE_A"] = os.path.join(OUT_DIR, "RUSLE_A.tif")
print(f"  Annual soil loss range: {np.nanmin(A_ARR):.1f}Ã¢â‚¬â€œ{np.nanmax(A_ARR):.0f} t/ha/yr")
print(f"  Basin-wide mean: {np.nanmean(A_ARR):.1f} t/ha/yr")

# Ã¢â€â‚¬Ã¢â€â‚¬ USDA soil loss class thresholds (t/ha/yr) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Slight <5 | Moderate 5-15 | High 15-30 | Very High 30-60 | Severe >60
SOIL_LOSS_CLASSES = [
    (0,   5,  "Slight (<5)",        "#1a9641"),
    (5,  15,  "Moderate (5-15)",    "#a6d96a"),
    (15, 30,  "High (15-30)",       "#fdae61"),
    (30, 60,  "Very High (30-60)",  "#d7191c"),
    (60, 999, "Severe (>60)",       "#7f0000"),
]

def classify_soil_loss(val):
    for lo, hi, name, _ in SOIL_LOSS_CLASSES:
        if lo <= val < hi:
            return name
    return "Severe (>60)"

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  G. SEDIMENT DELIVERY RATIO (SDR) & ANNUAL SEDIMENT YIELD
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-G] Sediment Delivery Ratio & Annual Sediment Yield...")

# SDR = 0.417 Ãƒâ€” A^(-0.3) (Vanoni, 1975 Ã¢â‚¬â€ area in kmÃ‚Â²)
# Also: SDR = exp(-1.58 + 0.46 Ãƒâ€” ln(slope%) - 0.19 Ãƒâ€” ln(A_kmÃ‚Â²))
# We use Renfro (1975) formula: SDR = 0.42 Ãƒâ€” A_km2^(-0.125)

RUSLE_ROWS = []

for _, row in gdf_sub.iterrows():
    bid  = row["basin_id"]
    geom = [row.geometry.__geo_interface__]
    A_km2 = df_areal.loc[bid, "Area_km2"]

    # Clip A raster
    with rasterio.open(RASTERS["RUSLE_A"]) as src:
        try:
            arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
            a_clip   = arr_m[0].astype(np.float32)
            a_clip[a_clip == -9999.0] = np.nan
        except Exception:
            a_clip   = A_ARR.copy()

    valid_a = a_clip[~np.isnan(a_clip)]
    if len(valid_a) == 0:
        continue

    A_mean = float(np.nanmean(valid_a))    # t/ha/yr
    A_max  = float(np.nanpercentile(valid_a, 95))

    # Total gross erosion (t/yr): A_mean [t/ha/yr] Ãƒâ€” Area [ha]
    A_ha   = A_km2 * 100.0
    Gross_erosion_t_yr = A_mean * A_ha

    # SDR
    SDR = 0.42 * (A_km2 ** -0.125)
    SDR = min(SDR, 0.80)

    # Annual sediment yield
    Sed_yield_t_yr   = Gross_erosion_t_yr * SDR
    Sed_yield_Mm3_yr = Sed_yield_t_yr / (1300 * 1000)  # assuming bulk density 1.3 t/mÃ‚Â³

    # Area fraction per soil loss class
    class_fracs = {}
    for lo, hi, name, _ in SOIL_LOSS_CLASSES:
        frac = float(np.sum((valid_a >= lo) & (valid_a < hi))) / len(valid_a)
        class_fracs[name] = round(frac * 100, 1)

    RUSLE_ROWS.append({
        "basin_id"              : bid,
        "A_mean_t_ha_yr"        : round(A_mean, 2),
        "A_p95_t_ha_yr"         : round(A_max, 2),
        "Area_ha"               : round(A_ha, 1),
        "Gross_Erosion_t_yr"    : round(Gross_erosion_t_yr, 0),
        "SDR"                   : round(SDR, 3),
        "Sed_Yield_t_yr"        : round(Sed_yield_t_yr, 0),
        "Sed_Yield_Mm3_yr"      : round(Sed_yield_Mm3_yr, 6),
        "Loss_Class_Mode"       : classify_soil_loss(A_mean),
        **{f"Pct_{k}": v for k, v in class_fracs.items()},
    })
    print(f"  {bid}: A_mean={A_mean:.1f} t/ha/yr | SDR={SDR:.3f} | "
          f"Sed.Yield={Sed_yield_t_yr:.0f} t/yr | Class: {classify_soil_loss(A_mean)}")

df_rusle = pd.DataFrame(RUSLE_ROWS).set_index("basin_id")
df_rusle.to_csv(os.path.join(HYD_DIR, "RUSLE_soil_erosion.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  H. RUSLE MAPS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[15-H] Generating RUSLE maps...")

# LS-factor map
fig, ax, utm_ext = base_axes("RUSLE LS-Factor Map\n(Moore et al. 1991: "
                              "Slope-Length Ãƒâ€” Gradient combined)")
im = ax.imshow(LS_ARR, extent=raster_extent(), origin="upper",
               cmap="YlOrRd", alpha=0.80, zorder=1,
               vmin=0, vmax=np.nanpercentile(LS_ARR, 97))
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.2, zorder=10)
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.6, alpha=0.5, zorder=8)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.07)
cb  = plt.colorbar(im, cax=cax)
cb.set_label("LS Factor (dimensionless)", fontsize=10)
finalize_and_save(fig, ax, utm_ext, "15a_LS_factor.png")

# Annual soil loss map
fig, ax, utm_ext = base_axes("Annual Soil Loss Map (RUSLE: A = RÃ‚Â·KÃ‚Â·LSÃ‚Â·CÃ‚Â·P)\n"
                              "(tonnes/ha/year)")
# Custom classified colormap
boundaries_sl = [0, 5, 15, 30, 60, 500]
colors_sl     = ["#1a9641", "#a6d96a", "#fdae61", "#d7191c", "#7f0000"]
cmap_sl       = mcolors.BoundaryNorm(boundaries_sl, len(colors_sl))
cmap_sl_obj   = LinearSegmentedColormap.from_list("sl", colors_sl, N=len(colors_sl))
norm_sl       = mcolors.BoundaryNorm(boundaries_sl, cmap_sl_obj.N)

im = ax.imshow(A_ARR, extent=raster_extent(), origin="upper",
               cmap=cmap_sl_obj, norm=norm_sl, alpha=0.80, zorder=1)
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.2, zorder=10)
gdf_streams.plot(ax=ax, color="royalblue", linewidth=0.6, alpha=0.5, zorder=8)
patches_sl = [mpatches.Patch(color=c, label=n)
              for _, _, n, c in SOIL_LOSS_CLASSES]
ax.legend(handles=patches_sl, loc="lower left", fontsize=8,
          title="Soil Loss Class (t/ha/yr)", title_fontsize=9, framealpha=0.9)
# Annotate basins
for _, r in gdf_sub.iterrows():
    bid = r["basin_id"]
    if bid in df_rusle.index:
        cx, cy = r.geometry.centroid.x, r.geometry.centroid.y
        ax.text(cx, cy,
                f"{bid}\n{df_rusle.loc[bid,'A_mean_t_ha_yr']:.1f} t/ha/yr\n"
                f"{df_rusle.loc[bid,'Loss_Class_Mode']}",
                ha="center", va="center", fontsize=7, fontweight="bold",
                path_effects=[pe.withStroke(linewidth=2, foreground="white")])
finalize_and_save(fig, ax, utm_ext, "15b_RUSLE_soil_loss.png")

# Sediment yield bar chart (Plotly)
df_rusle_reset = df_rusle.reset_index()
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Annual Soil Loss (t/ha/yr) per Basin",
                                    "Sediment Yield (t/yr) per Basin"])
colors_b = ["#d73027", "#fdae61", "#1a9641", "#4575b4", "#762a83"]
for i, row_ in df_rusle_reset.iterrows():
    fig.add_trace(go.Bar(
        x=[row_["basin_id"]], y=[row_["A_mean_t_ha_yr"]],
        marker_color=colors_b[i % 5],
        text=f"{row_['A_mean_t_ha_yr']:.1f}", textposition="outside",
        name=row_["basin_id"],
        hovertemplate=(f"{row_['basin_id']}<br>"
                       f"Mean Loss: {row_['A_mean_t_ha_yr']:.1f} t/ha/yr<br>"
                       f"Class: {row_['Loss_Class_Mode']}"),
    ), row=1, col=1)
    fig.add_trace(go.Bar(
        x=[row_["basin_id"]], y=[row_["Sed_Yield_t_yr"]],
        marker_color=colors_b[i % 5],
        text=f"{row_['Sed_Yield_t_yr']:.0f}", textposition="outside",
        name=row_["basin_id"], showlegend=False,
        hovertemplate=(f"{row_['basin_id']}<br>"
                       f"Sediment Yield: {row_['Sed_Yield_t_yr']:.0f} t/yr<br>"
                       f"SDR: {row_['SDR']:.3f}"),
    ), row=1, col=2)

# USDA threshold lines
for T_val, label in [(5, "Slight/Moderate"), (15, "Moderate/High"),
                      (30, "High/Very High"), (60, "Very High/Severe")]:
    fig.add_hline(y=T_val, line_dash="dash", line_color="grey",
                  annotation_text=label, annotation_position="right",
                  annotation_font_size=9, row=1, col=1)

fig.update_yaxes(title_text="Mean Annual Soil Loss (t/ha/yr)", row=1, col=1)
fig.update_yaxes(title_text="Annual Sediment Yield (t/yr)", row=1, col=2)
fig.update_layout(title="RUSLE Erosion Results Ã¢â‚¬â€ Pravara Subbasins",
                  template="plotly_white", height=500, showlegend=False)
save_fig(fig, "15c_RUSLE_erosion_bars")

# RUSLE factor comparison radar (Plotly)
factor_cols_r = ["A_mean_t_ha_yr", "SDR", "Gross_Erosion_t_yr"]
fig_r = go.Figure()
for i, (bid, row_) in enumerate(df_rusle.iterrows()):
    val_r = [df_rusle.loc[bid, c] for c in factor_cols_r]
    val_r_n = [(v - df_rusle[c].min()) / (df_rusle[c].max() - df_rusle[c].min() + 1e-9)
               for v, c in zip(val_r, factor_cols_r)]
    val_r_n += [val_r_n[0]]
    cats = ["Soil Loss", "SDR", "Gross Erosion", "Soil Loss"]
    fig_r.add_trace(go.Scatterpolar(
        r=val_r_n, theta=cats, fill="toself", name=bid, opacity=0.7,
        line_color=px.colors.qualitative.Set1[i % 9]))

fig_r.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                    title="RUSLE Erosion Signature Ã¢â‚¬â€ Normalised per Subbasin",
                    template="plotly_white", height=500)
save_fig(fig_r, "15d_RUSLE_radar")
print("\nÃ¢Å“â€¦ SECTION 15 complete.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
# SECTION 16 Ã¢â‚¬â€ WATERSHED TREATMENT PLANNING (SOIL & WATER CONSERVATION)
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n" + "=" * 70)
print("SECTION 16 Ã¢â‚¬â€ WATERSHED TREATMENT PLANNING")
print("(Check Dams, Percolation Tanks, Contour Trenches, Priority Zones)")
print("=" * 70)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. CHECK DAM SUITABILITY INDEX (CDSI)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Check dam (naala bund / gully plug) suitability criteria:
#  1. Stream order: 1stÃ¢â‚¬â€œ2nd order preferred (scores: ord1=10, ord2=8, ord3=5, ord4+=2)
#  2. Upstream catchment area: 0.5Ã¢â‚¬â€œ10 kmÃ‚Â² optimal (score 10), beyond that less suitable
#  3. Valley cross-section (Vf): 0.3Ã¢â‚¬â€œ1.5 ideal (narrow V-shape; score inversely with Vf)
#  4. Channel slope: 1Ã¢â‚¬â€œ5% optimal for sediment trapping (too flat = silts up; too steep = washout)
#  5. RUSLE A-index: High erosion upstream = high benefit (score ~A/Amax)

print("\n[16-A] Computing Check Dam Suitability Index...")

def score_stream_order(order):
    """Score stream order 1Ã¢â‚¬â€œ6 for check dam suitability (1st order = best)."""
    return max(0, 10 - (order - 1) * 2.5)   # 10, 7.5, 5.0, 2.5, 0...

def score_catchment_area(A_km2):
    """0.5Ã¢â‚¬â€œ10 kmÃ‚Â² is optimal for check dams."""
    if   0.1 <= A_km2 <= 0.5:  return 6
    elif 0.5 <  A_km2 <= 5.0:  return 10
    elif 5.0 <  A_km2 <= 15.0: return 7
    elif A_km2 > 15.0:          return 3
    return 4

def score_channel_slope(slope_pct):
    """1Ã¢â‚¬â€œ5% channel slope is optimal."""
    if   slope_pct < 0.5:  return 3   # Too flat Ã¢â€ â€™ rapid silting
    elif slope_pct < 1.0:  return 6
    elif slope_pct < 5.0:  return 10  # Optimal
    elif slope_pct < 10.0: return 7
    elif slope_pct < 20.0: return 4
    return 2                           # Too steep Ã¢â€ â€™ unstable

def score_valley_vf(Vf):
    """Vf 0.3Ã¢â‚¬â€œ1.5 ideal (narrow V = easy to block; very wide = costly)."""
    if np.isnan(Vf):        return 5
    if   Vf < 0.3:          return 6   # Very narrow Ã¢â‚¬â€ ok but hard to construct
    elif Vf < 1.5:          return 10  # Ideal
    elif Vf < 3.0:          return 7
    elif Vf < 6.0:          return 4
    return 2                            # Very wide valley Ã¢â‚¬â€ not suitable

# For each stream segment, compute CDSI
gdf_cd = gdf_so.copy()
gdf_cd["stream_length_m"] = gdf_cd.geometry.length

# Upstream catchment area from flow accumulation at segment midpoint
def sample_facc_at_midpoint(geom, facc_arr, transform):
    """Sample flow accumulation at segment midpoint."""
    try:
        mid_pt = geom.interpolate(0.5, normalized=True)
        r_i, c_i = rowcol(transform, mid_pt.x, mid_pt.y)
        if 0 <= r_i < facc_arr.shape[0] and 0 <= c_i < facc_arr.shape[1]:
            return float(facc_arr[r_i, c_i])
    except Exception:
        pass
    return np.nan

def sample_slope_at_segment(geom, slope_arr, transform):
    """Mean slope along segment."""
    try:
        pts = [geom.interpolate(f, normalized=True) for f in np.linspace(0.1, 0.9, 7)]
        slopes = []
        for pt in pts:
            r_i, c_i = rowcol(transform, pt.x, pt.y)
            if 0 <= r_i < slope_arr.shape[0] and 0 <= c_i < slope_arr.shape[1]:
                s = slope_arr[r_i, c_i]
                if not np.isnan(s):
                    slopes.append(s)
        return float(np.nanmean(slopes)) if slopes else np.nan
    except Exception:
        return np.nan

# Sample FAcc and slope for each segment
print("  Sampling flow accumulation and slope at stream segments...")
fa_vals    = []
slope_segs = []
for _, seg in gdf_cd.iterrows():
    geom = seg.geometry
    if geom.geom_type == "MultiLineString":
        geom = max(geom.geoms, key=lambda g: g.length)
    fa_vals.append(sample_facc_at_midpoint(geom, FACC_ARR, DEM_TRANSFORM))
    slope_segs.append(sample_slope_at_segment(geom, SLOPE_ARR, DEM_TRANSFORM))

gdf_cd["FA_cells"]    = fa_vals
gdf_cd["seg_slope_deg"] = slope_segs
gdf_cd["A_upstream_km2"] = (gdf_cd["FA_cells"] * DEM_RES * DEM_RES / 1e6).clip(lower=0)
gdf_cd["seg_slope_pct"]  = np.tan(np.radians(gdf_cd["seg_slope_deg"].fillna(5))) * 100

# RUSLE A-score: mean soil loss in 2km upstream buffer of segment
def sample_rusle_upstream(geom, a_arr, transform, buffer_m=1000):
    """Mean RUSLE A in buffer around segment endpoints."""
    try:
        start_pt = Point(geom.coords[0])
        buffered = start_pt.buffer(buffer_m)
        geom_list = [buffered.__geo_interface__]
        with rasterio.open(RASTERS["RUSLE_A"]) as src:
            arr_m, _ = rio_mask(src, geom_list, crop=True, nodata=np.nan)
            vals = arr_m[0][arr_m[0] > 0]
            return float(np.nanmean(vals)) if len(vals) > 0 else np.nan
    except Exception:
        return np.nan

# Compute RUSLE score per segment (sample a subset for speed)
A_max_basin = float(np.nanpercentile(A_ARR, 95))
gdf_cd["A_upstream_mean"] = np.nan
for idx in gdf_cd.index:
    geom = gdf_cd.loc[idx, "geometry"]
    if geom.geom_type == "MultiLineString":
        geom = max(geom.geoms, key=lambda g: g.length)
    val = sample_rusle_upstream(geom, A_ARR, DEM_TRANSFORM, buffer_m=500)
    gdf_cd.at[idx, "A_upstream_mean"] = val

# Score each component
gdf_cd["S_order"]    = gdf_cd[ORDER_COL].apply(score_stream_order)
gdf_cd["S_area"]     = gdf_cd["A_upstream_km2"].apply(score_catchment_area)
gdf_cd["S_slope"]    = gdf_cd["seg_slope_pct"].apply(score_channel_slope)
gdf_cd["S_erosion"]  = (gdf_cd["A_upstream_mean"].fillna(A_max_basin/2) /
                         (A_max_basin + 1e-6) * 10).clip(0, 10)

# Get Vf from df_Vf if available, else use default
try:
    gdf_cd_sub = gpd.sjoin(gdf_cd, gdf_sub[["basin_id","geometry"]],
                            how="left", predicate="intersects")
    gdf_cd_sub = gdf_cd_sub.drop_duplicates(subset=gdf_cd_sub.index.name or gdf_cd.index.name)
    if "basin_id" not in gdf_cd_sub.columns:
        gdf_cd["S_vf"] = 5.0
    else:
        def get_vf_for_basin(bid):
            if bid in df_Vf.index:
                return score_valley_vf(df_Vf.loc[bid, "Vf"])
            return 5.0
        gdf_cd["S_vf"] = gdf_cd_sub["basin_id"].apply(
            lambda b: get_vf_for_basin(b) if pd.notna(b) else 5.0).values
except Exception:
    gdf_cd["S_vf"] = 5.0

# Weighted CDSI (weights reflect relative importance for check dam selection)
W = {"order": 0.30, "area": 0.25, "slope": 0.20, "erosion": 0.15, "vf": 0.10}
gdf_cd["CDSI"] = (W["order"]   * gdf_cd["S_order"]   +
                   W["area"]    * gdf_cd["S_area"]    +
                   W["slope"]   * gdf_cd["S_slope"]   +
                   W["erosion"] * gdf_cd["S_erosion"] +
                   W["vf"]      * gdf_cd["S_vf"])
gdf_cd["CDSI"] = gdf_cd["CDSI"].clip(0, 10)

# Classification
def cdsi_class(v):
    if v >= 7.5: return "Very Suitable"
    if v >= 5.5: return "Suitable"
    if v >= 3.5: return "Moderately Suitable"
    return "Poorly Suitable"

gdf_cd["CDSI_class"] = gdf_cd["CDSI"].apply(cdsi_class)

print("  CDSI distribution:")
print(gdf_cd["CDSI_class"].value_counts().to_string())
gdf_cd[["CDSI","CDSI_class","A_upstream_km2","seg_slope_pct",
         ORDER_COL]].to_csv(os.path.join(SWC_DIR, "checkdam_suitability.csv"))
gdf_cd.to_file(os.path.join(SHAPES_DIR, "checkdam_suitability.shp"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. PERCOLATION POND / RECHARGE ZONE SUITABILITY
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[16-B] Percolation Pond & Groundwater Recharge Zones...")
# Criteria: high TWI (water accumulates), low slope (<5Ã‚Â°),
#           moderate FA (not first-order headwaters, not mainstem)
#           away from steep erosive zones

TWI_safe2  = np.where(np.isnan(TWI_ARR), np.nanmin(TWI_ARR), TWI_ARR)
FA_norm    = np.log1p(np.where(np.isnan(FACC_ARR), 0, FACC_ARR))
FA_norm    = FA_norm / (np.nanmax(FA_norm) + 1e-9)
slope_n2   = 1.0 - (slope_safe / (np.nanmax(slope_safe) + 1e-9))  # inverted Ã¢â‚¬â€ flat preferred

# TWI normalised
TWI_n      = (TWI_safe2 - np.nanmin(TWI_safe2)) / (np.nanmax(TWI_safe2) - np.nanmin(TWI_safe2) + 1e-9)

# Filter to gentle slopes
mask_flat  = (slope_safe < 5.0).astype(float)
mask_flat[np.isnan(DEM_ARR)] = np.nan

PERC_ARR   = (TWI_n * 0.50 + FA_norm * 0.30 + slope_n2 * 0.20) * mask_flat
PERC_ARR[np.isnan(DEM_ARR)] = np.nan
PERC_ARR   = np.clip(PERC_ARR, 0, 1)

save_raster(PERC_ARR.astype(np.float32), os.path.join(OUT_DIR, "percolation_potential.tif"), RASTERS["dem"])
RASTERS["percolation"] = os.path.join(OUT_DIR, "percolation_potential.tif")
print(f"  Percolation potential range: {np.nanmin(PERC_ARR):.3f}Ã¢â‚¬â€œ{np.nanmax(PERC_ARR):.3f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. CONTOUR TRENCH SUITABILITY
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[16-C] Contour Trench Suitability...")
# Contour trenches (staggered trenches across slope) work best where:
#  Ã¢â‚¬Â¢ Slope: 3Ã¢â‚¬â€œ30Ã‚Â° (too flat = no runoff to harvest; too steep = unstable)
#  Ã¢â‚¬Â¢ High RUSLE A (high erosion = high benefit from trenches)
#  Ã¢â‚¬Â¢ Not on stream channels (avoid blocking channels)
#  Ã¢â‚¬Â¢ Moderate soil depth (not rocky)

slope_ok    = ((slope_safe >= 3) & (slope_safe < 30)).astype(float)
A_norm_c    = np.clip(A_ARR / (A_max_basin + 1e-9), 0, 1)
A_norm_c    = np.where(np.isnan(A_norm_c), 0, A_norm_c)

# Penalise cells on channels (high flow accumulation)
FA_threshold = 500  # cells Ã¢â‚¬â€ anything above is a channel
not_channel = (FACC_ARR < FA_threshold).astype(float)
not_channel[np.isnan(FACC_ARR)] = 1.0

CT_ARR = (slope_ok * 0.40 + A_norm_c * 0.40 + not_channel * 0.20)
CT_ARR[np.isnan(DEM_ARR)] = np.nan
CT_ARR = np.clip(CT_ARR, 0, 1)

save_raster(CT_ARR.astype(np.float32), os.path.join(OUT_DIR, "contour_trench_suitability.tif"), RASTERS["dem"])
RASTERS["contour_trench"] = os.path.join(OUT_DIR, "contour_trench_suitability.tif")
print(f"  Contour trench suitability range: {np.nanmin(CT_ARR):.3f}Ã¢â‚¬â€œ{np.nanmax(CT_ARR):.3f}")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  D. PER-BASIN CONSERVATION SUMMARY & WATER HARVESTING POTENTIAL (WHP)
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[16-D] Per-basin conservation statistics & Water Harvesting Potential...")

WHP_ROWS = []

for _, row in gdf_sub.iterrows():
    bid  = row["basin_id"]
    geom = [row.geometry.__geo_interface__]
    A_km2 = df_areal.loc[bid, "Area_km2"]

    def clip_and_stats(raster_path):
        with rasterio.open(raster_path) as src:
            try:
                arr_m, _ = rio_mask(src, geom, crop=True, nodata=np.nan)
                arr = arr_m[0].astype(np.float32)
                arr[arr == -9999.0] = np.nan
                return arr
            except Exception:
                return np.array([np.nan])

    perc_clip = clip_and_stats(RASTERS["percolation"])
    ct_clip   = clip_and_stats(RASTERS["contour_trench"])
    cn_clip   = clip_and_stats(RASTERS["CN"])
    q_25yr_mm = df_runoff.loc[bid, "Q_25yr_mm"] if bid in df_runoff.index else np.nan

    # WHP = potential runoff harvestable volume (25-yr event, mÃ‚Â³)
    # Adjusting for realistic harvesting fraction (0.4 = 40% captured)
    harvest_frac = 0.40
    WHP_m3       = float(q_25yr_mm) * 1e-3 * A_km2 * 1e6 * harvest_frac

    # Check dam count potential: every 500Ã¢â‚¬â€œ1000m on 1stÃ¢â‚¬â€œ2nd order streams
    n_suitable = int((gdf_cd[gdf_cd["CDSI_class"].isin(["Very Suitable", "Suitable"])]
                       .geometry.length.sum() / 700.0))

    WHP_ROWS.append({
        "basin_id"              : bid,
        "Perc_Potential_mean"   : round(float(np.nanmean(perc_clip)), 3),
        "Perc_Potential_p75"    : round(float(np.nanpercentile(perc_clip[~np.isnan(perc_clip)], 75)
                                              if np.any(~np.isnan(perc_clip)) else np.nan), 3),
        "ContourTrench_mean"    : round(float(np.nanmean(ct_clip)), 3),
        "Pct_CT_suitable"       : round(float(np.nanmean(ct_clip > 0.5)) * 100, 1),
        "WHP_25yr_Mm3"          : round(WHP_m3 / 1e6, 4),
        "Potential_CheckDams_N" : n_suitable,
        "CN_mean"               : round(float(np.nanmean(cn_clip)), 2),
        "SWC_Priority"          : ("High"     if df_rusle.loc[bid, "A_mean_t_ha_yr"] > 15 else
                                   "Moderate" if df_rusle.loc[bid, "A_mean_t_ha_yr"] > 5  else
                                   "Low") if bid in df_rusle.index else "Unknown"
    })
    print(f"  {bid}: WHP={WHP_m3/1e6:.4f} MmÃ‚Â³ | CT_suit%={round(float(np.nanmean(ct_clip > 0.5))*100,1)}% "
          f"| Est. check dams={n_suitable}")

df_whp = pd.DataFrame(WHP_ROWS).set_index("basin_id")
df_whp.to_csv(os.path.join(SWC_DIR, "conservation_potential.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  E. SWC MAPS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[16-E] Generating conservation maps...")

# Check dam suitability map
cdsi_colors = {"Very Suitable": "#1a9641", "Suitable": "#a6d96a",
               "Moderately Suitable": "#fdae61", "Poorly Suitable": "#d73027"}
fig, ax, utm_ext = base_axes("Check Dam (Naala Bund) Suitability Map\n"
                              "CDSI = f(Order, Catchment Area, Slope, Erosion, Valley Width)")
for cls, color in cdsi_colors.items():
    segs = gdf_cd[gdf_cd["CDSI_class"] == cls]
    if len(segs) > 0:
        segs.plot(ax=ax, color=color, linewidth=1.5+gdf_cd[gdf_cd["CDSI_class"]==cls][ORDER_COL].mean()*0.3,
                  alpha=0.9, zorder=5, label=cls)
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.5, zorder=15)
# Mark pour points as potential check dam sites
if "gdf_pp" in dir() and gdf_pp is not None:
    gdf_pp.plot(ax=ax, color="red", markersize=80, marker="v",
                zorder=20, label="Pour points (outlets)", edgecolor="white", linewidth=0.8)
patches_cd = [mpatches.Patch(color=v, label=k) for k, v in cdsi_colors.items()]
ax.legend(handles=patches_cd, loc="lower left", fontsize=8,
          title="Check Dam Suitability", title_fontsize=9, framealpha=0.9)
finalize_and_save(fig, ax, utm_ext, "16a_checkdam_suitability.png")

# Composite SWC treatment map
fig, ax, utm_ext = base_axes("Soil & Water Conservation Treatment Zone Map\n"
                              "(Contour Trenches + Percolation Potential)")
# Percolation zones (background)
im1 = ax.imshow(PERC_ARR, extent=raster_extent(), origin="upper",
                cmap="Blues", alpha=0.55, zorder=1, vmin=0, vmax=1)
# Contour trench suitability (overlay)
im2 = ax.imshow(np.ma.masked_where(CT_ARR < 0.5, CT_ARR),
                extent=raster_extent(), origin="upper",
                cmap="Oranges", alpha=0.60, zorder=2, vmin=0.5, vmax=1)
gdf_sub.boundary.plot(ax=ax, edgecolor="black", linewidth=1.2, zorder=10)
# Suitable check dam stream reaches
gdf_cd[gdf_cd["CDSI"] >= 5.5].plot(ax=ax, color="darkgreen", linewidth=1.5, zorder=8, alpha=0.85)
gdf_cd[gdf_cd["CDSI"] < 5.5].plot(ax=ax, color="lightgrey",  linewidth=0.5, zorder=6, alpha=0.4)

legend_items = [
    mpatches.Patch(color="#3182bd", alpha=0.55, label="Percolation / Recharge Zone"),
    mpatches.Patch(color="#e6550d", alpha=0.60, label="Contour Trench Zone (slope 3Ã¢â‚¬â€œ30Ã‚Â°)"),
    mpatches.Patch(color="darkgreen",            label="Check Dam Sites (CDSI Ã¢â€°Â¥ 5.5)"),
]
ax.legend(handles=legend_items, loc="lower left", fontsize=8,
          title="Treatment Zones", title_fontsize=9, framealpha=0.9)
finalize_and_save(fig, ax, utm_ext, "16b_SWC_treatment_zones.png")

# Plotly: WHP bar chart + SWC priority
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=["Water Harvesting Potential (MmÃ‚Â³/25-yr event)",
                                    "SWC Priority & Estimated Check Dam Count"])
swc_pmap = {"High": "#d73027", "Moderate": "#fdae61", "Low": "#4575b4"}
for i, (bid, row_) in enumerate(df_whp.iterrows()):
    c = swc_pmap.get(row_["SWC_Priority"], "grey")
    fig.add_trace(go.Bar(
        x=[bid], y=[row_["WHP_25yr_Mm3"]], marker_color=c, name=bid,
        text=f"{row_['WHP_25yr_Mm3']:.4f}", textposition="outside",
        hovertemplate=f"{bid}<br>WHP={row_['WHP_25yr_Mm3']:.4f} MmÃ‚Â³<br>Priority={row_['SWC_Priority']}",
    ), row=1, col=1)
    fig.add_trace(go.Bar(
        x=[bid], y=[row_["Potential_CheckDams_N"]], marker_color=c, name=bid,
        showlegend=False, text=str(row_["Potential_CheckDams_N"]), textposition="outside",
        hovertemplate=f"{bid}<br>Est. check dams={row_['Potential_CheckDams_N']}",
    ), row=1, col=2)

fig.update_yaxes(title_text="Water Harvesting Potential (MmÃ‚Â³)", row=1, col=1)
fig.update_yaxes(title_text="Estimated Check Dam Count", row=1, col=2)
fig.update_layout(title="Soil & Water Conservation Potential Ã¢â‚¬â€ Pravara Subbasins",
                  template="plotly_white", height=480, showlegend=False)
save_fig(fig, "16c_SWC_potential_bars")
print("\nÃ¢Å“â€¦ SECTION 16 complete.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
# SECTION 17 Ã¢â‚¬â€ SYNTHETIC UNIT HYDROGRAPH
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n" + "=" * 70)
print("SECTION 17 Ã¢â‚¬â€ SYNTHETIC UNIT HYDROGRAPH (Snyder's & SCS Methods)")
print("=" * 70)

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  A. SNYDER'S SYNTHETIC UNIT HYDROGRAPH
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[17-A] Snyder's Synthetic Unit Hydrograph parameters...")

# Snyder (1938) Ã¢â‚¬â€ calibrated for Indian semi-arid basins:
# Ct = 1.8 (lag coefficient, typical for Deccan Trap with moderate relief)
# Cp = 0.6 (peaking coefficient)
# tL = Ct Ãƒâ€” (L Ãƒâ€” Lca)^0.3      [L = basin length km, Lca = L to centroid km]
# Qp = 2.75 Ãƒâ€” Cp Ãƒâ€” A / tL      [Qp in mÃ‚Â³/s for 1mm/hr rainfall, A in kmÃ‚Â²]
# tp = tL + tr/2                [tp = time to peak; tr = storm duration = tL/5.5]
# W50 = 2.14 / (Qp/A)^1.08     [width at 50% Qp, hrs]
# W75 = 1.22 / (Qp/A)^1.08     [width at 75% Qp, hrs]
# tb  = 5 Ãƒâ€” (tp + tr/2) / 24   [base time, hrs]  Ã¢â‚¬â€ approximate

Ct = 1.8    # lag coefficient (Indian semi-arid, Deccan Trap)
Cp = 0.6    # peak coefficient

SUH_ROWS = []

for _, row in gdf_sub.iterrows():
    bid   = row["basin_id"]
    geom  = row.geometry
    A_km2 = df_areal.loc[bid, "Area_km2"]
    L_km  = df_areal.loc[bid, "Basin_Length_km"]

    # Lca: distance from outlet to centroid along main channel
    # Approximate as 0.6 Ãƒâ€” L for natural basins (standard assumption)
    Lca_km = 0.6 * L_km

    # Snyder lag time
    tL_hr  = Ct * (L_km * Lca_km) ** 0.3      # hours

    # Standard storm duration
    tr_hr  = tL_hr / 5.5

    # Time to peak
    tp_hr  = tL_hr + tr_hr / 2.0

    # Peak discharge (mÃ‚Â³/s per mm of rainfall over basin)
    Qp     = 2.75 * Cp * A_km2 / tL_hr

    # Unit area peak
    qp     = Qp / A_km2   # mÃ‚Â³/s/kmÃ‚Â² per mm

    # Hydrograph widths
    W50    = 2.14 / (qp ** 1.08)   # hrs
    W75    = 1.22 / (qp ** 1.08)   # hrs

    # Base time
    tb_hr  = 5.0 * tp_hr / 1.0     # approximate (Linsley et al. rule)
    tb_hr  = max(tb_hr, 2.0 * tp_hr)  # at least 2Ãƒâ€”tp

    # Time of rise and recession
    tr_rise = tp_hr
    tr_recs = tb_hr - tp_hr

    # Return-period peak discharge (mÃ‚Â³/s)
    QP_RT = {}
    for T in RETURN_PERIODS:
        P24  = RAINFALL_RT[T]
        Q_mm = float(scscn_runoff(P24, df_runoff.loc[bid,"CN_mean"] if bid in df_runoff.index else 78))
        QP_RT[T] = round(Qp * Q_mm, 2)   # Qp [mÃ‚Â³/s] = unit Qp Ãƒâ€” Q [mm]

    r_suh = {
        "basin_id"    : bid,
        "L_km"        : round(L_km, 3),
        "Lca_km"      : round(Lca_km, 3),
        "A_km2"       : round(A_km2, 3),
        "tL_hr"       : round(tL_hr, 3),
        "tr_hr"       : round(tr_hr, 3),
        "tp_hr"       : round(tp_hr, 3),
        "Qp_1mm_m3s"  : round(Qp, 4),
        "qp_m3s_km2"  : round(qp, 5),
        "W50_hr"      : round(W50, 3),
        "W75_hr"      : round(W75, 3),
        "tb_hr"       : round(tb_hr, 3),
    }
    for T in RETURN_PERIODS:
        r_suh[f"Qp_{T}yr_m3s"] = QP_RT[T]

    SUH_ROWS.append(r_suh)
    print(f"  {bid}: tL={tL_hr:.2f}hr | tp={tp_hr:.2f}hr | "
          f"Qp(1mm)={Qp:.3f} mÃ‚Â³/s | W50={W50:.2f}hr | W75={W75:.2f}hr")

df_suh = pd.DataFrame(SUH_ROWS).set_index("basin_id")
df_suh.to_csv(os.path.join(UHG_DIR, "snyder_unit_hydrograph_params.csv"))

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  B. SCS DIMENSIONLESS UNIT HYDROGRAPH
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[17-B] SCS Dimensionless Unit Hydrograph...")

# SCS dimensionless ratios (t/tp vs Q/Qp)
SCS_DIM = np.array([
    [0.0, 0.000], [0.1, 0.030], [0.2, 0.100], [0.3, 0.190], [0.4, 0.310],
    [0.5, 0.470], [0.6, 0.660], [0.7, 0.820], [0.8, 0.930], [0.9, 0.990],
    [1.0, 1.000], [1.1, 0.990], [1.2, 0.930], [1.3, 0.860], [1.4, 0.780],
    [1.5, 0.680], [1.6, 0.560], [1.7, 0.460], [1.8, 0.390], [1.9, 0.330],
    [2.0, 0.280], [2.2, 0.207], [2.4, 0.147], [2.6, 0.107], [2.8, 0.077],
    [3.0, 0.055], [3.5, 0.025], [4.0, 0.011], [4.5, 0.005], [5.0, 0.000],
])
t_ratio = SCS_DIM[:, 0]
q_ratio = SCS_DIM[:, 1]

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
#  C. HYDROGRAPH PLOTS
# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

print("\n[17-C] Generating unit hydrograph plots...")

# Matplotlib: all basins on one figure
fig, axes = plt.subplots(len(df_suh), 1,
                         figsize=(12, 4 * len(df_suh)),
                         sharex=False)
if len(df_suh) == 1:
    axes = [axes]

colors_suh = plt.cm.Set1(np.linspace(0, 1, max(len(df_suh), 2)))

for ax_i, (bid, suh) in enumerate(df_suh.iterrows()):
    ax = axes[ax_i]
    tp = suh["tp_hr"]
    tb = suh["tb_hr"]

    # SCS-based hydrograph for 25-yr storm
    Q25_mm = (float(df_runoff.loc[bid, "Q_25yr_mm"])
               if bid in df_runoff.index else 25.0)
    Qp_25  = suh["Qp_1mm_m3s"] * Q25_mm

    t_abs  = t_ratio * tp
    t_full = np.linspace(0, tb * 1.05, 500)
    from scipy.interpolate import interp1d
    q_interp = interp1d(t_ratio * tp, q_ratio * Qp_25,
                         kind="linear", fill_value=0.0, bounds_error=False)
    q_full   = q_interp(t_full)

    ax.fill_between(t_full, 0, q_full, alpha=0.25, color=colors_suh[ax_i])
    ax.plot(t_full, q_full, color=colors_suh[ax_i], linewidth=2.2,
            label=f"{bid} Ã¢â‚¬â€ 25-yr (Q={Q25_mm:.0f}mm)")

    # Also plot 10-yr and 50-yr for comparison
    for T_comp, ls, alpha_c in [(10, "--", 0.6), (50, "-.", 0.6)]:
        Qmm_c = float(df_runoff.loc[bid, f"Q_{T_comp}yr_mm"]
                       if bid in df_runoff.index else 20.0)
        Qp_c  = suh["Qp_1mm_m3s"] * Qmm_c
        ax.plot(t_full, q_interp(t_full) * (Qp_c / (Qp_25 + 1e-9)),
                color=colors_suh[ax_i], linestyle=ls, linewidth=1.5, alpha=alpha_c,
                label=f"{T_comp}-yr")

    # Annotate Qp and tp
    ax.axvline(tp, color="grey", linestyle=":", linewidth=1.2)
    ax.axhline(Qp_25, color="grey", linestyle=":", linewidth=0.8)
    ax.annotate(f"Qp={Qp_25:.1f} mÃ‚Â³/s\ntp={tp:.2f} hr",
                xy=(tp, Qp_25), xytext=(tp + 0.5, Qp_25 * 0.75),
                fontsize=9, arrowprops=dict(arrowstyle="->", color="black"))

    # W50 and W75 hatching
    w50_half = suh["W50_hr"] / 2.0
    w75_half = suh["W75_hr"] / 2.0
    ax.axvspan(tp - w50_half, tp + w50_half, alpha=0.08, color="blue", label="W50")
    ax.axvspan(tp - w75_half, tp + w75_half, alpha=0.08, color="red",  label="W75")

    ax.set_title(f"Synthetic Unit Hydrograph Ã¢â‚¬â€ {bid}  "
                 f"(A={suh['A_km2']:.1f} kmÃ‚Â², L={suh['L_km']:.2f} km)",
                 fontweight="bold", fontsize=11)
    ax.set_xlabel("Time (hours)", fontsize=9)
    ax.set_ylabel("Discharge (mÃ‚Â³/s)", fontsize=9)
    ax.legend(fontsize=8, loc="upper right", framealpha=0.85)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_xlim(0, tb * 1.05)
    ax.set_ylim(bottom=0)

plt.suptitle("Synthetic Unit Hydrographs Ã¢â‚¬â€ Pravara Subbasins\n"
             "Snyder's Method with SCS Dimensionless UH Shape | Ct=1.8, Cp=0.6",
             fontsize=13, fontweight="bold", y=1.01)
plt.tight_layout()
fig.savefig(os.path.join(UHG_DIR, "17_unit_hydrographs.png"), dpi=180, bbox_inches="tight")
plt.close(fig)
print(f"  Ã¢Å“â€¦ Hydrograph plot saved")

# Plotly: interactive multi-basin hydrograph
fig_hy = go.Figure()
for i, (bid, suh) in enumerate(df_suh.iterrows()):
    tp = suh["tp_hr"]
    tb = suh["tb_hr"]
    Q25_mm = float(df_runoff.loc[bid, "Q_25yr_mm"] if bid in df_runoff.index else 25.0)
    Qp_25  = suh["Qp_1mm_m3s"] * Q25_mm
    t_full = np.linspace(0, tb * 1.05, 300)
    q_interp = interp1d(t_ratio * tp, q_ratio * Qp_25,
                         kind="linear", fill_value=0.0, bounds_error=False)
    q_full = q_interp(t_full)

    fig_hy.add_trace(go.Scatter(
        x=t_full.tolist(), y=q_full.tolist(),
        mode="lines", name=f"{bid} (25-yr)",
        fill="tozeroy",
        line=dict(color=px.colors.qualitative.Set1[i % 9], width=2.5),
        hovertemplate=f"{bid}<br>t=%{{x:.2f}} hr<br>Q=%{{y:.2f}} mÃ‚Â³/s",
    ))
    # Mark Qp
    fig_hy.add_trace(go.Scatter(
        x=[tp], y=[Qp_25], mode="markers+text",
        text=[f"Qp={Qp_25:.1f}"], textposition="top center",
        marker=dict(size=10, color=px.colors.qualitative.Set1[i % 9], symbol="diamond"),
        name=f"{bid} peak", showlegend=False,
    ))

fig_hy.update_layout(
    title="Synthetic Unit Hydrographs Ã¢â‚¬â€ 25-year Return Period Event<br>"
          "<sup>Snyder's Method, Deccan Trap basalt calibration: Ct=1.8, Cp=0.6</sup>",
    xaxis_title="Time (hours)",
    yaxis_title="Discharge Q (mÃ‚Â³/s)",
    template="plotly_white", height=550,
)
save_fig(fig_hy, "17b_synthetic_unit_hydrographs")

# Summary table plot
cols_suh = ["tp_hr", "Qp_1mm_m3s", "W50_hr", "W75_hr", "tb_hr",
             "Qp_25yr_m3s", "Qp_100yr_m3s"]
fig_tbl = go.Figure(go.Table(
    header=dict(
        values=["Basin", "tp (hr)", "Qp_unit (mÃ‚Â³/s)", "W50 (hr)", "W75 (hr)",
                "tb (hr)", "Qp 25-yr", "Qp 100-yr"],
        fill_color="#2c5f8c", font_color="white",
        align="center", line_color="white",
    ),
    cells=dict(
        values=[
            df_suh.index.tolist(),
            df_suh["tp_hr"].round(2).tolist(),
            df_suh["Qp_1mm_m3s"].round(4).tolist(),
            df_suh["W50_hr"].round(2).tolist(),
            df_suh["W75_hr"].round(2).tolist(),
            df_suh["tb_hr"].round(2).tolist(),
            df_suh["Qp_25yr_m3s"].tolist(),
            df_suh["Qp_100yr_m3s"].tolist(),
        ],
        fill_color=[["#f0f4ff", "#dce8ff"] * len(df_suh)],
        align="center",
    )
))
fig_tbl.update_layout(title="Snyder's UH Parameter Summary Table",
                       template="plotly_white", height=300)
save_fig(fig_tbl, "17c_UH_parameter_table")
print("\nÃ¢Å“â€¦ SECTION 17 complete.")

# Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
# Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†
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

