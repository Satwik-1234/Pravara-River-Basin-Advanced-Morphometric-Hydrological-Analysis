"""
================================================================================
E2E ACCEPTANCE TEST SUITE: PRAVARA RIVER BASIN REMEDIATION
================================================================================
Automated multi-tier end-to-end verification suite testing all scientific
remediations, physical boundary invariants, cross-feature hydrodynamics,
and cartographic deliverables for the Pravara River Basin project.

Test Architecture according to TEST_INFRA.md:
  - Tier 1: Feature & Deliverable Existence (Audit report, CSVs, pipeline, maps)
  - Tier 2: Physical Boundary & Invariant Assertions (Shear stress, stream power,
            bed slope, check dams, RUSLE soil loss, Melton MRN, Tc)
  - Tier 3: Cross-Feature Hydrodynamic & Morphometric Consistency (Manning Q,
            Horton's laws, SB identity/area, geomorphic stability, CN/Runoff)
  - Tier 4: Real-World Scenario Acceptance (Pipeline integrity, zero nulls,
            cartographic fidelity, end-to-end acceptance)

Total tests: 36 automated test methods (> 30 threshold).
Run with: pytest tests/test_remediation_e2e.py -v
================================================================================
"""

import ast
import re
from pathlib import Path
import pandas as pd
from PIL import Image
import pytest

# Dynamic workspace anchoring
BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"
SCRIPTS_DIR = BASE_DIR / "scripts"
OUTPUTS_DIR = BASE_DIR / "outputs"
TABLES_DIR = OUTPUTS_DIR / "tables"
HYD_DIR = OUTPUTS_DIR / "hydrology"
CONS_DIR = OUTPUTS_DIR / "conservation"
MAPS_DIR = OUTPUTS_DIR / "ultimate_publication_suite"


