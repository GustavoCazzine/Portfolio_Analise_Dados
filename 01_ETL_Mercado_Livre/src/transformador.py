import requests
import pandas as pd
import sqlite3

class TransformardorDados:
    def __init__(self, dados_brutos):
        self.dados_brutos = dados_brutos


    def transformar_e_salvar(self):
        dados_limpos = []
        resultados = self.dados_brutos

        for anuncio in resultados:
                    titulo = anuncio["title"]
                    preco = anuncio["price"]

                    dados_limpos.append({"Produto" : titulo, "Preço" : preco})

        df = pd.DataFrame(dados_limpos)

        # 1. Força a conversão para número e transforma lixo em NaN
        df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')
        # 2. Deleta as linhas onde o preço ficou vazio (NaN)
        df = df.dropna(subset=['Preço'])
        # 3. Remove produtos com nomes exatamente iguais
        df = df.drop_duplicates(subset=['Produto'])

        conexao = sqlite3.connect('banco_produtos.db')
        cursor = conexao.cursor()
        df.to_sql("tabela_produtos", conexao, if_exists="replace", index=False)
        conexao.close()
        print("Dados limpos e salvos no Banco SQL com sucesso!")