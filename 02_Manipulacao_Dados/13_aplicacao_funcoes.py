# Dia 13 - Aplicação de funções em DataFrames
"""Aplicação de funções em DataFrames."""
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})
print(df['A'].apply(lambda x: x * 2))
