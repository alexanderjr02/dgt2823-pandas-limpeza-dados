# DGT2823 | Tecnologias para desenvolvimento de soluções de big data

Trabalho prático individual: leitura, inspeção e limpeza de um conjunto de dados com **Python** e **Pandas**.

## Estrutura

```
.
├── dados/
│   └── dados.csv                    conjunto de dados fornecido (separador ";")
├── notebooks/
│   ├── 01_microatividades.ipynb     microatividades 1 a 5, com saídas
│   └── 02_trabalho_pratico.ipynb    trabalho prático (limpeza dos dados), com saídas
├── scripts/
│   ├── microatividades.py           mesmo conteúdo do notebook 01 em script
│   └── trabalho_pratico.py          mesmo conteúdo do notebook 02 em script
└── requirements.txt
```

## Conjunto de dados

Colunas: `ID;Duration;Date;Pulse;Maxpulse;Calories` (32 registros).

| Linha | Coluna | Problema |
|---|---|---|
| 18 | Calories | valor nulo |
| 28 | Calories | valor nulo |
| 22 | Date | valor nulo |
| 26 | Date | data fora do padrão (`20201226`) |

## Microatividades

| Nº | Objetivo | Recurso do Pandas |
|---|---|---|
| 1 | Ler um arquivo CSV | `pd.read_csv(sep=';', engine='python', encoding='utf-8')` |
| 2 | Criar um subconjunto com 3 colunas | `df[['Duration', 'Pulse', 'Calories']]` |
| 3 | Configurar o máximo de linhas exibidas | `pd.set_option('display.max_rows', 9999)` e `to_string()` |
| 4 | Exibir as primeiras e últimas 10 linhas | `head(10)` e `tail(10)` |
| 5 | Exibir informações gerais do conjunto | `info()`, `shape`, `isnull().sum()`, `dtypes`, `memory_usage()` |

Resultado da microatividade 5: 32 linhas, 6 colunas, 3 valores nulos (1 em `Date`, 2 em `Calories`),
`Calories` como `float64`, `Date` como texto e as demais colunas como `int64`, ocupando cerca de 1.6 KB de memória.

## Trabalho prático: etapas da limpeza

1. Leitura do CSV em `dados_originais` e verificação com `info()`, `head()` e `tail()`.
2. Cópia do conjunto em `dados` com `copy()`, preservando o original.
3. Nulos de `Calories` substituídos por `0` com `fillna(0)`.
4. Nulos de `Date` substituídos por `'1900/01/01'` com `fillna()`.
5. Primeira conversão com `to_datetime`: erro, pois `1900/01/01` não corresponde ao formato `'%Y/%m/%d'`
   (as datas do arquivo vêm entre aspas simples).
6. `'1900/01/01'` substituído por `NaN` com `replace()` e nova conversão: erro, agora com o valor `20201226`.
7. Correção pontual da linha 26 combinando `replace()` e `to_datetime(format='%Y%m%d')`.
8. Conversão de toda a coluna `Date` para `datetime64` com `to_datetime`.
9. Remoção do registro com data nula (linha 22) com `dropna(subset=['Date'])`.

Resultado final: **31 registros, nenhum valor nulo e a coluna `Date` no tipo datetime.**

Os dois erros das etapas 5 e 6 são exibidos com `try/except`, para que o notebook rode do início ao fim.

## Como executar

```bash
pip install -r requirements.txt
```

Notebooks (JupyterLab):

```bash
jupyter lab
```

Abra os arquivos da pasta `notebooks/` e execute todas as células.

Scripts:

```bash
cd scripts
python microatividades.py
python trabalho_pratico.py
```
