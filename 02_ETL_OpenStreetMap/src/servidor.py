from .service import Service
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import math

app = FastAPI(title = "Motor de Roteirização Logística")
service = Service()


class RequisicaoRota(BaseModel):
    cidade_origem : str
    cidade_destino: str

@app.post("/calcular_rota")
async def root(requisicao: RequisicaoRota):

    cidade1 = service.pegar_dados(requisicao.cidade_origem)
    cidade2 = service.pegar_dados(requisicao.cidade_destino)

    dados_cid1 = service.transformar_dados(cidade1)
    dados_cid2 = service.transformar_dados(cidade2)

    # Lendo do índice [0] da lista
    lat1 = dados_cid1[0]['Latitude']
    lon1 = dados_cid1[0]['Longitude']
    lat2 = dados_cid2[0]['Latitude']
    lon2 = dados_cid2[0]['Longitude']

    distancia = service.calcular_distancia(lat1, lon1, lat2, lon2)

    return {
        "status": "sucesso",
        "origem_valida": dados_cid1[0]['Display_Name'],
        "destino_valido": dados_cid2[0]['Display_Name'],
        "distancia_km": round(distancia, 2)
    }