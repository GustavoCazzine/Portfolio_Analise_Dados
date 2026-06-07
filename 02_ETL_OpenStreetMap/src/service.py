from .extrator import ExtratorDados
from .transformador import TransformarDados
from .calculadora_rotas import calcular_distancia

class Service:


    def pegar_dados(self, cidade):
        extrator = ExtratorDados(cidade)
        return extrator.extrair_dados()

    def transformar_dados(self, dados_brutos_cidade):
        tr = TransformarDados(dados_brutos_cidade)
        tr.transformar_dados()
        return tr.retornar_dados()

    def calcular_distancia(self, lat1, lon1, lat2, lon2):
        resultado = calcular_distancia(lat1, lon1, lat2, lon2)

        return resultado