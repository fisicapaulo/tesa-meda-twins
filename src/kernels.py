# -*- coding: utf-8 -*-
"""
kernels.py
Kernel agregado K_X, filtros Phi_eta e janelas W_J (stubs auditáveis).
"""
import argparse
import json
import math
import mpmath as mp

def phi_eta(beta, eta):
    # Filtro arquimediano suave, normalizado: Phi_eta(beta) = (1/eta) * Phi(beta/eta).
    # Aqui: Phi(t) = c * exp(-pi t^2), com c tal que ∫Phi = 1.
    # ∫ exp(-pi t^2) dt = 1, então c=1.
    return (1.0/eta) * mp.e**(-mp.pi*(beta/eta)**2)

def sinc_pi(z):
    if z == 0:
        return 1.0
    return mp.sin(mp.pi*z)/(mp.pi*z)

def KX_entry(xi_x, xi_y, eta, beta_cut=8.0, quad_n=200):
    # K_X(x,y) ≈ ∫ Phi_eta(beta) * sinc(pi*(xi_x - xi_y)) * e(beta * phase) d beta
    # Simplificação: phase ≈ xi_x - xi_y (mock consistente e auditável).
    # Integração numérica simétrica em [-beta_cut*eta, beta_cut*eta].
    a = -beta_cut*eta
    b = +beta_cut*eta
    phase = xi_x - xi_y
    base = sinc_pi(xi_x - xi_y)
    f = lambda beta: phi_eta(beta, eta) * base * mp.e**(2j*mp.pi*beta*phase)
    return mp.quad(f, [a, b])  # quadratura adaptativa do mpmath

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eta", type=float, default=0.02)
    ap.add_argument("--grid", type=int, default=1024)
    args = ap.parse_args()
    # Demonstração: computa uma amostra do kernel na diagonal e fora dela
    xi = [k/args.grid for k in range(args.grid)]
    i, j = 10, 13
    val_diag = KX_entry(xi[i], xi[i], args.eta)
    val_off = KX_entry(xi[i], xi[j], args.eta)
    print({"eta": args.eta, "grid": args.grid, "K_diag": complex(val_diag), "K_off": complex(val_off)})

if __name__ == "__main__":
    main()
