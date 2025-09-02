# Dia 12 - Merge e Join de DataFrames
"""Leitura de arquivos CSV com Pandas."""
import pandas as pd

# Cria um arquivo CSV de exemplo se não existir
df_exemplo = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_exemplo.to_csv('exemplo.csv', index=False)

df = pd.read_csv('exemplo.csv')
print(df.head())
