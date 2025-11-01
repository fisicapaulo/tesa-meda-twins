# -*- coding: utf-8 -*-
"""
anisobanach.py
Projeções Littlewood–Paley (via FFT) e normas anisotrópicas (stubs).
"""
import numpy as np

def lp_project(signal, j, N):
    # Projeção simples (mock): janela passa-banda centrada em |k| ~ 2^j
    # Para auditoria, retornamos o próprio sinal (stub); implementação real: FFT + máscara.
    return signal.copy()

def anisotropic_norm(signal, sigma_u=0.5, p=2):
    # Norma anisotrópica simples (stub): ||signal||_2 ponderada
    s = np.asarray(signal)
    return float(np.linalg.norm(s) + 1e-12)
