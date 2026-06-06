import pandas as pd
import sqlite3

conn = sqlite3.connect("banco_logistica.db")

cursor = conn.cursor()

df_lido = pd.read_sql("SELECT * FROM coordenadas_rotas", conn)

print(df_lido)

conn.close()