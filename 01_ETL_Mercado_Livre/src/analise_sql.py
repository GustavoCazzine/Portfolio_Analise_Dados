import pandas as pd
import sqlite3

conn = sqlite3.connect('banco_produtos.db')
cursor = conn.cursor()

df_lido = pd.read_sql("SELECT * FROM tabela_produtos ORDER BY 'Preço' DESC LIMIT 5", conn)

print(df_lido)

conn.close()