# ==============================================================================
# TIER 1: FEATURE & DELIVERABLE EXISTENCE
# ==============================================================================
class TestTier1DeliverableExistence:
    """Verifies existence, non-emptiness, and structural integrity of all key deliverables."""

    def test_audit_report_file_exists(self):
        """Verify that reports/AUDIT_AND_JUSTIFICATION_REPORT.md exists and is substantive."""
        report_path = REPORTS_DIR / "AUDIT_AND_JUSTIFICATION_REPORT.md"
        assert report_path.is_file(), f"Audit report not found at {report_path}"
        file_size = report_path.stat().st_size
        assert file_size > 15_000, (
            f"Audit report size ({file_size} bytes) is suspiciously small. Expected >15 KB."
        )

    def test_audit_report_contains_all_5_comparison_tables(self):
        """Verify that the audit report contains all 5 mandatory Before/After comparison tables."""
        report_path = REPORTS_DIR / "AUDIT_AND_JUSTIFICATION_REPORT.md"
        content = report_path.read_text(encoding="utf-8")

        required_tables = [
            ("Table 1", "Morphometry"),
            ("Table 2", "Hydrology"),
            ("Table 3", "Hydraulics"),
            ("Table 4", "Conservation"),
            ("Table 5", "Flash Flood"),
        ]
        for tbl_id, topic in required_tables:
            pattern = re.compile(rf"{tbl_id}:.*{topic}", re.IGNORECASE)
            assert pattern.search(content), (
                f"Missing {tbl_id} ({topic} Comparison Matrix) in {report_path.name}"
            )

    def test_audit_report_contains_literature_citations(self):
        """Verify that the audit report documents key theoretical and empirical literature."""
        report_path = REPORTS_DIR / "AUDIT_AND_JUSTIFICATION_REPORT.md"
        content = report_path.read_text(encoding="utf-8")

        required_citations = [
            "Horton",
            "Strahler",
            "Melton",
            "Leopold",
            "Manning",
            "Moore",
            "ICAR",
            "Central Water Commission",
        ]
        for citation in required_citations:
            assert citation.lower() in content.lower(), (
                f"Missing reference to '{citation}' in audit report literature section."
            )

    def test_consolidated_pipeline_exists_and_valid_syntax(self):
        """Verify that scripts/pravra_consolidated_pipeline.py exists and is syntactically valid."""
        pipeline_path = SCRIPTS_DIR / "pravra_consolidated_pipeline.py"
        assert pipeline_path.is_file(), f"Consolidated pipeline missing at {pipeline_path}"

        code = pipeline_path.read_text(encoding="utf-8")
        try:
            ast.parse(code, filename=str(pipeline_path))
        except SyntaxError as e:
            pytest.fail(f"Syntax error in consolidated pipeline: {e}")

    def test_tables_csv_existence_and_non_empty(self):
        """Verify that required tabular CSVs exist in outputs/tables/ and have records."""
        required_csvs = [
            "stream_order_summary.csv",
            "morphometric_master_table.csv",
            "hydrology_SWC_consolidated.csv",
        ]
        for name in required_csvs:
            csv_path = TABLES_DIR / name
            assert csv_path.is_file(), f"Missing table CSV: {csv_path}"
            df = pd.read_csv(csv_path)
            assert len(df) > 0, f"Table CSV {name} is empty"

    def test_hydrology_csv_existence_and_non_empty(self):
        """Verify that required hydrology CSVs exist in outputs/hydrology/ and have records."""
        required_csvs = [
            "channel_hydraulics.csv",
            "RUSLE_soil_erosion.csv",
            "rainfall_frequency.csv",
            "runoff_scscn.csv",
            "time_of_concentration_peak_discharge.csv",
        ]
        for name in required_csvs:
            csv_path = HYD_DIR / name
            assert csv_path.is_file(), f"Missing hydrology CSV: {csv_path}"
            df = pd.read_csv(csv_path)
            assert len(df) > 0, f"Hydrology CSV {name} is empty"

    def test_conservation_csv_existence_and_non_empty(self):
        """Verify that required conservation CSVs exist in outputs/conservation/ and have records."""
        required_csvs = [
            "conservation_potential.csv",
            "checkdam_suitability.csv",
        ]
        for name in required_csvs:
            csv_path = CONS_DIR / name
            assert csv_path.is_file(), f"Missing conservation CSV: {csv_path}"
            df = pd.read_csv(csv_path)
            assert len(df) > 0, f"Conservation CSV {name} is empty"

    def test_25_publication_maps_all_exist(self):
        """Verify that all 25 institutional publication map PNGs exist in outputs/ultimate_publication_suite/."""
        expected_maps = [
            "01_Digital_Elevation_Model.png",
            "02_Slope_Distribution.png",
            "03_Aspect_Map.png",
            "04_Topographic_Wetness_Index.png",
            "05_Stream_Power_Index.png",
            "06_Sediment_Transport_Index.png",
            "07_Topographic_Ruggedness_Index.png",
            "08_Tectonic_Lineament_Density.png",
            "09_Flow_Direction.png",
            "10_Flow_Accumulation.png",
            "11_Curve_Number_CN_Map.png",
            "12_Flash_Flood_Potential_Index.png",
            "13_Geomorphic_Anomaly_Index.png",
            "14_HI_High_Anomaly_Areas.png",
            "15_Percolation_Potential.png",
            "16_Contour_Trench_Suitability.png",
            "17_RUSLE_Potential_Soil_Loss.png",
            "18_RUSLE_C-Factor_Land_Cover.png",
            "19_RUSLE_K-Factor_Erodibility.png",
            "20_RUSLE_LS-Factor_Topography.png",
            "21_RUSLE_P-Factor_Conservation.png",
            "22_RUSLE_R-Factor_Rainfall.png",
            "23_Stream_Order_Map.png",
            "24_Drainage_Density_Map.png",
            "25_Topographic_Contour_Map.png",
        ]
        for map_name in expected_maps:
            map_path = MAPS_DIR / map_name
            assert map_path.is_file(), f"Publication map {map_name} missing at {map_path}"

    def test_publication_maps_file_sizes_exceed_threshold(self):
        """Verify that each of the 25 publication map PNGs exceeds the 500 KB non-trivial file size threshold."""
        png_files = list(MAPS_DIR.glob("*.png"))
        assert len(png_files) >= 25, f"Expected at least 25 PNG maps, found {len(png_files)}"
        for png in png_files:
            size_bytes = png.stat().st_size
            assert size_bytes > 500_000, (
                f"Map {png.name} size ({size_bytes} bytes) is below 500 KB threshold."
            )

    def test_publication_maps_institutional_dpi_and_dimensions(self):
        """Verify that maps have institutional 600 DPI resolution and large pixel dimensions."""
        sample_maps = [
            "01_Digital_Elevation_Model.png",
            "12_Flash_Flood_Potential_Index.png",
            "23_Stream_Order_Map.png",
        ]
        for name in sample_maps:
            map_path = MAPS_DIR / name
            with Image.open(map_path) as img:
                w, h = img.size
                dpi = img.info.get("dpi", (0, 0))
                # Check dimensions >= 4000x3000
                assert w >= 4000 and h >= 3000, (
                    f"Map {name} dimensions ({w}x{h}) are too small for 600-DPI publication."
                )
                # Check DPI >= 590
                assert dpi[0] >= 590 and dpi[1] >= 590, (
                    f"Map {name} DPI {dpi} is below 600 DPI institutional standard."
                )


