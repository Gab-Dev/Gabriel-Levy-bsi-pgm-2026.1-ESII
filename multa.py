def calcular_multa_com_carencia(
    dias_atraso,
    valor_dia,
    carencia
):
    dias_cobrados = max(
        0,
        dias_atraso - carencia
    )

    multa = dias_cobrados * valor_dia

    return round(multa, 2)