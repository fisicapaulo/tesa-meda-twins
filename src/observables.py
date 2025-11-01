# -*- coding: utf-8 -*-
"""
observables.py
Construção de A_X, B_X e emparelhamentos (stubs auditáveis).
"""
import numpy as np

def build_AX_BX(N=1024, seed=123):
    rng = np.random.default_rng(seed)
    # Stubs: A_X e B_X positivos em média (para projeção positiva)
    AX = np.abs(rng.normal(size=N)) + 0.1
    BX = np.abs(rng.normal(size=N)) + 0.1
    return AX, BX

def pairing(vec1, vec2):
    v1 = np.asarray(vec1, dtype=float)
    v2 = np.asarray(vec2, dtype=float)
    return float(np.vdot(v1, v2).real) / len(v1)
