# Dia 8 - Tratamento de valores nulos
"""Tratamento de valores nulos."""
import pandas as pd

df = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
print(df.fillna(0))
