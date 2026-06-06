# ⚙️ Pipeline ETL: Extração e Tratamento de Dados de E-commerce

Este projeto é um pipeline de dados (ETL - Extract, Transform, Load) construído em Python. O sistema consome dados de uma API pública, aplica regras de negócios e Data Cleaning, e carrega os resultados em um Banco de Dados Relacional local (SQLite).

## 🏗️ Arquitetura do Projeto

O código foi refatorado utilizando os princípios de **Responsabilidade Única (Clean Architecture)**, separando a lógica de requisição de rede da lógica de manipulação de dados:

* `src/extrator.py`: Motor responsável pela conexão com a API, contendo loops de paginação para lidar com limites de requisição e extração em massa.
* `src/transformador.py`: Cérebro da operação. Utiliza **Pandas** para varredura de valores nulos (NaN), tipagem rigorosa de colunas e remoção de duplicatas.
* `src/main.py`: O orquestrador que conecta o extrator ao transformador.
* `src/analise_sql.py`: Script de consumo analítico direto no banco de dados utilizando consultas SQL puras.

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Pandas** (Transformação e Data Cleaning)
* **Requests** (Consumo de APIs HTTP)
* **SQLite3** (Banco de Dados Relacional)
* **Matplotlib** (Visualização de Dados)
