from models.fabrica_equipamento import FabricaEquipamento
from models.emprestimo import Emprestimo


class RepositorioEmprestimo:

    def __init__(self):

        self.equipamentos = [

            FabricaEquipamento.criar(
                "notebook",
                1,
                "Notebook Dell"
            ),

            FabricaEquipamento.criar(
                "projetor",
                2,
                "Projetor Epson"
            ),

            FabricaEquipamento.criar(
                "camera",
                3,
                "Camera Canon"
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

    def buscar_atrasados(self):

        atrasados = []

        for emprestimo in self.emprestimos:

            if emprestimo.esta_atrasado():
                atrasados.append(
                    emprestimo
                )

        return atrasados