from datetime import datetime


def formatar_telefone(telefone):
    # remove tudo que não for número
    numeros = ''.join(filter(str.isdigit, telefone))

    if len(numeros) != 11:
        return None

    ddd = numeros[:2]
    parte1 = numeros[2:7]
    parte2 = numeros[7:]

    return f"({ddd}) {parte1}-{parte2}"


def normalizar_data(data_texto):
    # remove tudo que não for número
    numeros = ''.join(filter(str.isdigit, data_texto))

    try:
        if len(numeros) == 6:  # 020225
            dia = numeros[:2]
            mes = numeros[2:4]
            ano = numeros[4:]
        elif len(numeros) == 8:  # 02022025
            dia = numeros[:2]
            mes = numeros[2:4]
            ano = numeros[6:]
        else:
            return None

        return f"{dia}/{mes}/{ano}"
    except:
        return None


def converter_para_data(data_formatada):
    return datetime.strptime(data_formatada, "%d/%m/%y")
