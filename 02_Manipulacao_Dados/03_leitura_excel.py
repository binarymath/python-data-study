# Dia 3 - Leitura de arquivos Excel com Pandas
"""Leitura de arquivos Excel com Pandas."""
import pandas as pd

df = pd.read_excel('exemplo.xlsx')
print(df.head())
