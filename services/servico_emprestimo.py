from datetime import datetime, timedelta

from models.emprestimo import Emprestimo
from services.observer import Subject


class ServicoEmprestimo(Subject):

    def __init__(self, repo):
        super().__init__()
        self.repo = repo

    def registrar(self, email, exemplar):

        data_emprestimo = datetime.now().date()
        data_devolucao = data_emprestimo + timedelta(days=7)

        emprestimo = Emprestimo(
            email=email,
            exemplar=exemplar,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )

        self.repo.adicionar(emprestimo)

        self.notificar(
            {
                "tipo": "emprestimo",
                "email": email,
                "data_devolucao": data_devolucao
            }
        )

        return emprestimo

    def registrar_devolucao(self, emprestimo):

        emprestimo.registrar_devolucao()

        self.repo.atualizar(emprestimo)

        self.notificar(
            {
                "tipo": "devolucao",
                "email": emprestimo.email
            }
        )

    def listar_atrasados(self):

        atrasados = self.repo.buscar_atrasados()

        for emprestimo in atrasados:
            self.notificar(
                {
                    "tipo": "atraso",
                    "email": emprestimo.email
                }
            )

        return atrasados