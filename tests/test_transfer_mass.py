# -*- coding: utf-8 -*-
import numpy as np
from src.transfer import build_transfer_matrix

def test_mass_conservation():
    T = build_transfer_matrix(N=64, eta=0.03)
    one = np.ones((64,), dtype=complex)
    err = np.max(np.abs(one @ T - one))
    assert err < 1e-6
