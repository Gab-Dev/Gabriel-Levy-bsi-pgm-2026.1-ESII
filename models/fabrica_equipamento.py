from models.equipamento import (
    Notebook,
    Projetor,
    Camera
)

from models.multa_strategy import (
    MultaPorDia
)


class FabricaEquipamento:

    @staticmethod
    def criar(tipo, id, nome):

        if tipo == "notebook":
            return Notebook(
                id,
                nome,
                tipo,
                MultaPorDia(10)
            )

        if tipo == "projetor":
            return Projetor(
                id,
                nome,
                tipo,
                MultaPorDia(5)
            )

        if tipo == "camera":
            return Camera(
                id,
                nome,
                tipo,
                MultaPorDia(7)
            )

        raise ValueError(
            f"Tipo inválido: {tipo}"
        )