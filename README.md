# tesa-meda-twins

Repositório auditável para a implementação computacional do artigo: TESA/MEDA para primos gêmeos.

Estrutura:
- Certificação numérica de V_HL(2) via produto de Euler truncado, com controle de cauda.
- Discretização do operador de transferência T_X, renormalização de massa e testes de estabilidade.
- Espaços anisotrópicos à Gouëzel–Liverani, projeções Littlewood–Paley e quase-diagonalidade.
- Estimativa espectral periférica (alpha_0), TT* em minor arcs e IFBC em major arcs.
- Coerção TESA por tiles, forma de Dirichlet global e cálculo de lambda_* e delta.

Ambiente:
1) conda env create -f environment.yml
2) conda activate tesa-meda-twins
3) python -m pip install -r requirements.txt   # (opcional: redundante se usar conda)

Pipeline rápido:
- V_HL(2):        python -m src.vhl --Pmax 100000 --tol 1e-12
- Kernels:        python -m src.kernels --eta 0.02 --grid 2048
- Transfer:       python -m src.transfer --eta 0.02 --grid 2048
- Spectrum:       python -m src.spectrum --eta 0.02 --grid 2048 --maxiter 200
- TT*:            python -m src.ttstar --eta 0.02 --grid 2048
- IFBC (major):   python -m src.ifbc --eta 0.02 --Qmaj 5000
- Coercion:       python -m src.coercion --eta 0.02 --grid 2048
- Delta:          python -m src.delta --eta 0.02 --grid 2048

Testes:
- pytest -q

Dados:
- data/primes.cache (opcional): cache de primos e Λ(n).
- data/params.yaml: parâmetros globais (eta, grid, janelas...).

Geração do ZIP:
- Este script Colab já gera tesa-meda-twins.zip automaticamente.

Data de geração: 2025-11-01T19:29:13.454434Z
