# -*- coding: utf-8 -*-
from src.vhl import vhl_trunc

def test_vhl_monotone():
    V1 = vhl_trunc(Pmax=1000, mp_dps=40)
    V2 = vhl_trunc(Pmax=2000, mp_dps=40)
    assert float(V2) > 0 and abs(V2 - V1) < 0.05  # variação pequena ao dobrar corte
