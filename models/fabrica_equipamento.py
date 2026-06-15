from models.equipamento import (
    Notebook,
    Projetor,
    Camera
)


class FabricaEquipamento:

    @staticmethod
    def criar(tipo, id, nome):

        if tipo == "notebook":
            return Notebook(
                id,
                nome,
                tipo
            )

        if tipo == "projetor":
            return Projetor(
                id,
                nome,
                tipo
            )

        if tipo == "camera":
            return Camera(
                id,
                nome,
                tipo
            )

        raise ValueError(
            f"Tipo inválido: {tipo}"
        )