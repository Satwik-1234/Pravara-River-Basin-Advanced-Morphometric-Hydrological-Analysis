#!/usr/bin/env python3
"""
Fetch multi-station daily historical rainfall from Open-Meteo Archive (2000-2023)
for Pravara River Basin stations:
 - Station 1 (SB1): Bhandardara / Western Ghats Crest (19.5398°N, 73.7129°E)
 - Station 2 (SB2): Akole North / Upper Tributary (19.5936°N, 73.7551°E)
 - Station 3 (SB3): Pravara East / Valley Plain (19.5691°N, 73.8291°E)
"""

import os
import json
import urllib.request
from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "data" / "rainfall"
OUT_DIR.mkdir(parents=True, exist_ok=True)

stations = [
    {"basin_id": "SB1", "name": "Bhandardara_West", "lat": 19.5398, "lon": 73.7129},
    {"basin_id": "SB2", "name": "Akole_North", "lat": 19.5936, "lon": 73.7551},
    {"basin_id": "SB3", "name": "Pravara_East", "lat": 19.5691, "lon": 73.8291}
]

def fetch_station(st):
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={st['lat']}&longitude={st['lon']}&"
        f"start_date=2000-01-01&end_date=2023-12-31&"
        f"daily=precipitation_sum&timezone=Asia%2FKolkata"
    )
    print(f"Fetching Open-Meteo rainfall for {st['name']} ({st['lat']}, {st['lon']})...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    daily_p = data["daily"]["precipitation_sum"]
    dates = data["daily"]["time"]
    return [{"basin_id": st["basin_id"], "station": st["name"], "date": d, "precip_mm": p if p is not None else 0.0}
            for d, p in zip(dates, daily_p)]

def main():
    all_recs = []
    for st in stations:
        try:
            recs = fetch_station(st)
            all_recs.extend(recs)
        except Exception as e:
            print(f"Error fetching {st['name']}: {e}")

    df = pd.DataFrame(all_recs)
    csv_path = OUT_DIR / "pravara_openmeteo_stations_daily.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved {len(df)} daily precipitation records to {csv_path.name}")

    # Process Annual Maximum 24-hr series & Gumbel Distribution
    df["year"] = pd.to_datetime(df["date"]).dt.year
    ann_sum = df.groupby(["basin_id", "station", "year"])["precip_mm"].sum().reset_index()
    ann_max24 = df.groupby(["basin_id", "station", "year"])["precip_mm"].max().reset_index()

    ann_sum.to_csv(OUT_DIR / "annual_precipitation_totals.csv", index=False)
    ann_max24.to_csv(OUT_DIR / "annual_maximum_24hr_rainfall.csv", index=False)

    # Gumbel parameters per subbasin
    ret_periods = [2, 5, 10, 25, 50, 100]
    gumbel_rows = []
    for st in stations:
        bid = st["basin_id"]
        s_data = ann_max24[ann_max24["basin_id"] == bid]["precip_mm"].values
        mean_x = np.mean(s_data)
        std_x = np.std(s_data, ddof=1)
        mean_ann = float(ann_sum[ann_sum["basin_id"] == bid]["precip_mm"].mean())

        # Gumbel EV1 fits
        # y_T = -ln(-ln(1 - 1/T))
        # x_T = mean + (y_T - 0.5772) * (std * sqrt(6) / pi)
        alpha = std_x * np.sqrt(6.0) / np.pi
        u = mean_x - 0.5772 * alpha

        row = {
            "basin_id": bid,
            "station": st["name"],
            "Mean_Annual_P_mm": round(mean_ann, 1),
            "Mean_24h_Max_mm": round(mean_x, 1),
            "Std_24h_Max_mm": round(std_x, 1)
        }
        for T in ret_periods:
            y_T = -np.log(-np.log(1.0 - 1.0 / T))
            x_T = u + alpha * y_T
            row[f"P_{T}yr_mm"] = round(float(x_T), 1)

        gumbel_rows.append(row)

    df_gumbel = pd.DataFrame(gumbel_rows)
    df_gumbel.to_csv(OUT_DIR / "gumbel_design_rainfall_openmeteo.csv", index=False)
    print("\n=== CALIBRATED GUMBEL DESIGN RAINFALL (OPEN-METEO 2000-2023) ===")
    print(df_gumbel.to_string())

if __name__ == "__main__":
    main()

