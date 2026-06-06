# 🗺️ ETL de Geocodificação para Rotas Logísticas

Este projeto é um pipeline de dados (ETL - Extract, Transform, Load) focado em operações logísticas. O sistema converte lotes de endereços em texto bruto para coordenadas geográficas exatas (Latitude e Longitude), preparando a base de dados para cálculos de distâncias, auditoria de rotas e sistemas de roteirização de frotas.

## 🏗️ Arquitetura e Fluxo de Dados

O código foi construído seguindo os princípios de **Clean Architecture**, isolando responsabilidades para facilitar a manutenção e escalabilidade:

* `src/extrator.py`: Motor de extração conectado à API pública do OpenStreetMap (Nominatim). Implementa tratamento de requisições, envio de cabeçalhos de autenticação (User-Agent) e controle de **Rate Limiting** (`time.sleep`) para evitar banimento de IP em requisições em lote.
* `src/transformador.py`: Camada de processamento utilizando **Pandas**. Responsável por escavar os JSONs aninhados da API, isolar os dados de interesse e converter o formato de texto das coordenadas para decimais numéricos precisos (`pd.to_numeric`).
* `src/main.py`: O orquestrador central do pipeline.
* `src/analise_sql.py`: Script para consumo do banco de dados relacional via queries SQL.

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Pandas** (Transformação e Data Cleaning Matemático)
* **Requests** (Consumo de APIs e manipulação de Headers)
* **SQLite3** (Armazenamento em Banco de Dados Relacional local)
