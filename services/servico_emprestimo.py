
    
    
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from models.emprestimo import Emprestimo

from datetime import date, timedelta


LIMITE_EMPRESTIMOS = 2


class ServicoEmprestimo:

    def __init__(self, repo=None, notificador=None):

        self.repo = repo or RepositorioEmprestimo()

        self.notificador = (
            notificador or Notificador()
        )


    def pode_realizar_emprestimo(self, email):

        total = self.repo.contar_emprestimos_abertos(
            email
        )

        return total < LIMITE_EMPRESTIMOS


    def registrar(self, equip_id, nome, email, dias):

        equipamento = self.repo.buscar_equipamento(
            equip_id
        )

        if not equipamento:
            return False

        if not equipamento.disponivel:
            return False

        if not self.pode_realizar_emprestimo(
            email
        ):
            return False

        data_devolucao = date.today() + timedelta(
            days=dias
        )

        emprestimo = Emprestimo(
            id=len(self.repo.emprestimos) + 1,
            equipamento=equipamento,
            nome_usuario=nome,
            email=email,
            data_devolucao=data_devolucao
        )

        self.repo.salvar_emprestimo(
            emprestimo
        )

        self.repo.marcar_indisponivel(
            equip_id
        )

        self.notificador.notificar_emprestimo(
            email,
            data_devolucao
        )

        return True


    def registrar_devolucao(self, emprestimo_id):

        emprestimo = self.repo.buscar_emprestimo(
            emprestimo_id
        )

        if not emprestimo:
            return False

        self.repo.marcar_disponivel(
            emprestimo.equipamento.id
        )

        self.repo.finalizar_emprestimo(
            emprestimo_id
        )

        self.notificador.notificar_devolucao(
            emprestimo.email
        )

        return True


    def listar_atrasados(self):

        atrasados = self.repo.buscar_atrasados()

        return atrasados