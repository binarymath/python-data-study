"""Leitura de arquivos Excel com Pandas."""
import os
import pandas as pd

# Caminho absoluto para o arquivo Excel no mesmo diretório deste script
BASE_DIR = os.path.dirname(__file__)
excel_path = os.path.join(BASE_DIR, 'exemplo.xlsx')

# Cria um arquivo Excel de exemplo se não existir
if not os.path.exists(excel_path):
    df_exemplo = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df_exemplo.to_excel(excel_path, index=False)

# Lê o arquivo Excel
try:
    df = pd.read_excel(excel_path)
    print(df.head())
except FileNotFoundError:
    print(f"Arquivo não encontrado: {excel_path}")
