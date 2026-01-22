import json
from datetime import datetime, date
from periodo import obter_periodo_atual
from formatacao import normalizar_data

ARQUIVO = "atendimentos.json"

PONTOS = {
    "reparo": 1.73,
    "instalação": 2.37,
    "instalacao": 2.37
}


def carregar_dados():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def converter_data(data_str):
    data = normalizar_data(data_str)
    if not data:
        return None
    return datetime.strptime(data, "%d/%m/%y").date()


def calcular_pontos_periodo():
    dados = carregar_dados()
    inicio, fim = obter_periodo_atual()

    total = 0
    total_reparo = 0
    total_instalacao = 0

    for item in dados:
        data_atendimento = converter_data(item.get("data", ""))
        if not data_atendimento:
            continue

        tipo = item.get("tipo", "").lower()

        if inicio <= data_atendimento <= fim:
            pontos = PONTOS.get(tipo, 0)
            total += pontos

            if tipo == "reparo":
                total_reparo += pontos
            elif tipo in ["instalacao", "instalação"]:
                total_instalacao += pontos

    return total, total_reparo, total_instalacao