# ==============================================================================
# TIER 2: PHYSICAL BOUNDARY & INVARIANT ASSERTIONS
# ==============================================================================
class TestTier2PhysicalBoundariesAndInvariants:
    """Verifies that hydraulic, hydrologic, and morphometric values satisfy physical bounds."""

    @pytest.fixture(autouse=True)
    def setup_data(self):
        self.df_hyd = pd.read_csv(HYD_DIR / "channel_hydraulics.csv")
        self.df_ru = pd.read_csv(HYD_DIR / "RUSLE_soil_erosion.csv")
        self.df_cons = pd.read_csv(CONS_DIR / "conservation_potential.csv")
        self.df_master = pd.read_csv(TABLES_DIR / "morphometric_master_table.csv")
        self.df_tc = pd.read_csv(HYD_DIR / "time_of_concentration_peak_discharge.csv")

    def test_channel_bed_shear_stress_in_alluvial_bounds(self):
        """Verify that bed shear stress tau0 is within [20, 150] Pa for all sub-basins."""
        for _, row in self.df_hyd.iterrows():
            bid = row["basin_id"]
            tau0 = row["Shear_Stress_Pa"]
            assert 20.0 <= tau0 <= 150.0, (
                f"Sub-basin {bid} Bed Shear Stress {tau0:.2f} Pa violates alluvial bound [20, 150] Pa."
            )

    def test_channel_bed_shear_stress_not_inflated_by_relief(self):
        """Verify that bed shear stress is not erroneously inflated by relief ratio (>1000 Pa)."""
        for _, row in self.df_hyd.iterrows():
            bid = row["basin_id"]
            tau0 = row["Shear_Stress_Pa"]
            assert tau0 < 200.0, (
                f"Sub-basin {bid} Shear Stress {tau0:.2f} Pa indicates relief ratio slope inflation defect."
            )

    def test_specific_stream_power_within_physical_limits(self):
        """Verify that specific stream power omega is < 300 W/m2 for all sub-basins."""
        for _, row in self.df_hyd.iterrows():
            bid = row["basin_id"]
            omega = row["Stream_Power_spec_Wm2"]
            assert omega < 300.0, (
                f"Sub-basin {bid} Specific Stream Power {omega:.2f} W/m2 exceeds physical limit 300 W/m2."
            )
            assert omega > 30.0, (
                f"Sub-basin {bid} Specific Stream Power {omega:.2f} W/m2 is unphysically low for alluvial channels."
            )

    def test_channel_bed_slope_strictly_matches_10_85_slo(self):
        """Verify that Channel_Slope_S matches GIS 10_85_slo (0.003557, 0.012723, 0.001902)."""
        expected_slopes = {
            "SB1": 0.003557,
            "SB2": 0.012723,
            "SB3": 0.001902,
        }
        for _, row in self.df_hyd.iterrows():
            bid = row["basin_id"]
            s0 = row["Channel_Slope_S"]
            exp = expected_slopes[bid]
            assert pytest.approx(exp, rel=1e-2) == s0, (
                f"Sub-basin {bid} slope {s0:.6f} does not match 10-85 slope {exp:.6f}."
            )

    def test_channel_bed_slope_distinct_from_relief_ratio(self):
        """Verify that Channel_Slope_S is NOT equal to the watershed relief ratio Rh."""
        relief_ratios = {
            "SB1": 0.02808,
            "SB2": 0.04625,
            "SB3": 0.03695,
        }
        for _, row in self.df_hyd.iterrows():
            bid = row["basin_id"]
            s0 = row["Channel_Slope_S"]
            rh = relief_ratios[bid]
            assert abs(s0 - rh) > 0.01, (
                f"Sub-basin {bid} slope {s0:.6f} suspiciously identical to relief ratio {rh:.6f}."
            )

    def test_check_dam_counts_strictly_non_identical(self):
        """Verify that check dam counts are strictly non-identical across SB1, SB2, SB3."""
        cd_counts = dict(zip(self.df_cons["basin_id"], self.df_cons["Potential_CheckDams_N"]))
        assert cd_counts["SB1"] == 473, f"Expected SB1 check dams = 473, got {cd_counts['SB1']}"
        assert cd_counts["SB2"] == 142, f"Expected SB2 check dams = 142, got {cd_counts['SB2']}"
        assert cd_counts["SB3"] == 422, f"Expected SB3 check dams = 422, got {cd_counts['SB3']}"
        assert len(set(cd_counts.values())) == 3, "Check dam counts must be distinct for each sub-basin."
        assert sum(cd_counts.values()) == 1037, f"Total check dams must be 1037, got {sum(cd_counts.values())}"

    def test_check_dam_counts_no_global_duplication(self):
        """Verify that no individual sub-basin reports the global total 1037 (fixing loop unclipped bug)."""
        for _, row in self.df_cons.iterrows():
            bid = row["basin_id"]
            count = row["Potential_CheckDams_N"]
            assert count != 1037, (
                f"Sub-basin {bid} check dam count is 1037, indicating global loop duplication defect."
            )

    def test_rusle_mean_annual_soil_loss_in_icar_benchmark(self):
        """Verify that RUSLE mean annual soil loss is in [5, 25] t/ha/yr (ICAR Deccan benchmark)."""
        for _, row in self.df_ru.iterrows():
            bid = row["basin_id"]
            loss = row["A_mean_t_ha_yr"]
            assert 5.0 <= loss <= 25.0, (
                f"Sub-basin {bid} RUSLE soil loss {loss:.2f} t/ha/yr violates ICAR benchmark [5, 25] t/ha/yr."
            )

    def test_rusle_gross_erosion_and_sdr_physical_bounds(self):
        """Verify that gross erosion is non-negative and SDR is within [0.15, 0.35]."""
        for _, row in self.df_ru.iterrows():
            bid = row["basin_id"]
            sdr = row["SDR"]
            gross = row["Gross_Erosion_t_yr"]
            assert 0.15 <= sdr <= 0.35, f"Sub-basin {bid} SDR {sdr:.3f} outside physical range [0.15, 0.35]"
            assert gross > 10_000, f"Sub-basin {bid} Gross erosion {gross:.1f} t/yr is unexpectedly low"

    def test_melton_ruggedness_number_is_dimensionless(self):
        """Verify that Melton Ruggedness Number MRN is in [0.05, 0.15] dimensionless."""
        for _, row in self.df_master.iterrows():
            bid = row["basin_id"]
            mrn = row["Melton_MRN"]
            assert 0.05 <= mrn <= 0.15, (
                f"Sub-basin {bid} Melton MRN {mrn:.4f} violates dimensionless bound [0.05, 0.15]."
            )
            # Must not be the unscaled value ~80-114
            assert mrn < 1.0, f"Sub-basin {bid} Melton MRN {mrn:.4f} indicates unscaled unit mismatch defect."

    def test_time_of_concentration_realistic_bounds(self):
        """Verify that Time of Concentration Tc is in [5.0, 9.0] hr for large basins."""
        tc_dict = dict(zip(self.df_tc["basin_id"], self.df_tc["Tc_hr"]))
        # SB1 (150 km2) and SB3 (117 km2)
        assert 5.0 <= tc_dict["SB1"] <= 9.0, (
            f"SB1 Tc ({tc_dict['SB1']:.2f} hr) violates physical range [5.0, 9.0] hr."
        )
        assert 5.0 <= tc_dict["SB3"] <= 9.0, (
            f"SB3 Tc ({tc_dict['SB3']:.2f} hr) violates physical range [5.0, 9.0] hr."
        )
        # SB2 (45 km2)
        assert 4.0 <= tc_dict["SB2"] <= 7.0, (
            f"SB2 Tc ({tc_dict['SB2']:.2f} hr) violates physical range [4.0, 7.0] hr."
        )

    def test_basin_morphometric_shape_invariants(self):
        """Verify flow path length Lb, elongation ratio Re, and basin relief H invariants."""
        # Check Lb matches long_len from GIS: SB1 ~29.56, SB2 ~16.45, SB3 ~23.14 km
        exp_lb = {"SB1": 29.56, "SB2": 16.45, "SB3": 23.14}
        for _, row in self.df_master.iterrows():
            bid = row["basin_id"]
            lb = row["Basin_Length_km"]
            re_val = row["Elongation_Ratio_Re"]
            h_m = row["Basin_Relief_H_m"]
            assert pytest.approx(exp_lb[bid], rel=0.02) == lb, (
                f"Sub-basin {bid} Lb {lb:.2f} km differs from true longest flow path {exp_lb[bid]:.2f} km."
            )
            assert 0.40 <= re_val <= 0.60, f"Sub-basin {bid} Re {re_val:.3f} outside [0.40, 0.60]"
            assert 700.0 <= h_m <= 900.0, f"Sub-basin {bid} Relief {h_m:.1f} m outside [700, 900] m"


