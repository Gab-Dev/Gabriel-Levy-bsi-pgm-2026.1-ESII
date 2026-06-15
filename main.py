from app.sistema import SistemaDeEmprestimos


def main():

    sistema = SistemaDeEmprestimos()

    while True:

        print("\n1 - Registrar empréstimo")
        print("2 - Registrar devolução")
        print("3 - Listar atrasados")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            equip_id = int(input("ID equipamento: "))
            nome = input("Nome: ")
            email = input("Email: ")
            dias = int(input("Dias: "))

            resultado = sistema.registrar_emprestimo(
                equip_id,
                nome,
                email,
                dias
            )

            if resultado:
                print("Empréstimo registrado.")
            else:
                print("Erro ao registrar.")

        elif opcao == "2":

            emprestimo_id = int(
                input("ID empréstimo: ")
            )

            resultado = sistema.registrar_devolucao(
                emprestimo_id
            )

            if resultado:
                print("Devolução registrada.")
            else:
                print("Erro.")

        elif opcao == "3":

            atrasados = sistema.listar_atrasados()

            for emprestimo in atrasados:

                print(
                    emprestimo.nome_usuario,
                    emprestimo.equipamento.nome
                )

        elif opcao == "0":
            break


if __name__ == "__main__":
    main()