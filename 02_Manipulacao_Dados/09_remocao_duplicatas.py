# Dia 9 - Remoção de duplicatas
import pandas as pd

df = pd.DataFrame({'A': [1, 1, 2], 'B': [3, 3, 4]})
print(df.drop_duplicates())
