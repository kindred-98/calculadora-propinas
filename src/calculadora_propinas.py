# ============================================================
# VALIDACIONES
# ============================================================

def validar_monto(monto):
    if monto <= 0:
        raise ValueError("El monto debe ser un número positivo.")


def validar_porcentaje(porcentaje):
    if porcentaje < 0:
        raise ValueError("El porcentaje debe ser positivo.")


def validar_propina_fija(propina):
    if propina < 0:
        raise ValueError("La propina fija debe ser un número positivo.")


def validar_personas(personas):
    if personas <= 0 or not isinstance(personas, int):
        raise ValueError("El número de personas debe ser un entero positivo.")


# ============================================================
# UTILIDADES
# ============================================================

def formatear_moneda(valor):
    """Formatea un número como moneda con dos decimales."""
    return f"${valor:.2f}"


# ============================================================
# CÁLCULO DE PROPINAS
# ============================================================

def calcular_propina_porcentaje(monto, porcentaje):
    validar_monto(monto)
    validar_porcentaje(porcentaje)
    return round(monto * (porcentaje / 100), 2)


def calcular_propina_fija(monto, propina_fija):
    validar_monto(monto)
    validar_propina_fija(propina_fija)
    return round(propina_fija, 2)


def calcular_propina(monto, tipo, valor):
    """
    Calcula la propina según el tipo:
    - tipo = "porcentaje": valor es el porcentaje
    - tipo = "fija": valor es el monto fijo
    """
    if tipo == "porcentaje":
        return calcular_propina_porcentaje(monto, valor)
    elif tipo == "fija":
        return calcular_propina_fija(monto, valor)  # ✔ CORREGIDO
    else:
        raise ValueError("Tipo de propina no válido. Usa 'porcentaje' o 'fija'.")


# ============================================================
# DIVISIÓN DE LA CUENTA
# ============================================================

def dividir_cuenta(monto, tipo_propina, valor_propina, personas):
    validar_monto(monto)
    validar_personas(personas)

    propina = calcular_propina(monto, tipo_propina, valor_propina)
    total = round(monto + propina, 2)
    por_persona = round(total / personas, 2)

    return {
        "propina": propina,
        "total": total,
        "por_persona": por_persona
    }


# ============================================================
# PRUEBAS MANUALES
# ============================================================

if __name__ == "__main__":
    try:
        monto = float(input("Introduce el monto: "))

        print("\nElige tipo de propina:")
        print("1. Porcentaje")
        print("2. Fija")

        opcion = input("Opción: ")

        if opcion == "1":
            tipo = "porcentaje"
            valor = float(input("Introduce el porcentaje: "))
        elif opcion == "2":
            tipo = "fija"
            valor = float(input("Introduce el monto fijo de propina: "))
        else:
            raise ValueError("Opción no válida.")

        personas = int(input("Introduce el número de personas: "))

        resultado = dividir_cuenta(monto, tipo, valor, personas)

        print("\nResultados:")
        print("Propina:", formatear_moneda(resultado["propina"]))
        print("Total:", formatear_moneda(resultado["total"]))
        print("Por persona:", formatear_moneda(resultado["por_persona"]))

    except ValueError as e:
        print("Error:", e)
