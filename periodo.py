from datetime import datetime, date

# ---------------- PERÍODO DE PONTUAÇÃO ----------------

def obter_periodo_atual():
    hoje = date.today()

    if hoje.day >= 21:
        inicio = date(hoje.year, hoje.month, 21)

        if hoje.month == 12:
            fim = date(hoje.year + 1, 1, 20)
        else:
            fim = date(hoje.year, hoje.month + 1, 20)
    else:
        if hoje.month == 1:
            inicio = date(hoje.year - 1, 12, 21)
        else:
            inicio = date(hoje.year, hoje.month - 1, 21)

        fim = date(hoje.year, hoje.month, 20)

    return inicio, fim


def formatar_data(data):
    return data.strftime("%d/%m/%y")


def obter_periodo_formatado():
    inicio, fim = obter_periodo_atual()
    return f"{formatar_data(inicio)} até {formatar_data(fim)}"


# ---------------- PRAZOS DE 30 DIAS ----------------

def calcular_prazos(atendimentos):
    hoje = datetime.now()
    texto = ""

    for a in atendimentos:
        try:
            data = datetime.strptime(a["data"], "%d/%m/%y")
            dias = (hoje - data).days

            texto += f"{a['nome']} - {a['data']}\n"

            if dias >= 30:
                texto += "Status: PRAZO VENCIDO\n"
            else:
                faltam = 30 - dias
                texto += f"Faltam: {faltam} dias\n"

            texto += "-" * 30 + "\n"

        except:
            texto += f"{a.get('nome','')} - Data inválida\n"
            texto += "-" * 30 + "\n"

    return texto if texto else "Nenhum atendimento cadastrado."
