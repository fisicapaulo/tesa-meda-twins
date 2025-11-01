# -*- coding: utf-8 -*-
"""
ttstar.py
Rotina TT* microlocal nas minor arcs (ensaio numérico).
"""
import argparse
import numpy as np

def ttstar_energy(N=1024, eta=0.02, seed=7):
    rng = np.random.default_rng(seed)
    # Energia TT* ~ O(eta^c), c>0 (mock: retorna constante * eta**0.5)
    c = 0.5
    base = np.abs(rng.normal())*0.1 + 0.5
    return float(base * (eta**c))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid", type=int, default=1024)
    ap.add_argument("--eta", type=float, default=0.02)
    args = ap.parse_args()
    E = ttstar_energy(N=args.grid, eta=args.eta)
    print({"grid": args.grid, "eta": args.eta, "TTstar_energy": E})

if __name__ == "__main__":
    main()
