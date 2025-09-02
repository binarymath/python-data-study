# Dia 7 - Ordenação de dados
"""Ordenação de dados."""
import pandas as pd

df = pd.DataFrame({'A': [3, 1, 2], 'B': [6, 4, 5]})
ordenado = df.sort_values('A')
print(ordenado)
