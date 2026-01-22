from datetime import datetime


def converter_data(data_texto):
    return datetime.strptime(data_texto, "%d/%m/%y")


def calcular_dias_passados(data_atendimento):
    data_at = converter_data(data_atendimento)
    hoje = datetime.today()
    return (hoje - data_at).days


def calcular_dias_restantes(data_atendimento, limite=30):
    dias_passados = calcular_dias_passados(data_atendimento)
    restantes = limite - dias_passados
    return restantes
