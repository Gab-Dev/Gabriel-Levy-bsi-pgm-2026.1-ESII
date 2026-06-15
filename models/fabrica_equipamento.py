from models.equipamento import (
    Notebook,
    Projetor,
    Cabo
)


class FabricaEquipamento:

    @staticmethod
    def criar(tipo, id, nome):

        if tipo == "notebook":
            return Notebook(id, nome, tipo)

        elif tipo == "projetor":
            return Projetor(id, nome, tipo)

        elif tipo == "cabo":
            return Cabo(id, nome, tipo)

        raise ValueError(
            f"Tipo desconhecido: {tipo}"
        )