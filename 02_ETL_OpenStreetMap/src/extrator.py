import requests
import time

class ExtratorDados():

    def __init__(self, endereco):
        self.dados_brutos = []
        self.endereco = endereco

    def extrair_dados(self):
        

        cabecalho = {'User-Agent': 'Cazzine/1.0 (cazzinengustavo@gmail.com)'}

        link_api = f'https://nominatim.openstreetmap.org/search?q={self.endereco}&format=json'

        try:
            response = requests.get(link_api, headers=cabecalho)
        
            response.raise_for_status()

            dados_json = response.json()

            resultado = dados_json[0]

            self.dados_brutos.append(resultado)

            time.sleep(2)

        except requests.ConnectionError as e:
            print(f"Erro de conexão: {e}")
        except requests.HTTPError as e:
            print(f"Erro: {e}")
        except ValueError as e:
            print(f"Valor inválido: {e}")
        except TypeError as e:
            print(f"Tipo incorreto: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

        return self.dados_brutos