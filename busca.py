def buscar(atendimentos, termo):
    termo = termo.lower()
    resultados = []

    for a in atendimentos:
        for valor in a.values():
            if termo in str(valor).lower():
                resultados.append(a)
                break

    return resultados
