# Dia 6 - Seleção de linhas em DataFrames
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.iloc[1])
