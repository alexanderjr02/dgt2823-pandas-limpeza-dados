"""Microatividades 1 a 5 | DGT2823

Execute a partir da pasta scripts/: python microatividades.py
"""

# ----------------------------------------------------------------------
# Microatividades | DGT2823 Tecnologias para desenv. de soluções de big data
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Microatividade 1: ler um arquivo CSV
# ----------------------------------------------------------------------

import pandas as pd

CAMINHO_CSV = '../dados/dados.csv'

df = pd.read_csv(CAMINHO_CSV, sep=';', engine='python', encoding='utf-8')

print(df)

# ----------------------------------------------------------------------
# Microatividade 2: criar um subconjunto de dados
# ----------------------------------------------------------------------

subconjunto = df[['Duration', 'Pulse', 'Calories']]

print(subconjunto)

# ----------------------------------------------------------------------
# Microatividade 3: configurar o número máximo de linhas exibidas
# ----------------------------------------------------------------------

pd.set_option('display.max_rows', 9999)
print('display.max_rows =', pd.get_option('display.max_rows'))

print(df.to_string())

# ----------------------------------------------------------------------
# Microatividade 4: exibir as primeiras e as últimas N linhas
# ----------------------------------------------------------------------

print('Primeiras 10 linhas:')
print(df.head(10))

print('Últimas 10 linhas:')
print(df.tail(10))

# ----------------------------------------------------------------------
# Microatividade 5: informações gerais sobre colunas, linhas e dados
# ----------------------------------------------------------------------

df.info()

linhas, colunas = df.shape
print('Total de linhas:', linhas)
print('Total de colunas:', colunas)

print('\nQuantidade de dados nulos por coluna:')
print(df.isnull().sum())

print('\nTipo de dado de cada coluna:')
print(df.dtypes)

memoria = df.memory_usage(deep=False).sum()
print(f'\nMemória utilizada: {memoria} bytes ({memoria / 1024:.1f} KB)')
