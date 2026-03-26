import tkinter as tk
from src.gui import TipCalculatorGUI
import traceback
import sys


def main():
    try:
        root = tk.Tk()
        TipCalculatorGUI(root)  # ✔ Eliminamos variable innecesaria
        root.mainloop()

    except Exception as e:
        # ✔ Usamos el error (importante para debugging real)
        with open("error_log.txt", "w") as f:
            f.write(traceback.format_exc())

        print("Error crítico:", str(e))  # ✔ ahora sí usamos 'e'
        sys.exit(1)


if __name__ == "__main__":
    main()