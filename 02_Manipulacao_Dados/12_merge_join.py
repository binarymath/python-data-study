# Dia 12 - Merge e Join de DataFrames
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [1, 2], 'C': [5, 6]})
resultado = pd.merge(df1, df2, on='A')
print(resultado)
