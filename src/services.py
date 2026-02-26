# src/services.py

from .validators import (
    validar_monto,
    validar_porcentaje,
    validar_propina_fija,
    validar_personas
)


def calcular_propina_porcentaje(monto: float, porcentaje: float) -> float:
    """
    Calcula la propina basada en un porcentaje del monto total.

    Args:
        monto (float): Importe total de la cuenta.
        porcentaje (float): Porcentaje de propina a aplicar.

    Returns:
        float: Monto de la propina calculada, redondeada a 2 decimales.
    """
    validar_monto(monto)
    validar_porcentaje(porcentaje)

    propina = monto * (porcentaje / 100)
    return round(propina, 2)


def calcular_propina_fija(monto: float, propina_fija: float) -> float:
    """
    Devuelve una propina fija validada.

    Args:
        monto (float): Importe total de la cuenta.
        propina_fija (float): Cantidad fija de propina.

    Returns:
        float: Monto de la propina fija redondeada a 2 decimales.
    """
    validar_monto(monto)
    validar_propina_fija(propina_fija)

    return round(propina_fija, 2)


def calcular_propina(monto: float, tipo: str, valor: float) -> float:
    """
    Determina el tipo de propina (porcentaje o fija) y la calcula.

    Args:
        monto (float): Importe total de la cuenta.
        tipo (str): Tipo de propina ('porcentaje' o 'fija').
        valor (float): Valor correspondiente al tipo de propina.

    Returns:
        float: Monto de la propina calculada.

    Raises:
        ValueError: Si el tipo de propina no es válido.
    """
    if tipo == "porcentaje":
        return calcular_propina_porcentaje(monto, valor)

    if tipo == "fija":
        return calcular_propina_fija(monto, valor)

    raise ValueError("Tipo de propina inválido. Debe ser 'porcentaje' o 'fija'.")


def dividir_cuenta(monto: float, tipo: str, valor: float, personas: int) -> dict:
    """
    Calcula la propina, el total final y cuánto debe pagar cada persona.

    Args:
        monto (float): Importe total de la cuenta.
        tipo (str): Tipo de propina ('porcentaje' o 'fija').
        valor (float): Valor correspondiente al tipo de propina.
        personas (int): Número de personas para dividir la cuenta.

    Returns:
        dict: Diccionario con:
            - 'propina': Monto de la propina.
            - 'total': Total final incluyendo propina.
            - 'por_persona': Importe que debe pagar cada persona.
    """
    validar_monto(monto)
    validar_personas(personas)

    propina = calcular_propina(monto, tipo, valor)
    total = round(monto + propina, 2)
    por_persona = round(total / personas, 2)

    return {
        "propina": propina,
        "total": total,
        "por_persona": por_persona
    }