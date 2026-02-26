# main.py

import sys
import tkinter as tk

from src.menu import iniciar_cli
from src.gui import TipCalculatorGUI


def iniciar_gui():
    root = tk.Tk()
    app = TipCalculatorGUI(root)
    root.mainloop()


def main():
    """
    Si el programa se ejecuta en modo interactivo (con consola),
    mostramos menú CLI.

    Si no hay consola (ejecutable windowed),
    abrimos directamente la GUI.
    """

    # 🔹 Si no existe stdin (caso exe windowed)
    if sys.stdin is None or not sys.stdin.isatty():
        iniciar_gui()
        return

    # 🔹 Si hay consola disponible → menú normal
    print("\n=== CALCULADORA DE PROPINA ===")
    print("1. Modo Terminal (CLI)")
    print("2. Modo Gráfico (GUI)")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        iniciar_cli()

    elif opcion == "2":
        iniciar_gui()

    elif opcion == "3":
        sys.exit()

    else:
        print("Opción inválida.")


if __name__ == "__main__":
    main()