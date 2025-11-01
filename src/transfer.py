# -*- coding: utf-8 -*-
"""
transfer.py
Discretização de T_X e renormalização de massa (Markov).
"""
import argparse
import numpy as np
from .kernels import KX_entry

def build_transfer_matrix(N=512, eta=0.02):
    xi = np.linspace(0.0, 1.0, N, endpoint=False)
    K = np.zeros((N, N), dtype=np.complex128)
    for i in range(N):
        for j in range(N):
            K[i, j] = complex(KX_entry(xi[i], xi[j], eta))
    # Renormalização de massa por linha: soma_j K[i,j] = 1
    row_sum = K.sum(axis=1, keepdims=True)
    # Evitar divisão por zero em numérica degenerada:
    row_sum[row_sum == 0] = 1.0
    Ktil = K / row_sum
    # Discretização com Δx = 1/N (opcional)
    T = Ktil * (1.0/N)
    return T

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", type=int, default=256)
    ap.add_argument("--eta", type=float, default=0.02)
    args = ap.parse_args()
    T = build_transfer_matrix(N=args.grid, eta=args.eta)
    # Teste de massa: 1^T T ≈ 1^T
    ones = np.ones((args.grid,), dtype=np.complex128)
    lhs = ones @ T
    err_mass = np.max(np.abs(lhs - ones))
    print({"grid": args.grid, "eta": args.eta, "mass_err_inf": float(err_mass)})

if __name__ == "__main__":
    main()
