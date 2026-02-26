# menu.py
from .services import dividir_cuenta
from .utils import formatear_moneda


def iniciar_cli():
    while True:
        print("\n--- MODO TERMINAL ---")
        print("1. Calcular")
        print("2. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            ejecutar_calculo()
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")


def ejecutar_calculo():
    try:
        monto = float(input("Monto: "))

        print("1. Porcentaje")
        print("2. Fija")
        tipo_op = input("Tipo: ")

        if tipo_op == "1":
            tipo = "porcentaje"
            valor = float(input("Porcentaje: "))
        elif tipo_op == "2":
            tipo = "fija"
            valor = float(input("Propina fija: "))
        else:
            print("Tipo inválido.")
            return

        personas = int(input("Personas: "))

        resultado = dividir_cuenta(monto, tipo, valor, personas)

        print("\nResultados:")
        print("Propina:", formatear_moneda(resultado["propina"]))
        print("Total:", formatear_moneda(resultado["total"]))
        print("Por persona:", formatear_moneda(resultado["por_persona"]))

    except Exception as e:
        print("Error:", e)