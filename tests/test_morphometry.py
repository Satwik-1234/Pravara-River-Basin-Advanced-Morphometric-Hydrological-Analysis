"""
Unit tests for core morphometric and hydrological functions.
Run with: pytest tests/ -v
"""
import numpy as np
import pytest


def scscn_runoff(P_mm, CN):
    S = 25400.0 / CN - 254.0
    I_a = 0.2 * S
    Q = np.where(P_mm > I_a, (P_mm - I_a)**2 / (P_mm + 0.8*S), 0.0)
    return float(np.maximum(Q, 0.0))


def tc_kirpich(L_m, H_m):
    S = max(H_m / L_m, 0.0001) if L_m > 0 else 0.001
    return 0.0195 * (L_m ** 0.77) * (S ** -0.385)


class TestSCSCN:
    def test_no_runoff_below_ia(self):
        assert scscn_runoff(5.0, 75) == 0.0

    def test_runoff_increases_with_P(self):
        assert scscn_runoff(100, 78) > scscn_runoff(50, 78)

    def test_runoff_increases_with_CN(self):
        assert scscn_runoff(50, 85) > scscn_runoff(50, 70)

    def test_deccan_typical_values(self):
        q = scscn_runoff(120, 79)
        assert 30 <= q <= 70


class TestKirpich:
    def test_tc_positive(self):
        assert tc_kirpich(1000, 50) > 0

    def test_tc_increases_with_length(self):
        assert tc_kirpich(2000, 50) > tc_kirpich(1000, 50)


class TestRUSLE:
    def test_ls_factor_positive(self):
        slope_rad = np.radians(10.0)
        As = 100 * 30.0
        LS = ((As / 22.13) ** 0.6) * ((np.sin(slope_rad) / 0.0896) ** 1.3)
        assert LS >= 0

    def test_slight_erosion_on_flat(self):
        R, K, C, P = 650, 0.25, 0.20, 1.0
        slope_rad = np.radians(0.1)
        LS = ((30 / 22.13) ** 0.6) * ((np.sin(slope_rad) / 0.0896) ** 1.3)
        A = R * K * LS * C * P
        assert A < 5.0
