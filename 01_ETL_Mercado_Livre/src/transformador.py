import requests
import pandas as pd

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

        caminho_arquivo = f"data/processed/extrator_produtos.csv"
        df.to_csv(caminho_arquivo, index=False)
        print("Arquivo salvo e limpo com sucesso!")