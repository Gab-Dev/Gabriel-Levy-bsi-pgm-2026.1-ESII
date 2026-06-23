from services.observer import Observer


class Notificador(Observer):

    def update(self, evento):

        if evento["tipo"] == "emprestimo":
            print(
                f"[EMAIL] Empréstimo registrado para {evento['email']}."
            )
            print(
                f"Devolução até: {evento['data_devolucao']}"
            )

        elif evento["tipo"] == "devolucao":
            print(
                f"[EMAIL] Devolução registrada para {evento['email']}."
            )

        elif evento["tipo"] == "atraso":
            print(
                f"[EMAIL] Empréstimo em atraso para {evento['email']}."
            )