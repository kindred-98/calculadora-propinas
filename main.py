import sys
import tkinter as tk

from src.menu import iniciar_cli
from src.gui import TipCalculatorGUI


def iniciar_gui() -> None:
    """
    Inicializa y ejecuta la interfaz gráfica (GUI).
    """
    root = tk.Tk()
    _app = TipCalculatorGUI(root)
    root.mainloop()


def hay_consola_disponible() -> bool:
    """
    Verifica si el programa se está ejecutando en una terminal real.

    Algunos entornos como VS Code pueden alterar el comportamiento
    de sys.stdin.isatty(), por eso hacemos la comprobación más segura.
    """
    try:
        return sys.stdin is not None and sys.stdin.isatty()
    except Exception:
        return False


def main() -> None:
    """
    Punto de entrada principal del programa.

    Comportamiento:
    - Si NO hay consola disponible (ejecutable windowed),
      se abre directamente la GUI.
    - Si hay consola disponible,
      se muestra el menú para elegir modo CLI o GUI.
    """

    # 🔹 Si no hay consola → abrir GUI directamente
    if not hay_consola_disponible():
        iniciar_gui()
        return

    # 🔹 Si hay consola → mostrar menú
    print("\n=== CALCULADORA DE PROPINA ===")
    print("1. Modo Terminal (CLI)")
    print("2. Modo Gráfico (GUI)")
    print("3. Salir")

    try:
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            iniciar_cli()

        elif opcion == "2":
            iniciar_gui()

        elif opcion == "3":
            sys.exit()

        else:
            print("Opción inválida.")

    except Exception as e:
        print("Ocurrió un error:", e)


if __name__ == "__main__":
    main()