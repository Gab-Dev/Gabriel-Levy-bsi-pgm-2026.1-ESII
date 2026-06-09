import pytest

from models.equipamento import (
    Notebook,
    Projetor,
    Camera
)


@pytest.mark.parametrize(
    "equipamento,dias,esperado",
    [
        (Notebook(1, "Dell", "notebook"), 2, 20),
        (Notebook(1, "Dell", "notebook"), 5, 50),

        (Projetor(2, "Epson", "projetor"), 2, 10),
        (Projetor(2, "Epson", "projetor"), 5, 25),

        (Camera(3, "Canon", "camera"), 2, 14),
        (Camera(3, "Canon", "camera"), 5, 35),
    ]
)
def test_calcular_multa_atraso_positivo(
    equipamento,
    dias,
    esperado
):

    assert (
        equipamento.calcular_multa(dias)
        == esperado
    )


@pytest.mark.parametrize(
    "equipamento",
    [
        Notebook(1, "Dell", "notebook"),
        Projetor(2, "Epson", "projetor"),
        Camera(3, "Canon", "camera"),
    ]
)
def test_calcular_multa_atraso_negativo_retorna_zero(
    equipamento
):

    assert equipamento.calcular_multa(-5) == 0