"""
run_pipeline.py

Master orchestrator script that runs all 18 sections of the Pravara River Basin
morphometric and hydrological analysis sequentially.
"""

import os
import subprocess
import sys


def run_script(script_name):
    print(f"\n{'='*60}")
    print(f"🚀 Running: {script_name}")
    print(f"{'='*60}")

    script_path = os.path.join("scripts", script_name)

    if not os.path.exists(script_path):
        print(f"❌ Error: Script '{script_path}' not found.")
        return False

    try:
        # Run the script and stream output
        result = subprocess.run([sys.executable, script_path], check=True, text=True)
        print(f"✅ Successfully completed: {script_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Pipeline failed at: {script_name}")
        print(f"Exit code: {e.returncode}")
        return False


def main():
    print("==================================================")
    print("  PRAVARA RIVER BASIN ANALYSIS PIPELINE STARTER   ")
    print("==================================================")

    # List of scripts in execution order based on project architecture
    # Note: excluding section_00 for zip extraction assuming data is unzipped
    # excluding section_01 environment as that's already setup locally.
    scripts = [
        "section_02_data_paths.py",
        "section_03_morphometry.py",
        "section_04_maps.py",
        "section_05_statistics.py",
        "section_06_prioritization.py",
        "section_07_plotly.py",
        "section_08_export.py",
        "section_09_report.py",
        "section_10_tectonic.py",
        "section_11_geomorphic.py",
        "section_12_anomaly.py",
        "section_13_flood.py",
        "section_14_runoff.py",
        "section_15_rusle.py",
        "section_16_swc.py",
        "section_17_hydrograph.py",
        "section_18_hydraulics.py",
    ]

    # Ensure starting from the repository root
    if not os.path.exists("scripts"):
        print("Please run this script from the repository root directory.")
        print("Example: python scripts/run_pipeline.py")
        sys.exit(1)

    for script in scripts:
        success = run_script(script)
        if not success:
            print("\nPipeline execution halted due to errors.")
            sys.exit(1)

    print("\n==================================================")
    print("🎉 FULL PIPELINE COMPLETED SUCCESSFULLY 🎉")
    print("==================================================")


if __name__ == "__main__":
    main()
