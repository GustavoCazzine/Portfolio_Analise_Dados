import requests

class ExtratorAPI:
    
    def __init__(self):
        self.dados_brutos = []

    def extrair_dados(self):

        itens_pulados = 0

        # 1. Criamos um crachá falso fingindo ser o Google Chrome
        cabecalhos = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        while True:
            link_produto = f'https://dummyjson.com/products?limit=30&skip={itens_pulados}'

            try:
                response = requests.get(link_produto, headers=cabecalhos)

                response.raise_for_status()

                dados_json = response.json()


                resultado = dados_json["products"]

                if len(resultado) == 0:
                    break

                self.dados_brutos.extend(resultado)

                
            except requests.exceptions.ConnectionError:
                print("Erro de conexão.")
                break
            except requests.exceptions.Timeout:
                print("Tempo limite atingido")
                break
            except requests.exceptions.HTTPError as e:
                print(f"Erro inesperado: {e}")
                break    
            except requests.exceptions.RequestException as e:
                print(f"Erro inesperado: {e}")
                break
            except ValueError:
                print("Resposta não é JSON válido")
                break
            except KeyError:
                print("Chave informada não existe")
                break
            except TypeError:
                print("Erro na lista")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}" )
                break
            finally:
                itens_pulados += 30

        return self.dados_brutos