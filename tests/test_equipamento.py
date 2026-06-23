import pytest

from models.fabrica_equipamento import (
    FabricaEquipamento
)


@pytest.mark.parametrize(
    "tipo,nome,dias,esperado",
    [
        ("notebook", "Dell", 2, 20),
        ("notebook", "Dell", 5, 50),

        ("projetor", "Epson", 2, 10),
        ("projetor", "Epson", 5, 25),

        ("camera", "Canon", 2, 14),
        ("camera", "Canon", 5, 35),
    ]
)
def test_calcular_multa_atraso_positivo(
    tipo,
    nome,
    dias,
    esperado
):

    equipamento = FabricaEquipamento.criar(
        tipo,
        1,
        nome
    )

    assert (
        equipamento.calcular_multa(dias)
        == esperado
    )


@pytest.mark.parametrize(
    "tipo,nome",
    [
        ("notebook", "Dell"),
        ("projetor", "Epson"),
        ("camera", "Canon"),
    ]
)
def test_calcular_multa_atraso_negativo_retorna_zero(
    tipo,
    nome
):

    equipamento = FabricaEquipamento.criar(
        tipo,
        1,
        nome
    )

    assert (
        equipamento.calcular_multa(-5)
        == 0
    )