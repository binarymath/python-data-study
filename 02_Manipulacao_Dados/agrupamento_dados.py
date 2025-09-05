"""Agrupamento de dados."""
import pandas as pd

df = pd.DataFrame({'A': ['x', 'y', 'x'], 'B': [1, 2, 3]})
grupos = df.groupby('A').sum()
print(grupos)