# ==============================================================================
# TIER 3: CROSS-FEATURE HYDRODYNAMIC & MORPHOMETRIC CONSISTENCY
# ==============================================================================
class TestTier3CrossFeatureHydrodynamicConsistency:
    """Verifies relational consistency across hydrology, hydraulics, and stream morphology."""

    @pytest.fixture(autouse=True)
    def setup_data(self):
        self.df_hyd = pd.read_csv(HYD_DIR / "channel_hydraulics.csv")
        self.df_order = pd.read_csv(TABLES_DIR / "stream_order_summary.csv")
        self.df_master = pd.read_csv(TABLES_DIR / "morphometric_master_table.csv")
        self.df_runoff = pd.read_csv(HYD_DIR / "runoff_scscn.csv")
        self.df_tc = pd.read_csv(HYD_DIR / "time_of_concentration_peak_discharge.csv")
        self.df_ru = pd.read_csv(HYD_DIR / "RUSLE_soil_erosion.csv")

    def test_manning_bankfull_discharge_reconciliation(self):
        """Verify that Manning discharge Q_mann matches bankfull discharge Q_bf within 5%."""
        for _, row in self.df_hyd.iterrows():
            bid = row["basin_id"]
            q_bf = row["Q_bankfull_m3s"]
            q_mann = row["Q_Manning_m3s"]
            rel_diff = abs(q_mann - q_bf) / q_bf
            assert rel_diff <= 0.05, (
                f"Sub-basin {bid} Manning Q ({q_mann:.2f} m3/s) differs from Bankfull Q "
                f"({q_bf:.2f} m3/s) by {rel_diff * 100:.2f}% (exceeds 5% tolerance)."
            )

    def test_horton_law_of_stream_numbers_monotonicity(self):
        """Verify that stream counts Nu decrease monotonically with Strahler order."""
        for bid in ["SB1", "SB2", "SB3"]:
            sub = self.df_order[self.df_order["basin_id"] == bid].sort_values("order")
            nu_list = sub["Nu"].tolist()
            # For each order u, Nu(u) > Nu(u+1)
            for i in range(len(nu_list) - 1):
                assert nu_list[i] >= nu_list[i + 1], (
                    f"Sub-basin {bid} violates Horton's Law of Stream Numbers: "
                    f"Order {i + 1} Nu={nu_list[i]} <= Order {i + 2} Nu={nu_list[i + 1]}."
                )

    def test_horton_law_stream_number_outlet_reach(self):
        """Verify that highest Strahler order (Order 6) stream count Nu == 1 at outlet."""
        for bid in ["SB1", "SB2", "SB3"]:
            sub = self.df_order[(self.df_order["basin_id"] == bid) & (self.df_order["order"] == 6)]
            assert len(sub) == 1, f"Missing Order 6 record for {bid}"
            nu_6 = sub["Nu"].iloc[0]
            assert nu_6 == 1, f"Sub-basin {bid} Order 6 stream count is {nu_6}, expected exactly 1."

    def test_horton_mean_bifurcation_ratio_bounds(self):
        """Verify that mean bifurcation ratio Rbm is in [3.0, 5.5] for all sub-basins."""
        for _, row in self.df_master.iterrows():
            bid = row["basin_id"]
            rbm = row["Rbm"]
            assert 3.0 <= rbm <= 5.5, (
                f"Sub-basin {bid} mean bifurcation ratio {rbm:.2f} outside theoretical range [3.0, 5.5]."
            )

    def test_horton_law_of_stream_lengths_progression(self):
        """Verify that mean stream length Lsm increases geometrically for orders 1 through 4."""
        for bid in ["SB1", "SB2", "SB3"]:
            sub = self.df_order[self.df_order["basin_id"] == bid].sort_values("order")
            lsm_list = dict(zip(sub["order"], sub["Lsm"]))
            # Check orders 1 -> 2 -> 3 -> 4
            assert lsm_list[1] < lsm_list[2] < lsm_list[3] < lsm_list[4], (
                f"Sub-basin {bid} violates Horton's Law of Stream Lengths for orders 1-4: "
                f"Lsm = {lsm_list}."
            )

    def test_subbasin_spatial_identity_no_inversion(self):
        """Verify that subbasin areas match correct geographic IDs: SB1 ~150, SB2 ~45, SB3 ~117 km2."""
        areas = dict(zip(self.df_master["basin_id"], self.df_master["Area_km2"]))
        # SB1: ~150 km2
        assert 148.0 <= areas["SB1"] <= 152.0, (
            f"SB1 Area {areas['SB1']:.2f} km2 incorrect. Expected ~150 km2 (Check for inversion with SB3)."
        )
        # SB2: ~45.2 km2
        assert 44.0 <= areas["SB2"] <= 47.0, (
            f"SB2 Area {areas['SB2']:.2f} km2 incorrect. Expected ~45.2 km2."
        )
        # SB3: ~117 km2
        assert 115.0 <= areas["SB3"] <= 119.0, (
            f"SB3 Area {areas['SB3']:.2f} km2 incorrect. Expected ~117 km2 (Check for inversion with SB1)."
        )
        # Crucial check: SB1 Area > SB3 Area
        assert areas["SB1"] > areas["SB3"], "SB1 must be larger than SB3 (ID inversion detected)."

    def test_channel_geomorphic_stability_classifications(self):
        """Verify that channel stability classifications are physically grounded ('Stable' or 'Marginally Stable')."""
        stability_dict = dict(zip(self.df_hyd["basin_id"], self.df_hyd["Channel_Stability"]))
        assert stability_dict["SB1"] == "Stable", f"SB1 expected 'Stable', got {stability_dict['SB1']}"
        assert stability_dict["SB2"] == "Marginally Stable", f"SB2 expected 'Marginally Stable', got {stability_dict['SB2']}"
        assert stability_dict["SB3"] == "Stable", f"SB3 expected 'Stable', got {stability_dict['SB3']}"
        # Assert no sub-basin is classified as "Highly Unstable"
        assert "Highly Unstable" not in stability_dict.values(), (
            "Found 'Highly Unstable' classification resulting from legacy relief ratio bug."
        )

    def test_scs_cn_infiltration_deficit_and_retention(self):
        """Verify soil moisture retention S > 0 and runoff depth increases with rainfall return period."""
        for _, row in self.df_runoff.iterrows():
            bid = row["basin_id"]
            s_mm = row["S_mm"]
            assert s_mm > 0, f"Sub-basin {bid} retention S={s_mm} must be strictly positive."
            # Check monotonic increase with return period
            q2 = row["Q_2yr_mm"]
            q5 = row["Q_5yr_mm"]
            q10 = row["Q_10yr_mm"]
            q25 = row["Q_25yr_mm"]
            q50 = row["Q_50yr_mm"]
            q100 = row["Q_100yr_mm"]
            assert q2 < q5 < q10 < q25 < q50 < q100, (
                f"Sub-basin {bid} runoff depths do not increase monotonically with return period: "
                f"[{q2}, {q5}, {q10}, {q25}, {q50}, {q100}]"
            )

    def test_peak_discharge_return_period_and_area_scaling(self):
        """Verify that peak flood discharges scale monotonically with return period and basin area."""
        for _, row in self.df_tc.iterrows():
            bid = row["basin_id"]
            qp2 = row["Qp_2yr_m3s"]
            qp10 = row["Qp_10yr_m3s"]
            qp50 = row["Qp_50yr_m3s"]
            qp100 = row["Qp_100yr_m3s"]
            assert qp2 < qp10 < qp50 < qp100, (
                f"Sub-basin {bid} peak discharge does not increase with return period: "
                f"[{qp2}, {qp10}, {qp50}, {qp100}]"
            )

        # Cross-basin area scaling: SB1 (150 km2) > SB3 (117 km2) > SB2 (45 km2)
        tc_map = self.df_tc.set_index("basin_id")
        assert tc_map.loc["SB1", "Qp_100yr_m3s"] > tc_map.loc["SB3", "Qp_100yr_m3s"] > tc_map.loc["SB2", "Qp_100yr_m3s"], (
            "100-yr peak discharge does not follow drainage area order (SB1 > SB3 > SB2)."
        )


