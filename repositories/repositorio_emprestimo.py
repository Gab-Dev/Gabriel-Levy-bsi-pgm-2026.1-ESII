from models.equipamento import (
    Notebook,
    Projetor
)

from datetime import date


class RepositorioEmprestimo:

    def __init__(self):

        self.equipamentos = [

            Notebook(
                1,
                "Notebook Dell",
                "notebook"
            ),

            Projetor(
                2,
                "Projetor Epson",
                "projetor"
            )
        ]

        self.emprestimos = []


    def buscar_equipamento(self, equip_id):

        for equipamento in self.equipamentos:

            if equipamento.id == equip_id:
                return equipamento

        return None


    def salvar_emprestimo(self, emprestimo):

        self.emprestimos.append(
            emprestimo
        )


    def buscar_emprestimo(self, emprestimo_id):

        for emprestimo in self.emprestimos:

            if emprestimo.id == emprestimo_id:
                return emprestimo

        return None


    def finalizar_emprestimo(self, emprestimo_id):

        emprestimo = self.buscar_emprestimo(
            emprestimo_id
        )

        if emprestimo:
            self.emprestimos.remove(
                emprestimo
            )


    def marcar_indisponivel(self, equip_id):

        equipamento = self.buscar_equipamento(
            equip_id
        )

        if equipamento:
            equipamento.disponivel = False


    def marcar_disponivel(self, equip_id):

        equipamento = self.buscar_equipamento(
            equip_id
        )

        if equipamento:
            equipamento.disponivel = True


    def contar_emprestimos_abertos(self, email):

        total = 0

        for emprestimo in self.emprestimos:

            if emprestimo.email == email:
                total += 1

        return total


    def buscar_atrasados(self):

        atrasados = []

        for emprestimo in self.emprestimos:

            if emprestimo.data_devolucao < date.today():

                atrasados.append(
                    emprestimo
                )

        return atrasados