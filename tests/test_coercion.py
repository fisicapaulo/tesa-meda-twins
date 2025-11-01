# -*- coding: utf-8 -*-
from src.coercion import local_poincare_constant, coercion_global

def test_coercion_positive():
    lam_loc = local_poincare_constant(tile_size=16)
    lam_star = coercion_global(num_tiles=32, active_frac=0.4, w_min=0.5, lambda_min=lam_loc)
    assert lam_loc > 0
    assert lam_star > 0
