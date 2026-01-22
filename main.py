from cadastro import cadastrar_atendimento
from arquivo import salvar_atendimento, carregar_atendimentos
from busca import buscar_atendimentos
from pontuacao import calcular_pontos_periodo
from periodo import obter_periodo_formatado
from datetime import datetime, date


def menu():
    print("\n" + "="*45)
    print(" SISTEMA DE CADASTRO DE ATENDIMENTOS ")
    print("="*45)
    print("1 - Cadastrar atendimento")
    print("2 - Buscar atendimento")
    print("3 - Ver pontuação do período")
    print("4 - Ver prazos dos atendimentos (30 dias)")
    print("0 - Sair")
    print("="*45)


def opcao_cadastro():
    atendimento = cadastrar_atendimento()
    salvar_atendimento(atendimento)
    print("Registro salvo no banco.\n")


def opcao_busca():
    termo = input("\nDigite o que deseja buscar: ").strip()
    resultados = buscar_atendimentos(termo)

    if not resultados:
        print("\n❌ Nenhum resultado encontrado.")
        return

    print("\n🔎 RESULTADOS:\n")

    for i, item in enumerate(resultados, start=1):
        print(f"{i}) {item['data']} | {item['nome']} | {item['telefone']} | {item['tipo']}")
        print(f"   Endereço: {item['endereco']}")
        print(f"   MAC: {item.get('mac','')}")
        print(f"   Obs: {item.get('observacoes','')}")
        print(f"   Pontos: {item.get('pontos','')}")
        print("-"*45)


def opcao_pontuacao():
    total, reparos, instalacoes = calcular_pontos_periodo()
    periodo = obter_periodo_formatado()

    print("\n📊 PRODUÇÃO DO PERÍODO")
    print("Período:", periodo)
    print(f"Reparos: {reparos}")
    print(f"Instalações: {instalacoes}")
    print(f"Pontuação total: {total}")


def opcao_prazos():
    atendimentos = carregar_atendimentos()
    hoje = date.today()

    if not atendimentos:
        print("\nNenhum atendimento cadastrado.")
        return

    print("\n⏳ PRAZOS DOS ATENDIMENTOS (30 DIAS)\n")

    for a in atendimentos:
        data_atendimento = datetime.strptime(a["data"], "%d/%m/%y").date()
        dias_passados = (hoje - data_atendimento).days
        dias_restantes = 30 - dias_passados

        print(f"Cliente: {a['nome']}")
        print(f"Data: {a['data']}")

        if dias_passados < 0:
            print("Status: Data futura inválida")
        elif dias_passados >= 30:
            print(f"Dias passados: {dias_passados}")
            print("Status: ⚠ PRAZO VENCIDO")
        else:
            print(f"Dias passados: {dias_passados}")
            print(f"Faltam: {dias_restantes} dias")
            print("Status: Dentro do prazo")

        print("-"*45)


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            opcao_cadastro()

        elif opcao == "2":
            opcao_busca()

        elif opcao == "3":
            opcao_pontuacao()

        elif opcao == "4":
            opcao_prazos()

        elif opcao == "0":
            print("\nEncerrando sistema... Até mais 👋")
            break

        else:
            print("\n⚠ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
