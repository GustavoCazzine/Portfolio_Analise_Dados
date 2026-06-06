from extrator import ExtratorAPI
from transformador import TransformardorDados

ex = ExtratorAPI()

dados = ex.extrair_dados()

tr = TransformardorDados(dados)

tr.transformar_e_salvar()