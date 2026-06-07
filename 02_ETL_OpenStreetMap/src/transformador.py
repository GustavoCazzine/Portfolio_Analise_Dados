import pandas as pd
import sqlite3

class TransformarDados:

    def __init__(self, dados_brutos):
        self.dados_brutos = dados_brutos
        self.dados_limpos = []

    def transformar_dados(self):

        resultados = self.dados_brutos

        for resultado in resultados:
            display_name = resultado['display_name']
            latitude = float(resultado['lat'])
            longitude = float(resultado['lon'])
            
            self.dados_limpos.append({"Display_Name" : display_name, "Latitude" : latitude, "Longitude" : longitude})

    def retornar_dados(self):
        return self.dados_limpos

    def salvar_db(self):

        df = pd.DataFrame(self.dados_limpos)

        df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
        df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")



        conn = sqlite3.connect("banco_logistica.db")
        cursor = conn.cursor()

        df.to_sql("coordenadas_rotas", conn, if_exists="replace", index=False)

        conn.close()

        print("Informações salvas com sucesso no DB")