# ==============================================================================
# TIER 4: REAL-WORLD SCENARIO ACCEPTANCE
# ==============================================================================
class TestTier4RealWorldScenarioAcceptance:
    """Verifies end-to-end pipeline execution integrity, null-free schemas, and publication completeness."""

    def test_consolidated_pipeline_script_integrity(self):
        """Verify that scripts/pravra_consolidated_pipeline.py contains all 15 required phases."""
        pipeline_path = SCRIPTS_DIR / "pravra_consolidated_pipeline.py"
        code = pipeline_path.read_text(encoding="utf-8")

        required_phases = [
            "PHASE 1: DIRECTORY CONFIGURATION & ANCHORING",
            "PHASE 2: SPATIAL DATA INGESTION & CRS VERIFICATION",
            "PHASE 3: DIGITAL ELEVATION & TERRAIN ANALYSIS",
            "PHASE 4: MORPHOMETRIC ANALYSIS & TOPOLOGICAL REACH MERGING (HORTON'S LAWS)",
            "PHASE 5: STATISTICAL ANALYSIS & PRIORITIZATION",
            "PHASE 6: TECTONIC ACTIVITY & GEOMORPHIC ANOMALIES",
            "PHASE 7: FLASH FLOOD POTENTIAL INDEX (FFPI) REMEDIATION",
            "PHASE 8: RUNOFF & INFILTRATION (SCS-CN) & TC REMEDIATION",
            "PHASE 9: SYNTHETIC UNIT HYDROGRAPH (SNYDER & SCS)",
            "PHASE 10: RUSLE SOIL EROSION MODELING",
            "PHASE 11: CONSERVATION PLANNING & CHECK DAMS",
            "PHASE 12: STREAM CHANNEL HYDRAULICS REMEDIATION",
            "PHASE 13: CONSOLIDATED HYDROLOGY & SWC OUTPUT TABLE",
            "PHASE 14: PUBLICATION MAPS REGENERATION TRIGGER",
            "PHASE 15: MASTER PIPELINE VERIFICATION SUMMARY",
        ]
        for phase in required_phases:
            assert phase in code, f"Pipeline code missing mandatory module phase: {phase}"

    def test_pipeline_has_no_broken_hardcoded_paths(self):
        """Verify that scripts/pravra_consolidated_pipeline.py contains no obsolete hardcoded paths."""
        pipeline_path = SCRIPTS_DIR / "pravra_consolidated_pipeline.py"
        code = pipeline_path.read_text(encoding="utf-8")

        obsolete_patterns = [
            "E:/Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main",
            "E:\\Pravara-River-Basin-Advanced-Morphometric-Hydrological-Analysis-main",
            "C:/Users/",
            "C:\\Users\\",
        ]
        for pattern in obsolete_patterns:
            assert pattern not in code, (
                f"Found obsolete hardcoded path pattern '{pattern}' in consolidated pipeline."
            )

    def test_all_tabular_outputs_completeness_and_zero_nulls(self):
        """Verify that all generated CSV tables have 0 NaN values in critical columns."""
        tables_to_check = [
            (
                TABLES_DIR / "morphometric_master_table.csv",
                ["Area_km2", "Basin_Length_km", "Melton_MRN", "Rbm"],
            ),
            (
                HYD_DIR / "channel_hydraulics.csv",
                ["Q_bankfull_m3s", "Q_Manning_m3s", "Shear_Stress_Pa", "Stream_Power_spec_Wm2"],
            ),
            (
                HYD_DIR / "RUSLE_soil_erosion.csv",
                ["A_mean_t_ha_yr", "Gross_Erosion_t_yr", "SDR"],
            ),
            (
                CONS_DIR / "conservation_potential.csv",
                ["Potential_CheckDams_N", "WHP_25yr_Mm3"],
            ),
            (
                HYD_DIR / "time_of_concentration_peak_discharge.csv",
                ["Tc_hr", "Qp_100yr_m3s"],
            ),
        ]
        for path, cols in tables_to_check:
            assert path.is_file(), f"Missing CSV: {path}"
            df = pd.read_csv(path)
            assert len(df) == 3, f"Expected 3 sub-basin records in {path.name}, got {len(df)}"
            for col in cols:
                assert col in df.columns, f"Column '{col}' missing in {path.name}"
                nan_count = df[col].isna().sum()
                assert nan_count == 0, f"Found {nan_count} NaN values in column '{col}' of {path.name}"

    def test_publication_maps_complete_set_fidelity(self):
        """Verify that all 25 institutional maps are loadable, uncorrupted images with matching titles."""
        for i in range(1, 26):
            matches = list(MAPS_DIR.glob(f"{i:02d}_*.png"))
            assert len(matches) == 1, f"Missing or duplicate publication map {i:02d} in {MAPS_DIR}"
            map_file = matches[0]
            try:
                with Image.open(map_file) as img:
                    img.verify()
            except Exception as e:
                pytest.fail(f"Corrupted image file {map_file.name}: {e}")

    def test_end_to_end_project_acceptance_criteria(self):
        """Overarching acceptance test verifying all client remediation criteria simultaneously."""
        # 1. Audit report exists
        assert (REPORTS_DIR / "AUDIT_AND_JUSTIFICATION_REPORT.md").is_file()
        # 2. Consolidated pipeline exists
        assert (SCRIPTS_DIR / "pravra_consolidated_pipeline.py").is_file()
        # 3. Hydraulics bed shear stress and specific stream power in bounds
        df_hyd = pd.read_csv(HYD_DIR / "channel_hydraulics.csv")
        assert (df_hyd["Shear_Stress_Pa"].between(20.0, 150.0)).all()
        assert (df_hyd["Stream_Power_spec_Wm2"] < 300.0).all()
        # 4. Check dam counts unique
        df_cons = pd.read_csv(CONS_DIR / "conservation_potential.csv")
        counts = df_cons["Potential_CheckDams_N"].tolist()
        assert counts == [473, 142, 422]
        # 5. RUSLE within benchmark
        df_ru = pd.read_csv(HYD_DIR / "RUSLE_soil_erosion.csv")
        assert (df_ru["A_mean_t_ha_yr"].between(5.0, 25.0)).all()
        # 6. Melton MRN dimensionless
        df_master = pd.read_csv(TABLES_DIR / "morphometric_master_table.csv")
        assert (df_master["Melton_MRN"].between(0.05, 0.15)).all()
        # 7. 25 publication maps exist
        assert len(list(MAPS_DIR.glob("*.png"))) == 25
