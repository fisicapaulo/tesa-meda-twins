# -*- coding: utf-8 -*-
"""
delta.py
Cálculo de delta efetivo a partir de A_X, B_X e supressão do resíduo <A_X, R^n B_X>.
"""
import argparse
import numpy as np
from .observables import build_AX_BX, pairing
from .spectrum import estimate_alpha0

def choose_n_for_residual(alpha0, target=1e-6):
    if alpha0 >= 1.0:
        return 0
    n = int(np.ceil(np.log(target)/np.log(max(1e-12, alpha0))))
    return max(0, n)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", type=int, default=1024)
    ap.add_argument("--eta", type=float, default=0.02)
    ap.add_argument("--target", type=float, default=1e-6)
    args = ap.parse_args()
    AX, BX = build_AX_BX(N=args.grid)
    pi = pairing(AX, np.ones(args.grid))
    pj = pairing(np.ones(args.grid), BX)
    delta0 = float(pi*pj)
    _, alpha0 = estimate_alpha0(N=args.grid, eta=args.eta, maxiter=200)
    nX = choose_n_for_residual(alpha0, target=args.target)
    delta = 0.5*delta0  # margem final (conservadora)
    print({"grid": args.grid, "eta": args.eta, "delta0": delta0, "alpha0": alpha0, "nX": nX, "delta": delta})

if __name__ == "__main__":
    main()
