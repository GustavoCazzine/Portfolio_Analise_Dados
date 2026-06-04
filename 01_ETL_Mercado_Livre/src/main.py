import requests
import pandas as pd

class ExtratorMercadoLivre:
    def __init__(self, produto):
        self.produto = produto
        self.dados_limpos = []


    def extrair_dados(self):
        link_produto = f'https://dummyjson.com/products/search?q={self.produto}'

        # 1. Criamos um crachá falso fingindo ser o Google Chrome
        cabecalhos = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        try:
            response = requests.get(link_produto, headers=cabecalhos)

            response.raise_for_status()

            dados_json = response.json()

            resultados = dados_json["products"]

            for anuncio in resultados:
                titulo = anuncio["title"]
                preco = anuncio["price"]

                self.dados_limpos.append({"Produto" : titulo, "Preço" : preco})

        except requests.exceptions.ConnectionError:
            print("Erro de conexão.")
            
        except requests.exceptions.Timeout:
            print("Tempo limite atingido")
            
        except requests.exceptions.HTTPError as e:
            print(f"Erro inesperado: {e}")

        except requests.exceptions.RequestException as e:
            print(f"Erro inesperado: {e}")
            
        except ValueError:
            print("Resposta não é JSON válido")

        except KeyError:
            print("Chave informada não existe")

        except TypeError:
            print("Erro na lista")
    
        except Exception as e:
            print(f"Erro inesperado: {e}" )

    def transformar_e_salvar(self):
        df = pd.DataFrame(self.dados_limpos)

        caminho_arquivo = f"data/processed/{self.produto}_preco.csv"

        df.to_csv(caminho_arquivo, index=False)

        print("Arquivo salvo com sucesso!")




extrator = ExtratorMercadoLivre("laptop")

extrator.extrair_dados()

extrator.transformar_e_salvar()