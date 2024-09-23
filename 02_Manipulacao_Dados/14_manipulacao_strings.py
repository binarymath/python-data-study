# Dia 14 - Manipulação de strings em DataFrames
import pandas as pd

df = pd.DataFrame({'A': ['abc', 'def', 'ghi']})
print(df['A'].str.upper())
