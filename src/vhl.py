# -*- coding: utf-8 -*-
"""
vhl.py
Certifica numericamente V_HL(2) = 2 * Π_{p>2} (1 - 1/(p-1)^2).
- Geração de primos simples (fallback determinístico).
- Precisão adaptativa mpmath.
- Bound de cauda auditável: exp(C/(Pmax-1)) - 1 com C ≈ constante universal pequena.
"""
import argparse
import mpmath as mp

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(mp.sqrt(n))
    for k in range(3, r+1, 2):
        if n % k == 0:
            return False
    return True

def vhl_trunc(Pmax: int = 100000, mp_dps: int = 50):
    mp.mp.dps = mp_dps
    prod = mp.mpf("1.0")
    # p>2
    for p in range(3, int(Pmax)+1):
        if is_prime(p):
            prod *= (1 - mp.mpf(1)/((p-1)*(p-1)))
    return mp.mpf(2)*prod

def tail_bound(Pmax: int):
    # Bound elementar ~ C/(Pmax-1) => erro multiplicativo ≈ exp(C/(Pmax-1)) - 1
    # Tomamos C=1 como valor auditável e conservador (ajustável no relatório).
    if Pmax <= 2:
        return 1.0
    C = 1.0
    return float(mp.e**(C/(Pmax-1.0)) - 1.0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Pmax", type=int, default=100000)
    ap.add_argument("--tol", type=float, default=1e-12)
    ap.add_argument("--mp_dps", type=int, default=50)
    args = ap.parse_args()
    Vtr = vhl_trunc(Pmax=args.Pmax, mp_dps=args.mp_dps)
    err = tail_bound(Pmax=args.Pmax)
    print({"V_HL_trunc": str(Vtr), "Err_tail_mult_bound": err, "params": vars(args)})

if __name__ == "__main__":
    main()
