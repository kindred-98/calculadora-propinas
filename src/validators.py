# validators.py

# src/validators.py

def validar_monto(monto: float) -> None:
    """
    Valida que el monto total sea un número positivo mayor que cero.

    Args:
        monto (float): Importe total de la cuenta.

    Raises:
        ValueError: Si el monto es menor o igual a cero.
    """
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero.")


def validar_porcentaje(porcentaje: float) -> None:
    """
    Valida que el porcentaje de propina no sea negativo.

    Args:
        porcentaje (float): Porcentaje de propina a aplicar.

    Raises:
        ValueError: Si el porcentaje es negativo.
    """
    if porcentaje < 0:
        raise ValueError("El porcentaje no puede ser negativo.")


def validar_propina_fija(propina: float) -> None:
    """
    Valida que la propina fija no sea negativa.

    Args:
        propina (float): Cantidad fija de propina.

    Raises:
        ValueError: Si la propina fija es negativa.
    """
    if propina < 0:
        raise ValueError("La propina fija no puede ser negativa.")


def validar_personas(personas: int) -> None:
    """
    Valida que el número de personas sea un entero positivo mayor que cero.

    Args:
        personas (int): Número de personas entre las que se divide la cuenta.

    Raises:
        ValueError: Si el número no es entero o es menor o igual a cero.
    """
    if not isinstance(personas, int):
        raise ValueError("El número de personas debe ser un entero.")

    if personas <= 0:
        raise ValueError("Debe haber al menos una persona.")