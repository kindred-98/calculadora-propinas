# services.py

from .validators import (
    validar_monto,
    validar_porcentaje,
    validar_propina_fija,
    validar_personas
)

def calcular_propina_porcentaje(monto, porcentaje):
    validar_monto(monto)
    validar_porcentaje(porcentaje)
    return round(monto * (porcentaje / 100), 2)


def calcular_propina_fija(monto, propina_fija):
    validar_monto(monto)
    validar_propina_fija(propina_fija)
    return round(propina_fija, 2)


def calcular_propina(monto, tipo, valor):
    if tipo == "porcentaje":
        return calcular_propina_porcentaje(monto, valor)
    elif tipo == "fija":
        return calcular_propina_fija(monto, valor)
    else:
        raise ValueError("Tipo de propina inválido.")


def dividir_cuenta(monto, tipo, valor, personas):
    validar_personas(personas)

    propina = calcular_propina(monto, tipo, valor)
    total = round(monto + propina, 2)
    por_persona = round(total / personas, 2)

    return {
        "propina": propina,
        "total": total,
        "por_persona": por_persona
    }