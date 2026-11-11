"""
=============================================================================
PRAVARA RIVER BASIN: MASTER PRODUCTION PIPELINE RUNNER
=============================================================================
Unified CLI entrypoint executing:
  1. pravra_consolidated_pipeline.py (Sections 00 - 18 End-to-End)
  2. ultimate_publication_renderer.py (25 Institutional 600-DPI Maps)
=============================================================================
"""

import os
import sys
import subprocess
from pathlib import Path


def run_step(title, script_name):
    print("\n" + "=" * 70)
    print(f"🚀 STEP: {title}")
    print(f"   Executing: scripts/{script_name}")
    print("=" * 70)

    script_path = Path(__file__).resolve().parent / script_name
    if not script_path.exists():
        print(f"❌ Error: Script '{script_path}' not found.")
        return False

    try:
        subprocess.run([sys.executable, str(script_path)], check=True)
        print(f"✅ COMPLETED: {title}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ FAILED: {title} (Exit Code: {e.returncode})")
        return False


def main():
    print("=" * 70)
    print("  PRAVARA RIVER BASIN — PRODUCTION ANALYSIS PIPELINE (GOOGLE STD)  ")
    print("=" * 70)

    # Step 1: Execute Master Analytical Pipeline (Morphometry, Hydrology, SWC, Hydraulics)
    ok1 = run_step("Analytical Pipeline (Sections 00–18)", "pravra_consolidated_pipeline.py")
    if not ok1:
        sys.exit(1)

    # Step 2: Render 25 High-Resolution Atlas Cartography Maps (Lohara/Tuljapur Standard)
    ok2 = run_step("Atlas Cartography Suite (300 DPI Transparent Atlas Maps)", "pravara_atlas_engine.py")
    if not ok2:
        sys.exit(1)

    print("\n" + "=" * 70)
    print("🎉 ALL PIPELINE STEPS COMPLETED SUCCESSFULLY!")
    print("   • Master Tables: outputs/tables/")
    print("   • Thematic Rasters: outputs/thematic_rasters/")
    print("   • Publication Maps (600 DPI): outputs/ultimate_publication_suite/")
    print("   • Technical Audit: reports/AUDIT_AND_JUSTIFICATION_REPORT.md")
    print("=" * 70)


if __name__ == "__main__":
    main()
