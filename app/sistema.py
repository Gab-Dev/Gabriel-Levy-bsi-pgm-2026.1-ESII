from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from services.servico_emprestimo import ServicoEmprestimo


class SistemaDeEmprestimos:

    def __init__(self):

        repo = RepositorioEmprestimo()

        self.servico = ServicoEmprestimo(repo)

        self.servico.registrar_observer(
        Notificador()
        )

    def registrar_emprestimo(
        self,
        equip_id,
        nome,
        email,
        dias
    ):
        return self.servico.registrar(
            equip_id,
            nome,
            email,
            dias
        )

    def registrar_devolucao(
        self,
        emprestimo_id
    ):
        return self.servico.registrar_devolucao(
            emprestimo_id
        )

    def listar_atrasados(self):
        return self.servico.listar_atrasados()

    def calcular_multa(
        self,
        equip_id,
        dias_atraso
    ):
        return self.servico.calcular_multa(
            equip_id,
            dias_atraso
        )