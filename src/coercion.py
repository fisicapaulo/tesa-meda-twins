# -*- coding: utf-8 -*-
"""
coercion.py
Forma de Dirichlet discreta por tiles e lambda_* (stubs).
"""
import argparse
import numpy as np

def local_poincare_constant(tile_size=16):
    # Stub: λ_local crescente com conectividade (tile_size)
    return float(0.1 + 0.9 * (1 - np.exp(-tile_size/20.0)))

def coercion_global(num_tiles=64, active_frac=0.3, w_min=0.5, lambda_min=None):
    lam_loc = 0.2 if lambda_min is None else lambda_min
    theta = max(0.0, min(1.0, active_frac))
    return float(w_min * lam_loc * theta)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tiles", type=int, default=64)
    ap.add_argument("--active_frac", type=float, default=0.3)
    ap.add_argument("--tile_size", type=int, default=16)
    args = ap.parse_args()
    lam_loc = local_poincare_constant(tile_size=args.tile_size)
    lam_star = coercion_global(num_tiles=args.tiles, active_frac=args.active_frac, w_min=0.5, lambda_min=lam_loc)
    print({"tiles": args.tiles, "active_frac": args.active_frac, "lambda_local": lam_loc, "lambda_star": lam_star})

if __name__ == "__main__":
    main()
