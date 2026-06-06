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

        caminho_arquivo = f"data/processed/extrator_produtos.csv"

        df.to_csv(caminho_arquivo, index=False)

        print("Arquivo salvo com sucesso!")