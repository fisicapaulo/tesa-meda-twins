# TESA MEDA Twins
Este repositório contém código e notebooks para estudo e experimentação de sistemas de transferência, observáveis e análise espectral relacionados à abordagem “TESA” (Transfer Operator, Espectro e Sistemas Anisotrópicos) e variações “MEDA Twins”. O projeto inclui implementações de kernels de transferência, testes de coerção, análise de lacuna espectral e exemplos em notebooks Jupyter.

## Conteúdo
- notebooks/: exemplos práticos
  - 01_vhl_certificacao.ipynb — Certificação V_HL (variação Hölder/Lipschitz) e preparação de dados
  - 02_transfer_kernel_tests.ipynb — Testes e visualizações de kernels de transferência
  - 03_spectrum_gap_alpha0.ipynb — Análise de lacuna espectral (gap) para α=0 (casos base)
  - 04_coercao_tesa_tiles.ipynb — Experimentos de coerção e “TESA tiles”
- src/: código-fonte das rotinas principais
  - anisobanach.py, coercion.py, delta.py, ifbc.py, kernels.py, observables.py, spectrum.py, transfer.py, ttstar.py, vhl.py
- tests/: testes unitários (pytest) para coercão, espectro e massa da transferência
- data/: parâmetros e caches auxiliares (params.yaml, primes.cache)
- environment.yml e requirements.txt: dependências para conda/pip
- README.md: este arquivo

## Instalação rápida
Opção conda (recomendado):
1) conda env create -f environment.yml
2) conda activate tesa-meda-twins

Opção pip:
1) python -m venv .venv
2) Ative a venv (Windows: .venv\Scripts\activate | Linux/Mac: source .venv/bin/activate)
3) pip install -r requirements.txt

## Uso básico
- Executar notebooks:
  - jupyter lab (ou jupyter notebook)
  - Abra os arquivos em notebooks/ e rode célula a célula
- Rodar testes:
  - pytest -q

## Estrutura conceitual (resumo)
- Operadores de transferência: modelagem da dinâmica estatística de sistemas; estudo de espectro, medidas invariantes e taxas de mistura
- Espaços anisotrópicos de Banach: framework para capturar regularidades diferentes em direções distintas
- Lacuna espectral (spectral gap): separação entre autovalor dominante e restante do espectro, indicando estabilidade e decaimento de correlações
- Observáveis e kernels: construção de observáveis e kernels para análises numéricas e certificações

## Dados e reprodutibilidade
- Parâmetros padrão em data/params.yaml
- Alguns resultados/cache em data/primes.cache
- Para reprodutibilidade, fixe versões via environment.yml ou requirements.txt

## Contribuição
- Issues e PRs são bem-vindos
- Padrão de código: PEP8
- Antes de abrir PR, rode: pytest -q

## Licença
MIT

## Contato
- Autor/Mantenedor: (Paulo vieira)
- GitHub: https://github.com/fisicapaulo/tesa-meda-twins
