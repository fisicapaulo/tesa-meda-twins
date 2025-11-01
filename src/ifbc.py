# -*- coding: utf-8 -*-
"""
ifbc.py
Reconstrução numérica controlada nas major arcs (IFBC, stub).
"""
import argparse
import numpy as np

def ifbc_main_term(X=1.0, Qmaj=5000):
    # Stub: retorna X * (1 - c / sqrt(Qmaj))
    c = 1.0
    return float(X * (1.0 - c/np.sqrt(max(1, Qmaj))))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--X", type=float, default=1.0)
    ap.add_argument("--Qmaj", type=int, default=5000)
    args = ap.parse_args()
    mt = ifbc_main_term(X=args.X, Qmaj=args.Qmaj)
    print({"X": args.X, "Qmaj": args.Qmaj, "IFBC_main_term": mt})

if __name__ == "__main__":
    main()
