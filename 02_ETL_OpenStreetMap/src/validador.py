import requests 

def validar_cidade(buscar_cidade):

    link_api = f'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    try:
        response = requests.get(link_api)
    
        response.raise_for_status()

        dados_json = response.json()

        for municipio in dados_json:
            if municipio['nome'].lower() == buscar_cidade.lower():
               return True
        
        return False
        

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
