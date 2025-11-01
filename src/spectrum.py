# -*- coding: utf-8 -*-
"""
spectrum.py
Estimativa de autovalores/largura periférica e alpha_0 (método de potência).
"""
import argparse
import numpy as np
from .transfer import build_transfer_matrix

def power_iteration(M, maxiter=200, tol=1e-12, v0=None):
    n = M.shape[0]
    v = np.random.default_rng(123).normal(size=n) if v0 is None else v0.copy()
    v = v / np.linalg.norm(v)
    lam_old = 0.0
    for _ in range(maxiter):
        w = M @ v
        lam = float(np.vdot(v, w).real)
        nrm = np.linalg.norm(w)
        if nrm == 0:
            break
        v = w / nrm
        if abs(lam - lam_old) <= tol*(1.0 + abs(lam_old)):
            break
        lam_old = lam
    return lam, v

def estimate_alpha0(N=512, eta=0.02, maxiter=200):
    T = build_transfer_matrix(N=N, eta=eta)
    # autovalor principal
    lam1, v1 = power_iteration(T, maxiter=maxiter)
    # projeta no subespaço de média zero
    one = np.ones((N,), dtype=np.complex128)
    P = np.eye(N) - np.outer(one, one)/N
    R = P @ T @ P
    # raio espec. aproximado no subespaço
    lam0, _ = power_iteration(R, maxiter=maxiter)
    return float(lam1), float(lam0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", type=int, default=256)
    ap.add_argument("--eta", type=float, default=0.02)
    ap.add_argument("--maxiter", type=int, default=200)
    args = ap.parse_args()
    lam1, alpha0 = estimate_alpha0(N=args.grid, eta=args.eta, maxiter=args.maxiter)
    print({"grid": args.grid, "eta": args.eta, "lambda1": lam1, "alpha0": alpha0, "gap": max(0.0, 1.0-alpha0)})

if __name__ == "__main__":
    main()
