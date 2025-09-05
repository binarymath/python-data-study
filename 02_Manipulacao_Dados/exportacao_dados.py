"""Exportação de dados para CSV e Excel."""
import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df.to_csv('saida.csv', index=False)
df.to_excel('saida.xlsx', index=False)
print('Dados exportados!')
