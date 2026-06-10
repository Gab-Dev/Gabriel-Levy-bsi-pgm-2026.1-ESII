from multa import calcular_multa_com_carencia


def test_multa_zero_sem_atraso():

    resultado = calcular_multa_com_carencia(
        dias_atraso=0,
        valor_dia=10,
        carencia=2
    )

    assert resultado == 0.0


def test_multa_cobra_dias_apos_carencia():

    resultado = calcular_multa_com_carencia(
        dias_atraso=5,
        valor_dia=10,
        carencia=2
    )

    assert resultado == 30.0