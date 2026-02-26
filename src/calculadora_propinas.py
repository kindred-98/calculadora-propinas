# Archivo principal de la calculadora de propinas

# Archivo principal de la calculadora de propinas

def validar_monto(monto):
    if monto <= 0:
        raise ValueError("El monto debe ser un número positivo.")


def validar_porcentaje(porcentaje):
    if porcentaje < 0:
        raise ValueError("El porcentaje debe ser positivo.")


def validar_personas(personas):
    if personas <= 0 or not isinstance(personas, int):
        raise ValueError("El número de personas debe ser un entero positivo.")

#Formatea un número como moneda con dos decimales.
def formatear_moneda(valor): 
    return f"${valor:.2f}"

def calcular_propina_porcentaje(monto, porcentaje):
    validar_monto(monto)
    validar_porcentaje(porcentaje)
    return round(monto * (porcentaje / 100), 2)


def dividir_cuenta(monto, porcentaje, personas):
    validar_monto(monto)
    validar_porcentaje(porcentaje)
    validar_personas(personas)

    propina = calcular_propina_porcentaje(monto, porcentaje)
    total = round(monto + propina, 2)
    por_persona = round(total / personas, 2)

    return {
        "propina": propina,
        "total": total,
        "por_persona": por_persona
    }


# Pruebas manuales para este commit
if __name__ == "__main__":
    try:
        monto = float(input("Introduce el monto: "))
        porcentaje = float(input("Introduce el porcentaje de propina: "))
        personas = int(input("Introduce el número de personas: "))

        resultado = dividir_cuenta(monto, porcentaje, personas)

        print("\nResultados:")
        print("Propina:", formatear_moneda(resultado["propina"]))
        print("Total:", formatear_moneda(resultado["total"]))
        print("Por persona:", formatear_moneda(resultado["por_persona"]))

    except ValueError as e:
        print("Error:", e)
