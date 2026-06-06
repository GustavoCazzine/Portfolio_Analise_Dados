from extrator import ExtratorDados
from transformador import TransformarDados

# 1. Definimos a rota
cidades = ["Piracicaba, SP", "Campinas, SP", "Limeira, SP", "Rio Claro, SP", "Americana, SP"]

# 2. Extraímos as coordenadas (lembrando do sleep de 1.5s lá dentro!)
ex = ExtratorDados(cidades)
dados = ex.extrair_dados()

# 3. Limpamos e enviamos para o banco SQL
tr = TransformarDados(dados)
tr.transformar_dados()
tr.salvar_db()