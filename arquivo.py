import json
import os

ARQUIVO_DADOS = "atendimentos.json"


def carregar_atendimentos():
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_atendimento(atendimento):
    dados = carregar_atendimentos()
    dados.append(atendimento)

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
