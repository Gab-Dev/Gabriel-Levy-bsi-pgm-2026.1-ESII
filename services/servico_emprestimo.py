from models.emprestimo import Emprestimo

from datetime import date, timedelta


class ServicoEmprestimo:

    def __init__(self, repo, notificador):

        self.repo = repo
        self.notificador = notificador

    def registrar(self, equip_id, nome, email, dias):

        equipamento = self.repo.buscar_equipamento(equip_id)

        if not equipamento:
            return False

        if not equipamento.disponivel:
            return False

        data_devolucao = date.today() + timedelta(days=dias)

        emprestimo = Emprestimo(
            id=len(self.repo.emprestimos) + 1,
            equipamento=equipamento,
            nome_usuario=nome,
            email=email,
            data_devolucao=data_devolucao
        )

        self.repo.salvar_emprestimo(emprestimo)

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

    def calcular_multa(self, equip_id, dias_atraso):

        equipamento = self.repo.buscar_equipamento(
            equip_id
        )

        if not equipamento:
            return None

        multa = equipamento.calcular_multa(
            dias_atraso
        )

        return multa