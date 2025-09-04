"""Leitura de arquivos Excel com Pandas."""
import os
import pandas as pd

# Cria um arquivo Excel de exemplo se não existir
if not os.path.exists('exemplo.xlsx'):
    df_exemplo = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df_exemplo.to_excel('exemplo.xlsx', index=False)

df = pd.read_excel('exemplo.xlsx')
print(df.head())
