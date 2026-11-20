"""Trabalho Prático | DGT2823

Execute a partir da pasta scripts/: python trabalho_pratico.py
"""

# ----------------------------------------------------------------------
# Trabalho Prático | DGT2823 Tecnologias para desenv. de soluções de big data
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# 1. Leitura do CSV
# ----------------------------------------------------------------------

import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 9999)

CAMINHO_CSV = '../dados/dados.csv'

dados_originais = pd.read_csv(CAMINHO_CSV, sep=';', engine='python', encoding='utf-8')

# ----------------------------------------------------------------------
# 2. Verificação da importação
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Informações gerais
# ----------------------------------------------------------------------

dados_originais.info()

# ----------------------------------------------------------------------
# Primeiras e últimas N linhas
# ----------------------------------------------------------------------

N = 5

print(f'Primeiras {N} linhas:')
print(dados_originais.head(N))

print(f'Últimas {N} linhas:')
print(dados_originais.tail(N))

# ----------------------------------------------------------------------
# 3. Cópia do conjunto original
# ----------------------------------------------------------------------

dados = dados_originais.copy()

# ----------------------------------------------------------------------
# 4. Valores nulos da coluna `Calories` substituídos por 0
# ----------------------------------------------------------------------

dados['Calories'] = dados['Calories'].fillna(0)

print(dados.to_string())

# ----------------------------------------------------------------------
# 5. Valores nulos da coluna `Date` substituídos por `1900/01/01`
# ----------------------------------------------------------------------

dados['Date'] = dados['Date'].fillna('1900/01/01')

print(dados.to_string())

# ----------------------------------------------------------------------
# 6. Primeira tentativa de converter `Date` para datetime
# ----------------------------------------------------------------------

try:
    pd.to_datetime(dados['Date'])
except ValueError as erro:
    print('Erro:', erro)

# ----------------------------------------------------------------------
# 7. Correção: `1900/01/01` substituído por `NaN` e nova conversão
# ----------------------------------------------------------------------

dados['Date'] = dados['Date'].replace('1900/01/01', np.nan)

print(dados.to_string())

try:
    pd.to_datetime(dados['Date'])
except ValueError as erro:
    print('Erro:', erro)

# ----------------------------------------------------------------------
# 8. Correção do valor `20201226` combinando `replace` e `to_datetime`
# ----------------------------------------------------------------------

dados['Date'] = dados['Date'].replace(
    '20201226', pd.to_datetime('20201226', format='%Y%m%d')
)

print('Linha 26:', dados.loc[26, 'Date'])

# ----------------------------------------------------------------------
# 9. Conversão de toda a coluna `Date` para datetime
# ----------------------------------------------------------------------

dados['Date'] = pd.to_datetime(dados['Date'], format="'%Y/%m/%d'")

print(dados.to_string())

print(dados.dtypes)

# ----------------------------------------------------------------------
# 10. Remoção dos registros com valores nulos
# ----------------------------------------------------------------------

print('Nulos antes da remoção:')
print(dados.isnull().sum())

dados = dados.dropna(subset=['Date'])

# ----------------------------------------------------------------------
# 11. Resultado final
# ----------------------------------------------------------------------

print(dados.to_string())

dados.info()
