# src/menu.py

from .services import dividir_cuenta
from .utils import formatear_moneda


def iniciar_cli() -> None:
    """
    Inicia el modo de ejecución en terminal (CLI).

    Muestra un menú interactivo que permite al usuario:
    - Calcular una propina.
    - Salir del programa.
    """
    while True:
        print("\n--- MODO TERMINAL ---")
        print("1. Calcular")
        print("2. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            ejecutar_calculo()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def ejecutar_calculo() -> None:
    """
    Solicita datos al usuario, realiza el cálculo de la propina
    y muestra los resultados formateados en consola.

    Captura y maneja errores producidos por:
    - Conversión de tipos (ValueError).
    - Validaciones del sistema.
    """
    try:
        monto = float(input("Monto: ").strip())

        print("1. Porcentaje")
        print("2. Fija")
        tipo_op = input("Tipo: ").strip()

        if tipo_op == "1":
            tipo = "porcentaje"
            valor = float(input("Porcentaje: ").strip())

        elif tipo_op == "2":
            tipo = "fija"
            valor = float(input("Propina fija: ").strip())

        else:
            print("Tipo inválido.")
            return

        personas = int(input("Personas: ").strip())

        resultado = dividir_cuenta(monto, tipo, valor, personas)

        print("\nResultados:")
        print("Propina:", formatear_moneda(resultado["propina"]))
        print("Total:", formatear_moneda(resultado["total"]))
        print("Por persona:", formatear_moneda(resultado["por_persona"]))

    except ValueError as e:
        print("Error de entrada:", e)

    except Exception as e:
        print("Error inesperado:", e)