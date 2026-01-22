from formatacao import formatar_telefone, normalizar_data


def obter_pontuacao(tipo):
    if tipo == "reparo":
        return 1.73
    elif tipo == "instalacao":
        return 2.37
    else:
        return 0


def cadastrar_atendimento():
    print("\n=== NOVO ATENDIMENTO ===")

    # Data
    while True:
        data_input = input("Data do atendimento: ")
        data = normalizar_data(data_input)
        if data:
            break
        print("Data inválida. Tente novamente.")

    # Nome
    nome = input("Nome do cliente: ").strip()

    # Endereço
    endereco = input("Endereço: ").strip()

    # Tipo
    while True:
        print("\nTipo de atendimento:")
        print("1 - Reparo")
        print("2 - Instalação")
        opcao = input("Escolha: ")

        if opcao == "1":
            tipo = "reparo"
            break
        elif opcao == "2":
            tipo = "instalacao"
            break
        else:
            print("Opção inválida.")

    # Telefone
    while True:
        telefone_input = input("Telefone: ")
        telefone = formatar_telefone(telefone_input)
        if telefone:
            break
        print("Telefone inválido.")

    # MAC FINAL
    mac = input("Final do MAC do equipamento: ").strip()

    # Observações
    obs = input("Observações: ").strip()

    # Pontuação automática
    pontos = obter_pontuacao(tipo)

    atendimento = {
        "data": data,
        "nome": nome,
        "endereco": endereco,
        "tipo": tipo,
        "telefone": telefone,
        "mac": mac,
        "observacoes": obs,
        "pontos": pontos
    }

    print("\n✅ Atendimento cadastrado com sucesso!\n")
    return atendimento
