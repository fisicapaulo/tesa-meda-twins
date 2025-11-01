# -*- coding: utf-8 -*-
from src.spectrum import estimate_alpha0

def test_alpha0_range():
    lam1, alpha0 = estimate_alpha0(N=64, eta=0.03, maxiter=100)
    assert 0.0 < lam1 <= 1.5
    assert 0.0 <= alpha0 < 1.0
