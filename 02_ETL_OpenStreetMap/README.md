# 🗺️ API RESTful de Roteirização e Geocodificação Nacional

Este projeto evoluiu de um pipeline de extração em lote (ETL) para uma **API RESTful** de alta performance focada em logística. O sistema recebe pedidos de rotas em tempo real, valida a existência dos municípios na base de dados oficial do governo brasileiro, converte os endereços em coordenadas geográficas e calcula a distância exata em quilômetros utilizando trigonometria esférica.

## 🏗️ Padrão de Arquitetura (Controller-Service)

O backend foi estruturado utilizando o padrão **Controller-Service** para isolar as regras de negócio das rotas da API, garantindo escalabilidade e fácil manutenção para sistemas de auditoria e controle de frota:

* **`servidor.py` (Controller):** Ponto de entrada da API construído com **FastAPI**. Gerencia as requisições HTTP, define os modelos de dados esperados (Pydantic) e lida com o tratamento de erros (HTTP 400).
* **`service.py` (Service):** O cérebro orquestrador que conecta as camadas de extração, transformação, validação e matemática.
* **`extrator.py`:** Integração com a API do OpenStreetMap (Nominatim), com tratamento rigoroso de *Rate Limiting* para requisições externas.
* **`transformador.py`:** Camada de Data Cleaning utilizando **Pandas** para isolar chaves de JSONs aninhados e forçar a tipagem numérica das coordenadas.
* **`validador.py`:** Filtro de segurança integrado em tempo real à **API pública do IBGE** para garantir a integridade dos dados de origem e destino no território nacional.
* **`calculadora_rotas.py`:** Motor trigonométrico que aplica a **Fórmula de Haversine** (`math.radians`, `math.sin`, `math.cos`) para calcular distâncias considerando a curvatura da Terra.

## 🚀 Tecnologias e Bibliotecas

* **Python 3**
* **FastAPI & Uvicorn** (Criação do Servidor Web e Documentação Swagger)
* **Pandas** (Tratamento de Dados)
* **Requests** (Consumo de APIs de Terceiros e Governamentais)
* **Pydantic** (Validação de Tipos de Dados HTTP)
